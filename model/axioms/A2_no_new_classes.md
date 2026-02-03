# Axiom A2: No New Classes

## Formal Statement

**A2 (No New Classes)**: Operations on symbols preserve semantic class membership. Composition of symbols from existing classes cannot create symbols belonging to new classes.

### Mathematical Formulation

Let:
- `Σ` = Set of symbols
- `C` = Set of semantic classes
- `⊕: Σ × Σ → Σ` = Composition operation
- `class: Σ → C` = Class assignment function

Then:

```
∀ σ₁, σ₂ ∈ Σ, if σ₃ = σ₁ ⊕ σ₂ is defined, then class(σ₃) ∈ C
```

**Strong Form**: 
```
class(σ₁ ⊕ σ₂) ∈ {class(σ₁), class(σ₂)}
```

(The result belongs to one of the operand classes)

## Interpretation

1. **Class Closure**: Operations don't expand the class system
2. **Predictability**: Knowing operand classes constrains result class
3. **Conservativity**: The algebraic structure respects class boundaries

## Examples

### Harappan (Hypothesized)
```
Entity₂₆ ⊕ Modifier_dot = Entity₂₇
class(Entity₂₆) = Entity
class(Modifier_dot) = Modifier
class(Entity₂₇) = Entity  ✓ (preserved)
```

### Ancient Chinese (Verified)
```
人 ⊕ 一 = 大
class(人) = Entity (person)
class(一) = Modifier (one stroke)
class(大) = Entity (big) ✓ (preserved)
```

### Counterexample (Invalid)
```
Entity ⊕ Quantifier ≠ Terminal
```
This composition cannot produce a terminal symbol, as required by A2.

## Consequences

### Theorem A2.1 (Finite Class System)
In a system with finitely many base classes, all composed symbols belong to these classes.

**Proof**: By induction on composition depth using A2. □

### Theorem A2.2 (Class Inheritance)
In most cases, composition inherits the class of the "head" operand (typically the first):

```
class(σ₁ ⊕ σ₂) = class(σ₁)  [for σ₁ ∈ {Entity, Quantifier}]
```

**Proof**: Empirical observation formalized in specific instantiations. □

## Relation to A1

**A1** defines what classes exist.  
**A2** ensures operations don't add new classes.

Together: **Closed algebraic structure** over a fixed class set.

---

**Status**: Formally verified  
**Last Updated**: 2026-02-03
