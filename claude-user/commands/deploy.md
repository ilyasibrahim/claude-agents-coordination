---
description: Deploy application to production with devops-specialist agent
allowed-tools: Bash(git:*, docker:*, kubectl:*, npm:*, python:*)
argument-hint: [environment]
---

# Deploy Application

Deploy application to specified environment (staging, production) using devops-specialist agent.

## Process

1. **Pre-Deployment Checks**
   - Verify all tests pass in CI
   - Check deployment checklist (version bump, changelog)
   - Verify environment configuration
   - Review recent commits since last deployment

2. **Deployment Execution**
   - Invoke devops-specialist agent for deployment
   - Monitor deployment progress
   - Verify health checks pass
   - Check logs for errors

3. **Post-Deployment**
   - Verify application is running
   - Check monitoring dashboards
   - Set up alerts if not already configured
   - Document deployment details

4. **Rollback Plan**
   - Document rollback procedure
   - Keep previous version accessible
   - Monitor for issues in first 30 minutes

## Arguments

- **$1**: Optional environment (defaults to production)
  - `staging` - Deploy to staging environment
  - `production` - Deploy to production
  - `dev` - Deploy to development environment

## Examples

```bash
# Deploy to production (default)
/deploy

# Deploy to staging for testing
/deploy staging

# Deploy to development
/deploy dev
```

## Deployment Checklist

**Before Deployment:**
- [ ] All tests passing in CI
- [ ] Code reviewed and approved
- [ ] Version bumped in package.json/pyproject.toml
- [ ] Changelog updated
- [ ] Database migrations ready (if applicable)
- [ ] Environment variables configured
- [ ] Rollback plan documented

**During Deployment:**
- [ ] Monitor deployment logs
- [ ] Watch health check endpoints
- [ ] Check error rates in monitoring
- [ ] Verify no spike in error logs

**After Deployment:**
- [ ] Application responds to requests
- [ ] All services healthy
- [ ] Monitoring dashboards show green
- [ ] Alert configuration verified
- [ ] Document deployment in registry

## Notes

- Uses devops-specialist agent for execution
- Follows blue-green or canary deployment strategy
- Monitors for issues during deployment
- Automatic rollback on critical failures
