# Finite Automaton Model for Indus Script

## Overview

The Indus Script operates as a **finite-state automaton** for validating administrative and institutional notation sequences. This document provides the complete formal specification.

## Formal Definition

The Indus system is formally defined as:

**S = (B, O, Σ, R, F)**

Where:
- **B**: Base bodies (≈30 ontological classes)
- **O**: Graphic operators (≈15 universal modifiers)
- **Σ**: Valid states (417 catalogued symbols)
- **R**: Composition rules (extracted from corpus analysis)
- **F**: Final states (family 342-348 + specialized closers)

## State Machine

### States

The automaton has 6 states:

```
S₀: INICIAL (Initial - no symbol processed)
S₁: ENTIDADE_DEFINIDA (Entity defined - entity recognized)
S₂: QUALIFICADA (Qualified - qualification operators applied)
S₃: QUANTIFICADA (Quantified - quantity specified)
S₄: RELACIONADA (Related - relation established)
S₅: FECHADA (Closed - closure applied) ★ ACCEPTING STATE
```

### State Transition Function δ

The transition function δ: S × Σ → S is defined as:

```
δ(S₀, ENT_*) = S₁
  where ENT_* ∈ {ENT_OVAL, ENT_U, ENT_HASTE, ENT_ANIMAL, ENT_METRICA}

δ(S₁, OP_QUAL) = S₂
δ(S₁, OP_COUNT) = S₃
δ(S₁, OP_REL) = S₄
δ(S₁, OP_CLOSE) = S₅

δ(S₂, OP_QUAL) = S₂  (reflexive for multiple qualifications)
δ(S₂, OP_COUNT) = S₃
δ(S₂, OP_REL) = S₄
δ(S₂, OP_CLOSE) = S₅

δ(S₃, OP_REL) = S₄
δ(S₃, OP_CLOSE) = S₅

δ(S₄, OP_CLOSE) = S₅
```

### Language Accepted

The language L accepted by this automaton is:

```
L = {w ∈ Σ* | w ends with closure symbol ∧ w respects syntactic order}
```

Or more formally:

```
L = {w = e·q*·n?·r?·c | 
     e ∈ ENT, 
     q ∈ OP_QUAL, 
     n ∈ OP_COUNT, 
     r ∈ OP_REL, 
     c ∈ OP_CLOSE}
```

## Symbol Classes

### Entity Classes (Initial Position)

| Class | Range | Function | Count |
|-------|-------|----------|-------|
| ENT_OVAL | 373-399 | Basic institutional entities | 27 |
| ENT_U | 328-339 | Containers/vessels | 12 |
| ENT_HASTE | 250-260 | Authority/hierarchy | 11 |
| ENT_ANIMAL | 200-210 | Functional agents | 11 |
| ENT_METRICA | 100-150 | Measures/quantities | 51 |

### Operator Classes

| Class | Range/Type | Function | Position | Count |
|-------|------------|----------|----------|-------|
| OP_QUAL | Dot, Stroke | Qualification | Medial | Variable |
| OP_COUNT | 410-417 | Counting/aggregation | Medial | 8 |
| OP_REL | 400-409 | Binary relations | Medial | 10 |
| OP_CLOSE | 342-348 | Terminal closure | Terminal | 7 |
| OP_SCOPE | Bracket | Scope delimitation | Medial | Variable |

## Transition Matrix

The complete transition matrix (6×10) showing all valid state-symbol transitions:

```
        ENT  QL  CT  RL  CL
S₀      S₁   -   -   -   -
S₁      -    S₂  S₃  S₄  S₅
S₂      -    S₂  S₃  S₄  S₅
S₃      -    -   -   S₄  S₅
S₄      -    -   -   -   S₅
S₅      -    -   -   -   -  (absorbing state)
```

Legend:
- ENT: Entity classes
- QL: Qualification operators
- CT: Count operators
- RL: Relation operators
- CL: Closure operators
- `-`: Invalid transition

## Properties

### Theorem 1: Syntactic Completeness

```
∀ valid record r, ∃ sequence s ∈ Σ* such that:
  s ⊢ r ∧ last(s) ∈ OP_CLOSE
```

**Proof**: By construction, all accepting paths through the automaton end in state S₅, which requires a closure symbol.

### Theorem 2: Operational Consistency

```
If s₁ → s₂ and s₁ ∈ Class_X, then s₂ ∈ Class_X
```

**Proof**: Operators modify semantics but do not change the ontological class of the base entity.

### Theorem 3: Terminal Closure

```
If s ∈ OP_CLOSE, then ∄ t such that s → t
```

**Proof**: State S₅ has no outgoing transitions (absorbing state).

### Theorem 4: Determinism

```
∀ state s ∈ S, ∀ symbol σ ∈ Σ: |δ(s, σ)| ≤ 1
```

**Proof**: The transition function is deterministic - each state-symbol pair maps to at most one new state.

## Composition Rules

### Positional Syntax

```
[ENTITY] [QUALIFIERS*] [QUANTIFIERS?] [RELATIONS?] [CLOSURE]
   ↑          ↑              ↑             ↑           ↑
Required   Optional       Optional      Optional    Required
Position 0  Position 1+    Position 2+   Position 3+ Final
```

### Ordering Constraints

1. **Entity First**: Every sequence must begin with an entity symbol
2. **Closure Last**: Every valid sequence must end with a closure symbol
3. **Monotonic Progression**: Operator types must appear in fixed order:
   - Qualification → Quantification → Relation → Closure
4. **No Backtracking**: Once an operator type is applied, earlier types cannot be reapplied (except multiple qualifications)

### Compatibility Matrix

Based on corpus analysis (Table II), transitions are only allowed where:

```
freq(symbol₁, symbol₂) > θ
```

Where θ is the empirical threshold derived from the corpus.

Forbidden transitions have:
```
freq(symbol₁, symbol₂) = 0
```

## Implementation Notes

### Time Complexity

- State transition: O(1)
- Sequence validation: O(n) where n = sequence length
- Classification: O(1) using hash maps

### Space Complexity

- State storage: O(1) - fixed 6 states
- Transition table: O(|S| × |Σ|) = O(6 × 417) = O(1) constant
- History tracking: O(n) for sequence of length n

## References

1. Parpola, A. (1994). *Deciphering the Indus Script*. Cambridge University Press.
2. Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*. 
3. Wells, B. (2011). "Epigraphic Approaches to Indus Writing". Oxbow Books.

## Version History

- v1.0 (2026-02-03): Initial formal specification
- Complete automaton definition with 6 states
- Comprehensive transition matrix
- Full symbol classification (417 symbols)
