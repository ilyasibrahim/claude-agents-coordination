---
name: mlops-best-practices
description: MLOps best practices for model versioning, experiment tracking, deployment, monitoring, and retraining workflows. Covers reproducibility, CI/CD for ML, model registry, and production ML system design.
allowed-tools: Read
---

# MLOps Best Practices

## Reproducibility

### Essential Elements

**1. Version Everything:**
- Code (Git)
- Data (DVC, hash checksums)
- Models (model registry with versioning)
- Environment (requirements.txt, Docker)
- Hyperparameters (config files, MLflow)

**2. Set Random Seeds:**
```python
import random
import numpy as np
import torch

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
```

**3. Document Dependencies:**
```bash
# requirements.txt
transformers==4.35.0
torch==2.1.0
pandas==2.1.3
scikit-learn==1.3.2
```

---

## Experiment Tracking

### Using MLflow

```python
import mlflow

def train_with_tracking(model, train_data, config):
    """Train model with experiment tracking"""

    with mlflow.start_run():
        # Log hyperparameters
        mlflow.log_params(config)

        # Train model
        model.fit(train_data)

        # Evaluate
        metrics = evaluate(model, val_data)

        # Log metrics
        mlflow.log_metrics(metrics)

        # Log model
        mlflow.sklearn.log_model(model, "model")

        # Log artifacts (plots, configs)
        mlflow.log_artifact("confusion_matrix.png")
```

### Experiment Organization

```
experiments/
├── exp_001_baseline/
│   ├── config.yaml
│   ├── results.json
│   └── model.pkl
├── exp_002_xlm_r/
│   ├── config.yaml
│   ├── results.json
│   └── model/
└── exp_003_ensemble/
    ├── config.yaml
    ├── results.json
    └── models/
```

---

## Model Versioning

### Model Registry Pattern

```python
class ModelRegistry:
    """Simple model registry"""

    def register_model(self, model, version, metrics, metadata):
        """Register new model version"""
        model_info = {
            'version': version,
            'metrics': metrics,
            'metadata': metadata,
            'timestamp': datetime.now().isoformat(),
            'status': 'staging'  # staging, production, archived
        }

        # Save model
        model_path = f'models/v{version}/'
        os.makedirs(model_path, exist_ok=True)
        torch.save(model.state_dict(), f'{model_path}/model.pt')

        # Save metadata
        with open(f'{model_path}/metadata.json', 'w') as f:
            json.dump(model_info, f, indent=2)

        return model_path

    def promote_to_production(self, version):
        """Promote model version to production"""
        # Update status
        metadata = self.load_metadata(version)
        metadata['status'] = 'production'
        metadata['production_timestamp'] = datetime.now().isoformat()

        # Save updated metadata
        self.save_metadata(version, metadata)

        # Update production symlink
        os.symlink(f'models/v{version}', 'models/production', exist_ok=True)
```

---

## Deployment Patterns

### Pattern 1: REST API

```python
from fastapi import FastAPI
import torch

app = FastAPI()

# Load production model
model = load_model('models/production/model.pt')
tokenizer = load_tokenizer('models/production/tokenizer')

@app.post("/predict")
def predict(text: str):
    """Predict dialect for input text"""
    # Preprocess
    inputs = tokenizer(text, return_tensors='pt')

    # Predict
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    dialect_names = ['Northern', 'Southern', 'Central']

    return {
        'text': text,
        'predicted_dialect': dialect_names[prediction],
        'model_version': get_model_version()
    }
```

### Pattern 2: Batch Processing

```python
def batch_predict(input_file, output_file, batch_size=32):
    """Process large files in batches"""
    model = load_model()

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        batch = []
        for line in f_in:
            batch.append(line.strip())

            if len(batch) == batch_size:
                predictions = model.predict(batch)
                for text, pred in zip(batch, predictions):
                    f_out.write(json.dumps({'text': text, 'prediction': pred}) + '\n')
                batch = []

        # Process remaining
        if batch:
            predictions = model.predict(batch)
            for text, pred in zip(batch, predictions):
                f_out.write(json.dumps({'text': text, 'prediction': pred}) + '\n')
```

---

## Monitoring

### Key Metrics to Track

**Model Performance:**
- Prediction accuracy (rolling window)
- Confidence scores distribution
- Prediction latency (p50, p95, p99)

**Data Drift:**
- Input text length distribution
- Vocabulary shift
- Character/word frequency changes

**System Health:**
- Request rate
- Error rate
- Resource utilization (CPU, memory, GPU)

### Monitoring Code

```python
import prometheus_client as prom

# Define metrics
prediction_counter = prom.Counter('predictions_total', 'Total predictions')
prediction_latency = prom.Histogram('prediction_latency_seconds', 'Prediction latency')
confidence_gauge = prom.Gauge('prediction_confidence', 'Average confidence')

@app.post("/predict")
@prediction_latency.time()
def predict(text: str):
    prediction_counter.inc()

    result = model.predict(text)

    confidence_gauge.set(result['confidence'])

    return result
```

---

## Retraining Workflow

### Trigger Conditions

**Schedule-Based:**
- Weekly/monthly retraining
- Ensures model stays current

**Performance-Based:**
- Accuracy drops below threshold (e.g., <82%)
- Trigger retraining automatically

**Data-Based:**
- New labeled data available (>1000 examples)
- Retrain to incorporate new information

### Retraining Pipeline

```python
def retraining_pipeline():
    """Automated retraining workflow"""

    # 1. Check trigger conditions
    if not should_retrain():
        return

    # 2. Fetch latest data
    train_data = fetch_training_data()

    # 3. Train new model
    new_model = train_model(train_data, config)

    # 4. Evaluate
    metrics = evaluate_model(new_model, test_data)

    # 5. Compare to production
    prod_metrics = get_production_metrics()
    if metrics['f1'] > prod_metrics['f1']:
        # 6. Register new version
        version = register_model(new_model, metrics)

        # 7. Deploy to staging
        deploy_to_staging(version)

        # 8. Run integration tests
        if run_tests(version):
            # 9. Promote to production
            promote_to_production(version)
        else:
            rollback(version)
```

---

## CI/CD for ML

### Testing Strategy

**Unit Tests:**
- Model loading/saving
- Preprocessing functions
- Prediction logic

**Integration Tests:**
- End-to-end prediction pipeline
- API endpoints
- Data pipeline

**Model Tests:**
- Minimum accuracy threshold
- Inference latency requirements
- Output format validation

```python
# tests/test_model.py
def test_model_accuracy():
    """Ensure model meets minimum accuracy"""
    model = load_model()
    test_data = load_test_data()

    accuracy = evaluate(model, test_data)

    assert accuracy >= 0.85, f"Accuracy {accuracy} below threshold"

def test_inference_latency():
    """Ensure predictions are fast enough"""
    model = load_model()
    text = "Sample Somali text for testing"

    start = time.time()
    model.predict(text)
    latency = time.time() - start

    assert latency < 0.5, f"Latency {latency}s exceeds 500ms threshold"
```

---

## Configuration Management

### Centralized Config

```yaml
# config/model_config.yaml
model:
  name: xlm-roberta-base
  num_labels: 3
  max_length: 512

training:
  batch_size: 16
  learning_rate: 2e-5
  epochs: 5
  warmup_steps: 500

data:
  train_path: data/final/train.jsonl
  val_path: data/final/val.jsonl
  test_path: data/final/test.jsonl

deployment:
  api_port: 8000
  batch_size: 32
  max_concurrent_requests: 100
```

---

## Model Cards

### Documentation Template

```markdown
# Model Card: Somali Dialect Classifier v2.0

## Model Details
- **Model Type:** Fine-tuned XLM-RoBERTa
- **Version:** 2.0
- **Date:** 2025-11-06
- **License:** MIT

## Intended Use
- **Primary Use:** Classify Somali text into dialects (Northern, Southern, Central)
- **Out-of-Scope:** Other languages, sentiment analysis

## Training Data
- **Size:** 10,000 labeled examples
- **Sources:** Wikipedia, BBC Somali, social media
- **Distribution:** Northern (60%), Southern (25%), Central (15%)

## Performance
- **Overall Accuracy:** 87.3%
- **Macro F1:** 0.852
- **Per-Dialect F1:** Northern (0.92), Southern (0.83), Central (0.80)

## Limitations
- Performance lower on short texts (<50 words)
- Informal/social media text more challenging
- Central dialect underrepresented in training

## Ethical Considerations
- May not represent all dialectal variations
- Performance may vary across geographic regions
- Should not be used for discriminatory purposes
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- MLOps, ML operations, production ML
- Model versioning, model registry
- Experiment tracking, MLflow, WandB
- Deployment, serving, API
- Monitoring, drift detection
- Retraining, model updates
- CI/CD for ML, ML pipelines
- Reproducibility, model cards

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier
