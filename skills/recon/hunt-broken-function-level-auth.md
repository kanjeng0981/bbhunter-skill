---
name: hunt-broken-function-level-auth
description: Hunt broken function-level authorization via verb drift, route shadowing, and transport gaps.
scope: web2
---
Hunt broken function-level authorization via verb drift, route shadowing, and transport gaps.

- API has distinct user roles (admin, moderator, user) but role checks are per-controller, not per-method.
- Legacy or deprecated endpoints still served behind updated middleware.
- GraphQL, gRPC, and WebSocket transports exist alongside REST APIs without authorization parity.
- Feature flags or beta endpoints expose functionality before security review.
- Batch/job endpoints accept internal requests without role verification.

- **405 Method Not Allowed ≠ no auth.** The method must exist AND lack authorization to be a finding.
- **Route shadowing requires the shadow endpoint to accept authenticated requests.** A public user-info endpoint is not a finding.
- **GraphQL deleteUser on a consumer-facing mutation is an IDOR, not BFLA.** BFLA is about action-level privileges, not object ownership.
- **WebSocket authorization bypass requires proof that the WS handler skips REST middleware checks.** Compare WS vs REST for the same action.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-broken-function-level-auth/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
