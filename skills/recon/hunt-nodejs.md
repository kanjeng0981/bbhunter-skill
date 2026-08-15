---
name: hunt-nodejs
description: Hunt Node.js specific vulnerabilities — Prototype Pollution → RCE chains (lodash/merge/assign), Express trust proxy misconfiguration, child_process/eval injection, template engine SSTI (EJS/Pug/Handlebars), path traversal in file servers, require() injection, environment variable exfil via /proc/self/environ. Use when target runs Node.js/Express/Fastify/NestJS/Koa.
scope: web2
---
Hunt Node.js specific vulnerabilities — Prototype Pollution → RCE chains (lodash/merge/assign), Express trust proxy misconfiguration, child_process/eval injection, template engine SSTI (EJS/Pug/Handlebars), path traversal in file servers, require() injection, environment variable exfil via /proc/self/environ. Use when target runs Node.js/Express/Fastify/NestJS/Koa.

- **Prototype pollution without gadget** — __proto__ injection is a primitive. Need a gadget chain to RCE, auth bypass, or XSS.
- **eval with static input** — eval("'use strict'; ...") is not exploitable. Need dynamic, user-controllable input.
- **child_process without user input** — exec("ls -la") is not exploitable unless the command includes user input.
- **Server-Side JavaScript Injection (SSJI)** — different from prototype pollution. Distinguish the two attack classes.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-nodejs/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
