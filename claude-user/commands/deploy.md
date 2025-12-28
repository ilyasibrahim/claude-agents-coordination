---
description: Deploy with devops agent (mode: infra)
allowed-tools: Bash(git:*, docker:*, kubectl:*, npm:*, python:*)
argument-hint: [environment]
---

# Deploy Application

## Process

1. **Pre-check:** Tests pass, version bumped, changelog updated
2. **Deploy:** devops agent (mode: infra) handles deployment
3. **Verify:** Health checks, monitoring dashboards
4. **Document:** Update registry

## Arguments

- `production` (default) - Production deployment
- `staging` - Staging environment
- `dev` - Development environment

## Checklist

**Before:** Tests pass, code reviewed, version bumped, migrations ready
**During:** Monitor logs, watch health checks
**After:** Verify responses, check monitoring, document in registry
