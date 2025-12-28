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

1. **Parse active registry** for entries older than threshold (default: 7 days)
2. **Move report files** to `.claude/reports/archive/[category]/`
3. **Create dated archive registry** `.claude/reports/archive/_registry-archive-YYYYMMDD.md`
4. **Update active registry** (remove archived entries)
5. **Set status** of archived entries to "Archived" in dated registry
6. **Report summary** with archive date and file count

## Arguments

- `$ARGUMENTS`: Days threshold (default: 7)
  - `/archive` - Archive entries older than 7 days
  - `/archive 14` - Archive entries older than 14 days
  - `/archive 3` - Archive entries older than 3 days

## Archive Structure

```
.claude/reports/archive/
├── _registry-archive-YYYYMMDD.md  # Dated archive registries (snapshots)
├── README.md                      # Archive index and documentation
├── analysis/                      # Old analysis reports
├── arch/                          # Old architecture reports
├── bugs/                          # Old bug reports
├── design/                        # Old design reports
├── implementation/                # Old implementation reports
├── exec/                          # Old execution reports
├── handoff/                       # Old handoff reports
├── review/                        # Old review reports
├── security/                      # Old security reports
└── tests/                         # Old test reports
```

## Execution

Uses the Python archive script bundled with the agent-coordination skill:

```bash
# Script location (per Claude Code skill structure)
python .claude/skills/agent-coordination/scripts/archive_reports.py [days]

# Examples
python .claude/skills/agent-coordination/scripts/archive_reports.py     # Default: 7 days
python .claude/skills/agent-coordination/scripts/archive_reports.py 14  # 14 days
python .claude/skills/agent-coordination/scripts/archive_reports.py 7 --dry-run  # Preview only
```

## When to Run

- **Weekly:** As part of end-of-week cleanup
- **On demand:** When registry exceeds ~50 active entries
- **Before major work:** To ensure clean context

## Notes

- **Dated snapshots:** Each archive run creates a new `_registry-archive-YYYYMMDD.md`
- **No appending:** Archive registries are never appended to - each is a snapshot in time
- **Full automation:** Updates both active and archive registries automatically
- **Archived reports** remain accessible in archive folder by category
- **Reversible:** Can be reversed by moving entries back
- **No deletion:** Does NOT delete anything - only moves
- **Archive history:** Track all past archives via dated registry files
