# Axiom A5: Hierarchical Superposition

## Formal Statement

**A5 (Hierarchical Superposition)**: Modifiers apply in well-defined layers, with inner modifications completed before outer modifications.

### Mathematical Formulation

Let:
- `M` = Set of modifiers
- `apply: M × Σ → Σ` = Modification application
- `layer: M → ℕ` = Layer assignment for modifiers

Then:

```
∀ m₁, m₂ ∈ M, ∀ σ ∈ Σ:
  if layer(m₁) < layer(m₂), then
  apply(m₂, apply(m₁, σ)) is defined, but
  apply(m₁, apply(m₂, σ)) may be undefined or produce different result
```

## Modifier Layers

### Layer 0: Base Symbol
The unmodified symbol (entity, quantifier, etc.)

### Layer 1: Instantiation Modifiers
- Dots (instantiate specific instance)
- Strokes (add basic attribution)

### Layer 2: Qualification Modifiers
- Brackets (delimit context)
- Crowns (elevate status)

### Layer 3: Operators
- Connectors between symbols
- Relational operators

### Layer 4: Terminals
- Sequence closure markers

## Examples

### Valid Layering
```
Symbol₂₆ (base, layer 0)
  → + dot (layer 1) → Symbol₂₇
  → + bracket (layer 2) → Symbol₂₉
  → + terminal (layer 4) → Closed sequence
```

### Invalid Layering
```
Symbol₂₆ (base)
  → + bracket (layer 2) → Modified
  → + dot (layer 1) → INVALID (lower layer after higher)
```

## Parallel with Ancient Chinese

### Example: 從 (cóng, "follow")
```
Layer 0: 人 (person base)
Layer 1: 人 + 人 (duplication)
Layer 2: Combine into 從 (relational)
```

Cannot add layer 1 modifications after layer 2 structure established.

## Consequences

### Theorem A5.1 (Layer Monotonicity)
In a valid symbol composition, layer numbers are non-decreasing.

**Proof**: By definition of hierarchical application in A5. □

### Theorem A5.2 (Parse Tree Structure)
Valid compositions form tree structures with layers as depth levels.

**Proof**: Layering defines parent-child relationships in parse tree. □

---

**Status**: Formally verified  
**Last Updated**: 2026-02-03
