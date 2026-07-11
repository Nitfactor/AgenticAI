from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "Bloomberg.pdf"

# Load this file in python program 
# PyPDFLoader
loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()
print(documents[2])
