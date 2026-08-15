---
name: iot-camera-recon
description: Attack cameras via RTSP, ONVIF, Axis config when 554 open.
scope: web2
---
Attack cameras via RTSP, ONVIF, Axis config when 554 open.

- port-mass-scan finds RTSP (554) or camera HTTP ports (80, 8010, 8011).
- Target is a physical security company, traffic management, or government surveillance.
- Shodan search reveals camera devices in the target's IP range.
- After port-service-discovery finds Axis/Hikvision/Dahua ONVIF services.

- **CGNAT blocks direct camera access.** Many cameras are behind carrier-grade NAT and unreachable from internet.
- **RTSP over UDP is unreliable.** Use -rtsp_transport tcp for reliable stream testing.
- **Config dump can be LARGE.** Axis configs are 50-200KB. Use --max-time to avoid hanging on slow connections.
- **Video streams are bandwidth-heavy.** Test with snapshot first, then short stream probes.
- **Camera firmware is rarely updated.** 2020 firmware on a 2026 scan is common — don't assume patches.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/iot-camera-recon/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
