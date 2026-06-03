# Module 8 — Business AI in Practice

**Goal:** Bridge the gap between *knowing how to build* AI systems (Modules 1–7) and *knowing how to land them inside a real organisation*. By the end of this module you will be able to walk a stakeholder through the architecture choices, the governance model, and the POC → MVP → Production path for any AI-automation initiative.

**Estimated time:** 5–7 hours.
**Prerequisites:** Modules 1 (foundations) and at least one of Modules 4 (ML) or 5 (AI Engineering). Strong background reading: NB 24 / 27 capstones — they make the business cases here much more vivid.

```
        ┌──────────────────────────────────────────────────────────┐
        │                  Modules 1–7                              │
        │       (you can already BUILD AI systems)                  │
        └─────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
        ┌──────────────────────────────────────────────────────────┐
        │           Module 8 — Business AI in Practice              │
        │                                                            │
        │  NB 26  Digital transformation & AI-induced change        │
        │  NB 27  Architecture patterns for AI applications         │
        │  NB 28  AI-assisted software development                  │
        │  NB 29  BPM integration, governance, POC→MVP→Prod         │
        │                                                            │
        │      (you can SHIP AI systems inside organisations)        │
        └──────────────────────────────────────────────────────────┘
```

## Notebooks

| # | Notebook | What you'll learn |
|---|---|---|
| 28 | `26_digital_transformation.ipynb` | Why AI now, what's *actually* changing in organisations, the maturity model, adoption pitfalls, the human side |
| 29 | `27_architecture_patterns.ipynb` | Single-tier scripts → 3-tier client-server → service / microservice patterns → end-to-end ML pipelines; when to use which |
| 30 | `28_ai_assisted_software_development.ipynb` | Modern IDEs, Git basics, prompt engineering for code, critical review of AI-generated artefacts, when *not* to trust the LLM |
| 31 | `29_bpm_governance_poc_mvp.ipynb` | Embedding AI in the BPM lifecycle, governance + RACI for AI projects, the POC → MVP → Production journey, three case studies |

## How this module is different from the rest

The earlier modules teach *technique*. This module teaches *judgement*. The exercises are heavier on analysis and design than on writing code:

- **Reflection exercises** — write down what you'd do as the technical lead for a hypothetical project.
- **Architecture sketches** — choose an architecture pattern and justify it in writing.
- **Case-study walkthroughs** — read a realistic scenario, identify the failure modes, propose a fix.
- **Code is illustrative** — small snippets that show the shape of a choice, not full implementations.

This shape mirrors how the course is actually taught: Modules 1–7 are the workshop; Module 8 is the seminar.

## Cross-references back to Modules 1–7

| If you want to revisit… | Open |
|---|---|
| The technical implementation of a feature | the corresponding Module 1–7 notebook |
| Packaging a script into a project | NB 22 |
| Scheduling and orchestration | NB 23 |
| End-to-end AI feature | NB 25 (capstone AI assistant) |
| LLM evaluation patterns | NB 21 |

## Where next

→ **Module 7 — Capstones** (`../07_capstones/24_capstone_analytics.ipynb` or `25_capstone_ai_assistant.ipynb`), if you haven't done them yet. The capstones make many of the Module 8 ideas concrete.
