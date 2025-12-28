# Somali Dialect Classifier - Project Instructions

## Project Context

- **Domain:** Low-resource NLP, Somali dialect classification
- **Architecture:** Python ML pipeline + static HTML/JS dashboard
- **Data Sources:** BBC Somali, Wikipedia, HuggingFace, TikTok, Spraakbanken
- **Dialects:** Northern (Standard), Southern (Af-Maay), Central

---

## User-Level Contract

This project follows the user-level agent-coordination protocol:

| Component | User Level Defines | Project Level Implements |
|-----------|-------------------|-------------------------|
| Report categories | 15 standard categories | Project-specific report content |
| Registry format | `_registry.md` structure | All project reports indexed |
| Tech debt tracking | `_tech-debt.md` format | Pipeline/dashboard debt tracked |
| Templates | `templates.md` formats | Project uses standard templates |
| Verification | `verify.sh` script | Applied to project reports |

---

## Project-Specific Skills

These skills auto-invoke based on context:

| Skill | Triggers On | Path |
|-------|-------------|------|
| `lrl-nlp-techniques` | Somali NLP, dialect classification, low-resource | `skills/machine-learning/lrl-nlp-techniques/` |
| `data-quality-standards` | Data validation, quality metrics, filtering | `skills/data-engineering/data-quality-standards/` |
| `etl-patterns` | Data pipeline, ingestion, processing | `skills/data-engineering/etl-patterns/` |
| `dashboard-patterns` | Dashboard UI, Chart.js, visualization | `skills/frontend/dashboard-patterns/` |

---

## Project Commands

| Command | Purpose | Agent |
|---------|---------|-------|
| `/data/analyze [file]` | Run EDA on dataset | data-analyst |
| `/ml/run [experiment]` | Execute full ML pipeline | ml-engineer |

---

## Report Locations

Follow user-level categories. Project-specific usage:

| Category | Project Usage | Examples |
|----------|---------------|----------|
| `analysis/` | Data exploration, EDA, quality reports | Dataset profiling, dialect distribution |
| `arch/` | ADRs, database decisions, system design | SQLite ledger ADR, pipeline architecture |
| `bugs/` | Pipeline failures, data issues, dashboard bugs | Module import errors, data corruption |
| `implementation/` | Pipeline implementation, processor updates | Processor implementations, feature additions |
| `design/` | Dashboard UX, visualization specs | Navigation flows, chart designs |
| `review/` | Code reviews, pipeline reviews | Processor code quality, dashboard review |
| `tests/` | Test results, QA reports | Pipeline tests, dashboard QA |
| `handoff/` | Agent coordination, context transfers | Feature handoffs, QA handoffs |
| `exec/` | Orchestration logs, command outputs | Full pipeline runs |
| `security/` | Data security, access audits | Data handling compliance |
| `sre/` | Pipeline reliability, incident analysis | Crawl failures, rate limiting |
| `rfc/` | Major feature proposals | New source integration RFCs |
| `ci/` | CI pipeline results | Build/test results |

---

## Key Files

| Path | Purpose |
|------|---------|
| `src/somali_dialect_classifier/` | Main source code |
| `src/somali_dialect_classifier/ingestion/` | Data ingestion pipeline |
| `src/somali_dialect_classifier/ingestion/processors/` | Source-specific processors |
| `data/ledger/crawl_ledger.db` | SQLite ingestion ledger |
| `data/manifests/` | Ingestion run manifests |
| `dashboard/` | Static HTML/JS dashboard |
| `dashboard/js/main.js` | Dashboard entry point |
| `dashboard/js/components/` | Dashboard UI components |

---

## Data Sources

| Source | Processor | Status |
|--------|-----------|--------|
| BBC Somali | `bbc_processor.py` | Active |
| Wikipedia | `wikipedia_processor.py` | Active |
| HuggingFace | `huggingface_processor.py` | Active |
| TikTok | `tiktok_processor.py` | Active |
| Spraakbanken | `sprakbanken_processor.py` | Active |

---

## Conventions

### Database
- **Ledger:** SQLite at `data/ledger/crawl_ledger.db` (per ADR 2025-11-14)
- **Deduplication:** File-level using content hash

### Testing
- **Framework:** pytest
- **Coverage target:** 80%
- **CI:** GitHub Actions

### Code Style
- **Python:** Black + isort + flake8
- **JavaScript:** Vanilla JS, no framework

### Data Processing
- **Processors:** One per data source in `ingestion/processors/`
- **Quality:** Gold schema defined, quality scoring applied
- **Output:** JSONL format for ML pipeline

---

## Tech Debt Priority

For this project, tech debt is prioritized as:

| Priority | Project Context |
|----------|-----------------|
| Critical | Data pipeline corruption, loss of data integrity |
| High | Pipeline failures blocking ingestion, dashboard outages |
| Medium | Code quality issues, slow processing |
| Low | Refactoring, documentation gaps |

---

## Quick Reference

```bash
# Run data analysis
/data/analyze data/processed/cleaned_data.jsonl

# Run ML pipeline
/ml/run xlm-r-experiment-v1

# Check project registry
cat .claude/reports/_registry.md | head -30

# Check project tech debt
cat .claude/reports/_tech-debt.md
```

---

**Version:** 1.0.0
**Created:** 2025-12-16
