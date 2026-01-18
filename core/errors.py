class RAGError(Exception):
    """Base class for all RAG-related errors."""


class IngestionError(RAGError):
    """Raised when PDF ingestion fails."""


class RetrievalError(RAGError):
    """Raised when retrieval fails or returns no useful context."""


class GenerationError(RAGError):
    """Raised when LLM generation fails."""


class IntentError(RAGError):
    """Raised when intent classification fails."""
