from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import random
import requests

app = FastAPI()

# Request Model
class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=1000, description="Text to summarize")

# Response Model
class SummarizeResponse(BaseModel):
    summary: str
    model_version: Optional[str] = "v1.0"

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    # Fake Gemini-like logic for demo
    if random.random() < 0.05:
        raise HTTPException(status_code=500, detail="LLM service unavailable")

    summary = request.text[:75] + "..."  # Fake summary
    return SummarizeResponse(summary=summary)