# Python for AI-Driven Automation and Business Data Science

A modern, hands-on, self-paced course that takes you from your first line of Python to **shipping a real AI-powered automation**.

```
   ┌──────────────────────────────────────────────────────────────────────────┐
   │  25 notebooks (refined edition)  •  ~500 code cells                       │
   │  ~80 exercises with detailed worked solutions                             │
   │  Runs on Google Colab with zero setup                                     │
   │  AI workflows included — fully offline with a built-in MockLLM            │
   │  Real HTTP, SQL, time series, embeddings, agents, packaging, scheduling   │
   └──────────────────────────────────────────────────────────────────────────┘
```

> 🚀 **Start here:** [`refined_course/00_onboarding/00_master_onboarding.ipynb`](./refined_course/00_onboarding/00_master_onboarding.ipynb)
>
> 📊 **The course in one diagram:** [`refined_course/slides/00_course_overview.pdf`](./refined_course/slides/00_course_overview.pdf)

---

## What's in this repo

This repo holds **two editions of the same course**:

| Folder | What | When to use |
|---|---|---|
| **`refined_course/`** | The **recommended** edition: 7-module curriculum with onboarding deck, per-module READMEs, and 5 extra notebooks closing real gaps. | Use this. It's the polished one. |
| `01_*.ipynb` … `19_*.ipynb` (root) | The original linear 19-notebook course. | Use if you want a strictly-linear progression and don't care about the modular structure. |

The two editions share the same *content* — the refined edition reorganises the originals into modules and adds five new notebooks (statistics, model evaluation, feature engineering, AI evaluation, and a second capstone) plus a master onboarding notebook.

---

## Who this course is for

- **Analysts** who want to graduate from Excel/SQL to Python and pick up modern AI tools.
- **Engineers** who want to add data and AI engineering to their stack.
- **ML practitioners** who want to add the AI-engineering layer (LLMs, prompts, RAG, agents).
- **Students** of data science who want a curriculum that's *actually current* (not 2015's idea of data work).
- **Managers** curious enough to read the capstones and the overview deck.

There are five **learning paths** in the onboarding notebook, with time budgets from 8 to 35 hours.

---

## Why this course is different

Most introductory Python courses still teach Python the way it was taught in 2015. The work that actually matters today combines three skills:

1. **Solid Python fluency** — reading and writing code without friction.
2. **Working with data professionally** — cleaning, exploring, modelling, visualising.
3. **AI-driven automation** — using language models, APIs, and small scripts to replace repetitive analytical work.

This course is built around that combination from the *very first notebook*. You compute LLM token costs while you learn variables and loops. You write a ticket-triage rules engine while you learn `if/else`. You parse JSON-shaped API responses while you learn dictionaries. By the end you'll have built a packaged, tested, scheduled AI feature you can talk about in interviews.

---

## The 7-module structure (refined edition)

```
   ┌────────────────────────────────────────────────────────────────────┐
   │                                                                     │
   │  0  Onboarding         master onboarding notebook                    │
   │  1  Foundations        NB 1–5   Python basics                        │
   │  2  Real-world I/O     NB 7–8   HTTP + SQL                           │
   │  3  Data Science       NB 10–14 pandas, NumPy, plots, stats, TS      │
   │  4  Machine Learning   NB 15–17 sklearn + evaluation + features      │
   │  5  AI Engineering     NB 18–22 prompts, RAG, agents, docs, eval     │
   │  6  Production         NB 23–24 packaging, scheduling                │
   │  7  Capstones          NB 26–27 analytics + AI assistant             │
   │                                                                     │
   └────────────────────────────────────────────────────────────────────┘
```

Each module folder has its own `README.md` with goals, prerequisites, an ASCII diagram, and a list of common pitfalls. Read it before opening the first notebook of the module.

---

## What you'll build by the end

**Six small artefacts along the way:**

| What | From which notebook |
|---|---|
| A KPI snapshot for an AI support bot | NB 1 |
| A confidence-based ticket-triage rules engine | NB 2 |
| A live API ETL pipeline | NB 7 |
| A 3-month forecast with Holt-Winters | NB 14 |
| A multi-tool data assistant (LLM + tools) | NB 20 |
| A packaged, tested Python project | NB 23 |

**Two big capstones:**

- 🏆 **Capstone A — AI Support-Bot Analytics** (NB 26): 5 channels × 12 months → 2×2 executive dashboard → regression demonstrating Simpson's paradox → 5-bullet executive summary.
- 🏆 **Capstone B — AI Customer-Feedback Assistant** (NB 27): classify + validate + RAG + scheduled orchestration + cost dashboard + eval gate.

---

## Getting started — 2 minutes

### Option A — Google Colab *(easiest, no install)*

1. Go to [colab.research.google.com](https://colab.research.google.com).
2. **File → Upload notebook** → pick `refined_course/00_onboarding/00_master_onboarding.ipynb`.
3. Hit Shift+Enter on every cell. The last cell prints `✅ Setup looks good!`.

### Option B — Local Jupyter

```bash
git clone <repo-url>
cd "Python for AI-Driven Automation and Business Data Science"

python -m venv .venv
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\activate             # Windows

pip install -r refined_course/requirements.txt
jupyter lab refined_course/00_onboarding/00_master_onboarding.ipynb
```

Tested on Python 3.10–3.12.

---

## How each notebook is structured

Every notebook follows the same six-section template:

1. **🎯 Learning objectives** + **✅ Prerequisites**
2. **Numbered concept sections** — short prose, then runnable code, then a "what just happened" callout.
3. **🧪 Practice exercises** — with full solutions and *reasoning* (not just code).
4. **🧠 Stretch exercises** — 2 extra optional exercises (applied + harder).
5. **🎁 Bonus mini-project** — one larger applied task per notebook.
6. **🧠 Key takeaways** + **✅ Self-assessment** + **🚀 Next step**.

Total exercise count across the refined course: **~80 exercises**, every one with a detailed solution and explanation.

### Visual markers you'll see throughout

| Marker | Meaning |
|---|---|
| 💡 **Tip** | Stop-and-notice callout. |
| 🎯 **Intuition** | The mental model behind the syntax. |
| ⚠️ **Pitfall** | A bug or anti-pattern that bites you without warning. |
| 🧪 **Exercise** | Hands-on practice — try before peeking. |
| 🎁 **Bonus** | Larger applied task per notebook. |
| 🐞 **Debug me** | A cell with an *intentional* bug for you to find. |
| 🚀 **Next step** | Points to the next notebook on your path. |

---

## The five learning paths

Match yourself to the one that fits:

| You are … | You'll do | Time |
|---|---|---|
| **Complete beginner** | All 7 modules in order | ~35 h |
| **Analyst** (knows Excel + SQL) | Modules 0, 2, 3, 4, 7 | ~20 h |
| **Developer** (knows another language) | Modules 0, 2, 3, 4, 5, 6, 7 | ~28 h |
| **ML practitioner** | Modules 0, 5, 6, 7 | ~15 h |
| **Manager / curious** | Module 0 + capstones only | ~8 h |

The onboarding notebook and overview deck both visualise these paths.

---

## How to study a notebook — the five-step loop

```
   Read  →  Run  →  Try  →  Tweak  →  Predict
     │              │
     │              └── try every exercise before clicking the solution
     └────────── read the prose before looking at the code
```

Apply this loop to *every* notebook. Five minutes of genuine struggle beats five hours of passive reading.

---

## Slide decks

This repo ships two PDF decks:

- **Course overview** ([`refined_course/slides/00_course_overview.pdf`](./refined_course/slides/00_course_overview.pdf)) — 24 pages. The "you are here" deck: roadmap, dependency graph, learning paths, study loop, what-you'll-build gallery.
- **Technical deep dive** ([`slides/course_slides.pdf`](./slides/course_slides.pdf)) — 80 pages. Lecture-style summary of the original 19-notebook course; covers prompts, RAG, the capstone dashboard, the production wrapper, and more.

Both decks are built from `.tex` sources you can edit and recompile (`pdflatex deck.tex`, twice).

---

## ❓ FAQ

**Do I need to know Python before starting?**
No. Notebook 1 (and the onboarding) start from zero. Use the learning paths if you do.

**Do I need a GPU?**
No. Everything runs on a laptop or in free Colab. The AI-workflows notebooks (18–22, 27) use a built-in `MockLLM` and don't need internet.

**Do I need an OpenAI / Anthropic API key?**
No, but you can use one. Notebooks 18, 19, 22, 27 work offline with the MockLLM. The "Going live" sections show the exact line you swap to use a real model.

**Will this teach me deep learning?**
Not directly — that's a different course. You will learn the *Python and ML foundations* you'd need before specialising into deep learning. The AI-engineering modules cover using pre-trained LLMs, which is what most production AI applications need.

**Will this teach me fine-tuning?**
No, but it leaves you well-equipped to read a fine-tuning tutorial next.

**Can I use this for a workshop / classroom?**
Yes. Each notebook is roughly one 60–90-minute session. The course-overview deck doubles as the opening lecture.

**How long is this in total?**
- Motivated full-time learner: **~5–7 days**.
- Part-time learner (1 h/day): **~3–4 weeks**.
- Skim-and-reference reader: **a weekend**.

**Is the data real?**
The datasets are synthetic but **carefully calibrated** to mirror real-world patterns (e.g., the churn dataset in NB 15 produces a 30% churn rate with R² ≈ 0.75 on NPS prediction). Synthetic data lets us guarantee reproducibility and avoids licensing issues.

**Do the notebooks actually run?**
Yes — every code cell in every notebook executes top-to-bottom in CI on each commit. Three cells are *expected* to error: the `🐞 Debug me` exercises that are supposed to fail so you find the bugs.

---

## Repository layout

```
Python for AI-Driven Automation and Business Data Science/
├── README.md                       ← this file
├── LICENSE                         ← MIT
│
├── refined_course/                 ← the recommended 7-module edition
│   ├── README.md                   ← refined-course entry point
│   ├── 00_onboarding/              ← master onboarding notebook
│   ├── 01_foundations/             ← NB 1–5
│   ├── 02_real_world_io/           ← NB 7–8
│   ├── 03_data_science/            ← NB 10–14
│   ├── 04_machine_learning/        ← NB 15–17
│   ├── 05_ai_engineering/          ← NB 18–22
│   ├── 06_production/              ← NB 23–24
│   ├── 07_capstones/               ← NB 26–27
│   ├── slides/
│   │   ├── 00_course_overview.pdf  ← 24-slide overview deck
│   │   └── images/                 ← 7 overview figures
│   ├── data/                       ← 3 sample CSVs
│   ├── requirements.txt
│   └── LICENSE
│
├── 01_python_basics.ipynb          ← original linear edition (still works)
├── 02_control_structures.ipynb
├── …
├── 19_scheduling_orchestration.ipynb
│
├── slides/
│   ├── course_slides.pdf           ← 80-page technical deck
│   ├── course_slides.tex
│   └── images/                     ← 21 figures
│
└── data/                           ← 3 sample CSVs (mirrored in refined_course)
```

---

## What's *not* in the course (intentionally)

- ❌ Deep learning from scratch (PyTorch / TF training loops).
- ❌ Vendor-specific cloud deployment (AWS / GCP / Azure).
- ❌ Vector-database deep dives (Pinecone / Weaviate / etc.).
- ❌ Web scraping.

These are conscious trade-offs — the course is deep where it counts and stays out of vendor-specific or quickly-dating territory.

---

## Course philosophy

A few principles that guided every notebook:

- **Explain *why*, not just *how*.** Code without intuition is fragile.
- **Show real examples.** Tip calculators teach syntax; KPI parsers teach the job.
- **Practice over passive reading.** Every concept gets exercises *with reasoning*.
- **Modern tools, modern habits.** Type hints, virtual envs, validation, pytest, observability.
- **AI as a tool, not magic.** LLMs are function calls; calibration matters.

---

## LLM providers — local *and* hosted

Every AI notebook (NB 18 – 22, 27) ships with an offline `MockLLM` so you can run the whole course **with no internet and no API key**. When you're ready for real intelligence in the answers, swap one line. The course supports **four providers** through a single unified interface (`refined_course/llm_providers.py`):

| Provider | Class | When to pick it |
|---|---|---|
| 🟢 **OpenAI** | `OpenAILLM(model="gpt-4o-mini")` | Best default — reliable, well-documented, fast |
| 🟠 **Anthropic** (Claude) | `AnthropicLLM(model="claude-haiku-4-5-20251001")` | Strong reasoning, long context (200K), careful tone |
| 🔵 **Google** (Gemini) | `GoogleLLM(model="gemini-2.0-flash")` | Cheapest for high-volume; 1M+ token context |
| 🟣 **Ollama** (local) | `OllamaLLM(model="llama3.2:3b")` | **No internet, no key, no cost** — runs on your own hardware |

To swap providers in any AI notebook, change *one* line:

```python
# Default (offline)
from llm_providers import MockLLM
llm = MockLLM()

# Pick any one of these instead — the rest of the notebook is unchanged:
from llm_providers import OpenAILLM;    llm = OpenAILLM(model="gpt-4o-mini")
from llm_providers import AnthropicLLM; llm = AnthropicLLM(model="claude-haiku-4-5-20251001")
from llm_providers import GoogleLLM;    llm = GoogleLLM(model="gemini-2.0-flash")
from llm_providers import OllamaLLM;    llm = OllamaLLM(model="llama3.2:3b")
```

**Setup steps for each provider** are in [`refined_course/05_ai_engineering/A1_llm_providers_guide.ipynb`](./refined_course/05_ai_engineering/A1_llm_providers_guide.ipynb) — including authentication, model recommendations, cost estimates, and a decision table for picking the right one.

```bash
# For one of the hosted providers, set the corresponding env var (never inline it):
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...
# Ollama needs no key — `ollama serve` on localhost is the whole setup.
```

> ⚠️ **Never commit API keys to git.** The notebooks are designed so you don't have to touch a key inside the notebook itself.

---

## Contributing & feedback

The course gets better when real readers tell us what didn't land. If you spot a bug, an unclear explanation, or a missing example, please open an issue or pull request.

## Licence

MIT — see [`LICENSE`](./LICENSE). Use freely for personal learning, teaching, or any other purpose.

---

## At a glance

```
   25 notebooks   •   ~80 exercises with detailed solutions
   7 modules      •   2 hero capstones
   24-slide overview deck   +   80-slide technical deck
   Runs on Colab, locally, and offline.
```

**Open [`refined_course/00_onboarding/00_master_onboarding.ipynb`](./refined_course/00_onboarding/00_master_onboarding.ipynb) and start.**
