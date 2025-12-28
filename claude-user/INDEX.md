# User-Level Claude Code Configuration (`~/.claude/`)

This folder is meant to be copied into your user-level Claude Code config directory (`~/.claude/`).

It defines the shared contract across all projects:
- The coordination protocol (main agent only)
- Standard agents and slash commands
- Report taxonomy + verification scripts (used by projects)

---

## Directory Structure

```
claude-user/
├── agents/     # Tiered agent set (orchestrators + specialists)
├── commands/   # Standard workflows (/review-full, /ci, /debt, /rfc, ...)
└── skills/     # Auto-invoked knowledge + coordination protocol
```

---

## Agents (Tiered)

### Tier 1 — Workflow Orchestrators
- `code-quality` — Multi-level review + debugging/QA escalation.
- `test-engineer` — Runs tests, triages failures, detects flakes.
- `architect` — System design, ADRs, architecture reviews.
- `ml-engineer` — End-to-end ML workflows (train/eval/deploy).

### Tier 2 — Specialized Execution
- `security-engineer` — Threat modeling, scans, auth/input handling review.
- `sre` — Reliability reviews, SLOs, postmortems, capacity.
- `rfc` — RFC authoring + decision capture.
- `data-engineer` — Data pipelines, validation, ETL patterns.
- `frontend` / `backend` — Implementation work.
- `devops` — CI/CD, infra, git workflows, release hygiene.
- `docs` — Documentation and handoffs.

### Tier 3 — On-Demand Specialists
- `lrl-nlp-expert` — Low-resource NLP techniques.
- `data-viz-specialist` — Data storytelling and dashboards.
- `ux-designer` — UX/design review and writing.

---

## Skills

- `agent-coordination/` — Coordination protocol, report taxonomy, verification + archive scripts.
- `design/` — UX/design heuristics and review patterns.
- `ux-writing/` — Voice & tone + microcopy standards.

---

## Common Commands

- `/review-full [path]` — L1→L2→L3→L4 review chain (peer → arch → security → reliability).
- `/ci` — Local CI: lint → type-check → build → test → security scan.
- `/debt` — Tech-debt registry management (add/resolve/list).
- `/postmortem [incident]` — Incident learning + follow-ups (logs debt when needed).
- `/rfc [topic]` — Design document workflow.

---

## Install

```bash
mkdir -p ~/.claude
rsync -a claude-user/ ~/.claude/
```

