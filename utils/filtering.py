def filter_jobs(jobs, prefs):
    filtered = []

    for job in jobs:
        title = job.get("job_title", "").lower()
        location = job.get("location", "").lower()
        skills = job.get("skills") or []
        role_type = job.get("role_type") or "unknown"
        seniority = job.get("seniority") or "unknown"

        years = job.get("years_experience")

        # STRICT RULE: must be a tech job
        if not job.get("is_tech_job"):
            continue
        
        # Disqualify by title keywords
        if any(keyword in title for keyword in prefs["disqualify_title_keywords"]):
            continue

        # Disqualify by tech stack
        if any(tech in title for tech in prefs["disqualify_tech"]):
            continue


        # Must be in allowed cities or remote
        if "remote" not in location and not any(city in location for city in prefs["allowed_cities"]):
            continue

        # Must have at least one skill
        if not skills:
            continue

        # Must not be backend-only
        if role_type == "backend":
            continue

        # Must not be senior
        if job.get("seniority") == "senior":
            continue


        # Must not require > 3 years
        if years is not None and years > 3:
            continue

        filtered.append(job)

    return filtered
