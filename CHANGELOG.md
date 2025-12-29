# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.2.0] - 2025-12-29

### Changed
- Updated `/review-full` L2 architecture review trigger threshold from >500 lines to >200 lines for better precision
- Enhanced review trigger criteria with more explicit conditions for L2, L3, and L4 reviews
- Expanded `review-full.md` with comprehensive protocol documentation including pre-review analysis and decision flowchart

### Added
- Database queries to L3 security review trigger criteria
- Command-line flags support for `/review-full`: `--quick`, `--security`, `--all`
- Pre-review analysis section with file size and git diff statistics
- Post-review verification steps and registry update protocol
- Decision flowchart visualization for review level selection

### Improved
- Review trigger criteria now more accurately reflect real-world engineering judgment needs
- Better alignment between documented escalation criteria and actual code characteristics

## [2.1.1] - 2025-12-29

### Fixed
- Corrected inaccurate language in README.md that implied autonomous agent behavior
- Documentation now accurately describes Main Agent orchestration following documented protocols

### Changed
- Updated README.md: "Main Agent applies documented criteria" instead of "agents make autonomous decisions"
- Clarified system value comes from documented criteria consistently applied, not autonomous behavior

## [2.1.0] - 2025-12-28

### Added
- Python-based archive script (`archive_reports.py`) replacing bash implementation
- Dated archive registries (`_registry-archive-YYYYMMDD.md`) as temporal snapshots
- Archive README.md for documentation and navigation
- Full registry parsing and automated updating
- Dry-run mode for preview before archiving (`--dry-run` flag)

### Changed
- Archive process now creates dated registry snapshots instead of single append-only file
- Archive script now fully automated (updates both active and archive registries)
- Archive status tracking (automatically marks entries as "Archived")
- Improved robustness (parses registry dates instead of relying on filenames)

### Improved
- Archive organization with dated snapshots prevents unbounded growth
- Better archive history tracking (each archive run preserved as snapshot)
- Enhanced documentation in `reference.md` with complete usage examples
- Project template updated with dated registry example

### Fixed
- Manual registry cleanup no longer required after archiving
- Archive process now works with any filename format (not just *-YYYYMMDD.md)

## [2.0.0] - 2025-12-28

### Added
- Tiered agent architecture with three-tier hierarchy:
  - Tier 1: Workflow orchestrators (code-quality, test-engineer, architect, ml-engineer)
  - Tier 2: Specialized execution agents (security-engineer, sre, rfc, data-engineer, frontend/backend, devops, docs)
  - Tier 3: On-demand specialists (lrl-nlp-expert, data-viz-specialist, ux-designer)
- Dual-registry model for comprehensive project memory:
  - `_registry.md` for tracking completed work and deliverables
  - `_tech-debt.md` for explicit tracking of deferred improvements and shortcuts
- Multi-level review chain (`/review-full`) with automatic escalation:
  - L1: Peer review (always runs)
  - L2: Architecture review (triggered by API changes, schema changes, >200 lines)
  - L3: Security review (triggered by auth/authz, user input, external APIs, crypto)
  - L4: Reliability review (triggered by infrastructure, deployment, performance-critical paths)
- Standard workflow commands:
  - `/review-full` for graduated review escalation
  - `/ci` for local CI pipeline (lint → type-check → build → test → security)
  - `/debt` for tech-debt registry management
  - `/postmortem` for incident analysis with automatic debt logging
  - `/rfc` for RFC authoring and decision capture
- Protocol optimization through file splitting:
  - `SKILL.md` (core protocol, always loaded)
  - `templates.md` (loaded only when creating reports)
  - `reference.md` (loaded only for lookups)
  - `scripts/` (executable helpers for archiving, verification)
- Project template with complete report taxonomy folders (analysis/, arch/, bugs/, commits/, design/, exec/, handoff/, implementation/, review/, security/, sre/, rfc/, ci/, tests/, archive/)
- Enhanced INDEX.md files with comprehensive setup and workflow documentation

### Changed
- Restructured agents from flat 22-agent set to tiered delegation model
- Optimized coordination protocol for 40-60% token reduction through selective loading
- Updated README.md with comprehensive v2.0.0 architecture documentation
- Improved agent definitions to include delegation capabilities and engineering judgment
- Enhanced slash commands with quality gates and verification steps

### Improved
- Context efficiency through tiered invocation (orchestrators delegate to specialists)
- Agent autonomy through embedded engineering judgment in Tier 1 orchestrators
- Quality assurance through multi-level review chains and explicit tech-debt tracking
- Documentation structure with clear separation between user-level and project-level guides

## [1.0.0] - 2025-11-16

### Added
- Initial multi-agent coordination system with flat hierarchy (22 peer agents)
- Four-step coordination protocol:
  1. Registry check (main agent reads prior work)
  2. Context injection (relevant context distributed to specialized agents)
  3. Sequencing (sequential or parallel execution based on dependencies)
  4. Verification (quality gates ensure standards are met)
- Institutional memory through `_registry.md` registry file
- User-level configuration with 22 specialized agents:
  - Code Quality (4): code-reviewer, debugger, test-runner, qa-engineer
  - Architecture (2): system-architect, pipeline-orchestrator
  - Data (4): data-collector, data-analyst, data-preprocessor, data-viz-specialist
  - DevOps (2): devops-engineer, git-specialist
  - Documentation (2): documentation-writer, webdev-documentation-writer
  - Implementation (2): frontend-engineer, backend-engineer
  - Machine Learning (4): ml-trainer, ml-evaluator, ml-deployer, lrl-nlp-expert
  - UX (2): ux-ui-designer, ux-writer
- Auto-invoked skills system:
  - `agent-coordination` (370 lines): Coordination protocol with registry conventions
  - `design-system`: Dual-palette design system for dashboards
  - `style-guide`: Visual design philosophy and principles
  - `ux-writing`: Voice, tone, and messaging standards
- Seven slash commands:
  - `/commit` (`/c`): Create commit with Conventional Commits format
  - `/review` (`/r`): Code quality review
  - `/test` (`/t`): Run test suite
  - `/design-review` (`/dr`): UI/UX review with Playwright
  - `/deploy` (`/d`): Deploy application
  - `/ml:run`: ML pipeline orchestration
  - `/data:analyze`: Dataset analysis
- Project-level configuration structure with categorized report folders
- Standardized output styles for consistent deliverables
- Comprehensive INDEX.md documentation for both user-level and project-level configuration

### Performance
- Extended context window duration from 15-20 minutes to 2+ hours (8x improvement)
- Reduced agent definition size from 150-280 lines to 25-52 lines (67-73% reduction)
- Eliminated per-agent protocol loading (N× reduction in redundant context loading)
- Enabled automatic agent coordination through registry-based memory

[unreleased]: https://github.com/ilyasibrahim/claude-agents-coordination/compare/v2.2.0...HEAD
[2.2.0]: https://github.com/ilyasibrahim/claude-agents-coordination/compare/v2.1.1...v2.2.0
[2.1.1]: https://github.com/ilyasibrahim/claude-agents-coordination/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/ilyasibrahim/claude-agents-coordination/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/ilyasibrahim/claude-agents-coordination/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/ilyasibrahim/claude-agents-coordination/releases/tag/v1.0.0
