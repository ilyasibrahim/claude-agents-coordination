---
name: technical-report
description: Format for technical reports, architecture documents, and analysis deliverables
---

# Technical Report Output Style

Use this format for technical reports, analysis documents, and architectural specifications.

## Template

```markdown
# [Report Type]: [Title]

**Author:** [Agent Name]
**Date:** YYYY-MM-DD
**Status:** Draft | Active | Implemented | Archived
**Version:** X.Y.Z

---

## Executive Summary

[2-4 sentences summarizing the key points, decisions, or findings]

---

## Overview

### Context
[Background information and motivation for this work]

### Objectives
- Objective 1
- Objective 2
- Objective 3

### Scope
**In Scope:**
- Item 1
- Item 2

**Out of Scope:**
- Item 1
- Item 2

---

## Technical Details

### [Section 1]
[Detailed technical content]

```[language]
// Code examples when relevant
```

### [Section 2]
[More technical content]

---

## Key Decisions

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| Decision 1 | Why we chose this | What else we looked at |
| Decision 2 | Justification | Other options |

---

## Implementation

### Requirements
- Requirement 1
- Requirement 2

### Steps
1. Step 1
2. Step 2
3. Step 3

### Timeline
- Phase 1: [Duration] - [Description]
- Phase 2: [Duration] - [Description]

---

## Metrics & Success Criteria

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Metric 1 | Value | How to measure |
| Metric 2 | Value | How to measure |

---

## Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|-------------------|
| Risk 1 | High/Med/Low | High/Med/Low | How to address |
| Risk 2 | High/Med/Low | High/Med/Low | How to address |

---

## Dependencies

**Depends On:**
- Dependency 1 - Why
- Dependency 2 - Why

**Blocks:**
- What can't proceed without this
- What is waiting on this work

---

## References

- Reference 1: [Link or file path]
- Reference 2: [Link or file path]
- Related Report: [filename]

---

## Appendix

### Glossary
- **Term 1**: Definition
- **Term 2**: Definition

### Additional Resources
- Resource 1
- Resource 2

---

## Change Log

- **YYYY-MM-DD**: Initial creation
- **YYYY-MM-DD**: Updated - [what changed]
```

## Usage Guidelines

**Use this style for:**
- Architecture documents
- Technical specifications
- Analysis reports
- Design proposals
- Research findings
- Performance analysis

**Key Principles:**
- Start with executive summary (busy stakeholders)
- Include visual diagrams where helpful
- Provide concrete examples and code samples
- Document decision rationale (not just what, but why)
- Include metrics and success criteria
- Address risks and dependencies explicitly
- Maintain clear section hierarchy

**Length:**
- Executive Summary: 2-4 sentences
- Overview: 1-2 paragraphs
- Technical Details: As needed (be thorough)
- Total: Typically 1000-3000 words

## Examples

**Good Technical Report:**
- Clear purpose stated upfront
- Technical depth with examples
- Decisions explained with rationale
- Measurable success criteria
- Dependencies and risks documented

**Avoid:**
- Vague objectives without metrics
- Technical jargon without explanation
- Missing decision rationale
- No consideration of risks
- Incomplete references
