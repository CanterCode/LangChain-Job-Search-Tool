import re

def extract_salary_number(salary_str):
    if not salary_str:
        return None
    nums = re.findall(r"\d+", salary_str.replace(",", ""))
    return int(nums[-1]) if nums else None


def extract_years(exp_str):
    if not exp_str:
        return None
    nums = re.findall(r"\d+", exp_str)
    return int(nums[0]) if nums else None


def score_job(job, prefs):
    score = 0
    title = job.get("job_title", "").lower()
    skills = [s.lower() for s in job.get("required_skills", [])]
    location = job.get("location", "").lower()

    # 1. Seniority
    if any(s in title for s in prefs["preferred_seniority"]):
        score += 40

    # 2. Frontend role
    if any(k in title for k in ["frontend", "react", "javascript", "ui", "web"]):
        score += 40

    # 3. Core frontend skills
    for skill in prefs["core_frontend_skills"]:
        if skill in skills:
            score += 10

    # 4. Bonus skills
    for bonus in prefs["bonus_skills"]:
        if bonus in skills:
            score += 3

    # 5. Experience requirement
    years = extract_years(job.get("required_experience", ""))
    if years is not None:
        if years <= prefs["max_experience_years"]:
            score += 20
        else:
            score -= 20

    # 6. Salary scoring
    salary = extract_salary_number(job.get("salary"))
    if salary:
        if salary >= prefs["min_salary"]:
            score += 10
        if salary >= 80000:
            score += prefs["salary_bonus_80k"]
        if salary >= 90000:
            score += prefs["salary_bonus_90k"]

    # 7. Work arrangement
    if "hybrid" in location:
        score += prefs["hybrid_bonus"]
    elif "remote" in location:
        score += prefs["remote_bonus"]

    # 8. Benefits scoring
    raw_benefits = job.get("benefits") or []
    benefits = [b.lower() for b in raw_benefits]
    if benefits:
        score += prefs["benefit_bonus_any"]
        for good in prefs["benefit_bonus_good"]:
            if good in benefits:
                score += 5

    # 9. Commute scoring (UPDATED)
    for city in prefs["primary_cities"]:
        if city in location:
            score += prefs["primary_city_bonus"]

    for city in prefs["secondary_cities"]:
        if city in location:
            score += prefs["secondary_city_bonus"]

    return score