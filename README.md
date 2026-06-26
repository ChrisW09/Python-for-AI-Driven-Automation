<h1 align="center">Python for AI-Driven Automation &amp; Business Data Science</h1>

<p align="center">
  From your first line of Python to shipping a real AI-driven automation —<br>
  a hands-on, self-paced curriculum across Python fluency, business data science,<br>
  machine learning, AI engineering, and production.
</p>

<p align="center">
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-3da639.svg">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776ab.svg?logo=python&logoColor=white">
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-notebooks-f37726.svg?logo=jupyter&logoColor=white">
  <a href="#-open-any-notebook-in-colab"><img alt="Open in Colab" src="https://img.shields.io/badge/Open%20in-Colab-f9ab00.svg?logo=googlecolab&logoColor=white"></a>
  <img alt="Runs 100% offline" src="https://img.shields.io/badge/Runs-100%25%20offline-2ea44f.svg">
  <img alt="249 checkpoints, kernel-tested" src="https://img.shields.io/badge/249%20checkpoints-kernel--tested-8a2be2.svg">
</p>

<p align="center">
  <b>87 runnable notebooks · 14 modules · 300+ exercises · 249 in-lesson checkpoints · 100% offline</b>
</p>

<p align="center">
  <a href="#-quick-start">🚀 Quick start</a> &nbsp;·&nbsp;
  <a href="#-curriculum">📚 Curriculum</a> &nbsp;·&nbsp;
  <a href="#-how-each-notebook-works">📓 How it works</a> &nbsp;·&nbsp;
  <a href="#-open-any-notebook-in-colab">▶️ Open in Colab</a> &nbsp;·&nbsp;
  <a href="#-contributing--licence">🤝 Contributing</a>
</p>

---

## Contents

- [Why this course](#-why-this-course)
- [What's new](#-whats-new)
- [Quick start](#-quick-start)
- [Choose your path](#-choose-your-path)
- [Curriculum](#-curriculum)
- [Repository layout](#-repository-layout)
- [How each notebook works](#-how-each-notebook-works)
- [LLM providers](#-llm-providers)
- [Open any notebook in Colab](#-open-any-notebook-in-colab) — one-click links to all 87 notebooks
- [Contributing &amp; licence](#-contributing--licence)

---

## ⚡ Why this course

- **End to end.** From `print("hello")` to a deployed, scheduled AI automation — no gaps assumed, no steps skipped.
- **Runs anywhere.** One click into Google Colab, or `pip install` locally. Every notebook runs **100% offline** — no API key, no paid service required.
- **Learn by doing.** **300+ exercises** — including a deliberate 🐞 debug-me in each lesson — every one shipping with a worked solution and the *reasoning* behind it.
- **Built for live teaching.** Every lesson is punctuated with short ✋ **Quick exercise** checkpoints (~2 min each) at natural section breaks, so a class can alternate ~20 minutes of instruction with a quick hands-on pause. **249 across the course**, each with a scaffolded starter and a collapsible solution — and every solution has been **executed in a fresh kernel to confirm it runs**.
- **Modern, minimal code.** Charts in 1–3 lines (pandas `.plot()`, seaborn, sklearn's built-in plot helpers), pipelines over boilerplate — you learn the way practitioners actually write Python today.
- **Visual where it counts.** Key ideas — train/test splits, k-fold cross-validation, grid search, RAG pipelines, MCP topology — come with clean diagrams embedded right in the notebooks.
- **Real business problems.** Churn &amp; CLV, fraud detection, demand forecasting, customer segmentation, RAG assistants, and AI governance — not toy datasets.

---

## ✨ What's new

- **✋ Interactive in-lesson checkpoints.** Every lesson now embeds short ~2-minute *Quick exercise* checkpoints at natural section breaks — **249 across the course** — so you pause and *do* every ~20 minutes instead of reading straight through. Each ships a scaffolded starter and a collapsible solution, and **every solution has been executed in a fresh kernel to confirm it runs**. → [How each notebook works](#-how-each-notebook-works)
- **🧑‍🏫 Built for live teaching.** The checkpoint rhythm — lecture ~20 min → ~2-min try → reveal — turns any lesson into an interactive class with zero prep.
- **🔌 100% offline, end to end.** Every notebook — including the LLM, RAG, and agent lessons — runs with no API key via a built-in `MockLLM` and offline stand-ins for the heavy libraries.

---

## 🚀 Quick start

### ▶︎ Google Colab — zero setup *(recommended)*

Click a badge to open a notebook in your browser; nothing to install.

> 🔑 **You need a free Google account to *run* the notebooks.** Colab gives each signed-in user a free cloud runtime, so the first time you press **Run** it will ask you to sign in (any Gmail account works). Without signing in you can read a notebook but not execute its cells. No Google account? Use the **Local Jupyter** option below instead.

- **Start the full course** — `00_master_onboarding.ipynb` &nbsp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00_master_onboarding.ipynb)
- **Start the fast track** — `00_fast_track_onboarding.ipynb` &nbsp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/00_fast_track_onboarding.ipynb)
- **See it work first (5 min)** — `00c_see_it_work.ipynb` &nbsp; [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00c_see_it_work.ipynb)

Every notebook is listed with its own Colab link in [Open any notebook in Colab](#-open-any-notebook-in-colab).

### ⌥ Local Jupyter

```bash
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Tested with **Python 3.10+**. Module 0 includes an environment-check cell. The 13 appendices demo heavier libraries (PyTorch, Prophet, FAISS, LangChain, …), kept commented-out at the bottom of `requirements.txt` — each still runs offline via a built-in stand-in, so install them only to see the real library at work.

---

## 🧭 Choose your path

| | 🎓 **Complete course** | 🏎️ **Fast track** |
|---|---|---|
| **Scope** | All 14 modules + 13 optional appendices | The essentials, condensed |
| **Notebooks** | 46 lessons (+ appendices) | 14 lessons |
| **Time** | ~115 hours | ~15 hours |
| **Best for** | Depth — every exercise, stretch problem &amp; capstone | A credible end-to-end pass in a few evenings |
| **Start here** | [`00_master_onboarding.ipynb`](./00_onboarding/00_master_onboarding.ipynb) | [`fast_track/`](./fast_track/) |

New here? [`00c_see_it_work.ipynb`](./00_onboarding/00c_see_it_work.ipynb) is a 5-minute offline demo of what you'll build, and [`00b_course_overview.ipynb`](./00_onboarding/00b_course_overview.ipynb) has the full module map and an interactive time estimator.

---

## 📚 Curriculum

| Module | Lessons | Focus |
|---|:---:|---|
| [**0 · Onboarding**](./00_onboarding/) | — | Setup, orientation, 5-minute demo |
| [**1 · Foundations**](./01_foundations/) | 1–6 | Variables, control flow, lists, dicts, functions, classes |
| [**2 · Data Science**](./02_data_science/) | 7–11 | pandas, NumPy, seaborn/matplotlib, statistics, time series |
| [**3 · Real-world I/O**](./03_real_world_io/) | 12–13 | HTTP/APIs, SQL, data validation |
| [**4 · Machine Learning**](./04_machine_learning/) | 14–16 | scikit-learn, cross-validation &amp; hyperparameter tuning, model evaluation, feature engineering |
| [**5 · Industry Applications**](./05_industry_applications/) | 17–20 | Churn/CLV, fraud, segmentation + recommenders, demand &amp; maintenance |
| [**6 · AI Engineering**](./06_ai_engineering/) | 21–26 | LLM fundamentals, prompts, RAG, agents, document processing, eval &amp; observability |
| [**7 · Building AI POCs**](./07_building_ai_pocs/) | 27–30 | Copilot setup, three POCs, RAG deep dive, vector DBs + agentic AI |
| [**8 · Agents, Tools &amp; MCP**](./08_agents_tools_mcp/) | 31–34 | Agent architectures, robust tools, the Model Context Protocol, multi-agent systems |
| [**9 · NLP (Text Analytics)**](./09_nlp/) | 35–37 | Topic modeling (BERTopic, STREAM) &amp; sentiment analysis (VADER → classical → transformers) |
| [**10 · Optional: DeepTab**](./10_deeptab/) | 38 | Deep learning for tabular data — Mamba/FT-Transformer/SAINT… behind a scikit-learn API |
| [**11 · Production**](./11_production/) | 39–40 | Packaging notebooks into projects, scheduling |
| [**12 · CI/CD &amp; Deployment**](./12_cicd/) | — | Docker, Compose, GitHub Actions, registries, DNS, reverse proxies, HTTPS, Ubuntu deployment — a self-contained mini-book + runnable example app |
| [**13 · Capstones**](./13_capstones/) | 41–42 | Two end-to-end projects (analytics + AI assistant) |
| [**14 · Business AI**](./14_business_ai/) | 43–46 | Digital transformation, architecture, AI-assisted dev, governance |

> **13 optional appendices** (classical → deep-learning → foundation-model forecasting, PyTorch, vector stores, RAG/agent frameworks) live beside their modules — all runnable offline. **Modules 9–10 are optional, reference-style tracks** (text analytics + deep tabular), also fully offline.

---

## 🗂️ Repository layout

| Path | Contents |
|---|---|
| `00_onboarding/` … `14_business_ai/` | The complete course — 46 lessons + 13 appendices |
| `09_nlp/`, `10_deeptab/` | Optional reference tracks — text analytics (NB 35–37) &amp; deep tabular learning (NB 38) |
| `12_cicd/` | CI/CD, Docker &amp; deployment mini-book — 14 chapters + a runnable example app (no notebooks) |
| `fast_track/` | The fast track — 14 trimmed notebooks (~15 h) |
| `quizzes/` | 10 short multiple-choice quizzes (Modules 1–8, 11 &amp; 14) |
| `data/` | Sample CSVs the notebooks read (support_ops, api_log, customer_feedback) |
| `slides/` | Course-overview deck + lecture decks (PDF + LaTeX source) |
| `scripts/` | Helpers to run every notebook end-to-end or check NB-number references |
| `docs/` | Course-design notes (pedagogical review, module-descriptor coverage) |
| `llm_providers.py` | Unified interface to OpenAI / Anthropic / Google / Ollama (+ offline `MockLLM`) |
| `previous_versions/` | The legacy flat 19-notebook layout, archived |

---

## 📓 How each notebook works

A consistent six-part template:

> 🎯 **Objectives** + ✅ **prerequisites** → numbered **concept sections** (prose + runnable code), interleaved with ✋ **quick-exercise checkpoints** → 🧪 **practice exercises** (incl. a 🐞 debug-me) → 🧠 **stretch exercises** A–D → 🎁 **bonus mini-project** → ✅ **self-assessment** + 🚀 **next step**

Every exercise — **300+ across the course** — ships with a worked solution and the *reasoning* behind it.

### ✋ In-lesson checkpoints — designed for interactive teaching

Beyond the end-of-lesson exercise bank, each lesson embeds short **✋ Quick exercise** checkpoints at natural section breaks — roughly one every ~20 minutes of material. They turn a lecture into a rhythm: **teach ~20 min → pause for a ~2-minute hands-on exercise → teach again.**

Each checkpoint is a self-contained three-cell block:

1. **Prompt** — a focused, business/AI-flavoured task, solvable with *only* what the lesson has covered up to that point.
2. **`# ✍️ Your turn`** — a scaffolded starter cell to fill in.
3. **✅ Solution** — a collapsible answer with a one-line explanation.

There are **249 of these across the course** (3–4 per core lesson, 3 per fast-track lesson), and every code solution has been **executed in a fresh Jupyter kernel to verify it actually runs** (the few file-content solutions — `__init__.py`, pytest, `pyproject.toml` — are validated by inspection). They run 100% offline like everything else — no API key or network needed. Self-paced learners solve each one as they reach it; instructors use them as the built-in "pause and try" beats of a class. In the conceptual Business-AI lessons (43–46) the middle cell is a short written reflection/decision task instead of code.

> 🧑‍🏫 **Teaching live?** Lecture for ~20 minutes, then jump to the next ✋ checkpoint and give the room ~2 minutes to try it before you reveal the solution. With 3–4 per lesson, a 90-minute class gets several natural interactive breaks — no prep required.

Two more conventions you'll see throughout:

- **Charts take a few lines, not a page.** Plots are drawn with pandas `.plot()`, seaborn one-liners (`hue=` instead of loops, `sns.heatmap(cm, annot=True)` for matrices), and scikit-learn's `*Display` helpers — raw matplotlib appears only for final tweaks and multi-panel layouts.
- **Diagrams travel with the notebook.** Explanatory figures (the train/test split, 5-fold cross-validation, the GridSearchCV flow, RAG pipelines, MCP host/client/server topology, walk-forward backtesting, …) are embedded as attachments inside the `.ipynb` files, so they render on GitHub, in Colab, and locally with no extra image files.

---

## 🔌 LLM providers

Notebooks 21–26 and 42 run **entirely offline** with the built-in `MockLLM`. For real intelligence, swap one line — the unified interface in [`llm_providers.py`](./llm_providers.py) supports four providers:

| Provider | Class | When to use |
|---|---|---|
| 🟢 OpenAI | `OpenAILLM(model="gpt-4o-mini")` | Reliable default |
| 🟠 Anthropic | `AnthropicLLM(model="claude-haiku-4-5-20251001")` | Long context, careful tone |
| 🔵 Google | `GoogleLLM(model="gemini-2.0-flash")` | Cheap at scale |
| 🟣 Ollama | `OllamaLLM(model="llama3.2:3b")` | Local — no internet, key, or cost |

Set the matching `*_API_KEY` env var for hosted providers (never inline). See [`06_ai_engineering/A1_llm_providers_guide.ipynb`](./06_ai_engineering/A1_llm_providers_guide.ipynb) for setup and cost notes. **Never commit API keys.**

---

## ▶️ Open any notebook in Colab

Every notebook below runs in [Google Colab](https://colab.research.google.com/) with one click — no install, no download. Click a badge to open it. **Sign in with a free Google account** the first time you run a cell — Colab needs it to give you a cloud runtime.

### 0 · Onboarding

| Notebook | Open |
|---|---|
| `00_master_onboarding.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00_master_onboarding.ipynb) |
| `00b_course_overview.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00b_course_overview.ipynb) |
| `00c_see_it_work.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00c_see_it_work.ipynb) |

### 1 · Foundations

| Notebook | Open |
|---|---|
| `01_python_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/01_python_basics.ipynb) |
| `02_control_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/02_control_structures.ipynb) |
| `03_lists_data_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/03_lists_data_structures.ipynb) |
| `04_dictionaries_advanced.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/04_dictionaries_advanced.ipynb) |
| `05_functions_modules.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/05_functions_modules.ipynb) |
| `06_classes_and_oop.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/01_foundations/06_classes_and_oop.ipynb) |

### 2 · Data Science

| Notebook | Open |
|---|---|
| `07_pandas_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/07_pandas_fundamentals.ipynb) |
| `08_numpy_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/08_numpy_fundamentals.ipynb) |
| `09_matplotlib_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/09_matplotlib_basics.ipynb) |
| `10_statistics_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/10_statistics_basics.ipynb) |
| `11_time_series_forecasting.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/11_time_series_forecasting.ipynb) |
| `A1_forecasting_classical.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/A1_forecasting_classical.ipynb) |
| `A2_forecasting_prophet_libraries.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/A2_forecasting_prophet_libraries.ipynb) |
| `A3_forecasting_deep_learning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/A3_forecasting_deep_learning.ipynb) |
| `A4_forecasting_foundation_models.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/02_data_science/A4_forecasting_foundation_models.ipynb) |

### 3 · Real-world I/O

| Notebook | Open |
|---|---|
| `12_apis_and_http.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/03_real_world_io/12_apis_and_http.ipynb) |
| `13_sql_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/03_real_world_io/13_sql_fundamentals.ipynb) |
| `A1_web_scraping_firecrawl.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/03_real_world_io/A1_web_scraping_firecrawl.ipynb) |

### 4 · Machine Learning

| Notebook | Open |
|---|---|
| `14_sklearn_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/14_sklearn_basics.ipynb) |
| `15_model_evaluation.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/15_model_evaluation.ipynb) |
| `16_feature_engineering.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/16_feature_engineering.ipynb) |
| `A1_pytorch_foundations.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/A1_pytorch_foundations.ipynb) |
| `A2_pytorch_vision_and_sequences.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/A2_pytorch_vision_and_sequences.ipynb) |
| `A3_pytorch_fine_tuning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/A3_pytorch_fine_tuning.ipynb) |
| `A4_tabpfn_priorlab.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/A4_tabpfn_priorlab.ipynb) |
| `A5_conformal_prediction.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/04_machine_learning/A5_conformal_prediction.ipynb) |

### 5 · Industry Applications

| Notebook | Open |
|---|---|
| `17_churn_clv_retention.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/05_industry_applications/17_churn_clv_retention.ipynb) |
| `18_fraud_anomaly_detection.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/05_industry_applications/18_fraud_anomaly_detection.ipynb) |
| `19_segmentation_recommenders.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/05_industry_applications/19_segmentation_recommenders.ipynb) |
| `20_demand_maintenance.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/05_industry_applications/20_demand_maintenance.ipynb) |

### 6 · AI Engineering

| Notebook | Open |
|---|---|
| `21_llm_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/21_llm_fundamentals.ipynb) |
| `22_ai_workflows.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/22_ai_workflows.ipynb) |
| `23_embeddings_retrieval.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/23_embeddings_retrieval.ipynb) |
| `24_tools_and_agents.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/24_tools_and_agents.ipynb) |
| `25_document_processing.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/25_document_processing.ipynb) |
| `26_ai_evaluation_observability.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/26_ai_evaluation_observability.ipynb) |
| `A1_llm_providers_guide.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/A1_llm_providers_guide.ipynb) |
| `A2_vector_stores_survey.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/A2_vector_stores_survey.ipynb) |
| `A3_rag_and_agent_frameworks.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/06_ai_engineering/A3_rag_and_agent_frameworks.ipynb) |

### 7 · Building AI POCs

| Notebook | Open |
|---|---|
| `27_from_setup_to_first_poc.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/07_building_ai_pocs/27_from_setup_to_first_poc.ipynb) |
| `28_three_pocs_growing_complexity.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/07_building_ai_pocs/28_three_pocs_growing_complexity.ipynb) |
| `29_rag_pipeline_deep_dive.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/07_building_ai_pocs/29_rag_pipeline_deep_dive.ipynb) |
| `30_vector_db_and_agentic_ai.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/07_building_ai_pocs/30_vector_db_and_agentic_ai.ipynb) |

### 8 · Agents, Tools & MCP

| Notebook | Open |
|---|---|
| `31_agent_architectures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/08_agents_tools_mcp/31_agent_architectures.ipynb) |
| `32_designing_robust_tools.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/08_agents_tools_mcp/32_designing_robust_tools.ipynb) |
| `33_model_context_protocol.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/08_agents_tools_mcp/33_model_context_protocol.ipynb) |
| `34_multi_agent_systems.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/08_agents_tools_mcp/34_multi_agent_systems.ipynb) |

### 9 · NLP (Text Analytics)

| Notebook | Open |
|---|---|
| `35_topic_modeling_bertopic.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/09_nlp/35_topic_modeling_bertopic.ipynb) |
| `36_topic_modeling_stream.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/09_nlp/36_topic_modeling_stream.ipynb) |
| `37_sentiment_analysis.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/09_nlp/37_sentiment_analysis.ipynb) |

### 10 · Optional: DeepTab

| Notebook | Open |
|---|---|
| `38_deeptab_tabular_deep_learning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/10_deeptab/38_deeptab_tabular_deep_learning.ipynb) |

### 11 · Production

| Notebook | Open |
|---|---|
| `39_from_notebook_to_project.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/11_production/39_from_notebook_to_project.ipynb) |
| `40_scheduling_orchestration.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/11_production/40_scheduling_orchestration.ipynb) |

### 13 · Capstones

| Notebook | Open |
|---|---|
| `41_capstone_analytics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/13_capstones/41_capstone_analytics.ipynb) |
| `42_capstone_ai_assistant.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/13_capstones/42_capstone_ai_assistant.ipynb) |

### 14 · Business AI

| Notebook | Open |
|---|---|
| `43_digital_transformation.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/14_business_ai/43_digital_transformation.ipynb) |
| `44_architecture_patterns.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/14_business_ai/44_architecture_patterns.ipynb) |
| `45_ai_assisted_software_development.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/14_business_ai/45_ai_assisted_software_development.ipynb) |
| `46_bpm_governance_poc_mvp.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/14_business_ai/46_bpm_governance_poc_mvp.ipynb) |

### 🏎️ Fast track

| Notebook | Open |
|---|---|
| `00_fast_track_onboarding.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/00_fast_track_onboarding.ipynb) |
| `01_python_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/01_python_basics.ipynb) |
| `02_control_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/02_control_structures.ipynb) |
| `03_lists_and_dicts.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/03_lists_and_dicts.ipynb) |
| `04_functions.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/04_functions.ipynb) |
| `05_classes_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/05_classes_basics.ipynb) |
| `06_pandas_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/06_pandas_fundamentals.ipynb) |
| `07_visualization_and_stats.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/07_visualization_and_stats.ipynb) |
| `08_sklearn_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/08_sklearn_basics.ipynb) |
| `09_apis_and_sql.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/09_apis_and_sql.ipynb) |
| `10_ai_workflows.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/10_ai_workflows.ipynb) |
| `11_embeddings_and_rag.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/11_embeddings_and_rag.ipynb) |
| `12_tools_and_agents.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/12_tools_and_agents.ipynb) |
| `13_notebook_to_project.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/13_notebook_to_project.ipynb) |
| `14_agents_and_mcp.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/fast_track/14_agents_and_mcp.ipynb) |

### 🧠 Quizzes

| Notebook | Open |
|---|---|
| `quiz_01_foundations.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_01_foundations.ipynb) |
| `quiz_02_data_science.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_02_data_science.ipynb) |
| `quiz_03_real_world_io.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_03_real_world_io.ipynb) |
| `quiz_04_machine_learning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_04_machine_learning.ipynb) |
| `quiz_06_ai_engineering.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_06_ai_engineering.ipynb) |
| `quiz_11_production.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_11_production.ipynb) |
| `quiz_14_business_ai.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_14_business_ai.ipynb) |
| `quiz_07_building_ai_pocs.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_07_building_ai_pocs.ipynb) |
| `quiz_05_industry_applications.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_05_industry_applications.ipynb) |
| `quiz_08_agents_tools_mcp.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/Python-for-AI-Driven-Automation/blob/main/quizzes/quiz_08_agents_tools_mcp.ipynb) |

---

## 🤝 Contributing & licence

Spotted a bug or an unclear explanation? **Open an issue or PR** — contributions are welcome.

Licensed under the **MIT License** (see [`LICENSE`](./LICENSE)) — use freely for learning, teaching, or anything else.

<p align="center"><sub>Happy coding 🚀</sub></p>
