# Claude Code Agents Coordination

Tiered multi-agent coordination + delegation patterns for Claude Code, with **institutional memory** (`_registry.md`) and **explicit tech-debt tracking** (`_tech-debt.md`).

This repo ships two reusable layers:

- `claude-user/` → user-level config (copy into `~/.claude/`)
- `claude-project/` → project-level `.claude/` template (copy into each project)

---

## Core Model

- **4-step workflow:** Registry → Context injection → Sequencing → Verification
- **Two registries:**
  - `.claude/reports/_registry.md` tracks what was done (reports)
  - `.claude/reports/_tech-debt.md` tracks what was deferred (debt items with sources)
- **Multi-level review chain:** `/review-full` can escalate peer → architecture → security → reliability based on change characteristics.

---

## Quick Start

### 1) Install user-level config

```bash
mkdir -p ~/.claude
rsync -a claude-user/ ~/.claude/
```

### 2) Install project-level config (per project)

```bash
mkdir -p /path/to/your-project/.claude
rsync -a claude-project/ /path/to/your-project/.claude/
```

Then edit `/path/to/your-project/.claude/CLAUDE.md` with project context (domain, conventions, key paths, skills).

---

## What’s Inside

- `claude-user/INDEX.md` — tiered agent set + standard workflows
- `claude-project/INDEX.md` — project template layout + setup steps

---

## Repo Layout

```
claude-agents-coordination/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── claude-user/
│   ├── INDEX.md
│   ├── agents/
│   ├── commands/
│   └── skills/
└── claude-project/
    ├── CLAUDE.md
    ├── INDEX.md
    ├── commands/
    ├── skills/
    └── reports/
        ├── _registry.md
        ├── _tech-debt.md
        └── [categories]/
```

---

## Releases (Stable Links)

- `v1.0.0` — legacy “flat” system referenced by earlier articles (Parts 1–2)
- `v2.0.0` — tiered delegation system described in Part 3

---

## Articles

- Part 1: https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825
- Part 2: https://medium.com/@ilyas.ibrahim/the-4-step-protocol-that-fixes-claude-codes-context-amnesia-c3937385561c
