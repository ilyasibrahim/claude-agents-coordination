---
description: Run tests with test-engineer agent
allowed-tools: Bash(pytest:*, npm:test*)
argument-hint: [test suite]
---

# Run Tests

## Process

1. **Scope:** Argument → specific suite | None → full test suite
2. **Execute:** Python (`pytest`) or JavaScript (`npm test`)
3. **Report:** Results + coverage in `.claude/reports/tests/`

## Arguments

- `unit` - Unit tests only
- `integration` - Integration tests
- `e2e` - End-to-end tests
- `[path]` - Specific file/pattern
- None - Full suite

## Examples

```bash
/test                      # All tests
/test unit                 # Unit tests
/test tests/test_api.py    # Specific file
```
