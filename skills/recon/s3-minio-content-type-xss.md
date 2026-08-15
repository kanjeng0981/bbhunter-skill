---
name: s3-minio-content-type-xss
description: Exploit public bucket Content-Type override for stored XSS on target origin.
scope: web2
---
Exploit public bucket Content-Type override for stored XSS on target origin.

- Target serves user-uploaded files (images, avatars, attachments) from a public bucket.
- Files are served under the target's own domain or subdomain (not a random storage domain).
- Upload validation appears solid (extension whitelist, magic byte check, forced Content-Type) — the override bypasses all of these at serve time, not upload time.
- The bucket URL responds to ?response-content-type= with a changed Content-Type.
- The bucket returns an AWS SignatureDoesNotMatch error leaking the real bucket host and region.

- **Cross-origin buckets have low impact.** If the bucket is on s3.amazonaws.com or a random storage domain, the XSS executes in an isolated origin with no access to the target's session.
- **The override must be supported.** Not all storage systems honor response override parameters. S3-compatible systems other than AWS/MinIO may use different parameter names.
- **Upload validation still matters for payload delivery.** The file must pass upload-time checks to reach the bucket. Use polyglot files that satisfy both the validator and the browser.
- **The signed S3 URL expires.** Generated presigned URLs have a configurable expiration. The XSS link stops working after expiry.
- **CloudFront/CDN may cache the original Content-Type.** If a CDN sits in front of the bucket, it may ignore query parameter overrides. Test both the CDN URL and the direct bucket URL.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/s3-minio-content-type-xss/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
