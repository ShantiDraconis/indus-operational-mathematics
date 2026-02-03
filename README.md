# Indus Operational Mathematics: TCOP Implementation

This repository contains the formal specification, proof, and computational implementation of the **Theorem of Primitive Operational Composition (TCOP)**.

## Overview

The TCOP establishes that early non-phonetic graphic systems (such as the Indus Valley script, Ancient Chinese characters, early Egyptian hieroglyphs, and the Phaistos Disk) encode ontological classes and operational state transitions through finite graphical composition, implementing a closed algebra of validation rather than natural language.

### One-Line Summary

**Theorem (Primitive Operational Composition):** Early non-phonetic graphic systems encode ontological classes and operational state transitions through finite graphical composition, implementing a closed algebra of validation rather than natural language.

## Contents

- **tcop_theorem.tex** - Complete LaTeX document with formal theorem, proof, corollaries, and defense against criticisms
- **tcop_model.py** - Python implementation of the computational model (DFA + attributes)
- **examples/** - Example implementations for Harappan and Ancient Chinese systems

## Key Concepts

### Formal System Definition

A primitive graphic system is defined as **S = (B, O, Σ)** where:
- **B** = finite set of base symbols (ontological classes)
- **O** = finite set of graphical operators
- **Σ** = set of realized graphic states (compound symbols)

### Five Fundamental Hypotheses

1. **Finiteness:** |B| ≪ |Σ| (base symbols much fewer than realized states)
2. **Composition:** Every symbol s ∈ Σ can be decomposed as s = oₙ ∘ oₙ₋₁ ∘ ... ∘ o₁(b)
3. **Stability:** Operators don't create new classes, only new states
4. **Closure:** Terminal operators mark completion states
5. **Distribution:** Frequencies follow truncated Zipf-like hierarchy

### Modern Equivalents

Systems satisfying TCOP are formally equivalent to:
- Workflows
- Ledgers
- Finite automata
- JSON validation schemas
- State machines

They are **NOT** equivalent to:
- Literary texts
- Phonetic writing systems
- Natural language encodings

## Usage

### Running the Computational Model

```bash
python tcop_model.py
```

This will demonstrate:
1. Harappan script as a TCOP system
2. Ancient Chinese radicals as a TCOP system
3. TCOP validation for each system
4. Example states and their frequencies
5. JSON export of system structure

### Generating the LaTeX Document

```bash
pdflatex tcop_theorem.tex
```

Or use your preferred LaTeX compiler. The document includes:
- Formal theorem statement
- Complete proof with lemmas
- Four corollaries (Chinese, Harappan, Cognitive Universal, Mathematical Limit)
- Defense against linguistic, archaeological, historical, and universalist criticisms

## Examples

### Harappan Script

```python
from tcop_model import create_harappan_example, TCOPValidator

# Create system
harappan = create_harappan_example()
print(harappan)  # GraphicSystem('Harappan Script': |B|=4, |O|=5, |Σ|=29)

# Validate TCOP conditions
results = TCOPValidator.validate_system(harappan)
print(f"TCOP satisfied: {results['tcop_satisfied']}")  # True
```

### Ancient Chinese

```python
from tcop_model import create_ancient_chinese_example

# Create system
chinese = create_ancient_chinese_example()

# Get state by composition: 人 + duplication = 从 (follow)
state = chinese.get_state_by_composition("person", ["double", "terminal"])
print(state)  # 人 (rén) + [double, terminal]
```

## Corollaries

### 1. Ancient Chinese Application

The radical 人 (rén) doesn't have fixed semantic meaning but defines an agent class whose state varies with operators:

```
State = Human ∘ Σ Operators
```

### 2. Harappan Application

Harappan symbols are validated states, explaining:
- Short inscriptions (5-10 symbols)
- No narrative structure
- Recurrent terminal signs
- Saturation at ~417 states

### 3. Cognitive Universal

Systems like Harappan, Egyptian hieroglyphs, Ancient Chinese, and Phaistos Disk share a common cognitive substrate where graphical operators precede phonetic languages.

### 4. Mathematical Limit

Mathematics in such systems is finite, relational, and state-based:

```
N_finite + relations + partial orders
```

Symbolic algebra requires a different paradigm.

## Defense Against Criticisms

### Linguistic Criticism

**Q:** "All writing systems encode language, so these must encode language."

**A:** This assumes the conclusion. TCOP shows these systems implement operational algebras. The absence of long narratives, phonetic correspondences, and recursive structures supports the operational interpretation.

### Archaeological Criticism

**Q:** "Without bilingual texts, we can't know what these encode."

**A:** TCOP is based on structural analysis, not translation. Mathematical properties (finite states, compositional operators, statistical regularities) can be determined without decipherment.

### Historical Criticism

**Q:** "These systems evolved into phonetic writing, so they must have been proto-phonetic."

**A:** Evolution doesn't imply identity. TCOP describes systems at a specific historical moment. Later phonetic development doesn't invalidate earlier operational nature.

### Universalist Criticism

**Q:** "The theorem claims universal cognitive constraints without evidence."

**A:** TCOP claims structural equivalence under specific constraints (finite memory, institutional record-keeping, visual distinctiveness), not universal laws. It makes testable predictions.

## Mathematical Properties

The proof establishes four key lemmas:

1. **Finite State Space:** |Σ| ≤ |B| · ∏(|Oᵢ| + 1)
2. **Operational Closure:** System partitions into equivalence classes with terminal states
3. **Automaton Equivalence:** System ≡ DFA with attribute functions
4. **Non-linguistic Nature:** Structural properties incompatible with natural language

## Testable Predictions

TCOP predicts that systems satisfying its conditions will exhibit:

1. ✓ Short inscriptions (bounded by finite state space)
2. ✓ Recurrent base symbols across corpus
3. ✓ Systematic graphical modifications
4. ✓ Terminal/closing symbols
5. ✓ Truncated Zipf distribution (α ∈ [0.8, 1.2])
6. ✗ Long narrative texts
7. ✗ Recursive grammatical structures
8. ✗ Unbounded symbol combinations

## Applications

### Undeciphered Scripts

TCOP provides a framework for analyzing:
- Indus Valley script
- Linear A
- Rongorongo
- Proto-Elamite
- Other undeciphered systems

### Comparative Analysis

TCOP enables formal comparison across:
- Different historical periods
- Different geographical regions
- Different cultural contexts

Without assuming common origin or continuous transmission.

## Implementation Details

### State Representation

States are represented as tuples (base, operators):

```python
State(base=BaseSymbol("fish", "Fish", "animal"),
      operators=frozenset(["stroke1", "terminal"]))
```

### Transition Function

Transitions apply operators to states:

```python
δ((b, O'), o) = (b, O' ∪ {o})
```

### Accepting States

States containing terminal operators are accepting:

```python
F = {(b, O') : O' ∩ O_T ≠ ∅}
```

## Limitations

TCOP does **NOT** claim:
- Direct historical connection between systems
- Linguistic identity across systems
- Cultural transmission
- Universality without exceptions

TCOP claims **ONLY**:
- Structural equivalence under common cognitive and functional constraints

## Future Work

1. **Extended Corpus Analysis:** Apply TCOP to complete Harappan corpus
2. **Statistical Validation:** Detailed Zipf distribution analysis
3. **Comparative Studies:** Cross-system structural comparison
4. **Computational Tools:** Automated TCOP validation tools
5. **Archaeological Integration:** Combine with archaeological context
6. **Cognitive Science:** Link to modern cognitive theories

## References

### Primary Sources
- Indus Valley inscriptions corpus
- Ancient Chinese oracle bone inscriptions
- Early Egyptian hieroglyphic texts
- Phaistos Disk

### Theoretical Background
- Finite automata theory
- Formal language theory
- Cognitive archaeology
- History of writing systems

## License

See LICENSE file for details.

## Citation

If you use this work, please cite:

```
TCOP: Theorem of Primitive Operational Composition
Repository: indus-operational-mathematics
Year: 2026
```

## Contributing

Contributions welcome, especially:
- Corpus data for validation
- Additional system implementations
- Statistical analyses
- Criticism and counter-arguments
- Extensions and refinements

## Contact

For questions, discussions, or collaborations, please open an issue in this repository.

---

**Note:** This is a theoretical framework for understanding primitive graphic systems. It makes testable predictions but does not claim to "decipher" undeciphered scripts. The value lies in providing structural tools for analysis and comparison.