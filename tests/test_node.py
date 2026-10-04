from te_kore.node import SovereignNode


def test_node_starts_empty() -> None:
    node = SovereignNode("NODE-A")

    assert node.ledger == []
    assert node.frontier is None


def test_node_logs_state() -> None:
    node = SovereignNode("NODE-A")

    vector = node.log(
        "INGEST",
        {"sku": "CHOCOLATE", "delta": 24},
    )

    assert len(node.ledger) == 1
    assert node.ledger[0] == vector
    assert node.frontier == vector.signature


def test_second_state_carries_first_causal_parent() -> None:
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


def test_valid_vector_can_be_received() -> None:
    sender = SovereignNode("NODE-A")
    receiver = SovereignNode("NODE-B")

    vector = sender.log(
        "INGEST",
        {"value": 42},
    )

    accepted = receiver.receive(vector)

    assert accepted is True
    assert receiver.ledger == [vector]
    assert receiver.frontier == vector.signature


def test_invalid_vector_is_rejected() -> None:
    sender = SovereignNode("NODE-A")
    receiver = SovereignNode("NODE-B")

    vector = sender.log(
        "INGEST",
        {"value": 42},
    )

    vector.payload["value"] = 999

    accepted = receiver.receive(vector)

    assert accepted is False
    assert receiver.ledger == []
    assert receiver.frontier is None
