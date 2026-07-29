# Module 16 — Business AI

> 🧭  [◀ Capstones](../15_capstones/)  ·  [🏠 Course home](../README.md)  ·  [Django ▶](../17_django/)

**Goal:** Bridge the gap between *knowing how to build* AI systems (Modules 1–15) and *knowing how to land them inside a real organisation*. By the end of this module you will be able to walk a stakeholder through the architecture choices, the governance model, and the POC → MVP → Production path for any AI-automation initiative.

**Estimated time:** 5–7 hours.

**Prerequisites:** Modules 1 (foundations) and at least one of Modules 5 (ML) or 8 (AI Engineering). NB 50 additionally leans on Module 13 (packaging & scheduling, NB 45–46); NB 49 and NB 51 are flagged "recommended early" and are essentially prerequisite-free. Strong background reading: the NB 47–48 capstones — they make the business cases here much more vivid.

```
        ┌──────────────────────────────────────────────────────────┐
        │                  Modules 1–15                              │
        │       (you can already BUILD AI systems)                  │
        └─────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
        ┌──────────────────────────────────────────────────────────┐
        │           Module 16 — Business AI in Practice              │
        │                                                            │
        │  NB 49  Digital transformation & AI-induced change        │
        │  NB 50  Architecture patterns for AI applications         │
        │  NB 51  AI-assisted software development                  │
        │  NB 52  BPM integration, governance, POC→MVP→Prod         │
        │                                                            │
        │      (you can SHIP AI systems inside organisations)        │
        └──────────────────────────────────────────────────────────┘
```

One running example ties the four notebooks together: 🏢 **Meridian**, a fictional ~400-person B2B SaaS company, decides *what* to automate (NB 49), *how to structure it* (NB 50), *how to build it with an AI assistant* (NB 51), and *how to ship and govern it* (NB 52) — same company, four chapters, so the abstractions always have a face attached.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn |
|---|---|---|---|---|
| 49 | `49_digital_transformation.ipynb` | ~1.5 h | Intermediate | Why AI feels different *this* time, tasks-not-jobs framing, the five-stage maturity model, three change strategies, the four adoption pitfalls, the human side |
| 50 | `50_architecture_patterns.ipynb` | ~1.5 h | Intermediate | Single-tier → 3-tier → service-oriented → microservices, the end-to-end ML pipeline, and picking the simplest architecture that holds |
| 51 | `51_ai_assisted_software_development.ipynb` | ~2 h | Intermediate | The 2026 IDE landscape, Git & pull requests, prompt engineering for code, the four failure modes of AI-generated code, when *not* to trust the assistant |
| 52 | `52_bpm_governance_poc_mvp.ipynb` | ~2.5 h | Intermediate | Embedding AI in the BPM loop, RACI governance, POC → MVP → Production, three case studies, the EU AI Act risk map, the 10-question readiness checklist |

## Notebook guides

### 49 · Digital Transformation & AI-Induced Change — `49_digital_transformation.ipynb`

Module 16 opens with the broadest question: **why is AI suddenly everywhere, and what is it actually changing inside organisations?** The first thing it fixes is the unit of analysis — Meridian's leadership opens a strategy offsite asking *"how many support roles can AI replace?"*, and the notebook shows why the useful question is which **tasks within jobs** AI absorbs first. From there it builds the module's core mental model: don't ask *"which AI project should we fund?"* — ask *"which of our existing tasks should we redesign now that intelligence is a cheap utility?"*

Flagged 📍 **recommended early**: it is prerequisite-free, and the onboarding spiral suggests reading it near the start of the course to see *why* organisations automate, then returning to the rest of Module 16 later. Entirely conceptual — reading and reflection, no code cells.

**Learning objectives:**
- Explain why the current AI wave feels different from previous ones, in terms a non-technical stakeholder will follow
- Use the task-not-job framing to identify where AI can land first in a real business process
- Place an organisation on a five-stage AI-maturity model and propose the next concrete step
- Recognise the four most common adoption pitfalls and prevent them in a project you're advising on
- Distinguish substitution, augmentation, and reinvention as three different change strategies

**Sections:**
1. Why AI feels different *this* time
2. The unit of change — tasks, not jobs
3. The five-stage AI maturity model
4. Three change strategies — substitution, augmentation, reinvention
5. The four most common adoption pitfalls
6. 🧠 Mental model — the strategy map
7. The human side — what changes for the people in the room
8. 🧠 Mini-recap

**Frameworks covered:** the five-stage AI maturity model (Unaware → Experimenting → Operationalising → Industrialising → AI-native) · task-not-job framing · substitution / augmentation / reinvention change strategies · the four adoption pitfalls (technological solutionism, pilot purgatory, under-invested evaluation & monitoring, skipped change management — plus a bonus fifth on running ethics/governance in parallel) · the 2×2 strategy map (patterned vs one-off task × low vs high stakes).

**Practice:** 3 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a reasoning-based "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project: draft your own AI maturity assessment.

### 50 · Architecture Patterns for AI Applications — `50_architecture_patterns.ipynb`

Once you know *what* to automate (NB 49), the next question is *how to structure it*. This notebook walks four canonical architectures in order of growing complexity, plus the dedicated end-to-end ML pipeline pattern — each with the specific moment in an organisation's life when it's the right answer, and the specific failure mode when it's the wrong one. Meridian's lone engineer is at the whiteboard asking the notebook's driving question: *what's the simplest architecture that does the job — and how will I know when we've outgrown it?* The mental model: **architecture is the answer to a traffic question, not a fashion question** — user count, volume, and team size pick the pattern, never what sounds modern.

It isn't all prose: a 🔬 runnable, stdlib-only simulation demonstrates **failure isolation**, contrasting a monolith (one failing capability kills the whole request) with a service-oriented gateway that degrades gracefully behind per-service boundaries.

**Learning objectives:**
- Draw and label the five canonical architectures (single-tier, 3-tier, service-oriented, microservices, ML pipeline)
- Map a given AI requirement to the simplest architecture that meets it
- Recognise the smell that a project has outgrown its current architecture
- Avoid the two opposite mistakes: over-engineering (microservices for a 5-user pilot) and under-engineering (a 200-user system held together by one script + cron)
- Identify the ML-specific concerns (training data, model versioning, drift) that pure-software patterns don't address

**Sections:**
1. 🧠 Mental model — architecture as the answer to a *traffic* question
2. Pattern 1 — Single-tier (the script)
3. Pattern 2 — Three-tier (presentation / business logic / data)
4. Pattern 3 — Service-oriented (a few services, one team) — incl. 🔬 failure isolation, demonstrated
5. Pattern 4 — Microservices (one team per service)
6. The cross-cutting pattern — end-to-end ML / AI pipeline
7. The right size for *your* AI project — a decision table
8. How the course's notebooks map to these patterns

**Frameworks covered:** single-tier script · three-tier client-server · service-oriented · microservices · end-to-end ML/AI pipeline (cross-cutting) · the traffic-question heuristic and decision table, with the rule *"pick the architecture you'll have outgrown in 12 months, not the one you'll need in 36"* · failure isolation & graceful degradation.

**Practice:** 5 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. an architecture-review "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐, e.g. cost a microservices migration, review a real-ish ADR).

### 51 · AI-Assisted Software Development — `51_ai_assisted_software_development.ipynb`

In 2024–2026, *how* code gets written changed more than in the previous twenty years: a working professional now spends a significant fraction of the day directing an AI assistant rather than typing. This notebook is that workflow — the tools, the habits, and above all the **critical-review discipline** that separates *AI-assisted productivity* from *AI-assisted bug-introduction*. In the running example, Meridian's one engineer builds the 3-tier triage app from NB 50 with an assistant doing much of the typing. The mental model: the assistant is **a fast, confident junior who never says "I don't know"** — so (1) only delegate what you could review, and (2) review every diff before you trust it.

Flagged 📍 **do this early**: the Git + GitHub + Copilot workflow pays off across *every* notebook, and the onboarding recommends it right after the Python basics. Two 🔬 runnable demos show what a commit really is (a content-addressed snapshot, rebuilt with `hashlib` in ~10 lines) and how `git diff` is computed on demand with `difflib`.

**Learning objectives:**
- Pick an IDE and AI-assistant combination that matches your work style
- Use Git fluently for the operations 90% of working programmers do (commit / branch / pull request / merge conflict)
- Write prompts for code that consistently produce reviewable, runnable output — not vague drafts
- Critically review AI-generated code, naming the four most common failure modes
- Decide when *not* to use the AI assistant

**Sections:**
1. The modern IDE landscape (2026) — completion vs chat
2. Git basics — what 90% of professional work looks like (the 9 everyday commands, 🔬 commits-as-snapshots, pull requests)
3. Prompt engineering for code — what works in 2026 (five patterns)
4. Critical review of AI-generated artefacts — the four failure modes + the 60-second review checklist
5. When *not* to use the AI assistant
6. How this course is set up to teach this workflow

**Frameworks covered:** completion vs chat interaction modes (VS Code + Copilot, Cursor, PyCharm + JetBrains AI, Jupyter AI) · the 9-command Git core + pull-request workflow · five prompt patterns for code (give the AI what it can't see; ask for one thing; be specific about constraints; ask for tests; ask for alternatives) · the four failure modes (hallucinated APIs, plausible-but-wrong, architectural drift, silent over-confidence) · the 60-second review checklist · the "confident junior" delegation rule.

**Practice:** 5 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a review-style "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐, e.g. compare two assistants, write a team prompt-style guide) · 🎁 bonus mini-project: set up your AI-assisted workflow for *this* course.

### 52 · BPM Integration, Governance, POC → MVP → Production — `52_bpm_governance_poc_mvp.ipynb`

The closing notebook pulls the methodology together. You now know *what* to automate (NB 49), *how to structure it* (NB 50), and *how to build it efficiently* (NB 51) — what Meridian holds at this point is **working code that nobody uses yet**, and this is the last and longest stretch: turning it into a default tool the organisation trusts. The mental model: *POC, MVP, and Production are not three phases of one project — they are three different projects with three different questions* ("Can it work at all?" / "Will real users use it?" / "Can we run it for three years?"), and confusing them is the single most expensive mistake in AI project planning.

Three 📚 case studies make the pattern concrete: **Case 1 is Meridian's ticket-triage story told end-to-end from POC to production**; Case 2 is invoice processing in a 60-person finance department; Case 3 is "AI for sales analytics" — a project that *didn't* ship. A regulation section places the course's own systems on the **EU AI Act's** risk map — the tier follows the *use*, not the technology. A synthesis section distils everything into a 10-question readiness checklist, and a final section turns the whole module into a four-week, four-role team seminar (with an instructor grading rubric).

**Learning objectives:**
- Embed an AI feature at the right point in the BPM lifecycle (analyse → design → execute → monitor)
- Draft a RACI table for an AI initiative covering the human, AI, and platform roles
- Distinguish POC, MVP, and Production by their *purpose*, not their feature list — and avoid the most common confusion
- Walk through three case studies end-to-end, identifying where each project went well and where it struggled
- Place an AI system in the EU AI Act's risk tiers, and know which duties fall on a provider vs a deployer
- Produce a one-page project plan for a hypothetical AI initiative at your own organisation

**Sections:**
1. Embedding AI in the BPM lifecycle
2. Governance — drafting a RACI for an AI initiative
3. POC → MVP → Production — three projects, not three phases
4. Three case studies — what real AI initiatives look like
5. Regulation — the EU AI Act at working altitude
6. Synthesis — a one-page checklist for an AI initiative
7. Run it as a team — the seminar format

**Frameworks covered:** the BPM loop (analyse → design → execute → monitor) with three AI-integration patterns (AI in design / execute / monitor) · RACI matrices for AI initiatives · the POC → MVP → Production model · the 10-question readiness checklist ("a tool for the technical lead to say no constructively") · the four-role, four-week seminar format.

**Practice:** 5 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a post-mortem-reading "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐, e.g. design the production rollout, write a "this project should stop" memo) · 🎁 bonus mini-project: your own project plan.

## How these notebooks work

The earlier modules teach *technique*; this one teaches *judgement* — Modules 1–15 are the workshop, Module 16 is the seminar. The lessons are mostly prose, ASCII diagrams, decision tables, and case discussions: NB 49 and NB 52 contain no code at all, while NB 50 and NB 51 each embed a few small, deterministic, stdlib-only 🔬 demos (failure isolation; Git snapshots & diffs) that — like everything in the course — run 100% offline. The exercise rhythm is the standard one, adapted to the material: ✋ ~2-minute checkpoints with collapsible solutions after most sections, ⭐-rated 🧪 practice exercises where the "Debug me 🐞" items are flawed plans, architectures, and post-mortems to critique rather than broken code, 🧠 stretch exercises that produce written artefacts (stakeholder briefings, ADR reviews, rollout designs, stop memos), and 🎁 mini-projects in three of the four notebooks that leave you with a reusable maturity assessment, a personal AI-assisted workflow, and a project plan. Every notebook closes with 🧠 key takeaways and a ✅ self-assessment.

## Where next

→ **Module 8 — AI Engineering** (`../08_ai_engineering/27_llm_fundamentals.ipynb`) — the hands-on deep-dive companion to this module. After that, **Module 7 — Industry Applications** (`../07_industry_applications/`, NB 23–26) and **Module 10 — Agents, Tools & MCP** (`../10_agents_tools_mcp/`, NB 37–40) complete the course.

→ **Module 15 — Capstones** (`../15_capstones/47_capstone_analytics.ipynb` or `48_capstone_ai_assistant.ipynb`), if you haven't done them yet. The capstones make many of the Module 16 ideas concrete.

---

📝 **Finished this module?** Test yourself with the [Module 16 quiz](../quizzes/quiz_16_business_ai.ipynb) — five questions, ~10 minutes.
