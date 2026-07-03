from dataclasses import dataclass


@dataclass(slots=True)
class Article:
    id: int
    title: str
    slug: str
    url: str
    body: str
    updated_at: str