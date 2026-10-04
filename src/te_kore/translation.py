from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from typing import Any

from .state_vector import StateVector


Transformer = Callable[[dict[str, Any]], dict[str, Any]]


class StateTranslationLayer:
    """Transforms payloads while preserving the source StateVector."""

    def __init__(self) -> None:
        self._transformers: dict[str, list[Transformer]] = {}

    def register(
        self,
        stream_type: str,
        transformer: Transformer,
    ) -> None:
        self._transformers.setdefault(
            stream_type,
            [],
        ).append(transformer)

    def process(
        self,
        vector: StateVector,
        stream_type: str,
    ) -> dict[str, Any]:
        payload = deepcopy(vector.payload)

        for transformer in self._transformers.get(
            stream_type,
            [],
        ):
            payload = transformer(payload)

        return payload
