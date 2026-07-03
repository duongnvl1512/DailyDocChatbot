import time

import requests

from app.config import (
    ARTICLES_API,
    MAX_RETRIES,
    REQUEST_TIMEOUT,
)

class ZendeskClient:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url: str) -> dict:

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = self.session.get(
                    url,
                    timeout=REQUEST_TIMEOUT,
                )

                response.raise_for_status()
                return response.json()

            except requests.RequestException:
                if attempt == MAX_RETRIES:
                    raise

                time.sleep(2)
                
        return {}

    def fetch_all_articles(self):
        url = ARTICLES_API
        page = 1

        while url:
            data = self.get(url)
            yield data
            url = data.get("next_page")
            page += 1