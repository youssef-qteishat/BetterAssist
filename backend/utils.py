import hashlib
from langchain_unstructured import UnstructuredLoader
from langchain.embeddings import OpenAIEmbeddings
from db.chroma_init import init_chroma_store

def compute_pdf_hash(pdf_path: str) -> str:
    """
    Compute SHA256 hash of PDF content for uniqueness checking.
    """
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    return hashlib.sha256(pdf_bytes).hexdigest()

def load_pdf_with_unstructured(pdf_path: str):
    """
    Load PDF document with UnstructuredLoader.
    """
    loader = UnstructuredFileLoader(
        pdf_path,
        chunking_strategy="basic",
        max_characters=1500,
        include_orig_elements=False
    )
    docs = loader.load()
    return docs

def embed_and_populate_chroma(chunks, document_id, collection_name, persist_directory="chroma_persist"):
    """
    Embed chunks using OpenAI and store them with Chroma vector DB.
    Use existing Chroma instance initialized from db/chroma_init.
    Add document_id metadata for duplicate prevention.
    """
    vectordb = init_chroma_store(persist_dir=persist_directory, collection_name=collection_name)

    # Check if document with this ID already exists to avoid duplicates
    existing = vectordb._collection.get(where={"document_id": document_id}, limit=1)
    if existing and len(existing["ids"]) > 0:
        print(f"Document with ID {document_id} already ingested; skipping.")
        return vectordb

    # Add metadata with document_id for all chunks
    metadatas = [{"source": f"chunk_{i}", "document_id": document_id} for i in range(len(chunks))]

    vectordb.add_documents(chunks, metadatas=metadatas)
    vectordb.persist()

    return vectordb

def ingest_articulation_pdf(pdf_path: str):
    """
    Full ingestion pipeline from PDF file to populated Chroma DB.
    Checks for duplicates before ingestion.
    """
    document_id = compute_pdf_hash(pdf_path)

    vectordb = init_chroma_store()

    # Check for existing document to short-circuit
    existing = vectordb._collection.get(where={"document_id": document_id}, limit=1)
    if existing and len(existing["ids"]) > 0:
        print(f"Document with ID {document_id} already exists in DB.")
        return vectordb

    chunked_doc = load_pdf_with_unstructured(pdf_path)
    vectordb = embed_and_populate_chroma(chunked_doc, document_id,"articulation_agreements")
    return vectordb

# # Example usage:
# vectordb = ingest_articulation_pdf("backend/DIABLO_to_UCD_for_2022-2023_by_Computer_Science_B.S.pdf")
