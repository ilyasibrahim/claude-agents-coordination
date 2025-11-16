---
description: Review code quality with code-quality agent
allowed-tools: Bash(git:*)
argument-hint: [path]
---

# Code Review

Launch code-quality agent to review code for quality, best practices, potential bugs, and improvements.

## Process

1. **Determine Scope**
   - If path provided: Review specific file/directory
   - If no path: Review recent changes (git diff)

2. **Gather Context**
   - Run `git diff` to see uncommitted changes
   - Run `git log -5 --oneline` to see recent commits
   - Identify files to review

3. **Launch Code Quality Agent**
   - Invoke code-quality agent with scope
   - Agent will perform comprehensive review:
     - Correctness & logic
     - Security vulnerabilities
     - Performance & efficiency
     - Code quality & maintainability
     - Best practices
     - Documentation

4. **Report Findings**
   - Critical issues (must fix)
   - Suggestions for improvement
   - Positive observations
   - Questions/clarifications

## Arguments

- **$1**: Optional path to review
  - File: `src/pipeline/etl.py`
  - Directory: `src/models/`
  - If omitted: Review recent changes

## Examples

```bash
# Review recent uncommitted changes
/review

# Review specific file
/review src/models/model.py

# Review entire directory
/review src/pipeline/
```

## Notes

- Creates review report in `.claude/reports/review/`
- Automatically checks agent memory protocol
- Reviews follow project coding standards
