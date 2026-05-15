# Python for AI-Driven Automation and Business Data Science
## *Refined edition — 7 modules, 25 notebooks, end-to-end*

A modern, hands-on, self-paced course that takes you from your first line of Python to **shipping a real AI-driven automation**. This is the **refined edition** — the same business-AI-flavoured course you may know, restructured into a coherent module-based curriculum with five new notebooks closing real gaps and a dedicated onboarding deck.

> 🚀 **Start here:** [`00_onboarding/00_master_onboarding.ipynb`](./00_onboarding/00_master_onboarding.ipynb)
> 📊 **The roadmap:** [`slides/00_course_overview.pdf`](./slides/00_course_overview.pdf)

---

## Why a refined edition?

The original 19-notebook course had everything you needed but was organised as a flat list of files. The refined edition does three things on top:

| Was | Now |
|---|---|
| Flat list of 19 notebooks | **7 thematic modules** with per-module READMEs |
| No onboarding | Dedicated **Module 0** + 23-slide overview deck |
| Missing: stats, model evaluation, feature engineering, AI evaluation, second capstone | **5 new notebooks** filling those gaps |
| Linear progression assumed | **5 learning paths** for different audiences |
| One capstone | **Two capstones** — analytical + engineering twins |

The original course remains untouched in the parent directory. This `refined_course/` folder is the evolved version.

---

## The 7 modules

### 📍 [Module 0 — Onboarding](./00_onboarding/) *(start here)*
*Master onboarding notebook + environment check.* 20 minutes.

### 🐍 [Module 1 — Foundations](./01_foundations/) *(NB 1–5)*
Python you can read without friction. Variables, control flow, lists, dicts, functions.

### 🔌 [Module 2 — Real-world I/O](./02_real_world_io/) *(NB 7–9)*
HTTP requests, SQL, Pydantic validation. Pull real data from anywhere; refuse bad data at the boundary.

### 📊 [Module 3 — Data Science](./03_data_science/) *(NB 10–14)*
pandas, NumPy, matplotlib, **statistics**, time series. The analytical core.

### 🤖 [Module 4 — Machine Learning](./04_machine_learning/) *(NB 15–17)*
scikit-learn workflow + **honest model evaluation** + **feature engineering**.

### 🧠 [Module 5 — AI Engineering](./05_ai_engineering/) *(NB 18–22)*
LLM prompts, RAG, agents, document processing, **AI evaluation & observability**.

### 🚀 [Module 6 — Production](./06_production/) *(NB 23–24)*
Packaging notebooks into projects, scheduling, configuration & secrets.

### 🏆 [Module 7 — Capstones](./07_capstones/) *(NB 26–27)*
Two end-to-end projects — analytical and engineering.

---

## What's *new* in the refined edition

Five high-impact notebooks that close gaps in the original:

| # | New notebook | What it teaches |
|---|---|---|
| **13** | `13_statistics_basics.ipynb` | Confidence intervals, t-tests, Cohen's *d*, sample-size planning, A/B-test reporting that survives a stakeholder review. |
| **16** | `16_model_evaluation.ipynb` | Confusion matrices in cost units, threshold tuning, ROC/PR curves, **calibration**, learning curves. |
| **17** | `17_feature_engineering.ipynb` | Encoding strategies, scaling, datetime features, **target leakage**, feature selection, custom transformers. |
| **22** | `22_ai_evaluation_observability.ipynb` | Golden datasets, LLM-as-judge, tracing, cost dashboards, A/B testing prompts, regression detection. |
| **27** | `27_capstone_ai_assistant.ipynb` | An end-to-end AI feature combining everything from Modules 5 + 6. |

Plus the **master onboarding notebook**, **7 per-module READMEs** with diagrams, and a **23-slide course-overview deck**.

---

## Learning paths

Match yourself to the path that fits:

| You are | You'll touch | Time |
|---|---|---|
| **Complete beginner** | All 7 modules in order | ~35 h |
| **Analyst** (knows Excel/SQL) | Modules 0, 2, 3, 4, 7 | ~20 h |
| **Developer** (knows another language) | Modules 0, 2, 3, 4, 5, 6, 7 | ~28 h |
| **ML practitioner** | Modules 0, 5, 6, 7 | ~15 h |
| **Manager** (curious) | Module 0 + 7 only | ~8 h |

The course-overview deck has these paths visualised — open it before you pick.

---

## How each notebook is structured

Every notebook follows the same six-section template:

1. **🎯 Learning objectives** + **✅ Prerequisites**
2. **Numbered concept sections** — short prose, then runnable code.
3. **🧪 Exercises** — with full solutions and *reasoning* (not just the answer).
4. **🎁 Bonus mini-project** — one larger applied task.
5. **🧠 Key takeaways** + **✅ Self-assessment checklist**.
6. **🚀 Next step** — pointer to the next notebook in your path.

The six visual markers (💡 tip, 🎯 intuition, ⚠️ pitfall, 🧪 exercise, 🎁 bonus, 🐞 debug-me) are road signs you'll see throughout. They are explained in the onboarding notebook.

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

- 🏆 **Capstone A — AI Support-Bot Analytics** *(NB 26)*: 5 channels × 12 months → 2×2 dashboard → Simpson's-paradox demo → executive summary.
- 🏆 **Capstone B — AI Customer-Feedback Assistant** *(NB 27)*: classification + validation + RAG + scheduled orchestration + cost dashboard + eval gate.

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
- ❌ Vendor-specific cloud deployment (AWS / GCP / Azure). NB 24 teaches the *patterns* of scheduling — without committing to one platform.
- ❌ Vector-database deep dive. NB 19 implements the underlying retrieval logic and points you at Qdrant / Weaviate / Pinecone for the production scale-up.

These are conscious trade-offs.

---

## LLM providers — local and hosted, four options

Notebooks 18 – 22 and 27 can be run **entirely offline** with the built-in `MockLLM`. When you're ready for real intelligence, swap one line. The course supports four providers through a unified interface in [`llm_providers.py`](./llm_providers.py):

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

## Files in this folder

```
refined_course/
├── README.md                       ← you are here
├── requirements.txt
├── LICENSE
│
├── 00_onboarding/
│   ├── README.md
│   └── 00_master_onboarding.ipynb
│
├── 01_foundations/         ← NB 1–5: Python basics, control, lists, dicts, functions
├── 02_real_world_io/       ← NB 7–8: HTTP, SQL  (NB 9 reserved for Pydantic)
├── 03_data_science/        ← NB 10–14: pandas, NumPy, plots, stats, time series
├── 04_machine_learning/    ← NB 15–17: sklearn, evaluation, feature engineering
├── 05_ai_engineering/      ← NB 18–22: prompts, RAG, agents, docs, AI evaluation
├── 06_production/          ← NB 23–24: packaging, scheduling  (NB 25 reserved for config)
├── 07_capstones/           ← NB 26: analytics  +  NB 27: AI assistant
│
├── slides/
│   ├── 00_course_overview.pdf     ← 23-slide onboarding deck
│   └── images/                     ← 7 overview figures
│
└── data/                           ← 3 sample CSVs (support_ops, api_log, customer_feedback)
```

---

## How this relates to the original course

The parent folder still contains the original 19-notebook course as-is. The refined edition:

- Reorganises the same 19 notebooks into the 7-module structure (no content rewrite — copies of the originals).
- Adds 5 new notebooks (13, 16, 17, 22, 27) covering genuine gaps.
- Adds 1 onboarding notebook (00).
- Adds the course-overview slide deck (separate from the existing technical deck).
- Adds 7 per-module READMEs with diagrams.

You can take the refined edition as the recommended path, or use the original 19-notebook layout if you prefer to learn in a linear order.

---

## Contributing & feedback

The course gets better when real readers tell us what didn't land. If you spot a bug, an unclear explanation, or a missing example, please open an issue or pull request.

## Licence

MIT — see `LICENSE`. Use freely for personal learning, teaching, or any other purpose.

Happy coding.
