---
name: hunt-csrf
description: Hunting skill for csrf vulnerabilities. Built from 15 public bug bounty reports including modern variants — SameSite=Lax sibling-subdomain bypass (Argo CD CVE-2024-22424), GraphQL mutations-via-GET (GitLab $3,370), framework-wide CSRF middleware disabled (Stripe Dashboard $5,000), path-traversal CSRF-token bypass (GitHub Enterprise CVE-2022-23732 $10k), Origin-omission bypass (TikTok $2,500), OAuth-state null-byte (Streamlabs), WebSocket CSRF / CSWSH (Coda), default-SameSite email-change → ATO (YoYo Games $400), social-account-link CSRF (HackerOne), JSON-CSRF via text/plain on email-change (TikTok $500). Use when hunting modern CSRF — heavy emphasis on chain-to-ATO patterns.
scope: web2
---
Hunting skill for csrf vulnerabilities. Built from 15 public bug bounty reports including modern variants — SameSite=Lax sibling-subdomain bypass (Argo CD CVE-2024-22424), GraphQL mutations-via-GET (GitLab $3,370), framework-wide CSRF middleware disabled (Stripe Dashboard $5,000), path-traversal CSRF-token bypass (GitHub Enterprise CVE-2022-23732 $10k), Origin-omission bypass (TikTok $2,500), OAuth-state null-byte (Streamlabs), WebSocket CSRF / CSWSH (Coda), default-SameSite email-change → ATO (YoYo Games $400), social-account-link CSRF (HackerOne), JSON-CSRF via text/plain on email-change (TikTok $500). Use when hunting modern CSRF — heavy emphasis on chain-to-ATO patterns.

Use when the target has any state-changing endpoint that a logged-in user can trigger — POST/PUT/DELETE on account settings, email changes, social account linking, OAuth flows, API calls, or file operations. CSRF exploits the trust a site has in a user's browser by forging cross-origin requests. Every form submission, AJAX call, OAuth callback, and API mutation is a candidate. Highest-value targets: account takeover vectors (OAuth/SSO flows, social account linking), authentication infrastructure (login CSRF, session fixation), JSON APIs accepting cross-origin POST, and third-party integrations (Grafana, monitoring dashboards).

1. **Static CSRF tokens per session** — Developers generate one token at login and reuse it. Airbnb bug: authenticity_token was the same across all page loads for a session, makin
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-csrf/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
