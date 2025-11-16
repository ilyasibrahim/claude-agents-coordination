---
description: Quick alias for /commit - Create git commit with Conventional Commits format
allowed-tools: Bash(git:*)
argument-hint: [optional message]
---

# Commit (Quick Alias)

Abbreviated command for `/commit`. Creates a git commit following Conventional Commits format.

## Usage

```bash
# Same as /commit
/c

# Same as /commit "fix(api): handle null response"
/c "fix(api): handle null response"
```

## Notes

This is a shortcut for the full `/commit` command. See `commit.md` for complete documentation.

**Quick Reference:**
- `feat`: New feature
- `fix`: Bug fix
- `chore`: Maintenance
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `perf`: Performance
