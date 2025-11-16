# User-Level Configuration Index

This directory contains globally applicable Claude Code configuration that works across all your projects.

## Directory Structure

```
claude-user/
├── agents/         # 31 agent definitions (22 active, 9 deprecated)
├── commands/       # 7 slash commands for common workflows
└── skills/         # 4 auto-invoked skills
```

## Agents (22 Active)

### Code Quality (4 agents)
- **code-reviewer**: Comprehensive code reviews (correctness, security, performance, maintainability)
- **debugger**: Root cause analysis and bug investigation
- **test-runner**: Execute test suites and analyze results
- **qa-engineer**: Design test strategies and create test cases

### Architecture (2 agents)
- **system-architect**: System design specifications and technical architecture
- **pipeline-orchestrator**: Data/ML pipeline architecture and workflow orchestration

### Data (4 agents)
- **data-collector**: Web scraping, APIs, data acquisition integration
- **data-analyst**: Exploratory data analysis and statistical insights
- **data-preprocessor**: Clean, transform, and prepare data for ML
- **data-viz-specialist**: Complex visualizations, dashboards, data storytelling

### DevOps (2 agents)
- **devops-engineer**: CI/CD, infrastructure, deployment automation
- **git-specialist**: Advanced Git workflows and repository management

### Documentation (2 agents)
- **documentation-writer**: Technical documentation for general projects
- **webdev-documentation-writer**: Web dev documentation (components, APIs)

### Implementation (2 agents)
- **frontend-engineer**: Complex frontend features with performance focus
- **backend-engineer**: Backend APIs, databases, server-side integrations

### Machine Learning (4 agents)
- **ml-trainer**: Model training with hyperparameter tuning and tracking
- **ml-evaluator**: Model performance evaluation with comprehensive metrics
- **ml-deployer**: Deploy models to production with monitoring
- **lrl-nlp-expert**: Low-resource language NLP and cross-lingual transfer

### UX (2 agents)
- **ux-ui-designer**: UX guidance, design reviews, design system patterns
- **ux-writer**: User-facing content, microcopy, error messages

## Skills (4 auto-invoked)

### agent-coordination (370 lines)
**When invoked**: User says "mobilize agents" or "coordinate agents"
**Purpose**: Centralized coordination protocol for multi-agent tasks
**Key features**:
- Registry-based institutional memory
- Sequencing vs parallelism rules
- Report templates and conventions
- Verification patterns for quality assurance

**Critical**: This skill is loaded ONCE by the main Claude agent, then context is distributed to specialized agents. Individual agents should NEVER invoke this skill directly.

### design-system
**When invoked**: Working on styling, design, CSS, visual components, frontend
**Purpose**: Dual-palette design system for data/ML dashboards
**Key features**:
- Tableau-inspired brand colors for UI elements
- Colorblind-friendly data colors for visualizations
- Component patterns, spacing, shadows, typography
- Accessibility guidelines (WCAG AA)

### style-guide
**When invoked**: Discussing visual design, brand identity, design principles
**Purpose**: Visual design philosophy and aesthetic guidelines
**Key features**:
- Tableau-inspired professionalism
- Data-first clarity principles
- Generous spacing and dual-layer shadows
- Design influences and brand principles

### ux-writing
**When invoked**: Working on copy, messaging, user-facing text, labels, errors
**Purpose**: Voice, tone, and messaging standards for data/ML dashboards
**Key features**:
- Professional-yet-accessible voice
- Context-specific tone guidance
- Microcopy and error message standards
- Success states and data presentation language

## Commands (7 slash commands)

### General Workflows
- **/commit** (alias: `/c`): Create git commit with Conventional Commits format
- **/review** (alias: `/r`): Code quality review with code-quality agent
- **/test** (alias: `/t`): Run test suite with test-runner agent
- **/design-review** (alias: `/dr`): UI/UX review with ux-ui-designer + Playwright

### Specialized Workflows
- **/deploy** (alias: `/d`): Deploy application with devops-specialist agent
- **/ml:run**: Orchestrate full ML pipeline (data → train → deploy)
- **/data:analyze**: Analyze dataset with data-analyst agent

## Usage Guidelines

### Installing This Configuration

```bash
# Copy entire directory to user-level .claude
cp -r claude-user ~/.claude
```

### Invoking Agents

```
# Single agent task
"Use the debugger agent to investigate the login timeout issue"

# Multi-agent coordinated task
"Mobilize agents to implement user analytics feature"
→ Main agent will invoke agent-coordination skill
→ Plans which agents to use (e.g., architect → backend-engineer → test-runner)
→ Executes sequentially or in parallel as appropriate
→ Updates registry with work performed
```

### Using Slash Commands

```
# Quick commit
/commit

# Code review
/review src/dashboard/

# Run tests
/test integration

# Design review with Playwright
/design-review

# ML pipeline
/ml:run experiment-name

# Data analysis
/data:analyze data/raw/dataset.csv
```

### Customizing for Your Workflow

1. **Add new agents**: Create `.md` files in `~/.claude/agents/`
   - Keep definitions focused (25-50 lines recommended)
   - Specify tools available and primary responsibilities
   - Reference similar agents as templates

2. **Add new skills**: Create `skill-name/SKILL.md` in `~/.claude/skills/`
   - Define auto-invoke triggers clearly
   - Keep focused on specific domain knowledge
   - Test auto-invoke keywords to ensure they work

3. **Add new commands**: Create `.md` files in `~/.claude/commands/`
   - Use clear, memorable names
   - Include aliases for frequently used commands
   - Document expected arguments

## Agent Definitions Overview

Each agent definition follows this structure:
```markdown
# Agent Name

Brief description of agent's purpose and specialization.

## Primary Responsibilities
- Bullet list of main tasks this agent handles

## Available Tools
List of tools (Read, Write, Bash, etc.) the agent can use

## Usage Notes
- When to use this agent
- How it coordinates with other agents
- Any special considerations
```

Average agent size: **25-52 lines** (67-73% reduction from original 150-280 lines)

## Deprecated Agents (9)

These agents are kept for reference but are no longer actively used:
- ml-projects-orchestrator (merged into ml-orchestrator at project level)
- mlops-pipeline-orchestrator (merged into ml-orchestrator at project level)
- data-engineer (exists as consolidated agent, deprecated individual variant)
- full-stack-engineer (exists as consolidated agent, deprecated individual variant)
- code-quality (exists as consolidated agent, deprecated individual variant)
- devops-specialist (exists as consolidated agent, deprecated individual variant)
- ux-designer (exists as consolidated agent, deprecated individual variant)
- architect (exists as consolidated agent, deprecated individual variant)
- documentation (exists as consolidated agent, deprecated individual variant)

## Performance Characteristics

**Context Efficiency**:
- Main agent loads agent-coordination skill: 370 lines (once)
- Individual agent definitions: 25-52 lines each
- Skills auto-invoked only when relevant: 200-400 lines each
- **Total context window**: 2+ hours (vs 15-20 minutes with old design)

**Coordination Pattern**:
```
User Request
    ↓
Main Claude Agent
    ├── Loads agent-coordination skill (370 lines, once)
    ├── Reads registry for institutional memory
    ├── Plans agent invocations (sequential vs parallel)
    ├── Invokes specialized agents with context
    │   ├── Agent 1 (receives context from main, no skill loading)
    │   ├── Agent 2 (receives context from main, no skill loading)
    │   └── Agent N (receives context from main, no skill loading)
    ├── Verifies deliverables
    ├── Updates registry
    └── Reports to user
```

## Best Practices

1. **Let main agent coordinate**: Don't try to bypass the main Claude agent
2. **Keep agents focused**: Single responsibility, 25-50 lines
3. **Use skills for knowledge**: Auto-invoke just-in-time, not preloaded
4. **Registry is source of truth**: Always update after completing work
5. **Slash commands for repetition**: Common workflows deserve shortcuts
6. **Flat hierarchy**: No nested coordinators or sub-agents

## Troubleshooting

**Agents not coordinating?**
- Ensure you use trigger phrase: "mobilize agents" or "coordinate agents"
- Check that agent-coordination skill exists in `skills/agent-coordination/SKILL.md`
- Verify main agent can access the skill

**Skills not auto-invoking?**
- Check trigger keywords in SKILL.md match your request
- Ensure skill directory structure: `skills/skill-name/SKILL.md`
- Try explicitly mentioning skill name: "invoke design-system skill"

**Commands not working?**
- Verify command file exists: `commands/command-name.md`
- Check for typos in command invocation: `/commit` not `/commits`
- Ensure slash at beginning: `/commit` not `commit`

## Next Steps

1. Copy this configuration to `~/.claude/`
2. Explore agent definitions in `agents/` directory
3. Try slash commands: `/commit`, `/review`, `/test`
4. Experiment with coordinated tasks: "Mobilize agents to build feature X"
5. Customize agents, skills, and commands for your workflow

## Related Documentation

- [Main README](../README.md): Full architecture explanation and lessons learned
- [Project-Level Index](../claude-project/INDEX.md): Project-specific configuration guide
- [Claude Code Documentation](https://code.claude.com/docs): Official Claude Code docs

---

**Key Principle**: This user-level configuration provides globally applicable agents, skills, and commands. Project-specific customizations go in `claude-project/` at the project level.
