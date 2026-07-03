from pathlib import Path

import yaml

from app.processors.chunk_processor import ChunkProcessor
from app.services.embedding_service import EmbeddingService
from app.vectorstore.faiss_store import FaissStore


class IndexService:

    def __init__(self):
        self.processor = ChunkProcessor()
        self.embedding = EmbeddingService()

    def build(self):
        files = list(Path("docs").glob("*.md"))
        print(f"Building index from {len(files)} markdown files...\n")

        store = None
        total_chunks = 0

        for index, file in enumerate(files, start=1):
            print(f"[{index}/{len(files)}] {file.name}")
            chunks = self._load_chunks(file)
            print(f"    Chunks: {len(chunks)}")
            total_chunks += len(chunks)

            for chunk in chunks:

                vector = self.embedding.embed(chunk.content)

                if store is None:
                    store = FaissStore(len(vector))

                store.add(vector,chunk,)

        store.save()

        self._print_summary(
            files,
            total_chunks,
            store,
        )

        return store

    def load(self):
        print("Loading FAISS index...")
        store = FaissStore.load()

        print(f"Loaded {len(store.metadata)} chunks.")

        return store

    def _load_chunks(self, file):

        markdown = file.read_text(encoding="utf-8")
        parts = markdown.split("---")
        metadata = yaml.safe_load(parts[1])
        metadata["slug"] = file.stem
        content = "---".join(parts[2:])

        return self.processor.split(
            content,
            metadata,
        )

    def _print_summary(
        self,
        files,
        total_chunks,
        store,
    ):

        print()
        print("=" * 60)
        print("INDEX SUMMARY")
        print("=" * 60)
        print(f"Files      : {len(files)}")
        print(f"Chunks     : {total_chunks}")
        print(f"Vectors    : {len(store.metadata)}")
        print(f"Dimension  : {store.index.d}")
        print("=" * 60)