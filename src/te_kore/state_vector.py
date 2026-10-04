from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from typing import Any

from .constants import KEYS


def canonical_payload(payload: dict[str, Any]) -> str:
    """Create deterministic JSON for integrity calculation."""
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def calculate_signature(
    origin_identity: str,
    payload: dict[str, Any],
    causal_parent: str | None,
) -> str:
    material = (
        f"{origin_identity}:"
        f"{canonical_payload(payload)}:"
        f"{causal_parent or ''}:"
        f"{KEYS}"
    )

    return hashlib.sha256(
        material.encode("utf-8")
    ).hexdigest()[:16]


@dataclass(frozen=True)
class StateVector:
    vector_id: str
    origin_identity: str
    payload: dict[str, Any]
    causal_parent: str | None = None
    signature: str | None = None

    def __post_init__(self) -> None:
        expected = calculate_signature(
            self.origin_identity,
            self.payload,
            self.causal_parent,
        )

        if self.signature is None:
            object.__setattr__(
                self,
                "signature",
                expected,
            )

    def verify(self) -> bool:
        expected = calculate_signature(
            self.origin_identity,
            self.payload,
            self.causal_parent,
        )

        return self.signature == expected
