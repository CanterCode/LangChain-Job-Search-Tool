from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional


# -----------------------------
# 1. Define the JSON Schema
# -----------------------------
class JobDescriptionSchema(BaseModel):
    # Required fields
    job_title: str = Field(..., description="The job title")
    required_skills: List[str] = Field(..., description="List of required skills")
    responsibilities: List[str] = Field(..., description="List of job responsibilities")
    required_experience: str = Field(..., description="Experience requirement like '3+ years'")
    location: str = Field(..., description="Job location or remote status")

    # Optional fields
    company: Optional[str] = None
    seniority_level: Optional[str] = None
    preferred_skills: Optional[List[str]] = None
    experience_level: Optional[str] = None
    tech_stack: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    benefits: Optional[List[str]] = None


# -----------------------------
# 2. Create the parser
# -----------------------------
parser = JsonOutputParser(pydantic_object=JobDescriptionSchema)


# -----------------------------
# 3. Build the chain
# -----------------------------
def create_job_parser_chain():
    """
    Creates a production-ready job description parser that outputs validated JSON.
    """

    prompt = PromptTemplate(
        template="""
You are an expert job description parser.

Extract the following fields from the job description and return ONLY valid JSON that matches this schema:

{format_instructions}

Job Description:
{job_description}
""",
        input_variables=["job_description"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    model = ChatOpenAI(model="gpt-4o-mini")

    return prompt | model | parser


# -----------------------------
# 4. Wrapper with retry logic
# -----------------------------
def parse_job_description(job_description: str):
    """
    Runs the parser with retry logic and safe fallback.
    """

    chain = create_job_parser_chain()

    try:
        return chain.invoke({"job_description": job_description})

    except Exception:
        # Retry with a stricter instruction
        retry_prompt = f"""
Return ONLY valid JSON. No explanations. No markdown. Fix any formatting issues.

Job Description:
{job_description}
"""

        try:
            return chain.invoke({"job_description": retry_prompt})

        except Exception:
            # Final fallback — return empty structure
            return JobDescriptionSchema(
                job_title="",
                required_skills=[],
                responsibilities=[],
                required_experience="",
                location="",
                company=None,
                seniority_level=None,
                preferred_skills=None,
                experience_level=None,
                tech_stack=None,
                keywords=None,
                benefits=None,
            ).dict()