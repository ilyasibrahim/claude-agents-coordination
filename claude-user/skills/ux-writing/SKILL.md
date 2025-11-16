---
name: ux-writing
description: Voice, tone, messaging standards, and content guidelines for data/ML dashboards. Covers professional-yet-accessible voice, context-specific tone, microcopy standards, error messages, success states, and data presentation language. Auto-invokes when working on copy, messaging, content, user-facing text, UX writing, labels, error messages, or any user communication.
allowed-tools: Read
---

# UX Writing Skill

## Brand Voice Characteristics

Data/ML dashboards speak with a voice that is:

- **Professional yet Accessible:** Technical precision without jargon overload
- **Educational:** Explaining complex concepts clearly for diverse audiences
- **Evidence-Based:** Data-driven insights with context and interpretation
- **Collaborative:** Emphasizing open-source community and shared goals
- **Progress-Oriented:** Focusing on forward momentum and improvement

---

## Tone Variations by Context

### Executive Mode (High-Level Overview)

**Tone:** Strategic, narrative-driven, impact-focused

**Language:** Business outcomes, strategic value, big picture

**Audience:** Decision-makers, stakeholders, executives

**Example:**
> "Machine learning models require high-quality training data to achieve production-ready performance."

### Analyst Mode (Detailed Technical)

**Tone:** Precise, data-rich, operationally focused

**Language:** Technical metrics, pipeline details, granular insights

**Audience:** Data engineers, ML researchers, analysts

**Example:**
> "Retention through discovery → silver dataset"

### Error States

**Tone:** Calm, informative, solution-oriented

**Language:** Clear problem statement + actionable next steps

**Example:**
> "Unable to load metrics data. Check your connection and refresh the page."

### Success States

**Tone:** Confirming, encouraging, matter-of-fact

**Language:** Clear confirmation without over-enthusiasm

**Example:**
> "Pipeline run completed successfully."

### Guidance/Help

**Tone:** Supportive, clear, contextual

**Language:** Plain English, step-by-step when needed

**Example:**
> "Filter by acquisition method or SLA to focus on workstreams."

---

## Writing Principles

### 1. Clarity and Concision

**Rules:**
- Lead with the most important information
- Use concrete terms over abstract concepts
- Avoid redundant qualifiers ("very", "really", "actually")
- One idea per sentence when possible

**Examples:**
- ❌ "The data that was collected during the most recent ingestion process"
- ✅ "Latest ingestion data"

---

- ❌ "Click here to view your data"
- ✅ "View data"

### 2. Active vs. Passive Voice

**Active Voice (Preferred):**
- "The pipeline processes 1,200 records per minute"
- "Quality filters removed 450 duplicates"
- "This dashboard tracks real-time ingestion metrics"

**Passive Voice (Acceptable):**
- "Records are validated against quality guardrails" (focus on records)
- "Data is sourced from Wikipedia, BBC, HuggingFace" (focus on data origin)

### 3. Technical Terminology Usage

| Context | Term Choice | Example |
|---------|-------------|---------|
| First mention | Full term | "Extract, Transform, Load (ETL)" |
| Subsequent | Acronym | "ETL readiness" |
| Headers | Scannable | "Source Portfolio & ETL Readiness" |
| Help text | Plain | "Transform and clean your data" |

---

## Microcopy Standards

### Buttons

**Primary Actions:**
- "View Dashboard" (not "Click to View Dashboard")
- "Upload Data" (not "Upload Your Data File")
- "Run Pipeline" (not "Start Pipeline Run")

**Secondary Actions:**
- "Learn More" (not "Read Documentation")
- "Cancel" (not "Cancel Operation")
- "Back" (not "Go Back")

**Destructive Actions:**
- "Delete Dataset" (not "Delete")
- "Remove Source" (not "Remove")
- Use confirmation modals for irreversible actions

### Form Labels

**Clear and Descriptive:**
- "Dataset Name" (not "Name")
- "Source URL" (not "URL")
- "Target Language" (not "Language")

**Help Text (below label):**
- Provide context when field purpose isn't obvious
- Use sentence case
- Keep under 60 characters

**Example:**
```
Source URL
Enter the URL where data will be fetched
[input field]
```

### Error Messages

**Structure:** Problem + Reason (if helpful) + Solution

**Examples:**

✅ **Good:**
> "Unable to connect to data source. Check the URL and try again."

❌ **Bad:**
> "Error 404. Connection failed."

---

✅ **Good:**
> "File size exceeds 10MB limit. Compress the file or split into smaller chunks."

❌ **Bad:**
> "File too large."

---

✅ **Good:**
> "Invalid email format. Use: name@example.com"

❌ **Bad:**
> "Invalid input."

### Success Messages

**Keep it Simple:**
- "Data uploaded successfully"
- "Pipeline run completed"
- "Changes saved"

**Add Context When Helpful:**
- "1,234 records processed successfully"
- "Model deployed to production"
- "Report exported to downloads folder"

### Empty States

**Structure:** Explanation + Action

**Examples:**

✅ **Good:**
> "No datasets yet. Upload your first dataset to get started."

❌ **Bad:**
> "No data"

---

✅ **Good:**
> "No active pipelines. Create a pipeline to begin processing data."

❌ **Bad:**
> "Empty"

### Loading States

**Be Specific:**
- "Loading dashboard..." (not "Loading...")
- "Processing 1,234 records..." (not "Processing...")
- "Training model..." (not "Please wait...")

---

## Data Presentation Language

### Metrics and Numbers

**Use Formatting:**
- 1,234,567 (commas for thousands)
- 45.2% (one decimal for percentages)
- $1.2M (abbreviate large numbers with context)

**Provide Context:**
- "1,234 records (+12% from last month)"
- "85% accuracy (target: 80%)"
- "2.3s avg response time (down from 3.1s)"

### Trends and Changes

**Positive Changes:**
- "+12.5% increase"
- "↑ 450 records"
- "Improved from 85% to 92%"

**Negative Changes:**
- "-8.2% decrease"
- "↓ 120 records"
- "Dropped from 95% to 89%"

**Neutral Changes:**
- "Stable at 1,200 records"
- "Unchanged from last period"

### Chart Labels

**Axis Labels:**
- Capitalize first word only
- Be specific but concise
- "Number of records" (not "Records" or "Count")

**Legend Labels:**
- Use title case
- Be descriptive
- "Training Set" (not "training" or "train")

**Tooltips:**
- Include metric name, value, and context
- "Northern Dialect: 1,234 records (42% of total)"

---

## Voice & Tone Examples

### Headlines

**Executive Mode:**
- "Building Data Infrastructure for ML Excellence"
- "Transforming Raw Data into Training-Ready Datasets"
- "Open-Source Collaboration for Better Models"

**Analyst Mode:**
- "Pipeline Performance Metrics"
- "Data Quality Insights"
- "Distribution Overview"

### Descriptions

**Feature Descriptions:**
- "Track data ingestion in real-time with automatic quality validation"
- "Monitor pipeline health across all data sources"
- "Analyze class distribution patterns in your training data"

**Help Text:**
- "Select the classification model to apply. Each model is optimized for specific use cases."
- "Quality filters automatically remove duplicates, invalid entries, and low-confidence predictions."

---

## Accessibility in Writing

### Alt Text for Images

**Be Descriptive:**
- "Bar chart showing training data distribution across classification categories"
- "Pie chart displaying data source contribution percentages"

**Don't State the Obvious:**
- ❌ "Image of a chart"
- ✅ "Monthly ingestion trends from January to December 2024"

### Link Text

**Be Specific:**
- "View complete dataset documentation"
- "Download quality report (PDF, 2.3MB)"

**Avoid Generic:**
- ❌ "Click here"
- ❌ "Read more"
- ❌ "Learn more"

### ARIA Labels

**For Icon Buttons:**
```html
<button aria-label="Delete dataset">
  <svg>...</svg>
</button>
```

**For Status Indicators:**
```html
<span aria-label="Pipeline status: healthy">
  <svg class="status-icon--healthy">...</svg>
</span>
```

---

## Content Patterns

### Onboarding/Empty States

**Pattern:** Welcome + Explanation + Action

**Example:**
> "Welcome to Your Analytics Dashboard
>
> Track data quality, monitor pipeline performance, and explore dataset insights.
>
> [Upload First Dataset]"

### Confirmation Modals

**Pattern:** Question + Impact + Actions

**Example:**
> "Delete this dataset?
>
> This action cannot be undone. The dataset and all associated metrics will be permanently removed.
>
> [Cancel] [Delete Dataset]"

### Progress Indicators

**Pattern:** Current Step + What's Happening + What's Next

**Example:**
> "Step 2 of 4: Validating Data
>
> Checking for duplicates and invalid entries...
>
> Next: Quality scoring"

---

## Common Phrases & Terminology

### Preferred Terms

| Use This | Not This |
|----------|----------|
| Dataset | Data set, data-set |
| Pipeline | Data pipeline, ETL process |
| Quality score | Score, rating |
| Training data | Train data, training set |
| Validation set | Val set, validation data |
| Model accuracy | Accuracy, model performance |
| Real-time | Realtime, real time |

### Domain-Specific Terms

- Use full product/model names on first mention, then abbreviations
- Capitalize dialect, language, or category names consistently
- Use hyphenated compound adjectives (e.g., "low-resource language", "multi-class model")

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Copy, copywriting, UX writing
- Messaging, content, user-facing text
- Error messages, success messages
- Labels, placeholders, help text
- Tone, voice, writing style
- Microcopy, button text, form labels
- Alt text, ARIA labels, accessibility text
- Empty states, loading states
- User communication, user guidance

---

## Related Skills

- **style-guide:** Visual design philosophy, aesthetics
- **design-system:** Technical implementation, components
- **accessibility-checklist:** WCAG compliance (project-specific)

---

## Complete Reference

For complete UX writing guidelines with more examples, see:
`.claude/UX_WRITING_GUIDE.md`

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
