---
name: hunt-fastapi
description: Hunt FastAPI-specific vulnerabilities: dependency injection gaps, Pydantic coercion, and OpenAPI mining.
scope: web2
---
Hunt FastAPI-specific vulnerabilities: dependency injection gaps, Pydantic coercion, and OpenAPI mining.

- Target uses FastAPI (indicated by /docs, /redoc, /openapi.json, or server: uvicorn).
- OpenAPI schema is publicly accessible.
- API uses dependency injection (Depends) for authorization.
- WebSocket endpoints exist alongside REST API.
- Application uses Pydantic v1 or v2 for request validation.

- **Pydantic v2 model_config with extra='ignore' silently drops unknown fields.** Test both Pydantic v1 and v2 behavior.
- **OpenAPI schema may be restricted.** If /openapi.json returns 403, try /docs and /redoc which serve the same data.
- **FastAPI Depends with Security is NOT the same as Depends.** Security integrates with OpenAPI security schemes — but both can be misconfigured.
- **Uvicorn --proxy-headers must be enabled for IP spoofing to work.** Check with X-Forwarded-For — if the server sees your real IP, proxy headers are disabled.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-fastapi/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
