"""Minimal Ethereum JSON-RPC helpers (no heavy web3.py dependency)."""
from __future__ import annotations

from typing import Any

import httpx


class RPCError(Exception):
    pass


def rpc_call(rpc_url: str, method: str, params: list[Any], timeout: float = 20.0) -> Any:
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }
    try:
        resp = httpx.post(rpc_url, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except httpx.HTTPError as e:
        raise RPCError(f"RPC request failed: {e}") from e
    if "error" in data:
        raise RPCError(f"RPC error: {data['error']}")
    return data.get("result")


def get_chain_id(rpc_url: str) -> str:
    """Return chain id as a decimal string."""
    result = rpc_call(rpc_url, "eth_chainId", [])
    if isinstance(result, str) and result.startswith("0x"):
        return str(int(result, 16))
    return str(result)


def get_code(rpc_url: str, address: str) -> str:
    """Return contract bytecode (hex) for an address."""
    result = rpc_call(rpc_url, "eth_getCode", [address, "latest"])
    return result or ""


def get_balance(rpc_url: str, address: str) -> str:
    """Return balance in wei as a decimal string."""
    result = rpc_call(rpc_url, "eth_getBalance", [address, "latest"])
    if isinstance(result, str) and result.startswith("0x"):
        return str(int(result, 16))
    return str(result)


def get_chain_name(chain_id: str) -> str:
    known = {
        "1": "ethereum", "5": "goerli", "11155111": "sepolia",
        "56": "bsc", "137": "polygon", "42161": "arbitrum",
        "10": "optimism", "43114": "avalanche", "250": "fantom",
        "100": "gnosis", "8453": "base",
    }
    return known.get(chain_id, f"chain-{chain_id}")
