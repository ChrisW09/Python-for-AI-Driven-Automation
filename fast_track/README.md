# 🏎️ Fast Track

> 🧭  [🏠 Course home](../README.md)  ·  [🧪 Module quizzes ▶](../quizzes/)

The whole curriculum, condensed to its essentials. **22 notebooks. About 26 hours.** A shortcut you can finish in a few weeks of evenings — not a substitute for the full course, but a credible introduction that touches every layer of the stack: from Python basics through data science, machine learning, LLM agents and the Model Context Protocol (MCP), and on to forecasting, real business applications, NLP, deployment, an end-to-end capstone, and web scraping.

The first **14 notebooks** are the original linear essentials; notebooks **15–22** are *breadth extensions* that mirror the applied modules of the full course (time series, model evaluation, industry applications, document AI & observability, NLP, deployment, a capstone, and web scraping) — each still trimmed to fast-track size.

> 🚀 **Start here:** [`00_fast_track_onboarding.ipynb`](./00_fast_track_onboarding.ipynb)

**~7 exercises per notebook, every one with a worked solution.** Every fast-track notebook keeps the canonical Practice exercises (3–5 each) *and* two of the harder Stretch exercises (C + D) — the same two-tier exercise design as the full course, just with the very-deep Stretch A/B and the Bonus mini-project trimmed out so the path stays focused.

---

## What's here

| # | Notebook | What it teaches | Time |
|---|---|---|---|
| 0 | `00_fast_track_onboarding.ipynb`    | What the fast track is, what's been left out, environment check | ~10 min |
| 1 | `01_python_basics.ipynb`            | Types, casting, f-strings, defensive string handling | ~50 min |
| 2 | `02_control_structures.ipynb`       | if/elif, for/while, loop control, early return | ~55 min |
| 3 | `03_lists_and_dicts.ipynb`          | Lists, tuples, sets, dicts, comprehensions, `Counter` | ~60 min |
| 4 | `04_functions.ipynb`                | Functions, default args, `*args/**kwargs`, decorators | ~65 min |
| 5 | `05_classes_basics.ipynb`           | Classes, `__init__`, `self`, methods | ~60 min |
| 6 | `06_pandas_fundamentals.ipynb`      | DataFrames, groupby, merge, missing data | ~80 min |
| 7 | `07_visualization_and_stats.ipynb`  | charts in a few lines (pandas/seaborn); distributions, confidence intervals, hypothesis tests | ~80 min |
| 8 | `08_sklearn_basics.ipynb`           | train/test split, fit/predict, evaluation, pipelines | ~85 min |
| 9 | `09_apis_and_sql.ipynb`             | HTTP/REST APIs, status codes, JSON, SQL queries with pandas | ~85 min |
| 10 | `10_ai_workflows.ipynb`            | LLM prompting, classification, JSON output, validation | ~65 min |
| 11 | `11_embeddings_and_rag.ipynb`      | Embeddings, cosine similarity, retrieval, basic RAG, Ragas evaluation | ~70 min |
| 12 | `12_tools_and_agents.ipynb`        | Tool calling, the agent loop, multi-step agents | ~60 min |
| 13 | `13_notebook_to_project.ipynb`     | Packaging notebook code into an installable, tested project | ~60 min |
| 14 | `14_agents_and_mcp.ipynb`          | Agent loops with budgets, robust tools, the Model Context Protocol (MCP) | ~60 min |
| | *— breadth extensions (mirror the full course's applied modules) —* | | |
| 15 | `15_time_series_and_forecasting.ipynb` | Trend/seasonality, decomposition, time-ordered splits, baselines, Holt-Winters, backtesting | ~65 min |
| 16 | `16_model_evaluation_and_feature_engineering.ipynb` | Honest evaluation (ROC/PR, thresholds, CV) + feature engineering &amp; leakage | ~85 min |
| 17 | `17_industry_applications.ipynb`   | Churn/CLV targeting, fraud detection &amp; RFM segmentation — the *model → money → decision* pattern | ~80 min |
| 18 | `18_document_ai_and_observability.ipynb` | Document extraction + validation; golden sets, LLM-as-judge, cost/trace dashboards | ~80 min |
| 19 | `19_nlp_topic_modeling_and_sentiment.ipynb` | Topic modeling (TF-IDF + KMeans) and the sentiment ladder | ~75 min |
| 20 | `20_shipping_scheduling_and_deployment.ipynb` | Scheduling &amp; retries; Docker layers, build cache, and CI — simulated offline | ~75 min |
| 21 | `21_capstone_fast_track.ipynb`     | End-to-end support-ops project: analytics + AI assistant → executive summary | ~90 min |
| 22 | `22_web_scraping.ipynb`            | Web scraping (BeautifulSoup, `robots.txt`, politeness) & the *check-for-an-API-first* rule (OpenAlex) | ~65 min |
| | **Total** | | **~26 h** |

Each notebook (except the onboarding) is a **trimmed copy** of its canonical counterpart in the parent folders; notebooks 7, 9, 16 and 18 each combine two canonical chapters into one, and 17/19/21/22 condense a whole module. The first cell of every trimmed notebook links back to the full version(s). Notebooks 15–22 chain on from 14 but are self-contained — take them in order, or dip into the ones relevant to your work.

---

## 🧑‍🏫 Teaching plan: 12 lectures × 180 minutes

The fast track maps almost perfectly onto a **12-session course with 180-minute lectures** (36 h of contact time for ~26 h of material). Each session pairs roughly two notebooks and leaves ~30–60 minutes for the built-in ✋ Quick-exercise checkpoints (3 per notebook), a selection of the Practice exercises, and discussion. The natural rhythm: **teach ~20 min → ✋ checkpoint (~2 min, then reveal the solution) → repeat**, with a longer hands-on exercise block at the end of each notebook.

| Lecture | Theme | Notebooks | Content | Hands-on / buffer |
|---|---|---|---|---|
| **1** | Getting started with Python | 00 onboarding · 01 basics · 02 control structures | ~115 min | ~65 min — environment check in class, extra time on first-timers' setup issues |
| **2** | Data structures & functions | 03 lists and dicts · 04 functions | ~125 min | ~55 min — comprehension drills; decorators only if time allows |
| **3** | OOP & pandas | 05 classes · 06 pandas fundamentals | ~140 min | ~40 min — groupby/merge Practice exercises in pairs |
| **4** | Visualization, statistics & first models | 07 visualization and stats · 08 sklearn basics | ~165 min | ~15 min — **tightest session**: run checkpoints only, assign Practice exercises as homework |
| **5** | Getting data: APIs & SQL, first LLM calls | 09 APIs and SQL · 10 AI workflows | ~150 min | ~30 min — live API demo; prompt-engineering experiments |
| **6** | Embeddings, RAG & agents | 11 embeddings and RAG · 12 tools and agents | ~130 min | ~50 min — build-your-own-tool exercise; discuss RAG failure modes |
| **7** | From notebook to project; agents & MCP | 13 notebook to project · 14 agents and MCP | ~120 min | ~60 min — package a small project live; midpoint recap of NB 1–14 |
| **8** | Forecasting & honest evaluation | 15 time series · 16 model evaluation and feature engineering | ~150 min | ~30 min — leakage hunt exercise; announce capstone (lecture 11) |
| **9** | AI in the business | 17 industry applications · 18 document AI and observability | ~160 min | ~20 min — second-tightest session: checkpoints only, Stretch C/D as homework |
| **10** | NLP & shipping to production | 19 NLP topic modeling and sentiment · 20 scheduling and deployment | ~150 min | ~30 min — Docker layer-cache demo; sentiment-ladder discussion |
| **11** | Capstone | 21 capstone fast track | ~90 min guided | ~90 min — supervised project work: students extend the capstone with their own analysis |
| **12** | Web scraping & wrap-up | 22 web scraping | ~65 min | ~115 min — capstone presentations, [module quizzes](../quizzes/) as a review round, where-to-go-next (full course, Stretch A/B) |
| | **Total** | 22 notebooks + onboarding | **~26 h** | **~10 h** |

A few notes for instructors:

- **Lectures 4 and 9 are the tight ones** (~165 and ~160 min of material). Stick to the checkpoints in class and push the end-of-notebook Practice exercises to homework — every one ships with a worked solution, so they self-correct.
- **Homework cadence:** assign the Practice exercises of each session's notebooks between lectures; offer Stretch C/D to stronger students. That adds ~2–3 h/week of self-study and keeps contact time for the interactive parts.
- **Quizzes:** the [module quizzes](../quizzes/) make good 5-minute openers — quiz the previous session's topics before starting new material.
- **Fewer sessions?** With 10 lectures, merge 7+8 into one session (drop the midpoint recap, trim NB 15's backtesting section) and fold NB 22 into the capstone session as homework.

---

## What's intentionally missing

The breadth extensions (NB 15–22) now mirror most of the full course's applied modules — time series, model evaluation & feature engineering, industry applications, document AI & observability, NLP, deployment, a capstone, and web scraping. Even so, the fast track stays lean. Compared to the full course, these are still gone:

- **🧠 Stretch exercises A and B** (the very-deep problems) — the fast track keeps Stretch C and D, which are still notably harder than the Practice ones but realistic for the time budget.
- **🎁 Bonus mini-project** at the end of every notebook.
- **Full depth in every lesson** — each fast-track notebook is trimmed; the combined ones (NB 7, 9, 16, 18) and the module-condensing ones (NB 17, 19, 21, 22) keep the essential throughline and link back to the canonical chapters for the rest.
- **A standalone NumPy notebook** (`08_numpy_fundamentals.ipynb`) and **`04_dictionaries_advanced.ipynb`** — folded into pandas (NB 6) and the lists + dicts notebook (NB 3) respectively.
- **The optional appendices** (classical → deep-learning → foundation-model forecasting, PyTorch, TabPFN/conformal prediction, vector-store & RAG/agent-framework surveys), **Module 12 (DeepTab)**, **Module 16 (Business AI)** as a standalone lesson, and **Module 17 (Django)**.

The full course is at the parent level — entry point: `../00_onboarding/00_master_onboarding.ipynb`.

---

## When to switch to the full course

Three good signals:

1. **You want interview prep.** The full course has 140+ Stretch exercises (A–D in every notebook) that are deliberately interview-grade. The fast track keeps only C and D.
2. **You want to ship code.** The fast track covers the packaging basics (NB 13); the full course's Module 13 goes further into scheduling, orchestration, and config & secrets.
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
  08_sklearn_basics         ←  05_machine_learning/17_sklearn_basics
  09_apis_and_sql           ←  03_real_world_io/12_apis_and_http + 13_sql_fundamentals
  10_ai_workflows           ←  08_ai_engineering/28_ai_workflows
  11_embeddings_and_rag     ←  08_ai_engineering/29_embeddings_retrieval
  12_tools_and_agents       ←  08_ai_engineering/30_tools_and_agents
  13_notebook_to_project    ←  13_production/45_from_notebook_to_project
  14_agents_and_mcp         ←  10_agents_tools_mcp/* (agents, tools & MCP, condensed)
  ── breadth extensions ──
  15_time_series_and_forecasting              ←  02_data_science/11_time_series_forecasting (+ A1 classical)
  16_model_evaluation_and_feature_engineering ←  05_machine_learning/18_model_evaluation + 19_feature_engineering
  17_industry_applications                    ←  07_industry_applications/* (churn/CLV, fraud, condensed)
  18_document_ai_and_observability            ←  08_ai_engineering/31_document_processing + 32_ai_evaluation_observability
  19_nlp_topic_modeling_and_sentiment         ←  11_nlp/* (BERTopic→TF-IDF+KMeans; sentiment ladder)
  20_shipping_scheduling_and_deployment       ←  13_production/46_scheduling_orchestration + 14_cicd/* (labs)
  21_capstone_fast_track                      ←  15_capstones/47_capstone_analytics + 48_capstone_ai_assistant
  22_web_scraping                             ←  04_webscraping/* (fundamentals, Firecrawl, OpenAlex — condensed)
```

The fast-track notebooks are flat-numbered 1–22 deliberately — a single linear path you can work straight through (1–14 are the core essentials; 15–22 broaden coverage across the applied modules). Inside each notebook the cross-references use the **fast-track numbers** (e.g. *"pandas in NB 6"*); back-references to the full course always use explicit relative paths (e.g. [`../08_ai_engineering/`](../08_ai_engineering/)), so you can always follow a thread to the depth notebook.
