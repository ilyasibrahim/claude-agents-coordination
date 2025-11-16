# Claude Code Agents Coordination

**Multi-agent coordination system for Claude Code with institutional memory and efficient context management.**

Stop your Claude Code agents from forgetting what they just did. This battle-tested architecture extends context windows from 15-20 minutes to 2+ hours while enabling multiple agents to coordinate seamlessly through persistent memory.

---

## What This Does

- **Extends Context Windows**: 2+ hours vs 15-20 minutes (8x improvement)
- **Enables Agent Coordination**: Agents reference each other's work through a shared registry
- **Reduces Overhead**: 67-73% smaller agent definitions through focused design
- **Provides Institutional Memory**: Registry and reports persist knowledge across sessions
- **Optimizes Context Loading**: Main agent loads once, distributes to specialized agents
- **Uses Just-in-Time Skills**: Auto-invoke domain knowledge only when needed

## Quick Start

### 1. Install User-Level Configuration

```bash
git clone https://github.com/yourusername/claude-agents-coordination.git
cd claude-agents-coordination
cp -r claude-user ~/.claude
```

This gives you 22 specialized agents, 4 auto-invoked skills, and 7 slash commands available across all your projects.

### 2. Add Project-Level Configuration

```bash
# In your project directory
cp -r claude-project/.claude .
```

This adds institutional memory (registry + reports), project-specific skills, and standardized output formats.

### 3. Start Using

```
# Simple task
"Use the debugger agent to investigate the timeout issue"

# Coordinated multi-agent task
"Mobilize agents to implement user analytics dashboard"

# With slash commands
/commit
/review src/
/test integration
```

## How It Works

### Centralized Coordination

```
┌──────────────────────────────────────────────────────────────┐
│               Main Claude Code Agent                         │
│            (Orchestrates everything)                         │
│                                                              │
│  1. User says "mobilize agents"                              │
│  2. Loads agent-coordination skill (370 lines, once)         │
│  3. Reads registry + relevant reports                        │
│  4. Determines which agents to use                           │
│  5. Invokes agents with context excerpts                     │
│  6. Verifies deliverables                                    │
│  7. Updates registry                                         │
│  8. Reports results                                          │
└──────────────────┬───────────────────────────────────────────┘
                   │
                   │ Distributes context
                   ▼
┌──────────────────────────────────────────────────────────────┐
│         22 Specialized Agents (Flat Hierarchy)               │
│                                                              │
│  • Receive context from main agent                           │
│  • Do specialized work                                       │
│  • Return results                                            │
│  • Never load protocol/registry themselves                   │
└──────────────────────────────────────────────────────────────┘
```

**Key Principle**: Main agent loads context once, specialized agents execute with excerpts. No redundant loading, maximum efficiency.

### Institutional Memory

The registry (`.claude/reports/_registry.md`) acts as persistent memory:

```markdown
## 2024-11-16 - backend-engineer - User Authentication Implementation
- **Status**: Completed
- **Deliverables**:
  - implementation/auth-system.md
  - review/auth-code-review.md
  - tests/auth-test-report.md
- **Context**: Implemented JWT-based auth with refresh tokens
- **Follow-up**: Add OAuth integration in next phase
```

When agents start new tasks, the main agent reads this registry to provide context about prior work.

## What's Included

### User-Level Configuration (`claude-user/`)

**22 Specialized Agents** organized by domain:
- **Code Quality** (4): code-reviewer, debugger, test-runner, qa-engineer
- **Architecture** (2): system-architect, pipeline-orchestrator
- **Data** (4): data-collector, data-analyst, data-preprocessor, data-viz-specialist
- **DevOps** (2): devops-engineer, git-specialist
- **Documentation** (2): documentation-writer, webdev-documentation-writer
- **Implementation** (2): frontend-engineer, backend-engineer
- **ML** (4): ml-trainer, ml-evaluator, ml-deployer, lrl-nlp-expert
- **UX** (2): ux-ui-designer, ux-writer

**4 Auto-Invoked Skills**:
- `agent-coordination` (370 lines): Coordination protocol with registry conventions
- `design-system`: Dual-palette design system for dashboards
- `style-guide`: Visual design philosophy and principles
- `ux-writing`: Voice, tone, and messaging standards

**7 Slash Commands**:
- `/commit` (`/c`): Create commit with Conventional Commits format
- `/review` (`/r`): Code quality review
- `/test` (`/t`): Run test suite
- `/design-review` (`/dr`): UI/UX review with Playwright
- `/deploy` (`/d`): Deploy application
- `/ml:run`: ML pipeline orchestration
- `/data:analyze`: Dataset analysis

### Project-Level Configuration (`claude-project/`)

**Institutional Memory Structure**:
```
.claude/reports/
├── _registry.md          # Central index of all work
├── _TEMPLATE.md          # Standard report template
├── analysis/             # Data analysis reports
├── arch/                 # Architecture decisions
├── bugs/                 # Bug investigations
├── design/               # UI/UX design reviews
├── implementation/       # Feature implementations
├── review/               # Code reviews
├── tests/                # Test reports
└── [other categories]/
```

**Project-Specific Skills**: Domain knowledge modules (data engineering, ML, frontend patterns)

**Output Styles**: Standardized formats for reports, reviews, commits, handoffs

## Usage Examples

### Basic Agent Invocation

```
User: "Fix the authentication timeout in login.ts"

→ Main agent analyzes the issue
→ Invokes debugger agent with context
→ Debugger investigates and returns findings
→ Main agent verifies and reports back
```

### Multi-Agent Coordination

```
User: "Mobilize agents to implement user analytics dashboard"

→ Main agent invokes agent-coordination skill
→ Reads registry for prior analytics work
→ Plans: architect → frontend-engineer + backend-engineer → test-runner
→ Invokes agents sequentially with shared context
→ Each agent produces deliverables
→ Updates registry with new work
→ Reports summary to user
```

### With Slash Commands

```
/review src/dashboard/
→ Launches code-reviewer agent
→ Reviews all files in src/dashboard/
→ Generates standardized code review report

/ml:run experiment-v2
→ Orchestrates full ML pipeline
→ Data collection → preprocessing → training → evaluation → deployment
→ Tracks metrics and updates registry
```

## Performance Comparison

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Context window duration | 15-20 min | 2+ hours | **8x** |
| Agent definition size | 150-280 lines | 25-52 lines | **73% reduction** |
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
