# Python for AI-Driven Automation and Business Data Science

*From your first line of Python to shipping a real AI-driven automation — Python fluency, business data science, machine learning, AI engineering, and production wiring in one hands-on, self-paced curriculum.*

**10 modules · 38 notebooks (+ 11 optional appendices) · end-to-end**

---

## Two ways to take it

There are two learning paths — pick one:

### 🎓 Complete course — *the full depth*
All 10 modules / 38 notebooks (plus 11 optional appendices), worked in spiral order with every exercise, stretch problem, and capstone. **~105 hours.**
→ **Start:** [`00_onboarding/00_master_onboarding.ipynb`](./00_onboarding/00_master_onboarding.ipynb)

### 🏎️ Fast track — *the essentials, condensed*
The same teaching trimmed to **13 notebooks, ~14 hours** — a credible end-to-end pass you can finish in a few weeks of evenings (Stretch A/B and the bonus projects removed).
→ **Start:** [`fast_track/`](./fast_track/)

New here? The 5-minute offline demo [`00c_see_it_work.ipynb`](./00_onboarding/00c_see_it_work.ipynb) shows what you'll build before the Python begins, and [`00b_course_overview.ipynb`](./00_onboarding/00b_course_overview.ipynb) has the full module map and an interactive time estimator.

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

**Google Colab (easiest):** click the **“Open in Colab”** badge at the top of any notebook — it opens straight from GitHub, no download, and the required libraries are pre-installed.

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

## Contributing & licence

Spotted a bug or an unclear explanation? Open an issue or PR. Licensed **MIT** (see `LICENSE`) — use freely for learning, teaching, or anything else.

Happy coding.
