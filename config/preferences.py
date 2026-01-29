USER_PREFERENCES = {
    # === Disqualifiers ===
    "disqualify_title_keywords": [
        "senior", "lead", "principal", "architect", "manager", "backend", "cybersecurity", "cyber security", "it"
    ],
    "disqualify_tech": [
        "c++", "c#", ".net", "asp.net", "java", "go", "rust", "python"
    ],

    # === Tech Keywords (for is_tech_job) ===
    "tech_keywords": [
        "developer", "engineer", "software", "frontend", "front end",
        "fullstack", "full stack", "react", "javascript", "typescript",
        "web developer", "programmer"
    ],

    # === Skill Extraction ===
    "skill_keywords": [
    "react", "javascript", "typescript", "html", "css",
    "node", "python", "aws", "docker", "redux",
    "frontend", "ui", "web", "api"
    ],


    # === Role Type Inference ===
    "frontend_keywords": [
        "react", "frontend", "javascript", "typescript", "html", "css"
    ],
    "backend_keywords": [
        "backend", "api", "node", "django", "flask", "spring", "java"
    ],

    # === Seniority Inference ===
    "seniority_keywords": {
        "junior": ["junior", "entry level", "entry-level", "graduate", "associate", "assistant"],
        "mid": ["mid", "intermediate"],
        "senior": ["senior", "lead", "principal", "staff", "architect", "sr", "sr."]
    },
    
    # === Commute Scoring ===
    "primary_cities": [
        "watauga", "keller", "north richland hills", "haltom city",
        "saginaw", "hurst", "euless", "bedford", "colleyville",
        "grapevine", "southlake"
    ],
    "secondary_cities": [
        "trophy club", "roanoke", "flower mound", "lewisville",
        "coppell", "the colony", "carrollton", "highland village",
        "frisco", "plano"
    ],

    # === Allowed Cities (for filtering) ===
    "allowed_cities": [
        "watauga", "keller", "north richland hills", "haltom city",
        "saginaw", "hurst", "euless", "bedford", "colleyville",
        "grapevine", "southlake", "trophy club", "roanoke",
        "flower mound", "lewisville", "coppell", "the colony",
        "carrollton", "highland village", "frisco", "plano",
        "dallas", "fort worth", "tarrant county", "dfw"
    ],

    # === Preferred Seniority (for scoring) ===
    "preferred_seniority": ["junior", "entry-level", "associate"],

    # === Core Frontend Stack (optional scoring bonus) ===
    "core_frontend_skills": ["javascript", "typescript", "react", "html", "css"],

    # === Bonus Skills (optional scoring bonus) ===
    "bonus_skills": ["firebase", "next.js", "tailwind", "bootstrap"],

    # === Scoring Weights (0–100 scale) ===
    "scoring_weights": {
    # Title tech relevance (max 80)
    "react_title": 50,
    "frontend_title": 40,
    "javascript_title": 25,
    "ui_or_web_title": 15,
    "max_tech_score": 80,

    # Description bonuses (max 30)
    "react_description_bonus": 15,
    "frontend_description_bonus": 15,

    # Skill-based scoring (max 40)
    "per_core_skill": 10,
    "max_core_skill_score": 40,

    # Seniority (max 20)
    "junior_bonus": 20,
    "mid_bonus": 5,

    # Location (max 20)
    "primary_city_bonus": 20,
    "secondary_city_bonus": 10,

    # Work arrangement (max 15)
    "remote_bonus": 15,
    "hybrid_bonus": 8,

    # Penalties
    "low_relevance_penalty": 25
    },
}
