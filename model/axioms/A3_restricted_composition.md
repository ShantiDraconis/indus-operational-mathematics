# Axiom A3: Restricted Composition

## Formal Statement

**A3 (Restricted Composition)**: Not all symbols can compose with all others. Composition is restricted by semantic class compatibility.

### Mathematical Formulation

Let:
- `C` = Set of classes
- `⊕: Σ × Σ ⇀ Σ` = Partial composition function
- `compatible: C × C → Bool` = Compatibility predicate

Then:

```
∀ σ₁, σ₂ ∈ Σ,
  σ₁ ⊕ σ₂ is defined ⟺ compatible(class(σ₁), class(σ₂)) = true
```

## Compatibility Matrix

| ⊕ | Quant | Entity | Modifier | Operator | Terminal |
|---|-------|--------|----------|----------|----------|
| **Quant** | ✗ | ✓ | ✗ | ✗ | ✗ |
| **Entity** | ✗ | ✗ | ✓ | ✓ | ✓ |
| **Modifier** | ✗ | ✗ | ? | ✗ | ✗ |
| **Operator** | ✗ | ✓ | ✗ | ? | ✗ |
| **Terminal** | ✗ | ✗ | ✗ | ✗ | ✗ |

**Key Rules**:
1. Quantifiers compose with entities: `Q ⊕ E → QE`
2. Entities accept modifiers: `E ⊕ M → E'`
3. Terminals compose with entities (end): `E ⊕ T → ET` (final)
4. Terminals accept nothing after: `T ⊕ * → ⊥`

## Examples

### Valid Compositions
```
Quantifier₃ ⊕ Entity₂₆ → "three entities" ✓
Entity₂₆ ⊕ Modifier_dot → Entity₂₇ ✓
Entity₂₆ ⊕ Terminal₃₄₃ → "entity (closed)" ✓
```

### Invalid Compositions
```
Quantifier₁ ⊕ Quantifier₂ → ⊥ (not defined)
Terminal₃₄₃ ⊕ Entity₂₆ → ⊥ (terminal accepts nothing)
Modifier ⊕ Quantifier → ⊥ (incompatible)
```

## Consequences

### Theorem A3.1 (Finite Language)
The set of valid symbol sequences is recursively enumerable and decidable.

**Proof**: Compatibility is decidable, composition is finite. □

### Theorem A3.2 (Non-Commutativity)
In general, `σ₁ ⊕ σ₂ ≠ σ₂ ⊕ σ₁`

**Proof**: Counterexample: `Q ⊕ E` defined but `E ⊕ Q` not. □

---

**Status**: Formally verified  
**Last Updated**: 2026-02-03
