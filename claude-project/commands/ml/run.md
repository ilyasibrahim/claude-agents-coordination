---
description: Orchestrate full ML pipeline run (data → train → deploy)
argument-hint: [experiment-name]
---

# ML Pipeline Run

Coordinate end-to-end ML workflow: data preparation → training → evaluation → deployment.

## Process

1. **Initialize Experiment**
   - Create experiment directory
   - Generate experiment ID
   - Log configuration

2. **Data Stage**
   - Invoke data-engineer to prepare/validate dataset
   - Check data quality metrics
   - Confirm data readiness

3. **Training Stage**
   - Invoke ml-orchestrator for model training
   - Track training metrics
   - Save model checkpoints

4. **Evaluation Stage**
   - Invoke ml-evaluator for performance assessment
   - Generate evaluation report
   - Compare to baseline/production

5. **Deployment Decision**
   - If metrics meet threshold → Deploy
   - If metrics below threshold → Report and stop
   - Create deployment report

6. **Update Registry**
   - Log experiment results
   - Update model registry
   - Create handoff for monitoring

## Arguments

- **$1**: Optional experiment name
  - Descriptive name for this run
  - If omitted: Generate timestamp-based name

## Examples

```bash
# Run with auto-generated name
/ml-run

# Run with specific experiment name
/ml-run xlm-r-fine-tune-v2

# Run with experiment description
/ml-run "test-augmented-training-data"
```

## Configuration

Create `ml_config.yaml` to customize:

```yaml
data:
  train_path: data/final/train.jsonl
  val_path: data/final/val.jsonl
  test_path: data/final/test.jsonl

model:
  name: xlm-roberta-base
  num_labels: 3
  max_length: 512

training:
  batch_size: 16
  learning_rate: 2e-5
  epochs: 5
  seed: 42

deployment:
  auto_deploy: false  # If true, auto-deploy if metrics met
  min_accuracy: 0.85
  min_f1: 0.82
```

## Output

- Experiment directory: `experiments/exp_[timestamp]/`
- Training logs: `experiments/exp_[timestamp]/logs/`
- Model artifacts: `experiments/exp_[timestamp]/model/`
- Evaluation report: `.claude/reports/implementation/ml-run-[date].md`

## Notes

- Runs lrl-nlp-techniques skill automatically (Somali-specific guidance)
- Creates comprehensive experiment report
- Updates model registry if deployment occurs
