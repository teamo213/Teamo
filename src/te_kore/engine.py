from __future__ import annotations

from typing import Any

from .absolute_now import AbsoluteNowNode
from .node import SovereignNode
from .state_vector import StateVector
from .translation import StateTranslationLayer


class TeKoreUntimedEngine:
    """Main composition layer for the Te Kore Untimed Engine."""

    def __init__(self, node_name: str) -> None:
        self.node = SovereignNode(node_name)
        self.now = AbsoluteNowNode()
        self.translation = StateTranslationLayer()

    def commit(
        self,
        action: str,
        data: dict[str, Any],
    ) -> StateVector:
        vector = self.node.log(action, data)

        self.now.commit(
            state=vector.payload,
            causal_anchor=vector.signature,
        )

        return vector

    def receive(
        self,
        vector: StateVector,
    ) -> bool:
        accepted = self.node.receive(vector)

        if accepted:
            self.now.commit(
                state=vector.payload,
                causal_anchor=vector.signature,
            )

        return accepted

    def read(self) -> dict[str, Any] | None:
        return self.now.read()

    @property
    def frontier(self) -> str | None:
        return self.node.frontier
