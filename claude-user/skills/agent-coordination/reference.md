# Agent Coordination Reference

Load this file for detailed verification, archiving, retry logic, and edge cases.

---

## Archive Details

### archive_reports.py Usage

```bash
# Script location: .claude/skills/agent-coordination/scripts/archive_reports.py

# Basic archiving (default: 7 days)
python .claude/skills/agent-coordination/scripts/archive_reports.py

# Custom threshold (14 days)
python .claude/skills/agent-coordination/scripts/archive_reports.py 14

# Dry run (preview without moving)
python .claude/skills/agent-coordination/scripts/archive_reports.py 7 --dry-run
```

**How it works:**
1. Parses active registry entries (by date in registry, not filename)
2. Moves files older than threshold to `.claude/reports/archive/[category]/`
3. Creates dated archive registry: `_registry-archive-YYYYMMDD.md`
4. Updates active registry (removes archived entries)
5. Changes status to "Archived" in archive registry

**Output:**
- Dated archive: `.claude/reports/archive/_registry-archive-YYYYMMDD.md`
- Moved files: `.claude/reports/archive/[category]/[filename].md`
- Updated active registry: `.claude/reports/_registry.md`

**When to run:**
- Registry exceeds 50 entries
- Weekly cleanup
- Before starting major work (clean context)

---

## Verification Details

### verify.sh Usage

```bash
# Script location: .claude/skills/agent-coordination/scripts/verify.sh

# Basic verification
.claude/skills/agent-coordination/scripts/verify.sh "review" "code-security-audit" "20251213" ""

# With git path check
.claude/skills/agent-coordination/scripts/verify.sh "impl" "auth-module" "20251213" "src/auth/"
```

### Manual Verification (if script unavailable)

```bash
# 1. Report exists
test -f ".claude/reports/[cat]/[name]-[date].md" && echo "OK" || echo "MISSING"

# 2. Has content (>10 lines)
[ $(wc -l < ".claude/reports/[cat]/[name]-[date].md") -gt 10 ] && echo "OK" || echo "EMPTY"

# 3. Registry updated
grep -q "[name]-[date]" .claude/reports/_registry.md && echo "OK" || echo "NOT IN REGISTRY"

# 4. Code changed (optional)
git status --short | grep -q "[path]" && echo "OK" || echo "NO CHANGES"
```

---

## Retry Protocol

### Attempt 1: Initial Invocation
Standard task prompt.

### Attempt 2: Explicit Tool Requirements
Add to prompt:
```
CRITICAL: You MUST use the Write tool to create the report file at .claude/reports/[cat]/[name].md
Do NOT just describe the report - actually create the file.
```

### Attempt 3: Different Model
If using sonnet, try haiku for simpler tasks.
If using haiku, escalate to sonnet.

### Attempt 4: Escalate to User
Report:
- What was attempted
- What failed
- Suggested manual action

---

## Sequencing Examples

### Parallel Safe
```
# These don't share output files
Task(code-quality, "Review src/api/ for security", mode: review)
Task(code-quality, "Review src/models/ for correctness", mode: review)
Task(test-engineer, "Run test coverage")
```

### Sequential Required
```
# Architect output feeds frontend
Task(architect, "Design dashboard API contract", mode: system)
# VERIFY: .claude/reports/arch/arch-dashboard-api-*.md exists
Task(frontend, "Implement dashboard using API contract from arch report")
# VERIFY: src/components/Dashboard/* exists
Task(test-engineer, "Test dashboard components")
```

---

## Common Patterns

### Code Review + Fix Flow
```
1. code-quality (mode: review) → findings report
2. VERIFY report
3. IF critical issues: code-quality (mode: debug) → root cause
4. VERIFY report
5. [Implementation agent] → fixes
6. test-engineer → validate fixes
```

### Feature Implementation Flow
```
1. architect (mode: system) → design
2. VERIFY report
3. [backend/frontend] → implement
4. VERIFY code + report
5. code-quality (mode: review) → review
6. test-engineer → tests
7. docs → documentation
```

### Data Pipeline Flow
```
1. architect (mode: pipeline) → pipeline design
2. VERIFY report
3. data-engineer (mode: collect) → collection
4. data-engineer (mode: analyze) → EDA
5. data-engineer (mode: preprocess) → preprocessing
6. ml-engineer (mode: train) → training
7. ml-engineer (mode: evaluate) → evaluation
```

---

## Edge Cases

### Agent Creates Wrong File Location
- Retry with explicit path in prompt
- Add: "Save to EXACTLY this path: .claude/reports/[full/path]"

### Agent Describes Instead of Creates
- Add: "You MUST use Write tool, not describe what you would write"
- Check agent has Write in allowed-tools

### Registry Conflict
- If same-named report exists, append `-v2` or timestamp
- Update both entries in registry (mark old as Superseded)

### Context Too Large
- Summarize reports instead of including full text
- Use: "Key finding from [report]: [one sentence]"
- Limit to 3 most relevant prior reports

---

## Design Integration

When task involves frontend/styling:
1. Note in prompt: "Follow design-system skill (brand vs data colors)"
2. For data viz: "Use data colors only (#33BBEE, #0077BB sequence)"
3. For UI: "Use brand colors (#0176D3, #032D60)"

---

## Quality Checklist

Before marking task complete:
- [ ] All agent deliverables verified
- [ ] Registry updated with all new reports
- [ ] Handoff created if follow-up needed
- [ ] Summary provided to user
