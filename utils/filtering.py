def filter_jobs(jobs, prefs):
    filtered = []
    reasons = {
        "not_tech": 0,
        "disqualify_title": 0,
        "disqualify_tech": 0,
        "bad_location": 0,
        "no_skills_listed": 0,
        "backend_only": 0,
        "too_senior": 0,
        "too_much_experience": 0,
        "kept": 0,
    }

    for job in jobs:
        title = (job.get("job_title") or "").lower()
        location = (job.get("location") or "").lower()
        skills = job.get("skills") or []
        role_type = job.get("role_type") or "unknown"
        seniority = job.get("seniority") or "unknown"
        years = job.get("years_experience")

        # STRICT RULE: must be a tech job
        if not job.get("is_tech_job"):
            reasons["not_tech"] += 1
            continue

        # Disqualify by title keywords
        if any(keyword in title for keyword in prefs["disqualify_title_keywords"]):
            reasons["disqualify_title"] += 1
            continue

        # Disqualify by tech stack
        if any(tech in title for tech in prefs["disqualify_tech"]):
            reasons["disqualify_tech"] += 1
            continue

        # Must be in allowed cities or remote
        if "remote" not in location and not any(city in location for city in prefs["allowed_cities"]):
            reasons["bad_location"] += 1
            continue

        # Must have at least one skill
        if not skills and not any(term in title for term in ["react", "frontend", "javascript", "ui", "web"]):
            reasons["no_skills_listed"] += 1
            continue


        # Must not be backend-only
        if role_type == "backend":
            reasons["backend_only"] += 1
            continue

        # Must not be senior
        if seniority == "senior":
            reasons["too_senior"] += 1
            continue

        # Must not require > 3 years
        if years is not None and years > 3:
            reasons["too_much_experience"] += 1
            continue

        filtered.append(job)
        reasons["kept"] += 1

    print("\n--- FILTERING BREAKDOWN ---")
    for reason, count in reasons.items():
        print(f"{reason}: {count}")

    return filtered