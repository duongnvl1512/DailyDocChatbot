import pickle
from pathlib import Path

import faiss
import numpy as np


class FaissStore:

    def __init__(self, dimension=None):

        self.index = (
            faiss.IndexFlatIP(dimension)
            if dimension
            else None
        )

        self.metadata = []

    def add(self, embedding, chunk):

        vector = np.array(
            [embedding],
            dtype="float32",
        )

        faiss.normalize_L2(vector)

        self.index.add(vector)

        self.metadata.append(chunk)

    def search(self, embedding, k=5):

        vector = np.array(
            [embedding],
            dtype="float32",
        )

        faiss.normalize_L2(vector)

        scores, indexes = self.index.search(
            vector,
            k,
        )

        results = []

        for score, index in zip(scores[0], indexes[0]):

            if index == -1:
                continue

            chunk = self.metadata[index]

            results.append(
                (
                    score,
                    chunk,
                )
            )

        return results
    
    def save(self, folder="storage"):

        Path(folder).mkdir(
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            f"{folder}/index.faiss",
        )

        with open(
            f"{folder}/metadata.pkl",
            "wb",
        ) as f:

            pickle.dump(
                self.metadata,
                f,
            )

    @classmethod
    def load(cls, folder="storage"):

        store = cls()

        store.index = faiss.read_index(
            f"{folder}/index.faiss"
        )

        with open(
            f"{folder}/metadata.pkl",
            "rb",
        ) as f:

            store.metadata = pickle.load(f)

        return store