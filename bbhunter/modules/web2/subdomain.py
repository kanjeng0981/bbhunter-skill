"""Passive subdomain enumeration and DNS helpers."""
from __future__ import annotations

import socket

import httpx


def enumerate_subdomains(domain: str, client: httpx.Client) -> list[str]:
    """Collect subdomains from certificate transparency logs (crt.sh)."""
    subs: set[str] = set()
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        resp = client.get(url, timeout=30)
        resp.raise_for_status()
        for entry in resp.json():
            for name in str(entry.get("name_value", "")).split("\n"):
                name = name.strip().lower().lstrip("*.")
                if name and name.endswith("." + domain):
                    subs.add(name)
    except (httpx.HTTPError, ValueError):
        pass
    return sorted(subs)


def resolve(host: str) -> str:
    """Resolve a hostname to an IPv4 address (empty string on failure)."""
    try:
        infos = socket.getaddrinfo(host, None)
        for info in infos:
            addr = info[4][0]
            if ":" not in addr:  # prefer IPv4
                return addr
        return infos[0][4][0] if infos else ""
    except OSError:
        return ""
