import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://support.optisigns.com"

ARTICLES_API = f"{BASE_URL}/api/v2/help_center/articles.json"

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

ARTICLE_LIMIT = 10
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")