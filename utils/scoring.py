def score_job(job, prefs):
    score = 0
    title = job.get("job_title", "").lower()
    location = job.get("location", "").lower()
    description = (job.get("raw_description") or "").lower()
    skills = [s.lower() for s in job.get("skills", [])]
    weights = prefs["scoring_weights"]

    # === 1. Title-based frontend relevance (0–80) ===
    tech_score = 0
    if "react" in title:
        tech_score += weights["react_title"]
    if "frontend" in title:
        tech_score += weights["frontend_title"]
    if "javascript" in title:
        tech_score += weights["javascript_title"]
    if "ui" in title or "web" in title:
        tech_score += weights["ui_or_web_title"]
    tech_score = min(tech_score, weights["max_tech_score"])
    score += tech_score

    # === 2. Description-based signals (0–30) ===
    if "react" in description:
        score += weights["react_description_bonus"]
    if "frontend" in description:
        score += weights["frontend_description_bonus"]

    # === 3. Skill-based scoring (0–40) ===
    core_skills = prefs["core_frontend_skills"]
    skill_hits = sum(1 for s in core_skills if s in skills)
    score += min(skill_hits * weights["per_core_skill"], weights["max_core_skill_score"])

    # === 4. Seniority (0–20) ===
    if any(term in title for term in ["junior", "entry", "associate"]):
        score += weights["junior_bonus"]
    elif "mid" in title:
        score += weights["mid_bonus"]

    # === 5. Location (0–20) ===
    if any(city in location for city in prefs["primary_cities"]):
        score += weights["primary_city_bonus"]
    elif any(city in location for city in prefs["secondary_cities"]):
        score += weights["secondary_city_bonus"]

    # === 6. Work arrangement (0–15) ===
    if "remote" in location:
        score += weights["remote_bonus"]
    elif "hybrid" in location:
        score += weights["hybrid_bonus"]

    # === 7. Low relevance penalty (only for truly irrelevant jobs) ===
    frontend_terms = ["react", "frontend", "javascript", "ui", "web"]
    has_relevance = (
        any(term in title for term in frontend_terms)
        or any(term in description for term in frontend_terms)
        or any(s in skills for s in frontend_terms)
    )
    if not has_relevance:
        score -= weights["low_relevance_penalty"]

    # === 8. Floor: no negative scores ===
    if score < 0:
        score = 0

    job["score"] = score
    return score