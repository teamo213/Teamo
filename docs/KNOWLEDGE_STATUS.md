# Te Kore — Untimed Engine
## Knowledge Status

### 1. Purpose

This document records the status of knowledge represented by the repository.

The purpose is to distinguish what has been:

- created
- implemented
- observed
- tested
- inferred
- proposed
- not yet established

The repository should not convert an experimental result into a broader claim merely because the result has been successfully carried.

---

## 2. Core Distinction

The repository maintains the following distinction:

```text
CREATION
   ≠
CLAIM
   ≠
TEST RESULT
   ≠
PROOF

A created architecture can be real as an artefact without every proposition expressed by that architecture being established as fact.


---

3. Current Knowledge States

Implemented

The following are implemented in the current repository:

StateVector

deterministic signature calculation

causal parent relationships

SovereignNode

StateTranslationLayer

AbsoluteNowNode

TeKoreUntimedEngine

automated tests

two-node exchange example



---

Tested

The current test suite checks:

signature generation

signature verification

altered payload rejection

altered causal-parent rejection

causal-chain relationships

node-to-node state reception

translation composition

source-state preservation

current-state storage

absence of timestamp fields in the tested state model

engine integration


These are implementation-level test results.


---

Demonstrated

The example demonstrates that the current implementation can:

CREATE STATE
    ↓
CARRY STATE
    ↓
VERIFY STATE
    ↓
TRANSMIT STATE
    ↓
ACCEPT STATE
    ↓
RECONSTRUCT CURRENT STATE

without placing a timestamp or shared wall-clock in the semantic state representation used by the example.


---

4. Proposed

The broader architectural proposition remains experimental:

> Meaningful state and causal continuity may be representable and transferable without requiring timestamp ordering as the semantic foundation of the state model.



The repository provides an implementation through which this proposition can be explored.

The proposition should not be described as universally established by the current release.


---

5. Not Established

The current repository does not establish:

that all distributed systems can operate without clocks

that physical time is irrelevant

that all ordering problems can be represented through the current causal model

that network timing requirements disappear

that branching causal histories are solved

that concurrent states are solved

that causal merging is solved

that the current cryptographic mechanism provides secure authentication

that the model is formally proven


These remain open areas.


---

6. Representation and Reality

The repository distinguishes between a representation and the thing represented.

For example:

STATE VECTOR
     ↓
represents
     ↓
SOME MEANINGFUL STATE

Verification confirms properties of the state vector.

It does not independently establish that the represented event occurred in external reality.

Therefore:

REPRESENTATION VERIFIED
        ≠
EXTERNAL EVENT VERIFIED


---

7. Provenance

The current implementation emerged from an earlier conceptual and experimental code form.

The repository therefore preserves a distinction between:

SOURCE MATERIAL
      ↓
TRANSFORMATION
      ↓
CURRENT IMPLEMENTATION
      ↓
TESTED BEHAVIOUR

Future provenance documentation will record significant transformations and their reasons.


---

8. Experimental Discipline

New claims should follow this pattern:

IDEA
 ↓
IMPLEMENTATION
 ↓
TEST
 ↓
OBSERVATION
 ↓
DOCUMENTATION

A successful test should not automatically become a universal claim.

Likewise, an untested idea should remain identified as an idea.


---

9. Unknown

Unknown is an acceptable state.

Where the repository does not yet establish an answer, the correct status is:

UNKNOWN

rather than an assumed conclusion.

This allows future experimentation to add knowledge without rewriting the status of what was previously unknown.


---

10. Current Release Status

Version: 0.1.0

Knowledge status:

IMPLEMENTED
TESTED
DEMONSTRATED
EXPERIMENTAL

The broader proposition remains open for further investigation.


---

11. Guiding Principle

The repository should carry not only what was created, but also the status of what is known about what was created.

That distinction protects the integrity of the work as it develops.
