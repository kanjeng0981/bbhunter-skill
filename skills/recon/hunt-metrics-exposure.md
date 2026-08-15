---
name: hunt-metrics-exposure
description: Hunt public /metrics, /health, and actuator endpoints leaking AI usage, DB pools, and operational intelligence.
scope: web2
---
Hunt public /metrics, /health, and actuator endpoints leaking AI usage, DB pools, and operational intelligence.

The target uses modern observability tooling (Go, .NET, Java, Node.js). These frameworks often expose /metrics, /health, and /status endpoints that are forgotten behind auth. Unlike application data leaks, metrics leaks reveal the ENTIRE operational profile: which AI models are used, how many users are active, database connection exhaustion, and third-party service dependencies.

---

- **Prometheus /metrics without secrets** — metrics endpoints exposing request counts are informational. Need labels containing PII, internal hostnames, or credentials.
- **Spring Boot Actuator /actuator/metrics** — metrics are intentionally exposed for monitoring. Only report if they leak sensitive data (usernames in labels, internal IPs).
- **JMX without auth** — JMX exposure without authentication is critical only if write operations (MBean invocation) are possible. Read-only JMX is informational.
- **Health endpoint without sensitive data** — /health, /status, /ready endpoints are designed to be public. Need leaked internal data.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-metrics-exposure/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
