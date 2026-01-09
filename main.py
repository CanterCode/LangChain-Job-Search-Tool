from chains.job_parser import parse_job_description

job_description = """
We are seeking a Junior Python Developer to join our remote-first engineering team.
You will work on backend APIs, data pipelines, and automation tools.
Required skills: Python, SQL, REST APIs.
Preferred: AWS, Docker, CI/CD.
Experience: 1+ years.
Benefits include health insurance, 401k match, and unlimited PTO.
"""

result = parse_job_description(job_description)

print(result)
