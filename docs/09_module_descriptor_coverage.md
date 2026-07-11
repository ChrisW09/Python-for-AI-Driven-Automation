> **Note (July 2026).** This document predates the learning-order renumbering (modules 0–17 / lessons 1–52 were re-sequenced); lesson and module numbers below refer to the **old** numbering and are kept as a historical record.

# Module-Descriptor Coverage Matrix (Modulhandbuch ↔ Course)

Mapping the official **Lernergebnisse / Kompetenzen** and **Inhalte** to where the course actually delivers them. Notebook numbers are the canonical layout (NB 1–38, contiguous).

**Verdict:** the course covers **all six competencies and all thirteen content items.** Coverage is *full* for 12 of 13 contents and 5 of 6 competencies; the remaining items are *full on content* with one delivery-level nuance each (the "interdisciplinary team" dimension and "microservices" as an implemented — vs taught — pattern). Details and the two nuances are below.

---

## A. Lernergebnisse / Kompetenzen

| # | Competency (abridged) | Where it's delivered | Rating |
|---|---|---|---|
| 1 | Explain, critically discuss and form well-founded judgements about AI-based automation **in the business context** | **Module 14** — NB 43 (digital transformation, maturity model, adoption pitfalls), NB 44 (architecture trade-offs), NB 46 (BPM, governance, 3 case studies). Seminar-style reflection / architecture-sketch / case-study exercises throughout. | ✅ Full |
| 2 | Use modern data-science methods & tools — **especially Python** — for preparing, analysing, **visualising** and **modelling** business data | **Modules 1–4** — Python (NB 1–6), I/O (NB 12–13), pandas/NumPy/**matplotlib**/statistics/time-series (NB 7–11), scikit-learn modelling (NB 14–16). **Module 5** (NB 17–20) applies it to churn/CLV, fraud, segmentation & forecasting business cases; Capstone A (NB 41) proves it end-to-end. | ✅ Full |
| 3 | Use **AI-assisted software development** (AI code assistance, **version control & collaborative workflows on GitHub**) to build prototypes fast & quality-assured; **critically evaluate & improve AI-generated artefacts** | **NB 45** (IDE landscape, Git: commit/branch/merge/conflict, **Pull-Request & review workflow**, 5 prompt patterns, **4 failure modes + 60-second review checklist**, "when *not* to trust the AI") + **NB 27** (VS Code + Copilot Agent Mode, repo/`.gitignore`/secrets). Practiced via fork → branch → PR → self-review. | ✅ Full |
| 4 | Design **RAG** applications and **agentic AI** systems; implement them prototypically in **service-oriented (microservice) architectures** | RAG: **NB 22** (embeddings/retrieval), **NB 29** (RAG pipeline deep-dive + RAG-over-PDF POC), NB 24. Agentic: **NB 23** (tools + agents), **NB 30** (tool-calling + ReAct agent POC). Service-oriented impl.: **NB 28** (working **FastAPI** 3-tier REST service + ML pipeline, **§7 splits it into gateway + model microservice**), **NB 44** (service-/microservice patterns). | ✅ Full¹ |
| 5 | Turn a real AI use-case **in an interdisciplinary team** into a running **POC**, then sketch a viable **MVP** design and the path to **production** | **NB 46** (POC→MVP→Production methodology, Ist-analysis → Soll-architecture → readiness checklist → roadmap, 3 cases) + **NB 28–30** (build 3 progressive POCs incl. RAG & agent) + **Capstone B / NB 42** (end-to-end AI feature). | ✅ Full on content² |

¹ **Nuance — "microservices" (resolved):** the service-oriented prototype is fully built (FastAPI + REST + SQLite, NB 28), the pattern is taught with a decision rubric (NB 44 §5), and **NB 28 §7 now implements a real two-service decomposition** — the model split into its own FastAPI microservice behind the gateway, with the costs (network hop, health checks, graceful degradation) made explicit. Combining a RAG/agent *inside* that service in one artefact remains sketched (NB 44's deployment sketch) rather than built — a reasonable scope line for a POC-level course.

² **Nuance — "interdisciplinary team" (supported):** every content piece (POC, MVP roadmap, production sketch) is present, and **NB 46 §6 now prescribes the team format** — four roles mapped to the RACI, a four-week cadence (Ist-analysis → Soll-architecture → POC build → readiness + pitch), deliverables per role, and a grading rubric. Actually running it as a group remains a delivery choice, but the notebook now enforces the structure rather than merely permitting it.

---

## B. Inhalte

| # | Content item (abridged) | Where it's delivered | Rating |
|---|---|---|---|
| 1 | Digital transformation & AI-induced change in organisations | NB 43 | ✅ Full |
| 2 | Python data-science foundations: types, functions, data structures, **numeric computing**, **tabular data**, **visualisation** | NB 1–6 (types/control/structures/functions/OOP), NB 8 (NumPy), NB 7 (pandas), NB 9 (matplotlib) | ✅ Full |
| 3 | Intro to **machine learning** (supervised, **classification & regression**) | NB 14 (churn classification + NPS regression), NB 15 (evaluation), NB 16 (feature engineering) | ✅ Full |
| 4 | AI-assisted software development: modern IDEs, Git version control, AI code assistance, **prompt engineering**, critical review of AI artefacts | NB 45 (+ NB 27) | ✅ Full |
| 5 | **Architecture patterns of growing complexity**: single-tier → multi-tier client/server → service/microservice → end-to-end pipelines | NB 44 (all five patterns + decision table) implemented progressively in NB 28 (1-file → 3-tier → ML pipeline) | ✅ Full |
| 6 | **Generative language models**: principles, context handling, typical failure modes, quality assurance | NB 26 (Transformer, tokens, next-token prediction, attention, failure modes), NB 21 (LLM-as-function, structured output), NB 25 (eval/observability = QA) | ✅ Full |
| 7 | **RAG**: semantic knowledge representation & indexing | NB 22 (embeddings, TF-IDF vs dense, retrieval@k), NB 29 (chunking, ANN, full pipeline) | ✅ Full |
| 8 | **Semantic / vector databases** as a persistent base for conversational knowledge access | NB 30 (Chroma persistent vector DB + semantic-search POC), Appendix A2 (FAISS/Chroma/Qdrant/pgvector survey) | ✅ Full |
| 9 | **Agentic AI**: multi-step planning and the **limits** of autonomous systems | NB 23 (tool calling, small agents, "when NOT to use an agent"), NB 30 (ReAct loop + honest "does the agent earn its keep?") | ✅ Full |
| 10 | Embedding AI into existing business processes; **BPM lifecycle** | NB 46 §1 (AI across analyse/design/execute/monitor) | ✅ Full |
| 11 | Roles, responsibilities & **governance** (human + AI actors) | NB 46 §2 (**RACI** for AI, AI-as-participant, human always accountable) | ✅ Full |
| 12 | **POC & MVP project**: as-is analysis, target architecture, running POC with ≥1 modern AI component, MVP roadmap, production sketch | NB 46 (methodology + roadmap + readiness checklist) + NB 28–30 (running POCs with RAG/agent/ML components) + Capstone B (NB 42) | ✅ Full |
| 13 | **Case studies** of AI-based automation in companies | NB 46 (3 detailed cases incl. a project that was *stopped*), NB 43 (adoption pitfalls) | ✅ Full |

---

## C. Summary

- **Competencies:** 6 / 6 covered. Two carry a delivery-level nuance only (team format; microservices-as-implemented).
- **Contents:** 13 / 13 covered, all at full depth.
- The alignment is unsurprisingly strong because the course's structure mirrors the descriptor: **Modules 1–4** deliver the Python / data-science / ML competency (#2, contents 2–3), **Module 6** + **Module 7** deliver generative-AI / RAG / agentic / vector-DB / POC content (#4, contents 6–9, 12), **Module 11** the engineering discipline, **Module 5** the applied business use cases on top of Modules 1–4, and **Module 14** the business-context, BPM, governance and case-study content (#1, #5, contents 1, 5, 10, 11, 13). AI-assisted development (#3, content 4) is its own notebook (NB 45) plus the Copilot workflow in NB 27.

### Delivery notes (both formerly-open items now have course support)
1. **Team format — provided.** NB 46 §6 defines the four-role / four-week seminar format with RACI-mapped responsibilities, weekly deliverables and a grading rubric. The remaining instructor action is simply to assign teams.
2. **Microservices — implemented.** NB 28 §7 ("POC 3½") splits the 3-tier POC into a gateway + model microservice with code, run instructions, an Agent-Mode prompt and a self-check. The decision rubric stays in NB 44 §5; the cut is now demonstrated, not just described.
