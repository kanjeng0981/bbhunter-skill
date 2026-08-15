---
name: hunt-cloud-misconfig
description: Hunt cloud / infrastructure misconfigurations. AWS: public S3 buckets (s3:GetObject anonymous), permissive bucket policies (PutObjectAcl public-write), exposed CloudFront origin, public Lambda function URL, public RDS snapshot, IAM credentials in JS bundles, AWS metadata accessible via SSRF. GCP: public GCS buckets, exposed Cloud Run services, leaked service account JSON. Azure: public blob containers, exposed Function App. (Kubernetes/Docker exposure is owned by hunt-k8s; CI/CD pipeline attacks by hunt-cicd; post-credential IAM escalation by cloud-iam-deep.) Detection: targeted dorking, certificate transparency, JS bundle secret extraction, port scan for known service ports. Validate: actual data read / write / RCE. Use when hunting cloud-native storage and compute misconfig (S3/GCS/Blob, IMDS-via-SSRF, serverless, public managed services).
scope: web2
---
Hunt cloud / infrastructure misconfigurations. AWS: public S3 buckets (s3:GetObject anonymous), permissive bucket policies (PutObjectAcl public-write), exposed CloudFront origin, public Lambda function URL, public RDS snapshot, IAM credentials in JS bundles, AWS metadata accessible via SSRF. GCP: public GCS buckets, exposed Cloud Run services, leaked service account JSON. Azure: public blob containers, exposed Function App. (Kubernetes/Docker exposure is owned by hunt-k8s; CI/CD pipeline attacks by hunt-cicd; post-credential IAM escalation by cloud-iam-deep.) Detection: targeted dorking, certificate transparency, JS bundle secret extraction, port scan for known service ports. Validate: actual data read / write / RCE. Use when hunting cloud-native storage and compute misconfig (S3/GCS/Blob, IMDS-via-SSRF, serverless, public managed services).

- **S3 bucket listing without read access** — finding a listable bucket is recon, not a vulnerability. Need to demonstrate readable objects with sensitive content.
- **Firebase public read without sensitive data** — an open Firebase RTDB with only public app config is informational. Need PII, credentials, or internal data.
- **GCP/Azure storage without credential impact** — public blob storage containing static assets is not a finding. Need secrets, source code, or customer data.
- **Cloud metadata endpoint accessible from outside** — SSRF to 192.0.2.1 is only exploitable from inside the cloud. External access to metadata is a different
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-cloud-misconfig/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
