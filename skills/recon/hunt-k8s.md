---
name: hunt-k8s
description: Hunt Kubernetes & Docker — API anonymous access, kubelet 10250 exec (SPDY/WebSocket, NOT plain POST) and the simpler /run primitive, etcd 2379 unauth, dashboard skip-login, RBAC misconfig, secret/SA-token abuse, docker.sock host escape, runc/container-escape (Leaky Vessels CVE-2024-21626), API-server-mediated nodes/proxy RCE, EphemeralContainers node-shell, bound/projected SA-token audience+expiry abuse, admission-controller bypass, Helm/Tiller remnants. Use when target runs containerized infra, exposes K8s ports (6443/10250/10255/2379/8443), or cloud metadata reveals K8s service accounts.
scope: web2
---
Hunt Kubernetes & Docker — API anonymous access, kubelet 10250 exec (SPDY/WebSocket, NOT plain POST) and the simpler /run primitive, etcd 2379 unauth, dashboard skip-login, RBAC misconfig, secret/SA-token abuse, docker.sock host escape, runc/container-escape (Leaky Vessels CVE-2024-21626), API-server-mediated nodes/proxy RCE, EphemeralContainers node-shell, bound/projected SA-token audience+expiry abuse, admission-controller bypass, Helm/Tiller remnants. Use when target runs containerized infra, exposes K8s ports (6443/10250/10255/2379/8443), or cloud metadata reveals K8s service accounts.

- **Anonymous kubelet access without pod exec** — read-only kubelet access is recon. Need pod exec, log exfil, or credential access.
- **etcd without auth but encrypted** — etcd may store encrypted secrets. Test secret decryption before claiming credential theft.
- **Kubernetes dashboard without login** — the dashboard's skip-login option is a known misconfiguration. Test actual pod exec, not just visibility.
- **RBAC enumeration without exploitation** — listing roles is informational. Need to demonstrate what the roles allow you to do.
- **Service account token without cluster-admin** — default service account tokens have limited permissions. Verify the token's actual permissions before claiming cluster takeover.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-k8s/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
