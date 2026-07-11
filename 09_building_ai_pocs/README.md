# Module 9 — Building AI POCs

> 🧭  [◀ AI Engineering](../08_ai_engineering/)  ·  [🏠 Course home](../README.md)  ·  [Agents, Tools & MCP ▶](../10_agents_tools_mcp/)

**Goal:** Give the technical depth to actually build LLM-powered prototypes end-to-end. Module 8 (AI Engineering) taught you how the pieces fit; this module is the *deep version* — the vibe-coding workflow, full RAG pipeline, vector-DB landscape, agentic AI mechanics, and progressive POCs that take you from a one-file Streamlit app to a 3-tier ML application. One running scenario — **ChurnScope**, a churn-radar tool for a small SaaS company — threads through all four notebooks, growing from a "Hello, Streamlit" skeleton into a RAG-grounded, agent-driven system.

**Estimated time:** 12–16 hours.

**Prerequisites:** Modules 1 (foundations), 4 (ML basics), and 6 (AI engineering). Module 16 strongly recommended for the architecture vocabulary.

```
┌───────────────────────────────────────────────────────────────────────────────┐
│  Module 9 — Building AI POCs                                                  │
│                                                                               │
│  NB 33  From Setup to First POC  (VS Code, Copilot Agent Mode, vibe coding)   │
│  NB 34  Three POCs of Growing Complexity  (Streamlit → 3-tier → ML pipeline)  │
│  NB 35  RAG Pipeline Deep Dive  (chunking, ANN, chat-with-your-PDF POC)       │
│  NB 36  Vector DBs + Agentic AI  (Chroma, tool calling, ReAct, two POCs)      │
└───────────────────────────────────────────────────────────────────────────────┘
```

The lecture block opens with **NB 27 — LLM Fundamentals** (Transformer, tokens, parameters), which lives in Module 8 (`../08_ai_engineering/27_llm_fundamentals.ipynb`) but is taught as the theory opener for this block.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 27 | `33_from_setup_to_first_poc.ipynb` | ~2.5 h | Intermediate | VS Code + Copilot Agent Mode setup, the vibe-coding loop, a Hello-Streamlit POC, and a parse → validate → retry structured-output loop |
| 28 | `34_three_pocs_growing_complexity.ipynb` | ~4 h | Advanced | ChurnScope three ways: Streamlit CSV app → 3-tier app (FastAPI + SQLite) → XGBoost churn pipeline, plus a microservices split (POC 3½) |
| 29 | `35_rag_pipeline_deep_dive.ipynb` | ~3 h | Intermediate / Advanced | The full RAG pipeline step by step, an offline mini-RAG in ~40 lines, and a chat-with-your-PDF Streamlit POC |
| 30 | `36_vector_db_and_agentic_ai.ipynb` | ~3 h | Advanced | A Chroma-backed semantic product search and a command-line ReAct agent |

## Notebook guides

### 27 · From Setup to First POC — `33_from_setup_to_first_poc.ipynb`

The bridge between the theory of NB 27 and the hands-on POCs of NB 34–36. You set up VS Code with GitHub Copilot Agent Mode and learn the **vibe-coding loop** that powers the rest of the module: describe the goal in natural language → AI generates code → you review and run → describe the next adjustment. The module's mental model is set here — *you are the architect, the AI is the builder* — and the running example **ChurnScope** starts as a "Hello, Streamlit" skeleton built from a single Agent-Mode prompt.

Beyond setup, the notebook covers Copilot's four modes (Inline, Ask, Plan, Agent), the 5-building-block anatomy of a good code prompt, the Git-first workflow (repo before code), `.gitignore` and secrets discipline, the top 6 vibe-coding pitfalls, and closes with the **structured-output loop** — turning messy LLM text into reliable data via defensive parsing, field validation, and bounded retries, demonstrated with a deterministic mock.

**Learning objectives:**
- Set up VS Code, Python, and GitHub Copilot following the 6-step roadmap.
- Distinguish Copilot's four modes (Inline, Ask, Plan, Agent) and pick the right one for the task.
- Run the vibe-coding loop deliberately rather than as a series of one-off prompts.
- Write a good code prompt following the 5-building-block anatomy.
- Practise the Git-first GitHub workflow so every POC has version control from minute one.
- Spot the top 6 vibe-coding pitfalls before they bite.

**Sections:**
- 1 Why this specific toolchain · 2 The 6-step setup roadmap · 3 GitHub Copilot — the four modes
- 4 The vibe-coding loop · 5 Anatomy of a good code prompt · 6 The Git-first workflow
- 7 `.gitignore` and secrets · 8 The top 6 vibe-coding pitfalls
- 9 Your first POC — Hello, Streamlit · 10 The structured-output loop

**Practice:** 4 ✋ quick checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project ("Your environment is now your platform")

**Files/datasets:** none read in-notebook — the structured-output demo uses an offline deterministic mock LLM, no API key.

### 28 · Three POCs of Growing Complexity — `34_three_pocs_growing_complexity.ipynb`

The workshop notebook of Module 9: ChurnScope gets built for real, three times, each POC from a single Copilot Agent-Mode prompt, with the architecture climbing one rung at a time. **POC 1** is a single Streamlit app for CSV analysis (one process, one file); **POC 2** refactors the same use case into a 3-tier architecture (Streamlit + FastAPI + SQLite — two processes, three concerns); **POC 3** extends it with an XGBoost churn-prediction model (full train → serve → predict → log pipeline). A bonus **POC 3½** actually splits the model out into its own microservice, so you run three processes and see what the gateway-as-client change costs.

The notebook also introduces the *other* axis of growing complexity — LLM call-graphs (one call → a chain → an agent loop) — proven with an offline two-step chain built on a deterministic, stdlib-only mock LLM, plus monorepo setup for one repo with three sub-projects and a side-by-side comparison of all three architectures.

**Learning objectives:**
- Build a single-tier Streamlit data-analysis app from a single Agent Mode prompt.
- Refactor it into a 3-tier architecture (Streamlit + FastAPI + SQLite) and articulate what changed *and what didn't*.
- Extend a 3-tier app with an ML model (XGBoost classifier, full train→serve→predict→log pipeline).
- Read and review AI-generated multi-file scaffolds.
- Manage a monorepo with one repo and three sub-projects.

**Sections:**
- 1 The mental model — same use case, three architectures · 2 Monorepo setup
- 3 POC 1 — Streamlit-only CSV analysis · 4 POC 2 — Streamlit + FastAPI + SQLite (3-tier)
- 5 POC 3 — Add an XGBoost churn-prediction model · 6 Comparing the three POCs
- 7 POC 3½ — Split into two services (microservices, actually implemented)

**Practice:** 4 ✋ quick checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. Debug me 🐞 on multi-process bugs) · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project ("Add a 4th POC of your own")

**Files/datasets:** none read in-notebook — the chain demo uses an offline stdlib-only mock LLM, no API key; POC 3's churn dataset is synthetic and generated inside the POC.

### 29 · RAG Pipeline Deep Dive — `35_rag_pipeline_deep_dive.ipynb`

The applied deep-dive companion to NB 29 (Embeddings & Retrieval): where NB 29 introduces vectors and similarity, this notebook walks the full production RAG pipeline, names every trade-off knob, and ends with a runnable Streamlit POC that lets you **chat with a PDF**. The running scenario: ChurnScope can *score* at-risk customers (NB 34), but the retention team's follow-up — "what do we actually do about it?" — lives in a 40-page retention-playbook PDF the LLM has never seen. RAG turns the closed-book exam into an open-book one, with a **librarian** (the retriever) finding the right page before the model writes a word.

The pipeline is dissected step by step — ingestion, chunking strategies, embeddings, vector storage, ANN under the hood (HNSW, IVF, IVF-PQ), cosine similarity worked by hand, prompt augmentation, generation — and a complete **mini-RAG in ~40 lines runs fully offline** inside the notebook with deterministic hard-coded vectors. It closes with the five production tuning knobs, a customer-service-bot example, and the RAG-vs-fine-tuning decision.

**Learning objectives:**
- Explain RAG to a non-technical stakeholder using the *open-book exam* analogy.
- Draw the full RAG pipeline end-to-end (offline indexing + online query).
- Choose chunking parameters based on document type and use case.
- Reason about ANN algorithms (HNSW, IVF, IVF-PQ) and when each is right.
- Tune the 5 production knobs (chunk size, top-k, embedding dim, re-ranker, hybrid search).
- Build a RAG-over-PDF POC in 30 minutes using one Copilot Agent prompt.

**Sections:**
- 1 The core idea — connect the LLM to your knowledge · 2 The RAG architecture at a glance
- 3 The full pipeline — indexing vs query · 4 Ingestion and chunking · 5 Embeddings
- 6 Vector storage · 7 ANN under the hood · 8 Similarity search · 9 Prompt augmentation + generation
- 10 Why RAG reduces hallucinations · 11 The five production tuning knobs
- 12 Realistic example — the customer-service bot · 13 RAG vs fine-tuning · 14 POC — Chat with your PDF

**Practice:** 4 ✋ quick checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project ("Persistent RAG")

**Files/datasets:** none read in-notebook — the mini-RAG uses hard-coded deterministic embeddings (a `sentence-transformers` snippet is shown as a non-executed reference); the playbook PDF only enters via the Agent-Mode POC you build in VS Code.

### 30 · Vector Databases & Agentic AI — `36_vector_db_and_agentic_ai.ipynb`

The final notebook of Module 9 covers the *infrastructure* layer (vector databases) and the *behaviour* layer (agentic AI) — together they take the RAG POC from "one-PDF demo" to "actually useful AI system", framed by the three-level ladder **Just-LLM → LLM + RAG → LLM + RAG + Agent**. For ChurnScope this ties off two loose ends: NB 35's librarian kept its library in memory (restart = index gone), so Part A gives it a persistent, scalable shelf; and ChurnScope so far only *answers*, so Part B gives it the ability to *act*.

**Part A** times brute-force kNN, shows why O(n) doesn't scale and how an ANN index prunes the search, tours the vector-database landscape (FAISS, Chroma, Qdrant, Weaviate, Pinecone, pgvector) with a selection heuristic, and shows insert/query with Chroma in 15 lines. **Part B** defines an agent as LLM + Tools + Memory + Planning, walks JSON-schema tool calling end-to-end, traces the ReAct loop with a travel-planning agent, and weighs when multi-agent pays for its coordination overhead. Two POCs close the module: a **semantic product search** on Chroma and a **command-line ReAct agent**.

**Learning objectives:**
- Explain what makes a vector database different from SQL/NoSQL and when each is right.
- Compare FAISS, Chroma, Qdrant, Weaviate, Pinecone, pgvector by deployment context.
- Define an agent as LLM + Tools + Memory + Planning.
- Trace tool calling end-to-end using the JSON-schema function-call pattern.
- Distinguish ReAct, Plan-and-Execute, Tree-of-Thoughts, and Reflexion as control loops.
- Build two POCs: a semantic-product-search Chroma app and a ReAct command-line agent.

**Sections:**
- Part A — 1 Vector embedding refresher · 2 Traditional DB vs vector DB · 3 The vector-database landscape
- 4 Inserting and querying — Chroma in 15 lines · 5 POC 1 — Semantic Product Search with Chroma
- Part B — 6 Defining an agent · 7 JSON and JSON Schema primer · 8 How tool calling actually works
- 9 Memory — short-term vs long-term · 10 Planning — task decomposition · 11 The ReAct loop
- 12 Multi-agent — when and when not · 13 Example agent workflows
- 14 POC 2 — A ReAct command-line agent · 15 Synthesis — the three levels of LLM usage

**Practice:** 4 ✋ quick checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project ("Ship a small agent that earns its keep")

**Files/datasets:** none read in-notebook — kNN/ANN demos run on NumPy arrays and the tool-calling walkthrough is simulated with plain JSON, no API key.

## How these notebooks work

Every notebook runs **100% offline** — LLM behaviour comes from deterministic in-notebook mocks and hard-coded embedding vectors, so no API key is ever needed. Concepts are drilled with **✋ Quick exercise (~2 min)** checkpoints whose solutions sit in collapsible `<details>` blocks, and each notebook ends with ⭐-rated 🧪 practice exercises (always including a "Debug me 🐞"), ⭐⭐⭐ 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways, and a self-assessment.

The module builds directly on Module 8 — same stack, one level up:

| Module 8 (AI Engineering) | Module 9 (Building AI POCs) |
|---|---|
| One feature per notebook | Progressive POCs that compose |
| Conceptual + small code examples | Full Copilot Agent Mode prompts you can paste verbatim |
| MockLLM-first (works offline) | Real LLM provider workflow with cost/secrets discipline |
| Library-level (sklearn, FAISS) | Application-level (Streamlit + FastAPI + SQLite + Chroma) |

Each notebook ships a self-contained Copilot Agent-Mode prompt that builds a working prototype in VS Code, so the lab session is *paste the prompt → review the generated code → iterate* — while the in-notebook demo cells stay offline and mock-driven.

## Where next

→ Module 7 (`../07_industry_applications/`, NB 23–26) — apply the toolkit to churn + CLV, fraud, segmentation + recommenders, and forecasting use-cases.
→ Module 10 (`../10_agents_tools_mcp/`, NB 37–40) — the direct sequel to NB 36: agent architectures, hardened tools, MCP, multi-agent systems.
→ Module 15 capstones (`../15_capstones/`) — apply what you learned to a complete deliverable.
→ Module 16 (`../16_business_ai/`) — embed your POC into a real organisation: governance, BPM, POC→MVP→Production.

---

📝 **Finished this module?** Test yourself with the [Module 9 quiz](../quizzes/quiz_09_building_ai_pocs.ipynb) — five questions, ~10 minutes.
