import re

def extract_years(exp_str):
    """Extract the first number from an experience string like '3+ years'."""
    if not exp_str:
        return None
    nums = re.findall(r"\d+", exp_str)
    return int(nums[0]) if nums else None

def filter_jobs(jobs, prefs):
    filtered = []

    for job in jobs:
        # STRICT RULE: must be a tech job
        if not job.get("is_tech_job"):
            continue
        
        location = job.get("location", "").lower()
        
        if "remote" in location:
            pass

        # STRICT RULE: must be near Watauga
        if not any(region in location for region in ["fort worth", "tarrant", "dfw", "texas"]):
            continue

        # STRICT RULE: must have at least one skill
        if not job.get("skills"):
            continue

        # STRICT RULE: must not be backend-only
        if job.get("role_type") == "backend":
            continue

        # STRICT RULE: must not be senior
        if job.get("seniority") in ["senior", "lead", "principal", "staff", "architect", "sr", "sr."]:
            continue

        # STRICT RULE: must not require > 3 years
        years = job.get("years_experience")
        if years and years > 3:
            continue

        filtered.append(job)

    return filtered
