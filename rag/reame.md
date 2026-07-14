RAG (Retrieval-Augmented Generation) Project
A Python-based Retrieval-Augmented Generation system that indexes PDF documents and enables intelligent querying using LangChain, OpenAI embeddings, and Qdrant vector database.

Overview
This project demonstrates a complete RAG pipeline that:

Loads and processes PDF documents
Splits documents into manageable chunks
Generates embeddings using OpenAI's embedding models
Stores embeddings in a Qdrant vector database
Retrieves relevant content based on user queries
Generates contextual responses using OpenAI's GPT models


## Components

### `index.py`
Handles document preparation and indexing:
- Loads PDF files using `PyPDFLoader`
- Splits documents into chunks (1000 characters with 200-character overlap)
- Generates embeddings using OpenAI's `text-embedding-3-large` model
- Stores chunks in Qdrant vector database under the collection `bloomberg_terminal_guide`

### `chat.py`
Provides the query interface:
- Accepts user queries
- Performs similarity search in the vector database
- Constructs a system prompt with retrieved context and page numbers
- Generates responses using GPT with the relevant document context

### `docker-compose.yml`
Sets up the Qdrant vector database service:
- Runs Qdrant on port 6333
- Provides a persistent vector store for document embeddings

PDF Document
    ↓
PyPDFLoader (index.py)
    ↓
RecursiveCharacterTextSplitter
    ↓
OpenAI Embeddings (text-embedding-3-large)
    ↓
Qdrant Vector Store
    ↓
User Query
    ↓
Similarity Search (chat.py)
    ↓
GPT Response with Context
    ↓
Output to User

