---
description: QA review with code-quality + test-engineer agents
allowed-tools: Bash(pytest:*, npm:test*, git:*)
argument-hint: [scope]
---

# Quality Assurance Review

## Process

1. **Scope:** Determine review scope (full, PR, feature, security, performance)
2. **Execute:** code-quality (mode: review) + test-engineer
3. **Report:** QA report in `.claude/reports/tests/`

## Arguments

- `full` - Complete codebase QA
- `pr [number]` - Pull request review
- `feature [name]` - Specific feature
- `security` - Security-focused
- `performance` - Performance-focused

## Checklist

**Testing:** Unit ✓ Integration ✓ E2E ✓ Coverage ≥80%
**Quality:** No code smells, conventions followed, clear naming
**Security:** OWASP top 10 checked, auth correct
**Performance:** No N+1, proper caching
**Accessibility:** WCAG AA (for UI)
