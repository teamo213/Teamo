# Changelog

All notable changes to Te Kore — Untimed Engine are documented here.

## [0.1.0] — Initial Experimental Release

### Added

- `StateVector` for carrying meaningful state.
- Deterministic state signatures using SHA-256.
- Causal parent relationships between state vectors.
- `SovereignNode` local causal ledger.
- `StateTranslationLayer` for sequential payload transformation.
- `AbsoluteNowNode` for current-state representation without timestamp semantics.
- `TeKoreUntimedEngine` as the main composition layer.
- Verification tests for state integrity and causal relationships.
- Translation-layer composition tests.
- Untimed semantic-boundary tests.
- Two-node exchange example.
- Initial architecture README.

### Boundary

This release demonstrates an experimental model in which meaningful state and causal relationships can be represented without requiring timestamps or a shared wall-clock as part of the semantic state model.

It does not claim that physical time does not exist.

It does not establish that all distributed-system timing requirements can be removed.

It does not constitute formal proof of the broader architectural proposition.

### Status

**EXPERIMENTAL — 0.1.0**
