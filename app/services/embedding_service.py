from google import genai

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
        response = self.client.models.embed_content(
            model="gemini-embedding-2",
            contents=texts,
        )

        return [
            embedding.values
            for embedding in response.embeddings
        ]