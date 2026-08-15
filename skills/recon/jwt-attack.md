---
name: jwt-attack
description: Decode, forge, brute JWTs when Bearer auth header is seen.
scope: web2
---
Decode, forge, brute JWTs when Bearer auth header is seen.

- API uses Authorization: Bearer eyJ... headers.
- JavaScript bundles contain eyJ... token patterns.
- After js-secrets-extraction finds JWT tokens.
- After api-noauth-hunt needs token forging for auth bypass.
- Cookies contain jwt=, token=, or session= with base64-encoded values.

- **alg:none is rare.** Most JWT libraries reject it by default since 2017. But legacy apps exist.
- **RS256→HS256 requires the PUBLIC key.** This is usually available at /.well-known/jwks.json or in JS bundles.
- **Brute force is slow in Python.** Use hashcat -m 16500 for HS256 or john for production-speed cracking.
- **Laravel Passport uses jti validation.** Even if you forge a valid JWT, Passport checks if the jti (JWT ID) exists in the database.
- **Auth0/Firebase use JWKS.** The server fetches the public key from /.well-known/jwks.json — alg:none won't work because the server always verifies with the public key.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/jwt-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
