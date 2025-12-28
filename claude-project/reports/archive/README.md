# Archive Directory

This directory contains archived reports that have been moved from the active registry to reduce clutter and maintain clean context for active development.

## Structure

```
archive/
├── README.md                          # This file
├── _registry-archive-YYYYMMDD.md      # Dated archive registries (snapshots)
├── analysis/                          # Archived analysis reports
├── arch/                              # Archived architecture reports
├── bugs/                              # Archived bug reports
├── design/                            # Archived design reports
├── exec/                              # Archived execution reports
├── handoff/                           # Archived handoff reports
├── implementation/                    # Archived implementation reports
├── review/                            # Archived review reports
├── security/                          # Archived security reports
└── tests/                             # Archived test reports
```

## Archive Registries

Each time the archive script runs, it creates a dated registry snapshot:

| Registry | Archive Date | Threshold | Reports Archived |
|----------|--------------|-----------|------------------|
| [_registry-archive-20251216.md](_registry-archive-20251216.md) | 2025-12-16 | 7 days | Example |

## Archive Process

Reports are archived when they are:
- Older than the threshold (default: 7 days)
- Status: Complete, Resolved, Fixed, or Archived
- No longer needed for active development context

## Finding Archived Reports

1. **By Date:** Check the dated registry files (`_registry-archive-YYYYMMDD.md`)
2. **By Category:** Browse category subdirectories (e.g., `bugs/`, `implementation/`)
3. **By Name:** Use grep to search across all registries

```bash
# Find when a specific report was archived
grep -r "report-name" _registry-archive-*.md

# List all archive registries
ls -lh _registry-archive-*.md

# View specific archive
cat _registry-archive-20251216.md
```

## Archiving Reports

To archive old reports:

```bash
# Archive reports older than 7 days (default)
python ~/.claude/skills/agent-coordination/scripts/archive_reports.py

# Archive reports older than 14 days
python ~/.claude/skills/agent-coordination/scripts/archive_reports.py 14

# Preview what would be archived (dry run)
python ~/.claude/skills/agent-coordination/scripts/archive_reports.py 7 --dry-run
```

## Notes

- **Dated Registries:** Each archive run creates a new dated registry file (e.g., `_registry-archive-20251216.md`)
- **No Appending:** Archive registries are never appended to - each is a snapshot in time
- **Preservation:** All archived reports remain accessible in category subdirectories
- **No Deletion:** Archive process only moves files, never deletes them
- **Reversible:** Reports can be moved back to active registry if needed

---

**Last Updated:** 2025-12-28 (v2.1.0 - Dated Archive Registries)
