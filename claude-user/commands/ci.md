---
description: Run local CI pipeline with lint, build, test, and security gates before pushing
---

# Local CI Pipeline

Run comprehensive CI gates locally before pushing code.

## Usage

```
/ci                    # Run all gates
/ci --quick           # Lint + build only
/ci --security        # All gates + extra security
```

## Pipeline Gates

Execute gates sequentially. Stop on first failure.

### Gate 1: Lint & Format

```bash
# Detect project type and run appropriate linter
if [ -f "package.json" ]; then
    npm run lint 2>/dev/null || npx eslint . --ext .js,.ts,.tsx
    npm run format:check 2>/dev/null || npx prettier --check .
fi

if [ -f "pyproject.toml" ] || [ -f "setup.py" ]; then
    ruff check . 2>/dev/null || python -m flake8 .
    black --check . 2>/dev/null || true
fi

if [ -f "go.mod" ]; then
    go fmt ./...
    golangci-lint run 2>/dev/null || true
fi
```

**Pass criteria:** No lint errors, code formatted

### Gate 2: Type Check

```bash
# TypeScript
if [ -f "tsconfig.json" ]; then
    npx tsc --noEmit
fi

# Python
if [ -f "pyproject.toml" ]; then
    mypy . 2>/dev/null || pyright . 2>/dev/null || true
fi
```

**Pass criteria:** No type errors

### Gate 3: Build

```bash
# Node.js
if [ -f "package.json" ]; then
    npm run build
fi

# Python
if [ -f "setup.py" ] || [ -f "pyproject.toml" ]; then
    pip install -e . 2>/dev/null || python -m build
fi

# Go
if [ -f "go.mod" ]; then
    go build ./...
fi

# Docker
if [ -f "Dockerfile" ]; then
    docker build -t ci-test .
fi
```

**Pass criteria:** Build succeeds without errors

### Gate 4: Test

```bash
# Node.js
if [ -f "package.json" ]; then
    npm test -- --coverage --passWithNoTests
fi

# Python
if [ -f "pytest.ini" ] || [ -f "pyproject.toml" ]; then
    pytest --cov --cov-fail-under=80 2>/dev/null || pytest
fi

# Go
if [ -f "go.mod" ]; then
    go test -cover ./...
fi
```

**Pass criteria:** Tests pass, coverage >= 80% (if enforced)

### Gate 5: Security Scan

```bash
# Node.js dependencies
if [ -f "package-lock.json" ]; then
    npm audit --audit-level=high
fi

# Python dependencies
if [ -f "requirements.txt" ]; then
    pip-audit 2>/dev/null || safety check 2>/dev/null || true
fi

# Secret detection
npx secretlint "**/*" 2>/dev/null || \
    gitleaks detect --source . 2>/dev/null || \
    trufflehog filesystem . 2>/dev/null || \
    echo "No secret scanner available - manual review required"
```

**Pass criteria:** No high/critical vulnerabilities, no secrets detected

### Gate 6: Documentation Check (Optional)

```bash
# API docs generated
if [ -f "package.json" ]; then
    npm run docs 2>/dev/null || true
fi

# Changelog updated (for releases)
if git diff --name-only HEAD~1 | grep -q "^src/"; then
    if ! git diff --name-only HEAD~1 | grep -qE "CHANGELOG|changelog"; then
        echo "Warning: Code changed but CHANGELOG not updated"
    fi
fi
```

**Pass criteria:** Docs generate (if applicable)

## Output Report

```markdown
# CI Pipeline Report

**Date:** YYYY-MM-DD HH:MM
**Branch:** [branch name]
**Commit:** [short hash]

## Gate Results

| Gate | Status | Duration | Notes |
|------|--------|----------|-------|
| Lint & Format | ✅ Pass | 5s | |
| Type Check | ✅ Pass | 8s | |
| Build | ✅ Pass | 45s | |
| Test | ✅ Pass | 30s | Coverage: 85% |
| Security | ⚠️ Warning | 12s | 2 moderate vulnerabilities |
| Docs | ✅ Pass | 3s | |

## Summary
- **Overall:** PASS (with warnings)
- **Total Duration:** 1m 43s
- **Ready to Push:** Yes

## Warnings
1. npm audit found 2 moderate vulnerabilities in dev dependencies
   - Run `npm audit fix` to resolve

## Next Steps
- [ ] Push to remote
- [ ] Create PR
- [ ] Request review
```

Output: `.claude/reports/ci/ci-[branch]-YYYYMMDD-HHMM.md`

## Gate Failure Handling

When a gate fails:

1. **Stop pipeline** - Don't run subsequent gates
2. **Report failure** - Clear error message with fix instructions
3. **Suggest fix** - Specific commands to resolve

Example failure output:

```markdown
## Gate 4: Test - FAILED ❌

### Error
3 tests failed in `src/auth/login.test.ts`

### Failures
1. `should validate email format` - Expected true, got false
2. `should reject weak passwords` - Timeout after 5000ms
3. `should handle rate limiting` - Missing mock

### Suggested Fixes
```bash
# Run failed tests with verbose output
npm test -- --testPathPattern="login.test" --verbose

# Run single test for debugging
npm test -- -t "should validate email format"
```

### Pipeline Stopped
Fix test failures before continuing.
```

## Quick Variants

### /ci --quick
Gates 1-3 only (lint, type check, build). Skip tests and security.

### /ci --security
All gates + additional security:
- SAST scan (semgrep, bandit)
- License compliance check
- Outdated dependency report

### /ci --fix
Attempt to auto-fix issues:
- `npm run lint -- --fix`
- `prettier --write .`
- `npm audit fix`
