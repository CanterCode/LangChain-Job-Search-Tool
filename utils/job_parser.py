import re

SKILL_KEYWORDS = [
    "react", "javascript", "typescript", "html", "css",
    "node", "python", "aws",
]

FRONTEND_KEYWORDS = ["react", "frontend", "javascript", "typescript", "html", "css"]
BACKEND_KEYWORDS = ["backend", "api", "node", "django", "flask", "spring", "java"]

SENIORITY_KEYWORDS = {
    "junior": ["junior", "entry level", "entry-level", "graduate", "associate", "assistant"],
    "mid": ["mid", "intermediate"],
    "senior": ["senior", "lead", "principal", "staff", "architect"],
}

def extract_years_experience(text: str) -> int | None:
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    if match:
        return int(match.group(1))
    return None

def extract_skills(text: str) -> list[str]:
    text_lower = text.lower()
    return [skill for skill in SKILL_KEYWORDS if skill in text_lower]

def infer_seniority(title: str, description: str) -> str:
    text = f"{title} {description}".lower()
    for level, keywords in SENIORITY_KEYWORDS.items():
        if any(k in text for k in keywords):
            return level
    return "unknown"

def infer_role_type(text: str) -> str:
    t = text.lower()
    if any(k in t for k in FRONTEND_KEYWORDS) and not any(k in t for k in BACKEND_KEYWORDS):
        return "frontend"
    if any(k in t for k in BACKEND_KEYWORDS) and not any(k in t for k in FRONTEND_KEYWORDS):
        return "backend"
    if any(k in t for k in FRONTEND_KEYWORDS) and any(k in t for k in BACKEND_KEYWORDS):
        return "fullstack"
    return "unknown"

def parse_job(job: dict) -> dict:
    title = job.get("title", "")
    description = job.get("description", "")
    location = job.get("location", "")
    company = job.get("company", "")
    url = job.get("url", "")

    text = f"{title}\n{description}"

    years = extract_years_experience(text)
    skills = extract_skills(text)
    seniority = infer_seniority(title, description)
    role_type = infer_role_type(text)

    return {
        "job_title": title,
        "company": company,
        "location": location,
        "url": url,
        "skills": skills,
        "years_experience": years,
        "seniority": seniority,
        "role_type": role_type,
        "raw_description": description,
    }