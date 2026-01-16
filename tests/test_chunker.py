from core.chunker import TextChunker
from core.models import DocumentChunk

def test_text_chunker():
    docs = [
        DocumentChunk(
            text="This is a test document " * 100,
            metadata={"page": 1}
        )
    ]

    chunker = TextChunker(chunk_size=200, chunk_overlap=50)
    chunks = chunker.chunk(docs)

    assert len(chunks) > 1
    assert "chunk_id" in chunks[0].metadata
