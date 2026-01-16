from core.loader import PDFLoader
from core.chunker import TextChunker
from core.vector_store import VectorStore
from core.retriever import Retriever
from core.generation_engine import GenerationEngine

# Reset vector store for dev
store = VectorStore(reset=True)

loader = PDFLoader()
chunker = TextChunker()
retriever = Retriever(store)
generator = GenerationEngine()

docs = loader.load("data/raw/sample.pdf")
chunks = chunker.chunk(docs)
store.add_documents(chunks)

user_input = "Summarize the key themes discussed in the document."

system_instruction = (
    "You are an assistant that summarizes documents based on the given context."
)

context = retriever.retrieve(user_input, k=5)
output = generator.generate(
    user_input=user_input,
    context_chunks=context,
    system_instruction=system_instruction
)

print("\nGenerated Output:\n")
print(output)
