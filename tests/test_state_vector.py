from te_kore.state_vector import StateVector


def test_state_vector_signature_is_created() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={
            "action": "INGEST",
            "data": {"value": 24},
        },
    )

    assert vector.signature is not None
    assert len(vector.signature) == 16


def test_state_vector_signature_verifies() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={
            "action": "INGEST",
            "data": {"value": 24},
        },
    )

    assert vector.verify() is True


def test_changed_payload_fails_verification() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={
            "action": "INGEST",
            "data": {"value": 24},
        },
    )

    altered = StateVector(
        vector_id=vector.vector_id,
        origin_identity=vector.origin_identity,
        payload={
            "action": "INGEST",
            "data": {"value": 25},
        },
        causal_parent=vector.causal_parent,
        signature=vector.signature,
    )

    assert altered.verify() is False


def test_causal_parent_is_part_of_verification() -> None:
    first = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={"value": 1},
    )

    second = StateVector(
        vector_id="vector-002",
        origin_identity="NODE-A",
        payload={"value": 2},
        causal_parent=first.signature,
    )

    altered = StateVector(
        vector_id=second.vector_id,
        origin_identity=second.origin_identity,
        payload=second.payload,
        causal_parent="different-parent",
        signature=second.signature,
    )

    assert second.verify() is True
    assert altered.verify() is False
