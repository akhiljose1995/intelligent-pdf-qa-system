from typing import List
from pypdf import PdfReader

from core.models import DocumentChunk
from utils.logger import setup_logger

logger = setup_logger(__name__)


class PDFLoader:
    """
    PDFLoader is responsible for loading a PDF file and extracting
    page-level text along with metadata.

    This class performs only one responsibility:
    - Read a PDF file
    - Extract text per page
    - Attach basic metadata for traceability

    It is intentionally kept independent of chunking, embeddings,
    or LLM logic to maintain clean separation of concerns.
    """

    def __init__(self):
        """
        Initialize the PDFLoader.

        Currently, no configuration is required, but this constructor
        exists to support future extensions (e.g., OCR, password-protected PDFs).
        """
        pass

    def load(self, file_path: str) -> List[DocumentChunk]:
        """
        Load a PDF file and extract text from each page.

        Each page is converted into a DocumentChunk with metadata
        containing the page number and source file path.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            List[DocumentChunk]: A list of document chunks, one per page,
                                 containing extracted text and metadata.
        """
        logger.info(f"Loading PDF: {file_path}")
        reader = PdfReader(file_path)

        documents = []

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()

            if not text:
                continue

            documents.append(
                DocumentChunk(
                    text=text.strip(),
                    metadata={
                        "page": page_num + 1,
                        "source": file_path
                    }
                )
            )

        logger.info(f"Extracted {len(documents)} pages from PDF")
        return documents
