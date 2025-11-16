# Claude Code Agents Coordination

A comprehensive guide to coordinating multiple Claude Code agents with institutional memory and efficient context management.

## Overview

This repository documents a real-world journey of building and optimizing a multi-agent system in Claude Code for a low-resource language NLP project. It showcases the evolution from 26 isolated agents consuming excessive context to an efficient 22-agent system with centralized coordination and persistent memory.

## The Problem

Working with Claude Code's multi-agent system presents several challenges:

- **Context Amnesia**: Agents don't retain information between tasks
- **Poor Coordination**: Agents work in isolation without referencing each other's work
- **Context Consumption**: Inefficient designs can burn through context windows in 15-20 minutes
- **Duplication**: Multiple agents performing overlapping work without awareness
- **Report Sprawl**: Hundreds of lines of uncoordinated documentation

## The Solution

Through iterative experimentation, this repository presents a battle-tested architecture that:

- ✅ Extends context windows from 15-20 minutes to 2+ hours
- ✅ Reduces agent definition overhead by 67-73%
- ✅ Implements institutional memory through registries and reports
- ✅ Enables efficient agent coordination without redundant context loading
- ✅ Leverages Claude Skills for just-in-time knowledge injection
- ✅ Uses Slash Commands for high-frequency workflows

## Architecture Evolution

### Initial Attempt (26 Agents + Manual Coordination)
- 26 specialized agents with verbose definitions (150-280 lines each)
- Manual AGENT_MEMORY_POLICY.md checks (850+ lines, loaded multiple times)
- Context exhaustion in 15-20 minutes
- Heavy maintenance overhead

### Failed Optimization (Sub-Agent Design)
- Attempted to bypass main Claude agent with "coordinator" agents
- Created nested sub-agents within agent definitions
- Resulted in exponential context consumption
- Every agent loaded everything, even worse performance

### Final Architecture (22 Flat Agents + Centralized Coordination)
- 22 specialized agents with focused definitions (25-52 lines each)
- Centralized `agent-coordination` skill (370 lines, loaded once by main agent)
- Registry-based institutional memory
- Context windows extended to 2+ hours
- Main Claude agent orchestrates, specialized agents execute

## Repository Structure

```
claude-agents-coordination/
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── .claude-user/                # User-level configuration (~/.claude/)
│   ├── INDEX.md                 # User-level configuration guide
│   ├── agents/                  # 31 agent definitions (22 active + 9 deprecated)
│   ├── commands/                # Slash commands for workflows
│   └── skills/                  # Auto-invoked skills
│
└── .claude-project/             # Project-level configuration
    ├── INDEX.md                 # Project-level configuration guide
    ├── commands/                # Project-specific commands
    ├── output-styles/           # Standardized output formats
    ├── skills/                  # Project-specific skills
    └── reports/                 # Institutional memory structure
        ├── _registry.md         # Central registry of all work
        ├── _TEMPLATE.md         # Report template
        └── [subdirectories]/    # Categorized reports
```

## Key Components

### User-Level Configuration (`.claude-user/`)

Contains globally applicable agents, skills, and commands:

**22 Active Agents** (organized by domain):
- **Code Quality** (4): code-reviewer, debugger, test-runner, qa-engineer
- **Architecture** (2): system-architect, pipeline-orchestrator
- **Data** (4): data-collector, data-analyst, data-preprocessor, data-viz-specialist
- **DevOps** (2): devops-engineer, git-specialist
- **Documentation** (2): documentation-writer, webdev-documentation-writer
- **Implementation** (2): frontend-engineer, backend-engineer
- **ML** (4): ml-trainer, ml-evaluator, ml-deployer, lrl-nlp-expert
- **UX** (2): ux-ui-designer, ux-writer

**4 Core Skills**:
- `agent-coordination`: 370-line coordination protocol (loaded once by main agent)
- `design-system`: Dual-palette design system for dashboards
- `style-guide`: Visual design philosophy and principles
- `ux-writing`: Voice, tone, and messaging standards

**7 Slash Commands**:
- `/commit`, `/review`, `/test`, `/design-review`
- `/ml:run` (ML pipeline orchestration)
- `/data:analyze` (Dataset analysis)
- `/deploy` (Deployment automation)

### Project-Level Configuration (`.claude-project/`)

Project-specific customizations and institutional memory:

**Skills**: Domain-specific knowledge modules
- Data engineering standards and ETL patterns
- ML techniques for low-resource languages
- Model evaluation frameworks
- Dashboard UI patterns and accessibility

**Output Styles**: Standardized deliverable formats
- Technical reports, code reviews, test reports
- Commit messages, handoff documents

**Reports**: Institutional memory organized by category
- `_registry.md`: Central index of all agent work
- Categorized subdirectories: analysis, arch, bugs, design, implementation, review, tests, etc.

## How It Works

### Coordination Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                    Main Claude Code Agent                        │
│                 (User-facing, coordination)                      │
│                                                                  │
│  When user says "mobilize agents":                              │
│  1. Invokes agent-coordination skill (370 lines, once)          │
│  2. Reads project registry (.claude/reports/_registry.md)       │
│  3. Reads relevant reports (context from past work)             │
│  4. Determines which agents needed                              │
│  5. Decides parallel vs sequential execution                    │
│  6. Invokes agents with complete context                        │
│  7. Verifies deliverables                                       │
│  8. Synthesizes results                                         │
│  9. Updates registry                                            │
│  10. Reports to user                                            │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         │ Provides complete context in task prompts
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│              22 Specialized Task Agents (Flat)                   │
│                                                                  │
│  Each agent:                                                     │
│    - Receives context from main agent                            │
│    - Does specialized work                                       │
│    - Returns output to main agent                                │
│    - NEVER reads registry/reports directly                       │
│    - NEVER invokes agent-coordination skill                      │
└──────────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **Centralized Coordination**: Main agent loads context once, distributes to specialized agents
2. **Flat Agent Hierarchy**: No nested coordinators, all agents are peers
3. **Context Efficiency**: Agents receive only what they need from main agent
4. **Institutional Memory**: Registry tracks all work, reports preserve knowledge
5. **Just-in-Time Skills**: Auto-invoke based on task context, not loaded preemptively
6. **Standardized Workflows**: Slash commands for repetitive tasks

## Usage Examples

### Basic Task
```
User: "Fix the authentication bug in login.ts"
→ Main agent analyzes issue
→ Invokes debugger agent with context
→ Debugger returns fix
→ Main agent verifies and reports
```

### Complex Multi-Agent Task
```
User: "Mobilize agents to implement user analytics dashboard"
→ Main agent invokes agent-coordination skill
→ Reads registry for related prior work
→ Plans task: architect → frontend-engineer + backend-engineer → test-runner
→ Invokes agents sequentially with shared context
→ Each agent produces deliverables
→ Main agent updates registry
→ Reports completion with summary
```

### With Slash Command
```
User: "/review src/dashboard/"
→ Expands to code review workflow
→ Main agent invokes code-reviewer
→ Standardized review report generated
```

## Lessons Learned

### ✅ What Worked

1. **Flat agent hierarchy**: Simpler than nested coordinators, less context overhead
2. **Centralized coordination**: Main agent as orchestrator eliminates redundant context loading
3. **Compressed definitions**: 25-50 line agents vs 150-280 lines, 67-73% reduction
4. **Registry-based memory**: Simple, effective institutional memory
5. **Auto-invoke skills**: Load knowledge only when needed

### ❌ What Didn't Work

1. **Bypassing main agent**: Attempted "agent autonomy" resulted in worse context consumption
2. **Sub-agent nesting**: Nested agents within agent definitions confused Claude Code
3. **Verbose protocols**: 850-line AGENT_MEMORY_POLICY loaded multiple times
4. **Manual verification**: Agents reading reports instead of using bash checks
5. **Too many coordinators**: 3 orchestrators with overlapping responsibilities

### 💡 Key Insights

- **Validate architecture before optimizing**: Building on wrong foundation wastes effort
- **Understand tool constraints**: Claude Code has specific expectations, work with them
- **Context is king**: Every line loaded matters, optimize ruthlessly
- **Simplicity scales**: Flat structures outperform nested complexity
- **Main agent is essential**: Trying to bypass it creates more problems than it solves

## Performance Metrics

| Metric | Initial | Failed Optimization | Final |
|--------|---------|-------------------|-------|
| Agent count | 26 | 8 coordinators + 23 subs | 22 flat |
| Avg agent size | 150-280 lines | N/A | 25-52 lines |
| Protocol size | 850 lines | 280 lines | 370 lines (loaded once) |
| Context window | 15-20 min | <15 min | 2+ hours |
| Redundant loading | Yes (per agent) | Yes (worse) | No (main only) |

## Getting Started

1. **Copy user-level config**:
   ```bash
   cp -r .claude-user ~/.claude
   ```

2. **Copy project-level config**:
   ```bash
   cp -r .claude-project your-project/.claude
   ```

3. **Customize for your needs**:
   - Edit agent definitions in `~/.claude/agents/`
   - Add project-specific skills in `your-project/.claude/skills/`
   - Modify commands and output styles as needed

4. **Start using**:
   ```
   "Mobilize agents to [task]"
   /commit
   /review src/
   ```

## Related Work

This architecture was developed for the [Somali Dialect Classifier](https://github.com/yourusername/somali-dialect-classifier) project, a low-resource language NLP initiative.

## Contributing

This repository serves as documentation of a working system. Feel free to:
- Fork and adapt to your projects
- Open issues to discuss improvements
- Share your own agent coordination patterns

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

Built through trial, error, and systematic iteration with Claude Code. Special thanks to the Anthropic team for creating a tool powerful enough to enable this level of customization.

---

**Remember**: Efficiency gains built on unstable foundations are illusory. Validate your architecture before optimizing, and understand your tool's constraints before designing around them.
