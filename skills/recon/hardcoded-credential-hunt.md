---
name: hardcoded-credential-hunt
description: Detect hardcoded passwords in HTML forms, JavaScript, and API responses.
scope: web2
---
Detect hardcoded passwords in HTML forms, JavaScript, and API responses.

- An application serves HTML forms with pre-filled or hidden password fields.
- A configuration endpoint (/api/config, /env, /settings) returns JSON with credential-like strings.
- A debug/error page leaks application secrets in JavaScript variables.
- An unauthenticated API endpoint returns data that controls authentication (reset, exit registration, admin actions).
- JavaScript bundles contain string assignments matching password patterns.

- **Placeholder values look real.** Test password123, changeme, and empty strings before reporting — they are often development defaults.
- **The credential may be scoped.** A password for "exit registration" is not a full admin password. Map the credential to its actual permissions before scoring.
- **Form values may be dynamic.** Check if the password changes per session (CSRF token pattern) vs. being truly static.
- **Base64 is not encryption.** Decode any base64-looking strings found in JavaScript — they frequently contain credentials.
- **Rate limiting may block testing.** Space authentication attempts 2-3 seconds apart.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/hardcoded-credential-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
