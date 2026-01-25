USER_PREFERENCES = {
    # === Disqualifiers ===
    "disqualify_title_keywords": [
        "senior", "lead", "principal", "architect", "manager", "backend"
    ],
    "disqualify_tech": [
        "c++", "c#", ".net", "asp.net", "java", "go", "rust"
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
        "node", "python", "aws"
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

    # === Scoring Weights (0–100 scale) ===
    "scoring_weights": {
        # React / JS / Frontend (max 50)
        "react_title": 30,
        "javascript_title": 20,
        "frontend_title": 20,
        "ui_or_web_title": 10,
        "max_tech_score": 50,

        # Seniority (max 20)
        "junior_bonus": 20,
        "mid_bonus": 5,

        # Location (max 20)
        "primary_city_bonus": 20,
        "secondary_city_bonus": 10,
        "dallas_penalty": -20,

        # Tech penalties (max -20)
        "java_penalty": -20,
        "spring_dotnet_penalty": -10,

        # Work arrangement (max 10)
        "remote_bonus": 10,
        "hybrid_bonus": 5
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
    "bonus_skills": ["firebase", "next.js", "tailwind", "bootstrap"]
}
