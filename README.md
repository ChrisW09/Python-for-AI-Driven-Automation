# Python for AI-Driven Automation and Business Data Science

A modern, hands-on course that takes you from your first line of Python to building
practical AI-powered workflows for real business problems.

```
   ┌──────────────────────────────────────────────────────────────────────┐
   │  19 notebooks  •  ~450 code cells  •  All exercises with solutions    │
   │  Runs on Google Colab with zero setup                                 │
   │  AI / LLM workflows included — runs offline with a built-in MockLLM   │
   │  Real HTTP, SQL, time series, embeddings, agents, packaging, cron     │
   └──────────────────────────────────────────────────────────────────────┘
```

> **Who this is for.** Analysts, business and engineering students, early-career
> data professionals, and anyone who wants to stop *using* spreadsheets and start
> *programming* with data — with an eye on the AI-enabled work environment of today.

---

## What makes this course different

Most introductory Python courses still teach Python the way it was taught in 2015:
print statements, fizz-buzz, a quick tour of pandas, maybe a linear regression at
the end. That isn't where the value lies anymore.

The work that matters today combines three skills:

1. **Solid Python fluency** — reading and writing code without friction.
2. **Working with data professionally** — cleaning, exploring, modelling, visualising.
3. **AI-driven automation** — using language models, APIs, and small scripts to
   replace repetitive analytical work.

This course is built around that combination from the very first notebook.
You will compute LLM token costs while you learn variables and loops. You will
write a ticket-triage rules engine while you learn `if/else`. You will process
logs of API calls while you learn lists. You will parse JSON-shaped API
responses while you learn dictionaries. And by the end you will have built a
polished business-AI analytical capstone *and* your own AI-assisted automation
pipeline.

---

## 🎯 What you'll build

The course is anchored by two **hero projects** in the last three notebooks:

### 🏆 Notebook 10 — AI Support-Bot Analytics
A full end-to-end analytical study of an AI customer-support deployment:
**5 channels × 12 months × 8 KPIs**, leading to a 2×2 executive dashboard, a
regression that exposes **Simpson's paradox**, channel clustering, and a written
5-bullet executive summary.

```
   Automation rate over time  │  Annual ticket volume by channel
   ────────────────────────────┼────────────────────────────────
   Cost / satisfaction trade-  │  Distribution of monthly
   off                         │  automation rate
```

### 🤖 Notebook 11 — AI-Assisted Workflows
A complete tour of working with LLMs from Python — **runs entirely offline**
using a built-in `MockLLM` class so you can learn the patterns without spending
a cent. Topics:

- The system / user / assistant message structure
- The four core prompt patterns (instructions, few-shot, structured output, CoT)
- Batch classification with cost reporting
- A keyword-retrieval **RAG** pipeline grounded in your own docs
- Cost / latency / accuracy evaluation
- Copy-paste OpenAI and Anthropic SDK shims for going live

When you're ready, **one function swap** moves the whole notebook from the
MockLLM to a real provider.

---

## 📚 Full notebook map

### Part I — Foundations (NB 1–6)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 1 | `01_python_basics.ipynb`            | Variables, types, arithmetic, strings, f-strings | A KPI snapshot for an AI support bot |
| 2 | `02_control_structures.ipynb`       | `if/elif/else`, loops, error handling | A confidence-based ticket-triage rules engine |
| 3 | `03_lists_data_structures.ipynb`    | Lists, tuples, slicing, comprehensions | Latency-log analysis |
| 4 | `04_dictionaries_advanced.ipynb`    | Dicts, JSON, LLM chat-message lists | Defensive API-response parser |
| 5 | `05_pandas_preview.ipynb`           | Your first real DataFrame | LLM-call log analysis |
| 6 | `06_functions_modules.ipynb`        | Functions, modules, type hints | A reusable cost / cleaning toolkit |

### Part II — Real-world I/O (NB 12–13)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 12 | `12_apis_and_http.ipynb`           | `requests`, status codes, retries, pagination | A weather-data ETL pipeline against a live public API |
| 13 | `13_sql_fundamentals.ipynb`        | SQLite + pandas, joins, CTEs, window functions | A SQL-driven channel report |

### Part III — Data science (NB 7, 8, 14)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 7  | `07_numpy_fundamentals.ipynb`      | Arrays, vectorisation, broadcasting | A/B-testing two LLM providers |
| 8  | `08_matplotlib_basics.ipynb`       | Publication-quality charts | A 2×2 AI-ops executive dashboard |
| 14 | `14_time_series_forecasting.ipynb` | Resampling, rolling, decomposition, Holt-Winters | A 3-month automation-rate forecast |

### Part IV — Machine learning (NB 9)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 9  | `09_scikit_learn_basics.ipynb`     | The full ML workflow | Customer churn prediction + NPS regression + text classifier |

### Part V — The analytical capstone (NB 10)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 10 | `10_capstone_project.ipynb`        | End-to-end business-AI analytics | The AI Support-Bot Analytics project |

### Part VI — AI engineering (NB 11, 15–17)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 11 | `11_ai_assisted_workflows.ipynb`   | LLMs, prompts, structured output, RAG | Inbox-triage with the MockLLM |
| 15 | `15_embeddings_semantic_retrieval.ipynb` | TF-IDF + dense embeddings, retrieval@k | A real RAG system, benchmarked vs keyword |
| 16 | `16_tools_and_agents.ipynb`        | JSON-schema tools, call→execute→return loop | A multi-tool data assistant |
| 17 | `17_ai_document_processing.ipynb`  | Extract → chunk → LLM → validate → aggregate | An invoice-parsing pipeline |

### Part VII — Engineering polish (NB 18–19)
| # | Notebook | Focus | What you build |
|---|---|---|---|
| 18 | `18_from_notebook_to_project.ipynb`| `src/` layout, `pyproject.toml`, pytest, CLI | A packaged, tested, importable Python package |
| 19 | `19_scheduling_orchestration.ipynb`| cron / systemd / GitHub Actions / Prefect, idempotency, alerts | A production-shape automation wrapper |

**Total**: ~450 code cells, every concept exercised, every exercise solved with reasoning.

---

## 🧭 Learning paths

The notebooks are designed to be read in order, but pick the path that matches you:

### 👶 Complete beginner — never written code before
Work through all 11 in order. Plan for **15–25 hours total**, spread over 2–4 weeks
at one notebook every 1–2 sessions. Don't skip the exercises — they are where the
learning happens.

### 📊 Analyst who knows Excel and wants to move to Python
- **Skim** NB 1–4 (read the explanations, skip exercises you find trivial).
- **Engage fully** with NB 5 (pandas), NB 8 (matplotlib), NB 10 (capstone).
- **End with** NB 11 to see the AI-augmented version of your existing workflow.

### 💻 Developer who knows another language
- **Skim** NB 1–6 looking only for Python's idiosyncrasies (truthiness, mutable
  defaults, `*args/**kwargs`, the GIL is not covered, sorry).
- **Focus on** NB 7 (NumPy mental model), NB 9 (scikit-learn), NB 11 (LLM patterns).

### 🤖 ML/AI practitioner who wants to add business framing
- **Jump to** NB 10 (capstone) and NB 11 (AI workflows) — these are the hero
  projects and they're written to be readable standalone if you have the
  Python/pandas/sklearn background.

---

## ⚙️ How to run the notebooks

You have two options. Pick whichever you prefer.

### Option A — Google Colab *(recommended for getting started)*

No installation required.

1. Go to [colab.research.google.com](https://colab.research.google.com).
2. Choose **File → Upload notebook** and select one of the `.ipynb` files from this repo.
3. Run cells with **Shift + Enter** (or click ▶).

All notebooks are written to run cleanly on Colab with **no extra setup**.

### Option B — Locally with Jupyter

```bash
# 1. Clone this repository.
git clone <repo-url> course
cd course

# 2. Create a virtual environment (recommended).
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows

# 3. Install the dependencies.
pip install -r requirements.txt

# 4. Launch Jupyter.
jupyter lab
```

Tested on Python 3.10+ with the pinned versions in `requirements.txt`.

### Sample data

The `data/` folder contains three small CSV files (`support_ops.csv`, `api_log.csv`,
`customer_feedback.csv`) that mirror the synthetic datasets generated inline. You can
use them whenever you want to practise `pd.read_csv` against a real file. See
[`data/README.md`](./data/README.md) for the schemas.

### Companion slides

The `slides/` folder contains a 61-slide LaTeX Beamer deck that complements the
notebooks — a visual walk-through of the whole course with 15 custom figures.
[`slides/course_slides.pdf`](./slides/course_slides.pdf) is the compiled deck;
[`slides/course_slides.tex`](./slides/course_slides.tex) is the source. See
[`slides/README.md`](./slides/README.md) for how to recompile or regenerate the
figures.

---

## 🔐 Working with API keys (Notebook 11)

Notebook 11 can run **entirely offline** using the included `MockLLM` class —
that's the recommended way to learn the patterns. When you're ready to use a real
model:

1. Get an API key from **OpenAI** or **Anthropic**.
2. Set it as an **environment variable**, never paste it into a cell:
   ```bash
   export OPENAI_API_KEY=sk-...
   # or
   export ANTHROPIC_API_KEY=sk-ant-...
   ```
3. The notebook shows you exactly which function to swap in.

> ⚠️ **Never commit API keys to git.** The notebooks are designed so that you don't
> have to touch a key inside the notebook itself — keep them in your shell environment
> or in a `.env` file (with `.env` in `.gitignore`).

---

## 📖 How each notebook is structured

Every notebook follows the same pattern, so you always know where you are:

1. **🎯 Goals & prerequisites** — what you'll learn, what you should already know.
2. **Concepts** — short, focused explanations with intuition, analogies, motivating examples.
3. **Worked examples** — realistic problems with code and interpretation.
4. **🧪 Exercises** — increasing in difficulty, **all with full solutions and the *reasoning***, not just the answer.
5. **🎁 Bonus mini-project** — one larger applied task per notebook.
6. **🧠 Key takeaways & ✅ self-assessment** — a checklist you can use before moving on.

You'll see emoji markers throughout (💡 tips, 🎯 intuition, ⚠️ pitfalls, 🧪 exercises, 🎁 bonus, 🚀 next step) — signposts, not decoration.

---

## 💡 Teaching philosophy

A few principles guide the course:

- **Explain *why*, not just *how*.** Code without intuition is fragile.
- **Show real examples.** Tip calculators teach syntax; KPI parsers teach the job.
- **Practice over passive reading.** Every concept gets exercises *with reasoning*.
- **Modern tools, modern habits.** F-strings, type hints, pathlib, virtual
  environments — the muscle memory you actually want.
- **AI as a tool, not magic.** Language models are powerful, but they are still
  just function calls. You can — and should — understand the calls you make.

---

## ❓ FAQ

**Do I need to know Python before starting?**
No. Notebook 1 starts from zero. If you already know basics, use the learning paths above to skim.

**Do I need to know maths or statistics?**
No prior maths required. The course introduces what it uses, when it uses it (means, standard deviations, correlations, linear regression in plain English). Some comfort with arithmetic and percentages helps.

**Do I need a GPU?**
No. Everything runs on a laptop or in free Colab. Notebook 11's `MockLLM` doesn't even need internet.

**Will this teach me deep learning?**
Not directly — that's a different course. You will learn the *Python and ML foundations* you'd need before specialising into deep learning. Notebook 11 covers using pre-trained LLMs (which is what most working AI applications actually need).

**Will this teach me how to fine-tune an LLM?**
No, but it will leave you well-equipped to read a fine-tuning tutorial next. Most modern AI applications don't fine-tune — they use prompt engineering + retrieval (both covered).

**Can I use this for a workshop / classroom?**
Yes. The course is structured for self-paced study but works for instructor-led workshops too. Each notebook is roughly one 60–90-minute session.

**How long is this in total?**
- A motivated full-time learner can do it in **5–7 days**.
- A part-time learner (1 hour / day): **3–4 weeks**.
- A "skim and use as reference" reader: **a weekend**.

**Is the data real?**
The datasets are synthetic but **carefully calibrated** to mirror real-world patterns
(e.g., the churn dataset in NB9 produces a realistic 30% churn rate with R² ≈ 0.75
on NPS prediction). Synthetic data lets us guarantee reproducibility and avoids
licensing headaches.

**Do all the notebooks really run?**
Yes. The full course is regression-tested with `nbclient` — every code cell in
every notebook executes top-to-bottom on each commit. Three cells are *expected*
to error: the `Debug me 🐞` exercises that are *supposed* to fail so students
find the bugs.

---

## 🛠 Tooling reference

| Library | Used in | What for |
|---|---|---|
| `numpy` | NB 7, 9, 10 | Numerical arrays, broadcasting |
| `pandas` | NB 5, 6, 9, 10 | DataFrames, group-by, CSV I/O |
| `matplotlib` | NB 8, 10 | Visualisation, dashboards |
| `scikit-learn` | NB 9, 10 | Classification, regression, pipelines |
| `openai` / `anthropic` | NB 11 (optional) | Real LLM calls — only needed if you go beyond the MockLLM |

---

## 🤝 Contributing & feedback

This is a living course. If you spot a bug, an unclear explanation, or a missing
example, please open an issue or pull request. The course gets better because
real readers tell us what didn't land.

---

## 📜 Licence

MIT — see the `LICENSE` file. You are free to use these materials for personal
learning, teaching, or any other purpose.

Happy coding.
