from te_kore.engine import TeKoreUntimedEngine


def main() -> None:
    sender = TeKoreUntimedEngine("NODE-A")
    receiver = TeKoreUntimedEngine("NODE-B")

    vector = sender.commit(
        "INGEST",
        {
            "sku": "CHOCOLATE",
            "delta": 24,
        },
    )

    accepted = receiver.receive(vector)

    print("TE KORE — UNTIMED ENGINE")
    print()
    print("SENDER")
    print(f"  node: {sender.node.name}")
    print(f"  frontier: {sender.frontier}")
    print()

    print("STATE VECTOR")
    print(f"  id: {vector.vector_id}")
    print(f"  origin: {vector.origin_identity}")
    print(f"  payload: {vector.payload}")
    print(f"  causal_parent: {vector.causal_parent}")
    print(f"  signature: {vector.signature}")
    print(f"  verified: {vector.verify()}")
    print()

    print("RECEIVER")
    print(f"  node: {receiver.node.name}")
    print(f"  accepted: {accepted}")
    print(f"  frontier: {receiver.frontier}")
    print(f"  current state: {receiver.read()}")
    print()

    print("SEMANTIC CLOCK DEPENDENCY")
    print("  timestamp required: False")
    print("  shared wall-clock required: False")
    print()

    print("DEMONSTRATION COMPLETE")


if __name__ == "__main__":
    main()
