---
description: Run security scan on codebase or specific path using security-engineer agent
---

# Security Scan Command

Invoke `security-engineer` agent for security analysis.

## Usage

```
/security [path]                    # Full OWASP scan
/security [path] --threat-model     # STRIDE threat modeling
/security [path] --compliance       # Compliance review
/security [path] --deps             # Dependencies only
```

## Default Mode: Scan

```
Task(security-engineer, "
Mode: scan

Target: [path or entire codebase]

Perform comprehensive security scan:

1. OWASP Top 10 Check
   - Injection (SQL, Command, XSS)
   - Broken Authentication
   - Sensitive Data Exposure
   - XXE
   - Broken Access Control
   - Security Misconfiguration
   - XSS
   - Insecure Deserialization
   - Vulnerable Components
   - Insufficient Logging

2. Input Validation
   - All user input entry points
   - API parameter handling
   - File upload validation
   - Query string parsing

3. Authentication/Authorization
   - Session management
   - Password handling
   - Token validation
   - Permission checks

4. Secrets Detection
   - Hardcoded credentials
   - API keys in code
   - Private keys
   - Connection strings

5. Dependency Vulnerabilities
   - Known CVEs
   - Outdated packages
   - Unmaintained libraries

Output: .claude/reports/security/security-scan-[target]-YYYYMMDD.md
")
```

## Threat Model Mode

```
/security [feature-description] --threat-model
```

```
Task(security-engineer, "
Mode: threat-model

Feature: [description]

Perform STRIDE analysis:
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

Include:
- Data flow diagram
- Attack surface mapping
- Trust boundaries
- Threat mitigations

Output: .claude/reports/security/threat-model-[feature]-YYYYMMDD.md
")
```

## Compliance Mode

```
/security [path] --compliance [standard]
```

Standards: `gdpr`, `soc2`, `hipaa`, `pci`

```
Task(security-engineer, "
Mode: compliance

Target: [path]
Standard: [GDPR/SOC2/HIPAA/PCI]

Review compliance with:
- Data handling requirements
- Access control requirements
- Audit logging requirements
- Encryption requirements

Output: .claude/reports/security/compliance-[standard]-YYYYMMDD.md
")
```

## Dependencies Only

```
/security --deps
```

Quick scan of dependencies only:

```bash
# Node.js
npm audit --json > audit-results.json

# Python
pip-audit --format json > audit-results.json
safety check --json > safety-results.json

# Go
go list -json -m all | nancy sleuth

# Generate summary
```

## Output Format

```markdown
# Security Scan Report

## Executive Summary
- **Risk Level:** Critical | High | Medium | Low
- **Critical Issues:** [count]
- **High Issues:** [count]
- **Total Findings:** [count]

## Critical Findings

### SEC-001: [Title]
- **Severity:** Critical
- **Category:** [OWASP category]
- **Location:** `[file:line]`
- **Description:** [what's wrong]
- **Impact:** [potential damage]
- **Recommendation:** [how to fix]
- **CWE:** [CWE-XXX]

## High Findings
[Same structure]

## Medium Findings
[Same structure]

## Low Findings
[Same structure]

## Dependency Vulnerabilities

| Package | Version | Vulnerability | Severity | Fix Version |
|---------|---------|---------------|----------|-------------|
| [pkg] | [ver] | [CVE-XXXX] | High | [fixed ver] |

## Remediation Priority

1. **Immediate:** [critical issues to fix now]
2. **Short-term:** [high issues for next sprint]
3. **Medium-term:** [medium issues to plan]

## Scan Coverage
- Files scanned: [count]
- Lines analyzed: [count]
- Skipped: [patterns skipped]
```

## Integration with Review

Security scan is automatically included in `/review-full` as Level 3 when changes touch:
- Authentication code
- User input handling
- Database queries
- External API calls
- File operations
