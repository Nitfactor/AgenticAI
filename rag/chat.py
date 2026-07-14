from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


embeddings = OpenAIEmbeddings(
    model_name = "text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name = "bloomberg_terminal_guide",
    embedding = embeddings,
)

user_query = input("Query: ")

search_results = vector_db.similarity_search