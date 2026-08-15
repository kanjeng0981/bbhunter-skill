---
name: hunt-nosqli
description: Hunt NoSQL Injection — MongoDB operator injection ($where, $regex, $gt, $ne), CouchDB, Redis command injection, auth bypass via NoSQLi, data dump. Use when target uses MongoDB/Mongoose, CouchDB, Redis, or shows NoSQL error messages.
scope: web2
---
Hunt NoSQL Injection — MongoDB operator injection ($where, $regex, $gt, $ne), CouchDB, Redis command injection, auth bypass via NoSQLi, data dump. Use when target uses MongoDB/Mongoose, CouchDB, Redis, or shows NoSQL error messages.

- **NoSQL injection without data exfiltration** — blind NoSQLi returning true/false is harder to exploit. Need data extraction or auth bypass.
- **$regex injection without enumeration proof** — if $regex is injectable, demonstrate time-based or boolean-based data extraction.
- **MongoDB $where injection** — $where evaluates JavaScript. This is the highest-impact NoSQL injection variant.
- **Operator injection vs value injection** — injecting {"$gt":""} in a value field vs injecting operators in the query structure are different attack types.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-nosqli/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
