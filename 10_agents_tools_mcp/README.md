# Module 10 — Agents, Tools & MCP

> 🧭  [◀ Building AI POCs](../09_building_ai_pocs/)  ·  [🏠 Course home](../README.md)  ·  [NLP ▶](../11_nlp/)

**Goal:** Go from "an LLM that calls a tool" (Module 8, NB 30) to production-grade **agentic systems** — reliable agent loops, hardened tools, the **Model Context Protocol (MCP)**, and multi-agent orchestration. By the end you can design, build, and evaluate an agent that discovers its tools over a standard protocol and works in Claude Desktop, Claude Code, or your own app.

**Estimated time:** 6–8 hours.

**Prerequisites:** Module 8 (AI Engineering — especially NB 30 tools & agents), Modules 1–2 (functions, dicts, JSON). A real LLM is **not** required — every notebook runs 100% offline.

```
                        ┌──────────────────────────────────────┐
                        │   the agent control loop (NB 30)     │
                        └──────────────────┬───────────────────┘
                                           │
        ┌──────────────────┬───────────────┴───────┬──────────────────────┐
        ▼                  ▼                       ▼                      ▼
     NB 37              NB 38                   NB 39                  NB 40
   agent              robust tools          Model Context         multi-agent
   architectures      (schemas, valid-      Protocol (MCP):       systems +
   (ReAct, planning,  ation, approval,      host/client/server,   orchestrator,
   reflection,        parallel, idem-       JSON-RPC, tools/      routing, the
   memory)            potency)              resources/prompts     MCP capstone
```

One running example carries the whole module: an **AI support copilot** for a SaaS team. NB 37 gives it a brain (a bounded agent loop), NB 38 hardens its tools, NB 39 serves those tools over MCP, and NB 40 grows it into an orchestrated team of specialists — the module's finished artifact.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 31 | `37_agent_architectures.ipynb` | 70–90 min | Intermediate → Advanced | A ReAct agent with planning, reflection & memory — plus the failure-mode guardrails |
| 32 | `38_designing_robust_tools.ipynb` | 70–90 min | Intermediate → Advanced | A `ToolRegistry` with JSON-Schema validation, structured errors, an approval gate & parallel calls |
| 33 | `39_model_context_protocol.ipynb` | 80–100 min | Advanced | A working MCP server **and** client from scratch (JSON-RPC 2.0; tools, resources, prompts) |
| 34 | `40_multi_agent_systems.ipynb` | 80–100 min | Advanced | An orchestrator + specialist agents, evaluated end-to-end — the MCP-backed support copilot capstone |

## Notebook guides

### 31 · Agent Architectures: Loops, Planning & Reflection — `37_agent_architectures.ipynb`

Notebook 30 introduced the **call → execute → return** loop; this lesson goes professional. The mental model for the whole module: *an agent is an LLM sitting inside a `while`-loop with a memory and a budget* — the clever model isn't the architecture, the loop around it is. You build the support copilot's brain against a tiny in-memory world (channel-level CSAT scores plus a calculator) and a deterministic `policy()` stand-in that makes the same kind of decisions a real model would, so every run is reproducible.

Concretely you implement four escalating architectures — `react_agent()` (Thought → Action → Observation), `plan_and_execute()` (decompose first, act second), `reflexive_agent()` (a critic that triggers a retry), and `agent_with_memory()` (scratchpad + episodic cache) — then map each common failure mode (loops, hallucinated tools, runaway cost) to its guardrail. Section 9 sketches the one-line swap to a real Anthropic provider.

**Learning objectives:**
- Explain the **agent control loop** and why every agent needs a *budget*.
- Implement the **ReAct** pattern: interleaved Thought → Action → Observation.
- Add a **planner** that decomposes a task before acting.
- Add a **reflection** step that critiques an answer and retries on failure.
- Give an agent **memory** (scratchpad + episodic) and know when each matters.
- Name the common **failure modes** (loops, hallucinated tools, runaway cost) and the guardrail for each.

**Sections:**
1. The agent control loop in one picture
2. Setup — a tiny world the agent can act in
3. The "brain": a deterministic policy stand-in
4. ReAct: interleave Thought → Action → Observation
5. Planning: decompose *before* acting
6. Reflection: critique, then retry
7. Memory: scratchpad vs episodic
8. Failure modes & the guardrail for each
9. Going live — the real-provider sketch

**Practice:** 4 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project: a self-describing agent

**Files/datasets:** none — all data is in-memory; the "brain" is an offline deterministic stand-in, no API key needed (real `anthropic` client shown as a commented reference).

### 32 · Designing Robust Tools — `38_designing_robust_tools.ipynb`

An agent is only as good as its tools. The copilot gains one consequential new tool — `estimate_refund(order_id, pct)`, a tool that **moves money** — and it becomes the stress test for the whole lesson: what happens when the model sends `pct: "fifty"`, forgets `order_id`, or asks for `pct: 9999`? Mental model: *the schema is the contract you advertise; the validator is the bouncer at the door* — every argument the model sends is untrusted input.

You build the full defensive stack: a `Tool` dataclass (name, description, JSON-Schema parameters, function), a dependency-free `validate_args()` covering missing fields / wrong types / enums / ranges, a consistent `ok()`/`err()` result envelope via `safe_call()`, and a `ToolRegistry` that validates, dispatches, and logs every call. On top come tool selection among many, a human-in-the-loop approval gate (`gated_call()` with pluggable approvers), parallel calls (`call_many()`), and output bounding. The patterns map 1:1 onto OpenAI/Anthropic function-calling and onto MCP tools (NB 39).

**Learning objectives:**
- Describe a tool with a **JSON-Schema** the model can read.
- **Validate** arguments before executing — types, required fields, enums, ranges.
- Return **structured results and errors** (never raw exceptions) in a consistent envelope.
- Build a **ToolRegistry** that validates, dispatches, and logs every call.
- Add a **human-in-the-loop approval gate** for sensitive tools.
- Run independent tools **in parallel** and bound output size.

**Sections:**
1. Anatomy of a tool
2. Validate arguments *before* running
3. A consistent result envelope
4. A ToolRegistry: validate, dispatch, log
5. Tool selection among many
6. Approval gate: human-in-the-loop for dangerous tools
7. Parallel tool calls
8. Bound the output

**Practice:** 4 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐: idempotency keys, retry with backoff, timeouts, schema-driven coercion) · 🎁 bonus mini-project: a hardened tool call

**Files/datasets:** none — everything runs offline on in-memory data, no API key needed.

### 33 · The Model Context Protocol (MCP) — `39_model_context_protocol.ipynb`

Every framework wires tools *differently* — an OpenAI tool, a LangChain tool, and a Claude tool are described in three incompatible ways. **MCP**, open-sourced by Anthropic in late 2024, is the single open standard that fixes this: write one MCP **server** and it works in Claude Desktop, Claude Code, and any other MCP host. Mental model: *MCP is a USB-C port for AI* — it turns M×N bespoke glue into M+N standard plugs, and the plug is just two messages: "what can you do?" (discover) and "do this now" (invoke).

This notebook builds a **working MCP server and client from scratch, in process**, speaking the real protocol — JSON-RPC 2.0, the real method names (`initialize` → `tools/list` → `tools/call` → …) and message shapes — so the official SDK holds no surprises. You populate a **"support-ops" server** (`get_csat`, `count_tickets`, a tickets resource, a triage prompt), connect `MCPClient` over an `InProcessTransport`, and finish with `mcp_agent()`: an agent that discovers and calls tools it never hard-coded. Section 9 maps everything onto the real `mcp` SDK (FastMCP) and the Claude Desktop / Claude Code host config.

**Learning objectives:**
- Explain MCP's **host / client / server** architecture and when to use it.
- Name the three server **primitives** — **tools**, **resources**, **prompts** — and who controls each.
- Trace the **JSON-RPC** lifecycle: `initialize` → `tools/list` → `tools/call` → …
- Implement a minimal MCP **server** and **client** and exchange messages over a transport.
- Connect an **agent** to a server so it discovers and calls tools it never hard-coded.
- Map the offline build onto the real **`mcp` SDK** and a **Claude Desktop / Claude Code** config.

**Sections:**
1. Why MCP exists
2. The three primitives — and who controls them
3. The wire protocol: JSON-RPC 2.0
4. A minimal MCP server
5. Populate a server: the "support-ops" server
6. The transport + client
7. The full lifecycle — discover, then use
8. Connect an agent to the MCP server
9. The real thing — `mcp` SDK & Claude hosts

**Practice:** 4 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐: unknown-method errors, a logging transport, a two-server router, resource templates) · 🎁 bonus mini-project: a capability report

**Files/datasets:** none — server data (tickets, CSAT) lives in-memory and the protocol runs in process, no API key needed; the real `mcp` SDK (`pip install "mcp[cli]"`) and host configs appear as commented references.

### 34 · Multi-Agent Systems & Capstone — `40_multi_agent_systems.ipynb`

Some tasks have distinct sub-jobs — analyse, then draft, then check — that are cleaner and more testable when handled by **specialist agents** under an **orchestrator**. Mental model: *a multi-agent system is a team* — the orchestrator is the team lead, the "wiring" is just messages (text or dicts) passed between LLM calls, and you hire a new specialist only when the role is genuinely different. The lesson is honest about cost: it opens with a decision table for when one agent is enough.

The copilot becomes that team: a `Specialist` **analyst** that pulls the numbers, a **writer** that phrases them for a customer, and a **human** to escalate to via `run_with_handoff()`, coordinated by an `Orchestrator` that shares state on a **blackboard**. Section 6 is the module capstone — the analyst calls its tools through a `MiniMCPServer`/`MiniMCPClient` pair, combining NB 37's loop, NB 38's tool discipline, and NB 39's protocol — and Section 7 evaluates the whole system against golden cases. The bonus project ships it all as one `support_assistant(request)` function: the module's finished artifact.

**Learning objectives:**
- Decide **when multiple agents help — and when they're overkill**.
- Build the **orchestrator–worker** pattern with specialist agents.
- Implement **routing** and **handoff** between agents.
- Share state safely via a **blackboard**.
- **Evaluate** a multi-agent system end-to-end.
- Assemble a **capstone**: orchestrator + specialists + tools + an MCP server.

**Sections:**
1. When to use more than one agent
2. A specialist agent
3. A second specialist — the writer
4. The orchestrator
5. Routing & handoff
6. Capstone — an MCP-backed support-operations assistant
7. Evaluating a multi-agent system
8. Going live — the real multi-agent sketch

**Practice:** 4 ✋ quick exercises · 4 🧪 practice exercises (⭐–⭐⭐, incl. a Debug me 🐞) · 4 🧠 stretch exercises (⭐⭐⭐: parallel specialists, budgets, capability-based routing, a blackboard log) · 🎁 bonus mini-project: the full assistant as one function

**Files/datasets:** none — all data is in-memory; specialists use offline deterministic stand-ins, no API key needed (a real-provider sketch closes the notebook).

## How these notebooks work

Every notebook runs **100% offline** — the agent "brain", every tool call, and every MCP message use deterministic stand-ins, so no API key or install is needed, and each lesson marks exactly where a real provider (`anthropic`, `openai`, the `mcp` SDK) drops in. Each notebook opens with a Colab badge and a metadata line (estimated time & difficulty), then follows the course rhythm: short sections punctuated by ✋ **Quick exercise (~2 min)** checkpoints with collapsible solutions, followed by 🧪 practice exercises (⭐-rated, always including a "Debug me 🐞"), 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways, and a self-assessment. The module builds directly on Modules 8–9 — especially NB 30's tool-calling loop — and all four lessons develop the same AI support copilot, so each pattern lands on one concrete system.

## Where next

Turn the capstone into a real **FastMCP** server (NB 39 §9) and register it with **Claude Desktop** (`claude_desktop_config.json`) or **Claude Code** (`claude mcp add`). Then carry on to [Module 11 — NLP](../11_nlp/).

---

📝 **Finished this module?** Test yourself with the [Module 10 quiz](../quizzes/quiz_10_agents_tools_mcp.ipynb) — five questions, ~10 minutes.
