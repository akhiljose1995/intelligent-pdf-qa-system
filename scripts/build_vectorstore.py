import argparse
from core.pipeline import PDFRAGPipeline

parser = argparse.ArgumentParser(description="Build vector store from PDF")
parser.add_argument("--pdf", required=True, help="Path to PDF file")
parser.add_argument(
    "--reset",
    action="store_true",
    help="Reset vector store before ingestion"
)

args = parser.parse_args()

pipeline = PDFRAGPipeline(reset_vectorstore=args.reset)
pipeline.ingest_pdf(args.pdf)

print("Vector store built successfully.")
