---
name: hunt-springboot
description: Hunt Spring Boot specific vulnerabilities — Actuator endpoints (heapdump, env, loggers, mappings, shutdown), Spring Expression Language (SpEL) injection → RCE, H2 console RCE, Jolokia JMX exposure, Spring4Shell (CVE-2022-22965), Spring Cloud Function SPEL (CVE-2022-22963), heap dump credential extraction. Use when target runs Spring Boot — detected via X-Application-Context header, /actuator, Whitelabel Error Page, or Java stack traces.
scope: web2
---
Hunt Spring Boot specific vulnerabilities — Actuator endpoints (heapdump, env, loggers, mappings, shutdown), Spring Expression Language (SpEL) injection → RCE, H2 console RCE, Jolokia JMX exposure, Spring4Shell (CVE-2022-22965), Spring Cloud Function SPEL (CVE-2022-22963), heap dump credential extraction. Use when target runs Spring Boot — detected via X-Application-Context header, /actuator, Whitelabel Error Page, or Java stack traces.

- **Actuator endpoints without sensitive data** — /actuator/health or /actuator/info are intentionally public. Need /actuator/env, /actuator/heapdump, or /actuator/mappings.
- **/actuator/env with sanitized values** — Spring Boot 2.x+ sanitizes env values by default. Need unsanitized secrets.
- **/actuator/heapdump download** — heapdump analysis requires Eclipse MAT or similar. The finding is the dump is accessible, not what it contains (prove with actual extracted secrets).
- **/actuator/loggers modification** — changing log level to DEBUG can leak sensitive data. Demonstrate the leaked data.
- **Spring Boot version without CVE** — version disclosure is informational unless paired with a CVE affecting that specific version.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-springboot/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
