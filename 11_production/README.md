# Module 11 — Production

**Goal:** Take the code you've been writing in notebooks and graduate it into a packaged, scheduled, observable, configurable Python project that another engineer can pick up.

**Estimated time:** 5–7 hours.
**Prerequisites:** Module 1 (functions). Helpful: NB 12 (HTTP), NB 24 (the toolkit we'll package).

```
                  ┌─────────────────────────────────────┐
                  │  src/ layout + pyproject.toml +      │
                  │  pytest + CLI entry points +         │
                  │  config & secrets (folded in)        │
                  │            (NB 39)                   │
                  └─────────────────┬───────────────────┘
                                    │
                                    ▼
                              NB 40
                              Scheduling
                              cron / systemd /
                              GitHub Actions /
                              Prefect
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 22 | `39_from_notebook_to_project.ipynb` | A packaged, tested, importable `costkit` library — including YAML configs, dotenv, and dev/staging/prod patterns (config & secrets folded in here rather than split into a separate notebook). |
| 23 | `40_scheduling_orchestration.ipynb` | Production-shape automation wrapper with retries + alerts |

## What "production-ready" actually means here

You aren't deploying to a Kubernetes cluster in this course. You *are* learning the discipline that makes that step trivial when you get there:

- **A versioned package** with declared dependencies (`pyproject.toml`).
- **A tested codebase** with `pytest` (and a CI workflow that runs it).
- **A CLI** that a scheduler can invoke without surgery.
- **Configuration in files, secrets in env vars** — never hard-coded.
- **A retry-with-backoff wrapper** so a 3 a.m. failure doesn't ruin Monday.
- **Idempotent tasks** that survive duplicate runs.

## Where next

→ **Module 13 — Capstones** (`../13_capstones/41_capstone_analytics.ipynb`)
