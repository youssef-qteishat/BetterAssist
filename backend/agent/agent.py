import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from db.chroma_init import init_chroma_store

# Load environment variables
load_dotenv()

# Read the API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables")

vectordb = init_chroma_store()

# Assume vectordb is your Chroma vector store instance initialized elsewhere
# e.g., vectordb = ingest_articulation_pdf("path/to/articulation_agreement.pdf")

def retrieve_articulation_info(query: str) -> str:
    results = vectordb.similarity_search(query, k=3)  # fetch top 3 relevant chunks
    combined_text = "\n\n".join([doc.page_content for doc in results])
    return combined_text or "No relevant information found."

tools = [
    Tool(
        name="ArticulationRetriever",
        func=retrieve_articulation_info,
        description="Use this tool to answer questions about articulation agreements and transfer plans."
    ),
]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=openai_api_key)
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="conversational-react-description",
    memory=memory,
    verbose=True,
)

# Example interactive test call:
question = "What courses do I need to transfer from Diablo College to UC Davis for Computer Science?"
response = agent.run(question)
print(response)
