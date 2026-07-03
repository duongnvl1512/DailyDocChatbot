from typing import List

from app.clients.zendesk_client import ZendeskClient
from app.models.article import Article
from app.utils.slug import slugify
from app.utils.logger import logger
from app.config import ARTICLE_LIMIT

class ArticleService:
    def __init__(self):
        self.client = ZendeskClient()

    def get_articles(self) -> List[Article]:

        articles = []

        for page in self.client.fetch_all_articles():

            page_articles = page.get("articles", [])

            logger.info(
                "Found %s articles",
                len(page_articles),
            )

            for item in page_articles:

                article = Article(
                    id=item["id"],
                    title=item["title"],
                    slug=slugify(item["title"]),
                    url=item["html_url"],
                    body=item["body"],
                    updated_at=item["updated_at"],
                )

                articles.append(article)

                if (
                    ARTICLE_LIMIT is not None
                    and len(articles) >= ARTICLE_LIMIT
                ):
                    logger.info(
                        "Reached article limit: %s",
                        ARTICLE_LIMIT,
                    )
                    return articles

        logger.info(
            "Total Articles: %s",
            len(articles),
        )

        return articles