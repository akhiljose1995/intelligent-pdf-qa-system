from fastapi import APIRouter, HTTPException
from app.schemas.ingest import IngestRequest
from app.schemas.generate import GenerateRequest, GenerateResponse
from app.services.rag_service import RAGService
from core.errors import RAGError

router = APIRouter()
service = RAGService()


@router.post("/ingest")
def ingest_pdf(request: IngestRequest):
    try:
        service.ingest_pdf(
            pdf_path=request.pdf_path,
            reset=request.reset_vectorstore
        )
        return {"status": "ingestion successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        output = service.generate(request.user_input)
        intent = service.intent_classifier.classify(request.user_input)

        return GenerateResponse(
            output=output,
            intent=intent.value
        )

    except RAGError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal system error"
        )
