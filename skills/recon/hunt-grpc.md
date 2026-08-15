---
name: hunt-grpc
description: Hunt gRPC vulnerabilities — server reflection enabled (enumerate all services/methods), missing authentication / metadata-stripping on internal endpoints, plaintext gRPC over HTTP/2, internal endpoint disclosure, proto file leakage, gRPC-Web/grpc-gateway transcoding injection, and HTTP/2 Rapid Reset DoS (CVE-2023-44487). Use when target exposes port 50051 / 443 / 8443 / 9090 with HTTP/2, when grpcurl/grpcui detects reflection, when an Envoy or grpc-gateway proxy is fronting a microservice, or when recon reveals a microservice architecture.
scope: web2
---
Hunt gRPC vulnerabilities — server reflection enabled (enumerate all services/methods), missing authentication / metadata-stripping on internal endpoints, plaintext gRPC over HTTP/2, internal endpoint disclosure, proto file leakage, gRPC-Web/grpc-gateway transcoding injection, and HTTP/2 Rapid Reset DoS (CVE-2023-44487). Use when target exposes port 50051 / 443 / 8443 / 9090 with HTTP/2, when grpcurl/grpcui detects reflection, when an Envoy or grpc-gateway proxy is fronting a microservice, or when recon reveals a microservice architecture.

- **gRPC reflection enabled without sensitive methods** — reflection is a design choice. Only report when it exposes internal/admin methods.
- **No TLS on gRPC** — plaintext gRPC on internal networks is common. Only a finding on public-facing services.
- **gRPC-Web proxy bypass** — the proxy translating gRPC-Web to gRPC may have different auth than the backend. Test both paths.
- **Protobuf fuzzing without crash** — malformed protobuf causing 500 is not necessarily exploitable. Need RCE or data leak from the crash.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-grpc/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
