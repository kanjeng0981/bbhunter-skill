"""Reconnaissance stage: enumerate and probe web2 + web3 targets."""
from __future__ import annotations

from urllib.parse import urlparse

import httpx

from ..config import Settings
from ..models import ContractInfo, WebHost
from ..modules.web2 import probe, subdomain
from ..modules.web3 import rpc
from ..modules.web3.checks import fetch_source

# Cap on subdomains probed per domain (safety for broad scopes).
MAX_SUBDOMAINS = 100


def _domain_of(target: str) -> str:
    t = target.strip()
    if "://" in t:
        return urlparse(t).hostname or ""
    return t


def _client(settings: Settings) -> httpx.Client:
    return httpx.Client(
        follow_redirects=True,
        timeout=30.0,
        verify=False,
        headers=settings.http_headers(),
    )


def recon_web2(targets: list[str], settings: Settings) -> list[WebHost]:
    client = _client(settings)
    urls: list[str] = []

    for t in targets:
        domain = _domain_of(t)
        if domain:
            subs = subdomain.enumerate_subdomains(domain, client)[:MAX_SUBDOMAINS]
            for s in subs:
                urls.append(f"https://{s}")
        # Always probe the root target over both schemes.
        if t.startswith("http://") or t.startswith("https://"):
            urls.append(t)
        else:
            urls.append(f"https://{t}")
            urls.append(f"http://{t}")

    urls = list(dict.fromkeys(urls))
    return probe.probe_many(urls, settings.http_timeout, settings.user_agent)


def recon_web3(contracts: list[str], chain: str, settings: Settings) -> list[ContractInfo]:
    rpc_url = settings.rpc_url
    chain_id = ""
    try:
        chain_id = rpc.get_chain_id(rpc_url)
    except rpc.RPCError:
        pass

    chain_name = chain or (rpc.get_chain_name(chain_id) if chain_id else "")

    out: list[ContractInfo] = []
    for addr in contracts:
        info = ContractInfo(address=addr, chain=chain_name, chain_id=chain_id)
        try:
            code = rpc.get_code(rpc_url, addr)
            info.has_code = code not in ("", "0x")
            info.bytecode = code
        except rpc.RPCError:
            info.has_code = False
        try:
            info.balance = rpc.get_balance(rpc_url, addr)
        except rpc.RPCError:
            pass
        src, verified = fetch_source(addr, chain_id, settings.etherscan_api_key)
        info.source = src
        info.verified = verified
        out.append(info)
    return out
