# Release v2.3.0: Model Tiering and Colour Scheme Rationalisation

**Released**: April 20, 2026

## Overview

Minor release introducing capability-based model tiering across all 15 agents and a fully rationalised colour scheme using only valid Claude Code colours grouped into semantic clusters.

---

## What's New

### Model Tiering

All agents have been assigned a model matched to their workload, balancing quality against token cost:

| Model | Agents | Rationale |
|-------|--------|-----------|
| `opus` | `architect`, `rfc`, `security-engineer`, `sre` | Deep reasoning required: system trade-off analysis, adversarial threat modelling, postmortem root-cause, RFC decision-making |
| `haiku` | `test-engineer` | Mechanical execution: run tests, parse output, classify pass/fail — no deep reasoning needed |
| `sonnet` | All others (10 agents) | Balanced implementation and judgment work |

**Why this matters**: High-frequency agents like `test-engineer` run on every CI cycle. Dropping to `haiku` cuts token cost significantly without any quality loss on deterministic tasks. Conversely, `opus` on `architect` and `security-engineer` means the most consequential decisions get the most capable model.

---

### Colour Scheme Rationalisation

The previous scheme used `white` and `magenta` which are not part of the Claude Code supported colour palette (`red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`). All colours are now valid and organised into semantic clusters:

| Colour | Cluster | Agents |
|--------|---------|--------|
| `red` | Risk / incidents | `security-engineer`, `sre` |
| `orange` | Review / verify | `code-quality`, `test-engineer` |
| `pink` | Planning / docs | `architect`, `rfc`, `docs` |
| `green` | Build / ship | `backend`, `devops` |
| `cyan` | Data | `data-engineer`, `data-viz-specialist` |
| `blue` | UI / UX | `frontend`, `ux-designer` |
| `purple` | ML / AI | `ml-engineer`, `lrl-nlp-expert` |

**Design rationale**:
- `red` is reserved for agents that surface risk — security threats and reliability incidents
- `orange` signals caution/review — agents that inspect rather than build
- `pink` is the closest neutral available for meta/cross-cutting agents that design, document, and govern
- `green` maps to running systems — backend APIs and infrastructure shipping
- `cyan` is a conventional data colour across most dashboards and terminals
- `blue` is the standard UI/interactive colour
- `purple` is widely used in ML branding (W&B, Hugging Face, Cohere) — accurate for the AI cluster

---

## Files Changed

**Agent definitions** (`claude-user/agents/`):

| File | Changes |
|------|---------|
| `architect.md` | model: sonnet → opus, color: white → pink |
| `code-quality.md` | color: blue → orange |
| `data-viz-specialist.md` | color: yellow → cyan |
| `devops.md` | color: magenta → green |
| `docs.md` | color: white → pink |
| `frontend.md` | color: cyan → blue |
| `lrl-nlp-expert.md` | color: blue → purple |
| `ml-engineer.md` | color: magenta → purple |
| `rfc.md` | model: (none) → opus, color: white → pink |
| `security-engineer.md` | model: (none) → opus |
| `sre.md` | model: (none) → opus, color: yellow → red |
| `test-engineer.md` | model: sonnet → haiku, color: green → orange |
| `ux-designer.md` | color: magenta → blue |

---

## Migration from v2.2.1

No action required beyond pulling the updated agent files. Colour and model changes take effect immediately on next agent invocation.

---

## Documentation

**In-repository**:
- `README.md` — Architecture overview
- `claude-user/INDEX.md` — User-level setup
- `RELEASE_NOTES_v2.3.0.md` — This document
- `CHANGELOG.md` — Full version history

**Articles** (Medium):
- Part 1: [Context Amnesia Solution](https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825)
- Part 2: [The 4-Step Protocol](https://medium.com/@ilyas.ibrahim/the-4-step-protocol-that-fixes-claude-codes-context-amnesia-c3937385561c)
- Part 3: *Scaling to Enterprise-Grade Delegation* (Coming Soon)

---

## License

This is free and unencumbered software released into the public domain (Unlicense).

---

**Questions?** Open an issue or reach out via [Medium](https://medium.com/@ilyas.ibrahim).
