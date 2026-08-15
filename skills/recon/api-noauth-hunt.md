---
name: api-noauth-hunt
description: Use when an API may expose data or privileged operations without authentication.
scope: web2
---
Use when an API may expose data or privileged operations without authentication.

- Port scan reveals HTTP services on non-standard ports (3000, 5000, 8080-8085, 9000).
- Target has an API subdomain (api.target.com, backend.target.com).
- JavaScript bundles reference internal API endpoints.
- After port-service-discovery finds HTTP on unexpected ports.
- After firebase-supabase-attack identifies backend APIs.

- **HTTP 200 ≠ API.** Some services return HTML on unexpected paths. Verify JSON content type.
- **Pagination can turn validation into collection.** Request the smallest page
  that proves the access-control failure. Do not enumerate the dataset.
- **POST, PATCH, PUT, and DELETE change state.** Require explicit authorization
  and operate only on a synthetic object created for the test.
- **Authentication tests can lock accounts or trigger alerts.** Use approved
  test identities and the agreed request rate.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/api-noauth-hunt/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
