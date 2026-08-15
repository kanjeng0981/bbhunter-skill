---
name: hunt-supabase
description: Hunt Supabase exploitation — Supabase anon key discovery in JS bundles, REST API table enumeration with anon key, Row Level Security (RLS) bypass via missing organization_id check, RPC function abuse returning cross-organization data, Storage bucket listing, Auth signUp/signIn with anon key, multi-tenant enumeration via WHOIS, bucket file upload/download without auth. Built from field observation of Lovable.dev + Supabase stack on rapidly-built platforms where RLS policies are consistently misconfigured. Use when a JS bundle, .env, or APK reveals a Supabase URL (project.supabase.co) and anon key (eyJ...).
scope: web2
---
Hunt Supabase exploitation — Supabase anon key discovery in JS bundles, REST API table enumeration with anon key, Row Level Security (RLS) bypass via missing organization_id check, RPC function abuse returning cross-organization data, Storage bucket listing, Auth signUp/signIn with anon key, multi-tenant enumeration via WHOIS, bucket file upload/download without auth. Built from field observation of Lovable.dev + Supabase stack on rapidly-built platforms where RLS policies are consistently misconfigured. Use when a JS bundle, .env, or APK reveals a Supabase URL (project.supabase.co) and anon key (eyJ...).

- **Supabase anon key exposure** — the anon key is intentionally public. It grants RLS-restricted access. The finding is when RLS policies are missing.
- **Public bucket with RLS bypass** — if RLS policies allow public read on storage, that's intentional. Need access to data that should be private.
- **Supabase URL + anon key as credential** — these are configuration values, not secrets. Rate impact based on what the anon key can access via missing RLS.
- **Supabase realtime subscription without sensitive data** — subscribing to public channels is expected. Need subscription to private channels.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-supabase/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
