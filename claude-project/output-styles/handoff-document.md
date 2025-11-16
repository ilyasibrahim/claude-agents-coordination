---
name: handoff-document
description: Format for agent-to-agent coordination and task handoffs
---

# Handoff Document Output Style

Use this format for agent-to-agent coordination, task handoffs, and collaboration workflows.

## Template

```markdown
# Handoff: [From Agent] → [To Agent]

**From:** [Source Agent Name]
**To:** [Target Agent Name/Role]
**Date:** YYYY-MM-DD
**Priority:** 🔴 URGENT | 🟡 HIGH | 🟢 NORMAL | 🔵 LOW
**Handoff ID:** [Optional unique identifier]

---

## Context

### Background
[1-2 paragraphs explaining the situation, what work has been completed, and why the handoff is needed]

### Work Completed
- ✅ Task 1 - [Brief description]
- ✅ Task 2 - [Brief description]
- ✅ Task 3 - [Brief description]

### Current Status
[Current state of the work, what's functional, what's pending]

---

## Action Items

### Primary Tasks

#### Task 1: [Clear, Actionable Title]
**Priority:** 🔴 URGENT | 🟡 HIGH | 🟢 NORMAL | 🔵 LOW
**Estimated Effort:** X hours/days
**Dependencies:** [Any blockers or prerequisites]

**Description:**
[Detailed description of what needs to be done]

**Acceptance Criteria:**
- [ ] Criterion 1 (specific, measurable)
- [ ] Criterion 2
- [ ] Criterion 3

**Files Affected:**
- `path/to/file1.ext` - [What to do]
- `path/to/file2.ext` - [What to do]

**Code References:**
```[language]
// Example or starting point
function exampleFunction() {
  // Implement this logic
}
```

**Testing Requirements:**
- Test scenario 1
- Test scenario 2

---

#### Task 2: [Another Task]
[Same structure as Task 1]

---

### Secondary Tasks (Optional)

#### Task 3: [Nice-to-Have Task]
**Priority:** 🔵 LOW
**Description:** [Brief description]

---

## Must Read

### Critical Documents
**Priority Reading (Required):**
1. **[Document Name]** - `path/to/doc.md`
   - Read: Sections X, Y, Z
   - Why: [Reason these sections are critical]
   - Key Takeaway: [Main point to understand]

2. **[Another Document]** - `path/to/doc2.md`
   - Read: Full document
   - Why: [Importance]

**Supporting Reading (Optional):**
- [Doc 3] - Background context
- [Doc 4] - Related decisions

### Code to Review
**Critical Code Sections:**
1. **`src/module/file.py:lines 50-80`**
   - What it does: [Explanation]
   - Why it matters: [Relevance to handoff]
   - Watch out for: [Gotchas or edge cases]

2. **`src/another/file.js:lines 120-150`**
   - [Same structure]

### Recent Changes
**Recent Commits to Be Aware Of:**
- `abc1234` - feat: Added feature X
- `def5678` - fix: Fixed bug Y
- `ghi9012` - refactor: Restructured module Z

**Impact:** [How these changes affect the handoff work]

---

## Dependencies & Blockers

### Prerequisites (Must Be Complete First)
- [ ] **Dependency 1** - [Status: Complete | In Progress | Pending]
  - What: [Description]
  - Who: [Responsible agent/person]
  - ETA: [If not complete]

- [ ] **Dependency 2** - [Status]
  - [Details]

### Blocks (What This Work Enables)
- **Blocked Work 1:** [Description of what can't proceed without this]
- **Blocked Work 2:** [Description]

### External Dependencies
- API endpoint X must be deployed
- Database migration Y must run
- Configuration Z must be updated

---

## Known Issues & Gotchas

### Known Issues
1. **Issue 1:** [Description]
   - Impact: [How it affects the work]
   - Workaround: [Temporary solution if available]
   - Tracking: [Issue number or reference]

2. **Issue 2:** [Description]
   - [Details]

### Gotchas & Edge Cases
- ⚠️ **Gotcha 1:** [Unexpected behavior to watch for]
  - Why it happens: [Explanation]
  - How to handle: [Recommendation]

- ⚠️ **Gotcha 2:** [Another tricky aspect]
  - [Details]

### Technical Debt
- [Debt item 1] - Should be addressed but not blocking
- [Debt item 2] - Future improvement opportunity

---

## Technical Details

### Architecture Context
[Brief overview of relevant architecture, data flow, or system design]

```
[Optional diagram or ASCII art showing architecture]
```

### Key Design Decisions
1. **Decision 1:** [What was decided]
   - Rationale: [Why]
   - Alternatives Considered: [What else was evaluated]

2. **Decision 2:** [Another decision]
   - [Details]

### Configuration & Environment
**Environment Variables:**
- `VAR_NAME_1=value` - [Purpose]
- `VAR_NAME_2=value` - [Purpose]

**Required Tools/Dependencies:**
- Tool 1: version X.Y.Z
- Tool 2: version A.B.C

---

## Testing Requirements

### Test Scenarios
1. **Scenario 1:** [Description]
   - Steps: [How to test]
   - Expected Result: [What should happen]
   - Actual Behavior: [Current state if applicable]

2. **Scenario 2:** [Another scenario]
   - [Details]

### Test Data
**Available Test Data:**
- Dataset 1: `path/to/test/data.json` - [Description]
- Dataset 2: `path/to/fixtures/` - [Description]

**Test Commands:**
```bash
# Run tests for this feature
pytest tests/test_feature.py -v

# Run with coverage
pytest --cov=src.module tests/test_feature.py
```

---

## Success Criteria

### Definition of Done
- [ ] All action items completed
- [ ] Tests pass (unit, integration, e2e)
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] No regressions introduced

### Quality Standards
- Code coverage: ≥80%
- Performance: [Specific requirements]
- Security: [Security checks passed]
- Accessibility: [WCAG AA for UI work]

### Acceptance Validation
**How to verify success:**
1. Verification step 1
2. Verification step 2
3. Verification step 3

---

## Communication & Follow-Up

### Questions or Clarifications
**If you need clarification on:**
- [Topic 1]: Contact [Agent/Person] or reference [Document]
- [Topic 2]: Check [Resource]

**Common Questions Anticipated:**
1. **Q:** [Likely question]
   **A:** [Pre-answered]

2. **Q:** [Another question]
   **A:** [Answer]

### Progress Updates
**Expected Updates:**
- Checkpoint 1: [When] - [What to report]
- Checkpoint 2: [When] - [What to report]

**Report Back When:**
- Task completed
- Blockers encountered
- Significant issues discovered

### Next Handoff
**After completing this work, hand off to:**
- [Next Agent]: For [next step]
- [Another Agent]: For [another aspect]

---

## Appendix

### Related Handoffs
- Previous: [handoff-xxx-20251105.md]
- Related: [handoff-yyy-20251103.md]

### Additional Resources
- [Resource 1 title]: [Link or path]
- [Resource 2 title]: [Link or path]

### Rollback Plan
**If things go wrong:**
1. Rollback step 1
2. Rollback step 2
3. Contact: [Person/Team]

---

## Handoff Sign-Off

**From Agent:**
- [x] All context provided
- [x] Action items clearly defined
- [x] Dependencies documented
- [x] Must-read materials specified
- [x] Success criteria established

**Signature:** [Source Agent Name] - YYYY-MM-DD HH:MM

**To Agent Acknowledgment:**
- [ ] Handoff received and understood
- [ ] Prerequisites checked
- [ ] Ready to begin work
- [ ] Questions clarified (if any)

**Signature:** [Target Agent Name] - YYYY-MM-DD HH:MM
```

## Usage Guidelines

**Use this style for:**
- Agent-to-agent task coordination
- Work handoffs between specialists
- Cross-team collaboration
- Sequential workflow steps

**Key Principles:**
- Provide complete context (don't assume knowledge)
- Make action items specific and measurable
- Document dependencies and blockers explicitly
- Anticipate questions and provide answers
- Include reproduction/testing instructions
- Define success criteria clearly
- Maintain traceability (link to related handoffs)

**Priority Levels:**
- 🔴 **URGENT**: Immediate attention required, blocking
- 🟡 **HIGH**: Important, should start soon
- 🟢 **NORMAL**: Standard priority, complete in normal flow
- 🔵 **LOW**: Nice-to-have, can be deferred

**Handoff Types:**
- **Sequential**: One agent completes work, hands to next agent
- **Parallel**: Multiple agents work simultaneously on related tasks
- **Review**: Work completed, needs validation/approval
- **Blocked**: Work paused, awaiting prerequisite completion

## Examples

**Good Handoff:**
- Complete context with background
- Specific, actionable tasks
- Clear acceptance criteria
- Dependencies explicitly stated
- Must-read materials identified
- Success criteria defined
- Testing requirements specified

**Avoid:**
- Vague action items ("fix the bug")
- Missing context or background
- No success criteria
- Undocumented dependencies
- No testing guidance
- Missing file/code references
- Unclear priorities
