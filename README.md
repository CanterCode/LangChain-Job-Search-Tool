# Job Search Tool

A developer-focused job search automation engine that fetches, filters, and ranks software engineering jobs based on strict, configurable preferences. The system is built to be location-aware, frontend-focused, and extensible for future scrapers and a UI.

---

## 🚀 Project Overview

**This project automates the job search pipeline:**
- Fetch jobs from external sources (currently Adzuna).
- Parse and normalize raw job data into a consistent internal format.
- Filter aggressively based on the user's preferences (location, tech stack, seniority, etc.).
- Score and rank the remaining jobs using a modular scoring engine.
- Display the top matches in a clean output.
**The design emphasizes:**
- Real-world usefulness for an actual job search.
- Clean, modular architecture suitable for a portfolio.
- Easy tuning via centralized configuration.


---

## 🧱 Tech Stack

- Language: Python
- Data Source: Adzuna API (current primary source)
- Core Modules:
    - Fetching: API client for job retrieval
    - Parsing: Normalization and enrichment of raw job data
    - Filtering: Rule-based elimination of irrelevant roles
    - Scoring: Weighted scoring based on tech, location, and seniority
    - Ranking: Sorting and deduplication of final results
- Configuration: Centralized in config/preferences.py
- Interface: Command-line via main.py

---

## ✅ Current Features

**Fetching**
- Pulls job listings from the Adzuna API using multiple keyword queries.
- Combines all results into a single dataset.

**Parsing**
- Normalizes raw job data into a consistent structure.
- Extracts fields like title, company, location, description, seniority, role type, and experience.

**Filtering**
- Removes jobs that don’t match strict criteria:
- Prints a full breakdown showing why each job was filtered out.

**Scoring**
- Assigns a relevance score based on preferences

**Ranking**
- Deduplicates similar listings.
- Sorts jobs by score (highest first).
- Outputs clean, readable top matches with job posting URL.

---

## 📌 Roadmap & Future Enhancements

**Additional Data Sources**
- [ ] Add an Indeed scraper (likely via Playwright or similar).
- [ ] Explore LinkedIn or ZipRecruiter integration (where feasible).
- [ ] Add support for other APIs or RSS/JSON feeds.

**Frontend UI**
- [ ] Build a minimal web UI (React Next.js frontend).
- [ ] Display ranked jobs with tags.
- Filters (score threshold, city, remote-only, etc.)
- [ ] Add “Save” and “Applied” states for tracking.