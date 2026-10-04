from __future__ import annotations

from threading import RLock
from typing import Any


class AbsoluteNowNode:
    """Current-state abstraction.

    'Now' means the node's currently held state.
    It is not a claim about physical time.
    The node stores no timestamp.
    """

    def __init__(self) -> None:
        self._lock = RLock()
        self._state: dict[str, Any] | None = None
        self._frontier: str | None = None

    def commit(
        self,
        state: dict[str, Any],
        causal_anchor: str | None,
    ) -> None:
        with self._lock:
            self._state = dict(state)
            self._frontier = causal_anchor

    def read(self) -> dict[str, Any] | None:
        with self._lock:
            if self._state is None:
                return None

            return dict(self._state)

    @property
    def frontier(self) -> str | None:
        with self._lock:
            return self._frontier
