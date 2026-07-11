from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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


