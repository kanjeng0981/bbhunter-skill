---
name: staging-subdomain-hunt
description: Hunt staging via crt.sh when production is WAF-hardened.
scope: web2
---
Hunt staging via crt.sh when production is WAF-hardened.

- Running deep-invade Phase 5 on a high-value target.
- Production target is well-secured (WAF, no leaks) — pivot to staging.
- Target has a large attack surface (e-commerce, SaaS, franchise model).
- You need additional entry points when the main site is hardened.
- After subdomain-enumeration produces a list of subdomains.

- **crt.sh rate limiting.** crt.sh may return empty JSON if rate-limited. Use 2-3s delays between queries or query the PostgreSQL dump directly at crt.sh/?d=.
- **Wildcard certs hide subdomains.** If *.example.com is the only cert, individual subdomains won't appear in crt.sh. Use subfinder DNS brute force as fallback.
- **Staging may require VPN.** Some staging environments are IP-restricted.
  Test only from source addresses approved by the engagement.
- **WordPress install.php on production.** Some poorly maintained production sites also have this accessible. It's not always staging-specific. Check for "Welcome to WordPress" title text to confirm it's a fresh install.
- **CORS can differ between production and staging.** Test the same bounded
  endpoint matrix in both environments before claiming a security-control gap.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/staging-subdomain-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
