from google import genai

from app.config import GOOGLE_API_KEY


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )