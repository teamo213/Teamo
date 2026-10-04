from te_kore.engine import TeKoreUntimedEngine


def test_engine_starts_empty() -> None:
    engine = TeKoreUntimedEngine("NODE-A")

    assert engine.read() is None
    assert engine.frontier is None


def test_engine_commit_creates_current_state() -> None:
    engine = TeKoreUntimedEngine("NODE-A")

    vector = engine.commit(
        "INGEST",
        {
            "sku": "CHOCOLATE",
            "delta": 24,
        },
    )

    assert vector.verify() is True
    assert engine.read() == vector.payload
    assert engine.frontier == vector.signature


def test_engine_builds_causal_chain() -> None:
    engine = TeKoreUntimedEngine("NODE-A")

    first = engine.commit(
        "INGEST",
        {"value": 1},
    )

    second = engine.commit(
        "UPDATE",
        {"value": 2},
    )

    assert second.causal_parent == first.signature
    assert second.verify() is True
    assert engine.frontier == second.signature


def test_engine_can_receive_verified_state() -> None:
    sender = TeKoreUntimedEngine("NODE-A")
    receiver = TeKoreUntimedEngine("NODE-B")

    vector = sender.commit(
        "INGEST",
        {"value": 42},
    )

    accepted = receiver.receive(vector)

    assert accepted is True
    assert receiver.read() == vector.payload
    assert receiver.frontier == vector.signature


def test_engine_rejects_altered_state() -> None:
    sender = TeKoreUntimedEngine("NODE-A")
    receiver = TeKoreUntimedEngine("NODE-B")

    vector = sender.commit(
        "INGEST",
        {"value": 42},
    )

    vector.payload["value"] = 999

    accepted = receiver.receive(vector)

    assert accepted is False
    assert receiver.read() is None
    assert receiver.frontier is None
