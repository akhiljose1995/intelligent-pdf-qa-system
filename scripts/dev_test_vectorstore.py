from core.loader import PDFLoader
from core.chunker import TextChunker
from core.vector_store import VectorStore

loader = PDFLoader()
chunker = TextChunker()
store = VectorStore(reset=True)

docs = loader.load("data/raw/1.pdf")
chunks = chunker.chunk(docs)

store.add_documents(chunks)

results = store.similarity_search("What is this document about?", k=3)

for r in results:
    print(r.metadata, r.text[:200])
