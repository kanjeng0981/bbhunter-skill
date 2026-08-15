---
name: hunt-api-misconfig
description: Hunt API security misconfiguration — mass assignment, JWT attacks, prototype pollution, HTTP verb tampering. Mass assignment: send {is_admin:true, role:admin, verified:true} on profile/account/reset endpoints — server blindly applies. JWT: alg=none, weak HMAC bruteforce, kid path traversal, JWK injection, token confusion. Prototype pollution: __proto__ injection in JSON merge / Object.assign / lodash _.merge → polluted prototype reaches sink (RCE in Node, XSS in browser). HTTP verb: GET-bypass-CSRF, X-HTTP-Method-Override, TRACE enabled. Detection: API responses with extra fields, JWTs in headers (decode at jwt.io). CORS misconfiguration (reflect-any-origin, null origin, subdomain-regex bypass, postMessage) is owned by hunt-cors. Use when hunting API misconfigs, JWT flaws, mass-assignment, prototype pollution.
scope: web2
---
Hunt API security misconfiguration — mass assignment, JWT attacks, prototype pollution, HTTP verb tampering. Mass assignment: send {is_admin:true, role:admin, verified:true} on profile/account/reset endpoints — server blindly applies. JWT: alg=none, weak HMAC bruteforce, kid path traversal, JWK injection, token confusion. Prototype pollution: __proto__ injection in JSON merge / Object.assign / lodash _.merge → polluted prototype reaches sink (RCE in Node, XSS in browser). HTTP verb: GET-bypass-CSRF, X-HTTP-Method-Override, TRACE enabled. Detection: API responses with extra fields, JWTs in headers (decode at jwt.io). CORS misconfiguration (reflect-any-origin, null origin, subdomain-regex bypass, postMessage) is owned by hunt-cors. Use when hunting API misconfigs, JWT flaws, mass-assignment, prototype pollution.

- **Mass assignment without side effects** — sending {is_admin:true} and getting 200 doesn't prove the field was applied. Verify by reading back the profile and confirming the escalated value persists.
- **JWT alg:none only on test servers** — many production JWKS endpoints enforce algorithm validation. Test with the actual production token endpoint, not localhost.
- **Prototype pollution without a sink** — polluting __proto__ proves nothing unless you can reach a gadget (RCE sink, XSS sink, or auth bypass via polluted comparison). Map the pollution to a specific exploitable side effect.
- **HTTP verb tampering on read-only endpoints** — bypassing CSRF via GET on a rea
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-api-misconfig/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
