---
name: hunt-prototype-pollution
description: Hunt client-side and server-side prototype pollution for XSS, auth bypass, and RCE.
scope: web2
---
Hunt client-side and server-side prototype pollution for XSS, auth bypass, and RCE.

- Application uses JavaScript/Node.js with object merge, clone, or extend operations on user input.
- jQuery $.extend(true, ...) or $.fn.merge() with deep copy on untrusted data.
- Lodash _.merge(), _.defaultsDeep(), _.set() receiving request body/query params.
- Template engines (EJS, Pug, Handlebars) in the same runtime as user-controlled objects.
- Server-side Node.js with child_process.exec/spawn accessible via polluted options.

- **Not every __proto__ in a request is a finding.** Only report when the polluted property actually affects application behavior.
- **Node.js 12+ and newer lodash versions have partial mitigations.** Test with older versions first.
- **Server-side pollution requires a gadget.** Polluting random objects without reaching a sink (exec, eval, template) has no impact.
- **BlackFan's client-side prototype pollution catalog** is the canonical reference — cross-check findings against it.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-prototype-pollution/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
