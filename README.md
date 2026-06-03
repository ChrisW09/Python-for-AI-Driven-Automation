# Python for AI-Driven Automation and Business Data Science
## *9 modules, 34 notebooks (+ 11 optional appendices), end-to-end*

A modern, hands-on, self-paced course that takes you from your first line of Python to **shipping a real AI-driven automation** — Python fluency, business data science, machine learning, AI engineering, and production wiring, all in one curriculum.

> 🚀 **Start here:** [`00_onboarding/00_master_onboarding.ipynb`](./00_onboarding/00_master_onboarding.ipynb)
> 👀 **See it work first (5 min):** [`00_onboarding/00c_see_it_work.ipynb`](./00_onboarding/00c_see_it_work.ipynb) — a tiny *offline* demo of AI triage + RAG + a KPI snapshot, so you can see what you'll build before the Python begins.
> 🗺️  **Then the full map:** [`00_onboarding/00b_course_overview.ipynb`](./00_onboarding/00b_course_overview.ipynb) — module-map diagram, per-notebook time budgets, learning paths, interactive time estimator.
> 🏎️ **Tight on time?** Take the [Fast Track](./fast_track/) — 9 essential notebooks, about 10 hours total. Same teaching, Stretch and Bonus sections trimmed off.
> 📊 **Slide-deck version:** [`slides/00_course_overview.pdf`](./slides/00_course_overview.pdf)

---

## What's in this repo

| Folder | What |
|---|---|
| `00_onboarding/` … `09_building_ai_pocs/` | **The full course.** 34 main notebooks + 11 optional appendices, organised by topic. |
| `fast_track/` | **The fast track.** 9 trimmed notebooks (~10 h total) for a quick end-to-end pass at the essentials. |
| `quizzes/` | **Module quizzes.** 6 short multiple-choice quizzes (5 questions each, ~10 min) — one per module — to check what stuck. |
| `data/` | The three sample CSVs the notebooks read (support_ops, api_log, customer_feedback). |
| `slides/` | A 25-slide course-overview deck (PDF + LaTeX source). |
| `scripts/` | Local helper scripts — run every notebook end-to-end or check that NB-number references in the docs resolve to real files. Use them whenever you want a sanity-check pass. |
| `docs/` | Audit reports from the 2026 refinement pass + most recent execution snapshot. Reference material — not part of the course itself. |
| `llm_providers.py` | Unified interface to OpenAI / Anthropic / Google / Ollama (and an offline `MockLLM`). |
| `previous_versions/` | The legacy flat 19-notebook layout (pre-2026 refinement), preserved for archive purposes only. |

---

## The modules

### 📍 [Module 0 — Onboarding](./00_onboarding/) *(start here)*
*Master onboarding notebook + environment check.* 20 minutes.

### 🐍 [Module 1 — Foundations](./01_foundations/) *(NB 1–6)*
Python you can read without friction. Variables, control flow, lists, dicts, functions.

### 📊 [Module 2 — Data Science](./02_data_science/) *(NB 7–11)*
pandas, NumPy, matplotlib, **statistics**, time series. The analytical core.

### 🔌 [Module 3 — Real-world I/O](./03_real_world_io/) *(NB 12–13)*
HTTP requests, SQL, Pydantic validation. Pull real data from anywhere; refuse bad data at the boundary. *(Pydantic validation is folded into NB 13.)*

### 🤖 [Module 4 — Machine Learning](./04_machine_learning/) *(NB 14–16)*
scikit-learn workflow + **honest model evaluation** + **feature engineering**.

### 🧠 [Module 5 — AI Engineering](./05_ai_engineering/) *(NB 17–21)*
LLM prompts, RAG, agents, document processing, **AI evaluation & observability**.

### 🚀 [Module 6 — Production](./06_production/) *(NB 22–23)*
Packaging notebooks into projects and scheduling. *(Configuration & secrets are covered inline in NB 22.)*

### 🏆 [Module 7 — Capstones](./07_capstones/) *(NB 24–25)*
Two end-to-end projects — analytical and engineering.

### 🏢 [Module 8 — Business AI in Practice](./08_business_ai/) *(NB 26–29)*
Digital transformation context, architecture patterns, AI-assisted software development, BPM integration + governance + POC→MVP→Production. The seminar half of the course — pairs the technical fluency of Modules 1–7 with the judgement to deploy it inside organisations.

### 🛠️ [Module 9 — Building AI POCs (hands-on)](./09_building_ai_pocs/) *(NB 30–34)*
The applied deep-dive companion: LLM fundamentals (Transformer math), VS Code + Copilot setup and vibe coding, three POCs of growing complexity (Streamlit → 3-tier → ML pipeline), RAG pipeline deep dive with a RAG-over-PDF POC, vector databases + agentic AI with a Chroma semantic-search POC and a ReAct command-line agent. Every notebook ends with a paste-ready Copilot Agent Mode prompt — designed so the whole course can be taught from the notebooks alone.

---

## Five high-impact notebooks worth singling out

| # | Notebook | What it teaches |
|---|---|---|
| **10** | `10_statistics_basics.ipynb` | Confidence intervals, t-tests, Cohen's *d*, sample-size planning, A/B-test reporting that survives a stakeholder review. |
| **15** | `15_model_evaluation.ipynb` | Confusion matrices in cost units, threshold tuning, ROC/PR curves, **calibration**, learning curves. |
| **16** | `16_feature_engineering.ipynb` | Encoding strategies, scaling, datetime features, **target leakage**, feature selection, custom transformers. |
| **21** | `21_ai_evaluation_observability.ipynb` | Golden datasets, LLM-as-judge, tracing, cost dashboards, A/B testing prompts, regression detection. |
| **25** | `25_capstone_ai_assistant.ipynb` | An end-to-end AI feature combining everything from Modules 5 + 6. |

---

## Optional appendix track — 11 advanced notebooks

A second tier of optional, deep-dive notebooks for readers who want to go beyond the 34-notebook backbone. Each appendix lives next to its parent module and is fully runnable. Unlike the main notebooks, appendices are written as **reference notebooks**: they ship with pre-rendered outputs only when noted in their first cell, focus on demonstrating libraries rather than interactive exercises, and skip the Solution/Debug-me scaffolding.

| Module | Appendix | What it covers |
|---|---|---|
| 02 Data Science | `A1_forecasting_classical.ipynb` | ARIMA / SARIMA / ETS deep dive |
| 02 Data Science | `A2_forecasting_prophet_libraries.ipynb` | Prophet, NeuralProphet, sktime, Darts |
| 02 Data Science | `A3_forecasting_deep_learning.ipynb` | LSTM + Transformer forecasters in PyTorch |
| 02 Data Science | `A4_forecasting_foundation_models.ipynb` | TimesFM, Chronos, TabPFN-TS |
| 04 ML | `A1_pytorch_foundations.ipynb` | Tensors, autograd, MLPs |
| 04 ML | `A2_pytorch_vision_and_sequences.ipynb` | CNNs, RNNs, Transformers |
| 04 ML | `A3_pytorch_fine_tuning.ipynb` | Transfer learning + LoRA |
| 04 ML | `A4_tabpfn_priorlab.ipynb` | TabPFN tabular foundation model + cloud API |
| 05 AI Eng | `A1_llm_providers_guide.ipynb` | OpenAI / Anthropic / Google / Ollama |
| 05 AI Eng | `A2_vector_stores_survey.ipynb` | FAISS, Chroma, Qdrant, Weaviate, pgvector |
| 05 AI Eng | `A3_rag_and_agent_frameworks.ipynb` | LangChain, LlamaIndex, Haystack, agents |

---

## Learning paths

Match yourself to the path that fits:

| You are | You'll touch | Time |
|---|---|---|
| **Complete beginner** | All modules, in **spiral order** (orientation → skills → build → deploy → capstone) | ~90 h |
| **Analyst** (knows Excel/SQL) | Modules 0, 2, 3, 4, 7 | ~30 h |
| **Developer** (knows another language) | Modules 0, 2, 3, 4, 5, 6, 9, 7 | ~55 h |
| **ML practitioner** | Modules 0, 5, 6, 9, 7 | ~25 h |
| **Manager** (curious) | Module 0 (incl. `00c`) + 8 + 7 | ~10 h |

The times above are rough — the **interactive estimator** in [`00b_course_overview.ipynb`](./00_onboarding/00b_course_overview.ipynb) computes the exact total for *your* path, and the spiral order is spelled out in the master onboarding. The course-overview deck has these paths visualised — open it before you pick.

---

## How each notebook is structured

Every notebook follows the same six-section template:

1. **🎯 Learning objectives** + **✅ Prerequisites**
2. **Numbered concept sections** — short prose, then runnable code.
3. **🧪 Practice exercises** (numbered 1, 2, 3, …) — 3–5 per notebook, with full solutions and *reasoning* (not just the answer). One per notebook is a 🐞 *Debug-me* puzzle.
4. **🧠 Stretch exercises** (lettered A, B, C, D) — 4 per notebook, deliberately harder. The kind of question you'd want to be able to answer in an interview. Same Solution + Reasoning format as the practice exercises.
5. **🎁 Bonus mini-project** — one larger applied task.
6. **✅ Self-assessment checklist** + **🚀 Next step** — pointer to the next notebook in your path.

That's **~8 exercises per notebook on average** — and **180+ across the course**, every single one with a worked solution and an explanation of *why* it works.

The nine visual markers (💡 tip, 🎯 intuition, ⚠️ pitfall, 🧪 exercise, 🎁 bonus, 🐞 debug-me, 🧠 mental-model, 🔭 forward-reference, ⭐/⭐⭐/⭐⭐⭐ difficulty) are road signs you'll see throughout. They are explained in the onboarding notebook.

---

## How to study a notebook — the five-step loop

```
   Read  →  Run  →  Try  →  Tweak  →  Predict
     │              │
     │              └── try every exercise before clicking the solution
     └────────── read the prose before looking at the code
```

Apply this to every notebook. Five minutes of genuine struggle beats five hours of passive reading.

---

## Setup

### Google Colab *(easiest)*
Upload any notebook. Done. All required libraries are pre-installed.

### Local Jupyter
```bash
python -m venv .venv
source .venv/bin/activate         # macOS / Linux
.venv\Scripts\activate            # Windows
pip install -r requirements.txt
jupyter lab
```

Tested with Python 3.10+. Module 0 includes an environment-check cell.

---

## What you'll build by the end

Six smaller artefacts along the way (KPI snapshot, ETL pipeline, SQL report, forecast, inbox triage, scheduled job) **plus two big capstones**:

- 🏆 **Capstone A — AI Support-Bot Analytics** *(NB 24)*: 5 channels × 12 months → 2×2 dashboard → Simpson's-paradox demo → executive summary.
- 🏆 **Capstone B — AI Customer-Feedback Assistant** *(NB 25)*: classification + validation + RAG + scheduled orchestration + cost dashboard + eval gate.

You can talk through either of these as "a project I built" in an interview.

---

## Course philosophy

A few principles that guided every notebook:

- **Explain *why*, not just *how*.** Code without intuition is fragile.
- **Show real examples.** Tip calculators teach syntax; KPI parsers teach the job.
- **Practice over passive reading.** Every concept gets exercises *with reasoning*.
- **Modern tools, modern habits.** Type hints, virtual envs, validation, pytest, observability.
- **AI as a tool, not magic.** LLMs are function calls; calibration matters.

---

## What's *not* in the course

So you're not surprised later:

- ❌ Deep learning from scratch (PyTorch / TF training loops). You'll *use* pre-trained models — which is what most working AI applications need.
- ❌ Vendor-specific cloud deployment (AWS / GCP / Azure). NB 23 teaches the *patterns* of scheduling — without committing to one platform.
- ❌ Vector-database deep dive. NB 18 implements the underlying retrieval logic and points you at Qdrant / Weaviate / Pinecone for the production scale-up.

These are conscious trade-offs.

---

## LLM providers — local and hosted, four options

Notebooks 17 – 21 and 25 can be run **entirely offline** with the built-in `MockLLM`. When you're ready for real intelligence, swap one line. The course supports four providers through a unified interface in [`llm_providers.py`](./llm_providers.py):

| Provider | Class | When |
|---|---|---|
| 🟢 OpenAI    | `OpenAILLM(model="gpt-4o-mini")` | Reliable default. |
| 🟠 Anthropic | `AnthropicLLM(model="claude-haiku-4-5-20251001")` | Long context, careful tone. |
| 🔵 Google    | `GoogleLLM(model="gemini-2.0-flash")` | Cheap at scale. |
| 🟣 Ollama    | `OllamaLLM(model="llama3.2:3b")` | **Local** — no internet, no key, no cost. |

```bash
# For hosted providers, set the corresponding env var (never inline):
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...
# Ollama: `ollama pull llama3.2:3b` once, then `ollama serve` (auto-starts on macOS).
```

📓 **See [`05_ai_engineering/A1_llm_providers_guide.ipynb`](./05_ai_engineering/A1_llm_providers_guide.ipynb)** for setup, model recommendations, cost estimates, and a decision table.

> ⚠️ **Never commit API keys to git.** The notebooks are designed so you don't have to touch a key inside the notebook itself.

---

## Layout at a glance

```
.
├── README.md                       ← you are here
├── requirements.txt
├── LICENSE
├── llm_providers.py
│
├── 00_onboarding/
│   ├── README.md
│   ├── 00_master_onboarding.ipynb
│   └── 00b_course_overview.ipynb
│
├── 01_foundations/         ← NB 1–6: Python basics, control, lists, dicts, functions, classes & OOP
├── 02_data_science/        ← NB 7–11: pandas, NumPy, plots, stats, time series  (+ A1–A4 forecasting appendices)
├── 03_real_world_io/       ← NB 12–13: HTTP, SQL + Pydantic validation
├── 04_machine_learning/    ← NB 14–16: sklearn, evaluation, feature engineering  (+ A1–A4 PyTorch / TabPFN appendices)
├── 05_ai_engineering/      ← NB 17–21: prompts, RAG, agents, docs, AI evaluation  (+ A1–A3 provider / vector-store / framework appendices)
├── 06_production/          ← NB 22–23: packaging, scheduling  (config & secrets inline in NB 22)
├── 07_capstones/           ← NB 24: analytics  +  NB 25: AI assistant
├── 08_business_ai/         ← NB 26–29: digital transformation, architecture, AI-assisted dev, BPM + governance + cases
├── 09_building_ai_pocs/    ← NB 30–34: LLM theory, Copilot setup, three POCs, RAG deep dive, vector DBs + agents
│
├── fast_track/                     ← 9 trimmed notebooks (~10 h) — the shortcut path
│
├── quizzes/                        ← 6 multiple-choice quizzes, one per module
│
├── slides/                         ← HSBI Beamer decks (see slides/README.md)
│   ├── 00_course_overview.pdf     ← 25-slide onboarding deck
│   ├── 26–30 *.pdf                 ← 5 lecture decks for the conceptual lectures (Module 8 + LLM fundamentals)
│   └── images/                     ← 7 overview figures
│
├── data/                           ← 3 sample CSVs (support_ops, api_log, customer_feedback)
│
├── scripts/
│   ├── check_nb_references.py     ← link checker for NB-number references in docs
│   └── run_all_notebooks.py       ← execute every notebook end-to-end (for local sanity checks)
│
├── docs/                          ← audit reports + most recent execution snapshot
│
└── previous_versions/
    └── flat_19_notebook_layout/   ← the pre-2026 flat layout, kept for archive only
```

---

## About the previous_versions/ folder

Before the 2026 refinement pass, the course shipped as a flat list of 19 notebooks at the top level (`01_python_basics.ipynb` … `19_scheduling_orchestration.ipynb`) alongside their own `data/`, `slides/`, and `requirements.txt`. That layout is preserved verbatim in `previous_versions/flat_19_notebook_layout/` so old bookmarks keep working, but **the canonical course is the 9-module structure at the top level** — start there.

---

## Contributing & feedback

The course gets better when real readers tell us what didn't land. If you spot a bug, an unclear explanation, or a missing example, please open an issue or pull request.

## Licence

MIT — see `LICENSE`. Use freely for personal learning, teaching, or any other purpose.

Happy coding.
