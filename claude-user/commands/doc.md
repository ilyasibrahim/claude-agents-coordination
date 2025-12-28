---
description: Generate documentation with docs agent
allowed-tools: Read, Write, Edit, Grep, Glob
argument-hint: [type] [target]
---

# Generate Documentation

## Process

1. **Type:** Identify doc type (readme, api, architecture, guide)
2. **Context:** Read code, understand project structure
3. **Generate:** docs agent (mode: general or webdev)
4. **Validate:** Test code examples, verify accuracy

## Arguments

- `readme` - Project README.md
- `api` - API documentation
- `architecture` - Architecture docs
- `guide` - User guide
- `comments [path]` - Inline code comments

## Agent Mode Selection

- **general:** README, model cards, ADRs, guides
- **webdev:** React/Vue components, REST/GraphQL APIs, design system

## Examples

```bash
/doc readme
/doc api
/doc architecture
/doc comments src/models/
```
