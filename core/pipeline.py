from typing import List

from core.loader import PDFLoader
from core.chunker import TextChunker
from core.vector_store import VectorStore
from core.retriever import Retriever
from core.generation_engine import GenerationEngine
from core.models import DocumentChunk
from utils.logger import setup_logger

logger = setup_logger(__name__)


class PDFRAGPipeline:
    """
    Orchestrates the end-to-end RAG workflow:
    PDF → chunks → vectors → retrieval → generation.

    This class is intentionally thin and declarative.
    """

    def __init__(self, reset_vectorstore: bool = False):
        self.loader = PDFLoader()
        self.chunker = TextChunker()
        self.vector_store = VectorStore(reset=reset_vectorstore)
        self.retriever = Retriever(self.vector_store)
        self.generator = GenerationEngine()

    def ingest_pdf(self, pdf_path: str) -> None:
        """
        Load and index a PDF into the vector store.
        """
        logger.info(f"Ingesting PDF: {pdf_path}")

        documents = self.loader.load(pdf_path)
        chunks = self.chunker.chunk(documents)
        self.vector_store.add_documents(chunks)

    def retrieve_context(
        self,
        query: str,
        k: int = 5
    ) -> List[DocumentChunk]:
        """
        Retrieve relevant context chunks for a query.
        """
        return self.retriever.retrieve(query, k=k)

    def generate(
        self,
        user_input: str,
        system_instruction: str,
        k: int = 5
    ) -> str:
        """
        Full retrieval + generation step.
        """
        context = self.retrieve_context(user_input, k=k)
        return self.generator.generate(
            user_input=user_input,
            context_chunks=context,
            system_instruction=system_instruction
        )
