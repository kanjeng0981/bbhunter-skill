---
name: port-mass-scan
description: Port scan /8-/24 with Masscan+RustScan and nmap banners.
scope: web2
---
Port scan /8-/24 with Masscan+RustScan and nmap banners.

- Authorized red team engagement with signed RoE covering the target IP range.
- Fast single-host port discovery before Nmap service enumeration.
- After subdomain-enumeration — scan resolved IPs for non-HTTP services.
- ISP-wide or /8 scanning without explicit written authorization is illegal in most jurisdictions. This skill exists for legitimate authorized engagements, not mass scanning.

- **Masscan requires root.** Uses raw sockets. Run as root or with sudo.
- **Rate > 100k may trigger IDS/IPS.** Use --rate=50000 or lower for stealth. Use -T4 equivalent by setting appropriate --rate.
- **Banner grabbing kills connections.** Without --source-ip, Masscan must complete a full TCP handshake which tears down the connection. Use the two-phase approach (Masscan ports → Nmap services) for reliable service detection.
- **UDP scanning is experimental.** Masscan UDP support is limited. Use Nmap -sU for UDP.
- **Ctrl+C auto-saves.** Masscan saves progress on interrupt. Resume with --resume paused.conf.
- **--excludefile is critical.** Always exclude your own IPs and RFC 1918 ranges to avoid scanning yourself.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/port-mass-scan/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
