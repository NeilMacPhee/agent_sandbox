import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key_gemini = os.getenv("GEMINI_API_KEY")

## API key for Gemini API
genai.configure(api_key=api_key_gemini)

## Model to use
model = genai.GenerativeModel("gemini-1.5-flash")

## Prompt to send to the model
prompt = "Write a poem about a baby squirrel"

## Send the prompt to the model
response = model.generate_content(prompt)

## Print the response
print(response.text)