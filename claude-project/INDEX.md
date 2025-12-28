# Project-Level Claude Code Configuration (`<project>/.claude/`)

This folder is meant to be copied into a specific project as its `.claude/` directory.

It contains:
- `CLAUDE.md` project context (what the project is, key conventions, skills)
- Project-specific commands and skills
- The project’s registries and report output folders

---

## Directory Structure

```
claude-project/
├── CLAUDE.md
├── commands/         # Project workflows (e.g. /ml/run, /data/analyze)
├── skills/           # Project domain knowledge (invoked by context)
└── reports/
    ├── _registry.md      # What was done (work history)
    ├── _tech-debt.md     # What was deferred (explicit debt tracking)
    ├── analysis/
    ├── arch/
    ├── bugs/
    ├── commits/
    ├── design/
    ├── exec/
    ├── handoff/
    ├── implementation/
    ├── review/
    ├── security/
    ├── sre/
    ├── rfc/
    ├── ci/
    ├── tests/
    └── archive/
```

---

## Install Into a Project

From the repo root:

```bash
mkdir -p /path/to/your-project/.claude
rsync -a claude-project/ /path/to/your-project/.claude/
```

Then edit `/path/to/your-project/.claude/CLAUDE.md` with your project context.

