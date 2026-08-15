---
name: subdomain-takeover-hunt
description: Detect and verify subdomain takeover via dangling CNAME to unclaimed services.
scope: web2
---
Detect and verify subdomain takeover via dangling CNAME to unclaimed services.

- Subdomain enumeration produces a large list — scan for lingering DNS records.
- Target uses cloud services with shared-namespace identifiers (Heroku, S3, Azure, Zendesk, Shopify).
- A subdomain returns NXDOMAIN, 404, or "no such app" error pages.
- The CNAME target is a service with user-registrable names.

- **Resolving CNAME to a CDN service is not a finding.** Cloudflare/CloudFront/Akamai subdomains are not claimable.
- **The CNAME may point to a valid, in-use service.** Always verify the error page before claiming a finding.
- **Some services block automated scanners.** Visit the URL in a browser to confirm.
- **Subdomain takeover requires registration of the target resource.** Never register resources without explicit authorization.
- **Wildcard DNS (*.target.com → IP) produces false positives.** Filter out wildcard responses before scanning for takeover.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/subdomain-takeover-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
