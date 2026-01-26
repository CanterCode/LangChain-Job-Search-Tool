def score_job(job, prefs):
    score = 0
    title = job.get("job_title", "").lower()
    location = job.get("location", "").lower()
    weights = prefs["scoring_weights"]

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
    
    description = (job.get("description") or "").lower()

    if "frontend" in description and "frontend" not in title:
        score += weights.get("frontend_description_bonus", 5)

    if "junior" in description and not any(term in title for term in ["junior", "entry", "associate"]):
        score += weights.get("junior_description_bonus", 5)

    if "junior" in title or "entry" in title or "associate" in title:
        score += weights["junior_bonus"]
    elif "mid" in title:
        score += weights["mid_bonus"]

    if any(city in location for city in prefs["primary_cities"]):
        score += weights["primary_city_bonus"]
    elif any(city in location for city in prefs["secondary_cities"]):
        score += weights["secondary_city_bonus"]

    if "remote" in location:
        score += weights["remote_bonus"]
    elif "hybrid" in location:
        score += weights["hybrid_bonus"]
        
    has_relevance = any(term in title for term in ["react", "javascript", "frontend", "ui", "web", "react"]) \
    or "frontend" in description \
    or "junior" in description

    if not has_relevance:
        score -= weights.get("low_relevance_penalty", 10)


    job["score"] = score
    return score