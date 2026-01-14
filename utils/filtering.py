import re

def extract_years(exp_str):
    """Extract the first number from an experience string like '3+ years'."""
    if not exp_str:
        return None
    nums = re.findall(r"\d+", exp_str)
    return int(nums[0]) if nums else None


def is_disqualified(job, prefs):
    """Return True if the job should be removed before scoring."""

    title = job.get("job_title", "").lower()
    skills = [s.lower() for s in job.get("required_skills", [])]

    # 1. Disqualify by title keywords
    for bad in prefs["disqualify_title_keywords"]:
        if bad in title:
            return True

    # 2. Disqualify by backend/undesired tech
    for tech in prefs["disqualify_tech"]:
        if tech in skills:
            return True

    # 3. Disqualify by experience > max allowed
    years = extract_years(job.get("required_experience", ""))
    if years and years > prefs["max_experience_years"]:
        return True

    return False


def filter_jobs(jobs, prefs):
    """Return only jobs that pass all disqualifier checks."""
    return [job for job in jobs if not is_disqualified(job, prefs)]