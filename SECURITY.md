# Security Policy

## Supported versions

This project is a configuration layer distributed as files. Security fixes are applied
to the latest `main`. Tagged releases are documentation snapshots and are **not**
separately patched.

| Version | Supported |
|---------|-----------|
| `main` (latest) | ✅ |
| Tagged releases (`vX.Y.Z`) | ❌ (snapshots) |

## What counts as a security issue here

This repository ships no runtime binary, but its files instruct an AI coding agent
(Claude Code) and contain shell snippets. Please report things such as:

- Agent, command, or skill definitions that could induce destructive or unsafe actions
  (for example unscoped `rm`, data exfiltration, or disabling safety confirmations).
- Shell snippets in commands/skills with command-injection or data-loss potential.
- Supply-chain or social-engineering vectors via pull requests (for example unsolicited
  manifests, malicious scripts, or content designed to mislead a reviewing agent).
- Secrets or sensitive data accidentally committed to the repository.

## Reporting a vulnerability

Please report privately — **do not open a public issue**.

- **Preferred:** GitHub **Private vulnerability reporting**
  (repository → *Security* → *Report a vulnerability*). Enable this in repository
  settings if it is not already on.
- **Alternative:** contact the maintainer through the channels listed on the GitHub
  profile / project README.
  <!-- Maintainer: add a dedicated security contact email here. -->

Please include: the affected file(s), a description, a reproduction or proof-of-concept,
and the potential impact.

## Response targets

- **Acknowledgement:** within 5 business days.
- We will confirm the report, assess severity, and coordinate a fix and disclosure
  timeline with you.
- Please allow reasonable time for remediation before any public disclosure.

## Scope note for users

Because this project is public-domain configuration that you copy into your own
environment, **you are responsible for reviewing any agent, command, or skill before
installing it.** Treat third-party pull requests to this repository as untrusted until a
maintainer has reviewed them.
