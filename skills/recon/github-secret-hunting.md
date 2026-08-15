---
name: github-secret-hunting
description: Find leaked API keys, tokens, and credentials in public GitHub repositories.
scope: web2
---
Find leaked API keys, tokens, and credentials in public GitHub repositories.

- Target has public repositories under an organization account.
- JS bundle analysis reveals internal service names — search GitHub for related config files.
- Need to find valid API keys for cloud services, payment gateways, or third-party integrations.
- The target uses CI/CD systems that may leak tokens in build logs or workflow files.
- Want real-time monitoring for new secret leaks from the target org.

- **Most search results are documentation and examples, not real leaks.** Focus on .env, .config, .npmrc, and CI/CD workflow files.
- **Rate limiting on GitHub API is strict.** Use multiple tokens or rotate IPs.
- **Verified secrets may already be revoked.** Always verify before reporting.
- **Self-hosted GitLab instances may block external scanning.** Test connectivity first.
- **Never use found credentials for unauthorized access.** Verify minimally, document, and report.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/github-secret-hunting/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
