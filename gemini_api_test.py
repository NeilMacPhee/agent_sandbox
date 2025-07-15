import google.generativeai as genai

## API key for Gemini API
genai.configure(api_key="AIzaSyCLR6X4wDcLH9S66DqQzelMGQgU1of6qn4")

## Model to use
model = genai.GenerativeModel("gemini-1.5-flash")

## Prompt to send to the model
prompt = "Write a poem about a baby squirrel"

## Send the prompt to the model
response = model.generate_content(prompt)

## Print the response
print(response.text)