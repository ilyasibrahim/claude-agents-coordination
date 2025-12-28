---
description: Multi-level code review with peer, architecture, security, and reliability checks
---

# Full Review Protocol

Multi-level code review following enterprise engineering standards.

## Usage

```
/review-full [path]              # Full 4-level review
/review-full [path] --quick      # L1 only (peer review)
/review-full [path] --security   # L1 + L3 (peer + security)
```

## Review Levels

### Level 1: Peer Review (Always)

Invoke `code-quality` agent with mode=review:

```
Task(code-quality, "
Mode: review

Review target: [path]

Focus on:
- Code correctness and logic
- Style consistency
- Test coverage
- Error handling
- Documentation

Flag as:
- Blocking: Must fix before merge
- Non-blocking: Should fix
- Nit: Nice to have

Output: .claude/reports/review/L1-peer-[target]-YYYYMMDD.md
")
```

### Level 2: Architecture Review (If Applicable)

Trigger when:
- Change > 200 lines
- New API endpoints
- Database schema changes
- New services/modules
- Cross-cutting concerns

Invoke `architect` agent with mode=system:

```
Task(architect, "
Mode: system

Review target: [path]

Assess:
- Architectural alignment
- Pattern consistency
- Dependency appropriateness
- API design quality
- Scalability implications

Context from L1: [summary of peer review findings]

Output: .claude/reports/review/L2-arch-[target]-YYYYMMDD.md
")
```

### Level 3: Security Review (If Applicable)

Trigger when change touches:
- Authentication/authorization
- User input handling
- External API calls
- Database queries
- File operations
- Cryptographic operations
- Sensitive data (PII, credentials)

Invoke `security-engineer` agent with mode=scan:

```
Task(security-engineer, "
Mode: scan

Review target: [path]

Check for:
- OWASP Top 10 vulnerabilities
- Input validation gaps
- Auth/authz weaknesses
- Data exposure risks
- Dependency CVEs

Context from L1/L2: [summary of prior findings]

Output: .claude/reports/security/L3-security-[target]-YYYYMMDD.md
")
```

### Level 4: Reliability Review (If Applicable)

Trigger when change affects:
- Infrastructure configuration
- Service dependencies
- Error handling/retry logic
- Caching/performance
- Database operations
- External service calls

Invoke `sre` agent with mode=reliability-review:

```
Task(sre, "
Mode: reliability-review

Review target: [path]

Assess:
- Failure mode handling
- SLO impact
- Dependency reliability
- Graceful degradation
- Rollback safety

Context from L1/L2/L3: [summary of prior findings]

Output: .claude/reports/sre/L4-reliability-[target]-YYYYMMDD.md
")
```

## Aggregated Report

After all applicable levels complete, generate summary:

```markdown
# Full Review Summary: [target]

## Review Levels Completed
- [x] L1: Peer Review
- [x/NA] L2: Architecture Review
- [x/NA] L3: Security Review
- [x/NA] L4: Reliability Review

## Blocking Issues (Must Fix)
1. [L1] [Issue description] - [file:line]
2. [L3] [Security finding] - [file:line]

## Non-Blocking Issues (Should Fix)
1. [L1] [Issue description]
2. [L2] [Architectural concern]

## Recommendations
1. [Suggestion from reviews]

## Deferred to Tech Debt
_Non-blocking issues marked "won't fix now" → add to .claude/reports/_tech-debt.md_

## Verdict
- [ ] Ready to merge (all blocking resolved)
- [ ] Needs revision (blocking issues remain)

## Individual Reports
- L1: .claude/reports/review/L1-peer-[target]-YYYYMMDD.md
- L2: .claude/reports/review/L2-arch-[target]-YYYYMMDD.md
- L3: .claude/reports/security/L3-security-[target]-YYYYMMDD.md
- L4: .claude/reports/sre/L4-reliability-[target]-YYYYMMDD.md
```

Output: `.claude/reports/review/full-review-[target]-YYYYMMDD.md`

## Decision Flow

```
Start
  │
  ▼
L1 Peer Review ────────────────────────────┐
  │                                         │
  ▼                                         │
Change > 200 lines OR new API/schema?       │
  │                                         │
  ├─ Yes ─► L2 Architecture Review ────────┤
  │                                         │
  ▼                                         │
Touches auth/input/data/crypto?             │
  │                                         │
  ├─ Yes ─► L3 Security Review ────────────┤
  │                                         │
  ▼                                         │
Affects infra/deps/error handling?          │
  │                                         │
  ├─ Yes ─► L4 Reliability Review ─────────┤
  │                                         │
  ▼                                         │
Aggregate Results ◄────────────────────────┘
  │
  ▼
Generate Summary Report
```

## Quick Variants

### /review-full [path] --quick
Only L1 peer review. Use for small, isolated changes.

### /review-full [path] --security
L1 + L3 only. Use when security is primary concern.

### /review-full [path] --all
Force all 4 levels regardless of triggers.
