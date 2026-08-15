---
name: hunt-subdomain
description: Hunting skill for subdomain takeover vulnerabilities. Includes modern provider fingerprints — Microsoft Azure DevOps `cloudapp.azure.com` regional-pool re-issue (1-click OAuth ATO via wildcard `reply_to`, Binary Security), Zendesk help-desk takeover → email interception → password reset chain (0xprial writeup), Vercel `cname.vercel-dns.com` deleted-project takeover, plus general Fastly CDN service re-attach and S3 dangling-bucket cookie-scope techniques. Use when hunting subdomain takeover — emphasis on ATO-chain primitives (OAuth `redirect_uri`, cookie-domain, email DNS).
scope: web2
---
Hunting skill for subdomain takeover vulnerabilities. Includes modern provider fingerprints — Microsoft Azure DevOps `cloudapp.azure.com` regional-pool re-issue (1-click OAuth ATO via wildcard `reply_to`, Binary Security), Zendesk help-desk takeover → email interception → password reset chain (0xprial writeup), Vercel `cname.vercel-dns.com` deleted-project takeover, plus general Fastly CDN service re-attach and S3 dangling-bucket cookie-scope techniques. Use when hunting subdomain takeover — emphasis on ATO-chain primitives (OAuth `redirect_uri`, cookie-domain, email DNS).

1. **Service offboarding without DNS cleanup** — Developer removes a Heroku app, UserVoice account, or WordPress site but never deletes the CNAME record. DNS lives forever; service does not.

2. **Staging/preview infrastructure abandoned post-launch** — course., new., preview., beta. subdomains provisioned for a product launch, pointed at a third-party, then forgotten when the campaign ends.

3. **Subdomain provisioned by a third-party team** — Marketing sets up a UserVoice or Zendesk subdomain via IT, product sunset kills it, but DNS is owned by engineering who doesn't know.

4. **CDN misconfiguration without origin validation** — Fastly and similar CDNs historically allowed any domain to "claim" a backend hostname by creating a service pointing to it. Unregistered origin hostnames become claimable.

5. **GitHub/GitLab Pages namespace not reserved** — Organization renames, user accounts deleted, or repos
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-subdomain/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
