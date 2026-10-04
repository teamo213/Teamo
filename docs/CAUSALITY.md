

# Te Kore — Untimed Engine
## Causality Model

### 1. Purpose

The Te Kore — Untimed Engine represents state relationships through explicit causal references.

A state does not need a timestamp to identify the state from which it emerged.

The central relationship is:

```text
CAUSE
  ↓
STATE
  ↓
NEW STATE

The relationship is carried directly by the state vector.


---

2. Causal Parent

Each StateVector may contain a causal_parent.

The causal parent is the signature of the state from which the current vector follows.

For example:

VECTOR A
signature = A

VECTOR B
causal_parent = A
signature = B

This creates:

A → B

The relationship is explicit.


---

3. Causal Chain

Multiple state transitions can form a chain:

A
↓
B
↓
C
↓
D

Each state carries the reference to the state immediately preceding it.

The resulting structure can be followed through the signatures.

This allows the history of causal relationships to be reconstructed from the carried state itself.


---

4. Causality Is Not Timestamp Ordering

A conventional temporal model might represent:

A happened at T1
B happened at T2
therefore A preceded B

The model explored here instead represents:

B
└── causal_parent = A

The relationship is therefore encoded directly.

The experiment is not claiming that timestamps are useless in every context.

It is testing whether timestamp order must be part of the semantic definition of the relationship.


---

5. Frontier

The node exposes a frontier.

The frontier represents the latest causal state currently held by that node.

For a chain:

A → B → C

the frontier is:

C

More precisely, the implementation represents the frontier using the signature of the latest state.

The frontier therefore identifies the current causal edge without requiring a timestamp.


---

6. State Integrity

The causal relationship is included in the signature calculation.

The current signature is derived from:

origin identity
+
canonical payload
+
causal parent
+
architecture key material

Therefore changing the causal parent changes the expected signature.

Example:

VALID

A
↓
B

versus:

ALTERED

X
↓
B

If the signature still belongs to the original relationship, verification fails.


---

7. Causal Transmission

A state vector can move between nodes while retaining its origin and causal relationship.

Example:

NODE A
   │
   │ creates vector
   ▼
STATE VECTOR
   │
   │ transmitted
   ▼
NODE B
   │
   │ verifies
   ▼
ACCEPTED STATE

The receiving node does not need to recreate the original state from a timestamp.

It receives the carried state and verifies its integrity.


---

8. Causal Continuity

The model treats continuity as something that can be carried.

STATE
  ↓
CAUSAL RELATION
  ↓
NEW STATE
  ↓
CAUSAL RELATION
  ↓
NEW STATE

The continuity is therefore contained in the relationships between states.

This provides a basis for exploring systems in which meaningful continuity does not depend on a shared temporal reference.


---

9. Current Boundary

The present implementation uses a linear causal parent:

one state
   ↓
one next state

This is deliberately simple.

It does not yet fully specify:

branching

concurrent states

merging

conflict resolution

distributed causal frontiers

vector clocks

logical clocks

partial-order reconstruction

network partitions


These are future areas for testing.

They should not be assumed solved by the current implementation.


---

10. Physical Time

Physical time remains part of the world in which the software executes.

The architecture does not attempt to abolish physical time.

The narrower proposition is:

> A timestamp or shared wall-clock does not have to be the semantic carrier of the causal relationship represented by the state model.



This distinction is fundamental to the experiment.


---

11. Causal Verification

The current test suite checks that:

a state can be created without a timestamp

a causal parent can be carried

changing the causal parent invalidates the existing signature

a valid state can be transmitted

altered state can be rejected

the engine frontier can identify the current causal state


These tests establish the behaviour of the current implementation.

They do not constitute proof of the broader architectural proposition.


---

12. Open Question

The deeper question remains open:

> How far can meaningful state, continuity and relationship be carried through explicit causality before a temporal reference becomes necessary for a particular class of system?



That question defines the next stage of experimentation.


---

Status

CAUSALITY MODEL — EXPERIMENTAL

Current implementation:

State → Causal Relationship → Verification → Continuity

