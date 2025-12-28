---
description: Archive old registry entries and reports (run weekly or when registry > 50 entries)
allowed-tools: Bash, Read, Write, Edit
argument-hint: [days]
---

# Archive Registry

Move registry entries and reports older than N days to archive.

REPORTS_DIR=".claude/reports"
ARCHIVE_DIR="$REPORTS_DIR/archive"
REGISTRY="$REPORTS_DIR/_registry.md"

## Process

1. **Scan registry** for entries older than threshold (default: 7 days)
2. **Move entries** to `.claude/reports/archive/_registry-archive.md`
3. **Move reports** to `.claude/reports/archive/[category]/`
4. **Update status** of moved entries to "Archived"
5. **Report** what was archived

## Arguments

- `$ARGUMENTS`: Days threshold (default: 7)
  - `/archive` - Archive entries older than 7 days
  - `/archive 14` - Archive entries older than 14 days
  - `/archive 3` - Archive entries older than 3 days

## Archive Structure

```
.claude/reports/archive/
├── _registry-archive.md    # Archived registry entries
├── analysis/               # Old analysis reports
├── arch/                   # Old architecture reports
├── bugs/                   # Old bug reports
├── design/                 # Old design reports
├── impl/                   # Old implementation reports
├── review/                 # Old review reports
└── tests/                  # Old test reports
```

## Execution

Uses the archive script bundled with the agent-coordination skill:

```bash
# Script location (per Claude Code skill structure)
.claude/skills/agent-coordination/scripts/archive.sh [days]

# Examples
.claude/skills/agent-coordination/scripts/archive.sh      # Default: 7 days
.claude/skills/agent-coordination/scripts/archive.sh 14   # 14 days
```

## When to Run

- **Weekly:** As part of end-of-week cleanup
- **On demand:** When registry exceeds ~50 active entries
- **Before major work:** To ensure clean context

## Notes

- Archived reports remain accessible in archive folder
- Registry archive maintains full history
- Can be reversed by moving entries back
- Does NOT delete anything - only moves
