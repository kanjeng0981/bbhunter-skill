---
name: hunt-nextjs
description: Hunt Next.js specific vulnerabilities — Server Actions arbitrary function execution, Middleware auth bypass via static asset paths, ISR cache poisoning, Image Optimization SSRF (/_next/image), RSC payload leakage, getServerSideProps injection, source map exposure, debug endpoint leakage. Use when target runs Next.js 13/14/15 or any React SSR framework.
scope: web2
---
Hunt Next.js specific vulnerabilities — Server Actions arbitrary function execution, Middleware auth bypass via static asset paths, ISR cache poisoning, Image Optimization SSRF (/_next/image), RSC payload leakage, getServerSideProps injection, source map exposure, debug endpoint leakage. Use when target runs Next.js 13/14/15 or any React SSR framework.

- **Next.js source maps in production** — .map files in /_next/ are information disclosure (source code visibility), not RCE.
- **_next/data endpoint enumeration** — build ID + data endpoints expose server-side props. Test if sensitive data passes through getServerSideProps.
- **Middleware bypass** — Next.js middleware runs on Edge. Test if /api/ paths bypass middleware via direct access.
- **ISR cache poisoning** — Incremental Static Regeneration can be poisoned if revalidation triggers are controllable.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-nextjs/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
