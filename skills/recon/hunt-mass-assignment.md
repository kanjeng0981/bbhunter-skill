---
name: hunt-mass-assignment
description: Hunt mass assignment via sensitive field injection and ORM framework exploitation.
scope: web2
---
Hunt mass assignment via sensitive field injection and ORM framework exploitation.

- API accepts JSON/XML/form body with fields beyond what the UI exposes.
- User profile updates, registration, checkout, or resource creation endpoints.
- Framework ORMs (Rails ActiveRecord, Laravel Eloquent, Django ORM, Mongoose, Prisma) where bulk assignment is the default.
- PATCH endpoints that accept sparse updates — may skip per-field authorization.

- **Some frameworks silently ignore unknown fields.** Try the same field with different naming conventions (snake_case, camelCase, PascalCase).
- **PATCH may be more permissive than PUT.** Test both methods — some frameworks apply different serializers per HTTP method.
- **GraphQL input types are self-documenting.** Use introspection to find all writable fields, then test for extras not in the schema.
- **Batch endpoints often skip per-item authorization.** Test with mixed arrays where only one item belongs to the attacker.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-mass-assignment/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
