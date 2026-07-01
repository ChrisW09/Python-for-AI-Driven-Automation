# Module 14 — Business AI in Practice

**Goal:** Bridge the gap between *knowing how to build* AI systems (Modules 1–13) and *knowing how to land them inside a real organisation*. By the end of this module you will be able to walk a stakeholder through the architecture choices, the governance model, and the POC → MVP → Production path for any AI-automation initiative.

**Estimated time:** 5–7 hours.
**Prerequisites:** Modules 1 (foundations) and at least one of Modules 4 (ML) or 5 (AI Engineering). Strong background reading: NB 41 / 25 capstones — they make the business cases here much more vivid.

```
        ┌──────────────────────────────────────────────────────────┐
        │                  Modules 1–13                              │
        │       (you can already BUILD AI systems)                  │
        └─────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
        ┌──────────────────────────────────────────────────────────┐
        │           Module 14 — Business AI in Practice              │
        │                                                            │
        │  NB 43  Digital transformation & AI-induced change        │
        │  NB 44  Architecture patterns for AI applications         │
        │  NB 45  AI-assisted software development                  │
        │  NB 46  BPM integration, governance, POC→MVP→Prod         │
        │                                                            │
        │      (you can SHIP AI systems inside organisations)        │
        └──────────────────────────────────────────────────────────┘
```

## Notebooks

| # | Notebook | What you'll learn |
|---|---|---|
| 43 | `43_digital_transformation.ipynb` | Why AI now, what's *actually* changing in organisations, the maturity model, adoption pitfalls, the human side |
| 44 | `44_architecture_patterns.ipynb` | Single-tier scripts → 3-tier client-server → service / microservice patterns → end-to-end ML pipelines; when to use which |
| 45 | `45_ai_assisted_software_development.ipynb` | Modern IDEs, Git basics, prompt engineering for code, critical review of AI-generated artefacts, when *not* to trust the LLM |
| 46 | `46_bpm_governance_poc_mvp.ipynb` | Embedding AI in the BPM lifecycle, governance + RACI for AI projects, the POC → MVP → Production journey, three case studies |

## How this module is different from the rest

The earlier modules teach *technique*. This module teaches *judgement*. The exercises are heavier on analysis and design than on writing code:

- **Reflection exercises** — write down what you'd do as the technical lead for a hypothetical project.
- **Architecture sketches** — choose an architecture pattern and justify it in writing.
- **Case-study walkthroughs** — read a realistic scenario, identify the failure modes, propose a fix.
- **Code is illustrative** — small snippets that show the shape of a choice, not full implementations.

This shape mirrors how the course is actually taught: Modules 1–13 are the workshop; Module 14 is the seminar.

## Cross-references back to Modules 1–13

| If you want to revisit… | Open |
|---|---|
| The technical implementation of a feature | the corresponding Module 1–13 notebook |
| Packaging a script into a project | NB 39 |
| Scheduling and orchestration | NB 40 |
| End-to-end AI feature | NB 42 (capstone AI assistant) |
| LLM evaluation patterns | NB 26 |

## Where next

→ **Module 6 — AI Engineering** (`../06_ai_engineering/21_llm_fundamentals.ipynb`) — the hands-on deep-dive companion to this module. After that, **Module 5 — Industry Applications** (`../05_industry_applications/`, NB 17–20) and **Module 8 — Agents, Tools & MCP** (`../08_agents_tools_mcp/`, NB 31–34) complete the course.

→ **Module 13 — Capstones** (`../13_capstones/41_capstone_analytics.ipynb` or `42_capstone_ai_assistant.ipynb`), if you haven't done them yet. The capstones make many of the Module 14 ideas concrete.
