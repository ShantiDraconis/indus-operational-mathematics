# Operator Algebra for the Indus Script

## Introduction

This document formalizes the algebraic properties of the Indus script operators, treating symbol composition as an algebraic operation.

## Definitions

### 1. Basic Algebraic Structure

Let **Σ** be the set of all Indus symbols (|Σ| = 417).

Define the composition operator **⊕** such that for symbols s₁, s₂ ∈ Σ:
```
s₁ ⊕ s₂ = composite symbol/state
```

### 2. Operator Classes

We partition Σ into disjoint operator classes:

```
Σ = B ∪ O
```

Where:
- **B** (Base symbols): Entities that can stand alone
- **O** (Operators): Modifiers that require a base

Further:
```
O = O_qual ∪ O_count ∪ O_rel ∪ O_close
```

## Properties

### Property 1: Non-Commutativity

The composition operation is generally **not commutative**:

```
s₁ ⊕ s₂ ≠ s₂ ⊕ s₁ for most s₁, s₂
```

**Example**:
- Entity ⊕ Closure = Valid (373 ⊕ 342 ✓)
- Closure ⊕ Entity = Invalid (342 ⊕ 373 ✗)

**Exception**: Some qualifiers are commutative:
```
Dot ⊕ Stroke = Stroke ⊕ Dot (both valid qualifications)
```

### Property 2: Associativity

For valid sequences, composition is **associative**:

```
(s₁ ⊕ s₂) ⊕ s₃ = s₁ ⊕ (s₂ ⊕ s₃)
```

This allows us to write sequences without parentheses:
```
s₁ ⊕ s₂ ⊕ s₃ ⊕ ... ⊕ sₙ
```

### Property 3: Identity Element

The **null sequence** (ε) acts as a right identity:

```
s ⊕ ε = s for all s ∈ B
```

However, there is **no left identity** (operators must follow bases).

### Property 4: Absorption

Closure operators are **absorbing**:

```
c ⊕ s = undefined for all c ∈ O_close, s ∈ Σ
```

Once a closure is applied, no further composition is possible.

### Property 5: Class Preservation

Operators **preserve entity classes**:

```
If e ∈ Class_X and o ∈ O, then class(e ⊕ o) = Class_X
```

**Example**:
- Animal(200) ⊕ Count(410) = Animal(200)+Count(410) [still animal class]
- Oval(373) ⊕ Qual(dot) = Oval(373)+Qual(dot) [still oval class]

## Algebraic Structure

### Monoid Structure

The base symbols with concatenation form a **free monoid**:

```
(B, ⊕, ε)
```

Where:
- **B**: Set of base symbols
- **⊕**: Concatenation operation
- **ε**: Empty sequence (identity)

### Operator Semigroups

Each operator class forms a **semigroup**:

```
(O_qual, ⊕)  - Qualification semigroup
(O_count, ⊕) - Counting semigroup
(O_rel, ⊕)   - Relation semigroup
```

These are not groups (no inverse elements).

## Composition Rules

### Rule 1: Entity First

```
∀ valid sequence s: s = e ⊕ ... where e ∈ B
```

Every sequence must start with a base entity.

### Rule 2: Ordered Application

Operators must be applied in fixed order:

```
e ⊕ q* ⊕ c* ⊕ r* ⊕ close
```

Where:
- q* = zero or more qualifications
- c* = zero or more counts
- r* = zero or more relations
- close = exactly one closure

### Rule 3: Closure Finality

```
∀ sequence s ending in c ∈ O_close: s ⊕ σ = undefined ∀σ ∈ Σ
```

Closure terminates all composition.

## Examples

### Example 1: Simple Record

```
373 ⊕ 342
= Entity(basic_token) ⊕ Close(simple)
= Valid Record
```

### Example 2: Quantified Record

```
200 ⊕ 410 ⊕ 411 ⊕ 343
= Entity(unicorn) ⊕ Count(1) ⊕ Count(2) ⊕ Close(confirmed)
= Entity(unicorn, quantity=3) ⊕ Close(confirmed)
= Valid Record
```

### Example 3: Invalid Composition (Non-Commutative)

```
342 ⊕ 373
= Close(simple) ⊕ Entity(basic_token)
= Invalid (closure first)
```

### Example 4: Invalid Composition (Out of Order)

```
373 ⊕ 400 ⊕ 410
= Entity ⊕ Relation ⊕ Count
= Invalid (count cannot follow relation)
```

## Operator Precedence

Define precedence levels:

```
Level 0: Base entities (highest binding)
Level 1: Qualifications
Level 2: Quantifications  
Level 3: Relations
Level 4: Closures (lowest binding, terminates)
```

### Precedence Rules

1. Lower level operators bind tighter
2. Same level operators associate left-to-right
3. Higher precedence operations must follow lower precedence

## Homomorphisms

### H1: To Boolean (Validity)

```
h: Σ* → {True, False}
h(s) = True iff s is accepted by the automaton
```

### H2: To JSON (Semantics)

```
j: Σ* → JSON
j(s) = structured representation of s
```

**Example**:
```
j(373 ⊕ 410 ⊕ 342) = {
  "entity": "basic_token",
  "quantity": 1,
  "closure": "simple"
}
```

### H3: To Natural Language (Interpretation)

```
n: Σ* → String
n(s) = human-readable description
```

**Example**:
```
n(200 ⊕ 410 ⊕ 343) = "One unicorn, confirmed"
```

## Formal Theorems

### Theorem A1: Finite Composition

**Statement**: Every valid sequence has finite length.

**Proof**: 
1. Must start with entity (1 symbol)
2. Optional operators are finite (bounded by corpus)
3. Must end with closure (1 symbol)
4. Therefore, 2 ≤ |s| ≤ max_observed ≈ 13 ∎

### Theorem A2: Unique Decomposition

**Statement**: Every valid sequence has a unique decomposition into components.

**Proof**:
By the ordering constraints, we can uniquely identify:
1. The entity (first symbol in B)
2. The qualifiers (symbols in O_qual before first non-qualifier)
3. The quantifiers (symbols in O_count)
4. The relations (symbols in O_rel)
5. The closure (last symbol in O_close)

This decomposition is unique. ∎

### Theorem A3: Composition Determinacy

**Statement**: For any partial sequence, the set of valid continuations is deterministic.

**Proof**:
The automaton is deterministic, so from any state, each symbol class leads to at most one new state. Therefore, the set of valid next symbols is uniquely determined by the current state. ∎

## Applications

### A1: Sequence Generation

Use the algebra to generate all valid sequences:

```python
def generate_sequences(max_length):
    for entity in B:
        for quals in powerset(O_qual):
            for counts in powerset(O_count):
                for rels in powerset(O_rel):
                    for close in O_close:
                        seq = entity + quals + counts + rels + close
                        if len(seq) <= max_length:
                            yield seq
```

### A2: Sequence Validation

Use algebraic properties for fast validation:

```python
def is_valid_algebraic(seq):
    # Check entity first
    if seq[0] not in B:
        return False
    
    # Check closure last
    if seq[-1] not in O_close:
        return False
    
    # Check ordering
    precedence = get_precedence_sequence(seq)
    if not is_monotonic_increasing(precedence):
        return False
    
    return True
```

### A3: Semantic Extraction

Use homomorphisms to extract meaning:

```python
def extract_semantics(seq):
    entity = get_entity(seq[0])
    qualifiers = [q for q in seq if q in O_qual]
    quantity = sum([count_value(c) for c in seq if c in O_count])
    relations = [r for r in seq if r in O_rel]
    closure = get_closure(seq[-1])
    
    return {
        'entity': entity,
        'qualifiers': qualifiers,
        'quantity': quantity,
        'relations': relations,
        'closure': closure
    }
```

## Conclusion

The operator algebra of the Indus script reveals:

1. **Non-trivial structure**: Not just concatenation
2. **Strict constraints**: Enforced by algebraic properties
3. **Compositional semantics**: Meaning built systematically
4. **Computational tractability**: Efficient algorithms possible

This algebraic framework complements the automaton model and provides alternative tools for analysis.

## References

- Hopcroft, J. E., & Ullman, J. D. (1979). *Introduction to Automata Theory, Languages, and Computation*.
- Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*.
- Abstract Algebra principles applied to formal languages.

---

**Version**: 1.0  
**Date**: 2026-02-03  
**Author**: ShantiDraconis
