from utils.scoring import score_job

def rank_jobs(jobs, prefs):
    return sorted(
        jobs,
        key=lambda job: score_job(job, prefs),
        reverse=True
    )