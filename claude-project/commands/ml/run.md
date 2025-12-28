---
description: Orchestrate full ML pipeline run (data → train → evaluate → deploy)
argument-hint: [experiment-name]
---

# ML Pipeline Run

Coordinate end-to-end ML workflow following user-level agent-coordination protocol.

## Workflow

Follows user-level agent-coordination protocol:

1. **Check Registry** - Look for prior ML runs, baseline metrics
2. **Context Injection** - Provide prior experiment results to agents
3. **Sequential Execution** - Data → Train → Evaluate (with verification)
4. **Update Registries** - Add report to `_registry.md`, tech debt if issues found

## Process

1. **Initialize Experiment**
   - Create experiment directory
   - Generate experiment ID
   - Log configuration

2. **Data Stage** (data-analyst agent)
   - Validate dataset quality (invokes data-quality-standards)
   - Check data readiness
   - Report data issues to tech debt if found

3. **Training Stage** (ml-trainer agent)
   - Train model (invokes lrl-nlp-techniques for Somali-specific guidance)
   - Track training metrics
   - Save model checkpoints

4. **Evaluation Stage** (ml-evaluator agent)
   - Assess model performance
   - Compare to baseline/production
   - Generate evaluation report

5. **Deployment Decision**
   - If metrics meet threshold → Proceed to deploy
   - If metrics below threshold → Report and document tech debt
   - Create deployment report

6. **Update Registries**
   - Add to `_registry.md`: experiment summary
   - Add to `_tech-debt.md`: any deferred improvements

## Arguments

- **$1**: Optional experiment name
  - Descriptive name for this run
  - If omitted: Generate timestamp-based name

## Examples

```bash
# Run with auto-generated name
/ml/run

# Run with specific experiment name
/ml/run xlm-r-fine-tune-v2

# Run with experiment description
/ml/run "test-augmented-training-data"
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

**Report Location:** `.claude/reports/implementation/impl-ml-run-[experiment]-YYYYMMDD.md`

**Artifacts:**
- Experiment directory: `experiments/exp_[timestamp]/`
- Training logs: `experiments/exp_[timestamp]/logs/`
- Model artifacts: `experiments/exp_[timestamp]/model/`

## Skills Invoked

- `lrl-nlp-techniques` - Somali-specific NLP guidance
- `data-quality-standards` - Data validation before training
- `mlops-best-practices` - Training/deployment patterns

## Registry Updates

After completion, add to `.claude/reports/_registry.md`:
```
- impl-ml-run-[experiment]-YYYYMMDD | Complete | [metrics summary]
```

If issues found, add to `.claude/reports/_tech-debt.md`:
```
- [ ] **TD-NNN**: [Issue description]
  - **Impact:** [Priority]
  - **Source:** impl-ml-run-[experiment]-YYYYMMDD.md
```
