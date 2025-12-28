---
name: ux-writing
description: Voice, tone, and content guidelines for data/ML dashboards. Covers microcopy, error messages, success states, and data presentation language. Auto-invokes on copy, messaging, content, labels, error messages keywords.
allowed-tools: Read
---

# UX Writing (Core)

## Voice

- **Professional yet Accessible** - Technical precision without jargon
- **Educational** - Explain complex concepts clearly
- **Evidence-Based** - Data-driven with context
- **Progress-Oriented** - Focus on forward momentum

---

## Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Executive | Strategic, narrative | "ML models require quality data for production performance" |
| Analyst | Precise, data-rich | "Retention: discovery → silver dataset" |
| Error | Calm, solution-focused | "Unable to load metrics. Check connection and refresh." |
| Success | Confirming, brief | "Pipeline completed successfully." |

---

## Microcopy Patterns

### Buttons
- Primary: "View Dashboard" (not "Click to View")
- Secondary: "Learn More" (not "Read Documentation")
- Destructive: "Delete Dataset" (not just "Delete")

### Errors
**Structure:** Problem + Solution
- "Unable to connect. Check URL and try again."
- "File exceeds 10MB. Compress or split."

### Empty States
**Structure:** Explanation + Action
- "No datasets yet. Upload your first dataset to get started."

### Loading
Be specific: "Loading dashboard..." not "Loading..."

---

## Data Presentation

### Numbers
- Use commas: 1,234,567
- One decimal for %: 45.2%
- Context: "1,234 records (+12% from last month)"

### Trends
- Positive: "+12.5%" or "↑ 450 records"
- Negative: "-8.2%" or "↓ 120 records"

---

## Accessibility

### Alt Text
Describe: "Bar chart showing training data distribution"
Not: "Image of chart"

### Links
Specific: "View dataset documentation"
Not: "Click here"

---

## Preferred Terms

| Use | Avoid |
|-----|-------|
| Dataset | Data set |
| Pipeline | ETL process |
| Real-time | Realtime |
| Training data | Train data |

---

**Version:** 2.0.0
