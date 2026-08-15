---
name: hunt-cicd
description: Hunt CI/CD pipeline vulnerabilities — GitHub Actions workflow injection (pull_request_target Pwnrequest + ${{ }}-into-shell), self-hosted runner poisoning, OIDC trust-policy abuse, Jenkins script-console RCE and CVE-2024-23897 file read, GitLab CI runner-token registration, Terraform state file leakage, artifact/log secret leakage, pipeline env-var disclosure. Use when target has a public GitHub/GitLab org, exposed CI dashboards (Jenkins/TeamCity/Drone/Argo), or build artifacts/images are reachable.
scope: web2
---
Hunt CI/CD pipeline vulnerabilities — GitHub Actions workflow injection (pull_request_target Pwnrequest + ${{ }}-into-shell), self-hosted runner poisoning, OIDC trust-policy abuse, Jenkins script-console RCE and CVE-2024-23897 file read, GitLab CI runner-token registration, Terraform state file leakage, artifact/log secret leakage, pipeline env-var disclosure. Use when target has a public GitHub/GitLab org, exposed CI dashboards (Jenkins/TeamCity/Drone/Argo), or build artifacts/images are reachable.

- **Exposed .git/config without object access** — a 200 on /.git/config proves the repo is reachable, but without /.git/objects/ access you can't extract source. Test both paths.
- **CI/CD log leakage** — build logs often contain secrets (API keys, tokens) but are only visible to authenticated users. Test both anonymous and authenticated access.
- **Pipeline injection without execution proof** — injecting into a pipeline YAML or Jenkinsfile doesn't prove execution. Need confirmation that the pipeline actually ran your code.
- **GitHub Actions workflow_dispatch** — if the action has workflow_dispatch trigger, it can be triggered via API. Test if the trigger is restricted to specific branches or users.
- **Container registry misconfig** — public container images may contain build secrets, source code, or credentials. Always pull and inspect the layers.
- **Artifact poisoning across builds** — if build artifacts are stored without per-build isolation, a previous build's artifacts ma
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-cicd/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
