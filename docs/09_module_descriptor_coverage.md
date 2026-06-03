# Module-Descriptor Coverage Matrix (Modulhandbuch ↔ Course)

Mapping the official **Lernergebnisse / Kompetenzen** and **Inhalte** to where the course actually delivers them. Notebook numbers are the canonical layout (NB 1–36; 9 and 25 intentionally absent).

**Verdict:** the course covers **all six competencies and all thirteen content items.** Coverage is *full* for 12 of 13 contents and 5 of 6 competencies; the remaining items are *full on content* with one delivery-level nuance each (the "interdisciplinary team" dimension and "microservices" as an implemented — vs taught — pattern). Details and the two nuances are below.

---

## A. Lernergebnisse / Kompetenzen

| # | Competency (abridged) | Where it's delivered | Rating |
|---|---|---|---|
| 1 | Explain, critically discuss and form well-founded judgements about AI-based automation **in the business context** | **Module 8** — NB 28 (digital transformation, maturity model, adoption pitfalls), NB 29 (architecture trade-offs), NB 31 (BPM, governance, 3 case studies). Seminar-style reflection / architecture-sketch / case-study exercises throughout. | ✅ Full |
| 2 | Use modern data-science methods & tools — **especially Python** — for preparing, analysing, **visualising** and **modelling** business data | **Modules 1–4** — Python (NB 1–6), I/O (NB 7–8), pandas/NumPy/**matplotlib**/statistics/time-series (NB 10–14), scikit-learn modelling (NB 15–17). Capstone A (NB 26) applies it end-to-end. | ✅ Full |
| 3 | Use **AI-assisted software development** (AI code assistance, **version control & collaborative workflows on GitHub**) to build prototypes fast & quality-assured; **critically evaluate & improve AI-generated artefacts** | **NB 30** (IDE landscape, Git: commit/branch/merge/conflict, **Pull-Request & review workflow**, 5 prompt patterns, **4 failure modes + 60-second review checklist**, "when *not* to trust the AI") + **NB 33** (VS Code + Copilot Agent Mode, repo/`.gitignore`/secrets). Practiced via fork → branch → PR → self-review. | ✅ Full |
| 4 | Design **RAG** applications and **agentic AI** systems; implement them prototypically in **service-oriented (microservice) architectures** | RAG: **NB 19** (embeddings/retrieval), **NB 35** (RAG pipeline deep-dive + RAG-over-PDF POC), NB 21. Agentic: **NB 20** (tools + agents), **NB 36** (tool-calling + ReAct agent POC). Service-oriented impl.: **NB 34** (working **FastAPI** 3-tier REST service + ML pipeline), **NB 29** (service-/microservice patterns). | ✅ Full¹ |
| 5 | Turn a real AI use-case **in an interdisciplinary team** into a running **POC**, then sketch a viable **MVP** design and the path to **production** | **NB 31** (POC→MVP→Production methodology, Ist-analysis → Soll-architecture → readiness checklist → roadmap, 3 cases) + **NB 34–36** (build 3 progressive POCs incl. RAG & agent) + **Capstone B / NB 27** (end-to-end AI feature). | ✅ Full on content² |

¹ **Nuance — "microservices":** the *service-oriented prototype* is fully built (FastAPI + REST + SQLite, NB 34) and the **microservices** pattern is taught with a decision rubric (NB 29 §5). A true *multi-service decomposition* is conceptual rather than implemented — appropriate for a POC-level course, but worth knowing the implemented artefact is a single 3-tier service. Combining a RAG/agent *inside* that service in one artefact is sketched (NB 29's "NB 27 → production" deployment sketch) rather than built as one combined app.

² **Nuance — "interdisciplinary team":** every content piece (POC, MVP roadmap, production sketch) is present and the capstone/Module-9 POCs are exactly the right deliverables, but the materials are written for **self-study**. The *team* dimension is a course-delivery/assessment choice (run NB 31's project + a Module-9 POC as a group); the notebooks support it but don't simulate or enforce a team. Not a content gap — a delivery note.

---

## B. Inhalte

| # | Content item (abridged) | Where it's delivered | Rating |
|---|---|---|---|
| 1 | Digital transformation & AI-induced change in organisations | NB 28 | ✅ Full |
| 2 | Python data-science foundations: types, functions, data structures, **numeric computing**, **tabular data**, **visualisation** | NB 1–6 (types/control/structures/functions/OOP), NB 11 (NumPy), NB 10 (pandas), NB 12 (matplotlib) | ✅ Full |
| 3 | Intro to **machine learning** (supervised, **classification & regression**) | NB 15 (churn classification + NPS regression), NB 16 (evaluation), NB 17 (feature engineering) | ✅ Full |
| 4 | AI-assisted software development: modern IDEs, Git version control, AI code assistance, **prompt engineering**, critical review of AI artefacts | NB 30 (+ NB 33) | ✅ Full |
| 5 | **Architecture patterns of growing complexity**: single-tier → multi-tier client/server → service/microservice → end-to-end pipelines | NB 29 (all five patterns + decision table) implemented progressively in NB 34 (1-file → 3-tier → ML pipeline) | ✅ Full |
| 6 | **Generative language models**: principles, context handling, typical failure modes, quality assurance | NB 32 (Transformer, tokens, next-token prediction, attention, failure modes), NB 18 (LLM-as-function, structured output), NB 22 (eval/observability = QA) | ✅ Full |
| 7 | **RAG**: semantic knowledge representation & indexing | NB 19 (embeddings, TF-IDF vs dense, retrieval@k), NB 35 (chunking, ANN, full pipeline) | ✅ Full |
| 8 | **Semantic / vector databases** as a persistent base for conversational knowledge access | NB 36 (Chroma persistent vector DB + semantic-search POC), Appendix A2 (FAISS/Chroma/Qdrant/pgvector survey) | ✅ Full |
| 9 | **Agentic AI**: multi-step planning and the **limits** of autonomous systems | NB 20 (tool calling, small agents, "when NOT to use an agent"), NB 36 (ReAct loop + honest "does the agent earn its keep?") | ✅ Full |
| 10 | Embedding AI into existing business processes; **BPM lifecycle** | NB 31 §1 (AI across analyse/design/execute/monitor) | ✅ Full |
| 11 | Roles, responsibilities & **governance** (human + AI actors) | NB 31 §2 (**RACI** for AI, AI-as-participant, human always accountable) | ✅ Full |
| 12 | **POC & MVP project**: as-is analysis, target architecture, running POC with ≥1 modern AI component, MVP roadmap, production sketch | NB 31 (methodology + roadmap + readiness checklist) + NB 34–36 (running POCs with RAG/agent/ML components) + Capstone B (NB 27) | ✅ Full |
| 13 | **Case studies** of AI-based automation in companies | NB 31 (3 detailed cases incl. a project that was *stopped*), NB 28 (adoption pitfalls) | ✅ Full |

---

## C. Summary

- **Competencies:** 6 / 6 covered. Two carry a delivery-level nuance only (team format; microservices-as-implemented).
- **Contents:** 13 / 13 covered, all at full depth.
- The alignment is unsurprisingly strong because the course's structure mirrors the descriptor: **Modules 1–4** deliver the Python / data-science / ML competency (#2, contents 2–3), **Module 5** + **Module 9** deliver generative-AI / RAG / agentic / vector-DB / POC content (#4, contents 6–9, 12), **Module 6** the engineering discipline, and **Module 8** the business-context, BPM, governance and case-study content (#1, #5, contents 1, 5, 10, 11, 13). AI-assisted development (#3, content 4) is its own notebook (NB 30) plus the Copilot workflow in NB 33.

### Two things to decide at delivery time (not gaps)
1. **Run the POC/MVP work as a team.** The content is all there (NB 31 + a Module-9 POC + Capstone B); to satisfy "*in an interdisciplinary team*" literally, assign it as a group project with defined roles (NB 31's RACI section gives the vocabulary).
2. **If "microservices (plural)" must be *implemented***, extend NB 34 with a second service (e.g., split the model server from the API, or add the RAG service from NB 35 as a separate microservice the FastAPI app calls). NB 34 Stretch B (Postgres) and the NB 29 → NB 34 bridge are natural starting points. As written, the course *teaches* microservices and *implements* a service-oriented 3-tier prototype, which matches the descriptor's intent at POC level.
