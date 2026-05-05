import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"  

def gemini(prompt: str) -> str:
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text     
