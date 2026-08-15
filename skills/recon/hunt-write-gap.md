---
name: hunt-write-gap
description: Hunt read-protected write-gaping endpoints. PATCH/POST/DELETE without authorization while GET is protected. Agnostic: Supabase, Firebase, REST, GraphQL.
scope: web2
---
Hunt read-protected write-gaping endpoints. PATCH/POST/DELETE without authorization while GET is protected. Agnostic: Supabase, Firebase, REST, GraphQL.

You have authenticated access to a target and can READ your own data (profile, settings, records), but need to test if you can MODIFY data beyond your authorization level. This is the #1 pattern in Supabase-backed SaaS and increasingly common in Firebase, custom REST APIs, and GraphQL backends.

**The pattern**: GET /resource returns only your data (RLS/auth working). PATCH /resource lets you change anything including tier, role, balance, and subscription status.

---

- **Write-what-where primitive without exploitation** — the ability to write arbitrary data to arbitrary addresses is the finding. Need to demonstrate what the write achieves.
- **Race condition write vs atomic write** — if the write is atomic (single instruction), it may not be exploitable. Need a race window.
- **File write without execution** — writing to disk is a primitive. Need ability to execute the written content (web shell, cron job, DLL hijack).
- **Memory corruption write without control** — crashing the server isn't a finding. Need controlled write with predictable impact.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-write-gap/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
