from utils.job_fetcher import fetch_raw_jobs_from_rss
from chains.job_parser import parse_job_description
from utils.filtering import filter_jobs
from utils.ranking import rank_jobs
from utils.scoring import score_job
from config.preferences import USER_PREFERENCES


def parse_rss_jobs(raw_jobs):
    parsed_jobs = []

    for raw in raw_jobs:
        description = raw.get("description", "")
        parsed = parse_job_description(description)

        # Attach metadata from RSS so it survives the pipeline
        parsed["job_url"] = raw.get("link")
        parsed["company"] = raw.get("company")
        parsed["job_title"] = parsed.get("job_title") or raw.get("title")
        parsed["location"] = parsed.get("location") or raw.get("location")

        parsed_jobs.append(parsed)

    return parsed_jobs


def main():
    print("Fetching jobs from RSS feeds...")
    raw_jobs = fetch_raw_jobs_from_rss()
    print(f"Fetched {len(raw_jobs)} raw jobs")

    print("Parsing job descriptions...")
    parsed_jobs = parse_rss_jobs(raw_jobs)

    print("Filtering jobs...")
    filtered_jobs = filter_jobs(parsed_jobs, USER_PREFERENCES)

    print("Ranking jobs...")
    ranked_jobs = rank_jobs(filtered_jobs, USER_PREFERENCES)

    print("\n=== TOP MATCHES ===\n")
    for job in ranked_jobs[:10]:
        score = score_job(job, USER_PREFERENCES)
        print(f"{job.get('job_title')} — Score: {score}")
        print(f"Company: {job.get('company')}")
        print(f"Location: {job.get('location')}")
        print(f"Link: {job.get('job_url')}")
        print("-" * 40)


if __name__ == "__main__":
    main()