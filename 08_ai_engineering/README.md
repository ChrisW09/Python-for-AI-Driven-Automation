# Module 8 — AI Engineering

> 🧭  [◀ Industry Applications](../07_industry_applications/)  ·  [🏠 Course home](../README.md)  ·  [Building AI POCs ▶](../09_building_ai_pocs/)

**Goal:** Use LLMs from Python as engineered, observable, evaluated components — not as magic. By the end of this module you can build, test, and ship an AI feature.

**Estimated time:** 8–10 hours.

**Prerequisites:** Modules 1–2 (functions, JSON, HTTP). Module 5 is helpful for the evaluation chapter.

```
                  ┌────────────────────────────────────┐
                  │  NB 27 — LLM fundamentals:         │
                  │  the LLM as a next-token loop      │
                  │  (tokens, attention, prompting)    │
                  └─────────────────┬──────────────────┘
                                    │
        ┌───────────────────┬───────┴───────┬─────────────────┐
        ▼                   ▼               ▼                 ▼
   NB 28                NB 29          NB 30             NB 31
   prompts +            embeddings     tools +           document
   structured           + RAG          agents            processing
   output
        └───────────────────┴───────┬───────┴─────────────────┘
                                    ▼
                            NB 32 — evaluation
                          golden sets, LLM-as-judge,
                          cost dashboards, regression tests
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 21 | `27_llm_fundamentals.ipynb` | ~75 min | Intermediate | The theory floor: tokens, next-token prediction, the Transformer & attention, prompting techniques, hallucinations & knowledge cutoff — told through "Helpa" |
| 22 | `28_ai_workflows.ipynb` | 60–90 min | Intermediate | Helpa's first real code: prompt patterns, safe JSON output, inbox batch classification, keyword RAG (offline MockLLM) |
| 23 | `29_embeddings_retrieval.ipynb` | 60–80 min | Intermediate | A semantic retriever: TF-IDF + dense embeddings, retrieval@k / MRR benchmark, end-to-end RAG |
| 24 | `30_tools_and_agents.ipynb` | 60–80 min | Intermediate | A multi-tool support-ops data assistant (call → execute → return loop, safety budget, trace log) |
| 25 | `31_document_processing.ipynb` | 60–75 min | Intermediate | An invoice-extraction pipeline: extract → chunk → LLM-extract → validate → DataFrame |
| 26 | `32_ai_evaluation_observability.ipynb` | 55–70 min | Intermediate | An eval harness: golden set, LLM-as-judge, tracing, cost dashboard, A/B test, regression detection |

## Optional appendices at a glance

| Appendix | Notebook | ⏱ Time | Focus |
|---|---|---|---|
| A1 | `A1_llm_providers_guide.ipynb` | 30–45 min | OpenAI / Anthropic / Google / Ollama behind one `chat()` interface (`../llm_providers.py`) — decision table, model picks, cost math |
| A2 | `A2_vector_stores_survey.ipynb` | 45–60 min | FAISS, Chroma, Qdrant, Weaviate, Pinecone, Milvus, pgvector — index families + a 4-question decision rubric |
| A3 | `A3_rag_and_agent_frameworks.ipynb` | 45–60 min | LangChain, LlamaIndex, Haystack, DSPy, smolagents, AutoGen, CrewAI — the same RAG task in each + a 3-question rubric |

## Notebook guides

### 21 · LLM Fundamentals — `27_llm_fundamentals.ipynb`

Module 8 opens with the question every learner asks first: *what is an LLM actually doing inside?* This is the *theory* notebook (NB 28–32 are the hands-on ones), built around one mental model — **an LLM is a next-token predictor run in a loop** (sample → append → repeat) — and one running example: **Helpa**, an AI customer-support assistant you've been asked to build for a small SaaS company. Tokens become Helpa's monthly bill, attention becomes how Helpa reads a question, hallucinations become the support reply that invents a product that doesn't exist.

The concepts are prerequisite-free (you can read it early, alongside `00c`); the light maths in §4 and §6 lands more easily after the vectors of NB 29, so skim those on a first pass if needed. By the end you've diagnosed exactly why a "Just LLM" Helpa hallucinates — and NB 28–30 become the cure.

**Learning objectives:**
- Explain what a Large Language Model is and how it generates text, one token at a time.
- Distinguish tokens, parameters, and the training objective (next-token prediction with cross-entropy loss).
- Describe the Transformer architecture and the Attention mechanism (Q/K/V) in your own words.
- Distinguish pre-training, fine-tuning, and prompting — three different intervention points.
- Name five prompting techniques and pick the right one for a given task.
- Identify the two structural limitations (hallucinations, knowledge cutoff) and explain why they exist.

**Sections:** 1 What is a Large Language Model? · 2 How LLMs see text: tokens · 3 What are parameters? Why "large"? · 4 The training objective: next-token prediction · 5 The architecture: the Transformer · 6 The Attention mechanism · 7 Pre-training, fine-tuning, prompting · 8 Common prompting techniques · 9 Limitation 1 — hallucinations · 10 Limitation 2 — knowledge cutoff · 11 Mental model — the three levels of LLM usage

**Practice:** 4 ✋ quick checkpoints · 5 🧪 practice exercises (incl. a Debug me 🐞) · 4 🧠 stretch exercises · 🎁 bonus mini-project: a token-budget calculator.

**Files/datasets:** none — the next-token loop, temperature dial, and attention demos are toy models built in-notebook with NumPy/matplotlib. No LLM calls at all.

### 22 · AI-Assisted Workflows — `28_ai_workflows.ipynb`

The bridge between everything you've learned and what modern AI-driven work looks like — and the notebook where **Helpa stops being a thought experiment and becomes Python**. One mental model carries the whole lesson: **an LLM call is just a function call**, `reply = f(messages)`; every pattern (system prompts, JSON output, batch loops, retrieval) is plumbing around that one call.

You write prompts that are *reliable, not just clever*: the four core prompt patterns, defensive JSON parsing, a KPI report over a classified feedback inbox, and Helpa's first grounded answer via a tiny keyword-retrieval workflow. The final section shows how to go live with OpenAI or Anthropic — the calling code is identical to the mock.

**Learning objectives:**
- Explain what happens when you "call an LLM" — it's just a function call.
- Use the system / user / assistant message structure correctly.
- Apply the four core prompt patterns: instructions, few-shot, structured output, chain-of-thought.
- Parse JSON output safely with `try / except`.
- Classify and summarise a batch of records and report the results.
- Build a tiny retrieval workflow (keyword RAG) and reason about cost, latency, and evaluation.

**Sections:** 1 An LLM call is just a function call · 2 Our offline `MockLLM` · 3 Your first prompt — system + user messages · 4 The four core prompt patterns · 5 Batch processing — classify a whole inbox · 6 A tiny retrieval workflow · 7 Cost, latency, evaluation — the engineer's checklist · 8 Going live with a real model

**Practice:** 4 ✋ quick checkpoints · 3 🧪 practice exercises · 4 🧠 stretch exercises · 🎁 bonus mini-project: an inbox-triage CLI.

**Files/datasets:** offline `MockLLM` imported from the repo-root `llm_providers.py` — no API key, no internet. The customer-feedback batch is defined in-notebook.

### 23 · Embeddings and Semantic Retrieval — `29_embeddings_retrieval.ipynb`

NB 28's keyword RAG has a glaring weakness: *"how do I end my plan?"* won't match a document about *"cancelling your subscription"* — so Helpa shrugs, or invents an answer. This notebook fixes that with a **semantic** retriever, under the mental model **meaning becomes geometry**: embeddings turn texts into arrows, and retrieval is "which stored arrow points most like my query arrow?". One query pair runs through everything: *"How do I cancel my subscription?"* vs. its evil twin *"How can I end my plan?"*.

You build TF-IDF and dense-embedding retrievers, run a head-to-head evaluation of keyword vs TF-IDF vs dense on the same test set, and finish with an upgraded end-to-end RAG — every piece of a production-grade RAG system except the vector database (which A2 covers).

**Learning objectives:**
- Explain what an embedding is and what cosine similarity measures.
- Build a TF-IDF retriever with scikit-learn (offline, no API calls).
- Build an embedding-based retriever with a deterministic offline fallback.
- Compute retrieval@k and MRR to evaluate retrievers.
- Compare keyword vs TF-IDF vs dense retrieval on the same test set.
- Combine retrieval with an LLM — and recognise the failure modes (synonyms, paraphrase, domain jargon).

**Sections:** 1 What is an embedding? · 2 Setup · 3 Baseline — keyword overlap (the NB 28 approach) · 4 TF-IDF — a stronger lexical baseline · 5 Dense embeddings — semantic similarity · 6 Plugging in a real embedding model (reference) · 7 Evaluating retrievers — retrieval@k and MRR · 8 Where keyword wins and dense loses · 9 End-to-end RAG with the new retriever

**Practice:** 4 ✋ quick checkpoints · 4 🧪 practice exercises (incl. a Debug me 🐞) · 4 🧠 stretch exercises · 🎁 bonus mini-project: a confidence threshold that refuses out-of-corpus questions gracefully.

**Files/datasets:** offline throughout — a minimal in-notebook `MockLLM` plus the deterministic `MockEmbedder` from the repo-root `llm_providers.py`; the document corpus is defined in-notebook. Real options (OpenAI embeddings, `sentence-transformers`) are shown as reference code.

### 24 · Tool Calling and Small Agents — `30_tools_and_agents.ipynb`

So far the LLM took text and returned text. Here you give it **tools** — functions it can decide to call — and watch it do multi-step work. The mental model is **planner + hands + a `while` loop**: the model is the planner (it only ever *asks*), your code is the hands (it *acts*), and the loop is the agent. "Tool calling", "function calling", "agents", "ReAct" are all brand names for this one machine.

The running example is a **support-ops data assistant**: a ~100-line program that answers business questions (*"how many tickets in total?"*, *"which channel is cheapest?"*) by running pandas queries on its own — assembled one tool at a time, with a safety budget and a debuggable trace.

**Learning objectives:**
- Define a tool with a JSON schema the model can read.
- Run the call → execute → return loop manually, step by step.
- Build a multi-tool agent that picks the right tool for each question.
- Add a safety budget (max steps, max tool calls) to prevent runaway loops.
- Log every tool call so you can debug what the agent did.
- Recognise when an agent is overkill — and when a single LLM call is enough.

**Sections:** 1 The tool-calling loop in one picture · 2 Setup — a richer MockLLM that understands tools · 3 Tool schemas — what the model needs to know · 4 One round of tool calling — manually · 5 Wrapping the loop in a function · 6 Inspecting the trace — debugging an agent · 7 A multi-step agent — calculator chain · 8 When NOT to use an agent · 9 Going live — the real-provider sketch

**Practice:** 4 ✋ quick checkpoints · 4 🧪 practice exercises (incl. a Debug me 🐞) · 4 🧠 stretch exercises · 🎁 bonus mini-project: a pandas-query tool.

**Files/datasets:** a tool-aware `MockLLM` defined in-notebook (offline, no API key); the `support_ops` DataFrame is generated in-notebook (same shape as NB 13's table).

### 25 · AI Document Processing — `31_document_processing.ipynb`

A huge fraction of business work is extracting structured information from unstructured documents — invoices, receipts, contracts, KYC forms. The mental model is an **assembly line**: a raw document rolls through **extract → chunk → LLM-extract → validate → aggregate**, and a tidy database row rolls out; validation is the quality-control inspector at the end of the belt.

The running example is an **invoice parser**: a finance-ops tool that turns a stack of messy free-form invoices into a clean table of (vendor, total, due_date, line_items) records you can sum, group, and bill from — finished off with field-level accuracy against a labelled set and a ranked vendor report.

**Learning objectives:**
- Extract text from a PDF (`pypdf`) — and handle multi-page documents.
- Chunk text into LLM-sized pieces, respecting sentence boundaries.
- Use structured-output prompting to extract typed fields.
- Validate the model's output with JSON Schema and Pydantic-style checks.
- Compute field-level accuracy against a labelled set.
- Aggregate extracted records into a pandas DataFrame — and recognise the pitfalls (low-confidence fields, missing data, table extraction).

**Sections:** 1 The shape of every document-processing pipeline · 2 Setup · 3 Generate a small set of synthetic invoices · 4 Chunking — when documents are too big for one prompt · 5 Extracting structured fields with the LLM · 6 Validating the extracted fields · 7 Building the final DataFrame · 8 Line-item drill-down · 9 Field-level accuracy · 10 Common pitfalls

**Practice:** 3 ✋ quick checkpoints · 4 🧪 practice exercises (incl. a Debug me 🐞) · 4 🧠 stretch exercises · 🎁 bonus mini-project: a "monthly billing report".

**Files/datasets:** the invoices are synthesised in-notebook (no external files); an inline invoice-extractor `MockLLM` keeps it offline. `pypdf` (and OCR options for scans) appear as reference snippets for real PDFs.

### 26 · AI Evaluation & Observability — `32_ai_evaluation_observability.ipynb`

You shipped an AI feature in NB 28–31 and the demo answers looked great — but how do you know it still works after someone tweaks a prompt or the provider updates the model? This notebook is "the difference between hobby AI and production AI". Mental model: **an eval is a regression test for something that won't sit still** — a smoke detector bolted to your feature, silent on a good day, the only thing that wakes you up on a bad one.

The running example is an **inbox-triage feature** that tags customer messages with a sentiment and a topic. Against it you build the whole observability stack: a 12-example golden set, per-class metrics, an LLM-as-judge (with its known biases, validated against human labels), call tracing, a cost dashboard, an A/B test of two prompt variants, and regression detection — assembled into one eval pipeline.

**Learning objectives:**
- Build a golden dataset for an AI feature and re-run it on every change.
- Choose the right metric: exact-match, structured-output match, semantic similarity, LLM-as-judge.
- Implement call tracing so every prompt + response is logged.
- Compute a cost dashboard from a trace log.
- Run an A/B test of two prompt variants and reach a defensible verdict.
- Detect regression (a new prompt makes things worse on previously-passing examples).

**Sections:** 1 Why "look at it and it seems fine" doesn't scale · 2 Setup — the MockLLM and a tiny golden dataset · 3 Run the feature and score it · 4 Per-class metrics · 5 LLM-as-judge · 6 Tracing — log every call · 7 The cost dashboard · 8 A/B-testing two prompt variants · 9 Regression detection · 10 Putting it together — the eval pipeline

**Practice:** 4 ✋ quick checkpoints · 3 🧪 practice exercises · 4 🧠 stretch exercises · 🎁 bonus mini-project: a pre-commit eval check.

**Files/datasets:** an inline `MockLLM` and a 12-example golden set built in-notebook (offline, no API key); the real-provider swap is one line via `../llm_providers.py`, documented in appendix A1.

## Appendix guides

Appendices are **reference-style**: demo/survey notebooks without the full exercise scaffolding, and every one runs end-to-end offline — real-library cells fall back to a built-in stand-in or appear as commented reference code.

### A1 · LLM Providers Guide — `A1_llm_providers_guide.ipynb`

The reference for swapping the course's `MockLLM` for real intelligence. Surveys the four providers wired into the repo-root `llm_providers.py` — 🟢 OpenAI, 🟠 Anthropic (Claude), 🔵 Google (Gemini), 🟣 Ollama (fully local) — all sharing the same `chat()` interface, so swapping providers in NB 27–32 (and the NB 48 capstone) is a one-line change. Covers install/auth for each, common model lists, a side-by-side comparison on the same task, back-of-envelope cost estimation, the embedding equivalents for NB 29 (hosted vs `sentence-transformers` vs `MockEmbedder`), and production patterns (retries, caching, fallbacks).

**Decision guidance:** a provider decision table over cost, latency, quality, and data-privacy constraints — plus how to size a local Ollama model to your RAM. 3 ✋ quick checkpoints and 3 exercises (provider-swap drill, cost estimate for your own workload, a local-first dev workflow).

### A2 · Vector-Store Landscape — `A2_vector_stores_survey.ipynb`

Picks up where NB 29's hand-rolled NumPy retriever hits its limits (latency, memory, operability) and surveys the vector-store field: index families first (IVF, HNSW, PQ), then **FAISS** (the workhorse local index, with an HNSW walk-through), **Chroma** (simplest embedded option), **Qdrant** (production-flavoured), **Weaviate / Pinecone / Milvus** (the rest of the field), and **pgvector** ("the boring-good choice when you already have Postgres") — closing with what LangChain / LlamaIndex / Haystack retrievers actually wrap. Runs offline on the course `MockEmbedder`; each store's real client code is shown as commented reference.

**Decision guidance:** a 4-question rubric — scale, hosting, filtering, ecosystem — so you can pick a store from constraints instead of hype. 3 ✋ quick checkpoints and 2 exercises (metadata filtering on the FAISS stand-in, recall-vs-k measurement).

### A3 · RAG & Agent Frameworks — `A3_rag_and_agent_frameworks.ipynb`

NB 29 built RAG by hand and NB 30 built agents by hand — so why do frameworks exist? Answer: *when your pipeline grows past hand-rolled and you want batteries — loaders, retrievers, tracing, evaluation, deploy — without writing them yourself.* This is a code-level tour of the major frameworks against the **same FAQ-with-citations RAG task**: a plain-Python baseline, then **LangChain** (LCEL pipes), **LlamaIndex** (retrieval-first), **Haystack** (production pipelines), **DSPy** (programmatic prompting), and the agent frameworks — **smolagents**, **AutoGen**, with **CrewAI** in the comparison table. Runs offline via `MockLLM`/`MockEmbedder`; framework snippets are reference code.

**Decision guidance:** a 3-question rubric for picking a framework — or *not* picking one and shipping faster. 3 ✋ quick checkpoints and 2 exercises (translate the baseline to LCEL style, frame an agent task as a state machine).

## The 5 disciplines this module trains

1. **Treat the LLM as a function call.** Typed inputs, structured outputs, retries, costs.
2. **Always wrap `json.loads` in `try/except`.** Real models occasionally misbehave.
3. **Confidence thresholds beat hallucination.** Refuse weak retrievals before they become wrong answers.
4. **Tools, not free-form generation.** When the answer is computable, *compute* it — don't ask the LLM.
5. **Eval set first, prompt iteration second.** Otherwise every "improvement" is a guess.

## How these notebooks work

Every notebook runs **100% offline** — a deterministic `MockLLM` (and `MockEmbedder`) stands in for real providers, so you need no API key, no internet, and no credit card; when you want real answers, the swap is one import via the repo-root `llm_providers.py` (appendix A1 is the guide). Each lesson opens with a Colab badge and a time/difficulty line, then follows the course rhythm: ✋ **Quick exercise (~2 min)** checkpoints with collapsible solutions as you go, end-of-lesson 🧪 practice exercises (⭐-rated, usually including a "Debug me 🐞"), 🧠 stretch exercises, and a 🎁 bonus mini-project. The three appendices are optional reference surveys — skip them on a first pass, return when you're choosing a real provider, vector store, or framework.

## Where next

→ **Module 13 — Production** (`../13_production/45_from_notebook_to_project.ipynb`)

---

📝 **Finished this module?** Test yourself with the [Module 8 quiz](../quizzes/quiz_08_ai_engineering.ipynb) — five questions, ~10 minutes.
