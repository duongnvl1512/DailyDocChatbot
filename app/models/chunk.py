from dataclasses import dataclass


@dataclass
class Chunk:
    article_id: int
    article_title: str
    article_slug: str
    article_url: str
    chunk_index: int
    content: str