---
name: js-secrets-extraction
description: Analyze JS bundles and source maps for hardcoded secrets, API keys, JWTs, and internal endpoints
scope: web2
---
Analyze JS bundles and source maps for hardcoded secrets, API keys, JWTs, and internal endpoints

# JS Bundle & Source Map Analysis -- Secret Extraction

## When to Use

- **ALWAYS** after initial web enumeration
- When you find modern SPA (React, Angular, Vue)
- When target uses Firebase, Supabase, Auth0
- Higher yield than directory scanning on many targets

## Why Analyze JS Bundles

Modern JavaScript bundles (Webpack, Vite, esbuild) often contain:
- Hardcoded API keys and tokens
- Internal API URLs
- Firebase, Auth0, Supabase configurations
- Environment variables (VITE_*, REACT_APP_*, NEXT_PUBLIC_*)
- Internal routes

## Bundle Download and Analysis



## Source Map Reconstruction



**Real-world case**: Enterprise Angular SPA admin, 2 JS bundles (250KB each) exposed:
- Internal API URL (apiv3.empresa.com.br)
- Firebase API key (AIzaSy...2GXA)
- Encryption keys (AD5oDjsJaTJOzLe1Llj9mz)
- Cloudinary upload endpoint

## Port-Specific URL Analysis

Modern deployments often serve the main SPA on port 443 and admin/API on separate ports (8080, 8081, 8084). **Always check JS bundles on ALL discovered ports:**



Source maps on administrative or alternate-port applications may expose a
different route and configuration set from the public SPA. Analyze each
authorized application independently.

## Admin Portal JS Analysis Pattern

When you find an admin portal on a separate port, the JS bundle often contains different secrets than the main site:



## Source Map Content Analysi
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/js-secrets-extraction/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
