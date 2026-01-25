def score_job(job, prefs):
    score = 0
    title = job.get("job_title", "").lower()
    location = job.get("location", "").lower()
    weights = prefs["scoring_weights"]

    # --- CATEGORY 1: React / JS / Frontend (max 50) ---
    tech_score = 0
    if "react" in title:
        tech_score += weights["react_title"]
    if "javascript" in title:
        tech_score += weights["javascript_title"]
    if "frontend" in title:
        tech_score += weights["frontend_title"]
    if "ui" in title or "web" in title:
        tech_score += weights["ui_or_web_title"]
    tech_score = min(tech_score, weights["max_tech_score"])
    score += tech_score

    # --- CATEGORY 2: Seniority (max 20) ---
    if "junior" in title or "entry" in title or "associate" in title:
        score += weights["junior_bonus"]
    elif "mid" in title:
        score += weights["mid_bonus"]

    # --- CATEGORY 3: Location (max 20) ---
    if any(city in location for city in prefs["primary_cities"]):
        score += weights["primary_city_bonus"]
    elif any(city in location for city in prefs["secondary_cities"]):
        score += weights["secondary_city_bonus"]
    if "dallas" in location:
        score += weights["dallas_penalty"]


    # --- CATEGORY 4: Tech penalties (max -20) ---
    if "java" in title and "react" not in title:
        score += weights["java_penalty"]
    if "spring" in title or ".net" in title:
        score += weights["spring_dotnet_penalty"]

    # --- CATEGORY 5: Work arrangement (max 10) ---
    if "remote" in location:
        score += weights["remote_bonus"]
    elif "hybrid" in location:
        score += weights["hybrid_bonus"]

    # Clamp score to 0–100
    score = max(0, min(score, 100))

    job["score"] = score
    return score