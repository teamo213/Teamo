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
