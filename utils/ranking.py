from utils.scoring import score_job

def rank_jobs(jobs, prefs):
    ranked = []

    for job in jobs:
        score = score_job(job, prefs)
        job["score"] = score
        ranked.append(job)

    # Deduplicate by (title, company, location)
    seen = set()
    deduped = []
    for job in ranked:
        key = (
            job.get("job_title", "").lower(),
            job.get("company", "").lower(),
            job.get("location", "").lower()
        )
        if key not in seen:
            seen.add(key)
            deduped.append(job)

    return sorted(deduped, key=lambda j: j["score"], reverse=True)

