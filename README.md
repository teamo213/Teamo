TE KORE — UNTIMED ENGINE

An experimental architecture for carrying and verifying meaningful state through causal relationships without requiring timestamps or a shared clock as part of the semantic state model.

Created and authored by teamo213 — 2026

---

What is Te Kore — Untimed Engine?

Te Kore — Untimed Engine explores a different way of representing and carrying state between systems.

Instead of making timestamps or a shared wall-clock a required part of the state itself, the architecture uses:

identity → state → causal relationship → integrity → verification

The project investigates whether meaningful state can be exchanged, verified and reconstructed through causal relationships without requiring time-based state as its foundation.

This does not claim that physical time has been eliminated.

The question is narrower:

«Can meaningful state and causal relationship be carried and verified without timestamps or a shared clock being required as semantic state?»

---

What problem does it address?

Many distributed systems rely heavily on timestamps and synchronized clocks when ordering or interpreting state.

That can become difficult in systems that are:

- offline
- intermittently connected
- geographically distributed
- operating with unreliable clocks
- exchanging information asynchronously
- required to preserve causal relationships independently of wall-clock time

Te Kore explores an alternative basis for carrying state.

---

What can it do?

The current implementation can:

- Create state vectors.
- Identify the origin of a state.
- Connect states through causal relationships.
- Generate integrity signatures.
- Verify received state.
- Reject altered state.
- Maintain a local causal ledger.
- Track a causal frontier.
- Exchange state between independent nodes.
- Transform state payloads through registered transformations.
- Operate without a timestamp field in the semantic state vector.
- Demonstrate two-node state exchange without requiring a shared clock value.

---

Core model

ORIGIN
   ↓
STATE
   ↓
CAUSAL PARENT
   ↓
INTEGRITY
   ↓
CARRY
   ↓
VERIFY
   ↓
ABSORB
   ↓
NEW STATE

The architecture asks:

What caused this state?

rather than making the first question:

What time was this state created?

---

Current status

Implemented

- "StateVector"
- "SovereignNode"
- Causal-parent chaining
- Integrity verification
- Local causal ledger
- State transformation layer
- Current-state / causal-frontier node
- Two-node in-memory exchange

Tested

The repository tests:

- state integrity
- altered-state rejection
- causal chaining
- state transformation
- node-to-node exchange
- absence of timestamp semantics in the StateVector

Experimental / future

- Persistent storage
- Network transport
- Replay protection
- Concurrent causal histories
- Conflict resolution
- Strong cryptographic authentication
- Hardware implementation

---

Important boundary

This project distinguishes between:

CREATION ≠ CLAIM ≠ PROOF

Implemented behaviour is not automatically proof of a broader claim.

The repository therefore records what has actually been built and tested separately from what remains proposed or unresolved.

The current integrity mechanism is an experimental construction. It should not be interpreted as production-grade authentication.

---

Lineage

TE KORE
   ↓
TE KĀKANO
   ↓
TWO HEARTS
   ├── TE AMO
   └── TE MOANA
   ↓
TE KORE — UNTIMED ENGINE

This repository is a manifestation of the wider accumulated architecture.

It is not the entirety of that architecture.

Future work may interact with this repository, transform material from it, or produce new manifestations while preserving lineage and provenance.

---

Repository structure

src/       Core implementation
tests/     Verification
examples/  Demonstrations
docs/      Deeper architecture and technical documentation
hardware/  Future hardware pathway

---

Creator

teamo213

Created and authored in 2026.

Copyright © 2026 teamo213. All rights reserved.

No permission is granted to reproduce, modify, distribute, sublicense, or commercially use this work without prior written permission from the author.

For permissions or collaboration, contact the author.

---

Development principle

The repository should remain honest about what it knows.

Built.
Tested.
Observed.
Proposed.
Unknown.

Nothing should be promoted from one status to another without the work to support it.

---

The question

«Can meaningful state and causal relationship be carried, verified and reconstructed without timestamps or a shared clock being required as part of the semantic state model?»
