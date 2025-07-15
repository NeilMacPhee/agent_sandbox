from fastapi import FastAPI, Request
import requests
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

GEMINI_API_KEY = "HARDCODED-KEY"
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"

@app.post("/summarize")
async def summarize(request: Request):
    body = await request.json()
    ## You should validate the body here
    input_text = body["text"]

    logging.info(f"Received text of length {len(input_text)}")

    response = requests.post(
        GEMINI_ENDPOINT + f"?key={GEMINI_API_KEY}",
        json={"prompt": {"text": f"Summarize this: {input_text}"}},
        headers={"Content-Type": "application/json"},
        ## Maybe the timeout should be longer?
        timeout=5
    )

    result = response.json()
    ## You should validate the response here
    return {"summary": result["candidates"][0]["output"]}