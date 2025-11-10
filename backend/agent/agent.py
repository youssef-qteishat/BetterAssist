from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

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

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
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
