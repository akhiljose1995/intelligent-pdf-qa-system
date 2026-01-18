from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

class AppSettings(BaseModel):
    openai_api_key: str = os.getenv("OPENAI_API_KEY") #OpenAI API Key
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large") #Embedding model
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4.1-mini") #Language model
    #vectorstore_dir: str = os.getenv("VECTORSTORE_DIR", "data/vectorstore") #Directory for vector store
    vectorstore_dir: str = os.path.join(BASE_DIR, "data", "vectorstore") #Directory for vector store


settings = AppSettings()
