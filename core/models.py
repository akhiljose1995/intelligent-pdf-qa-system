from dataclasses import dataclass
from typing import Dict

@dataclass
class DocumentChunk:
    """
    Lightweight internal representation of a document chunk.

    This class acts as a framework-agnostic data model used across
    the RAG pipeline to pass text along with its associated metadata
    (e.g., page number, source file, chunk id).

    Attributes:
        text (str): The textual content of the chunk.
        metadata (Dict): Arbitrary metadata associated with the chunk,
                         such as page number, source path, or chunk id.
    """
    text: str
    metadata: Dict
