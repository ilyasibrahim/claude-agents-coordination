---
name: model-evaluation-framework
description: Model evaluation metrics, testing protocols, and performance assessment for Somali dialect classification. Covers accuracy, F1-score, confusion matrix analysis, per-dialect performance, and evaluation best practices for multi-class classification tasks.
allowed-tools: Read, Grep
---

# Model Evaluation Framework

## Evaluation Metrics

### Primary Metrics

**Accuracy:**
- Overall correctness across all dialects
- Target: >85% for production
- Formula: (Correct Predictions) / (Total Predictions)

**Macro F1-Score:**
- Average F1 across all dialect classes
- Treats all dialects equally (good for imbalanced data)
- Target: >0.82

**Weighted F1-Score:**
- F1 weighted by class support
- Accounts for class imbalance
- Target: >0.85

### Per-Class Metrics

**Precision (per dialect):**
- Of predicted Northern, how many are actually Northern?
- Formula: True Positives / (True Positives + False Positives)

**Recall (per dialect):**
- Of actual Northern texts, how many did we find?
- Formula: True Positives / (True Positives + False Negatives)

**F1-Score (per dialect):**
- Harmonic mean of precision and recall
- Formula: 2 × (Precision × Recall) / (Precision + Recall)

---

## Evaluation Protocol

### Standard Evaluation

```python
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix
)

def evaluate_model(y_true, y_pred, dialect_names):
    """Comprehensive model evaluation"""

    # Overall metrics
    accuracy = accuracy_score(y_true, y_pred)

    # Per-class metrics
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, average=None, labels=range(len(dialect_names))
    )

    # Macro averages
    macro_f1 = f1.mean()

    # Detailed report
    report = classification_report(
        y_true, y_pred,
        target_names=dialect_names,
        digits=4
    )

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    return {
        'accuracy': accuracy,
        'macro_f1': macro_f1,
        'per_class': {
            dialect_names[i]: {
                'precision': precision[i],
                'recall': recall[i],
                'f1': f1[i],
                'support': support[i]
            }
            for i in range(len(dialect_names))
        },
        'report': report,
        'confusion_matrix': cm
    }
```

---

## Confusion Matrix Analysis

### Interpreting Results

**Example Confusion Matrix:**
```
               Predicted
           N    S    C
Actual N [[450  20   10]
       S [ 30 380   15]
       C [ 15  25  255]]
```

**Analysis:**
- Northern most accurately classified (93.8%)
- Southern confused with Northern in 7% of cases
- Central most challenging (86.4% accuracy)
- Northern rarely confused with Central (2%)

### Visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, dialect_names):
    """Visualize confusion matrix"""
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=dialect_names,
        yticklabels=dialect_names
    )
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Dialect Classification Confusion Matrix')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300)
```

---

## Cross-Validation

### K-Fold Strategy

```python
from sklearn.model_selection import StratifiedKFold
import numpy as np

def cross_validate_model(model, X, y, n_folds=5):
    """Stratified k-fold cross-validation"""
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)

    fold_scores = []

    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_train, X_val = X[train_idx], X[val_idx]
        y_train, y_val = y[train_idx], y[val_idx]

        # Train model
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_val)
        accuracy = accuracy_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred, average='macro')

        fold_scores.append({'accuracy': accuracy, 'f1': f1})
        print(f"Fold {fold + 1}: Accuracy={accuracy:.4f}, F1={f1:.4f}")

    # Report mean and std
    acc_mean = np.mean([s['accuracy'] for s in fold_scores])
    acc_std = np.std([s['accuracy'] for s in fold_scores])
    f1_mean = np.mean([s['f1'] for s in fold_scores])
    f1_std = np.std([s['f1'] for s in fold_scores])

    print(f"\nCross-Validation Results:")
    print(f"Accuracy: {acc_mean:.4f} ± {acc_std:.4f}")
    print(f"Macro F1: {f1_mean:.4f} ± {f1_std:.4f}")

    return fold_scores
```

---

## Performance Thresholds

### Minimum Acceptable Performance

**For Production Deployment:**
- Overall Accuracy: ≥85%
- Macro F1-Score: ≥0.82
- Per-Class F1: ≥0.75 for all dialects
- No class with recall <70%

**For Research/Experimental:**
- Overall Accuracy: ≥75%
- Macro F1-Score: ≥0.70
- Document performance gaps

---

## Error Analysis

### Qualitative Review

```python
def analyze_errors(X, y_true, y_pred, dialect_names, n_examples=10):
    """Identify and display misclassified examples"""
    errors = []

    for i in range(len(y_true)):
        if y_true[i] != y_pred[i]:
            errors.append({
                'text': X[i],
                'true_label': dialect_names[y_true[i]],
                'pred_label': dialect_names[y_pred[i]]
            })

    # Sample random errors for review
    import random
    sample_errors = random.sample(errors, min(n_examples, len(errors)))

    print(f"\nError Analysis ({len(errors)} total errors):\n")
    for idx, error in enumerate(sample_errors):
        print(f"Example {idx + 1}:")
        print(f"  Text: {error['text'][:100]}...")
        print(f"  True: {error['true_label']}, Predicted: {error['pred_label']}\n")

    return errors
```

---

## Baseline Comparison

### Establish Baselines

```python
# Majority class baseline
def majority_baseline(y_train, y_test):
    """Predict most frequent class"""
    from collections import Counter
    majority_class = Counter(y_train).most_common(1)[0][0]
    y_pred = [majority_class] * len(y_test)
    return accuracy_score(y_test, y_pred)

# Random baseline
def random_baseline(y_train, y_test):
    """Random predictions based on train distribution"""
    from collections import Counter
    class_dist = Counter(y_train)
    classes, counts = zip(*class_dist.items())
    probs = [c / sum(counts) for c in counts]

    y_pred = np.random.choice(classes, size=len(y_test), p=probs)
    return accuracy_score(y_test, y_pred)
```

**Report Format:**
```
Baseline Results:
- Random: 33.5% accuracy
- Majority: 58.2% accuracy
- Our Model: 87.3% accuracy ✓ (significantly better)
```

---

## Evaluation Report Template

```markdown
# Model Evaluation Report

**Model:** XLM-R Fine-Tuned for Somali Dialect Classification
**Date:** 2025-11-06
**Test Set Size:** 1,500 examples

## Overall Performance

| Metric | Value |
|--------|-------|
| Accuracy | 87.3% |
| Macro F1 | 0.852 |
| Weighted F1 | 0.871 |

## Per-Dialect Performance

| Dialect | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| Northern | 0.91 | 0.94 | 0.92 | 750 |
| Southern | 0.85 | 0.82 | 0.83 | 450 |
| Central | 0.81 | 0.79 | 0.80 | 300 |

## Confusion Matrix

[Insert visualization]

## Error Analysis

- Northern-Southern confusion: 3.2% of cases
- Most errors occur with short texts (<50 words)
- Informal/social media text more challenging

## Comparison to Baseline

- Majority class baseline: 50.0%
- Our model: 87.3%
- **Improvement: +37.3 percentage points**

## Recommendations

- Collect more Southern and Central dialect training data
- Investigate short text performance
- Consider ensemble approaches for difficult cases
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Model evaluation, model assessment, performance
- Accuracy, precision, recall, F1-score
- Confusion matrix, error analysis
- Cross-validation, k-fold
- Metrics, evaluation metrics
- Test set, validation set
- Per-class performance, per-dialect
- Baseline comparison

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier
