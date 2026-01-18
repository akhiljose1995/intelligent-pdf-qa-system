from fastapi import FastAPI
from app.routers import health, rag

app = FastAPI(
    title="Intelligent PDF RAG System",
    version="0.1.0"
)

app.include_router(health.router, tags=["health"])
app.include_router(rag.router, prefix="/rag", tags=["rag"])
