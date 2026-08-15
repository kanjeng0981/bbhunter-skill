"""Shared data models."""
from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field

SEVERITIES = ["info", "low", "medium", "high", "critical"]
SEVERITY_ORDER = {s: i for i, s in enumerate(SEVERITIES)}


@dataclass
class WebHost:
    """A probed web target."""
    url: str
    domain: str = ""
    status: int = 0
    title: str = ""
    server: str = ""
    ip: str = ""
    content_type: str = ""
    technologies: list[str] = field(default_factory=list)
    headers: dict[str, str] = field(default_factory=dict)

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class ContractInfo:
    """A probed web3 contract."""
    address: str
    chain: str = ""
    chain_id: str = ""
    has_code: bool = False
    bytecode: str = ""
    source: str = ""
    verified: bool = False
    balance: str = ""

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class Finding:
    module: str
    target: str
    title: str
    description: str
    severity: str = "info"
    evidence: str = ""
    confidence: str = "medium"
    cwe: str = ""
    cvss: str = ""
    reasoning: str = ""
    references: list[str] = field(default_factory=list)
    id: str = field(default="", repr=False)

    def __post_init__(self) -> None:
        if self.severity not in SEVERITIES:
            self.severity = "info"
        if not self.id:
            key = f"{self.module}:{self.target}:{self.title}".encode()
            self.id = hashlib.md5(key).hexdigest()[:12]

    def as_dict(self) -> dict:
        return asdict(self)
