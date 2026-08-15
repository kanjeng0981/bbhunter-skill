---
name: hunt-host-header
description: Hunt Host Header Injection — password reset poisoning → ATO, web cache poisoning via unkeyed Host/X-Forwarded-Host, routing-based SSRF (Host picks upstream → cloud metadata/internal services), path-override SSRF/ACL-bypass (X-Original-URL/X-Rewrite-URL), OAuth redirect_uri/issuer poisoning, and absolute-URL link poisoning in emails. High to Critical when it reaches ATO or mass cache poisoning. Built on public Host-header research (PortSwigger 'Practical web cache poisoning' + James Kettle, and the classic password-reset-poisoning class). Use on any forgot-password flow, CDN/reverse-proxy-fronted app, OAuth/OIDC endpoint, or absolute-URL-in-email feature.
scope: web2
---
Hunt Host Header Injection — password reset poisoning → ATO, web cache poisoning via unkeyed Host/X-Forwarded-Host, routing-based SSRF (Host picks upstream → cloud metadata/internal services), path-override SSRF/ACL-bypass (X-Original-URL/X-Rewrite-URL), OAuth redirect_uri/issuer poisoning, and absolute-URL link poisoning in emails. High to Critical when it reaches ATO or mass cache poisoning. Built on public Host-header research (PortSwigger 'Practical web cache poisoning' + James Kettle, and the classic password-reset-poisoning class). Use on any forgot-password flow, CDN/reverse-proxy-fronted app, OAuth/OIDC endpoint, or absolute-URL-in-email feature.

- **Host header reflection without impact** — the header being echoed in the page is not a vulnerability. Need cache poisoning, password reset poisoning, or SSRF.
- **Password reset poisoning without email confirmation** — reflected host in response doesn't prove the reset link was poisoned. Read the actual email.
- **Absolute URL generation vs relative** — if the app uses relative URLs, host header injection has no impact.
- **X-Forwarded-Host accepted but not used for link generation** — the header may be logged but not used in application logic. Test what the app actually does with it.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-host-header/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
