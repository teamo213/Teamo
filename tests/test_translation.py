from te_kore.state_vector import StateVector
from te_kore.translation import StateTranslationLayer


def test_translation_without_transformer_preserves_payload() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={"value": 10},
    )

    layer = StateTranslationLayer()

    result = layer.process(
        vector,
        "default",
    )

    assert result == {"value": 10}


def test_translation_applies_transformer() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={"value": 10},
    )

    layer = StateTranslationLayer()

    layer.register(
        "numeric",
        lambda payload: {
            **payload,
            "value": payload["value"] + 5,
        },
    )

    result = layer.process(
        vector,
        "numeric",
    )

    assert result == {"value": 15}


def test_multiple_transformers_compose_in_order() -> None:
    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload={"value": 10},
    )

    layer = StateTranslationLayer()

    layer.register(
        "numeric",
        lambda payload: {
            **payload,
            "value": payload["value"] + 5,
        },
    )

    layer.register(
        "numeric",
        lambda payload: {
            **payload,
            "value": payload["value"] * 2,
        },
    )

    result = layer.process(
        vector,
        "numeric",
    )

    assert result == {"value": 30}


def test_translation_does_not_mutate_source_vector() -> None:
    original_payload = {
        "value": 10,
    }

    vector = StateVector(
        vector_id="vector-001",
        origin_identity="NODE-A",
        payload=original_payload,
    )

    layer = StateTranslationLayer()

    layer.register(
        "numeric",
        lambda payload: {
            **payload,
            "value": 999,
        },
    )

    result = layer.process(
        vector,
        "numeric",
    )

    assert result["value"] == 999
    assert vector.payload["value"] == 10
