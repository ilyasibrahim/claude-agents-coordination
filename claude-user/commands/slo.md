---
description: Generate SLO document and error budget analysis using SRE agent
---

# SLO Command

Invoke `sre` agent in reliability-review mode to define and analyze SLOs.

## Usage

```
/slo [service-name]             # Generate SLO document
/slo budget [service-name]      # Calculate error budget status
/slo review [service-path]      # Review existing SLO
```

## Generate SLO Document

```
/slo [service-name]
```

```
Task(sre, "
Mode: reliability-review

Service: [service-name]

Generate comprehensive SLO document:

1. Service Overview
   - Purpose and scope
   - Key user journeys
   - Critical dependencies

2. SLI Definitions
   - Availability (success rate)
   - Latency (P50, P95, P99)
   - Error rate
   - Throughput

3. SLO Targets
   - Target percentages
   - Measurement windows
   - Rationale for each target

4. Error Budget
   - Budget calculation
   - Spend rate tracking
   - Budget policy

5. Alerting Thresholds
   - Warning vs critical
   - Burn rate alerts
   - Escalation paths

6. Failure Modes
   - Known failure scenarios
   - Impact assessment
   - Mitigation strategies

7. Dependencies
   - Upstream services
   - Downstream consumers
   - Dependency SLOs

Output: .claude/reports/sre/slo-[service]-YYYYMMDD.md
")
```

## Error Budget Analysis

```
/slo budget [service-name]
```

```
Task(sre, "
Mode: reliability-review

Service: [service-name]

Analyze error budget status:

1. Current Period Status
   - Budget allocated
   - Budget consumed
   - Burn rate

2. Trend Analysis
   - Last 7 days
   - Last 30 days
   - Projected exhaustion

3. Budget Consumers
   - Top incidents by budget impact
   - Patterns in budget spend

4. Recommendations
   - If healthy: feature velocity OK
   - If degraded: reliability focus areas
   - If exhausted: required actions

Output: .claude/reports/sre/budget-[service]-YYYYMMDD.md
")
```

## SLO Reference

### Standard SLO Tiers

| Tier | Availability | Monthly Downtime | Use Case |
|------|--------------|------------------|----------|
| Tier 1 | 99.99% | 4.3 minutes | Payment, Auth |
| Tier 2 | 99.9% | 43.2 minutes | Core features |
| Tier 3 | 99.5% | 3.6 hours | Non-critical |
| Tier 4 | 99% | 7.2 hours | Internal tools |

### Error Budget Policy

| Budget Remaining | Development Mode |
|-----------------|------------------|
| > 50% | Normal velocity - ship features |
| 25-50% | Caution - prioritize stability |
| < 25% | Feature freeze - reliability only |
| 0% | All hands on reliability |

### Common SLIs

| SLI | Definition | Measurement |
|-----|------------|-------------|
| Availability | Successful requests / Total requests | `sum(rate(http_success)) / sum(rate(http_total))` |
| Latency P50 | Median response time | `histogram_quantile(0.50, http_duration)` |
| Latency P99 | 99th percentile response | `histogram_quantile(0.99, http_duration)` |
| Error Rate | Failed requests / Total requests | `sum(rate(http_5xx)) / sum(rate(http_total))` |
| Throughput | Requests per second | `sum(rate(http_requests_total[5m]))` |

## Integration with Workflow

SLO documents inform:
- `/review-full` L4 reliability review
- `/postmortem` impact assessment
- `/rfc` non-functional requirements
- `/deploy` rollback thresholds
