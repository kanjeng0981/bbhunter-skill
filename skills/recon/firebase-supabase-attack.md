---
name: firebase-supabase-attack
description: Exploit Firebase/Supabase for data via JS config leak probe.
scope: web2
---
Exploit Firebase/Supabase for data via JS config leak probe.

- JavaScript bundle analysis reveals Firebase config (apiKey, projectId) or Supabase URL + anon key.
- Target uses a modern SPA (React, Vue, Angular) with BaaS backend.
- After js-secrets-extraction finds Firebase/Supabase identifiers.
- After source-leak-hunt finds .env with FIREBASE_* or SUPABASE_* variables.

- **Anon key is NOT a secret.** It's designed to be public. The vulnerability is missing RLS, not the key exposure itself.
- **Firestore rules may allow reads but not writes.** Test SELECT, INSERT, UPDATE, DELETE separately.
- **Supabase RLS may protect some tables but not others.** Test every table independently.
- **Firebase Auth signup may require email verification.** Check if the app auto-confirms emails (many do).
- **Rate limiting on Firestore REST API.** Spread requests 0.5-1s apart for large extractions.
- **API key in JS bundle may be truncated/redacted.** The key string visible in the minified bundle may show AIzaSy...USd4 or similar truncation. This happens when the bundler splits the key across multiple string literals or when the key references a variable defined elsewhere. If the Firebase API tests return "API key not valid", the key may be a partial match from the regex. Extract the surrounding context (50+ chars on each side) to find the complete key.
- **Firebase project may not be deployed.** The Firebase project ID (e.g., medxgo-2e637) may exist in the GCP project registry but have no de
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/firebase-supabase-attack/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
