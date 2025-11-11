import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool
from db.chroma_init import init_chroma_store
from langchain.agents import createAgent

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY")

# Initialize Chroma vector store
vectordb = init_chroma_store()

# Define your tool
@tool
def retrieve_articulation_info(query: str) -> str:
    results = vectordb.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in results]) or "No relevant information found."

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

# Create the agent using LangGraph style
system_message = "You are a helpful assistant that answers questions about articulation agreements."
agent = createAgent(
    llm=llm,
    tools=[retrieve_articulation_info],
    system_message=system_message,
    memory=memory
)

# Test the agent
if __name__ == "__main__":
    question = "What courses do I need to transfer from Diablo College to UC Davis for Computer Science?"
    response = agent(question)
    print(response)
