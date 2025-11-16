# Project-Level Configuration Index

This directory contains project-specific Claude Code configuration that extends the user-level setup for a particular project.

## Directory Structure

```
.claude-project/
├── commands/          # Project-specific slash commands
├── output-styles/     # Standardized output formats
├── skills/            # Project-specific skills
└── reports/           # Institutional memory (registry + categorized reports)
    ├── _registry.md   # Central index of all agent work
    ├── _TEMPLATE.md   # Standard report template
    └── [categories]/  # Organized by work type
```

## Commands

Project-specific slash commands that extend the user-level commands with domain-specific workflows.

### Example Commands Structure
```
commands/
├── commit.md           # Project-specific commit workflow
├── review.md          # Custom code review process
├── test.md            # Project-specific test execution
├── design-review.md   # UI/UX review workflow
├── ml/
│   └── run.md         # ML pipeline orchestration
├── data/
│   └── analyze.md     # Dataset analysis workflow
└── deploy.md          # Deployment automation
```

### Usage
```bash
/commit              # Create commit with project standards
/review src/path/    # Review code with project guidelines
/ml:run exp-name     # Run ML pipeline end-to-end
/data:analyze file   # Analyze dataset with project metrics
```

## Output Styles

Standardized formats for deliverables to ensure consistency across all agent outputs.

### Available Styles
- **technical-report.md**: Structured technical reports with sections for context, analysis, findings, recommendations
- **code-review.md**: Code review format covering correctness, security, performance, maintainability
- **design-review.md**: UI/UX review structure with accessibility, usability, visual design feedback
- **test-report.md**: Test execution results with pass/fail status, coverage metrics, failure analysis
- **commit-message.md**: Conventional Commits format with proper scope and description
- **handoff-document.md**: Knowledge transfer format for completed work

### Usage
Agents automatically use these styles when generating deliverables. No explicit invocation needed.

## Skills

Project-specific knowledge modules that auto-invoke based on task context.

### Data Engineering Skills
```
skills/data-engineering/
├── data-quality-standards/SKILL.md    # Quality thresholds and validation rules
└── etl-patterns/SKILL.md              # Extract, transform, load patterns
```

**When invoked**: Working on data pipelines, quality checks, ETL processes
**Purpose**: Ensure consistent data quality standards and pipeline patterns

### Machine Learning Skills
```
skills/machine-learning/
├── lrl-nlp-techniques/SKILL.md        # Low-resource language NLP methods
├── model-evaluation-framework/SKILL.md # Evaluation metrics and benchmarks
└── mlops-best-practices/SKILL.md      # MLOps workflows and standards
```

**When invoked**: Training models, evaluating performance, deploying ML systems
**Purpose**: Apply domain-specific ML knowledge and best practices

### Frontend Skills
```
skills/frontend/
├── dashboard-patterns/SKILL.md        # Common dashboard UI patterns
└── accessibility-checklist/SKILL.md   # WCAG AA compliance checklist
```

**When invoked**: Building dashboards, implementing UI components
**Purpose**: Ensure consistent UI patterns and accessibility compliance

## Reports (Institutional Memory)

The heart of agent coordination - a persistent memory system that tracks all work.

### Registry (`_registry.md`)

Central index of all agent work. Updated after every significant task.

**Structure**:
```markdown
# Agent Work Registry

## [Date] - [Agent Name] - [Task Title]
- **Status**: Completed/In Progress/Blocked
- **Deliverables**: Links to reports, code files, documentation
- **Context**: Brief description of the work
- **Follow-up**: Any pending items or next steps
```

**Usage**:
- Main agent reads registry before starting new tasks
- Provides context about previous related work
- Prevents duplication and ensures continuity
- Updated by main agent after task completion

### Report Categories

```
reports/
├── analysis/        # Data analysis, exploratory analysis, statistical insights
├── arch/            # Architecture decisions, system design, technical specs
├── bugs/            # Bug investigations, root cause analysis, fixes
├── commits/         # Commit summaries and changelogs
├── design/          # UI/UX design reviews, design decisions
├── exec/            # Execution reports, task completion summaries
├── handoff/         # Knowledge transfer documents
├── impl/            # Implementation reports (deprecated, use implementation/)
├── implementation/  # Feature implementation details
├── review/          # Code reviews, security reviews, quality assessments
├── screenshots/     # Visual documentation and UI screenshots
├── security/        # Security assessments and vulnerability reports
└── tests/           # Test reports, coverage analysis, test plans
```

### Report Template (`_TEMPLATE.md`)

Standard structure for all reports:
```markdown
# [Report Title]

**Date**: YYYY-MM-DD
**Agent**: [Agent Name]
**Type**: [Analysis/Architecture/Review/etc.]

## Context
Brief background and motivation for this work.

## Approach
Methodology and steps taken.

## Findings
Key discoveries and insights.

## Deliverables
- Links to code, documentation, artifacts

## Recommendations
Next steps and suggestions.

## Follow-up
Pending items and future work.
```

## Setting Up for Your Project

### 1. Copy Project Configuration
```bash
# Copy this directory to your project
cp -r .claude-project your-project/.claude
```

### 2. Initialize Registry
Edit `.claude/reports/_registry.md` with your project name:
```markdown
# Agent Work Registry - [Your Project Name]

Last updated: [Date]

---

## Getting Started
[Instructions for your team on using the registry]
```

### 3. Customize Skills
Add project-specific skills in `.claude/skills/`:
```bash
mkdir -p .claude/skills/your-domain/your-skill
# Create SKILL.md with auto-invoke triggers and knowledge
```

### 4. Configure Commands
Adapt commands in `.claude/commands/` to your workflow:
- Update `/commit` with project commit conventions
- Modify `/review` with project-specific review criteria
- Add new commands for project-specific workflows

### 5. Define Output Styles
Customize `.claude/output-styles/` for project needs:
- Add report sections specific to your domain
- Define metrics and KPIs to include
- Set documentation standards

## Coordination Workflow

### How Main Agent Uses Project Configuration

1. **User requests task**: "Implement user authentication feature"

2. **Main agent preparation**:
   - Invokes `agent-coordination` skill (from user-level)
   - Reads `.claude/reports/_registry.md` for prior auth work
   - Reads relevant reports (e.g., `arch/auth-system-design.md`)
   - Checks project skills (e.g., security best practices)

3. **Agent invocation**:
   - Main agent plans: `architect → backend-engineer → test-runner`
   - Invokes architect with full context
   - Architect designs auth system, references project skills
   - Returns design to main agent

4. **Execution continues**:
   - Main agent invokes backend-engineer with architect's design
   - Backend-engineer implements, uses output-styles for documentation
   - Main agent invokes test-runner with implementation details
   - Test-runner validates, produces test-report

5. **Completion**:
   - Main agent verifies all deliverables exist
   - Updates registry with new entries
   - Reports to user with summary

### Agent Never Reads Registry Directly

**Critical**: Individual specialized agents (backend-engineer, test-runner, etc.) should NEVER read the registry or reports directly. The main Claude agent handles all context retrieval and distribution.

**Why**: Loading registry (500+ lines) + reports (2000+ lines) per agent would exhaust context window. Main agent loads once, distributes relevant excerpts.

## Best Practices

### Registry Management
- **Update after every task**: Don't batch updates
- **Link to deliverables**: Reports, PRs, commits, documentation
- **Keep entries concise**: 5-10 lines per entry
- **Use consistent format**: Follow template structure

### Report Organization
- **Use categories**: Place reports in appropriate subdirectories
- **Follow template**: Use `_TEMPLATE.md` structure
- **Include dates**: YYYY-MM-DD format for easy sorting
- **Link between reports**: Reference related work

### Skill Development
- **Clear triggers**: Define specific keywords for auto-invoke
- **Focused knowledge**: Single domain per skill
- **Tested invocation**: Verify auto-invoke works with test phrases
- **Reasonable size**: 200-400 lines recommended

### Output Styles
- **Standard sections**: Consistent structure across deliverables
- **Project metrics**: Include KPIs and measurements
- **Action items**: Always include follow-up section
- **Versioning**: Track changes to style templates

## Example: Multi-Agent Task with Project Memory

```
User: "Mobilize agents to optimize the data preprocessing pipeline"

Main Agent:
  ├─ Invokes agent-coordination skill (user-level)
  ├─ Reads registry: finds 3 prior entries about preprocessing
  │   ├─ 2024-11-10: data-preprocessor - Initial pipeline setup
  │   ├─ 2024-11-12: ml-trainer - Slow training due to data format
  │   └─ 2024-11-13: data-analyst - Data quality issues identified
  ├─ Reads relevant reports:
  │   ├─ implementation/preprocessing-pipeline-v1.md (context)
  │   ├─ analysis/data-quality-assessment.md (known issues)
  │   └─ arch/data-architecture.md (system design)
  ├─ Invokes data-analyst with full context
  │   ├─ Receives: prior work summary, quality issues, architecture
  │   ├─ Analyzes: bottlenecks, data quality improvements
  │   ├─ Returns: analysis report to main agent
  ├─ Invokes data-preprocessor with analysis
  │   ├─ Receives: analyst findings, architecture constraints
  │   ├─ Implements: optimized pipeline, quality checks
  │   ├─ Returns: implementation details to main agent
  ├─ Invokes test-runner with implementation
  │   ├─ Receives: pipeline changes, success criteria
  │   ├─ Executes: performance tests, quality validation
  │   ├─ Returns: test results to main agent
  ├─ Verifies all deliverables created:
  │   ├─ analysis/preprocessing-optimization-analysis.md ✓
  │   ├─ implementation/preprocessing-pipeline-v2.md ✓
  │   └─ tests/preprocessing-performance-tests.md ✓
  ├─ Updates registry with new entry:
  │   └─ 2024-11-16: Multi-agent optimization completed
  └─ Reports to user:
      "Preprocessing pipeline optimized. Performance improved 3.2x.
       All tests passing. See implementation/preprocessing-pipeline-v2.md"
```

## Performance Characteristics

**Context Efficiency**:
- Registry: ~500 lines (loaded once by main agent)
- Typical report: ~300-500 lines (selective loading)
- Project skills: ~200-400 lines each (auto-invoked as needed)
- Output styles: ~50-100 lines (templates only)

**Coordination Overhead**:
- Main agent context loading: 370 (skill) + 500 (registry) + 1000 (reports) ≈ 1870 lines
- Per-agent context: 0 lines (receives excerpts from main agent)
- Total context saved: (# agents - 1) × 1870 lines

## Troubleshooting

**Registry not being read?**
- Check file path: `.claude/reports/_registry.md`
- Ensure main agent invoked with "mobilize agents" trigger
- Verify registry format matches template structure

**Skills not auto-invoking?**
- Check trigger keywords in project SKILL.md files
- Ensure directory structure: `skills/domain/skill-name/SKILL.md`
- Try explicit invocation: "use [skill-name] skill"

**Reports not updating?**
- Main agent should update, not individual agents
- Check that task completed successfully
- Verify agent-coordination skill loaded properly

**Context window exhausted?**
- Check if individual agents are loading registry (they shouldn't)
- Verify flat agent hierarchy (no coordinators)
- Consider archiving old registry entries

## Maintenance

### Regular Cleanup
- **Archive old reports**: Move completed work to `archive/` monthly
- **Compress registry**: Keep last 30-50 entries active, archive rest
- **Update skills**: Incorporate new learnings and best practices
- **Review output styles**: Adapt templates as project evolves

### Monitoring
- **Context usage**: Track how long sessions last (target: 2+ hours)
- **Registry growth**: Monitor size, compress if >1000 lines
- **Skill effectiveness**: Verify auto-invoke triggers work
- **Agent efficiency**: Check if agents produce expected outputs

## Next Steps

1. Copy project configuration to your project's `.claude/` directory
2. Initialize registry with project name and first entry
3. Add project-specific skills for your domain
4. Customize output styles for your deliverables
5. Test coordination: "Mobilize agents to [simple task]"
6. Monitor registry updates and report generation
7. Iterate on skills and commands based on usage patterns

## Related Documentation

- [Main README](../README.md): Full architecture explanation
- [User-Level Index](../.claude-user/INDEX.md): Global configuration guide
- [Claude Code Documentation](https://code.claude.com/docs): Official docs

---

**Key Principle**: Project-level configuration extends user-level with domain-specific knowledge, workflows, and institutional memory. The registry is the source of truth for all agent coordination.
