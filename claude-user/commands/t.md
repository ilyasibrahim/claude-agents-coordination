---
description: Quick alias for /test - Run test suite with test-runner agent
allowed-tools: Bash(pytest:*, npm:test*)
argument-hint: [test suite]
---

# Test (Quick Alias)

Abbreviated command for `/test`. Execute test suite and report results.

## Usage

```bash
# Run all tests
/t

# Run unit tests only
/t unit

# Run specific test file
/t tests/test_model.py
```

## Notes

This is a shortcut for the full `/test` command. See `test.md` for complete documentation.
