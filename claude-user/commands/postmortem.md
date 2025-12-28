---
description: Generate incident postmortem using SRE agent for blameless root cause analysis
---

# Postmortem Command

Invoke `sre` agent in incident mode for blameless postmortem generation.

## Usage

```
/postmortem [incident-description]
/postmortem --from-logs [log-path]
/postmortem --template               # Generate blank template
```

## Default Mode

```
Task(sre, "
Mode: incident

Incident: [description from user]

Generate blameless postmortem:

1. Incident Summary
   - Severity classification (SEV1-4)
   - Duration and impact
   - Detection method

2. Timeline Reconstruction
   - First indication
   - Detection time
   - Response actions
   - Resolution steps
   - Recovery confirmation

3. Root Cause Analysis
   - Technical root cause
   - Contributing factors
   - Why detection was delayed (if applicable)

4. Impact Assessment
   - Users affected
   - Business impact
   - Data implications

5. Action Items
   - Prevent recurrence
   - Improve detection
   - Process improvements
   - Each with owner and priority

6. Lessons Learned
   - What went well
   - What went wrong
   - What we'll do differently

Output: .claude/reports/sre/postmortem-[incident-slug]-YYYYMMDD.md

After generating postmortem:
- Add P0/P1 action items to .claude/reports/_tech-debt.md as Critical/High priority
- Format: TD-NNN with link to postmortem
")
```

## From Logs Mode

When analyzing existing logs/alerts:

```
/postmortem --from-logs [path-to-logs]
```

```
Task(sre, "
Mode: incident

Analyze logs at: [path]

Extract from logs:
- Error patterns
- Timeline of events
- Affected components
- Recovery indicators

Reconstruct incident narrative and generate postmortem.

Output: .claude/reports/sre/postmortem-[extracted-title]-YYYYMMDD.md
")
```

## Template Mode

Generate blank postmortem template:

```
/postmortem --template
```

Creates:

```markdown
# Postmortem: [TITLE]

## Incident Summary

| Field | Value |
|-------|-------|
| Severity | SEV1 / SEV2 / SEV3 / SEV4 |
| Duration | HH:MM to HH:MM (X hours Y minutes) |
| Impact | [Users affected, revenue impact] |
| Detection | Alert / Customer Report / Internal |
| Resolution | [How it was fixed] |

## Timeline (All times UTC)

| Time | Event |
|------|-------|
| | First signs of issue |
| | Issue detected |
| | Incident declared |
| | Root cause identified |
| | Fix implemented |
| | Service restored |
| | Incident closed |

## Root Cause

[Technical explanation of what caused the incident. Be specific about the chain of events.]

## Contributing Factors

1. [Factor that made the incident worse or more likely]
2. [Factor that delayed detection]
3. [Factor that complicated response]

## Impact

### User Impact
- [Number of users affected]
- [User-visible symptoms]
- [Duration of impact]

### Business Impact
- [Revenue impact if applicable]
- [Reputation impact]
- [SLA implications]

### Data Impact
- [Any data loss or corruption]
- [Recovery status]

## Response Analysis

### What Went Well
- [Effective monitoring/alerting]
- [Quick response time]
- [Good communication]
- [Effective mitigation]

### What Went Wrong
- [Detection gaps]
- [Response delays]
- [Communication issues]
- [Missing runbooks]

## Action Items

| Priority | Action | Owner | Due Date | Status |
|----------|--------|-------|----------|--------|
| P0 | [Prevent recurrence] | | | Open |
| P1 | [Improve detection] | | | Open |
| P1 | [Add missing test] | | | Open |
| P2 | [Update documentation] | | | Open |
| P2 | [Process improvement] | | | Open |

## Lessons Learned

### Technical
- [Technical insight gained]

### Process
- [Process improvement identified]

### Communication
- [Communication improvement]

## Related

- Previous similar incidents: [links]
- Related documentation: [links]
- Monitoring dashboards: [links]
```

## Severity Definitions

| Severity | Criteria | Response |
|----------|----------|----------|
| **SEV1** | Complete outage, data loss, security breach | Immediate (24/7 page) |
| **SEV2** | Major feature broken, significant degradation | < 1 hour response |
| **SEV3** | Minor feature broken, workaround exists | < 4 hours response |
| **SEV4** | Minimal impact, cosmetic issues | Next business day |

## Blameless Culture

The postmortem process is **blameless**:

- Focus on **systems**, not **people**
- Ask "what" and "how", not "who"
- Assume everyone acted with best intentions
- Look for systemic improvements
- Share learnings widely

**Bad:** "John deployed broken code"
**Good:** "Code with bug passed CI and was deployed due to missing test coverage for edge case"

## Follow-up Tracking

After postmortem:

1. **Create tickets** for each action item
2. **Schedule review** for action item completion
3. **Update runbooks** with lessons learned
4. **Share summary** with broader team
5. **Archive** in postmortem repository
