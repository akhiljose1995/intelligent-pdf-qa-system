from pydantic import BaseModel


class GenerateRequest(BaseModel):
    user_input: str


class GenerateResponse(BaseModel):
    output: str
    intent: str