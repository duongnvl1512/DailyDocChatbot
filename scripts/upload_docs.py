from pathlib import Path

from app.clients.gemini_client import GeminiClient


def main():

    client = GeminiClient().client

    docs = list(Path("docs").glob("*.md"))

    print("=" * 60)
    print("UPLOAD DOCUMENTS")
    print("=" * 60)

    uploaded = 0

    for file in docs:

        print(f"Uploading {file.name}")

        client.files.upload(
            file=file
        )

        uploaded += 1

    print()
    print("=" * 60)
    print(f"Uploaded {uploaded} markdown files.")
    print("=" * 60)


if __name__ == "__main__":
    main()