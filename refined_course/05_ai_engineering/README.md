# Module 5 — AI Engineering

**Goal:** Use LLMs from Python as engineered, observable, evaluated components — not as magic. By the end of this module you can build, test, and ship an AI feature.

**Estimated time:** 8–10 hours.
**Prerequisites:** Modules 1–2 (functions, JSON, HTTP). Module 4 is helpful for the evaluation chapter.

```
                  ┌────────────────────────────────────┐
                  │  LLM = function call               │
                  │  (system + user + assistant)       │
                  └─────────────────┬──────────────────┘
                                    │
        ┌───────────────────┬───────┴───────┬─────────────────┐
        ▼                   ▼               ▼                 ▼
   NB 18                NB 19          NB 20             NB 21
   prompts +            embeddings     tools +           document
   structured           + RAG          agents            processing
   output                                                    
                                    │
                                    ▼
                            NB 22 — evaluation
                          golden sets, LLM-as-judge,
                          cost dashboards, regression tests
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 18 | `18_ai_workflows.ipynb` | Inbox-triage with the MockLLM (prompts, JSON output, batch) |
| 19 | `19_embeddings_retrieval.ipynb` | TF-IDF + dense retrieval, retrieval@k benchmark |
| 20 | `20_tools_and_agents.ipynb` | A multi-tool data assistant |
| 21 | `21_document_processing.ipynb` | An invoice-extraction pipeline with validation |
| 22 | `22_ai_evaluation_observability.ipynb` | LLM evals, cost dashboards, regression tests |

## The 5 disciplines this module trains

1. **Treat the LLM as a function call.** Typed inputs, structured outputs, retries, costs.
2. **Always wrap `json.loads` in `try/except`.** Real models occasionally misbehave.
3. **Confidence thresholds beat hallucination.** Refuse weak retrievals before they become wrong answers.
4. **Tools, not free-form generation.** When the answer is computable, *compute* it — don't ask the LLM.
5. **Eval set first, prompt iteration second.** Otherwise every "improvement" is a guess.

## Where next

→ **Module 6 — Production** (`../06_production/23_from_notebook_to_project.ipynb`)
