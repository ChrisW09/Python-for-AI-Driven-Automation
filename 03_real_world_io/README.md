# Module 2 — Real-world I/O

**Goal:** Move beyond toy data. Make HTTP calls against live APIs, query a SQL database from Python, and validate structured data with Pydantic.

**Estimated time:** 4–6 hours of focused study.
**Prerequisites:** Module 1 (especially NB 4 — dictionaries and JSON).

```
   Public APIs         Your databases + schemas
   (NB 12 — HTTP)  ──►  (NB 13 — SQL + Pydantic)
        │                    │
        └────────────────────┘
                  │
                  ▼
   Now you can pull real data from anywhere
        and trust it before using it.
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 7 | `12_apis_and_http.ipynb` | A weather-data ETL pipeline against a live API |
| 8 | `13_sql_fundamentals.ipynb` | A SQL-driven channel report (joins, CTEs, window functions) — including Pydantic-validated rows where they enter Python (originally planned as a standalone NB 9; folded in here). |

## Why this module matters

Up to Module 1 every dataset was generated inline. From now on you'll *pull* data — from APIs, from databases, from LLMs — and that data **will be messy**. This module gives you the three skills that let you handle it without your code crashing every other Tuesday:

1. **HTTP** — make polite, retry-aware requests with timeouts and proper error handling.
2. **SQL** — read data straight out of a database with `SELECT … GROUP BY` (and know when SQL beats pandas).
3. **Validation** — refuse bad data at the boundary with Pydantic; everything downstream stays clean.

## Where next

→ **Module 3 — Data Science** (`../02_data_science/07_pandas_fundamentals.ipynb`)
