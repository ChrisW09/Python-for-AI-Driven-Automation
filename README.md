# Python for AI-Driven Automation and Business Data Science

*From your first line of Python to shipping a real AI-driven automation — Python fluency, business data science, machine learning, AI engineering, and production wiring in one hands-on, self-paced curriculum.*

**10 modules · 38 notebooks (+ 11 optional appendices) · end-to-end**

---

## Two ways to take it

There are two learning paths — pick one:

### 🎓 Complete course — *the full depth*
All 10 modules / 38 notebooks (plus 11 optional appendices), worked in spiral order with every exercise, stretch problem, and capstone. **~105 hours.**
→ **Start:** [`00_onboarding/00_master_onboarding.ipynb`](./00_onboarding/00_master_onboarding.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00_master_onboarding.ipynb)

### 🏎️ Fast track — *the essentials, condensed*
The same teaching trimmed to **13 notebooks, ~14 hours** — a credible end-to-end pass you can finish in a few weeks of evenings (Stretch A/B and the bonus projects removed).
→ **Start:** [`fast_track/00_fast_track_onboarding.ipynb`](./fast_track/00_fast_track_onboarding.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/00_fast_track_onboarding.ipynb)

New here? The 5-minute offline demo [`00c_see_it_work.ipynb`](./00_onboarding/00c_see_it_work.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00c_see_it_work.ipynb) shows what you'll build before the Python begins, and [`00b_course_overview.ipynb`](./00_onboarding/00b_course_overview.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00b_course_overview.ipynb) has the full module map and an interactive time estimator.

---

## The modules (complete course)

| Module | NB | Focus |
|---|---|---|
| 0 · Onboarding | — | Setup, orientation, 5-min demo |
| 1 · Foundations | 1–6 | Variables, control flow, lists, dicts, functions, classes |
| 2 · Data Science | 7–11 | pandas, NumPy, matplotlib, statistics, time series |
| 3 · Real-world I/O | 12–13 | HTTP/APIs, SQL, data validation |
| 4 · Machine Learning | 14–16 | scikit-learn, model evaluation, feature engineering |
| 5 · AI Engineering | 17–21 | prompts, RAG, agents, document processing, AI eval & observability |
| 6 · Production | 22–23 | packaging notebooks into projects, scheduling |
| 7 · Capstones | 24–25 | two end-to-end projects (analytics + AI assistant) |
| 8 · Business AI | 26–29 | digital transformation, architecture, AI-assisted dev, governance |
| 9 · Building AI POCs | 30–34 | LLM theory, Copilot setup, three POCs, RAG deep dive, vector DBs + agents |
| 10 · Industry Applications | 35–38 | churn/CLV, fraud, segmentation + recommenders, demand & maintenance |

11 optional **appendices** (classical → deep-learning → foundation-model forecasting, PyTorch, vector stores, RAG/agent frameworks) live beside their modules — all runnable offline.

---

## What's in the repo

| Folder | What |
|---|---|
| `00_onboarding/` … `10_industry_applications/` | The complete course — 38 notebooks + 11 optional appendices. |
| `fast_track/` | The fast track — 13 trimmed notebooks (~14 h). |
| `quizzes/` | 9 short multiple-choice quizzes (Modules 1–6 & 8–10). |
| `data/` | The three sample CSVs the notebooks read (support_ops, api_log, customer_feedback). |
| `slides/` | Course-overview deck + lecture decks (PDF + LaTeX source). |
| `scripts/` | Local helpers to run every notebook end-to-end or check NB-number references. |
| `llm_providers.py` | Unified interface to OpenAI / Anthropic / Google / Ollama (+ offline `MockLLM`). |
| `previous_versions/` | The legacy flat 19-notebook layout, archived. |

---

## How each notebook is structured

A consistent six-part template: **🎯 objectives + ✅ prerequisites → numbered concept sections (prose + runnable code) → 🧪 practice exercises (incl. a 🐞 debug-me) → 🧠 stretch exercises A–D → 🎁 bonus mini-project → ✅ self-assessment + 🚀 next step.** Every exercise — **300+ across the course** — ships with a worked solution and the *reasoning* behind it.

---

## Setup

**Google Colab (easiest):** click the **“Open in Colab”** badge at the top of any notebook — it opens straight from GitHub, no download, and the required libraries are pre-installed. Or use the [**Open-in-Colab index**](#-open-any-notebook-in-colab) below to jump straight to any notebook.

**Local Jupyter:**
```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```
Tested with Python 3.10+. Module 0 includes an environment-check cell.

The 11 optional appendices demo heavier libraries (PyTorch, Prophet, FAISS, LangChain, …), listed commented-out at the bottom of `requirements.txt`. Each still runs offline via a built-in stand-in, so install them only to see the real library at work.

---

## LLM providers

Notebooks 17–21 and 25 run **entirely offline** with the built-in `MockLLM`. For real intelligence, swap one line — the unified interface in [`llm_providers.py`](./llm_providers.py) supports four providers:

| Provider | Class | When |
|---|---|---|
| 🟢 OpenAI | `OpenAILLM(model="gpt-4o-mini")` | Reliable default |
| 🟠 Anthropic | `AnthropicLLM(model="claude-haiku-4-5-20251001")` | Long context, careful tone |
| 🔵 Google | `GoogleLLM(model="gemini-2.0-flash")` | Cheap at scale |
| 🟣 Ollama | `OllamaLLM(model="llama3.2:3b")` | Local — no internet, key, or cost |

Set the matching `*_API_KEY` env var for hosted providers (never inline). See [`05_ai_engineering/A1_llm_providers_guide.ipynb`](./05_ai_engineering/A1_llm_providers_guide.ipynb) for setup and cost notes. **Never commit API keys.**

---

## 🚀 Open any notebook in Colab

Every notebook runs in [Google Colab](https://colab.research.google.com/) with one click — no install, no download. Expand a module and click a badge.

<details>
<summary><b>0 · Onboarding</b></summary>

| Notebook | Colab |
|---|---|
| `00_master_onboarding.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00_master_onboarding.ipynb) |
| `00b_course_overview.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00b_course_overview.ipynb) |
| `00c_see_it_work.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/00_onboarding/00c_see_it_work.ipynb) |

</details>

<details>
<summary><b>1 · Foundations</b></summary>

| Notebook | Colab |
|---|---|
| `01_python_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/01_python_basics.ipynb) |
| `02_control_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/02_control_structures.ipynb) |
| `03_lists_data_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/03_lists_data_structures.ipynb) |
| `04_dictionaries_advanced.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/04_dictionaries_advanced.ipynb) |
| `05_functions_modules.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/05_functions_modules.ipynb) |
| `06_classes_and_oop.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/01_foundations/06_classes_and_oop.ipynb) |

</details>

<details>
<summary><b>2 · Data Science</b></summary>

| Notebook | Colab |
|---|---|
| `07_pandas_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/07_pandas_fundamentals.ipynb) |
| `08_numpy_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/08_numpy_fundamentals.ipynb) |
| `09_matplotlib_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/09_matplotlib_basics.ipynb) |
| `10_statistics_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/10_statistics_basics.ipynb) |
| `11_time_series_forecasting.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/11_time_series_forecasting.ipynb) |
| `A1_forecasting_classical.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/A1_forecasting_classical.ipynb) |
| `A2_forecasting_prophet_libraries.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/A2_forecasting_prophet_libraries.ipynb) |
| `A3_forecasting_deep_learning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/A3_forecasting_deep_learning.ipynb) |
| `A4_forecasting_foundation_models.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/02_data_science/A4_forecasting_foundation_models.ipynb) |

</details>

<details>
<summary><b>3 · Real-world I/O</b></summary>

| Notebook | Colab |
|---|---|
| `12_apis_and_http.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/03_real_world_io/12_apis_and_http.ipynb) |
| `13_sql_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/03_real_world_io/13_sql_fundamentals.ipynb) |

</details>

<details>
<summary><b>4 · Machine Learning</b></summary>

| Notebook | Colab |
|---|---|
| `14_sklearn_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/14_sklearn_basics.ipynb) |
| `15_model_evaluation.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/15_model_evaluation.ipynb) |
| `16_feature_engineering.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/16_feature_engineering.ipynb) |
| `A1_pytorch_foundations.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/A1_pytorch_foundations.ipynb) |
| `A2_pytorch_vision_and_sequences.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/A2_pytorch_vision_and_sequences.ipynb) |
| `A3_pytorch_fine_tuning.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/A3_pytorch_fine_tuning.ipynb) |
| `A4_tabpfn_priorlab.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/04_machine_learning/A4_tabpfn_priorlab.ipynb) |

</details>

<details>
<summary><b>5 · AI Engineering</b></summary>

| Notebook | Colab |
|---|---|
| `17_ai_workflows.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/17_ai_workflows.ipynb) |
| `18_embeddings_retrieval.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/18_embeddings_retrieval.ipynb) |
| `19_tools_and_agents.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/19_tools_and_agents.ipynb) |
| `20_document_processing.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/20_document_processing.ipynb) |
| `21_ai_evaluation_observability.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/21_ai_evaluation_observability.ipynb) |
| `A1_llm_providers_guide.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/A1_llm_providers_guide.ipynb) |
| `A2_vector_stores_survey.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/A2_vector_stores_survey.ipynb) |
| `A3_rag_and_agent_frameworks.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/05_ai_engineering/A3_rag_and_agent_frameworks.ipynb) |

</details>

<details>
<summary><b>6 · Production</b></summary>

| Notebook | Colab |
|---|---|
| `22_from_notebook_to_project.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/06_production/22_from_notebook_to_project.ipynb) |
| `23_scheduling_orchestration.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/06_production/23_scheduling_orchestration.ipynb) |

</details>

<details>
<summary><b>7 · Capstones</b></summary>

| Notebook | Colab |
|---|---|
| `24_capstone_analytics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/07_capstones/24_capstone_analytics.ipynb) |
| `25_capstone_ai_assistant.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/07_capstones/25_capstone_ai_assistant.ipynb) |

</details>

<details>
<summary><b>8 · Business AI</b></summary>

| Notebook | Colab |
|---|---|
| `26_digital_transformation.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/08_business_ai/26_digital_transformation.ipynb) |
| `27_architecture_patterns.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/08_business_ai/27_architecture_patterns.ipynb) |
| `28_ai_assisted_software_development.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/08_business_ai/28_ai_assisted_software_development.ipynb) |
| `29_bpm_governance_poc_mvp.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/08_business_ai/29_bpm_governance_poc_mvp.ipynb) |

</details>

<details>
<summary><b>9 · Building AI POCs</b></summary>

| Notebook | Colab |
|---|---|
| `30_llm_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/09_building_ai_pocs/30_llm_fundamentals.ipynb) |
| `31_from_setup_to_first_poc.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/09_building_ai_pocs/31_from_setup_to_first_poc.ipynb) |
| `32_three_pocs_growing_complexity.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/09_building_ai_pocs/32_three_pocs_growing_complexity.ipynb) |
| `33_rag_pipeline_deep_dive.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/09_building_ai_pocs/33_rag_pipeline_deep_dive.ipynb) |
| `34_vector_db_and_agentic_ai.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/09_building_ai_pocs/34_vector_db_and_agentic_ai.ipynb) |

</details>

<details>
<summary><b>10 · Industry Applications</b></summary>

| Notebook | Colab |
|---|---|
| `35_churn_clv_retention.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/10_industry_applications/35_churn_clv_retention.ipynb) |
| `36_fraud_anomaly_detection.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/10_industry_applications/36_fraud_anomaly_detection.ipynb) |
| `37_segmentation_recommenders.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/10_industry_applications/37_segmentation_recommenders.ipynb) |
| `38_demand_maintenance.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/10_industry_applications/38_demand_maintenance.ipynb) |

</details>

<details>
<summary><b>🏎️ Fast track</b></summary>

| Notebook | Colab |
|---|---|
| `00_fast_track_onboarding.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/00_fast_track_onboarding.ipynb) |
| `01_python_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/01_python_basics.ipynb) |
| `02_control_structures.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/02_control_structures.ipynb) |
| `03_lists_and_dicts.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/03_lists_and_dicts.ipynb) |
| `04_functions.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/04_functions.ipynb) |
| `05_classes_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/05_classes_basics.ipynb) |
| `06_pandas_fundamentals.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/06_pandas_fundamentals.ipynb) |
| `07_visualization_and_stats.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/07_visualization_and_stats.ipynb) |
| `08_sklearn_basics.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/08_sklearn_basics.ipynb) |
| `09_apis_and_sql.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/09_apis_and_sql.ipynb) |
| `10_ai_workflows.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/10_ai_workflows.ipynb) |
| `11_embeddings_and_rag.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/11_embeddings_and_rag.ipynb) |
| `12_tools_and_agents.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/12_tools_and_agents.ipynb) |
| `13_notebook_to_project.ipynb` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChrisW09/python-ai-business-data-science/blob/main/fast_track/13_notebook_to_project.ipynb) |

</details>

---

## Contributing & licence

Spotted a bug or an unclear explanation? Open an issue or PR. Licensed **MIT** (see `LICENSE`) — use freely for learning, teaching, or anything else.

Happy coding.
