---
name: cache-attack
description: Poison CDN cache or deceive when X-Cache header is detected.
scope: web2
---
Poison CDN cache or deceive when X-Cache header is detected.

- Target uses a CDN (CloudFront, Cloudflare, Fastly) or reverse proxy (Varnish, Nginx cache).
- Headers show X-Cache, Age, cf-cache-status, or X-Cache-Hits.
- After surface recon finds no direct vulnerabilities — pivot to infrastructure layer.
- Target allows file extension manipulation in URL paths (.css, .json, .js).

- **Reflection ≠ cache poisoning.** Just because a header is reflected doesn't mean it's CACHED. Always prove storage with a second request.
- **Cache buster is mandatory.** Never test without a unique cache buster per test, or you'll poison real user cache.
- **Cache Key Normalization.** CDNs may normalize URLs before caching. Test case variations, trailing slashes, and ignored parameters.
- **Fat GET smuggling.** Some CDNs accept 4000+ character query strings. The oversized request may be handled differently by origin vs cache.
- **Parameter Cloaking.** Duplicate parameters (e.g., ?p=1&p=2) may cause cache key confusion.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/cache-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
