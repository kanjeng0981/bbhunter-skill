---
name: port-service-discovery
description: Nmap scan for MySQL, Redis, FTP, SSH, internal API services.
scope: web2
---
Nmap scan for MySQL, Redis, FTP, SSH, internal API services.

- Running deep-invade Phase 6 on a high-value target.
- After surface recon shows no exploitable web vulnerabilities — pivot to infrastructure.
- When the target is a SaaS with backend APIs on non-standard ports.
- After discovering a staging subdomain — check for database/admin ports.

- **nmap SYN scan requires raw-socket privileges.** Use -sT (TCP connect)
  when the execution environment does not grant them.
- **Rate limiting on port scans.** Some providers (AWS, Cloudflare) rate-limit or block port scans. Use -T2 (polite timing) and --max-retries 1 on sensitive targets.
- **MySQL/MongoDB banner grab may not work.** Some DBs require TLS negotiation (MySQL 8.0+ defaults to caching_sha2_password). Banner may be empty.
- **Internal API ports may time out.** Some services only respond to specific Host headers or valid HTTP requests. Use curl with various Host headers.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/port-service-discovery/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
