from pathlib import Path

import time
import yaml

from app.processors.chunk_processor import ChunkProcessor
from app.services.embedding_service import EmbeddingService
from app.vectorstore.faiss_store import FaissStore


class IndexService:

    def __init__(self):
        self.processor = ChunkProcessor()
        self.embedding = EmbeddingService()

    def embed_with_retry(self, texts):
        while True:
            try:
                return self.embedding.embed_batch(texts)

            except Exception as e:

                error = str(e)

                if "429" in error:
                    print()
                    print("Quota exceeded.")
                    print("Sleeping 10 seconds...")
                    print()

                    time.sleep(10)

                    continue
                raise
        
    def build(self):

        files = list(Path("docs").glob("*.md"))

        print(f"Building index from {len(files)} markdown files...\n")

        store = None
        total_chunks = 0

        BATCH_SIZE = 20

        batch_chunks = []
        batch_texts = []

        for file_index, file in enumerate(files, start=1):

            print(f"[{file_index}/{len(files)}] {file.name}")

            markdown = file.read_text(
                encoding="utf-8"
            )

            parts = markdown.split("---")
            metadata = yaml.safe_load(parts[1])
            metadata["slug"] = file.stem
            content = "---".join(parts[2:])

            chunks = self.processor.split(
                content,
                metadata,
            )

            print(f"    Chunks: {len(chunks)}")

            total_chunks += len(chunks)

            for chunk in chunks:

                batch_chunks.append(chunk)
                batch_texts.append(chunk.content)

                if len(batch_texts) >= BATCH_SIZE:

                    vectors = self.embed_with_retry(batch_texts)

                    if store is None:
                        store = FaissStore(len(vectors[0]))

                    for vector, chunk in zip(vectors, batch_chunks):
                        store.add(vector, chunk)

                    batch_chunks.clear()
                    batch_texts.clear()

        if batch_texts:
            vectors = self.embed_with_retry(batch_texts)

            if store is None:
                store = FaissStore(len(vectors[0]))

            for vector, chunk in zip(vectors, batch_chunks):
                store.add(vector, chunk)

        store.save()

        print()
        print("=" * 60)
        print("INDEX SUMMARY")
        print("=" * 60)
        print(f"Files      : {len(files)}")
        print(f"Chunks     : {total_chunks}")
        print(f"Vectors    : {len(store.metadata)}")
        print(f"Dimension  : {store.index.d}")
        print("=" * 60)

        return store

    def load(self):
        print("Loading FAISS index...")
        store = FaissStore.load()
        print(f"Loaded {len(store.metadata)} chunks.")

        return store