from app.services.chat_service import ChatService
from app.services.embedding_service import EmbeddingService


class RagService:

    def __init__(self, store):

        self.store = store
        self.embedding = EmbeddingService()
        self.chat = ChatService()

    def ask(self, question: str):

        query_vector = self.embedding.embed(question)

        chunks = self.store.search(
            query_vector,
            k=5,
        )

        if not chunks:
            return "I couldn't find any related documentation."

        print("\nRetrieved Chunks")
        print("=" * 60)

        context = ""

        for score, chunk in chunks:

            print(f"{score:.3f} | {chunk.article_title}")

            context += f"""
                ==================================================

                Similarity:
                {score:.3f}

                Title:
                {chunk.article_title}

                Article URL:
                {chunk.article_url}

                Content:

                {chunk.content}

                """

        print("=" * 60)

        answer = self.chat.ask(
            question,
            context,
        )

        return answer