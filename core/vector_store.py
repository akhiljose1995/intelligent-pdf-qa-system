from typing import List
import os

#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma

from core.models import DocumentChunk
from core.embedder import Embedder
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class VectorStore:
    """
    VectorStore is a thin wrapper around ChromaDB that handles:
    - Storing embeddings
    - Persisting vectors to disk
    - Performing similarity search
    """

    def __init__(self, reset: bool = False):
        """
        Initialize or load a persistent ChromaDB vector store.
        """
        print("Vectorstore dir:", settings.vectorstore_dir)
        self.embedder = Embedder()

        os.makedirs(settings.vectorstore_dir, exist_ok=True)

        if reset and os.path.exists(settings.vectorstore_dir):
            import shutil
            shutil.rmtree(settings.vectorstore_dir)

        self.store = Chroma(
            collection_name="pdf_chunks",
            embedding_function=self.embedder.embedding_model,
            persist_directory=settings.vectorstore_dir
        )

    def add_documents(self, chunks: List[DocumentChunk]) -> None:
        """
        Add document chunks to the vector store.

        Args:
            chunks (List[DocumentChunk]): Chunks containing text and metadata.
        """
        logger.info(f"Adding {len(chunks)} chunks to vector store")

        texts = [c.text for c in chunks]
        metadatas = [c.metadata for c in chunks]

        self.store.add_texts(texts=texts, metadatas=metadatas)

    def similarity_search(self, query: str, k: int = 5) -> List[DocumentChunk]:
        """
        Perform similarity search for a given query.

        Args:
            query (str): User query.
            k (int): Number of similar chunks to retrieve.

        Returns:
            List[DocumentChunk]: Retrieved document chunks.
        """
        logger.info(f"Running similarity search for query: {query}")

        results = self.store.similarity_search(query, k=k)

        return [
            DocumentChunk(text=doc.page_content, metadata=doc.metadata)
            for doc in results
        ]
