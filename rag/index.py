from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "Bloomberg.pdf"

# Load this file in python program 
# PyPDFLoader
loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()
print(documents[2])

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Vector embedding for these chunks

embeddings = OpenAIEmbeddings(
    model_name = "text-embedding-3-large"
)

vectorstore = QdrantVectorStore(
    document_chunks = chunks,
    embedding = embeddings,
    url = "http://localhost:6333",
    collection_name = "bloomberg_terminal_guide"
)

print("Indexing documents done !")


