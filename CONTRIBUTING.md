# Contributing

Thanks for your interest in **Claude Code Agents Coordination**.

This repository is a *configuration layer* for Claude Code — sets of agents, slash
commands, skills, and report scaffolding that you copy into `~/.claude/` and
`<project>/.claude/`. There is no application to build or run; contributions are
changes to Markdown/YAML configuration and documentation.

Please read this guide before opening an issue or pull request.

## Contents

- [Code of Conduct](#code-of-conduct)
- [What this project is — and the vocabulary](#what-this-project-is--and-the-vocabulary)
- [Ways to contribute](#ways-to-contribute)
- [Automated, promotional, and unsolicited-manifest PRs](#automated-promotional-and-unsolicited-manifest-prs)
- [Proposing a change](#proposing-a-change)
- [Conventions](#conventions)
- [Commit messages](#commit-messages)
- [Pull request process](#pull-request-process)
- [Local checks](#local-checks)
- [Security](#security)
- [License of contributions](#license-of-contributions)

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating,
you are expected to uphold it.

## What this project is — and the vocabulary

Using the right terms keeps reviews fast. This project has four building blocks:

| Term | Lives in | What it is |
|------|----------|-----------|
| **Agent** | `claude-user/agents/*.md` | A specialised sub-agent with YAML frontmatter (`name`, `description`, `tools`, `model`, `color`) and a short body. Single responsibility. |
| **Command** | `claude-user/commands/*.md` | A slash command — a prompt that launches one or more agents toward a goal. |
| **Skill** | `**/skills/<domain>/<skill>/SKILL.md` | Auto-invoked domain knowledge with explicit trigger keywords. |
| **Report** | `claude-project/reports/<category>/` | Output artifacts, indexed in `_registry.md`; deferred work in `_tech-debt.md`. |

Agents, commands, and skills are **distinct** — please don't conflate them (e.g. an
agent is not a "skill"). The coordination model itself is documented in
`claude-user/skills/agent-coordination/SKILL.md`.

## Ways to contribute

- **Report a bug** in an agent, command, skill, or doc — use the Bug report issue form.
- **Propose a new agent/command/skill or a protocol change** — open a Proposal issue
  *first* (see below). Significant changes start as a discussion, not a PR.
- **Improve documentation** — fixes and clarifications are always welcome.
- **Share coordination patterns** in Discussions.

## Automated, promotional, and unsolicited-manifest PRs

To keep this repository trustworthy and maintainable, the following are **closed
without review**:

- PRs opened by bots or as part of automated outreach campaigns.
- PRs that add support for a third-party "standard", manifest, registry, or runtime we
  did not ask for — for example dropping a root-level `agent.yaml`, `SOUL.md`,
  `AGENTS.md`, or similar — or that enroll this project in an external registry.
- PRs whose primary purpose is promotion (requesting stars, linking a product,
  onboarding the project into an ecosystem).
- PRs that assert capabilities this project does not have (for example
  compliance/audit/kill-switch attestations that nothing here implements).

If you genuinely believe an integration fits, **open an issue first** describing the
value, the ongoing maintenance cost, and the stability/governance of the external
dependency. A maintainer will decide whether to invite a PR. Manifests and registry
entries, if ever adopted, are authored deliberately by the maintainers — they are not
accepted as drive-by contributions.

## Proposing a change

For anything beyond a small fix, open an issue using the **Proposal** form before
writing code. Describe the problem, the proposed design, and the maintenance cost. This
saves you from building something that doesn't fit, and gives reviewers context.

## Conventions

- **Agents** (`claude-user/agents/*.md`): YAML frontmatter with `name`, `description`,
  `tools`, `model`, `color`; **25–75 lines**; single responsibility. Use the model tier
  that matches the workload (see `CHANGELOG.md` for the `opus`/`sonnet`/`haiku` tiering)
  and a `color` from the documented palette.
- **Commands** (`claude-user/commands/*.md`): a focused prompt that names the agent(s),
  the context to inject, and the expected deliverables.
- **Skills** (`SKILL.md`): **200–400 lines**, explicit auto-invoke trigger keywords,
  split heavy content into `reference.md`/`templates.md` to keep the core lean.
- **Reports**: file naming `[category]-[topic]-YYYYMMDD.md`; index in `_registry.md`.

## Commit messages

This project uses [Conventional Commits](https://www.conventionalcommits.org):

```
<type>(<scope>): <subject>
```

Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `ci`.
Common scopes: `agents`, `commands`, `skills`, `docs`, `archive`, `ci`.

Examples:

- `feat(agents): add a profiler agent for performance investigations`
- `fix(commands): correct the /review-full escalation threshold`
- `docs: clarify the dual-registry update rules`

## Pull request process

1. Branch from an up-to-date `main`; use a topic branch (don't push to `main`).
2. Keep PRs **small and focused** — one logical change per PR.
3. Fill in the pull request template and **link the issue** it resolves.
4. Don't add unrelated root-level files.
5. Make sure local checks pass (below).

Sign-off (DCO) is encouraged: `git commit -s`.

## Local checks

Before pushing, run the same checks CI runs:

```bash
# Markdown lint (config in .markdownlint-cli2.jsonc)
npx --yes markdownlint-cli2

# YAML lint
python -m yamllint -d "{extends: relaxed, rules: {line-length: disable}}" .
```

If you add shell snippets to a command or skill, make sure they are safe (no
unscoped destructive operations) and work under both `bash` and `zsh`.

## Security

See [SECURITY.md](SECURITY.md). Report vulnerabilities **privately** — do not open a
public issue for them.

## License of contributions

This project is released under the [Unlicense](LICENSE) (public domain). By
contributing, you agree that your contributions are dedicated to the public domain
under the same terms.
