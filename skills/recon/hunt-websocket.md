---
name: hunt-websocket
description: Hunt WebSocket vulnerabilities — Cross-Site WebSocket Hijacking (CSWSH), missing/weak Origin validation on the WS handshake, no per-message authentication, message tampering, socket.io namespace/room authorization bypass, and handshake-layer Upgrade smuggling. Use when target has WebSocket endpoints (ws:// or wss://), socket.io / SignalR / Phoenix Channels, real-time features, chat, live dashboards, notifications, or trading platforms.
scope: web2
---
Hunt WebSocket vulnerabilities — Cross-Site WebSocket Hijacking (CSWSH), missing/weak Origin validation on the WS handshake, no per-message authentication, message tampering, socket.io namespace/room authorization bypass, and handshake-layer Upgrade smuggling. Use when target has WebSocket endpoints (ws:// or wss://), socket.io / SignalR / Phoenix Channels, real-time features, chat, live dashboards, notifications, or trading platforms.

- **WebSocket without auth** — if the WebSocket endpoint doesn't require auth tokens, anyone can connect. Test post-connection auth requirements.
- **ws:// instead of wss://** — plaintext WebSocket on public services allows MITM. This is Medium if the WebSocket carries sensitive data.
- **WebSocket CSWSH** — Cross-Site WebSocket Hijacking: if the WebSocket handshake doesn't validate Origin, an attacker's page can open a WebSocket. Test with Origin: evil.com.
- **WebSocket message injection** — injecting into WebSocket messages that are reflected to other users is stored XSS via WebSocket.

---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-websocket/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
