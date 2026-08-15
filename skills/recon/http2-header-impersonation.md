---
name: http2-header-impersonation
description: Spoof HTTP/2 SETTINGS frames and pseudo-header order per browser profile.
scope: web2
---
Spoof HTTP/2 SETTINGS frames and pseudo-header order per browser profile.

- TLS fingerprint is correct but target still detects non-browser HTTP behavior.
- Target uses HTTP/2-specific detection (SETTINGS frame analysis, pseudo-header order).
- Need browser-accurate sec-ch-ua, Accept, Accept-Encoding, Priority, and sec-fetch-* headers.
- Mobile API endpoints require Android OkHttp header profiles.
- Combining with TLS impersonation for a complete network-level browser profile.

- **curl cannot spoof HTTP/2 SETTINGS frames.** Only use curl-based headers for HTTP/1.1 targets or when TLS fingerprinting is the primary concern, not HTTP/2.
- **Header order matters in HTTP/2.** Some detectors check the order of header fields, not just their presence.
- **sec-ch-ua must match User-Agent.** Using Chrome headers with Firefox UA creates an inconsistency that detectors flag.
- **sec-ch-ua format is version-specific.** Chrome 100+ uses different brand strings than Chrome 124+.
- **Mobile headers without TLS matching is detectable.** Using Safari iOS headers over a desktop TLS fingerprint is flagged.
- **Custom headers are deduplicated case-insensitively.** Adding User-Agent as custom overrides the fingerprint's User-Agent.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/http2-header-impersonation/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
