import os
from dotenv import load_dotenv
load_dotenv(".env")
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents='Say hello world',
)
print(response.text)
