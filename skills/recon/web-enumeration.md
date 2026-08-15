---
name: web-enumeration
description: Sensitive file scanning, path traversal bypass, vHost enum, .env extract, log mining, Varnish detect
scope: web2
---
Sensitive file scanning, path traversal bypass, vHost enum, .env extract, log mining, Varnish detect

# Web Enumeration -- Sensitive Files, Path Traversal, vHost, Log Mining

## When to Use

- **ALWAYS** on every target -- first thing after port scan
- Success rate is high on neglected infrastructure
- One finding (.env, .git) often leads to full credential access

## Sensitive File Scanning (200+ Paths)



## Path Traversal & Bypass (10+ Techniques)



## Virtual Host (vHost) Enumeration



## Automatic .env Credential Extraction



## Log Data Extraction



## Varnish Cache Detection



## Real-World Cases

**OVH Laravel server**: .env, .git/config, storage/oauth-private.key all exposed (200 OK). Credentials for MySQL, SendGrid, cloud storage, Firebase.

**Government agency Vite dev mode**: 45 TypeScript files served publicly with VITE_JWT_SECRET and VITE_API_TOKEN in plain text.

See references/batch-probe-methodology.md for a bounded probe template,
catch-all detection, endpoint-specific CORS checks, and XML-RPC response
classification.

## Pitfalls


## Verification



### Phase 6 — Parameter Discovery

Find hidden parameters on known endpoints:



### Phase 7 — URL Category Extraction

Categorize discovered URLs by sensitivity to prioritize testing:



### Phase 8 — WAF & 403 Bypass



### Phase 9 — Historical Page Recovery & Robots.txt History

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/web-enumeration/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
