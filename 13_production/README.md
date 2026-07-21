# Module 13 — Production

> 🧭  [◀ DeepTab](../12_deeptab/)  ·  [🏠 Course home](../README.md)  ·  [CI/CD & Deployment ▶](../14_cicd/)

**Goal:** Take the code you've been writing in notebooks and graduate it into a packaged, tested, scheduled, observable Python project that another engineer can pick up.

**Estimated time:** 5–7 hours.

**Prerequisites:** Module 1 (functions). Helpful: NB 12 (HTTP), NB 31 (the toolkit we'll package).

```
                  ┌─────────────────────────────────────┐
                  │  src/ layout + pyproject.toml +     │
                  │  pytest + CLI entry point +         │
                  │  mypy / ruff / virtualenv           │
                  │            (NB 45)                  │
                  └─────────────────┬───────────────────┘
                                    │
                                    ▼
                              NB 46
                              Scheduling
                              cron / systemd /
                              GitHub Actions /
                              Prefect
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 45 | `45_from_notebook_to_project.ipynb` | ~50–70 min | Intermediate | `costkit` — a packaged, tested, importable library with a `src/` layout, `pyproject.toml`, pytest suite, and `argparse` CLI, built file-by-file in `/tmp` |
| 46 | `46_scheduling_orchestration.ipynb` | ~45–60 min | Intermediate | A weekly support-ops report that runs itself — task function, scheduler loop, idempotency, retries, and alerts, plus ready-to-ship cron / systemd / GitHub Actions / Prefect snippets |

## Notebook guides

### 45 · From Notebook to Project — `45_from_notebook_to_project.ipynb`

A notebook is a great place to *figure things out* and a terrible place to *deploy* from. This lesson follows one concrete story the whole way through: the loose helpers you've been copy-pasting between notebooks (`call_cost`, `safe_get`, `parse_number`) get assembled — in front of you, on the real filesystem under `/tmp` — into a shippable package called **`costkit`**, a cost toolkit for LLM usage. The mental model is "from a messy workbench to a labelled toolbox": every function gets a drawer (`cost.py`, `parsing.py`), the lid (`__init__.py`) lists the public API, and anyone can carry the whole box to CI, a server, or a teammate's laptop.

By the last cell the project has a standard folder layout, a `pyproject.toml` with declared dependencies, real pytest tests (run in-process from the notebook), a `costkit total ...` CLI a scheduler can invoke, a README and `.gitignore`, and mypy/ruff configuration — plus a detour into what `import` actually does (modules, packages, `sys.path`) and the reproducible virtualenv workflow.

> 🎯 **The rule of thumb.** Once *two* notebooks copy-paste the same function, move that function into a project. Once *one* notebook needs to be re-run on a schedule, build the project around it.

**Learning objectives:**
- Lay out a Python project with the standard `src/` layout — and decide what `__init__.py` exposes vs. keeps private
- Write a `pyproject.toml` that declares your package and its dependencies
- Create a virtualenv and `pip install` your project in editable mode
- Write pytest tests with fixtures and parametrize
- Build a CLI with `argparse` (or `typer`)
- Run type checks with mypy and linting with ruff

**Sections:**
1. Why graduate from a notebook?
2. The standard layout — `src/` vs flat
3. Build the project — for real, in `/tmp`
4. Write the package modules (what `import` actually does; module vs package)
5. The project metadata — `pyproject.toml`
6. The CLI
7. The tests
8. README + `.gitignore`
9. Install the package and run the tests
10. Type hints and linting — mypy & ruff
11. The virtualenv workflow
12. Where to go next — the rest of "production Python"

**Practice:** 3 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project: a `monthly_report` entry point.

**Tools covered:** `src/` layout · `pyproject.toml` (setuptools) · `pytest` (`approx`, `raises`, `parametrize`) · `argparse` (with `typer`/`click` as the step-up) · `mypy` · `ruff` · `venv` + editable installs.

### 46 · Scheduling and Automation Orchestration — `46_scheduling_orchestration.ipynb`

You have a package (NB 45); the last mile of automation is making it run **without a human present**. One concrete job carries the whole notebook: a **weekly support-ops report** that every Monday at 6 a.m. fetches last week's ticket numbers, computes the share handled automatically, writes a summary file, and pings the team in Slack — the same scenario Capstone A (NB 47) picks up later. The mental model is "hire a night-shift robot": it needs a job description (the task function), a shift schedule (cron / systemd / Prefect), the habit of writing down what it did (logging), and the sense to phone you when something breaks (alerts) — without re-doing work it already finished (idempotency).

Starting from a bare task function, the notebook layers on each production essential in turn — an in-process scheduling loop you can watch tick, idempotency, retries with backoff, failure notifications — then compares the four hosting options with copy-paste snippets, dissects how cron reads `0 9 * * 1-5` (proved offline with a tiny `matches(cron_expr, dt)` function), and assembles everything into a production-shape skeleton with a closing tour of common pitfalls. Picking a host boils down to the notebook's decision tree:

```
                          ┌── on your laptop, low-frequency ──→ cron
                          │
   Where does the task    ┼── on a Linux server, low-frequency ──→ systemd timer
   actually run?          │
                          ├── on GitHub already, weekly / on-PR ──→ GitHub Actions
                          │
                          └── multiple tasks, dependencies between them ──→ Prefect / Airflow / Dagster
```

**Learning objectives:**
- Write a task function that's safe to call repeatedly
- Use the `schedule` library for in-process scheduling (no extra infrastructure)
- Add structured logging so a failed 3 a.m. run leaves a clear trace
- Make tasks idempotent and add retries with backoff at the task level
- Wire up email / Slack / webhook notifications for failures
- Pick between cron, systemd, GitHub Actions, and Prefect/Airflow

**Sections:**
1. What does "automation" actually mean? (task function / scheduler / observability)
2. The task function — a runnable unit of work
3. In-process scheduling with `schedule`
4. Idempotency — safe to re-run
5. Retries with backoff — survive the flaky internet
6. Notifications — fail loud
7. Picking a host — cron, systemd, GitHub Actions, Prefect (incl. how cron parses `0 9 * * 1-5`, proved offline)
8. Logging — what to record
9. Putting it together — the production-shape skeleton
10. Common pitfalls

**Practice:** 4 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a lock-file guard and a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: circuit breaker, chained tasks with file-based handoff, exponential backoff, cron pretty-printer) · 🎁 bonus mini-project: a daily metrics digest.

**Tools covered:** the `schedule` library (re-implemented in ~20 lines for offline runnability) · `logging` · a retry-with-backoff wrapper · Slack incoming-webhook alerts · cron · systemd `.service`/`.timer` units · GitHub Actions workflow YAML · Prefect flows (Airflow/Dagster compared).

## How these notebooks work

Both lessons run **100% offline**, like every notebook in this course: NB 45 creates its package on the local filesystem and runs pytest in-process, while NB 46 stands in a 20-line `TinyScheduler` for the `schedule` library and proves cron expressions with pure Python — no server, network, or scheduler daemon required. Each notebook opens with a Colab badge and a time/difficulty line, drops "✋ Quick exercise (~2 min)" checkpoints with collapsible solutions as you go, and closes with ⭐-rated 🧪 practice exercises (including a "Debug me 🐞"), 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways, and a self-assessment checklist.

## Where next

→ **Module 14 — CI/CD & Deployment** (`../14_cicd/README.md`) — you learned packaging and scheduling here; Module 14 takes the same app through Docker, pipelines, and a live server. Then the **Capstones** (`../15_capstones/47_capstone_analytics.ipynb`).

---

📝 **Finished this module?** Test yourself with the [Module 13 quiz](../quizzes/quiz_13_production.ipynb) — five questions, ~10 minutes.
