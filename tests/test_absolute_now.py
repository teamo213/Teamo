from te_kore.absolute_now import AbsoluteNowNode


def test_node_starts_without_state() -> None:
    node = AbsoluteNowNode()

    assert node.read() is None
    assert node.frontier is None


def test_commit_stores_current_state() -> None:
    node = AbsoluteNowNode()

    state = {
        "action": "INGEST",
        "data": {"value": 42},
    }

    node.commit(
        state=state,
        causal_anchor="anchor-001",
    )

    assert node.read() == state
    assert node.frontier == "anchor-001"


def test_new_commit_replaces_current_state() -> None:
    node = AbsoluteNowNode()

    node.commit(
        state={"value": 1},
        causal_anchor="anchor-001",
    )

    node.commit(
        state={"value": 2},
        causal_anchor="anchor-002",
    )

    assert node.read() == {"value": 2}
    assert node.frontier == "anchor-002"


def test_read_returns_a_copy() -> None:
    node = AbsoluteNowNode()

    node.commit(
        state={"value": 42},
        causal_anchor="anchor-001",
    )

    state = node.read()
    assert state is not None

    state["value"] = 999

    assert node.read() == {"value": 42}


def test_absolute_now_node_does_not_require_timestamp() -> None:
    node = AbsoluteNowNode()

    node.commit(
        state={"value": 42},
        causal_anchor="anchor-001",
    )

    state = node.read()

    assert state is not None
    assert "timestamp" not in state
    assert "time" not in state
