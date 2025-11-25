# intelligent-pdf-qa-system
A modular, FastAPI-ready RAG system for intelligent PDF question-answering. Built with LangChain, OpenAI embeddings, ChromaDB, and a scalable OOP pipeline architecture.

---

## Overview

The Intelligent PDF Q&A System extracts text from PDFs, generates embeddings, stores them in a vector database, retrieves relevant context based on a user query, and uses an LLM to generate accurate answers. The project is developed with production readiness in mind, including separation of concerns, clear module boundaries, and clean extensibility.

The system supports:

- PDF ingestion and text extraction  
- Chunking and preprocessing  
- Embedding generation  
- Vector storage using ChromaDB  
- Context retrieval for queries  
- LLM-based answer generation  
- A structure prepared for FastAPI integration  
- Fully modular OOP components  

---

## Architecture

Pipeline flow:
PDFLoader → TextChunker → Embedder → VectorStore → Retriever → AnswerGenerator
This pipeline is wrapped inside a unified `PDFQAPipeline` class for easy orchestration in both CLI and API modes.

---

## Project Structure
intelligent-pdf-qa-system/
│
├── app/
│ ├── main.py
│ ├── routers/
│ ├── services/
│ └── schemas/
│
├── core/
│ ├── loader.py
│ ├── chunker.py
│ ├── embedder.py
│ ├── vector_store.py
│ ├── retriever.py
│ ├── generator.py
│ └── pipeline.py
│
├── config/
│ └── settings.py
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── vectorstore/
│
├── scripts/
│ ├── build_vectorstore.py
│ └── query.py
│
├── utils/
│ ├── logger.py
│ └── file_utils.py
│
└── tests/

---

## Key Features

- Clean modular architecture using Python OOP  
- PDF extraction support with PyPDF2 / pdfplumber  
- Configurable text chunking optimized for semantic search  
- Embedding generation using OpenAI or alternative models  
- Vector storage and similarity search via ChromaDB  
- Retrieval-Augmented Generation (RAG) to improve LLM accuracy  
- FastAPI-ready folder structure for future deployment  
- Local CLI scripts for vectorstore creation and querying  
- Unit testing support for all core modules  

---

## Installation

1. Clone the repository:

git clone https://github.com/<your-username>/intelligent-pdf-qa-system.git
cd intelligent-pdf-qa-system

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Create a .env file:
OPENAI_API_KEY=your_api_key
EMBEDDING_MODEL=text-embedding-3-large
LLM_MODEL=gpt-4.1-mini

## Usage (Local CLI)
Build the vectorstore from a PDF:
python scripts/build_vectorstore.py --pdf data/raw/sample.pdf

## Query the processed document:
python scripts/query.py "What does section 2 describe?"

# FastAPI Usage (Phase 2)

## Start the API server:
uvicorn app.main:app --reload

## Planned endpoints:
Method	Endpoint	    Description
POST	/upload-pdf	    Upload and process PDF
POST	/ask	        Ask a question
GET	    /health	        Health check

## Technologies Used
Python 3.10+
LangChain
ChromaDB
OpenAI embeddings and LLMs
FastAPI (Phase 2)
PyPDF2 / pdfplumber
dotenv
Pydantic

## Testing
Run unit tests:
pytest

# Roadmap
## Phase 1 (Current)
Core RAG pipeline
Local PDF ingestion and querying
Vectorstore creation and retrieval
## Phase 2
FastAPI integration
PDF upload and query endpoints
Authentication (optional)
## Phase 3
Dashboard UI
Multi-PDF knowledge graph
Streaming responses
Advanced contextual reasoning