HARDWARE

TE KORE — UNTIMED ENGINE

Hardware Boundary

This directory records the relationship between the Te Kore — Untimed Engine and physical computing systems.

The current release is primarily a software implementation.

No specific hardware implementation is claimed by version 0.1.0.

---

1. Physicality

The architecture does not treat software as disconnected from the physical systems through which it is executed.

Computing systems have physical components and material relationships.

These may include:

- processors
- memory
- storage
- circuit boards
- power systems
- networking equipment
- cables
- servers
- computers
- data-centre infrastructure
- physical interfaces

The current repository records this boundary without claiming that these components have already been implemented as part of the engine.

---

2. Software ↔ Hardware

The relationship may be represented as:

HARDWARE
↓
EXECUTION ENVIRONMENT
↓
SOFTWARE
↓
STATE
↓
CAUSAL RELATIONSHIPS
↓
MANIFESTATION

The current implementation occupies the software portion of this relationship.

Future work may investigate how the model behaves when connected to physical computing systems.

---

3. Current Boundary

Version 0.1.0 does not provide:

- a hardware controller
- embedded firmware
- a physical clock replacement
- specialised hardware
- distributed hardware coordination
- hardware-level causal verification

These remain outside the current implementation.

---

4. Future Investigation

Future experiments may examine:

- state carried between physical devices
- causal relationships across hardware nodes
- local state without timestamp semantics
- hardware/software boundaries
- physical input and output
- persistence across devices
- failure and recovery
- distributed state exchange

Any future implementation should be documented as a new transformation rather than assumed to have existed in version 0.1.0.

---

5. Provenance

The hardware boundary forms part of the wider lineage:

TE KORE
↓
TE KĀKANO
↓
TWO HEARTS
↓
TE KORE — UNTIMED ENGINE
↓
SOFTWARE
↓
HARDWARE INTERACTION

The hardware layer is therefore recorded as a potential future manifestation and relationship, not as an existing capability of the current release.

---

6. Guiding Principle

Physical implementation does not begin by pretending that the physical layer is already solved.

The boundary is recorded first.

Future implementation can then emerge from what is actually built, tested and observed.

---

HARDWARE BOUNDARY RECORDED — 0.1.0
