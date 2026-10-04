from te_kore.engine import TeKoreUntimedEngine
from te_kore.node import SovereignNode


def test_logged_state_contains_no_timestamp() -> None:
    node = SovereignNode("NODE-A")

    vector = node.log(
        "INGEST",
        {"sku": "CHOCOLATE", "delta": 24},
    )

    assert "timestamp" not in vector.payload
    assert "time" not in vector.payload
    assert "created_at" not in vector.payload


def test_causal_relationship_does_not_require_timestamp() -> None:
    node = SovereignNode("NODE-A")

    first = node.log(
        "INGEST",
        {"value": 1},
    )

    second = node.log(
        "UPDATE",
        {"value": 2},
    )

    assert second.causal_parent == first.signature
    assert second.verify() is True


def test_engine_state_has_no_timestamp_dependency() -> None:
    engine = TeKoreUntimedEngine("NODE-A")

    vector = engine.commit(
        "INGEST",
        {"value": 42},
    )

    state = engine.read()

    assert state is not None
    assert state == vector.payload
    assert "timestamp" not in state
    assert "time" not in state
    assert "created_at" not in state


def test_engine_frontier_is_causal_signature() -> None:
    engine = TeKoreUntimedEngine("NODE-A")

    vector = engine.commit(
        "INGEST",
        {"value": 42},
    )

    assert engine.frontier == vector.signature
