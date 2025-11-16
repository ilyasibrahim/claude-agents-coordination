---
name: code-review
description: Format for code review reports and pull request assessments
---

# Code Review Output Style

Use this format for code reviews, PR assessments, and quality evaluations.

## Template

```markdown
# Code Review: [PR Title or Scope]

**Reviewer:** [Agent Name]
**Date:** YYYY-MM-DD
**PR/Commit:** [PR number or commit hash]
**Overall Quality Score:** X.X/10.0

---

## Summary

[2-3 sentences summarizing the changes and overall assessment]

**Recommendation:** ✅ Approve | ⚠️ Approve with Comments | ❌ Request Changes

---

## Changes Overview

**Files Changed:** X files (+Y lines, -Z lines)

**Categories:**
- New Features: X files
- Bug Fixes: X files
- Refactoring: X files
- Tests: X files
- Documentation: X files

---

## Detailed Findings

### ✅ Strengths

**What's Done Well:**
1. [Positive aspect] - [Why it's good]
   ```[language]
   // Example of good code
   ```

2. [Another strength]
   ```[language]
   // Another good example
   ```

### ⚠️ Issues by Severity

#### 🔴 CRITICAL (Must Fix Before Merge)

**Issue 1: [Title]**
- **File:** `path/to/file.ext:line`
- **Problem:** [Description of the issue]
- **Impact:** [What could go wrong]
- **Fix:** [Specific recommendation]
  ```[language]
  // Current code
  const result = dangerousOperation();

  // Recommended fix
  const result = await safeOperation();
  ```

#### 🟡 HIGH (Should Fix)

**Issue 2: [Title]**
- **File:** `path/to/file.ext:line`
- **Problem:** [Description]
- **Impact:** [Consequences]
- **Fix:** [Recommendation]

#### 🟢 MEDIUM (Nice to Have)

**Issue 3: [Title]**
- **File:** `path/to/file.ext:line`
- **Problem:** [Description]
- **Fix:** [Recommendation]

#### 🔵 LOW (Nitpick/Style)

**Issue 4: [Title]**
- **File:** `path/to/file.ext:line`
- **Suggestion:** [Minor improvement]

---

## Quality Assessment

### Correctness ✅ / ⚠️ / ❌
- [ ] Logic is correct and handles edge cases
- [ ] No off-by-one errors or null pointer exceptions
- [ ] Proper error handling and validation
- [ ] Expected behavior matches implementation

**Score:** X/10
**Comments:** [Observations]

### Security ✅ / ⚠️ / ❌
- [ ] No SQL injection vulnerabilities
- [ ] No XSS or CSRF vulnerabilities
- [ ] Sensitive data properly protected
- [ ] Authentication/authorization correct

**Score:** X/10
**Comments:** [Observations]

### Performance ✅ / ⚠️ / ❌
- [ ] No N+1 queries or inefficient loops
- [ ] Efficient algorithms and data structures
- [ ] Proper caching where appropriate
- [ ] Acceptable resource usage

**Score:** X/10
**Comments:** [Observations]

### Maintainability ✅ / ⚠️ / ❌
- [ ] Clear, descriptive names
- [ ] Adequate comments for complex logic
- [ ] Follows DRY and SOLID principles
- [ ] Consistent with project conventions

**Score:** X/10
**Comments:** [Observations]

### Testing ✅ / ⚠️ / ❌
- [ ] Unit tests for new functions
- [ ] Integration tests for new features
- [ ] Edge cases covered
- [ ] Tests are maintainable

**Score:** X/10
**Test Coverage:** XX%

---

## Recommendations

### Required Changes
1. [Must-fix issue 1 summary]
2. [Must-fix issue 2 summary]

### Suggested Improvements
1. [Optional improvement 1]
2. [Optional improvement 2]

### Follow-Up Tasks
- [ ] Task 1 (create separate issue)
- [ ] Task 2 (address in next PR)

---

## Test Results

**Tests Run:** XX passed, YY failed
**Coverage:** XX% (target: 80%)

**Failed Tests:**
- `test_name_1` - [Reason]
- `test_name_2` - [Reason]

---

## Files Reviewed

| File | Lines | Status | Issues |
|------|-------|--------|--------|
| path/file1.py | +50, -10 | ✅ | 0 |
| path/file2.js | +100, -20 | ⚠️ | 2 |
| path/file3.css | +30, -5 | ✅ | 0 |

---

## Next Steps

**For Author:**
1. Address critical issues
2. Consider high-priority suggestions
3. Update tests as needed
4. Request re-review

**For Reviewer:**
- Available for questions/clarifications
- Will re-review after fixes

---

## References

- Related PR: #XXX
- Related Issue: #XXX
- Design Doc: [filename]
- Coding Standards: [link]
```

## Usage Guidelines

**Use this style for:**
- Pull request reviews
- Code quality assessments
- Pre-merge validation
- Post-implementation reviews

**Key Principles:**
- Start with summary and recommendation
- Categorize issues by severity (Critical → Low)
- Provide specific file:line references
- Include code examples for fixes
- Balance criticism with positive feedback
- Focus on high-impact issues first
- Be actionable and constructive

**Severity Definitions:**
- **CRITICAL**: Security, data loss, production breakage
- **HIGH**: Bugs, performance issues, maintainability problems
- **MEDIUM**: Code smells, minor bugs, improvements
- **LOW**: Style, formatting, nitpicks

**Review Checklist:**
- Correctness and logic
- Security vulnerabilities
- Performance implications
- Maintainability and clarity
- Test coverage
- Documentation

## Examples

**Good Code Review:**
- Clear severity categorization
- Specific file:line references
- Code examples for issues and fixes
- Balanced positive and constructive feedback
- Actionable recommendations

**Avoid:**
- Vague feedback ("this looks wrong")
- Missing code references
- Only negative feedback
- Nitpicking without impact assessment
- Missing fix recommendations
