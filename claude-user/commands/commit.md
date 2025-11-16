---
description: Create a git commit with Conventional Commits format
allowed-tools: Bash(git:*)
argument-hint: [optional message]
---

# Create Git Commit

Stage changes and create a commit following the Conventional Commits format.

## Process

1. **Review Changes**
   - Run `git status` to see all untracked/modified files
   - Run `git diff` for staged changes
   - Run `git diff HEAD` for all uncommitted changes

2. **Analyze Changes**
   - Identify the nature of changes (feat, fix, chore, docs, style, refactor, test)
   - Determine appropriate scope (component, module, or feature affected)
   - Draft concise commit message focusing on "why", not "what"

3. **Draft Commit Message**
   Format: `type(scope): message`

   **Types:**
   - `feat`: New feature
   - `fix`: Bug fix
   - `chore`: Maintenance (deps, config)
   - `docs`: Documentation
   - `style`: Formatting, styling
   - `refactor`: Code restructuring
   - `test`: Adding/updating tests
   - `perf`: Performance improvement

   **CRITICAL - Commit Body Rules:**
   - Keep body MINIMAL and professional
   - ONLY add body if truly needed for context
   - Use bullet points (max 2-3 bullets)
   - Each bullet: one line, concise benefit/reason
   - NO verbose explanations or implementation details
   - NO obvious statements about what code does
   - Focus on WHY and business impact, not HOW

   **Good Commit Examples:**
   ```
   chore(deps): bump fastapi from 0.95.0 to 0.110.0
   ```

   ```
   chore(ci): add caching to GitHub Actions workflows
     - Improves build time by reusing previously installed dependencies.
     - Closes #83.
   ```

   **Bad Commit Examples:**
   ```
   update stuff
   chore: changed files and fixed some things
   feat(api): add new endpoint
     - This commit adds a new endpoint to handle user authentication
     - The endpoint validates credentials and returns a token
     - It uses bcrypt for password hashing
     - Error handling has been implemented for invalid requests
   ```

4. **Stage Files**
   - Use `git add <file>` for specific files
   - Skip files that shouldn't be committed (.env, credentials, etc.)
   - Warn if sensitive files detected

5. **Create Commit**

   **Prefer single-line commits when possible:**
   ```bash
   git commit -m "type(scope): concise message"
   ```

   **Only add body if essential (use heredoc for multi-line):**
   ```bash
   git commit -m "$(cat <<'EOF'
   type(scope): concise message
     - Concise benefit or reason (one line).
     - Closes #123.
   EOF
   )"
   ```

   **Remember:**
   - Most commits should be single-line
   - Body should be 0-3 bullet points maximum
   - Each bullet: one line, no fluff

6. **Verify**
   - Run `git status` to confirm commit succeeded
   - Run `git log -1` to view the commit

## Arguments

- **$ARGUMENTS**: Optional commit message override
  - If provided, use as commit message directly
  - If not provided, analyze changes and draft message

## Examples

```bash
# Auto-generate commit message
/commit

# Use provided message
/commit "fix(api): handle null response from data source"
```

## Notes

- **Commit body discipline**: Default to single-line commits. Only add body for truly important context (bug fixes with issue numbers, non-obvious reasons)
- Never commit files containing secrets or credentials
- Ensure commit message is specific and descriptive
- Follow project's existing commit message style (check git log)
- **NO verbose commit bodies**: Avoid explaining implementation details or obvious changes
- DO NOT include tool attribution in commit message
