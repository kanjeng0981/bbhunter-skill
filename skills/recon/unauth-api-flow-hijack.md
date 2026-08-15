---
name: unauth-api-flow-hijack
description: Exploit unauthenticated multi-step API flows without credentials.
scope: web2
---
Exploit unauthenticated multi-step API flows without credentials.

- An API serves a multi-step workflow (start → step1 → step2 → ... → complete).
- No authentication token, session cookie, or API key is required at any step.
- The API returns session identifiers (UUIDs, tokens) that can be reused across steps.
- The workflow includes file upload, data submission, or export functionality.
- Error messages reveal the expected request format (validating that endpoints are live).

- **Rate limiting kills the flow.** Multi-step APIs often have per-IP rate limits. Slow down between steps (0.5-1s delay).
- **State expires.** Some flows invalidate session IDs after a timeout. If steps start failing, restart the flow.
- **Validation gates exist.** The API may require valid data formats (email, phone, file type). Read error messages carefully — they tell you exactly what format is expected.
- **Not every step is POST.** Some flows use GET for status checks, PUT for updates, and DELETE for cancellation. Test all methods.
- **The export may be empty.** A freshly started flow produces an empty export. Run through the full flow before testing export.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/unauth-api-flow-hijack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
