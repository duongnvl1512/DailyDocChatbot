from app.models.scrape_result import ScrapeResult
from app.services.article_service import ArticleService
from app.services.document_service import DocumentService
from app.services.index_service import IndexService
from app.services.state_service import StateService


def main():

    article_service = ArticleService()
    document_service = DocumentService()
    state_service = StateService()

    result = ScrapeResult()

    articles = article_service.get_articles()

    print(f"\nChecking {len(articles)} articles...\n")

    for article in articles:

        if state_service.is_new(article):

            document_service.export(article)

            state_service.update(article)

            result.added += 1

            continue

        if state_service.is_updated(article):

            document_service.export(article)

            state_service.update(article)

            result.updated += 1

            continue

        result.skipped += 1

    state_service.save()

    print()
    print("=" * 60)
    print("SCRAPE SUMMARY")
    print("=" * 60)
    print(f"Added   : {result.added}")
    print(f"Updated : {result.updated}")
    print(f"Skipped : {result.skipped}")
    print("=" * 60)

    if result.has_changes:

        print("\nChanges detected.")
        print("Rebuilding index...\n")

        IndexService().build()

    else:

        print("\nNo changes detected.")
        print("Skip rebuilding index.")


if __name__ == "__main__":
    main()