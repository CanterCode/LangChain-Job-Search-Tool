from utils.adzuna_fetcher import fetch_adzuna_jobs
from utils.filtering import filter_jobs
from utils.ranking import rank_jobs
from utils.job_parser import parse_job
from config.preferences import USER_PREFERENCES

# 1. Fetch raw jobs
print("Fetching jobs...")
raw_jobs = fetch_adzuna_jobs()
print(f"Fetched {len(raw_jobs)} raw jobs")

# 2. Parse jobs
print("Parsing jobs...")
parsed_jobs = []
for job in raw_jobs:
    parsed = parse_job(job)
    parsed_jobs.append(parsed)

print(f"Parsed {len(parsed_jobs)} jobs")

# 3. Filter jobs
print("Filtering jobs...")
filtered_jobs = filter_jobs(parsed_jobs, USER_PREFERENCES)
print(f"Filtered down to {len(filtered_jobs)} jobs")

# 4. Rank jobs
print("Ranking jobs...")
ranked_jobs = rank_jobs(filtered_jobs, USER_PREFERENCES)

# 5. Print top matches
print("\n--- TOP MATCHES ---")
for job in ranked_jobs[:10]:
    print(f"{job['score']} — {job['job_title']} — {job['location']} — {job['url']}")
    