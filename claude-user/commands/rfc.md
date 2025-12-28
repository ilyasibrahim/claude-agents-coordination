---
description: Create or review RFC (Request for Comments) design document using rfc agent
---

# RFC Command

Invoke `rfc` agent for design document lifecycle management.

## Usage

```
/rfc [topic]                    # Create new RFC
/rfc review [RFC-path]          # Review existing RFC
/rfc decision [RFC-path]        # Record decision on RFC
/rfc list                       # List all RFCs
```

## Create New RFC

```
/rfc [topic description]
```

```
Task(rfc, "
Mode: author

Topic: [user's topic description]

Create comprehensive RFC covering:
1. Problem statement and motivation
2. Proposed solution with technical design
3. Alternatives considered
4. Security, privacy, performance considerations
5. Rollout plan with milestones

Assign next RFC number based on:
ls .claude/reports/rfc/ | grep -oE 'RFC-[0-9]+' | sort -t- -k2 -n | tail -1

Output: .claude/reports/rfc/RFC-[NNNN]-[slug].md
")
```

## Review RFC

```
/rfc review [path-to-rfc]
```

```
Task(rfc, "
Mode: review

RFC: [path-to-rfc]

Provide technical review:
1. Feasibility assessment
2. Risk identification
3. Completeness check
4. Security review
5. Scalability concerns
6. Specific change requests

Output: .claude/reports/rfc/review-RFC-[NNNN]-YYYYMMDD.md
")
```

## Record Decision

```
/rfc decision [path-to-rfc] [approve|reject|revise]
```

```
Task(rfc, "
Mode: decision

RFC: [path-to-rfc]
Decision: [approve/reject/revise]

Record:
1. Decision and rationale
2. Conditions (if approved)
3. Required revisions (if revise)
4. Rejection reasons (if rejected)
5. Implementation priority
6. Next steps

Update RFC status in original document.

Output: .claude/reports/rfc/decision-RFC-[NNNN]-YYYYMMDD.md
")
```

## List RFCs

```
/rfc list
```

```bash
# List all RFCs with status
echo "# RFC Registry"
echo ""
echo "| RFC | Title | Status | Date |"
echo "|-----|-------|--------|------|"
for f in .claude/reports/rfc/RFC-*.md; do
    num=$(basename "$f" | grep -oE 'RFC-[0-9]+')
    title=$(head -1 "$f" | sed 's/^# //')
    status=$(grep -m1 "Status:" "$f" | sed 's/.*Status:\*\* //')
    date=$(grep -m1 "Created:" "$f" | sed 's/.*Created:\*\* //')
    echo "| $num | $title | $status | $date |"
done
```

## When to Write an RFC

| Change Type | RFC Required? |
|-------------|---------------|
| New service or major feature | ✅ Yes |
| API breaking change | ✅ Yes |
| Database schema change | ✅ Yes |
| New external dependency | ✅ Yes |
| Security model change | ✅ Yes |
| Infrastructure change | ✅ Yes |
| Bug fix | ❌ No |
| Minor feature | ❌ No |
| Refactoring (no behavior change) | ❌ No |
| Documentation update | ❌ No |

## RFC Workflow Integration

```
1. Create RFC          /rfc "Add user authentication"
                              │
                              ▼
2. Stakeholder Review  /rfc review .claude/reports/rfc/RFC-0001-auth.md
                              │
                              ▼
3. Address Feedback    Edit RFC based on review
                              │
                              ▼
4. Decision            /rfc decision RFC-0001-auth.md approve
                              │
                              ▼
5. Implementation      Normal development workflow
```

## RFC Output Location

- RFCs: `.claude/reports/rfc/RFC-NNNN-[slug].md`
- Reviews: `.claude/reports/rfc/review-RFC-NNNN-YYYYMMDD.md`
- Decisions: `.claude/reports/rfc/decision-RFC-NNNN-YYYYMMDD.md`

## RFC Status Values

| Status | Meaning |
|--------|---------|
| Draft | Initial creation, not ready for review |
| In Review | Open for stakeholder feedback |
| Approved | Ready for implementation |
| Rejected | Will not be implemented |
| Needs Revision | Requires changes before approval |
| Implemented | Development complete |
| Superseded | Replaced by newer RFC |
