from dataclasses import dataclass


@dataclass
class ScrapeResult:
    added: int = 0
    updated: int = 0
    skipped: int = 0

    @property
    def has_changes(self):
        return self.added > 0 or self.updated > 0