from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import uuid

from .state_vector import StateVector


@dataclass
class SovereignNode:
    """Local causal ledger that does not require timestamp semantics."""

    name: str
    ledger: list[StateVector] = field(default_factory=list)

    @property
    def latest_signature(self) -> str | None:
        return self.ledger[-1].signature if self.ledger else None

    @property
    def frontier(self) -> str | None:
        return self.latest_signature

    def log(self, action: str, data: dict[str, Any]) -> StateVector:
        payload = {
            "action": action,
            "data": data,
        }

        vector = StateVector(
            vector_id=str(uuid.uuid4()),
            origin_identity=self.name,
            payload=payload,
            causal_parent=self.latest_signature,
        )

        self.ledger.append(vector)
        return vector

    def receive(self, vector: StateVector) -> bool:
        if not vector.verify():
            return False

        self.ledger.append(vector)
        return True
