# Module 6 — Production

**Goal:** Take the code you've been writing in notebooks and graduate it into a packaged, scheduled, observable, configurable Python project that another engineer can pick up.

**Estimated time:** 5–7 hours.
**Prerequisites:** Module 1 (functions). Helpful: NB 7 (HTTP), NB 21 (the toolkit we'll package).

```
                  ┌─────────────────────────────────────┐
                  │  src/ layout + pyproject.toml +      │
                  │  pytest + CLI entry points           │
                  │           (NB 23)                    │
                  └─────────────────┬───────────────────┘
                                    │
                       ┌────────────┴────────────┐
                       ▼                          ▼
                 NB 24                       NB 25
                 Scheduling                  Config &
                 cron / systemd /            secrets management
                 GitHub Actions /            yaml + dotenv +
                 Prefect                     12-factor app
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 23 | `23_from_notebook_to_project.ipynb` | A packaged, tested, importable `costkit` library |
| 24 | `24_scheduling_orchestration.ipynb` | Production-shape automation wrapper with retries + alerts |
| 25 | `25_configuration_secrets.ipynb` | YAML configs, dotenv, dev/staging/prod patterns |

## What "production-ready" actually means here

You aren't deploying to a Kubernetes cluster in this course. You *are* learning the discipline that makes that step trivial when you get there:

- **A versioned package** with declared dependencies (`pyproject.toml`).
- **A tested codebase** with `pytest` (and a CI workflow that runs it).
- **A CLI** that a scheduler can invoke without surgery.
- **Configuration in files, secrets in env vars** — never hard-coded.
- **A retry-with-backoff wrapper** so a 3 a.m. failure doesn't ruin Monday.
- **Idempotent tasks** that survive duplicate runs.

## Where next

→ **Module 7 — Capstones** (`../07_capstones/26_capstone_analytics.ipynb`)
