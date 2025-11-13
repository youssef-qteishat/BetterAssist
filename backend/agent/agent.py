import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from db.chroma_init import vectordb

load_dotenv()

# Assume vectordb is your Chroma vector store instance initialized elsewhere
# e.g., vectordb = ingest_articulation_pdf("path/to/articulation_agreement.pdf")

def retrieve_articulation_info(query: str) -> str:
    results = vectordb.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in results]) or "No relevant information found."

tools = [
    Tool(
        name="ArticulationRetriever",
        func=retrieve_articulation_info,
        description="Use this tool to answer questions about articulation agreements and transfer plans."
    ),
]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=tools,
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
