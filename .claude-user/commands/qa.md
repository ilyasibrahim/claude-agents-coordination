---
description: Perform comprehensive QA review with code-reviewer, test-runner, and qa-engineer
allowed-tools: Bash(pytest:*, npm:test*, git:*)
argument-hint: [scope]
---

# Quality Assurance Review

Perform comprehensive quality assurance review using code-reviewer, test-runner, and qa-engineer.

## Process

1. **Define Review Scope**
   - Full codebase review
   - Specific feature/module
   - Pull request review
   - Pre-release validation

2. **Execute QA Checks**
   - Invoke code-reviewer (security, correctness)
   - Run test-runner (all tests, coverage)
   - Use qa-engineer (strategy, test cases)
   - Check code coverage
   - Review for security vulnerabilities
   - Validate accessibility (for UI)
   - Check performance implications

3. **Generate QA Report**
   - Test results summary
   - Code quality assessment
   - Security findings
   - Performance analysis
   - Recommendations

4. **Track Issues**
   - Create bug reports for failures
   - Prioritize issues (critical/high/medium/low)
   - Create fix handoffs for developers

## Arguments

- **$1**: Review scope (optional, defaults to full)
  - `full` - Complete codebase QA
  - `pr [number]` - Pull request review
  - `feature [name]` - Specific feature review
  - `security` - Security-focused review
  - `performance` - Performance review

## Examples

```bash
# Full QA review
/qa full

# Review specific PR
/qa pr 234

# Feature-specific QA
/qa feature authentication

# Security-focused review
/qa security

# Performance review
/qa performance
```

## QA Checklist

### Testing
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] All e2e tests pass
- [ ] Code coverage ≥ 80%
- [ ] Edge cases covered

### Code Quality
- [ ] No code smells or anti-patterns
- [ ] Follows project conventions
- [ ] No unused variables/imports
- [ ] Clear variable/function names
- [ ] Adequate comments for complex logic

### Security
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] No CSRF vulnerabilities
- [ ] Sensitive data protected
- [ ] Authentication/authorization correct

### Performance
- [ ] No N+1 queries
- [ ] Efficient algorithms
- [ ] Proper caching
- [ ] No memory leaks
- [ ] Acceptable response times

### Accessibility (UI)
- [ ] WCAG AA compliant
- [ ] Keyboard navigation works
- [ ] Screen reader compatible
- [ ] Color contrast adequate
- [ ] ARIA labels present

## Output

**Test Results:**
- Pass/Fail counts
- Failure details with stack traces
- Coverage report

**Code Quality Report:**
- Quality score (1-10)
- Issues by severity
- Specific file:line references
- Recommended fixes

**Security Assessment:**
- Vulnerabilities found
- OWASP top 10 checks
- Security best practices validation

**Performance Analysis:**
- Slow queries/functions identified
- Optimization opportunities
- Resource usage metrics

## Notes

- Uses code-reviewer + test-runner + qa-engineer for comprehensive review
- Generates detailed QA report in `.claude/reports/tests/`
- Creates bug reports for failures
- Prioritizes issues by severity
- Provides actionable recommendations
