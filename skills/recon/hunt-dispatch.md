---
name: hunt-dispatch
description: Skill-set loader for /hunt orchestrator. Fingerprints the target, picks the right platform attack skills, and loads the Red Team or WAPT skill set. Use when /hunt has just received a mode answer (redteam or wapt + blackbox|greybox) and needs to load the appropriate skills and print the taxonomy. Not for direct user invocation.
scope: web2
---
Skill-set loader for /hunt orchestrator. Fingerprints the target, picks the right platform attack skills, and loads the Red Team or WAPT skill set. Use when /hunt has just received a mode answer (redteam or wapt + blackbox|greybox) and needs to load the appropriate skills and print the taxonomy. Not for direct user invocation.

- **Wrong platform classification** — misidentifying a React app as Next.js or a Django app as Flask leads to loading wrong hunt-* skills. Always verify with multiple fingerprint signals.
- **Dispatch before scope confirmation** — loading hunt-* skills before confirming the target is in scope wastes time on out-of-scope assets.
- **Over-classification** — some apps don't fit neatly into one category. Multi-stack apps (React frontend + Django API) need both skill sets loaded.
- **Assuming framework version from headers** — X-Powered-By can be spoofed or removed. Cross-validate with JS bundle analysis, cookie names, and error page signatures.


---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-dispatch/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
