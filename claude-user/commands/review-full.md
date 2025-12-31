---
description: Multi-level code review with peer, architecture, security, and reliability checks.
argument-hint: <path> [--quick|--security|--all]
allowed-tools: Read, Glob, Grep, Bash
---

# Full Review Protocol

Multi-level code review following enterprise engineering standards.

**Before proceeding:** Read the `agent-coordination` skill at `.claude/skills/agent-coordination/SKILL.md` for registry management, verification scripts, and coordination protocols.

## Review Target

**Path to review:** $1  
**Options:** $ARGUMENTS

## Quick Reference

- `/review-full src/` — Full 4-level review
- `/review-full src/ --quick` — L1 only (peer review)
- `/review-full src/ --security` — L1 + L3 (peer + security)
- `/review-full src/ --all` — Force all 4 levels

---

## Pre-Review Analysis

Before starting, analyze the target to determine which review levels apply:

<analysis>
!find $1 -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" -o -name "*.rs" \) 2>/dev/null | head -20 | xargs wc -l 2>/dev/null | tail -1 || echo "0 total"
!git diff --stat HEAD~1 -- $1 2>/dev/null | tail -1 || echo "No git history"
</analysis>

<prior_work>
!cat .claude/reports/_registry.md 2>/dev/null | grep -i "review\|security\|arch\|sre" | head -10 || echo "No prior reviews found"
</prior_work>

---

## Review Levels

### Level 1: Peer Review (Always Required)

Invoke the `code-quality` agent with mode=review:

```
Task(code-quality, "
Mode: review
Target: $1

Focus areas:
- Code correctness and logic errors
- Style consistency with project conventions
- Test coverage gaps
- Error handling completeness
- Documentation quality

Severity classification:
- BLOCKING: Must fix before merge
- NON-BLOCKING: Should fix, can defer
- NIT: Nice to have improvements

Output: .claude/reports/review/L1-peer-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L1 report entry.

---

### Level 2: Architecture Review

**Trigger when ANY of these apply:**
- Change exceeds 200 lines
- New API endpoints added
- Database schema modifications
- New services or modules introduced
- Cross-cutting concerns affected

Invoke the `architect` agent with mode=system:

```
Task(architect, "
Mode: system
Target: $1

Context from L1: [Include key findings from peer review]

Assessment criteria:
- Alignment with existing architecture
- Pattern consistency across codebase
- Dependency appropriateness and direction
- API design quality and versioning
- Scalability implications

Output: .claude/reports/review/L2-arch-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L2 report entry.

---

### Level 3: Security Review

**Trigger when change touches ANY of:**
- Authentication or authorization logic
- User input handling or validation
- External API integrations
- Database queries (especially dynamic)
- File system operations
- Cryptographic operations
- Sensitive data (PII, credentials, tokens)

Invoke the `security-engineer` agent with mode=scan:

```
Task(security-engineer, "
Mode: scan
Target: $1

Context from L1/L2: [Include relevant findings]

Security checklist:
- OWASP Top 10 vulnerability scan
- Input validation completeness
- Authentication/authorization weaknesses
- Data exposure risks
- Dependency CVE check

Output: .claude/reports/security/L3-security-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L3 report entry.

---

### Level 4: Reliability Review

**Trigger when change affects ANY of:**
- Infrastructure configuration
- Service dependencies
- Error handling or retry logic
- Caching mechanisms
- Database operations at scale
- External service integrations

Invoke the `sre` agent with mode=reliability-review:

```
Task(sre, "
Mode: reliability-review
Target: $1

Context from L1/L2/L3: [Include relevant findings]

Reliability assessment:
- Failure mode identification and handling
- SLO/SLI impact analysis
- Dependency reliability risks
- Graceful degradation capability
- Rollback safety and procedures

Output: .claude/reports/sre/L4-reliability-YYYYMMDD.md
")
```

**After completion:** Update `_registry.md` with L4 report entry.

---

## Execution Flow

Based on the `$ARGUMENTS` provided:

1. **`--quick`**: Execute L1 only, skip all other levels
2. **`--security`**: Execute L1 + L3, skip L2 and L4
3. **`--all`**: Execute all four levels regardless of triggers
4. **No flag**: Analyze target and apply triggers automatically

**Sequencing rule (from agent-coordination skill):**  
Each level MAY need prior level's output → Execute sequentially, verify between each.

---

## Post-Review Actions

### Verify Deliverables

After each agent completes, run verification:

```bash
.claude/skills/agent-coordination/scripts/verify.sh "[category]" "[name]" "[date]"
```

### Update Registries

1. **Always:** Add each report to `_registry.md`
2. **If issues deferred:** Add to `_tech-debt.md` with format:
   ```
   - [ ] **TD-NNN**: [Description]
     - **Impact:** [Critical|High|Medium|Low]
     - **Source:** full-review-YYYYMMDD.md
   ```

---

## Aggregated Summary Report

After completing applicable levels, generate:

```markdown
# Full Review Summary: $1

**Review Date:** YYYY-MM-DD
**Reviewed By:** Claude Code Review System

## Levels Completed
- [x] L1: Peer Review
- [ ] L2: Architecture Review (if applicable)
- [ ] L3: Security Review (if applicable)
- [ ] L4: Reliability Review (if applicable)

## Blocking Issues (Must Fix)
| Level | Issue | Location | Severity |
|-------|-------|----------|----------|
| L1 | [description] | file:line | BLOCKING |

## Non-Blocking Issues (Should Fix)
| Level | Issue | Location | Priority |
|-------|-------|----------|----------|
| L1 | [description] | file:line | HIGH |

## Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]

## Tech Debt (Deferred)
Items marked "won't fix now" → append to `.claude/reports/_tech-debt.md`

## Verdict
- [ ] **APPROVED**: Ready to merge (all blocking resolved)
- [ ] **CHANGES REQUESTED**: Blocking issues remain

## Report Links
- L1: `.claude/reports/review/L1-peer-YYYYMMDD.md`
- L2: `.claude/reports/review/L2-arch-YYYYMMDD.md`
- L3: `.claude/reports/security/L3-security-YYYYMMDD.md`
- L4: `.claude/reports/sre/L4-reliability-YYYYMMDD.md`
```

**Output:** `.claude/reports/review/full-review-YYYYMMDD.md`

**Final step:** Add summary report to `_registry.md`.

---

## Decision Flowchart

```
┌─────────────────────────────────────────────────────────────┐
│                         START                                │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
              ┌────────────────────────┐
              │   L1: Peer Review      │ ◄── Always runs
              └───────────┬────────────┘
                          ▼
              ┌────────────────────────┐
              │ --quick flag present?  │
              └───────────┬────────────┘
                    │           │
                   Yes          No
                    │           ▼
                    │   ┌──────────────────────────┐
                    │   │ Change > 200 lines OR    │
                    │   │ new API/schema/module?   │
                    │   └───────────┬──────────────┘
                    │         │           │
                    │        Yes          No
                    │         ▼           │
                    │   ┌─────────────┐   │
                    │   │ L2: Arch    │   │
                    │   └──────┬──────┘   │
                    │          ▼          ▼
                    │   ┌──────────────────────────┐
                    │   │ Touches auth/input/data/ │
                    │   │ crypto/external APIs?    │
                    │   └───────────┬──────────────┘
                    │         │           │
                    │        Yes          No
                    │         ▼           │
                    │   ┌─────────────┐   │
                    │   │ L3: Security│   │
                    │   └──────┬──────┘   │
                    │          ▼          ▼
                    │   ┌──────────────────────────┐
                    │   │ Affects infra/deps/      │
                    │   │ error handling/caching?  │
                    │   └───────────┬──────────────┘
                    │         │           │
                    │        Yes          No
                    │         ▼           │
                    │   ┌─────────────┐   │
                    │   │ L4: SRE     │   │
                    │   └──────┬──────┘   │
                    │          │          │
                    ▼          ▼          ▼
              ┌────────────────────────────────┐
              │      Aggregate Results          │
              └───────────────┬────────────────┘
                              ▼
              ┌────────────────────────────────┐
              │   Generate Summary Report       │
              └───────────────┬────────────────┘
                              ▼
              ┌────────────────────────────────┐
              │   Update _registry.md          │
              └────────────────────────────────┘
```
