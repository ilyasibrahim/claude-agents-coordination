---
name: agent-coordination
description: Coordination protocol for the main Claude Code agent only. User must explicitly invoke this skill when coordinating multiple agents, managing institutional memory, or maintaining project reports. Provides agent orchestration, registry management, sequencing patterns, and handoff protocols. Not accessible to subagents - main agent provides all necessary context to subagents in task prompts.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, TodoWrite
---

# Agent Coordination Protocol

## Purpose & Scope

**Who:** Main Claude Code agent only (explicit user invocation required)
**What:** Agent orchestration, registry management, report structure, handoff protocols
**Critical:** Subagents never access this protocol, registries, or reports. Main agent provides all context in task prompts.

---

## Core Principle

**Build on existing work. Never recreate.**

Before invoking agents:
1. Check project registry for relevant prior work
2. Read relevant reports to extract context
3. Provide complete context to agents in task prompts

---

## File Locations (Project-Based)

**Registry:** `.claude/reports/_registry.md`

**Report folders:**
- `.claude/reports/analysis/` - Research, investigations
- `.claude/reports/arch/` - Architecture, specs, ADRs
- `.claude/reports/bugs/` - Bug reports, root cause analyses
- `.claude/reports/commits/` - Commit documentation
- `.claude/reports/design/` - UI/UX designs, design reviews
- `.claude/reports/exec/` - Executive summaries
- `.claude/reports/handoff/` - Agent coordination, task handoffs
- `.claude/reports/impl/` or `.claude/reports/implementation/` - Implementation details
- `.claude/reports/review/` - Code/design/QA reviews
- `.claude/reports/tests/` - Test results, coverage analysis
- `.claude/reports/archive/` - Completed/superseded reports

---

## Pre-Work Checklist

```
□ Check `.claude/reports/_registry.md` (date filter: last 3 days)
□ Identify relevant reports for current task
□ Read reports to extract decisions, constraints, requirements
□ Synthesize context for agent task prompts
```

---

## Registry Management

### Structure

```markdown
# Report Registry

**Last Updated:** YYYY-MM-DD (status summary)

> **Purpose:** Central index. Check here first.

---

## Reports by Category

### Analysis
| Report | Date | Status | Summary |
|--------|------|--------|---------|
| [name.md](analysis/name.md) | YYYY-MM-DD | Active | 2-5 sentence summary with key findings, decisions, metrics, recommendations. |

### Arch
[Same structure for all categories: Design, Bugs, Commits, Exec, Handoff, Impl, Review, Tests]
```

**Status:** Active | Completed | Superseded

### Date Filtering

Read last 3 days only to avoid context overload.

```bash
TODAY=$(date +%Y-%m-%d)
TWO_DAYS_AGO=$(date -v-2d +%Y-%m-%d)  # macOS
TWO_DAYS_AGO=$(date -d '2 days ago' +%Y-%m-%d)  # Linux
# Manually scan registry for Date >= TWO_DAYS_AGO
```

### Updating Registry

1. Determine category
2. Create table row: `| [category-topic-YYYYMMDD.md](category/category-topic-YYYYMMDD.md) | YYYY-MM-DD | Active | Summary (2-5 sentences). |`
3. Add to appropriate category section
4. Update "Last Updated" header
5. Sort chronologically

---

## Report Template

```markdown
# [Category]: [Topic]

**Created by:** [Agent Name]
**Date:** YYYY-MM-DD
**Status:** Draft | Active | Implemented | Completed | Superseded

---

## Executive Summary
[2-4 sentences]

---

## Key Decisions
- **Decision 1:** [Description with rationale]
- **Decision 2:** [Description with rationale]

---

## Context & Background
[Problem, current state, links to prior reports]

---

## [Content Sections]
[Organize clearly with subheadings, bullets, code blocks, tables]

---

## Implementation Items

### For [Agent/Role]:
- [ ] Task 1 (Priority: High/Medium/Low) - [Details]

---

## Dependencies

**Depends on:** [report.md] - [Why]
**Blocks:** [What can't proceed]

---

## Handoffs

### To [Agent]:
**Context:** [Background]
**Action items:**
- [ ] Task with acceptance criteria
**Must read:** This report: [Sections], Related: [report.md]
**Success criteria:** [How to verify completion]

---

## References
- [report.md] - [Relevance]
- [URL] - [Description]

---

## Change Log
- **YYYY-MM-DD:** Initial creation
```

**Naming:** `[category]-[topic]-YYYYMMDD.md`

---

## Agent Orchestration

### Workflow

1. Invoke this protocol (explicit user request)
2. Check registry (date-filtered: last 3 days)
3. Read relevant reports
4. Identify needed agents
5. Determine parallel vs sequential
6. Invoke agents with complete context
7. Verify deliverables
8. Collect outputs, create summary report
9. Update registry

### Sequencing Rule

**Will Agent B need to READ Agent A's output files?**
- YES → Sequential (A before B, verify between)
- NO → Parallel (invoke simultaneously)

### Parallel Execution

Use when: agents don't need each other's outputs, create different deliverables, work independently.

```
Task(agent-1, "context...")
Task(agent-2, "context...")
Task(agent-3, "context...")
```

### Sequential Execution

Use when: Agent B reads Agent A's output, depends on A's decisions, modifies same files, or order matters.

```
Task(agent-A, "context...")
↓ Verify deliverables
Task(agent-B, "context including A's output...")
```

### Providing Context

Subagents never read registry/reports. Provide all context in task prompt:

```
Task(agent-name, "
[Objective]

Context from registry:
- Decision 1 from [report-name]
- Decision 2 from [report-name]
- Current state: [summary]
- Constraints: [list]

Requirements:
- Req 1
- Req 2

Files:
- path/to/file

Expected deliverable:
- [Format, location, success criteria]

Focus areas:
- [Concern 1]
- [Concern 2]
")
```

---

## Verification (Mandatory After Every Agent)

### Phase 1: Define Expectations

Before invoking:
```
Expected deliverables:
1. Primary output: [description]
2. Report: .claude/reports/[category]/[name]-YYYYMMDD.md
3. Registry update: Entry in _registry.md
4. Code changes: [paths]
```

### Phase 2: Invoke

```
Task(agent-name, "context...")
```

### Phase 3: Verify

```bash
# Report exists
test -f ".claude/reports/[cat]/[name]-[date].md" && echo "✅" || echo "❌"

# Substantial content
wc -l ".claude/reports/[cat]/[name]-[date].md"

# Registry updated
grep -q "[name]-[date].md" ".claude/reports/_registry.md" && echo "✅" || echo "❌"

# Files modified
git status --short | grep "path/to/file" && echo "✅" || echo "❌"
```

### Phase 4: Decision

**All pass:** Proceed to next agent
**Any fail:** Retry with clarified instructions → try different model → escalate to user

### Retry Logic

1. **Attempt 1:** Initial invocation
2. **Attempt 2:** Clarified instructions + explicit tool requirements ("You MUST use Write tool to create report", "Create actual files, not describe")
3. **Attempt 3:** Different model (sonnet ↔ haiku)
4. **Attempt 4:** Escalate to user with failure details

---

## Handoff Protocol

When work creates follow-up tasks:

1. Create handoff report: `.claude/reports/handoff/handoff-[from]-to-[to]-[topic]-YYYYMMDD.md`
2. Use template from Report Template section
3. Update registry
4. Be specific: action items, success criteria

---

## Design & Frontend Protocol

**Before visual/styling work:**

```
□ Invoke `design-system` skill (color palettes, components)
□ Determine: UI work (brand colors) or visualization (data colors)
□ Check existing CSS patterns
□ Verify WCAG AA contrast
```

**Color Rules:**
- **Brand colors (#0176D3, #032D60):** UI elements only (buttons, nav, forms, cards)
- **Data colors (#33BBEE, #0077BB, etc.):** Charts/visualizations only
- Never mix brand + data colors
- Use CSS variables, not hardcoded values
- Test contrast: 4.5:1 text, 3:1 UI

**Code comments:**
```python
# Brand color per design-system: UI button
# Data color per design-system: chart bars
```

---

## Cross-Referencing

Reference reports in code:

```python
# OAuth2 per arch-api-design-20251106.md: Section 3.2
# Fixes bugs-auth-20251107.md
```

---

## Success Indicators

✅ No duplicate work (registry checked first)
✅ No missed requirements (reports read for context)
✅ Full traceability (code references reports)
✅ Smooth handoffs (clear action items)
✅ Institutional knowledge preserved
✅ Consistent design (system followed)
✅ Proper color usage (brand vs data separated)
✅ All deliverables verified before proceeding
✅ Correct sequencing (parallel vs sequential)
✅ Failed agents retried systematically
✅ Clear escalation when automation fails

---

## Related Skills

- **design-system** - Color palettes, component patterns
- **style-guide** - Visual philosophy, brand principles
- **ux-writing** - Content standards, messaging, tone

---

**Version:** 3.1.0
**Last Updated:** 2025-11-13
