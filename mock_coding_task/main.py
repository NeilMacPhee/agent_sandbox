from fastapi import FastAPI, Request, Body, HTTPException
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
import requests

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

### Remove hardercode API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")
GEMINI_ENDPOINT = os.getenv("GEMINI_ENDPOINT")
if not GEMINI_ENDPOINT:
    raise ValueError("GEMINI_ENDPOINT environment variable is not set.")

### Request Model
class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=1000, description="Text to summarize")

### Response Model
class SummarizeResponse(BaseModel):
    summary: str

def call_gemini_api(prompt: str) -> str:
    try:
        response = requests.post(
            GEMINI_ENDPOINT + f"?key={GEMINI_API_KEY}",
            json={"prompt": {"text": prompt}},
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["output"]
    except (KeyError, IndexError, TypeError):
        raise HTTPException(status_code=502, detail="Invalid response from Gemini API")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail="Gemini API call failed")
    

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    summary = call_gemini_api("Summarize the following text: " + request.text)
    return SummarizeResponse(summary=summary)