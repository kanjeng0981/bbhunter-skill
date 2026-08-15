---
name: hunt-ssrf
description: Hunting skill for ssrf vulnerabilities. Built from 15 public bug bounty reports including AWS metadata SSRF (HackerOne $25k Analytics PDF, Shopify Exchange $25k, Capital One 106M-record breach, Dropbox/HelloSign $4,913), GCP metadata SSRF (Snapchat $4k), Azure IMDS SSRF (Azure DevOps $15k chain, ChatGPT Custom Actions MSRC), DNS rebinding SSRF (Concrete CMS, GitLab UrlBlocker), gopher-protocol-to-Redis-RCE (Yahoo Mail $15k), link-preview SSRF (Reddit Matrix $6k), and headless-browser PDF-generator SSRF chains. Use when hunting SSRF on any target — OOB Collaborator confirmation mandatory for blind cases.
scope: web2
---
Hunting skill for ssrf vulnerabilities. Built from 15 public bug bounty reports including AWS metadata SSRF (HackerOne $25k Analytics PDF, Shopify Exchange $25k, Capital One 106M-record breach, Dropbox/HelloSign $4,913), GCP metadata SSRF (Snapchat $4k), Azure IMDS SSRF (Azure DevOps $15k chain, ChatGPT Custom Actions MSRC), DNS rebinding SSRF (Concrete CMS, GitLab UrlBlocker), gopher-protocol-to-Redis-RCE (Yahoo Mail $15k), link-preview SSRF (Reddit Matrix $6k), and headless-browser PDF-generator SSRF chains. Use when hunting SSRF on any target — OOB Collaborator confirmation mandatory for blind cases.

Use when the target has any feature that fetches a URL, imports data from a remote source, generates previews/screenshots, processes webhooks, or renders documents. SSRF allows an attacker to make the server itself perform network requests — reaching internal services, cloud metadata endpoints, and otherwise inaccessible infrastructure. Every link-preview, file-import, image-proxy, webhook-registration, PDF-generation, and redirect-following endpoint is a candidate. Highest-value targets: cloud-hosted SaaS, Kubernetes/orchestration platforms, CI/CD systems, and URL-fetching features.

1. **"The user said it was safe"** — Developers trust user-supplied URLs for fetching remote resources (link previews, thumbnails, webhooks) without validating the destination. The feature is legitimate; the missing validation is the bug.

2. **Allowlist bypass via redirects** — Developers valid
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-ssrf/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
