import argparse
from core.pipeline import PDFRAGPipeline

parser = argparse.ArgumentParser(description="Generate output from PDF RAG")
parser.add_argument("--input", required=True, help="User input")
parser.add_argument(
    "--instruction",
    required=True,
    help="System instruction for generation"
)
parser.add_argument("--k", type=int, default=5)

args = parser.parse_args()

pipeline = PDFRAGPipeline(reset_vectorstore=False)

output = pipeline.generate(
    user_input=args.input,
    system_instruction=args.instruction,
    k=args.k
)

print("\nGenerated Output:\n")
print(output)
