# Module 0 — Onboarding

> 🧭  [🏠 Course home](../README.md)  ·  [Foundations ▶](../01_foundations/)

**Goal:** in 30–45 minutes, give you a clear map of the course, a working Python environment, and a mental model of *how to study* the rest of the course.

**Estimated time:** ~40 minutes (~20 + ~5 + ~15 across the three notebooks).

**Prerequisites:** none — this is the entry point. You only need a way to run notebooks: Google Colab (free Google account) or a local Python + Jupyter/VS Code setup; `00_master_onboarding.ipynb` walks you through both.

```
        ┌────────────────────────────────┐
        │  Master onboarding (00)        │   ← you start here (env check + the spiral)
        └──────────────┬─────────────────┘
                       │
        ┌──────────────┴─────────────────┐
        │  See it work (00c)             │   ← 5-min offline demo of what you'll build
        └──────────────┬─────────────────┘
                       │
        ┌──────────────┴─────────────────┐
        │  Course overview (00b)         │   ← the full map + interactive time estimator
        └──────────────┬─────────────────┘
                       │
        ┌──────────────┴─────────────────┐
        │  Module 1 — Foundations        │
        └────────────────────────────────┘
```

## Notebooks at a glance

| Notebook | ⏱ Time | Difficulty | What it's for |
|---|---|---|---|
| **`00_master_onboarding.ipynb`** | ~20 min | — | Course philosophy, the recommended **spiral** order, the 5-step study loop, learning paths, environment check. The "you are here" notebook. |
| **`00c_see_it_work.ipynb`** | ~5 min | — | An **offline** demo of the finished shapes — AI triage, RAG, a KPI snapshot — so you see the destination before the Python begins. |
| **`00b_course_overview.ipynb`** | ~15 min | — | The companion overview: module-map diagram, per-notebook time budgets (read / practice / stretch / bonus), five learning paths, interactive time estimator, study habits that actually work. |

*(No difficulty ratings here — these are orientation notebooks, not lessons.)*

## Notebook guides

### `00_master_onboarding.ipynb` — Master Onboarding

The first notebook of the course. It explains what the course is (and *is not*), how the modules fit together, and how to study each notebook effectively as a self-learner — then verifies that your environment actually works. It covers both ways to run the material (Google Colab with a free account, or local Jupyter / VS Code) and lays out the recommended **spiral** route: see the destination first (`00c`), build the skills bottom-up (Modules 1–8), build the real thing (Modules 9–14), then synthesise (capstones + Business AI).

Its core teaching device is the **5-step loop** you'll apply to every notebook — *Read → Run → Try → Tweak → Predict* ("5 minutes of struggle beats 5 hours of passive reading"). Two things happen *in code*: an **environment check** that reports your Python version and ticks off the required packages (numpy, pandas, matplotlib, seaborn, scikit-learn) plus optional ones you'll need later (requests, statsmodels, pytest) — you want it to print `✅ Setup looks good!` — and a tiny self-test proving you can run Python right now. Section 5 matches you to one of five learning paths (complete beginner ~115h · analyst ~43h · developer ~55h · ML practitioner ~34h · manager ~10h), and a troubleshooting section covers the usual first-day snags.

**Sections:** How to run these notebooks · The recommended order — a quick spiral · 1 The course in one paragraph · 2 Where the course sits · 3 How to study a notebook — the 5-step loop · 4 The modules at a glance · 5 Pick a learning path · 6 Environment check · 7 A tiny self-test · 8 A note on style · 9 What this course is *not* · 10 Troubleshooting · 11 Which file do you open next?

**Practice:** none — orientation notebook. (It *introduces* the ✋ / 🧪 / 🧠 / 🎁 exercise markers you'll meet from Module 1 on.)

### `00c_see_it_work.ipynb` — See It Work: a 5-minute tour of what you'll build

Optional but recommended *before* the Python foundations: a five-minute, run-the-cells-and-watch demo of the finished shapes you'll spend the course building. Three mini-demos run end to end: an AI **triages free-form customer feedback** into structured tags, a tiny **RAG** pipeline answers a question grounded in your own policy documents instead of making things up, and the same ticket data becomes a **business KPI snapshot** — first as numbers, then as a one-glance bar chart.

The notebook's explicit instruction is *don't read the code closely yet* — watch the outputs. Each demo ends with a pointer to where you'll build the real version (AI workflows in NB 28, retrieval in NB 29 and a full RAG pipeline in NB 35, dashboards from NB 1 through Capstone A), and a closing table maps everything you just saw to the module that teaches it.

**Sections:** 1 An AI reads and triages customer feedback · 2 An AI answers a question grounded in *your* documents (RAG) · 3 The same data, turned into a business KPI snapshot (+ the same KPI as a picture) · What you just saw — and where you'll build it · Now start the journey

**Practice:** none — just run the cells; the outputs are the point.

**Files/datasets:** no datasets — all demo data is generated inline. It imports the repo-root **`llm_providers.py`** (the built-in `MockLLM`); on Colab the first cell fetches that one file automatically, so the notebook runs standalone.

### `00b_course_overview.ipynb` — Course Overview

The companion to the master onboarding — open it when you want the **full course map** and the **time budgets**. It compresses the course into sixty seconds (business data science + machine learning + AI engineering, ending in two interview-ready capstones), draws the module chain from the analytical core through the AI-engineering layer to "ship it" and "synthesise", and documents the six-section template and nine visual markers every main notebook follows — so you know exactly what ✋, 🧪, 🧠 and 🎁 will mean when you meet them.

Its centrepiece is practical planning: a per-notebook time-budget table broken into *read + run*, practice, stretch and bonus components, five learning paths with total-hours estimates, and an **interactive estimator** — edit one list of notebooks and it computes your total hours plus how long that takes at 1 h/day, 3 h/week or 8 h/week, with a chart of the time budget across your chosen path. It closes with self-pacing tips that survive real life and a concept-introduction index ("which notebook first teaches X?").

**Sections:** What this notebook gives you · 1 The course in 60 seconds · 2 The modules and how they chain together · 3 How each notebook is structured · 4 The nine visual markers · 5 Per-notebook time budget · 6 Five learning paths · 7 Estimate *your* time · 8 Tips for actually finishing the course · 9 Concept-introduction index · 10 Where to go next

**Practice:** none as such — the estimator cell is the hands-on part (edit `MY_NOTEBOOKS` and re-run).

## How these notebooks work

Everything in this folder runs **100% offline** — no API key, no sign-ups. The "AI" in `00c_see_it_work.ipynb` is the course's built-in `MockLLM`, the same offline stand-in used by every LLM lesson later on (swap one line and the same code calls a real model). Unlike the numbered lessons, these three notebooks have **no exercise checkpoints**: they're pure orientation, and instead *explain* the rhythm you'll live in from Module 1 onward — short ✋ quick-exercise checkpoints with collapsible solutions mid-lesson, then 🧪 practice, 🧠 stretch and a 🎁 bonus mini-project at the end.

Suggested order:

1. Run `00_master_onboarding.ipynb` end-to-end. Confirm the environment check prints `✅ Setup looks good!`.
2. Run `00c_see_it_work.ipynb` — a 5-minute demo of what you'll be able to build.
3. Skim `00b_course_overview.ipynb` to pick a learning path and estimate your total time.

## Where next

→ **Module 1 — Foundations** (`../01_foundations/01_python_basics.ipynb`).

If you've already programmed in Python before, you can skim Module 1 and start fully engaging from Module 2. Short on time overall? The **`../fast_track/`** folder is the 21-notebook, ~24-hour condensed path through the same material.
