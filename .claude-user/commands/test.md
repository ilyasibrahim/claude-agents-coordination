---
description: Run tests with test-runner agent
allowed-tools: Bash(pytest:*, npm:test*)
argument-hint: [test suite]
---

# Run Tests

Execute test suite and report results.

## Process

1. **Determine Test Scope**
   - If argument provided: Run specific test suite
   - If no argument: Run full test suite

2. **Execute Tests**
   - Python: `pytest [path] -v`
   - JavaScript: `npm test [pattern]`
   - Display results in real-time

3. **Report Results**
   - Total tests run
   - Passed/Failed/Skipped
   - Failure details
   - Coverage metrics (if available)

4. **Create Test Report**
   - Save to `.claude/reports/tests/`
   - Include: timestamp, results, failures, recommendations

## Arguments

- **$1**: Optional test suite specifier
  - `unit` - Run unit tests only
  - `integration` - Run integration tests
  - `e2e` - Run end-to-end tests
  - Specific file/pattern
  - If omitted: Run all tests

## Examples

```bash
# Run all tests
/test

# Run unit tests only
/test unit

# Run integration tests
/test integration

# Run specific test file
/test tests/test_model.py
```

## Test Commands by Type

**Python (pytest):**
```bash
# All tests
pytest

# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# With coverage
pytest --cov=src --cov-report=html
```

**JavaScript (Jest/Vitest):**
```bash
# All tests
npm test

# Watch mode
npm test -- --watch

# Coverage
npm test -- --coverage
```

## Notes

- Fails if any tests fail
- Generates coverage report if configured
- Creates test report in reports directory
