---
name: data-quality-standards
description: Data quality validation rules, quality metrics, and acceptance criteria for Somali dialect classifier datasets. Covers duplicate detection, language filtering, quality scoring, and validation protocols. Auto-invokes when discussing data quality, validation, cleaning, or quality guardrails for this project.
allowed-tools: Read, Grep
---

# Data Quality Standards for Somali Dialect Classifier

## Quality Dimensions

### 1. Completeness
- All required fields present (text, label, source, timestamp)
- No null or empty text fields
- Labels properly assigned (Northern/Southern/Central)

### 2. Accuracy
- Text is in Somali (not English, Arabic, or other languages)
- Labels match actual dialect (validated by native speakers)
- Geographic metadata aligns with dialect labels

### 3. Consistency
- Uniform text encoding (UTF-8)
- Consistent label format (standardized names)
- Timestamp format standardized (ISO 8601)

### 4. Uniqueness
- No exact duplicates
- Near-duplicate detection (>95% similarity flagged)
- Source URL deduplication

### 5. Validity
- Text length within acceptable range (10-5000 characters)
- No corrupted/garbled text
- No HTML tags or formatting artifacts

---

## Quality Metrics

### Critical Metrics

**Language Purity:**
- Target: >98% Somali text
- Method: Language detection (langdetect, fastText)
- Action: Remove non-Somali text

**Duplicate Rate:**
- Target: <2% duplicates
- Method: Exact match + fuzzy matching (Levenshtein distance)
- Action: Keep first occurrence, remove duplicates

**Label Confidence:**
- Target: >90% inter-annotator agreement
- Method: Multiple annotators for sample
- Action: Re-label low-confidence examples

**Text Quality Score:**
- Target: Average score >7/10
- Components: Length, vocabulary richness, grammar
- Action: Filter texts with score <5

---

## Validation Pipeline

### Stage 1: Basic Validation
```python
def basic_validation(record):
    checks = {
        'has_text': bool(record.get('text', '').strip()),
        'has_label': record.get('label') in ['Northern', 'Southern', 'Central'],
        'valid_length': 10 <= len(record.get('text', '')) <= 5000,
        'valid_encoding': is_valid_utf8(record['text'])
    }
    return all(checks.values()), checks
```

### Stage 2: Language Detection
```python
from langdetect import detect

def validate_language(text):
    try:
        lang = detect(text)
        return lang == 'so'  # Somali ISO code
    except:
        return False
```

### Stage 3: Duplicate Detection
```python
from difflib import SequenceMatcher

def is_near_duplicate(text1, text2, threshold=0.95):
    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity >= threshold
```

### Stage 4: Quality Scoring
```python
def compute_quality_score(text):
    score = 0
    # Length appropriateness (1-3 points)
    if 50 <= len(text) <= 1000:
        score += 3
    elif 20 <= len(text) < 50 or 1000 < len(text) <= 3000:
        score += 2
    else:
        score += 1

    # Vocabulary richness (1-3 points)
    unique_words = len(set(text.split()))
    total_words = len(text.split())
    if total_words > 0:
        vocab_ratio = unique_words / total_words
        if vocab_ratio > 0.7:
            score += 3
        elif vocab_ratio > 0.5:
            score += 2
        else:
            score += 1

    # No HTML/formatting artifacts (1-2 points)
    if not ('<' in text or '>' in text or '{' in text):
        score += 2

    # Proper sentences (1-2 points)
    if text.count('.') >= 1:  # At least one sentence
        score += 2

    return min(score, 10)  # Cap at 10
```

---

## Acceptance Criteria

### Minimum Quality Thresholds

**For Training Set:**
- Language purity: >98% Somali
- Duplicate rate: <1%
- Quality score: Average >7.5
- Label confidence: >95%

**For Validation/Test Sets:**
- Language purity: >99% Somali
- Duplicate rate: 0% (strict)
- Quality score: Average >8.0
- Label confidence: >98% (manually validated)

---

## Quality Guardrails

### Automatic Filters

1. **Remove if:**
   - Non-Somali language detected
   - Exact duplicate found
   - Text length <10 or >5000 characters
   - Quality score <5
   - Contains >20% numbers/special characters

2. **Flag for review if:**
   - Near-duplicate (>95% similarity)
   - Quality score 5-7
   - Label confidence <90%
   - Unusual character patterns

3. **Accept if:**
   - All validation checks pass
   - Quality score ≥7
   - No duplicates
   - Language = Somali

---

## Quality Reporting

### Metrics to Track

**Dataset-Level:**
- Total records
- Records passing validation (%)
- Average quality score
- Duplicate count
- Language distribution (% Somali)

**Per-Source:**
- Source name
- Records contributed
- Average quality score
- Duplicate rate
- Rejection rate

**Per-Dialect:**
- Dialect label
- Record count
- Average quality score
- Inter-annotator agreement

**Example Report:**
```
Dataset Quality Report - 2025-11-06

Total Records: 10,000
Passing Validation: 9,200 (92%)
Average Quality Score: 7.8/10
Duplicates Removed: 600 (6%)
Language Purity: 98.5% Somali

Per-Source Quality:
- Wikipedia: 8.5/10 (3,000 records)
- BBC Somali: 8.2/10 (2,500 records)
- Social Media: 6.9/10 (4,500 records, 30% rejected)

Per-Dialect Distribution:
- Northern: 5,500 (59.8%)
- Southern: 2,200 (23.9%)
- Central: 1,500 (16.3%)
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Data quality, data validation, quality checks
- Duplicates, deduplication, duplicate detection
- Quality metrics, quality score, quality standards
- Data cleaning, data filtering, guardrails
- Language detection, language purity
- Acceptance criteria, validation rules

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier
