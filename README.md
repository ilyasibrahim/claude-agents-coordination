# Claude Code Agents Coordination

Tiered multi-agent coordination + delegation patterns for Claude Code, with **institutional memory** (work registry) and **explicit tech-debt tracking**.

This repo ships two layers you can reuse across projects:

- `claude-user/` → copy into `~/.claude/` (standard agents, skills, commands)
- `claude-project/` → copy into `<project>/.claude/` (project context, registries, report folders, project skills/commands)

---

## Quick Start

### 1) Install user-level config

```bash
mkdir -p ~/.claude
rsync -a claude-user/ ~/.claude/
```

### 2) Install project-level config (per project)

```bash
mkdir -p /path/to/your-project/.claude
rsync -a claude-project/ /path/to/your-project/.claude/
```

Then edit `/path/to/your-project/.claude/CLAUDE.md` with your project context.

---

## Core Ideas

- **4-step protocol:** Registry → Context injection → Sequencing → Verification
- **Two registries:**
  - `.claude/reports/_registry.md` tracks what was done (reports)
  - `.claude/reports/_tech-debt.md` tracks what was deferred (debt items with sources)
- **Multi-level review chain:** `/review-full` can escalate peer → architecture → security → reliability based on changes.

---

## What’s Inside

- `claude-user/INDEX.md` — tiered agent set + standard workflows
- `claude-project/INDEX.md` — project template layout + setup steps

---

## Releases (Stable Links)

- `v1.0.0` — legacy “flat” system referenced by earlier articles (Parts 1–2)
- `release/v2` — tiered delegation system described in Part 3 (tag `v2.0.0` once published)

## Articles

- Part 1: https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825
- Part 2: https://medium.com/@ilyas.ibrahim/the-4-step-protocol-that-fixes-claude-codes-context-amnesia-c3937385561c

| Protocol loading | Per agent | Once (main only) | **N×** fewer loads |
| Coordination | Manual/broken | Automatic | **Seamless** |
| Memory persistence | None | Registry-based | **Full history** |

## Architecture Highlights

### Flat Agent Hierarchy
No nested coordinators or sub-agents. All 22 agents are peers, orchestrated by main agent.

**Why**: Nested designs cause exponential context consumption. Flat structure is simple and efficient.

### Context Efficiency
- Main agent loads agent-coordination skill: 370 lines (once)
- Main agent reads registry + reports: ~500-2000 lines (selective)
- Specialized agents: Receive excerpts only, never load full context

**Why**: Prevents redundant loading. 5 agents × 3000 lines each = 15,000 lines wasted. Now: 3000 lines loaded once.

### Registry-Based Memory
Simple markdown files tracking all agent work with links to deliverables.

**Why**: Easy to read, easy to update, works with Claude's strengths (reading markdown).

### Just-in-Time Skills
Skills auto-invoke based on keywords in task descriptions.

**Why**: Load domain knowledge only when relevant, not preemptively.

## Key Principles

1. **Main agent orchestrates, specialized agents execute**
   Don't bypass the main agent—work with Claude Code's design.

2. **Load context once, distribute excerpts**
   Centralized loading prevents exponential context waste.

3. **Flat hierarchy beats nested complexity**
   Simple structures scale better than clever architectures.

4. **Registry is source of truth**
   All work gets recorded, all new work checks the registry first.

5. **Every line matters**
   Ruthlessly optimize agent definitions and protocols.

## Repository Structure

```
claude-agents-coordination/
├── README.md              # You are here
├── LICENSE                # Unlicense (public domain)
│
├── claude-user/           # User-level configuration (~/.claude/)
│   ├── INDEX.md           # Detailed user-level guide
│   ├── agents/            # 22 agent definitions
│   ├── commands/          # 7 slash commands
│   └── skills/            # 4 auto-invoked skills
│
└── claude-project/        # Project-level configuration
    ├── INDEX.md           # Detailed project-level guide
    ├── commands/          # Project-specific commands
    ├── output-styles/     # Standardized output formats
    ├── skills/            # Project-specific skills
    └── reports/           # Registry + categorized reports
```

## Documentation

- **[claude-user/INDEX.md](claude-user/INDEX.md)**: Complete guide to user-level configuration
- **[claude-project/INDEX.md](claude-project/INDEX.md)**: Complete guide to project-level configuration

## Customization

### Add New Agents

Create `~/.claude/agents/my-agent.md`:
```markdown
# My Agent

Specializes in [specific task].

## Primary Responsibilities
- Task 1
- Task 2

## Available Tools
Read, Write, Bash, Grep

## Usage
Invoke when [specific condition].
```

Keep it focused: 25-50 lines recommended.

### Add New Skills

Create `~/.claude/skills/my-skill/SKILL.md`:
```markdown
# My Skill

Auto-invokes when user mentions: [trigger words]

## Purpose
Provide [specific knowledge]

## Key Concepts
[Domain knowledge here]
```

### Add Slash Commands

Create `~/.claude/commands/my-command.md`:
```markdown
Launch [agent-name] to [do specific task]

[Detailed instructions for the agent]
```

Use: `/my-command [arguments]`

## Real-World Usage

This system was developed for the [Somali Dialect Classifier](https://github.com/yourusername/somali-dialect-classifier) project, a low-resource language NLP initiative. It enabled:

- Coordinated data collection from 5+ sources
- Quality-controlled preprocessing pipeline
- ML experimentation with persistent metrics
- Dashboard development with consistent design
- All while maintaining context across 2+ hour sessions

## Contributing

This serves as documentation of a working system. You're encouraged to:

- Fork and adapt for your projects
- Open issues to discuss improvements
- Share your own coordination patterns
- Submit PRs with enhancements

## License

This is free and unencumbered software released into the public domain. See [LICENSE](LICENSE) for details.

Use it however you want. No attribution required (though appreciated).

## Why This Exists

I learn by doing—build it, break it, learn from mistakes. I tried to make Claude Code agents coordinate efficiently, failed twice, and finally found something that works. This repository shares the working solution so you don't have to make the same mistakes.

---

**Built through systematic iteration.** If you found this useful, star the repo and share your own experiences with Claude Code agent coordination.
