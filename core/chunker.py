from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

from core.models import DocumentChunk
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TextChunker:
    """
    TextChunker splits long documents into smaller, overlapping chunks
    suitable for embedding and semantic retrieval.

    It uses a recursive character-based splitting strategy to preserve
    semantic structure while controlling chunk size.
    """
    def __init__(
        self,
        chunk_size: int = 2000,
        chunk_overlap: int = 500
    ):
        """
        Initialize the TextChunker.

        Args:
            chunk_size (int): Maximum number of characters per chunk.
            chunk_overlap (int): Number of overlapping characters between
                                 consecutive chunks to preserve context.
        """
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk(self, documents: List[DocumentChunk]) -> List[DocumentChunk]:
        """
        Split a list of document chunks into smaller overlapping chunks.

        Original metadata is preserved and extended with a chunk identifier
        to uniquely identify each chunk.

        Args:
            documents (List[DocumentChunk]): List of page-level document chunks.

        Returns:
            List[DocumentChunk]: A list of smaller, overlapping chunks with
                                 updated metadata.
        """
        logger.info("Chunking documents")

        chunks: List[DocumentChunk] = []

        for doc in documents:
            split_texts = self.splitter.split_text(doc.text)

            for idx, text in enumerate(split_texts):
                chunks.append(
                    DocumentChunk(
                        text=text,
                        metadata={
                            **doc.metadata,
                            "chunk_id": idx
                        }
                    )
                )

        logger.info(f"Generated {len(chunks)} chunks")
        return chunks
