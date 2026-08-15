---
name: scada-hikvision-isapi
description: Enumerate Hikvision ISAPI endpoints on SCADA and IoT web interfaces.
scope: web2
---
Enumerate Hikvision ISAPI endpoints on SCADA and IoT web interfaces.

- A web interface on a non-standard port (443, 8443, 9443) loads a large JavaScript bundle with references to /ISAPI/, Bumblebee, or Streaming/channels.
- Port scan reveals RTSP (554), ONVIF (8899), or Hikvision-specific ports (8000, 9010).
- The server header or SSL certificate references Hikvision, HikCentral, iVMS, or Pyramid.
- A target has industrial/energy/infrastructure context where SCADA systems are likely.
- The web client loads Common/common.js, Common/components.js, or Common/vendorGraph.js from a relative path.

- **ErrorCode 216 is not a hard block.** It means "session required" — the endpoint is live but needs authentication. This is still a finding (exposed service).
- **HikCentral vs. standalone device.** HikCentral Professional (web-managed) uses CAS/SlaveSession. Standalone NVRs/cameras use Basic or Digest auth. The auth method tells you the deployment type.
- **WebSocket endpoints are hidden.** The JS references ws://127.0.0.1: for local WebSocket connections. External WebSocket endpoints may use different ports.
- **RTSP is often UDP.** Standard port scans miss it. Use nmap -sU -p 554 for UDP RTSP detection.
- **ONVIF may be on port 80/8080, not 8899.** Probe multiple ports with the ONVIF SOAP request.

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/scada-hikvision-isapi/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
