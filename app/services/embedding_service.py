from google import genai
import time
from app.config import GOOGLE_API_KEY


class EmbeddingService:

    def __init__(self):
        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

    def embed(self, text: str):
        response = self.client.models.embed_content(
            model="gemini-embedding-2",
            contents=text,
        )

        return response.embeddings[0].values



    def embed_batch(self, texts: list[str]):
        vectors = []

        for text in texts:
            response = self.client.models.embed_content(
                model="gemini-embedding-2",
                contents=text,
            )

            vectors.append(response.embeddings[0].values)
            time.sleep(0.1)

        return vectors