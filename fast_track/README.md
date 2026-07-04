# 🏎️ Fast Track

The whole curriculum, condensed to its essentials. **21 notebooks. About 24 hours.** A shortcut you can finish in a few weeks of evenings — not a substitute for the full course, but a credible introduction that touches every layer of the stack: from Python basics through data science, machine learning, LLM agents and the Model Context Protocol (MCP), and on to forecasting, real business applications, NLP, deployment, and an end-to-end capstone.

The first **14 notebooks** are the original linear essentials; notebooks **15–21** are *breadth extensions* that mirror the applied modules of the full course (time series, model evaluation, industry applications, document AI & observability, NLP, deployment, and a capstone) — each still trimmed to fast-track size.

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
| | *— breadth extensions (mirror the full course's applied modules) —* | | |
| 15 | `15_time_series_and_forecasting.ipynb` | Trend/seasonality, time-ordered splits, baselines, Holt-Winters, backtesting | ~65 min |
| 16 | `16_model_evaluation_and_feature_engineering.ipynb` | Honest evaluation (ROC/PR, thresholds, CV) + feature engineering &amp; leakage | ~85 min |
| 17 | `17_industry_applications.ipynb`   | Churn/CLV targeting &amp; fraud detection — the *model → money → decision* pattern | ~80 min |
| 18 | `18_document_ai_and_observability.ipynb` | Document extraction + validation; golden sets, LLM-as-judge, cost/trace dashboards | ~80 min |
| 19 | `19_nlp_topic_modeling_and_sentiment.ipynb` | Topic modeling (TF-IDF + KMeans) and the sentiment ladder | ~75 min |
| 20 | `20_shipping_scheduling_and_deployment.ipynb` | Scheduling &amp; retries; Docker layers, build cache, and CI — simulated offline | ~75 min |
| 21 | `21_capstone_fast_track.ipynb`     | End-to-end support-ops project: analytics + AI assistant → executive summary | ~90 min |
| | **Total** | | **~24 h** |

Each notebook (except the onboarding) is a **trimmed copy** of its canonical counterpart in the parent folders; notebooks 7, 9, 16 and 18 each combine two canonical chapters into one, and 17/19/21 condense a whole module. The first cell of every trimmed notebook links back to the full version(s). Notebooks 15–21 chain on from 14 but are self-contained — take them in order, or dip into the ones relevant to your work.

---

## What's intentionally missing

The breadth extensions (NB 15–21) now mirror most of the full course's applied modules — time series, model evaluation & feature engineering, industry applications, document AI & observability, NLP, deployment, and a capstone. Even so, the fast track stays lean. Compared to the full course, these are still gone:

- **🧠 Stretch exercises A and B** (the very-deep problems) — the fast track keeps Stretch C and D, which are still notably harder than the Practice ones but realistic for the time budget.
- **🎁 Bonus mini-project** at the end of every notebook.
- **Full depth in every lesson** — each fast-track notebook is trimmed; the combined ones (NB 7, 9, 16, 18) and the module-condensing ones (NB 17, 19, 21) keep the essential throughline and link back to the canonical chapters for the rest.
- **A standalone NumPy notebook** (`08_numpy_fundamentals.ipynb`) and **`04_dictionaries_advanced.ipynb`** — folded into pandas (NB 6) and the lists + dicts notebook (NB 3) respectively.
- **The optional appendices** (classical → deep-learning → foundation-model forecasting, PyTorch, TabPFN/conformal prediction, vector-store & RAG/agent-framework surveys), **Module 10 (DeepTab)**, **Module 14 (Business AI)** as a standalone lesson, and **Module 15 (Django)**.

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
  ── breadth extensions ──
  15_time_series_and_forecasting              ←  02_data_science/11_time_series_forecasting (+ A1 classical)
  16_model_evaluation_and_feature_engineering ←  04_machine_learning/15_model_evaluation + 16_feature_engineering
  17_industry_applications                    ←  05_industry_applications/* (churn/CLV, fraud, condensed)
  18_document_ai_and_observability            ←  06_ai_engineering/25_document_processing + 26_ai_evaluation_observability
  19_nlp_topic_modeling_and_sentiment         ←  09_nlp/* (BERTopic→TF-IDF+KMeans; sentiment ladder)
  20_shipping_scheduling_and_deployment       ←  11_production/40_scheduling_orchestration + 12_cicd/* (labs)
  21_capstone_fast_track                      ←  13_capstones/41_capstone_analytics + 42_capstone_ai_assistant
```

The fast-track notebooks are flat-numbered 1–21 deliberately — a single linear path you can work straight through (1–14 are the core essentials; 15–21 broaden coverage across the applied modules). Inside each notebook the cross-references use the **fast-track numbers** (e.g. *"pandas in NB 6"*); back-references to the full course always use explicit relative paths (e.g. [`../06_ai_engineering/`](../06_ai_engineering/)), so you can always follow a thread to the depth notebook.
