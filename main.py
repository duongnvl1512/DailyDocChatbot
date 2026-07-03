from app.services.article_service import ArticleService
from app.services.document_service import DocumentService


def main():

    article_service = ArticleService()

    document_service = DocumentService()

    articles = article_service.get_articles()

    for article in articles:
        document_service.export(article)

    print(f"Saved {len(articles)} markdown files.")


if __name__ == "__main__":
    main()