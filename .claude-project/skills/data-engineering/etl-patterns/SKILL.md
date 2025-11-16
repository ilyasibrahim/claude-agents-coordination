---
name: etl-patterns
description: ETL workflow patterns, data pipeline architecture, and ingestion strategies for Somali dialect classifier. Covers source integration, transformation logic, staging patterns, and load strategies. Auto-invokes when discussing data pipelines, ETL, ingestion workflows, or data processing architecture.
allowed-tools: Read, Grep
---

# ETL Patterns for Somali Dialect Classifier

## Pipeline Architecture

### Three-Stage Design

**1. Extract (Raw Layer)**
- Fetch data from multiple sources
- Store raw, unmodified data
- Maintain source provenance
- Location: `data/raw/[source-name]/`

**2. Transform (Staging/Silver Layer)**
- Clean and validate data
- Apply quality filters
- Normalize format
- Location: `data/staging/` or `data/processed/`

**3. Load (Gold Layer)**
- Prepare for model training
- Split into train/val/test
- Export to final format
- Location: `data/final/` or `data/gold/`

---

## Extract Patterns

### Source Integration

**Pattern 1: Web Scraping (Wikipedia, News)**
```python
def extract_from_web(url, source_name):
    """Extract text from web sources"""
    raw_data = fetch_url(url)
    save_raw(raw_data, f'data/raw/{source_name}/')
    return raw_data
```

**Pattern 2: API Integration (HuggingFace, Språkbanken)**
```python
def extract_from_api(endpoint, api_key, source_name):
    """Extract from external API"""
    response = requests.get(endpoint, headers={'Authorization': api_key})
    save_raw(response.json(), f'data/raw/{source_name}/')
    return response.json()
```

**Pattern 3: File Upload (Manual Datasets)**
```python
def extract_from_file(file_path, source_name):
    """Extract from uploaded files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = f.read()
    save_raw(raw_data, f'data/raw/{source_name}/')
    return raw_data
```

---

## Transform Patterns

### Pattern 1: Cleaning Pipeline

```python
def transform_text(raw_text):
    """Standard cleaning pipeline"""
    # 1. Remove HTML tags
    text = remove_html_tags(raw_text)

    # 2. Normalize whitespace
    text = ' '.join(text.split())

    # 3. Remove URLs
    text = remove_urls(text)

    # 4. Normalize Unicode
    text = text.encode('utf-8').decode('utf-8')

    return text
```

### Pattern 2: Validation & Filtering

```python
def validate_and_filter(records):
    """Apply quality guardrails"""
    validated = []
    for record in records:
        # Language detection
        if not is_somali(record['text']):
            continue

        # Quality scoring
        score = compute_quality_score(record['text'])
        if score < 5:
            continue

        # Duplicate detection
        if is_duplicate(record['text'], validated):
            continue

        validated.append(record)

    return validated
```

### Pattern 3: Enrichment

```python
def enrich_record(record):
    """Add metadata and features"""
    record['word_count'] = len(record['text'].split())
    record['char_count'] = len(record['text'])
    record['quality_score'] = compute_quality_score(record['text'])
    record['ingestion_timestamp'] = datetime.now().isoformat()
    return record
```

---

## Load Patterns

### Pattern 1: Train/Val/Test Split

```python
def create_splits(data, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    """Stratified split by dialect"""
    from sklearn.model_selection import train_test_split

    # First split: train vs. (val + test)
    train, temp = train_test_split(
        data,
        train_size=train_ratio,
        stratify=data['label'],
        random_state=42
    )

    # Second split: val vs. test
    val, test = train_test_split(
        temp,
        train_size=val_ratio/(val_ratio + test_ratio),
        stratify=temp['label'],
        random_state=42
    )

    return train, val, test
```

### Pattern 2: Export to Model Format

```python
def export_for_training(data, output_path):
    """Export to format expected by model"""
    # Option 1: JSON Lines
    with open(f'{output_path}/data.jsonl', 'w') as f:
        for record in data:
            f.write(json.dumps(record) + '\n')

    # Option 2: CSV
    df = pd.DataFrame(data)
    df.to_csv(f'{output_path}/data.csv', index=False)

    # Option 3: Parquet (efficient for large datasets)
    df.to_parquet(f'{output_path}/data.parquet')
```

---

## Incremental Processing

### Pattern: Delta Load

```python
def incremental_etl(source, last_run_timestamp):
    """Process only new data since last run"""
    # 1. Extract new records
    new_records = extract_since(source, last_run_timestamp)

    # 2. Transform
    transformed = transform_batch(new_records)

    # 3. Append to existing dataset
    append_to_dataset(transformed, 'data/processed/dataset.jsonl')

    # 4. Update last run timestamp
    update_last_run(source, datetime.now())
```

---

## Error Handling

### Pattern: Robust Pipeline

```python
def robust_etl_pipeline(sources):
    """ETL with error handling and logging"""
    results = {'success': [], 'failed': []}

    for source in sources:
        try:
            # Extract
            raw_data = extract(source)
            log_info(f"Extracted {len(raw_data)} records from {source['name']}")

            # Transform
            transformed = transform(raw_data)
            log_info(f"Transformed {len(transformed)} records")

            # Load
            load(transformed, source['name'])
            log_info(f"Loaded {len(transformed)} records")

            results['success'].append(source['name'])

        except Exception as e:
            log_error(f"Failed to process {source['name']}: {str(e)}")
            results['failed'].append((source['name'], str(e)))

    return results
```

---

## Monitoring & Logging

### Key Metrics to Track

**Per-Source:**
- Records extracted
- Records transformed (after filtering)
- Records loaded
- Processing time
- Error rate

**Overall Pipeline:**
- Total records processed
- Average quality score
- Duplicate rate
- Language purity
- Processing throughput (records/second)

**Example Log:**
```
[2025-11-06 19:00:00] INFO: Starting ETL pipeline
[2025-11-06 19:00:15] INFO: Wikipedia - Extracted 5,000 records
[2025-11-06 19:00:45] INFO: Wikipedia - Transformed 4,800 records (200 filtered)
[2025-11-06 19:01:00] INFO: Wikipedia - Loaded 4,800 records
[2025-11-06 19:01:05] INFO: BBC Somali - Extracted 2,500 records
[2025-11-06 19:01:25] INFO: BBC Somali - Transformed 2,450 records (50 filtered)
[2025-11-06 19:01:35] INFO: BBC Somali - Loaded 2,450 records
[2025-11-06 19:01:40] INFO: Pipeline completed: 7,250 records loaded
```

---

## Directory Structure

```
data/
├── raw/                    # Unprocessed source data
│   ├── wikipedia/
│   ├── bbc-somali/
│   ├── huggingface/
│   └── sprakbanken/
│
├── staging/                # Cleaned, validated data
│   └── cleaned_data.jsonl
│
├── processed/              # Deduplicated, enriched data
│   └── processed_data.jsonl
│
└── final/                  # Train/val/test splits
    ├── train.jsonl
    ├── val.jsonl
    └── test.jsonl
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- ETL, data pipeline, ingestion, data processing
- Extract, transform, load
- Data workflow, pipeline architecture
- Source integration, data sources
- Staging, intermediate processing
- Train/val/test split, data export
- Incremental processing, delta load
- Pipeline monitoring, logging

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier
