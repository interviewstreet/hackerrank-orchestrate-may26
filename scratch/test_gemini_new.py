import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
if not key:
    print("No key")
    exit(1)

client = genai.Client(api_key=key)
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Say hello"
    )
    print(f"Success: {response.text}")
except Exception as e:
    print(f"Error: {e}")
