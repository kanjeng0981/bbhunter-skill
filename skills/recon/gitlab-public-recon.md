---
name: gitlab-public-recon
description: Mine GitLab for secrets, CI tokens when subdomain found.
scope: web2
---
Mine GitLab for secrets, CI tokens when subdomain found.

- Target has a gitlab. subdomain or self-hosted GitLab instance.
- crt.sh reveals gitlab.target.com in certificates.
- After subdomain-enumeration discovers GitLab hosts.
- After js-secrets-extraction finds GitLab CI/CD references.
- Target is a government agency or large enterprise (common self-hosted GitLab users).

- **Rate limiting.** GitLab API has rate limits (typically 300-600 requests/min). Use --max-time and delays.
- **File path encoding.** Special characters in paths must be URL-encoded (/ → %2F, . → %2E).
- **Default branch may not be main.** Try main, master, develop for file access.
- **Large files may truncate.** The API may limit response size. Use git clone for full access if registration is open.
- **GitLab authentication.** Public repos are accessible without auth. Private repos return 404.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/gitlab-public-recon/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
