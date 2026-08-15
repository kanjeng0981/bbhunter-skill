---
name: hunt-firebase
description: Hunt Firebase / Firestore / GCP exploitation — Firebase API key discovery in JS bundles, anonymous auth via signUp endpoint, Firestore collection enumeration with anon key, Realtime Database read/write without auth, Firebase Storage bucket listing, Firebase Hosting detection, GCP service account JSON exploitation, IAM policy enumeration from leaked SA keys. Built from field experience where Firebase API keys in JS bundles unlocked full Firestore read-access on 12+ targets including healthcare platforms and delivery apps. Use when a JS bundle, APK, or .env file reveals a Firebase API key (AIzaSy...) or when target uses firebaseio.com / firestore.googleapis.com endpoints.
scope: web2
---
Hunt Firebase / Firestore / GCP exploitation — Firebase API key discovery in JS bundles, anonymous auth via signUp endpoint, Firestore collection enumeration with anon key, Realtime Database read/write without auth, Firebase Storage bucket listing, Firebase Hosting detection, GCP service account JSON exploitation, IAM policy enumeration from leaked SA keys. Built from field experience where Firebase API keys in JS bundles unlocked full Firestore read-access on 12+ targets including healthcare platforms and delivery apps. Use when a JS bundle, APK, or .env file reveals a Firebase API key (AIzaSy...) or when target uses firebaseio.com / firestore.googleapis.com endpoints.

- **Public Firebase config without sensitive data** — the Firebase config object is intentionally public. Only report when the database/storage is writable or contains PII.
- **Realtime DB rules test without write** — reading .json is recon. Writing to .json and having it persist proves misconfiguration.
- **Firestore public read** — test /documents/users for PII, not /documents/public_config.
- **Storage bucket listing without object read** — listable buckets are informational. Need readable objects with sensitive content.
- **API key scope testing** — Firebase API keys are not secrets. They're identifiers. Test what the key grants access to, not just that it exists.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-firebase/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
