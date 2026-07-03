from pathlib import Path

from app.models.article import Article


class MarkdownWriter:

    def __init__(self, output_dir: str = "docs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def save(self, article: Article, markdown: str):

        filename = f"{article.slug}.md"

        filepath = self.output_dir / filename

        content = f"""---
id: {article.id}
title: {article.title}
url: {article.url}
updated_at: {article.updated_at}
---

# {article.title}

{markdown}
"""

        filepath.write_text(content, encoding="utf-8")