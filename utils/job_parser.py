import re

def extract_years_experience(text: str) -> int | None:
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    return int(match.group(1)) if match else None

def is_tech_job(text: str, prefs: dict) -> bool:
    t = text.lower()
    return any(keyword in t for keyword in prefs["tech_keywords"])

def infer_seniority(title: str, description: str, prefs: dict) -> str:
    text = f"{title} {description}".lower()
    for keyword in prefs["seniority_keywords"]["senior"]:
        if keyword in text:
            return "senior"
    for keyword in prefs["seniority_keywords"]["junior"]:
        if keyword in text:
            return "junior"
    for keyword in prefs["seniority_keywords"]["mid"]:
        if keyword in text:
            return "mid"
    return "unknown"

def infer_role_type(text: str, prefs: dict) -> str:
    t = text.lower()
    frontend = any(k in t for k in prefs["frontend_keywords"])
    backend = any(k in t for k in prefs["backend_keywords"])
    if frontend and not backend:
        return "frontend"
    if backend and not frontend:
        return "backend"
    if frontend and backend:
        return "fullstack"
    return "unknown"

def parse_job(job: dict, prefs: dict) -> dict:
    title = job.get("title", "")
    description = job.get("description", "")
    location = job.get("location", "")
    company = job.get("company", "")
    url = job.get("url", "")

    text = f"{title}\n{description}".lower()

    extracted_skills = [kw for kw in prefs["skill_keywords"] if kw in text]

    api_skills = job.get("skills") or []
    skills = api_skills if api_skills else extracted_skills

    return {
        "job_title": title,
        "company": company,
        "location": location,
        "url": url,
        "skills": skills,
        "years_experience": extract_years_experience(text),
        "seniority": infer_seniority(title, description, prefs),
        "role_type": infer_role_type(text, prefs),
        "is_tech_job": is_tech_job(text, prefs),
        "raw_description": description,
    }