# Module 6 — AI Engineering

**Goal:** Use LLMs from Python as engineered, observable, evaluated components — not as magic. By the end of this module you can build, test, and ship an AI feature.

**Estimated time:** 8–10 hours.
**Prerequisites:** Modules 1–2 (functions, JSON, HTTP). Module 4 is helpful for the evaluation chapter.

```
                  ┌────────────────────────────────────┐
                  │  NB 21 — LLM fundamentals:         │
                  │  the LLM as a function call        │
                  │  (system + user + assistant)       │
                  └─────────────────┬──────────────────┘
                                    │
        ┌───────────────────┬───────┴───────┬─────────────────┐
        ▼                   ▼               ▼                 ▼
   NB 22                NB 23          NB 24             NB 25
   prompts +            embeddings     tools +           document
   structured           + RAG          agents            processing
   output                                                    
                                    │
                                    ▼
                            NB 26 — evaluation
                          golden sets, LLM-as-judge,
                          cost dashboards, regression tests
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 21 | `21_llm_fundamentals.ipynb` | The theory floor: tokens, next-token prediction, the Transformer, prompting, limitations |
| 22 | `22_ai_workflows.ipynb` | Inbox-triage with the MockLLM (prompts, JSON output, batch) |
| 23 | `23_embeddings_retrieval.ipynb` | TF-IDF + dense retrieval, retrieval@k benchmark |
| 24 | `24_tools_and_agents.ipynb` | A multi-tool data assistant |
| 25 | `25_document_processing.ipynb` | An invoice-extraction pipeline with validation |
| 26 | `26_ai_evaluation_observability.ipynb` | LLM evals, cost dashboards, regression tests |

## Optional appendices — provider, vector-store & framework surveys

| Appendix | Notebook | Focus |
|---|---|---|
| A1 | `A1_llm_providers_guide.ipynb` | OpenAI / Anthropic / Google / Ollama — unified `chat()` interface, model picks, cost notes |
| A2 | `A2_vector_stores_survey.ipynb` | FAISS, Chroma, Qdrant, Weaviate, Pinecone, pgvector — decision rubric |
| A3 | `A3_rag_and_agent_frameworks.ipynb` | LangChain, LlamaIndex, Haystack, DSPy, AutoGen, CrewAI, smolagents |

## The 5 disciplines this module trains

1. **Treat the LLM as a function call.** Typed inputs, structured outputs, retries, costs.
2. **Always wrap `json.loads` in `try/except`.** Real models occasionally misbehave.
3. **Confidence thresholds beat hallucination.** Refuse weak retrievals before they become wrong answers.
4. **Tools, not free-form generation.** When the answer is computable, *compute* it — don't ask the LLM.
5. **Eval set first, prompt iteration second.** Otherwise every "improvement" is a guess.

## Where next

→ **Module 11 — Production** (`../11_production/39_from_notebook_to_project.ipynb`)
