from chains.job_parser import parse_job_description
from utils.filtering import filter_jobs
from utils.ranking import rank_jobs
from utils.scoring import score_job
from config.preferences import USER_PREFERENCES


# -----------------------------
# Test job descriptions
# -----------------------------
job_descriptions = [
    """
    Junior React Developer needed in Southlake. 
    Hybrid role. Salary: $85,000 - $95,000.
    Required skills: JavaScript, React, HTML, CSS.
    Preferred: Next.js, Tailwind.
    Experience: 1-2 years.
    Benefits: Health insurance, 401k match, PTO.
    """,

    """
    Backend Java Engineer - Irving.
    On-site only. Salary: $110,000.
    Required skills: Java, Spring Boot, SQL.
    Experience: 4+ years.
    """,

    """
    Frontend Engineer (TypeScript/React) - Remote.
    Salary: $75,000.
    Required skills: TypeScript, React, HTML, CSS.
    Preferred: Firebase.
    Experience: 2 years.
    Benefits: PTO.
    """,

    """
    Web Developer - The Colony.
    Hybrid. Salary: $65,000.
    Required skills: HTML, CSS, JavaScript.
    Experience: 1 year.
    """
]


# -----------------------------
# Parse all jobs
# -----------------------------
parsed_jobs = [parse_job_description(jd) for jd in job_descriptions]

print("\n--- PARSED JOBS ---")
for job in parsed_jobs:
    print(job)
    print()


# -----------------------------
# Filter out disqualified jobs
# -----------------------------
filtered_jobs = filter_jobs(parsed_jobs, USER_PREFERENCES)

print("\n--- AFTER FILTERING ---")
for job in filtered_jobs:
    print(job["job_title"], "-", job["location"])
print()


# -----------------------------
# Rank remaining jobs
# -----------------------------
ranked_jobs = rank_jobs(filtered_jobs, USER_PREFERENCES)

print("\n--- RANKED JOBS ---")
for job in ranked_jobs:
    s = score_job(job, USER_PREFERENCES)
    print(f"{job['job_title']} ({job['location']}) → Score: {s}")