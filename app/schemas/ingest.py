from pydantic import BaseModel

class IngestRequest(BaseModel):
    pdf_path: str
    reset_vectorstore: bool = False
