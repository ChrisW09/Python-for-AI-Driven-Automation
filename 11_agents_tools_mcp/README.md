# Module 11 — Agents, Tools & MCP

**Goal:** Go from "an LLM that calls a tool" (Module 5, NB 19) to production-grade **agentic systems** — reliable agent loops, hardened tools, the **Model Context Protocol (MCP)**, and multi-agent orchestration. By the end you can design, build, and evaluate an agent that discovers its tools over a standard protocol and works in Claude Desktop, Claude Code, or your own app.

**Estimated time:** 6–8 hours.
**Prerequisites:** Module 5 (AI Engineering — especially NB 19 tools & agents), Modules 1–2 (functions, dicts, JSON). A real LLM is **not** required — every notebook runs 100% offline.

```
                        ┌──────────────────────────────────────┐
                        │   the agent control loop (NB 19)     │
                        └──────────────────┬───────────────────┘
                                           │
        ┌──────────────────┬───────────────┴───────┬──────────────────────┐
        ▼                  ▼                       ▼                      ▼
     NB 39              NB 40                   NB 41                  NB 42
   agent              robust tools          Model Context         multi-agent
   architectures      (schemas, valid-      Protocol (MCP):       systems +
   (ReAct, planning,  ation, approval,      host/client/server,   orchestrator,
   reflection,        parallel, idem-       JSON-RPC, tools/       routing, the
   memory)            potency)              resources/prompts     MCP capstone
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 39 | `39_agent_architectures.ipynb` | A ReAct agent with planning, reflection & memory — plus the failure-mode guardrails |
| 40 | `40_designing_robust_tools.ipynb` | A `ToolRegistry` with JSON-Schema validation, structured errors, an approval gate & parallel calls |
| 41 | `41_model_context_protocol.ipynb` | A working MCP server **and** client from scratch (JSON-RPC 2.0; tools, resources, prompts) |
| 42 | `42_multi_agent_systems.ipynb` | An orchestrator + specialist agents, evaluated end-to-end — the MCP-backed support copilot capstone |

## What makes this module different

- **Offline-first, real-ready.** Every agent "brain", tool call, and MCP message runs with zero install via deterministic stand-ins; the real `mcp` SDK, the `anthropic`/`openai` providers, and a Claude host config are shown as drop-in references.
- **Protocol from scratch.** NB 41 implements the *real* MCP method names and JSON-RPC message shapes, so the official SDK holds no surprises.
- **Ends in a capstone.** NB 42 combines agents + tools + MCP into one support-operations assistant you can grow into a portfolio project.

## Next step

Turn the capstone into a real **FastMCP** server (NB 41 §9) and register it with **Claude Desktop** (`claude_desktop_config.json`) or **Claude Code** (`claude mcp add`).
