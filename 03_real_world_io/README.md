# Module 3 — Real-world I/O

> 🧭  [◀ Data Science](../02_data_science/)  ·  [🏠 Course home](../README.md)  ·  [Web Scraping ▶](../04_webscraping/)

**Goal:** Move beyond toy data. Make polite, retry-aware HTTP calls against live APIs and query a SQL database from Python — the two ways real business data reaches your code (with an optional appendix for the API-less web: scraping).

**Estimated time:** 4–6 hours of focused study.

**Prerequisites:** Modules 1–2 (especially NB 4 — dictionaries and JSON — and NB 7 — pandas; the ETL and SQL examples build DataFrames).

```
   Public APIs               Your databases
   (NB 12 — HTTP)   ──►   (NB 13 — SQL/SQLite)
        │                        │
        └───────────┬────────────┘
                    ▼
   Now you can pull real data from anywhere —
    and appendix A1 covers pages with no API
             (scraping + Firecrawl).
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn / build |
|---|----------|--------|------------|---------------------------|
| 12 | `12_apis_and_http.ipynb` | ~45–60 min | Beginner / Intermediate | GET/POST with `requests`, status codes, auth headers, retry + backoff, pagination — capped by a weather ETL pipeline that writes `forecast.csv` |
| 13 | `13_sql_fundamentals.ipynb` | ~50–70 min | Beginner / Intermediate | The six core SQL clauses, aggregations, JOINs, CTEs, and a window-function tour on an in-memory SQLite database — plus when SQL beats pandas |

## Optional appendix at a glance

| Appendix | Notebook | ⏱ Time | Difficulty | Focus |
|----------|----------|--------|------------|-------|
| A1 | `A1_web_scraping_firecrawl.ipynb` | ~50–70 min | Intermediate | Optional, demo/reference style. DIY scraping with `requests` + BeautifulSoup (`robots.txt`, polite-scraper habits), then Firecrawl for LLM-ready markdown and structured extraction — runs fully offline via a local HTML fixture and a built-in Firecrawl mock |

## Notebook guides

### 12 · APIs, HTTP, and Real-World Data Fetching — `12_apis_and_http.ipynb`

One question threads the whole notebook: *"What's the weather going to do this week?"* You start by asking the Open-Meteo API for the current temperature in Berlin, and every new idea — status codes, headers, retries, pagination — earns its keep by making that same weather question more robust. By the last section the pieces snap together into a real **E**xtract–**T**ransform–**L**oad pipeline that pulls a 7-day forecast for four cities (Berlin, London, New York, Tokyo) into a tidy CSV. A second, fake API (JSONPlaceholder) is borrowed for two detours weather can't demonstrate: POST and pagination.

The mental model throughout: *talking to an API is like mailing a letter and waiting for the reply* — you format an envelope (method + URL + headers, plus a body for POST), `requests` is the courier, the server mails back a status code, headers, and body. The same patterns transfer directly to calling OpenAI, Anthropic, Stripe, Salesforce, or your internal data warehouse. Both APIs are free and keyless, and every networked cell degrades gracefully to a recorded response when there is no internet.

**Learning objectives:**
- Send `GET` and `POST` requests with the **`requests`** library
- Read **HTTP status codes** and handle errors gracefully
- Add **query parameters**, **headers**, and **bearer-token auth**
- Parse **JSON** responses into Python dicts and pandas DataFrames
- Handle **rate limits** and **flaky networks** with retry + backoff, and paginate multi-page result sets
- Build a small **ETL pipeline** that fetches API data and saves it locally

**Sections:**
1. The shape of every HTTP request
2. Setup
3. Your first GET request (incl. the request/response lifecycle, status codes, and headers up close)
4. HTTP status codes — what the server is telling you
5. Headers, authentication, and `User-Agent`
6. POST — sending data to a server
7. Retry with exponential backoff
8. Pagination — when one request isn't enough
9. Putting it together — a real ETL pipeline
10. Common pitfalls

**Practice:** 3 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 1 🎁 bonus mini-project (a weekly weather dashboard built on the §9 `fetch_forecast` helper).

**Files/datasets:** Writes **`forecast.csv`** (city, date, max/min temperature, precipitation — 7 days × 4 cities). The copy shipped in this folder is the output of a sample run, so you can see what the pipeline should produce. No input files needed.

### 13 · SQL Fundamentals with pandas — `13_sql_fundamentals.ipynb`

Every analyst job description asks for SQL, yet you can read most of the Python data-science internet without seeing a single `SELECT`. This notebook closes that gap. One dataset runs through everything: `support_ops` — customer support across five channels (Email, Chat, Phone, Web Form, Social) where an AI bot automates part of the load, with monthly ticket volume, automation rate, latency, satisfaction, and cost. That table is the question machine for the whole lesson: *which channels does the bot serve well, and which need help?*

The data (60 channel-month rows, built inline with a seeded RNG so the notebook is self-contained) is pushed into a SQLite database that lives entirely in RAM — SQLite ships with Python, so there is nothing to install. The mental model: *a SQL query is an assembly line* whose stations (`WHERE`, `GROUP BY`, `HAVING`, `SELECT`, …) don't run in the order you write them — §5 shows the real logical order, which explains half of SQL's confusing errors. Along the way you mirror queries in pandas and learn when each tool wins; the same SQL transfers (with minor syntax differences) to PostgreSQL, MySQL, BigQuery, and Snowflake.

**Learning objectives:**
- Connect to a **SQLite** database from Python and create tables from a DataFrame
- Write the **six SQL clauses** that cover ~95% of analytics work: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY`, `LIMIT`
- **Aggregate** with `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` (and filter buckets with `HAVING`)
- **Join** two tables on a key, and break complex queries into readable **CTEs** (`WITH …`)
- Move data between SQL and pandas with `read_sql` and `to_sql`
- Decide when SQL is the better tool than pandas (and vice versa)

**Sections:**
1. SQL in one slide
2. Setup — load the data into SQLite (built inline, pushed in via `to_sql`)
3. Your first SELECT
4. WHERE — filtering rows
5. Aggregations — the part that earns its keep (the *logical* clause order, `HAVING`)
6. Grouping by multiple columns and time
7. JOINs — bringing two tables together
8. CTEs — making complex queries readable
9. SQL vs pandas — when to use which
10. Tiny tour of window functions
11. Cleaning up

**Practice:** 4 ✋ quick exercises (plus a 🔮 predict-the-output checkpoint) · 5 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 1 🎁 bonus mini-project (a SQL-driven mini report combining a CTE with a JOIN).

**Files/datasets:** Nothing on disk — `sqlite3.connect(":memory:")` creates the database in RAM, holding `support_ops` plus a `channel_meta` lookup table (team leads, launch years) and a tiny `budgets` table for the JOIN section. The notebook shows `sqlite3.connect("ops.db")` as the one-line change that would persist it to a file.

## Appendix guide

### A1 · Web Scraping & Firecrawl — `A1_web_scraping_firecrawl.ipynb`

Notebook 12 pulled data from a clean JSON API — but most of the web has no API, and the data you want is trapped in HTML meant for human eyes. This optional, reference-style appendix has two halves: **do it yourself** (`requests` + **BeautifulSoup**, the rules of the road — `robots.txt`, ToS, rate limits, GDPR/PII — and the four polite-scraper habits: identify, throttle, cache, retry), then **let a service do the hard part** — **Firecrawl**, an API that turns any URL (including JavaScript-heavy, anti-bot pages) into clean, LLM-ready markdown or structured JSON in one call, the modern way to feed a RAG pipeline or an agent.

Everything runs offline: the hands-on BeautifulSoup cells parse a local HTML fixture (a mock bookshop catalogue page) instead of fetching a live site, and the Firecrawl cells use a small built-in mock that mimics the v2 SDK surface — install `firecrawl-py` and set `FIRECRAWL_API_KEY` to swap in the real service. The structured-extraction demo validates Firecrawl's JSON output with Pydantic (falling back to a dataclass if Pydantic isn't installed), and real SDK calls (scrape / crawl / map / search) are shown as commented reference code.

**Sections:**
1. When to scrape — and the rules you don't break
2. The anatomy of a scrape
3. Respect `robots.txt`
4. Polite scraping — the four habits
5. Where DIY scraping hurts
6. Firecrawl — the LLM-ready web API (incl. structured extraction into typed JSON)
7. Choosing your approach

**Practice:** 3 ✋ quick exercises · 2 🧪 exercises (unrated — appendices favour demo over drill) · no stretch exercises or mini-project.

**Files/datasets:** None — the HTML fixture and the Firecrawl mock live inline in the notebook.

## How these notebooks work

Every notebook runs **100% offline**. NB 12 talks to two free, keyless public APIs (Open-Meteo and JSONPlaceholder) when you have internet, and every networked cell wraps its call in `try/except` with a graceful fallback to a recorded response — plus "offline proof" cells that model the whole request/response lifecycle with plain dicts. NB 13 never touches the network at all (in-memory SQLite), and A1 scrapes a local HTML fixture and mocks the Firecrawl SDK. Each lesson opens with a Colab badge and a metadata line (estimated time, difficulty), then follows the course rhythm: ✋ Quick exercise (~2 min) checkpoints with collapsible 💡 solutions, end-of-lesson 🧪 practice exercises (⭐-rated, including a "Debug me 🐞"), 🧠 stretch exercises, and a 🎁 bonus mini-project in the core lessons.

## Where next

→ **Module 4 — Web Scraping** (`../04_webscraping/`) — get data *off the web* politely when there's no API, or
→ **Module 5 — Machine Learning** (`../05_machine_learning/17_sklearn_basics.ipynb`)

---

📝 **Finished this module?** Test yourself with the [Module 3 quiz](../quizzes/quiz_03_real_world_io.ipynb) — five questions, ~10 minutes.
