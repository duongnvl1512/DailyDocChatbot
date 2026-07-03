from app.services.rag_service import RagService
from app.vectorstore.faiss_store import FaissStore


def main():

    print("=" * 60)
    print("Loading FAISS index...")
    print("=" * 60)

    store = FaissStore.load()

    print(f"Loaded {len(store.metadata)} chunks\n")

    rag = RagService(store)

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            break

        print()

        answer = rag.ask(question)

        print(answer)

        print()


if __name__ == "__main__":
    main()