---
description: Create git commit with Conventional Commits format
allowed-tools: Bash(git:*)
argument-hint: [optional message]
---

# Create Git Commit

## Process

1. **Review:** `git status` + `git diff HEAD`
2. **Analyze:** Determine type (feat|fix|chore|docs|style|refactor|test|perf)
3. **Draft:** `type(scope): message` - focus on WHY, not WHAT
4. **Stage:** `git add <files>` (skip .env, credentials)
5. **Commit:** Use single-line when possible
6. **Verify:** `git status` + `git log -1`

## Commit Format

```bash
# Single-line (preferred)
git commit -m "type(scope): concise message"

# With body (only if essential)
git commit -m "$(cat <<'EOF'
type(scope): concise message
  - One concise reason or benefit.
  - Closes #123.
EOF
)"
```

## Types

| Type | Use For |
|------|---------|
| feat | New feature |
| fix | Bug fix |
| chore | Maintenance, deps |
| docs | Documentation |
| style | Formatting |
| refactor | Code restructuring |
| test | Tests |
| perf | Performance |

## Rules

- Most commits: single-line, no body
- Body if essential: max 2-3 bullets, one line each
- NO verbose explanations
- NO implementation details
- Focus on WHY and business impact
