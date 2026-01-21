from utils.scoring import score_job

def rank_jobs(jobs, prefs):
    ranked = []

    for job in jobs:
        score = score_job(job, prefs)
        job["score"] = score
        ranked.append(job)

    return sorted(ranked, key=lambda j: j["score"], reverse=True)
