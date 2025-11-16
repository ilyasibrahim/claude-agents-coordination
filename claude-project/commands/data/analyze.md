---
description: Analyze dataset with data-analyst agent
allowed-tools: Bash(python:*), Bash(jupyter:*)
argument-hint: [file path]
---

# Data Analysis

Perform exploratory data analysis (EDA) on dataset using data-analyst agent.

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

3. **Quality Analysis**
   - Duplicate detection
   - Language purity check (for text data)
   - Quality score distribution
   - Outlier identification

4. **Content Analysis** (for Somali dialect data)
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

**Console:**
- Quick statistics
- Key insights
- Quality metrics

**Report:**
- Saved to `.claude/reports/analysis/data-analysis-[date].md`
- Includes: summary, statistics, visualizations, recommendations

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

## Notes

- Invokes data-quality-standards skill automatically
- Uses etl-patterns skill for data loading
- Creates visualizations using matplotlib/seaborn
- Report follows agent-coordination
