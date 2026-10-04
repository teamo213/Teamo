

# Te Kore — Untimed Engine
## Architecture

### 1. Purpose

Te Kore — Untimed Engine is an experimental architecture for carrying and verifying meaningful state through causal relationships without requiring timestamps or a shared wall-clock as part of the semantic state model.

The central question is:

> Can meaningful state be carried, related, verified and reconstructed through causality without making timestamp order the definition of that state?

The implementation explores that question through small composable components.

---

## 2. Architectural Shape

The current implementation is composed of five primary elements:

```text
StateVector
    ↓
SovereignNode
    ↓
AbsoluteNowNode

StateVector
    ↓
StateTranslationLayer

All components
    ↓
TeKoreUntimedEngine

These components have distinct responsibilities.


---

3. StateVector

StateVector is the basic carrier of meaningful state.

It contains:

vector_id

origin_identity

payload

causal_parent

signature


The payload carries the meaningful state.

The causal_parent identifies the preceding state relationship.

The signature provides deterministic integrity verification for the represented state and its causal parent.

The vector does not require a timestamp.


---

4. Causal Relationship

A state can reference a previous state through causal_parent.

For example:

STATE A
   │
   └── signature A
          │
          ▼
STATE B
   │
   └── causal_parent = signature A

This establishes an explicit relationship between states.

The relationship is represented directly rather than inferred from timestamp ordering.


---

5. SovereignNode

SovereignNode provides a local causal ledger.

It can:

create state vectors

retain vectors

expose the latest causal frontier

receive verified vectors

reject vectors whose integrity verification fails


The node does not require a shared clock to establish the semantic relationship between its states.

Its frontier is represented by the latest verified signature.


---

6. StateTranslationLayer

The translation layer allows a state payload to be transformed for a particular stream type.

Transformers are registered against a stream type and applied sequentially.

The source StateVector remains unchanged.

This distinction matters:

SOURCE STATE
     │
     ▼
TRANSLATION
     │
     ▼
TRANSFORMED PAYLOAD

Translation changes the representation being processed.

It does not rewrite the original source vector.


---

7. AbsoluteNowNode

AbsoluteNowNode represents the state currently held by a node.

It stores:

current state

causal frontier


It does not require a timestamp to identify that current state.

In this architecture, "now" means:

> the state currently held at the node.



This is an architectural abstraction.

It is not a claim that physical time has ceased to exist.


---

8. TeKoreUntimedEngine

TeKoreUntimedEngine composes the individual components into one usable interface.

It provides:

commit

receive

read

frontier


The engine therefore provides a simple movement:

INPUT
  ↓
COMMIT
  ↓
STATE VECTOR
  ↓
CAUSAL FRONTIER
  ↓
CURRENT STATE

A receiving engine can accept the vector when its integrity verification succeeds.


---

9. Integrity

The current implementation uses SHA-256 to calculate a deterministic signature from:

origin identity
+
canonical payload
+
causal parent
+
architecture key material

The signature currently functions as an integrity and determinism mechanism.

It should not be described as cryptographic authentication.

The current public key material is not a secret authentication key.

This boundary is intentional and documented.


---

10. No Timestamp Semantic Dependency

The architecture does not place timestamp fields inside the state model.

The causal relationship is represented explicitly through signatures and causal parents.

Therefore:

STATE A
   │
   │ causal relationship
   ▼
STATE B

does not require:

STATE A → timestamp → STATE B

The experiment is specifically concerned with whether causality can carry meaningful state without timestamp ordering being a required part of semantic state.


---

11. What This Architecture Does Not Claim

This repository does not claim:

that physical time does not exist

that clocks are unnecessary for every distributed system

that all ordering problems are solved

that network latency disappears

that synchronization problems disappear

that SHA-256 signatures provide authentication

that the architecture is formally proven


The current repository is an experimental implementation and testable demonstration.


---

12. Current Lineage

The repository is one manifestation within a larger body of work:

TE KORE
   ↓
TE KĀKANO
   ↓
TWO HEARTS
   ↓
TE KORE — UNTIMED ENGINE

The repository is a carrier of this particular manifestation.

It is not the whole architecture from which it emerged.

Future interaction with other manifestations may produce changes, transformations or new architectures.


---

13. Current Status

EXPERIMENTAL — 0.1.0

The implementation currently demonstrates:

meaningful state representation

deterministic integrity calculation

causal parent relationships

local causal ledgers

verified state exchange

sequential state translation

current-state representation without timestamp semantics

automated tests

a two-node exchange example


Further development will test the boundaries of the model rather than assume them.
