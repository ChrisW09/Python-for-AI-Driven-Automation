# Module 7 — Building AI POCs (Hands-On Deep Dives)

**Goal:** Give the technical depth to actually build LLM-powered prototypes end-to-end. Module 6 (AI Engineering) taught you how the pieces fit; this module is the *deep version* — Transformer mechanics, full RAG pipeline, vector-DB landscape, agentic AI mechanics, and three progressive POCs that take you from a one-file Streamlit app to a 3-tier ML application.

This module mirrors the lecture-slide flow used in the course, so the entire syllabus can be taught from the notebooks alone.

**Estimated time:** 12–16 hours.
**Prerequisites:** Modules 1 (foundations), 4 (ML basics), and 6 (AI engineering). Module 14 strongly recommended for the architecture vocabulary.

```
        ┌──────────────────────────────────────────────────────────────────┐
        │  Module 7 — Building AI POCs                                     │
        │                                                                    │
        │  NB 27  From Setup to First POC (VS Code, Copilot, vibe coding)   │
        │  NB 28  Three POCs (Streamlit → 3-tier → ML pipeline)             │
        │  NB 29  RAG Pipeline Deep Dive (chunking, ANN, RAG-over-PDF POC)  │
        │  NB 30  Vector DBs + Agentic AI (tool calling, ReAct, two POCs)   │
        └──────────────────────────────────────────────────────────────────┘
```

The lecture block opens with **NB 21 — LLM Fundamentals** (Transformer, tokens, parameters), which lives in Module 6 (`../06_ai_engineering/21_llm_fundamentals.ipynb`) but is taught as the theory opener for this block.

## Notebooks

| # | Notebook | Slide source |
|---|---|---|
| 21 | `../06_ai_engineering/21_llm_fundamentals.ipynb` (Module 6) | "Building with LLMs" Parts 1–2 |
| 27 | `27_from_setup_to_first_poc.ipynb` | "Getting Started with POCs" + "POCs mit VS Code" §1–§3 |
| 28 | `28_three_pocs_growing_complexity.ipynb` | "POCs mit VS Code" §4–§7 |
| 29 | `29_rag_pipeline_deep_dive.ipynb` | "Building with LLMs" Part 3 |
| 30 | `30_vector_db_and_agentic_ai.ipynb` | "Building with LLMs" Parts 4–5 |

## How this module is different from Module 6

| Module 6 (AI Engineering) | Module 7 (Building AI POCs) |
|---|---|
| One feature per notebook | Progressive POCs that compose |
| Conceptual + small code examples | Full Copilot Agent Mode prompts you can paste verbatim |
| MockLLM-first (works offline) | Real LLM provider workflow with cost/secrets discipline |
| Library-level (sklearn, FAISS) | Application-level (Streamlit + FastAPI + SQLite + Chroma) |

## Recommended teaching order

1. NB 21 — Transformer / LLM theory (1 lecture)
2. NB 27 — Setup + first Streamlit POC (1 lecture, with live setup)
3. NB 28 — Three POCs progression (2 lectures — one per architecture step)
4. NB 29 — RAG deep dive + PDF POC (1 lecture + lab)
5. NB 30 — Vector DBs + Agentic AI + two POCs (1 lecture + lab)

Each notebook ends with a self-contained Copilot Agent Mode prompt that builds a working prototype in VS Code, so the lab session is *paste the prompt → review the generated code → iterate*.

## Where next

→ Module 5 (`../05_industry_applications/`, NB 17–20) — apply the toolkit to churn + CLV, fraud, segmentation + recommenders, and forecasting use-cases.
→ Module 8 (`../08_agents_tools_mcp/`, NB 31–34) — the direct sequel to NB 30: agent architectures, hardened tools, MCP, multi-agent systems.
→ Module 13 capstones (`../13_capstones/`) — apply what you learned to a complete deliverable.
→ Module 14 (`../14_business_ai/`) — embed your POC into a real organisation: governance, BPM, POC→MVP→Production.
