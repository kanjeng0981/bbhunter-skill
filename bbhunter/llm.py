"""Minimal OpenAI-compatible chat-completions client."""
from __future__ import annotations

import json
from typing import Any

import httpx

from .config import Settings


class LLMError(Exception):
    """Raised when the LLM backend returns something unexpected."""


class LLM:
    def __init__(self, settings: Settings):
        self.settings = settings
        headers = {"Content-Type": "application/json"}
        if settings.llm_api_key:
            headers["Authorization"] = f"Bearer {settings.llm_api_key}"
        self._client = httpx.Client(
            base_url=settings.llm_base_url,
            timeout=settings.llm_timeout,
            headers=headers,
        )

    def chat(
        self,
        messages: list[dict[str, str]],
        *,
        temperature: float = 0.2,
        max_tokens: int | None = None,
        json_mode: bool = False,
    ) -> str:
        payload: dict[str, Any] = {
            "model": self.settings.llm_model,
            "messages": messages,
            "temperature": temperature,
        }
        if max_tokens:
            payload["max_tokens"] = max_tokens
        if json_mode:
            payload["response_format"] = {"type": "json_object"}

        try:
            resp = self._client.post("/chat/completions", json=payload)
            resp.raise_for_status()
            data = resp.json()
        except httpx.HTTPError as e:
            raise LLMError(f"LLM request failed: {e}") from e

        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as e:
            raise LLMError(f"Unexpected LLM response: {data}") from e

    def chat_json(self, messages: list[dict[str, str]], **kwargs: Any) -> Any:
        raw = self.chat(messages, json_mode=True, **kwargs)
        return _extract_json(raw)


def _extract_json(raw: str) -> Any:
    """Best-effort JSON extraction (handles code fences and stray prose)."""
    text = raw.strip()
    if text.startswith("```"):
        text = text.lstrip("`")
        first_nl = text.find("\n")
        if first_nl != -1:
            text = text[first_nl + 1:]
        text = text.rstrip("`").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Fall back to first { ... last }
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError as e:
            raise LLMError(f"LLM returned invalid JSON: {raw[:400]}") from e
    raise LLMError(f"LLM returned no JSON: {raw[:400]}")
