---
name: hunt-cache-poison
description: Hunting skill for cache poison vulnerabilities. Built from 10 public bug bounty reports including X-Forwarded-Host poisoning, X-HTTP-Method-Override / GCS cache, reflected→stored XSS via cache, classic Omer-Gil Web Cache Deception, Cloudflare Cache Deception Armor bypass, session-token cache deception, Akamai hop-by-hop smuggling → server-side edge poisoning, and Kettle's 2024 path-normalization WCD against Cloudflare/Fastly/GCP. Use when hunting cache poisoning, Web Cache Deception, CDN-fronted apps.
scope: web2
---
Hunting skill for cache poison vulnerabilities. Built from 10 public bug bounty reports including X-Forwarded-Host poisoning, X-HTTP-Method-Override / GCS cache, reflected→stored XSS via cache, classic Omer-Gil Web Cache Deception, Cloudflare Cache Deception Armor bypass, session-token cache deception, Akamai hop-by-hop smuggling → server-side edge poisoning, and Kettle's 2024 path-normalization WCD against Cloudflare/Fastly/GCP. Use when hunting cache poisoning, Web Cache Deception, CDN-fronted apps.

1. **CDN misconfiguration — caching based on URL path only.** Engineers configure cache rules like "cache everything matching *.js" without realizing the path can be appended to dynamic routes. The origin server ignores the extra path segments, but the CDN uses them as cache keys.

2. **Unkeyed header forwarding.** Developers configure reverse proxies to forward X-Forwarded-Host to backends for URL generation (canonical links, redirects, password reset emails) without including it in the cache key. The CDN caches the poisoned response.

3. **Web Cache Deception via permissive routing.** Frameworks that normalize URLs (e.g., Rails, Express) accept /account/settings.css and serve the same response as /account/settings. The CDN sees a .css extension and applies aggressive caching rules.

4. **Shared caching of multi-tenant responses.** SaaS platforms that use a single CDN without tenant isolation in the cache key allow cross-tenant cache poisoning.

5. **Error responses cached wit
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-cache-poison/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
