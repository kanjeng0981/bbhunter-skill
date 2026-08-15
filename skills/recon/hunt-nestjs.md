---
name: hunt-nestjs
description: Hunt NestJS-specific vulnerabilities: guard bypass, decorator gaps, and microservice auth drift.
scope: web2
---
Hunt NestJS-specific vulnerabilities: guard bypass, decorator gaps, and microservice auth drift.

- Target uses NestJS (indicated by x-powered-by: NestJS or TypeScript decorator patterns in error messages).
- GraphQL endpoints exist alongside REST API.
- Microservice transports (TCP, Redis, NATS, MQTT, gRPC) are configured.
- Swagger/OpenAPI docs are exposed at /api or /api-json.
- CRUD endpoints follow predictable NestJS naming conventions.

- **NestJS Swagger module may expose all endpoints regardless of auth.** Always check /api-json for hidden endpoints.
- **@Public() decorator is framework-specific (not built into NestJS).** Different projects use @SkipAuth(), @NoAuth(), or @AllowAnonymous().
- **Microservice transports often run on internal ports.** Test from within the target network if possible.
- **@Res({ passthrough: true }) bypasses the standard response pipeline.** Response headers and status codes can be injected.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-nestjs/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
