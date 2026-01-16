from typing import List
from langchain_openai import OpenAIEmbeddings

from core.models import DocumentChunk
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class Embedder:
    """
    Embedder is responsible for converting text chunks into vector embeddings.

    This class encapsulates all embedding-related logic so that:
    - The embedding provider can be swapped easily
    - The rest of the pipeline remains unaffected
    """

    def __init__(self):
        """
        Initialize the embedding model using configuration settings.
        """
        self.embedding_model = OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key
        )

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of text strings.

        Args:
            texts (List[str]): Text content to embed.

        Returns:
            List[List[float]]: Corresponding embedding vectors.
        """
        logger.info(f"Generating embeddings for {len(texts)} texts")
        return self.embedding_model.embed_documents(texts)
