# Quick Reference Guide

## Running the Examples

### 1. Core System Demo
```bash
python src/harappan_core.py
```
Shows basic inscription creation, validation, and semantic interpretation.

### 2. Chinese-Harappan Comparison
```bash
python examples/chinese_harappan_comparison.py
```
Demonstrates structural equivalence between Chinese radicals and Harappan operators.

### 3. Theorem Validation
```bash
python examples/theorem_validation.py
```
Validates key theorems through concrete examples:
- Theorem 2: Decidability
- Theorem 3: DFA Isomorphism
- Axiom 10: Monotone Progression
- Axiom 5: Linear Order
- Theorem 5: Descriptive Incompleteness

### 4. Composition Examples
```bash
python examples/composition_examples.py
```
Demonstrates the ⊕ operator and symbol composition:
- Axiom 2: Hierarchical Compositionality
- Axiom 18: Modifier Algebra
- Axiom 8: Property Inheritance
- Axiom 24: Core Modifiers

## Core Concepts

### Symbol Classes
```python
ENT    = Entity       # Base agent/entity
QUAL   = Qualifier    # State modifier
COUNT  = Counter      # Quantity
REL    = Relation     # Institutional relation
CLOSE  = Closure      # Validation marker
```

### Automaton States
```python
Q0 = Initial
Q1 = Entity_Loaded
Q2 = Qualified
Q3 = Counted
Q4 = Related
Q5 = Closed (absorbing)
```

### Composition Operator
```python
# Axiom 2: s = B ⊕ ⨁_{m∈M} m
symbol = CompositionEngine.compose(base, modifiers)
```

### Valid Inscription Structure
```
ENT → [QUAL] → [COUNT] → [REL] → CLOSE

Where:
- ENT is mandatory first element
- CLOSE is mandatory last element
- Intermediate elements follow strict order
- Elements can be skipped
- Maximum length is 5 symbols
```

## Key Axioms Summary

| Axiom | Statement |
|-------|-----------|
| 0 | System exists and is operational |
| 1 | Form-function duality (417 symbols) |
| 2 | Hierarchical composition (30 bases, 15 modifiers) |
| 3 | Finite state space (max length 5) |
| 4 | Entity primacy (start with ENT) |
| 5 | Strict linear order |
| 6 | Terminal closure (end with CLOSE) |
| 9 | System determinism (DFA) |
| 10 | Monotone progression (no regression) |
| 11 | Closure absorption (Q5 absorbing) |
| 27 | Anti-narrative (no stories) |

## Implementation Architecture

```
src/
├── __init__.py         # Package exports
└── harappan_core.py    # Core implementation
    ├── Symbol          # Individual symbol with class
    ├── Inscription     # Sequence of symbols
    ├── HarappanAutomaton  # DFA validator
    ├── CompositionEngine  # Symbol composition
    └── SemanticInterpreter  # State mapping
```

## Chinese-Harappan Equivalence

| Chinese Radical | Function | Harappan Operator |
|-----------------|----------|-------------------|
| 人 (rén) | agent | 373 Entity Base |
| 一 (yī) | intensity | Crown/Comb |
| 口 (kǒu) | channel | U-shape |
| 心 (xīn) | internal state | Fill |
| 力 (lì) | energy | Hook/Arm |

Both systems: **Base + Operator → New State**

## Theoretical Results

### Theorem 1: Completeness
The system is complete for institutional validation.

### Theorem 2: Decidability
Validation is O(|w|) - linear in inscription length.

### Theorem 3: DFA Isomorphism
System ≅ Deterministic Finite Automaton

### Theorem 4: Shannon Optimality
Achieves information-theoretic optimum for validation.

### Theorem 5: Descriptive Incompleteness
Complete for validation, incomplete for narrative.

## Further Reading

- `docs/comparativo-operacional.md` - Detailed Chinese-Harappan comparison
- `docs/axiomatica-harappana.md` - Complete axiomatic system (31 axioms)
- `README.md` - Project overview and theoretical framework
