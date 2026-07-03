import json
from pathlib import Path


class StateService:

    def __init__(self):

        self.path = Path("data/state.json")
        self.path.parent.mkdir(exist_ok=True)
        self.state = self.load()

    def load(self):
        if not self.path.exists():
            return {}
        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)

    def save(self):

        with open(
            self.path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                self.state,
                f,
                indent=4,
            )

    def is_new(self, article):
        return str(article.id) not in self.state

    def is_updated(self, article):
        key = str(article.id)
        if key not in self.state:
            return False

        return (
            self.state[key]["updated_at"]
            != article.updated_at
        )

    def update(self, article):

        self.state[str(article.id)] = {
            "updated_at": article.updated_at
        }