

# Te Kore — Untimed Engine
## Verification Model

### 1. Purpose

Verification in Te Kore — Untimed Engine means checking whether a carried state still corresponds to the state from which its signature was produced.

The current implementation uses deterministic SHA-256 hashing.

The purpose is to detect alteration and preserve integrity of the represented state.

---

## 2. What Is Verified

A `StateVector` contains:

```text id="f7r2m9"
origin_identity
payload
causal_parent
signature

The signature is calculated from:

origin identity
+
canonical payload
+
causal parent
+
architecture key material

The resulting SHA-256 digest is reduced to the first 16 hexadecimal characters for the current experimental implementation.


---

3. Deterministic Payload

Payload data is converted into canonical JSON before signature calculation.

The implementation uses:

sorted dictionary keys

compact JSON separators

UTF-8 encoding

preservation of non-ASCII characters


This allows equivalent payload structures to produce deterministic signature material.


---

4. Verification Process

When a vector is verified:

RECEIVED VECTOR
      ↓
RECREATE SIGNATURE MATERIAL
      ↓
CALCULATE EXPECTED SIGNATURE
      ↓
COMPARE WITH CARRIED SIGNATURE
      ↓
VALID / INVALID

If the calculated signature matches the carried signature, the vector passes the current integrity check.

If the state has been altered, the calculated signature no longer matches.


---

5. Causal Integrity

The causal parent is part of the signature material.

Therefore the verification covers both:

WHAT THE STATE CONTAINS

and:

WHAT STATE IT CLAIMS TO FOLLOW

Changing either changes the expected signature.

This means the current implementation does not treat the causal relationship as separate metadata that can be altered without affecting verification.


---

6. Example

A valid chain may look like:

STATE A
signature = 1111aaaa
       │
       ▼
STATE B
causal_parent = 1111aaaa
signature = 2222bbbb

If the payload of State B is altered:

STATE B
causal_parent = 1111aaaa
signature = 2222bbbb
payload = ALTERED

the calculated signature no longer corresponds to the carried signature.

Verification therefore fails.


---

7. Node Acceptance

SovereignNode.receive() verifies the incoming vector before adding it to the local ledger.

The current behaviour is:

RECEIVE
  ↓
VERIFY
  ↓
VALID ─────→ ACCEPT
  │
  └────────→ INVALID → REJECT

An invalid vector is not added to the receiver's ledger.


---

8. What the Current Signature Does

The current signature provides:

deterministic integrity checking

detection of payload alteration

detection of causal-parent alteration

a compact causal identifier

a reproducible verification mechanism


It does not provide every property associated with secure distributed authentication.


---

9. Important Security Boundary

The current implementation uses architecture key material that is present in the source code.

Therefore the current signature mechanism should not be described as secret-key authentication.

In particular, it does not establish:

proof of identity against an unknown attacker

secure private-key authentication

resistance to someone who can reproduce the signing material

protection equivalent to a production cryptographic protocol


The correct current description is:

> deterministic integrity and causal verification.



A future implementation could introduce stronger cryptographic identity mechanisms if required.


---

10. What Verification Does Not Establish

Passing verification does not prove:

that the originating actor is truthful

that the payload represents external reality

that the underlying event actually occurred

that the causal interpretation is philosophically or scientifically complete

that the architecture solves all distributed-system ordering problems


Verification establishes correspondence between the carried state, its causal parent and its calculated signature under the current implementation.

That boundary must remain explicit.


---

11. Relationship Between Verification and Knowledge

A verified vector is not automatically a verified fact about the external world.

The distinction is:

SIGNATURE VERIFIED
        ≠
EVENT PROVEN
        ≠
CLAIM TRUE

The signature verifies the integrity of the representation being carried.

It does not independently verify the truth of what that representation describes.


---

12. Current Test Coverage

The repository tests:

signature creation

signature verification

altered payload rejection

altered causal-parent rejection

valid node reception

invalid node rejection

causal-chain continuity

timestamp-independent state representation


The tests provide executable evidence of current implementation behaviour.

They are not a formal proof of the entire architectural proposition.


---

13. Future Verification Work

Future work may investigate:

stronger authentication

explicit identity models

branching causal histories

concurrent states

causal merges

conflict detection

distributed verification

larger state graphs

persistence

tamper-evident storage

formal properties and invariants


These should be added only when implemented and tested.


---

Status

VERIFICATION MODEL — EXPERIMENTAL

Current principle:

CARRY → CALCULATE → COMPARE → ACCEPT OR REJECT

