---
name: tls-fingerprint-impersonation
description: Spoof TLS ClientHello and JA4 fingerprints for browser impersonation.
scope: web2
---
Spoof TLS ClientHello and JA4 fingerprints for browser impersonation.

- Target returns 403/blocked on curl/httpx even with correct User-Agent headers.
- Cloudflare or Akamai is fingerprinting TLS ClientHello (JA3/JA4 mismatch with browser).
- API probing requires mobile-app impersonation (OkHttp fingerprint for Android).
- Need high-throughput HTTP requests that pass TLS fingerprint checks without running a full browser.
- Target shows different behavior based on TLS fingerprint (mobile vs desktop endpoints).

- **Not all sites use TLS fingerprinting.** Test with curl first — if it works, TLS fingerprinting is not the blocker.
- **Fingerprint must match User-Agent.** Using Chrome TLS with Firefox UA headers will be detected.
- **HTTP/1.1-only sites don't use HTTP/2 impersonation.** The with_http3() flag only matters for sites that support it.
- **OkHttp 3 is TLS 1.2 only.** Some modern servers reject TLS 1.2 connections.
- **TLS fingerprint caching means first request is slowest.** CryptoProvider instances are cached per fingerprint — subsequent requests are fast.
- **Vanilla fallback may leak your real TLS fingerprint.** Disable vanilla_fallback if stealth is critical.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/tls-fingerprint-impersonation/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
