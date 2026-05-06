from google import genai

class LLM:
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash") -> None:
        self.client = genai.Client(api_key=api_key)
        self.model = model_name

    def get_response(self, prompt: str) -> str | None:
        res = self.client.models.generate_content(model=self.model, contents=prompt)
        return res.text
