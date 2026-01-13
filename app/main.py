from fastapi import FastAPI

app = FastAPI(title="Intelligent PDF Q&A System")

@app.get("/health")
def health_check():
    return {"status": "ok"}
