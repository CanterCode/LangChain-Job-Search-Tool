import requests
from config import adzuna_setup


SEARCH_QUERIES = [
    "developer",
    "software",
    "frontend",
    "react",
    "javascript",
]


LOCATION = "Dallas, TX"


def fetch_adzuna_jobs():
    all_jobs = []

    for query in SEARCH_QUERIES:
        url = f"{adzuna_setup.ADZUNA_BASE_URL}/{adzuna_setup.ADZUNA_COUNTRY}/search/1"

        params = {
            "app_id": adzuna_setup.ADZUNA_APP_ID,
            "app_key": adzuna_setup.ADZUNA_APP_KEY,
            "results_per_page": 50,
            "what": query,
            "where": LOCATION,
            "content-type": "application/json",
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        print(f"Query '{query}' returned {len(data.get('results', []))} results")

        # we'll normalize results next
        for job in data.get("results", []):
            normalized = {
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "description": job.get("description", ""),
                "url": job.get("redirect_url"),
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
            }
            all_jobs.append(normalized)


    return all_jobs