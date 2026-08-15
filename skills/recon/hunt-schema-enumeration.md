---
name: hunt-schema-enumeration
description: Enumerate hidden tables, fields, and endpoints via API error hints. Agnostic across PostgREST, Zod, FastAPI, GraphQL, and REST.
scope: web2
---
Enumerate hidden tables, fields, and endpoints via API error hints. Agnostic across PostgREST, Zod, FastAPI, GraphQL, and REST.

The target API returns structured error messages (JSON) that hint at valid table names, field names, or endpoint paths. This is the single most productive black-box recon technique for REST/GraphQL APIs — one fuzz request reveals the entire database schema.

Most common on: PostgREST (Supabase), FastAPI (.NET), Zod (Next.js/Node), tRPC, GraphQL, and any framework with validation error details enabled in production.

---

- **Schema enumeration without sensitive fields** — knowing the API schema is recon. Need to demonstrate exploitable fields/mutations.
- **GraphQL schema via introspection** — introspection is a feature, not a bug (unless explicitly disabled in production).
- **Database schema via error messages** — SQL errors revealing table names is information disclosure, not schema-specific. Rate based on what's disclosed.
- **OpenAPI spec publicly accessible** — /swagger.json or /openapi.json is intentionally public for API consumers. Rate based on exposed admin/internal endpoints.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-schema-enumeration/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
