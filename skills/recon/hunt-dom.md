---
name: hunt-dom
description: Hunt client-side DOM vulnerabilities — DOM Clobbering (overwrite JS globals via HTML injection), PostMessage hijacking (missing origin check), Service Worker abuse (intercept requests from same-origin script), CSS Injection/Exfiltration (attribute selectors → token char-by-char via OOB), client-side template injection, dangerouslySetInnerHTML. Grounded in named public research: Gareth Heyes / PortSwigger DOM-clobbering + DOM-Invader, Michał Bentkowski DOMPurify clobbering bypasses, jQuery htmlPrefilter XSS (CVE-2020-11022 / CVE-2020-11023), d0nut CSS-exfil research. Use when hunting DOM-XSS, client-side auth bypass, or token exfiltration without server-side interaction.
scope: web2
---
Hunt client-side DOM vulnerabilities — DOM Clobbering (overwrite JS globals via HTML injection), PostMessage hijacking (missing origin check), Service Worker abuse (intercept requests from same-origin script), CSS Injection/Exfiltration (attribute selectors → token char-by-char via OOB), client-side template injection, dangerouslySetInnerHTML. Grounded in named public research: Gareth Heyes / PortSwigger DOM-clobbering + DOM-Invader, Michał Bentkowski DOMPurify clobbering bypasses, jQuery htmlPrefilter XSS (CVE-2020-11022 / CVE-2020-11023), d0nut CSS-exfil research. Use when hunting DOM-XSS, client-side auth bypass, or token exfiltration without server-side interaction.

- **DOM XSS without sink confirmation** — finding innerHTML or document.write with user input is a potential sink, not a confirmed bug. Trace the full data flow from source to sink.
- **postMessage without origin check** — receiving postMessage events without verifying event.origin is the vulnerability. Test with window.postMessage(payload, '*').
- **Source maps without secrets** — .map files alone are informational. Need extracted API keys, internal paths, or credentials.
- **eval with static strings** — eval("constant") is not exploitable. Need dynamic input reaching eval.
- **Sanitizer bypass claim without proof** — claiming DOMPurify bypass requires a working payload against the specific version in use.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-dom/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
