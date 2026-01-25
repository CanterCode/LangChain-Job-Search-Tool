def score_job(job, prefs):
    score = 0
    title = job.get("job_title", "").lower()
    location = job.get("location", "").lower()

    # --- CATEGORY 1: React / JS / Frontend (max 50) ---
    tech_score = 0
    if "react" in title:
        tech_score += 30
    if "javascript" in title:
        tech_score += 20
    if "frontend" in title:
        tech_score += 20
    if "ui" in title or "web" in title:
        tech_score += 10
    tech_score = min(tech_score, 50)
    score += tech_score

    # --- CATEGORY 2: Seniority (max 20) ---
    if "junior" in title or "entry" in title or "associate" in title:
        score += 20
    elif "mid" in title:
        score += 5

    # --- CATEGORY 3: Location (max 20) ---
    if any(city in location for city in prefs["primary_cities"]):
        score += 20
    elif any(city in location for city in prefs["secondary_cities"]):
        score += 10

    # Dallas penalties
    if "dallas" in location:
        score -= 20
    if any(city in location for city in ["irving", "richardson", "plano", "frisco"]):
        score -= 10

    # --- CATEGORY 4: Tech penalties (max -20) ---
    if "java" in title and "react" not in title:
        score -= 20
    if "spring" in title or ".net" in title:
        score -= 10

    # --- CATEGORY 5: Work arrangement (max 10) ---
    if "remote" in location:
        score += 5
    elif "hybrid" in location:
        score += 10


    job["score"] = score
    return score
