from app.models.chunk import Chunk


class ChunkProcessor:

    def __init__(self, chunk_size=1000):
        self.chunk_size = chunk_size

    def split(self, article: str, metadata: dict):

        paragraphs = article.split("\n\n")

        chunks = []

        current = ""

        chunk_index = 0

        for paragraph in paragraphs:

            if len(current) + len(paragraph) < self.chunk_size:

                current += paragraph + "\n\n"

            else:

                chunks.append(
                    Chunk(
                        article_id=metadata["id"],
                        article_title=metadata["title"],
                        article_slug=metadata["slug"],
                        article_url=metadata["url"],
                        chunk_index=chunk_index,
                        content=current.strip(),
                    )
                )

                chunk_index += 1

                current = paragraph + "\n\n"

        if current:

            chunks.append(
                Chunk(
                    article_id=metadata["id"],
                    article_title=metadata["title"],
                    article_slug=metadata["slug"],
                    article_url=metadata["url"],
                    chunk_index=chunk_index,
                    content=current.strip(),
                )
            )

        return chunks