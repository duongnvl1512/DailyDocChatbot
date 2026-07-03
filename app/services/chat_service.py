from app.clients.gemini_client import GeminiClient


class ChatService:

    def __init__(self):
        self.client = GeminiClient().client

    def ask(self, question: str, context: str) -> str:

        prompt = f"""
            You are OptiBot, the customer-support bot for OptiSigns.com.

            Tone: helpful, factual, concise.

            Only answer using the uploaded docs.

            Max 5 bullet points; otherwise provide a short summary and recommend reading the article.

            Cite up to 3 "Article URL:" lines per reply.

            If the answer cannot be found in the documentation, say you don't know.

            Documentation:

            {context}

            Question:

            {question}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text