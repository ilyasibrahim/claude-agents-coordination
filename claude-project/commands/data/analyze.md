---
description: Analyze dataset with data-analyst agent (project-specific EDA)
allowed-tools: Bash(python:*), Bash(jupyter:*)
argument-hint: [file path]
---

# Data Analysis

Perform exploratory data analysis (EDA) on dataset.

## Workflow

Follows user-level agent-coordination protocol:

1. **Check Registry** - Look for prior analysis reports
2. **Context Injection** - Provide relevant prior work to agent
3. **Execute Analysis** - Run EDA with data-analyst agent
4. **Update Registry** - Add report to `_registry.md`

## Process

1. **Load Dataset**
   - Read file (CSV, JSON, JSONL, Parquet)
   - Verify format and structure
   - Display basic info (rows, columns, dtypes)

2. **Descriptive Statistics**
   - Dataset size and shape
   - Missing values analysis
   - Data type distribution
   - Basic statistics (mean, median, std)

3. **Quality Analysis** (invokes data-quality-standards skill)
   - Duplicate detection
   - Language purity check (for text data)
   - Quality score distribution
   - Outlier identification

4. **Content Analysis** (Somali dialect specific)
   - Dialect distribution (Northern/Southern/Central)
   - Text length distribution
   - Vocabulary analysis
   - Source contribution breakdown

5. **Visualizations**
   - Distribution plots
   - Bar charts (dialect counts)
   - Histograms (text length)
   - Word clouds (optional)

6. **Generate Report**
   - Executive summary
   - Key findings
   - Data quality assessment
   - Recommendations for cleaning/preprocessing

## Arguments

- **$1**: Required file path
  - CSV: `data/raw/dataset.csv`
  - JSONL: `data/processed/data.jsonl`
  - Parquet: `data/final/train.parquet`

## Examples

```bash
# Analyze CSV file
/data/analyze data/raw/wikipedia_somali.csv

# Analyze processed JSONL
/data/analyze data/processed/cleaned_data.jsonl

# Analyze training set
/data/analyze data/final/train.jsonl
```

## Output

**Report Location:** `.claude/reports/analysis/analysis-[topic]-YYYYMMDD.md`

**Console:**
- Quick statistics
- Key insights
- Quality metrics

**Artifacts:**
- Charts: `data/analysis/charts/`
- Notebooks: `data/analysis/notebooks/` (if Jupyter used)

## Analysis Includes

**Dataset-Level:**
- Total records
- Records per dialect
- Average text length
- Quality score distribution
- Duplicate rate

**Per-Source:**
- Records contributed
- Quality metrics
- Rejection rate

**Per-Dialect:**
- Record count
- Percentage of total
- Average quality score
- Text length statistics

## Skills Invoked

- `data-quality-standards` - Quality validation rules
- `etl-patterns` - Data loading patterns
- `lrl-nlp-techniques` - Low-resource NLP context (if dialect analysis)

## Registry Update

After completion, add to `.claude/reports/_registry.md`:
```
- analysis-[topic]-YYYYMMDD | Complete | [1-line summary]
```
