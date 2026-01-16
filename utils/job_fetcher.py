import requests
import feedparser
from urllib.parse import quote_plus

# Base RSS URL pattern (Indeed)
INDEED_RSS_URL = "https://www.indeed.com/rss?q={query}&l=dfw"

# Search queries
SEARCH_QUERIES = [
    "junior react developer dfw",
    "frontend developer dfw",
    "javascript developer dfw",
    "entry level software engineer dfw",
    "junior web developer dfw",
]


def build_rss_url(query: str) -> str:
    encoded = quote_plus(query)
    return INDEED_RSS_URL.format(query=encoded)


def fetch_rss_feed(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return feedparser.parse(response.text)


def fetch_raw_jobs_from_rss():
    jobs = []

    for query in SEARCH_QUERIES:
        url = build_rss_url(query)
        feed = fetch_rss_feed(url)

        for entry in feed.entries:
            job = {
                "title": entry.get("title"),
                "link": entry.get("link"),
                "description": entry.get("description", ""),
                "published": entry.get("published", None),
                "company": entry.get("author", None),
                "location": None,
            }
            jobs.append(job)

    return jobs