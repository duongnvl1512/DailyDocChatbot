from app.services.index_service import IndexService


def main():

    print("=" * 60)
    print("BUILD INDEX")
    print("=" * 60)

    service = IndexService()

    service.build()


if __name__ == "__main__":
    main()