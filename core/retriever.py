from typing import List, Optional

from core.models import DocumentChunk
from core.vector_store import VectorStore
from utils.logger import setup_logger

logger = setup_logger(__name__)


class Retriever:
    """
    Generic retrieval component responsible for fetching relevant
    document chunks based on a query and retrieval parameters.

    This class does NOT assume any downstream task (Q&A, summary, etc.).
    """

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        k: int = 5,
        filters: Optional[dict] = None
    ) -> List[DocumentChunk]:
        """
        Retrieve relevant document chunks.

        Args:
            query (str): Retrieval query.
            k (int): Number of chunks to retrieve.
            filters (dict, optional): Metadata filters for retrieval.

        Returns:
            List[DocumentChunk]: Retrieved chunks.
        """
        logger.info(f"Retrieving top {k} chunks")

        # Filters are future-ready; not used yet
        return self.vector_store.similarity_search(query, k=k)
