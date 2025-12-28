---
description: Code review with code-quality agent (mode: review)
allowed-tools: Bash(git:*)
argument-hint: [path]
---

# Code Review

## Process

1. **Scope:** Path provided → specific file/dir | None → recent changes (`git diff`)
2. **Launch:** code-quality agent with mode: review
3. **Output:** Review report in `.claude/reports/review/`

## Arguments

- `$ARGUMENTS`: Optional path (file or directory)
- If omitted: review uncommitted changes

## Examples

```bash
/review                    # Recent changes
/review src/models/        # Specific directory
/review src/api/routes.py  # Specific file
```
