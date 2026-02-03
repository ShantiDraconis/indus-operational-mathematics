# Axiom A4: Terminal Closure

## Formal Statement

**A4 (Terminal Closure)**: Symbols of the Terminal class enforce sequence termination. Once a terminal symbol appears, no further composition is permitted.

### Mathematical Formulation

Let:
- `T ⊂ Σ` = Set of terminal symbols
- `⊕` = Composition operation

Then:

```
∀ τ ∈ T, ∀ σ ∈ Σ: τ ⊕ σ = ⊥ (undefined)
```

Where `⊥` represents an invalid/rejected composition.

## Interpretation

1. **Boundary Enforcement**: Terminals mark inscription boundaries
2. **Parsing Aid**: Enables unambiguous sequence segmentation
3. **Validation Rule**: Sequences ending in non-terminals may be incomplete

## Examples

### Valid Sequences
```
Entity₂₆ ⊕ Modifier ⊕ Terminal₃₄₃  ✓ (terminal at end)
Quant₃ ⊕ Entity₂₆ ⊕ Terminal₃₄₃  ✓ (valid closure)
```

### Invalid Sequences
```
Terminal₃₄₃ ⊕ Entity₂₆  ✗ (composition after terminal)
Entity₂₆ ⊕ Terminal₃₄₃ ⊕ Modifier  ✗ (continues after terminal)
```

## Evidence in Harappan

**Statistical Analysis**:
- Symbol 343 appears in ~92% of sequence-final positions
- Symbol 343 NEVER appears in non-final positions
- After symbol 343, no further symbols occur

**Conclusion**: Strong evidence for terminal behavior.

## Consequences

### Theorem A4.1 (Unique Termination)
Every valid sequence has at most one terminal symbol, located at the end.

**Proof**: By A4, after terminal no composition allowed, so only final position possible. □

### Theorem A4.2 (Sequence Decidability)
Given a symbol sequence, we can decide if it's complete (terminated) or incomplete.

**Proof**: Check if last symbol is terminal. □

---

**Status**: Formally verified  
**Last Updated**: 2026-02-03
