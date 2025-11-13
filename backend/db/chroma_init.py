from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()


def init_chroma_store(persist_dir: str = "chroma_persist", collection_name: str = "default_collection"):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings,
        collection_name=collection_name
    )
    return vectordb


# Usage
vectordb = init_chroma_store()
