from core.models import DocumentChunk
from core.vector_store import VectorStore


def test_vector_store_similarity_search():
    store = VectorStore()

    chunks = [
        DocumentChunk(
            text="Python is a programming language",
            metadata={"source": "test"}
        ),
        DocumentChunk(
            text="Cats are animals",
            metadata={"source": "test"}
        ),
    ]

    store.add_documents(chunks)

    results = store.similarity_search("What is Python?", k=1)

    assert len(results) == 1
    assert "Python" in results[0].text
