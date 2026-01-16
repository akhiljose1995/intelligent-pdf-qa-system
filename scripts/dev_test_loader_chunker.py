from core.loader import PDFLoader
from core.chunker import TextChunker

loader = PDFLoader()
chunker = TextChunker()

docs = loader.load("data/raw/sample.pdf")
chunks = chunker.chunk(docs)

print(f"Pages: {len(docs)}")
print(f"Chunks: {len(chunks)}")
print(chunks[0])
