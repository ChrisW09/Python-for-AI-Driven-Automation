# 🏎️ Fast Track

The whole curriculum, condensed to its essentials. **14 notebooks. About 15 hours.** A shortcut you can finish in a few weeks of evenings — not a substitute for the full course, but a credible introduction that touches every layer of the stack, from Python basics all the way to LLM agents, the Model Context Protocol (MCP), and packaging a real project.

> 🚀 **Start here:** [`00_fast_track_onboarding.ipynb`](./00_fast_track_onboarding.ipynb)

**~7 exercises per notebook, every one with a worked solution.** Every fast-track notebook keeps the canonical Practice exercises (3–5 each) *and* two of the harder Stretch exercises (C + D) — the same two-tier exercise design as the full course, just with the very-deep Stretch A/B and the Bonus mini-project trimmed out so the path stays focused.

---

## What's here

| # | Notebook | What it teaches | Time |
|---|---|---|---|
| 0 | `00_fast_track_onboarding.ipynb`    | What the fast track is, what's been left out, environment check | ~10 min |
| 1 | `01_python_basics.ipynb`            | Types, casting, f-strings, defensive string handling | ~50 min |
| 2 | `02_control_structures.ipynb`       | if/elif, for/while, loop control, early return | ~55 min |
| 3 | `03_lists_and_dicts.ipynb`          | Lists, tuples, sets, dicts, comprehensions, `defaultdict`, `Counter` | ~60 min |
| 4 | `04_functions.ipynb`                | Functions, default args, `*args/**kwargs`, decorators | ~65 min |
| 5 | `05_classes_basics.ipynb`           | Classes, `__init__`, `self`, methods | ~60 min |
| 6 | `06_pandas_fundamentals.ipynb`      | DataFrames, groupby, merge, missing data | ~80 min |
| 7 | `07_visualization_and_stats.ipynb`  | charts in a few lines (pandas/seaborn); distributions, confidence intervals, hypothesis tests | ~80 min |
| 8 | `08_sklearn_basics.ipynb`           | train/test split, fit/predict, evaluation, pipelines | ~85 min |
| 9 | `09_apis_and_sql.ipynb`             | HTTP/REST APIs, status codes, JSON, SQL queries with pandas | ~85 min |
| 10 | `10_ai_workflows.ipynb`            | LLM prompting, classification, JSON output, validation | ~65 min |
| 11 | `11_embeddings_and_rag.ipynb`      | Embeddings, cosine similarity, retrieval, basic RAG | ~65 min |
| 12 | `12_tools_and_agents.ipynb`        | Tool calling, the agent loop, multi-step agents | ~60 min |
| 13 | `13_notebook_to_project.ipynb`     | Packaging notebook code into an installable, tested project | ~60 min |
| 14 | `14_agents_and_mcp.ipynb`          | Agent loops with budgets, robust tools, the Model Context Protocol (MCP) | ~60 min |
| | **Total** | | **~15 h** |

Each notebook (except the onboarding) is a **trimmed copy** of its canonical counterpart in the parent folders; notebooks 7 and 9 each combine two canonical chapters into one. The first cell of every trimmed notebook links back to the full version(s).

---

## What's intentionally missing

Compared to the full course, these are gone:

- **🧠 Stretch exercises A and B** (the very-deep problems) — the fast track keeps Stretch C and D, which are still notably harder than the Practice ones but realistic for the time budget.
- **🎁 Bonus mini-project** at the end of every notebook.
- **`04_dictionaries_advanced.ipynb`** — merged into the fast-track NB 3.
- **NumPy and time-series forecasting** — pandas plus the new visualization/statistics notebook (NB 7) cover ~80 % of what beginners need first.
- **Model evaluation, feature engineering, document processing, AI evaluation & observability, and scheduling/orchestration** — defer these to the full course when you need the depth.
- **Both capstones**, **Module 8's business-AI applications**, **Module 9's proof-of-concept builds**, **Module 10's industry applications** (churn value, fraud, segmentation, forecasting), and **all 11 optional appendices**.

The full course is at the parent level — entry point: `../00_onboarding/00_master_onboarding.ipynb`.

---

## When to switch to the full course

Three good signals:

1. **You want interview prep.** The full course has 140+ Stretch exercises (A–D in every notebook) that are deliberately interview-grade. The fast track keeps only C and D.
2. **You want to ship code.** The fast track covers the packaging basics (NB 13); the full course's Module 6 goes further into scheduling, orchestration, and config & secrets.
3. **You're curious about a specific topic.** The full course has dedicated notebooks on NumPy, time-series forecasting, model evaluation, feature engineering, document processing, and AI observability. Pick the one that matters for your work.

---

## Setup

Same dependencies as the full course:

```bash
pip install -r ../requirements.txt
```

You don't need anything extra — the `llm_providers.py` shim at the repo root means the AI notebooks (NB 10, 11, 12, and 14) run offline by default with the built-in `MockLLM`.

---

## How notebooks here relate to the canonical course

```
fast_track/                      canonical full course
  01_python_basics          ←  01_foundations/01_python_basics
  02_control_structures     ←  01_foundations/02_control_structures
  03_lists_and_dicts        ←  01_foundations/03_lists_data_structures
  04_functions              ←  01_foundations/05_functions_modules
  05_classes_basics         ←  01_foundations/06_classes_and_oop
  06_pandas_fundamentals    ←  02_data_science/07_pandas_fundamentals
  07_visualization_and_stats←  02_data_science/09_matplotlib_basics + 10_statistics_basics
  08_sklearn_basics         ←  04_machine_learning/14_sklearn_basics
  09_apis_and_sql           ←  03_real_world_io/12_apis_and_http + 13_sql_fundamentals
  10_ai_workflows           ←  06_ai_engineering/22_ai_workflows
  11_embeddings_and_rag     ←  06_ai_engineering/23_embeddings_retrieval
  12_tools_and_agents       ←  06_ai_engineering/24_tools_and_agents
  13_notebook_to_project    ←  11_production/39_from_notebook_to_project
  14_agents_and_mcp         ←  08_agents_tools_mcp/* (agents, tools & MCP, condensed)
```

The fast-track notebooks are flat-numbered 1–14 deliberately — a single linear path you work straight through. Inside each notebook the cross-references use the **fast-track numbers** (e.g. *"pandas in NB 6"*); back-references to the full course always use explicit relative paths (e.g. [`../06_ai_engineering/`](../06_ai_engineering/)), so you can always follow a thread to the depth notebook.
