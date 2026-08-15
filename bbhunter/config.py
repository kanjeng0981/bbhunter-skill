"""Configuration for bbhunter.

All settings can be overridden via environment variables (or a ``.env`` file
in the current working directory).
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def _env(key: str, default: str) -> str:
    return os.getenv(key, default)


@dataclass
class Settings:
    # --- LLM (OpenAI-compatible) ---
    llm_base_url: str = _env("BBHUNTER_LLM_BASE_URL", "http://llm.lightvela.ai/v1")
    llm_api_key: str = _env("BBHUNTER_LLM_API_KEY", "")
    llm_model: str = _env("BBHUNTER_LLM_MODEL", "deepseek-chat")
    llm_timeout: float = float(_env("BBHUNTER_LLM_TIMEOUT", "120"))

    # --- Output ---
    output_dir: Path = field(
        default_factory=lambda: Path(_env("BBHUNTER_OUTPUT_DIR", "reports"))
    )
    skills_dir: Path = field(
        default_factory=lambda: Path(_env("BBHUNTER_SKILLS_DIR", "skills"))
    )

    # --- Web3 ---
    rpc_url: str = _env("BBHUNTER_RPC_URL", "https://eth.llamarpc.com")
    etherscan_api_key: str = _env("BBHUNTER_ETHERSCAN_API_KEY", "")

    # --- HTTP / general ---
    user_agent: str = _env("BBHUNTER_USER_AGENT", "bbhunter/0.1 (+bug bounty research)")
    http_timeout: float = float(_env("BBHUNTER_HTTP_TIMEOUT", "15"))
    max_concurrency: int = int(_env("BBHUNTER_MAX_CONCURRENCY", "10"))

    @property
    def llm_enabled(self) -> bool:
        """True when an LLM API key is configured (enables triage/analysis)."""
        return bool(self.llm_api_key)

    def resolve(self, base: Path | None = None) -> "Settings":
        """Resolve relative paths against an optional base directory."""
        if base is not None:
            if not self.output_dir.is_absolute():
                self.output_dir = base / self.output_dir
            if not self.skills_dir.is_absolute():
                self.skills_dir = base / self.skills_dir
        return self

    def http_headers(self) -> dict[str, str]:
        return {"User-Agent": self.user_agent}
