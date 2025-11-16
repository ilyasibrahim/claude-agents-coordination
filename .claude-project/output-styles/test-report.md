---
name: test-report
description: Format for test execution reports and QA validation results
---

# Test Report Output Style

Use this format for test execution reports, QA validation, and test coverage analysis.

## Template

```markdown
# Test Report: [Test Suite or Feature Name]

**Tester:** [Agent Name]
**Date:** YYYY-MM-DD
**Test Scope:** [Unit | Integration | E2E | Full Suite]
**Test Environment:** [Development | Staging | Production]

---

## Executive Summary

**Overall Result:** ✅ PASS | ⚠️ PASS WITH ISSUES | ❌ FAIL

**Test Statistics:**
- **Total Tests:** XXX
- **Passed:** XXX (XX%)
- **Failed:** XX (XX%)
- **Skipped:** XX (XX%)
- **Duration:** X minutes Y seconds

**Verdict:** [1-2 sentences on overall quality and readiness]

**Recommendation:** ✅ Approve for Deployment | ⚠️ Fix Issues First | ❌ Major Problems - Block Release

---

## Test Results Summary

### Pass Rate by Category

| Category | Total | Passed | Failed | Skipped | Pass Rate |
|----------|-------|--------|--------|---------|-----------|
| Unit Tests | 250 | 248 | 2 | 0 | 99.2% |
| Integration Tests | 80 | 75 | 5 | 0 | 93.8% |
| E2E Tests | 30 | 28 | 2 | 0 | 93.3% |
| **TOTAL** | **360** | **351** | **9** | **0** | **97.5%** |

### Test Coverage

| Component | Line Coverage | Branch Coverage | Function Coverage |
|-----------|---------------|-----------------|-------------------|
| src/classifier/ | 92% | 85% | 95% |
| src/pipeline/ | 88% | 80% | 90% |
| src/api/ | 95% | 90% | 98% |
| **OVERALL** | **91%** | **84%** | **94%** |

**Coverage Target:** 80% minimum
**Status:** ✅ Target Met

---

## Failed Tests Detail

### 🔴 CRITICAL FAILURES (Block Release)

#### Test 1: `test_authentication_with_invalid_token`
- **File:** `tests/integration/test_auth.py:line 45`
- **Category:** Integration
- **Error:**
  ```
  AssertionError: Expected 401 Unauthorized, got 200 OK
  ```
- **Root Cause:** Authentication middleware not validating expired tokens
- **Impact:** HIGH - Security vulnerability
- **Fix Required:** Implement token expiration validation in auth middleware
- **File to Fix:** `src/auth/middleware.py:line 78`
- **Estimated Fix Time:** 30 minutes

#### Test 2: `test_data_pipeline_handles_duplicates`
- **File:** `tests/unit/test_pipeline.py:line 123`
- **Category:** Unit
- **Error:**
  ```
  AssertionError: Expected 1000 records, got 1250 records
  ```
- **Root Cause:** Deduplication logic not applied correctly
- **Impact:** HIGH - Data quality issue
- **Fix Required:** Apply deduplication before final output
- **File to Fix:** `src/pipeline/processor.py:line 234`
- **Estimated Fix Time:** 45 minutes

### 🟡 HIGH PRIORITY FAILURES

#### Test 3: `test_dashboard_performance_under_load`
- **File:** `tests/e2e/test_dashboard.py:line 89`
- **Category:** E2E
- **Error:**
  ```
  TimeoutError: Page load exceeded 5000ms threshold (actual: 7200ms)
  ```
- **Root Cause:** Inefficient database query in metrics endpoint
- **Impact:** MEDIUM - Performance degradation
- **Fix Required:** Optimize query with proper indexing
- **File to Fix:** `src/api/routes/metrics.py:line 56`
- **Estimated Fix Time:** 1 hour

### 🟢 MEDIUM PRIORITY FAILURES

[Additional failures with lower severity]

---

## Test Execution Details

### Unit Tests (250 total)

**Passed:** 248/250 (99.2%)
**Duration:** 2 minutes 15 seconds

**Failed Tests:**
1. `test_data_pipeline_handles_duplicates` - See detail above
2. `test_quality_score_calculation` - Rounding error in edge case

**Skipped:** None

### Integration Tests (80 total)

**Passed:** 75/80 (93.8%)
**Duration:** 5 minutes 30 seconds

**Failed Tests:**
1. `test_authentication_with_invalid_token` - See detail above
2. `test_api_rate_limiting` - Rate limiter not enforcing correctly
3. `test_database_transaction_rollback` - Connection pool issue
4. `test_file_upload_large_files` - Timeout on 100MB file
5. `test_cache_invalidation` - Redis connection intermittent

**Skipped:** None

### End-to-End Tests (30 total)

**Passed:** 28/30 (93.3%)
**Duration:** 8 minutes 45 seconds

**Failed Tests:**
1. `test_dashboard_performance_under_load` - See detail above
2. `test_complete_user_flow` - Element not clickable (flaky test)

**Skipped:** None

---

## Test Quality Analysis

### Code Coverage

**Coverage Trend:**
- Previous run: 89%
- Current run: 91%
- **Change:** +2% ✅

**Uncovered Areas:**
- Error handling in `src/classifier/error_handlers.py` (45% coverage)
- Edge cases in `src/pipeline/validators.py` (60% coverage)

**Recommendation:** Add tests for error scenarios

### Test Stability

**Flaky Tests Identified:**
- `test_complete_user_flow` - Intermittent failures (3/10 runs)
- `test_cache_invalidation` - Redis connection issues (2/10 runs)

**Recommendation:** Investigate and stabilize flaky tests

### Test Performance

| Test Suite | Duration | Change from Previous |
|-------------|----------|---------------------|
| Unit | 2m 15s | +10s ⚠️ |
| Integration | 5m 30s | -15s ✅ |
| E2E | 8m 45s | +30s ⚠️ |
| **TOTAL** | **16m 30s** | **+25s** |

**Target:** <20 minutes
**Status:** ✅ Within target

---

## Browser/Platform Testing (E2E Only)

| Browser | Version | Status | Failed Tests |
|---------|---------|--------|--------------|
| Chrome | 130 | ✅ PASS | 0 |
| Firefox | 120 | ✅ PASS | 0 |
| Safari | 17 | ⚠️ ISSUES | 1 |
| Edge | 130 | ✅ PASS | 0 |

**Safari Issue:**
- `test_chart_rendering` - Chart.js not loading properly

---

## Security & Accessibility Tests

### Security Tests

- [x] SQL Injection Prevention: **PASS**
- [x] XSS Prevention: **PASS**
- [ ] CSRF Protection: **FAIL** (Test 1 above)
- [x] Authentication: **FAIL** (Test 1 above)
- [x] Authorization: **PASS**
- [x] Sensitive Data Encryption: **PASS**

**Security Score:** 4/6 tests passing (67%) ⚠️

### Accessibility Tests (WCAG AA)

- [x] Keyboard Navigation: **PASS**
- [x] Screen Reader Compatibility: **PASS**
- [x] Color Contrast: **PASS** (4.5:1 minimum)
- [x] ARIA Labels: **PASS**
- [x] Focus Indicators: **PASS**

**Accessibility Score:** 5/5 tests passing (100%) ✅

---

## Regression Analysis

### Comparison with Previous Run

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Pass Rate | 96.8% | 97.5% | +0.7% ✅ |
| Coverage | 89% | 91% | +2% ✅ |
| Duration | 16m 5s | 16m 30s | +25s ⚠️ |
| Failed Tests | 12 | 9 | -3 ✅ |

**Trend:** ✅ Improving

### New Failures (Not in Previous Run)
- None

### Fixed Since Last Run
- `test_pipeline_error_handling` (previously failing)
- `test_api_response_format` (previously failing)
- `test_dashboard_data_loading` (previously failing)

---

## Recommendations

### Critical Actions (Before Deployment)
1. **Fix authentication token validation** (Test 1)
   - Priority: CRITICAL
   - Estimated: 30 minutes
   - Assignee: Backend team

2. **Fix deduplication logic** (Test 2)
   - Priority: CRITICAL
   - Estimated: 45 minutes
   - Assignee: Data engineering team

### High Priority Actions
1. **Optimize dashboard query** (Test 3)
   - Priority: HIGH
   - Estimated: 1 hour
   - Assignee: Backend team

2. **Stabilize flaky tests**
   - Priority: HIGH
   - Estimated: 2 hours
   - Assignee: QA team

### Improvements
1. Increase coverage in error handlers (target: 80%)
2. Add performance benchmarks to CI
3. Investigate Safari compatibility issue

---

## Test Environment

**System:**
- OS: Ubuntu 22.04 LTS
- Python: 3.11.5
- Node.js: 20.10.0
- Database: PostgreSQL 15.4
- Cache: Redis 7.0

**Configuration:**
- Test Database: `test_database`
- Test User: `test_user`
- Environment: `testing`
- Debug Mode: Enabled

---

## Artifacts

**Test Output Files:**
- Coverage Report: `htmlcov/index.html`
- JUnit XML: `test-results.xml`
- Screenshots (E2E failures): `screenshots/`
- Logs: `logs/test-run-20251106.log`

**Commands to Reproduce:**
```bash
# Run all tests
pytest --cov=src --cov-report=html

# Run failed tests only
pytest --lf

# Run specific test
pytest tests/integration/test_auth.py::test_authentication_with_invalid_token -v
```

---

## Sign-Off

**Tested By:** [Agent Name]
**Date:** YYYY-MM-DD
**Status:** ⚠️ CONDITIONAL PASS - Fix 2 critical issues before deployment

**Next Steps:**
1. Development team fixes critical failures
2. Re-run test suite after fixes
3. Verify all tests pass
4. Approve for deployment
```

## Usage Guidelines

**Use this style for:**
- Test execution reports
- QA validation results
- Coverage analysis
- Regression testing reports

**Key Principles:**
- Start with executive summary and verdict
- Provide detailed failure analysis with root causes
- Include specific fix recommendations with estimates
- Show test quality metrics (coverage, stability, performance)
- Compare with previous runs (regression analysis)
- Document test environment for reproducibility
- Provide reproduction commands

**Severity Definitions:**
- **CRITICAL**: Blocks release, security issues, data corruption
- **HIGH**: Significant bugs, performance issues, functionality broken
- **MEDIUM**: Minor bugs, edge cases, non-critical features
- **LOW**: Cosmetic issues, flaky tests, minor improvements

**Pass Criteria:**
- Unit tests: ≥95% pass rate
- Integration tests: ≥90% pass rate
- E2E tests: ≥85% pass rate
- Coverage: ≥80%
- No critical failures

## Examples

**Good Test Report:**
- Clear pass/fail verdict upfront
- Detailed failure analysis with fixes
- Coverage metrics with trends
- Regression comparison
- Actionable recommendations
- Reproduction instructions

**Avoid:**
- Missing root cause analysis
- No fix recommendations
- Ignoring flaky tests
- Missing coverage data
- No comparison with previous runs
- Unclear verdict
