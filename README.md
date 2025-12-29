# Claude Code Agents Coordination

**Production-grade multi-agent coordination system with tiered delegation, institutional memory, and explicit tech-debt tracking.**

This repository provides reusable configuration layers for Claude Code that enable sophisticated agent orchestration across projects—from solo development to enterprise-scale workflows.

## What This Solves

Three critical problems in Claude Code agent usage:

1. **Context Amnesia**: Agents forget prior work within 15-20 minutes
2. **Coordination Chaos**: Multiple agents overwrite each other's work
3. **Delegation Limits**: Manual oversight required for every decision

**Solution**: A tiered delegation architecture with persistent memory (registry + tech-debt tracking) that extends productive context windows to 2+ hours while enabling the Main Agent to consistently apply documented engineering criteria.

---

## Core Architecture

### Tiered Agent System

```
Tier 1: Workflow Orchestrators
├── code-quality      → Multi-level review chain (L1→L2→L3→L4)
├── test-engineer     → Test execution with failure triage
├── architect         → System design + ADRs + RFC lifecycle
└── ml-engineer       → End-to-end ML workflows

Tier 2: Specialized Execution
├── security-engineer → Threat modeling, OWASP scans
├── sre               → SLOs, postmortems, capacity planning
├── rfc               → Design document workflow
├── data-engineer     → Data pipelines + quality validation
├── frontend/backend  → Implementation work
├── devops            → CI/CD, infrastructure, git workflows
└── docs              → Technical documentation

Tier 3: On-Demand Specialists
├── lrl-nlp-expert        → Low-resource language NLP
├── data-viz-specialist   → Data storytelling + dashboards
└── ux-designer           → UX/design review + writing
```

### Dual-Registry Model

**`_registry.md`** — What was done
- Tracks completed work, deliverables, and outcomes
- Main agent reads this for context before starting new tasks
- Updated after every significant task completion

**`_tech-debt.md`** — What was deferred
- Explicit tracking of shortcuts, workarounds, and deferred improvements
- Links each debt item to its source (commit, report, or incident)
- Prevents silent degradation of code quality

### 4-Step Coordination Protocol

1. **Registry Check** → Main agent reads prior work
2. **Context Injection** → Relevant context distributed to specialized agents
3. **Sequencing** → Sequential or parallel execution based on dependencies
4. **Verification** → Quality gates ensure standards are met

---

## Quick Start

### 1. Install User-Level Configuration

```bash
mkdir -p ~/.claude
rsync -a claude-user/ ~/.claude/
```

This installs:
- Tiered agent set (orchestrators + specialists + on-demand experts)
- Standard workflows (`/review-full`, `/ci`, `/debt`, `/postmortem`, `/rfc`)
- Auto-invoked skills (agent-coordination protocol, design system, UX writing)

### 2. Install Project-Level Configuration

```bash
# In your project directory
mkdir -p .claude
rsync -a claude-project/ .claude/
```

This creates:
- `CLAUDE.md` project context file (edit with your project details)
- Institutional memory structure (registries + categorized report folders)
- Project-specific commands and skills

### 3. Start Using

```bash
# Multi-level code review
/review-full src/authentication/

# Local CI pipeline before pushing
/ci

# View and manage tech debt
/debt

# Create RFC for system design
/rfc authentication-system

# Incident postmortem with automatic debt logging
/postmortem login-timeout-2025-12-28
```

---

## Key Features

### Multi-Level Review Chain

The `/review-full` command implements graduated review escalation:

```
L1: Peer Review (code-quality agent)
    ↓ Triggers: Always runs
L2: Architecture Review (architect agent)
    ↓ Triggers: New APIs, schema changes, >500 lines, new dependencies
L3: Security Review (security-engineer agent)
    ↓ Triggers: Auth/authz, user input, external APIs, crypto
L4: Reliability Review (sre agent)
    ↓ Triggers: Infrastructure changes, deployment configs, perf-critical paths
```

**Why**: Main Agent applies documented escalation criteria by reading code, ensuring consistent decisions without relying on memory.

### Local CI Pipeline

The `/ci` command runs the full quality gate before pushing:

```
1. Lint → Check code style
2. Type-check → Verify type safety
3. Build → Ensure compilation succeeds
4. Test → Run test suite with coverage
5. Security scan → OWASP checks
```

**Why**: Catch issues locally before CI/CD, faster feedback cycles.

### Explicit Tech-Debt Tracking

The `_tech-debt.md` registry captures:
- What shortcut was taken
- Why it was necessary (time pressure, missing info, external dependency)
- Where it lives (file paths, commit SHAs)
- Impact severity (cosmetic → critical)
- Remediation plan

**Why**: Prevents "just this once" from becoming permanent, maintains quality over time.

### Protocol Efficiency Optimization

The agent-coordination protocol is split across multiple files:
- `SKILL.md` (core protocol, always loaded)
- `templates.md` (loaded only when creating reports)
- `reference.md` (loaded only for lookups)
- `scripts/` (executable helpers for archiving, verification)

**Why**: Reduces per-task token consumption by 40-60% through selective loading.

---

## Releases

This repository maintains stable release versions to support documentation and article references:

- **[v1.0.0](https://github.com/ilyasibrahim/claude-agents-coordination/releases/tag/v1.0.0)** — Initial "flat" coordination system (22 peer agents)
  - Referenced by Part 1 and Part 2 articles
  - Foundational 4-step protocol implementation
  - Proved agent coordination viability

- **[v2.0.0](https://github.com/ilyasibrahim/claude-agents-coordination/releases/tag/v2.0.0)** — Tiered delegation system (current)
  - Production-grade delegation with multi-level review chains
  - Dual-registry model (work done + tech debt)
  - Protocol optimization for token efficiency
  - Described in Part 3 article

**Versioning approach**: Major versions represent architectural shifts, minor versions add features, patches fix documentation/bugs.

---

## Articles & Documentation

This system is documented through a three-part series on Medium:

1. **[How I Made Claude Code Agents Coordinate 100% (and Solved Context Amnesia)](https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825)**
   - The journey from 26-agent chaos to working coordination
   - 8x context window improvement (15 min → 2+ hours)

2. **[The 4-Step Protocol That Fixes Claude Code's Context Amnesia](https://medium.com/@ilyas.ibrahim/the-4-step-protocol-that-fixes-claude-codes-context-amnesia-c3937385561c)**
   - Deep dive into the coordination protocol
   - Registry-based institutional memory

3. **Scaling Claude Code: From Solo Testing to Enterprise-Grade Delegation** *(Part 3 - Coming Soon)*
   - Tiered delegation architecture
   - Multi-level review chains
   - Production deployment lessons

**In-repo documentation**:
- `claude-user/INDEX.md` — User-level configuration guide
- `claude-project/INDEX.md` — Project-level setup and workflow

---

## Repository Structure

```
claude-agents-coordination/
├── README.md                    # You are here
├── CHANGELOG.md                 # Version history
├── LICENSE                      # Unlicense (public domain)
│
├── claude-user/                 # User-level config (~/.claude/)
│   ├── INDEX.md                 # Detailed user-level guide
│   ├── agents/                  # Tiered agent definitions
│   ├── commands/                # Standard workflows (/review-full, /ci, etc.)
│   └── skills/                  # Auto-invoked knowledge + coordination protocol
│
└── claude-project/              # Project-level config (<project>/.claude/)
    ├── INDEX.md                 # Detailed project-level guide
    ├── CLAUDE.md                # Project context template
    ├── commands/                # Project-specific workflows
    ├── skills/                  # Project domain knowledge
    └── reports/
        ├── _registry.md         # Work done (institutional memory)
        ├── _tech-debt.md        # Deferred work (explicit debt tracking)
        └── [categories]/        # Organized report folders
```

---

## Performance Characteristics

| Metric | v1.0.0 (Flat) | v2.0.0 (Tiered) | Improvement |
|--------|---------------|-----------------|-------------|
| Context window duration | 2 hours | 2+ hours | Maintained |
| Protocol token cost | 370 lines (always loaded) | 150-250 lines (selective) | **40-60% reduction** |
| Review depth | Single-level | Multi-level (L1→L4) | **Graduated escalation** |
| Tech-debt visibility | None | Explicit tracking | **Prevents silent decay** |
| Delegation capability | Task execution only | Documented criteria | **Consistent application** |

---

## Customization

### Add Custom Agents

Create `~/.claude/agents/my-agent.md`:

```markdown
# My Agent

Specializes in [specific capability].

## Primary Responsibilities
- Responsibility 1
- Responsibility 2

## Available Tools
Read, Write, Bash, Grep, Glob

## Invocation Context
Use when [specific conditions].
```

**Best practice**: Keep agents focused (25-75 lines), single responsibility.

### Add Project Skills

Create `.claude/skills/my-domain/my-skill/SKILL.md`:

```markdown
# My Skill

Auto-invokes when task mentions: [trigger keywords]

## Domain Knowledge
[Specific domain expertise, patterns, conventions]

## Usage Guidelines
[When to apply this knowledge, examples]
```

**Best practice**: 200-400 lines, clear auto-invoke triggers.

### Add Slash Commands

Create `~/.claude/commands/my-workflow.md`:

```markdown
Launch [agent-name] to [accomplish specific goal]

Provide context:
- [Detail 1]
- [Detail 2]

Expected deliverables:
- [Deliverable 1]
- [Deliverable 2]
```

Use: `/my-workflow [arguments]`

---

## Real-World Usage

This system was developed for the **Somali Dialect Classifier** project—a low-resource language NLP initiative requiring:

- Multi-source data collection (BBC Somali, Wikipedia, HuggingFace, TikTok, Språkbanken)
- Quality-controlled preprocessing pipeline
- ML experimentation with persistent metrics tracking
- Static dashboard with Tableau-inspired design system
- All coordinated by a single developer

**Results**:
- 2+ hour productive sessions without context loss
- Main Agent consistently applied documented criteria to escalate security/architecture reviews
- Tech-debt registry prevented quality degradation
- 40% reduction in protocol overhead through optimization

---

## Contributing

This repository documents a working system. Contributions welcome:

- **Issues**: Report bugs, suggest improvements
- **Pull Requests**: Enhancements to agents, protocols, documentation
- **Discussions**: Share your coordination patterns and lessons learned

**Philosophy**: Iterate, fail, learn, document. If you found a better approach, share it.

---

## License

This is free and unencumbered software released into the public domain (Unlicense).

Use it however you want. No attribution required (though appreciated).

See [LICENSE](LICENSE) for full text.

---

## Why This Exists

Built through systematic iteration on real production needs. Started with 26-agent chaos, refined to 22-agent flat coordination, evolved to tiered delegation for autonomous engineering judgment.

**This repository shares the working solution** so others can build sophisticated agent systems without repeating the same failures.

**If this helped you**: Star the repo, share your experiences, contribute improvements.

---

**Questions?** Open an issue or reach out via [Medium](https://medium.com/@ilyas.ibrahim).
