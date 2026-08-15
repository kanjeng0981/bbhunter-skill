"""Web3 smart-contract checks (LLM-driven + light heuristics)."""
from __future__ import annotations

import httpx

from ...llm import LLM
from ...models import ContractInfo, Finding
from ...skills import Skill

# Opcode hex signatures (single-byte opcodes).
# These are informational flags only — they need manual/LLM review.
_SELFDESTRUCT = "ff"
_DELEGATECALL = "f4"
_CALLCODE = "f2"

CONTRACT_ANALYZER_SYSTEM = (
    "You are a senior smart-contract security researcher. Analyze the provided "
    "Solidity source code for vulnerabilities and unsafe patterns. Consider "
    "reentrancy, unchecked low-level calls, integer overflow/underflow, access "
    "control flaws, tx.origin misuse, flash-loan vectors, unchecked external "
    "call return values, and missing events. Only report issues with clear "
    "technical justification. Be precise and conservative to avoid false "
    "positives."
)


def analyze_contract(
    contract: ContractInfo, llm: LLM, skills: list[Skill]
) -> list[Finding]:
    findings: list[Finding] = []

    if not contract.has_code:
        findings.append(
            Finding(
                module="web3.eoa",
                target=contract.address,
                title="Address is not a contract (EOA)",
                description="No bytecode deployed at this address; it is an "
                "externally-owned account or an empty address.",
                severity="info",
                evidence="eth_getCode returned 0x",
                confidence="high",
            )
        )
        return findings

    if contract.source:
        if llm.settings.llm_enabled:
            findings.extend(_llm_analyze_source(contract, llm, skills))
        else:
            findings.append(
                Finding(
                    module="web3.source",
                    target=contract.address,
                    title="Source available — LLM analysis skipped (no API key)",
                    description="Contract source is verified but automated LLM "
                    "review is disabled. Set BBHUNTER_LLM_API_KEY to enable it, "
                    "or review the source manually.",
                    severity="info",
                    confidence="high",
                )
            )
            findings.extend(_bytecode_heuristics(contract))
    else:
        findings.append(
            Finding(
                module="web3.unverified",
                target=contract.address,
                title="Contract source not available (unverified)",
                description="Contract is not verified, so only bytecode-level "
                "analysis is possible. Provide source for deeper review.",
                severity="info",
                confidence="high",
            )
        )
        findings.extend(_bytecode_heuristics(contract))

    return findings


def _llm_analyze_source(
    contract: ContractInfo, llm: LLM, skills: list[Skill]
) -> list[Finding]:
    skill_prompts = "\n\n".join(s.as_prompt() for s in skills)
    user = (
        f"Contract address: {contract.address}\n"
        f"Chain: {contract.chain} (chain id {contract.chain_id})\n\n"
        f"Solidity source:\n```solidity\n{contract.source[:24000]}\n```\n\n"
    )
    if skill_prompts:
        user += f"Use these researcher skills to guide your analysis:\n\n{skill_prompts}\n\n"
    user += (
        "Return a JSON object with a 'findings' array. Each item must have keys: "
        "title (string), description (string), severity (one of info/low/medium/"
        "high/critical), cwe (string, e.g. CWE-841), confidence (low/medium/high). "
        "If nothing is found, return {\"findings\": []}."
    )

    try:
        data = llm.chat_json(
            [{"role": "system", "content": CONTRACT_ANALYZER_SYSTEM},
             {"role": "user", "content": user}],
            temperature=0.1,
        )
    except Exception as e:  # noqa: BLE001 — degrade gracefully
        return [
            Finding(
                module="web3.llm.error",
                target=contract.address,
                title="LLM contract analysis failed",
                description=f"Could not analyze contract source: {e}",
                severity="info",
                confidence="low",
            )
        ]

    findings: list[Finding] = []
    for item in data.get("findings", []):
        findings.append(
            Finding(
                module="web3.llm",
                target=contract.address,
                title=str(item.get("title", "Contract issue"))[:200],
                description=str(item.get("description", "")),
                severity=str(item.get("severity", "info")),
                cwe=str(item.get("cwe", "")),
                confidence=str(item.get("confidence", "medium")),
                reasoning="Identified by LLM source analysis.",
            )
        )
    return findings


def _bytecode_heuristics(contract: ContractInfo) -> list[Finding]:
    """Flag presence of risky opcodes in raw bytecode (informational only)."""
    findings: list[Finding] = []
    code = contract.bytecode[2:] if contract.bytecode.startswith("0x") else contract.bytecode
    lowered = code.lower()

    checks = [
        (_DELEGATECALL, "delegatecall present", "Contract uses DELEGATECALL; "
         "review for delegatecall-based proxy/logic vulnerabilities.", "CWE-829"),
        (_SELFDESTRUCT, "selfdestruct present", "Contract contains SELFDESTRUCT; "
         "review for privileged selfdestruct.", "CWE-459"),
        (_CALLCODE, "callcode present", "Contract uses CALLCODE (deprecated); "
         "review for storage clobbering.", "CWE-829"),
    ]
    for opcode, title, desc, cwe in checks:
        # scan byte stream for the opcode byte (naive, low confidence)
        if opcode in lowered:
            findings.append(
                Finding(
                    module="web3.bytecode",
                    target=contract.address,
                    title=title,
                    description=desc,
                    severity="info",
                    confidence="low",
                    cwe=cwe,
                    evidence=f"Opcode 0x{opcode} found in bytecode",
                )
            )
    return findings


def fetch_source(
    address: str, chain_id: str, api_key: str, timeout: float = 20.0
) -> tuple[str, bool]:
    """Fetch verified source from Etherscan-compatible API. Returns (source, verified)."""
    if not api_key:
        return "", False
    host = "api.etherscan.io" if chain_id == "1" else f"api-{_etherscan_sub(chain_id)}.etherscan.io"
    url = "https://" + host + "/api"
    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": address,
        "apikey": api_key,
    }
    try:
        resp = httpx.get(url, params=params, timeout=timeout)
        data = resp.json()
        result = data.get("result", [{}])
        if result and isinstance(result, list):
            entry = result[0]
            src = entry.get("SourceCode", "")
            abi = entry.get("ABI", "")
            if src:
                return src, abi != "Contract source code not verified"
    except (httpx.HTTPError, ValueError, IndexError):
        pass
    return "", False


def _etherscan_sub(chain_id: str) -> str:
    sub = {
        "56": "bscscan.com",
        "137": "polygonscan.com",
        "43114": "snowtrace.io",
        "42161": "arbiscan.io",
        "10": "optimistic.etherscan.io",
        "8453": "basescan.org",
    }
    return sub.get(chain_id, "etherscan.io")
