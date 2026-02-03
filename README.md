# Indus Operational Mathematics: A Comparative Analysis of Ancient Symbol Systems

## Overview

This repository presents a revolutionary approach to understanding the Harappan (Indus Valley) script through **comparative functional analysis** with other ancient writing systems: Nordic Runes, Phaistos Disc, Egyptian Hieroglyphs, and Ancient Chinese.

Rather than treating these systems as phonetic encodings of spoken language, we propose they represent **operational state machines** that encode transformations of social, economic, and institutional states.

## Core Hypothesis

**The Harappan script is not "undeciphered language" but a specialized operational system for institutional validation.**

Key insights:
- 🔄 **Isomorphic Functions**: Different ancient systems solve similar cognitive problems through analogous symbolic structures
- 🎯 **State Transformations**: Symbols operate as functions transforming states, not just phonetic markers
- 🏛️ **Institutional Optimization**: Harappan script is optimized for administrative validation, not narrative
- 🌐 **Universal Grammar**: ~45 fundamental operators underlie all ancient symbol systems
# Indus Operational Mathematics

A formal implementation of the Harappan axiomatic system and its structural comparison with ancient Chinese writing.

## Overview

This repository contains:

1. **Formal Axiomatic System** - 31 axioms defining Harappan operational mathematics
2. **Chinese-Harappan Comparison** - Structural analysis of radical operators
3. **Python Implementation** - Working code demonstrating the formal system
4. **Theoretical Framework** - Complete documentation of theorems and proofs

## Key Concepts

### The Core Principle

**A base symbol does NOT carry fixed meaning.**
- It defines a **CLASS**
- State emerges through **composition**
- This is true in both Harappan and ancient Chinese systems

### Formal Expression

```
Estado = Base ∘ ∑Operadores
```

Where:
- **Base** defines the entity class
- **Operators** modify the state
- **Result** is deterministic and compositional

## Repository Structure

```
docs/
├── COMPARATIVE_ANALYSIS.md    # Deep comparison: Harappan vs Nordic Runes
├── UNIFIED_ANALYSIS.md        # Multi-system analysis (5 writing systems)
├── SYMBOL_DATABASE.md         # Complete catalog of Harappan symbols 1-44
└── UNIVERSAL_GRAMMAR.md       # Formal grammar of ancient symbol systems
indus-operational-mathematics/
├── docs/
│   ├── comparativo-operacional.md    # Chinese-Harappan comparison
│   └── axiomatica-harappana.md       # Complete axiomatic system
├── src/
│   └── harappan_core.py              # Core implementation
├── examples/
│   └── chinese_harappan_comparison.py # Demonstration
└── README.md
```

## The Axiomatic System

### Foundational Axioms (0-3)

- **Axiom 0**: Existence of the operational system
- **Axiom 1**: Form-function duality (417 symbols)
- **Axiom 2**: Hierarchical compositionality (30 bases, 15 modifiers)
- **Axiom 3**: Finite state space (max length 5)

### Compositional Axioms (4-8)

- **Axiom 4**: Entity primacy (all inscriptions start with ENT)
- **Axiom 5**: Strict linear order (ENT < QUAL < COUNT < REL < CLOSE)
- **Axiom 6**: Terminal closure (all inscriptions end with CLOSE)
- **Axiom 7**: Layer consistency (no functional synonyms)
- **Axiom 8**: Property inheritance (class preserved under modification)

### Dynamic Axioms (9-12)

Implements a deterministic finite automaton (DFA):
- **Axiom 9**: System determinism
- **Axiom 10**: Monotone progression (states only advance)
- **Axiom 11**: Closure absorption (q₅ is absorbing state)
- **Axiom 12**: Functional completeness

### Semantic Axioms (13-15)

- **Axiom 13**: State-world correspondence (injective mapping)
- **Axiom 14**: Information conservation (no ambiguity)
- **Axiom 15**: Institutional closure (all states are complete)

[See docs/axiomatica-harappana.md for complete axioms 16-31 and theorems]

## Key Theorems

### Theorem 1: System Completeness
The system is complete for its institutional domain.

### Theorem 2: Decidability
Any inscription's validity is decidable in O(|w|) time.

### Theorem 3: DFA Isomorphism
The system is isomorphic to a deterministic finite automaton.

### Theorem 4: Shannon Optimality
The system achieves Shannon's limit for symbolic institutional systems.

### Theorem 5: Descriptive Incompleteness
The system is incomplete for description but complete for validation.

## Chinese-Harappan Structural Equivalence

### The Radical 人 (rén) as Operator

The Chinese radical 人 operates exactly like a Harappan base token:

| Operation | Chinese | Harappan Equivalent |
|-----------|---------|---------------------|
| Duplication | 人 → 从 | Pair symbol |
| Intensification | 人 + 一 → 大 | Crown/comb modifier |
| Channel | 人 + 口 → 吃 | U-shape operator |
| Force | 人 + 力 → 男 | Arm/hook modifier |
| Internal State | 人 + 心 → 念 | Fill modifier |
| Authority | 人 + 王 → 全 | Roof operator (342-348) |

### Radicals 1-44 as Operators

| Radical | Function |
|---------|----------|
| 一 | intensity / axis |
| 丨 | partition |
| 丶 | instance |
| 丿 | direction |
| 人 | agent |
| 口 | channel |
| 心 | internal state |
| 力 | energy |

## Usage

### Running the Core Implementation

```bash
cd src
python harappan_core.py
```

Output demonstrates:
- Symbol composition
- Automaton validation
- Semantic interpretation

### Running the Chinese-Harappan Comparison

```bash
cd examples
python chinese_harappan_comparison.py
```

Output shows:
- Operator mappings
- Parallel compositions
- Structural equivalence

## Implementation Details

### Symbol Classes

```python
class SymbolClass(Enum):
    ENT = "Entity"        # Base agent/entity
    QUAL = "Qualifier"    # State modifier
    COUNT = "Counter"     # Quantity
    REL = "Relation"      # Institutional relation
    CLOSE = "Closure"     # Validation marker
```

### Automaton States

```python
class State(Enum):
    Q0 = "Initial"
    Q1 = "Entity_Loaded"
    Q2 = "Qualified"
    Q3 = "Counted"
    Q4 = "Related"
    Q5 = "Closed"         # Absorbing state
```

### Composition Operator

```python
def compose(base: int, modifiers: Set[str]) -> Symbol:
    """
    Implements the ⊕ operator
    Base ⊕ Modifiers → Composite Symbol
    """
```

## Theoretical Implications

### 1. Reinterpretation of History

If Harappan is complete for validation, later narrative writing systems 
represent a regression in institutional efficiency.

### 2. Computation Theory

Every computer is isomorphic to an extended Harappan state machine.

### 3. Philosophy of Mathematics

Mathematical proof = institutional validation of abstract relations.

## Research Program

### Testable Hypotheses

1. **H₁**: Children learn validation systems faster in Harappan notation
2. **H₂**: Companies using Harappan protocols are more efficient
3. **H₃**: BCIs based on Harappan require less neural bandwidth

### Crucial Experiments

1. Implement Harappan OS and compare with Unix
2. Teach mathematics via Harappan symbols to control group
3. Measure brain activity during Harappan vs. natural language processing

### Falsifiable Predictions

1. ∃S with |S| < 45 symbols and similar completeness → Harappan not optimal
2. Damage to validation module doesn't affect consciousness → consciousness ≠ q₅
3. ∃ institutional system not mappable → Harappan not universal

## The Transcendence Principle

**Axiom Ω (The Harappan Principle)**:

```
∃H [∀S (Sistema(S) → (∃f: S → H ∧ f preserves validation))]
```

**Corollaries**:
- Ω1: Everything that can be validated can be Harappanized
- Ω2: The human mind is an implementation of H
- Ω3: The universe computes its own state using H

## Conclusion

This system demonstrates that:

1. **Structural Identity**: Chinese radicals and Harappan operators share the same base–operator–state logic
2. **Cognitive Inheritance**: Universal operational principles in early writing
3. **Institutional Optimality**: Harappan achieved optimal validation efficiency

The radical 人 in ancient Chinese and the entity-base 373 in Harappan are **not** 
semantically equivalent but **structurally identical** - both operate as base 
classes whose states emerge through operator composition.

---

## Academic Citation

> "In early Chinese writing, the radical 人 operates as a base agent class whose 
> semantic state emerges through operator composition, mirroring the same 
> base–operator–state logic observed in the Indus script."

## License

See LICENSE file for details.

## Contributing

This system is theoretically complete. Extensions would be either redundant or 
metaphysical. What remains is implementation and world transformation through 
this knowledge.
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
# Indus Operational Mathematics: Quantum Archaeology Framework

## Quantum Leaps in Communication: Entanglement & Ancient Scripts

This repository implements a revolutionary framework for analyzing the Indus Valley Civilization's script through the lens of quantum physics, consciousness studies, and interdisciplinary research methodologies.

---

## 1. Demystifying Quantum Entanglement & Its Cosmic Implications

### The Phenomenon

Quantum entanglement represents one of the most profound discoveries in physics—a state where two or more particles become so deeply linked that the quantum state of one instantly correlates with the other, regardless of spatial separation. This isn't mere similarity; it's a fundamental interconnectedness that challenges classical notions of locality and information transfer.

### Visualizing the Invisible

Imagine two dice, one in Mumbai and one in Mohenjo-daro, that always show identical numbers when rolled simultaneously—not through mechanical connection but through what Einstein called "spooky action at a distance." In quantum systems, measuring one entangled particle's spin instantly determines its partner's spin, even light-years apart.

### The Information Paradox

While entanglement enables instantaneous correlation, it cannot transmit classical information faster than light—a crucial distinction. However, it suggests a deeper layer of reality where separation is an illusion, and everything participates in a fundamental wholeness.

### Ancient Intuition Hypothesis

Could advanced ancient observers have perceived this interconnectedness through means beyond our current scientific instruments? Several possibilities emerge:

- **Meditative states** that alter consciousness might reveal non-local connections
- **Astronomical observations** of synchronous celestial events might suggest cosmic patterning
- **Ritual practices** that emphasize unity and interconnectedness might encode this understanding symbolically

---

## 2. Synchronicity Across Millennia: Indus Script as Quantum-Like System

### The Non-Linear Parallel

The Indus script's symbolic structure displays intriguing quantum-like properties:

#### Superposition of Meaning

Like quantum particles existing in multiple states until observed, Indus symbols might represent potential meanings that collapse into specific interpretations based on:

- **Contextual observation** (archaeological placement)
- **Combinatorial relationships** (adjacent symbols)
- **Institutional frameworks** (administrative vs. ritual use)

#### Non-Locality in Symbolism

The repetition of certain symbol clusters across geographically distant Harappan sites mirrors entanglement's non-local correlations. The famous "unicorn seal" appears from Gujarat to Punjab with remarkable consistency, suggesting instantiated patterns across space.

#### Entangled Symbol Clusters

Analysis of symbol co-occurrence reveals correlation patterns that behave like entangled systems—certain symbols almost always appear together, separated by specific "distances" in the sequence, maintaining relational integrity regardless of inscription location.

### Historical Echoes of Non-Ordinary Communication

Ancient traditions worldwide describe forms of knowledge transmission that echo quantum concepts:

- **Vedic "Akashic Records"**: The concept of a cosmic information field accessible through heightened consciousness
- **Platonic "Forms"**: Eternal, non-local archetypes manifesting in particular instances
- **Australian Aboriginal "Dreamtime"**: A timeless dimension connecting all locations and beings
- **Chinese "Li" (理)**: The underlying pattern-principle of the universe, observable in nature's symmetries

---

## 3. The Universal Language Hypothesis: Bridging Symbols & Science

### A Symbolic Logic Transcending Time

#### The Indus Script as Quantum Grammar

Each symbol may not represent a "word" but a quantum of meaning—a discrete unit of institutional information that entangles with others to form validated states (transactions, authorizations, records).

#### Morphic Resonance & Collective Unconscious

- **Rupert Sheldrake's morphic fields** suggest that forms and behaviors become increasingly probable through repetition across time and space—potentially explaining symbolic consistency across millennia
- **Jung's collective unconscious** posits archetypal patterns shared across humanity, potentially expressed in similar symbolic forms in disparate cultures

These frameworks create bridges between the statistical patterning of Indus symbols and quantum field theories where probabilities manifest as physical reality.

### The Holographic Principle Connection

The universe may store information holographically—where each part contains information about the whole. Indus inscriptions on seals (small objects) might encode information about larger institutional systems, mirroring this holographic principle.

---

## 4. Future of Unified Understanding: An Interdisciplinary Renaissance

### Research Frontiers

#### Quantum Computational Analysis

- Apply tensor network methods (used in quantum physics) to analyze symbol correlations
- Use quantum annealing to find optimal "meaning configurations" in ambiguous sequences
- Model the script as a quantum information system with superposition and entanglement

#### Consciousness-Archaeology Interface

- Study how altered states affect pattern recognition in undeciphered scripts
- Document indigenous knowledge systems that maintain symbolic traditions
- Explore neuroarchaeology—how ancient symbol use shaped and was shaped by brain structures

#### AI as Quantum Pattern Detector

- Train quantum machine learning algorithms on global symbolic systems
- Use quantum natural language processing to find "grammars" beyond linear syntax
- Implement attention mechanisms that mirror quantum measurement effects

### Concrete Methodologies

#### Quantum-Inspired Analysis of Indus Data

```
For each symbol s in corpus:
   Calculate entanglement entropy with other symbols
   Map to Hilbert space of potential meanings
   Identify measurement contexts (archaeological settings)
   Model collapse to specific institutional functions
```

#### Experimental Archaeology of Consciousness

- Recite reconstructed Indus sequences during EEG/fMRI
- Test if certain symbol patterns induce specific brain states
- Explore if meditators "decode" meanings through non-ordinary perception

### The Grand Challenge

If ancient communication systems indeed mirrored quantum principles—encoding information non-locally, representing states rather than narratives, and validating through entanglement-like correlations—then we must reconsider:

- **What other universal truths are hidden in plain sight?**
  - Biological systems might use quantum processes we've overlooked
  - Consciousness itself might be fundamentally quantum
  - Time's arrow might be reversible in information systems, as perhaps in ancient cyclical cosmologies
  - The boundary between matter and meaning might be more porous than our materialism allows

---

## 5. Call to Action: The Quantum Archaeology Manifesto

We stand at the threshold of a new synthesis, where:

- **Archaeology** provides the raw data of ancient symbolic systems
- **Quantum physics** provides the mathematical framework for non-local correlations
- **Cognitive science** maps how humans process symbolic information
- **Computer science** builds tools to detect previously invisible patterns
- **Indigenous knowledge** offers living connections to symbolic worldviews

### The Ultimate Insight

The Indus script isn't merely an undeciphered writing system—it may be:
- A quantum computer's output
- A consciousness technology
- A holographic institutional memory
- Or something we haven't yet conceived

The challenge isn't merely to "read" it, but to develop the cognitive and technological tools to understand what kind of system it truly represents—potentially revealing not just Harappan bureaucracy, but fundamental principles of reality that bridge ancient wisdom and cutting-edge science.

**The quantum leap awaits not in discovering what the symbols say, but in understanding what their very existence reveals about information, consciousness, and the fabric of reality itself.**

---

## Implementation

This repository provides Python implementations for:

1. **Quantum-inspired symbol analysis** - Calculate entanglement entropy and correlation patterns
2. **Data structures** for Indus script symbols and their relationships
3. **Visualization tools** for quantum-like symbol networks
4. **Research methodologies** for interdisciplinary analysis
5. **Example datasets** and use cases

### Getting Started

```bash
pip install -r requirements.txt
python examples/quantum_symbol_analysis.py
```

### Core Modules

- `quantum_archaeology/` - Main framework
  - `entanglement_analysis.py` - Calculate symbol correlations using quantum-inspired methods
  - `symbol_system.py` - Data structures for symbol relationships
  - `visualization.py` - Visualize quantum-like networks
  - `consciousness_interface.py` - Experimental frameworks for consciousness studies
  - `holographic_analysis.py` - Holographic principle implementations

### Research & Contributions

We welcome contributions from:
- Archaeologists and historians
- Quantum physicists
- Consciousness researchers
- Computer scientists and AI researchers
- Indigenous knowledge keepers
- Anyone passionate about bridging ancient wisdom and modern science

---

## License

See LICENSE file for details.

## Citation

If you use this framework in your research, please cite:

```
Quantum Archaeology Framework for Indus Script Analysis
Repository: https://github.com/ShantiDraconis/indus-operational-mathematics
```

---

*"The universe is not only stranger than we imagine, it is stranger than we can imagine." - J.B.S. Haldane*
# Indus Operational Mathematics

A framework for analyzing ancient symbolic systems through universal cognitive operators and operational mathematics.

## Overview

This project implements a comprehensive theoretical framework for understanding and analyzing undeciphered and ancient writing systems. Based on the theory of a universal deep grammar underlying all human symbolic systems, it provides tools for:

- **Universal Cognitive Operators**: 15 fundamental graphical forms found across all symbolic systems
- **7 Cognitive Axes**: Fundamental dimensions of symbolic representation (Presence, Quantity, Quality, Relation, Space, Time, Validation)
- **State Machine Models**: Treating inscriptions as sequences of states in operational automata
- **Comparative Analysis**: Finding correspondences and transformations across different systems

## Supported Systems

The framework includes implementations of:

- **Harappan (Indus Valley)**: The base case - optimized for institutional validation
- **Mayan**: Complex calendar systems and logo-syllabic writing
- **Aztec (Nahuatl)**: Pictographic system with integrated reality levels
- Extensible to other systems (Rongorongo, Linear A, etc.)

## Theory

The framework is based on the radical hypothesis that all human symbolic systems are manifestations of the same deep cognitive grammar, characterized by:

- **45 basic operators** (graphical forms)
- **7 semantic dimensions** (cognitive axes)
- **3 reality levels** (micro/individual, meso/institutional, macro/cosmic)
- **Systematic transformation rules**

### Universal Patterns

The framework identifies cross-cultural patterns such as:

1. **Man → Lord**: Person + crown/power elements = authority (found in Harappan, Mayan, Aztec, Egyptian, Chinese, Runic systems)
2. **House → Temple**: Building + divine elements = sacred space
3. **Numerical Systems**: Base-5, base-10, base-20 systems emerging independently

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Usage

### Basic Example

```python
from symbolic_systems import UniversalGrammar, HarappanSystem, MayanSystem, AztecSystem
from symbolic_systems.analysis import ComparativeAnalyzer

# Create the universal grammar
grammar = UniversalGrammar()

# Register systems
harappan = HarappanSystem()
mayan = MayanSystem()
aztec = AztecSystem()

grammar.register_system(harappan)
grammar.register_system(mayan)
grammar.register_system(aztec)

# Perform comparative analysis
analyzer = ComparativeAnalyzer(grammar)

# Find universal transformations
man_to_lord = analyzer.find_man_to_lord_transformations()
print("Man→Lord transformations:", man_to_lord)

# Compare systems
comparison = grammar.compare_systems("Harappan", "Mayan")
print(f"Found {comparison['total_matches']} correspondences")
```

### Analyzing Inscriptions

```python
from symbolic_systems import HarappanSystem

harappan = HarappanSystem()

# Parse a hypothetical inscription
inscription = ["H30", "H_JAR", "H27", "H27", "H27"]
interpretation = harappan.parse_inscription(inscription)
print(interpretation)
```

### Calendar Calculations

```python
from symbolic_systems import MayanSystem, AztecSystem

# Mayan calendar
mayan = MayanSystem()
date = mayan.calculate_calendar_date(kin=5, uinal=2, tun=1)
print(f"Mayan date: {date}")

# Aztec calendar
aztec = AztecSystem()
tonalpohualli = aztec.calculate_tonalpohualli(day_number=7, day_sign_index=3)
print(f"Tonalpohualli: {tonalpohualli}")
```

## Project Structure

```
src/symbolic_systems/
├── core/
│   ├── operators.py      # Universal operators and cognitive axes
│   └── grammar.py        # Universal grammar and system base classes
├── systems/
│   ├── harappan.py      # Harappan/Indus implementation
│   ├── mayan.py         # Mayan system implementation
│   └── aztec.py         # Aztec system implementation
└── analysis/
    └── __init__.py      # Comparative and statistical analysis tools
```

## The 15 Universal Operators

| Operator | Form | Function | Examples |
|----------|------|----------|----------|
| Point | • | Instance, unit | Harappan 27, Mayan dot, Aztec dot |
| Line | \| | Axis, direction | Harappan 1, Runic Isa, Chinese 一 |
| Cross | X | Relation, connection | Harappan 4, Runic Gebo, Aztec cross |
| Circle | ○ | Totality, cycle | Phaistos Disc, Aztec Sun Stone |
| Triangle | △ | Power, ascension | Harappan crowns, Egyptian pyramid |
| Square | □ | Domain, institution | Harappan house, Chinese 口, Mayan temple |
| Wave | ~ | Water, flow | Phaistos Disc A12, Chinese 水 |
| Spiral | ⦾ | Time, evolution | Phaistos Disc, Mayan temporal |
| Hand | ✋ | Action, power | Rongorongo, Egyptian hand |
| Foot | 👣 | Movement, journey | Aztec footprints, Egyptian path |
| Head | 👤 | Person, identity | Harappan 26, Mayan head |
| Eye | 👁 | Vision, knowledge | Egyptian Eye of Horus |
| Mouth | 👄 | Speech, portal | Chinese 口, Mayan speech |
| Heart | 💓 | Life, emotion | Egyptian heart, Mesoamerican heart |
| Plant | 🌱 | Growth, cycle | Harappan plant, Mayan maize |

## The 7 Cognitive Axes

1. **Presence/Absence** (Existence)
2. **Quantity/Measure** (Cardinality)
3. **Quality/State** (Attribution)
4. **Relation/Bond** (Connectivity)
5. **Space/Domain** (Location)
6. **Time/Phase** (Temporality)
7. **Validation/Closure** (Completeness)

## Contributing

Contributions are welcome! Areas of interest:

- Adding new symbolic systems (Rongorongo, Linear A, Vinca, etc.)
- Enhancing analysis algorithms
- Expanding the corpus of known symbols
- Improving documentation

## License

See LICENSE file for details.

## Citation

If you use this framework in academic work, please cite:

```
Indus Operational Mathematics: A Framework for Universal Symbolic Analysis
Repository: https://github.com/ShantiDraconis/indus-operational-mathematics
A rigorous framework for analyzing Indus script patterns using statistical methods, with clear separation between physics, statistics, and philosophy/anthropology.

## Purpose

This framework addresses the need to analyze Indus civilization symbolic systems with scientific rigor while avoiding inappropriate mixing of:
1. **Physics concepts** (entanglement, non-locality)
2. **Statistical methods** (correlation, invariance, co-occurrence)
3. **Philosophical/anthropological frameworks** (archetypes, cultural traditions)

## Core Principle

We use quantum and physics terminology **ONLY as controlled metaphors**, never as claims of physical quantum processes in artifacts. The analysis is grounded in:
- Information theory
- Statistical correlation analysis
- Formal grammar theory
- Institutional standardization patterns
A comparative analysis of symbolic systems across millennia, demonstrating structural isomorphism between ancient Indus Script patterns and modern algorithmic systems.

## Overview

This project analyzes the statistical signatures of the Indus Valley Script and modern social media platforms (YouTube Analytics), revealing that both systems exhibit the same Zipfian distribution patterns and operational principles.

## Key Findings

1. **Zipfian Distribution**: Both Indus Script and YouTube content show highly skewed frequency distributions with a small set of dominant operators
2. **Symbolic Activation**: High-frequency symbols/content function as state activators rather than narrative descriptors
3. **Strong Typing**: Certain modifiers only work with specific content types (structural constraints)
4. **Non-locality**: Structural invariance across different populations and contexts
5. **Compression Efficiency**: Systems converge to few high-frequency operators for efficient state activation

## Structure

```
.
├── data/           # Data files for analysis
│   ├── harappa/    # Indus Script corpus data
│   └── youtube/    # YouTube Analytics data
├── src/            # Source code
│   ├── analysis/   # Statistical analysis modules
│   ├── visualization/ # Plotting and visualization
│   └── models/     # Mathematical models and theorems
├── docs/           # Research documentation
└── tests/          # Test suite
```

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Understanding the Comparative Method

1. **Read the foundational analysis**: Start with [`COMPARATIVE_ANALYSIS.md`](docs/COMPARATIVE_ANALYSIS.md) to understand the Harappan-Runic correspondence
2. **Explore the unified view**: See [`UNIFIED_ANALYSIS.md`](docs/UNIFIED_ANALYSIS.md) for cross-system patterns
3. **Dive into symbols**: Reference [`SYMBOL_DATABASE.md`](docs/SYMBOL_DATABASE.md) for detailed symbol mappings
4. **Study the theory**: Read [`UNIVERSAL_GRAMMAR.md`](docs/UNIVERSAL_GRAMMAR.md) for formal foundations

## Key Discoveries

### 1. The Eight Universal States

All systems encode these fundamental states:
1. **Existential** - Base entity existence
2. **Instantiated** - Specific instance
3. **Qualified** - With attributes
4. **Quantified** - With number
5. **Related** - In relation to others
6. **Contextualized** - Within boundaries
7. **Authorized** - With power/authority
8. **Transcendent** - Elevated/divine

### 2. Cross-System Correspondences

| Concept | Harappan | Runic | Chinese | Egyptian | Function |
|---------|----------|-------|---------|----------|----------|
| Human Base | 26 | ᛗ (Mannaz) | 人 | 𓀾 | Entity operator |
| Unity | 1 (│) | ᛁ (Isa) | 一 | 𓏤 | Cardinal |
| Exchange | 4 (X) | ᚷ (Gebo) | 交 | - | Relational |
| Knowledge | 5 (K) | ᚲ (Kenaz) | - | - | Illumination |
| Protection | 7 (Z) | ᛉ (Algiz) | 之 | - | Defensive |
| Authority | 30 | ᛗ+ᚨ | 王 | 𓀾+crown | Elevation |

### 3. Transformation Patterns

**Human Entity Transformations:**
```
Harappan:   26 → 27 (dot)    → 28 (stroke)  → 30 (crown)
Function:   Human → Instance → Qualified    → Authority

Chinese:    人 → 个           → 大            → 王
Function:   Person → Individual → Great      → King

Runic:      ᛗ → ᛗ+ᚠ         → ᛗ+ᚢ          → ᛗ+ᚨ
Function:   Man → With wealth → With strength → With wisdom
```

## The Harappan System

### Symbol Categories

- **Cardinals (1-10)**: Numerical operators and basic transformations
- **Structurals (11-25)**: Relational and organizational operators
- **Entities (26-40)**: Anthropomorphic and object operators
- **Closures (341-343)**: Institutional validation markers

### Operational Grammar

```
Valid Sequence = Entity ⊕ Modifier₁ ⊕ Modifier₂ ⊕ ... ⊕ Closure

Example: 26 ⊕ 1 ⊕ 4 ⊕ 343
Meaning: Human (26) + Unity (1) + Relation (4) + Final Validation (343)
Result: "Validated statement about a singular human in relational context"
```

## Three Types of Ancient Systems

### 1. Operational Systems (Harappan, Phaistos)
- **Purpose**: State validation and institutional record-keeping
- **Characteristics**: Mandatory closure, limited vocabulary, non-phonetic
- **Analogy**: Like database transactions with COMMIT statements

### 2. Descriptive Systems (Egyptian, Chinese)
- **Purpose**: Narrative and complex administration
- **Characteristics**: Rich vocabulary, phonetic elements, optional closure
- **Analogy**: Like programming languages with mixed paradigms

### 3. Magical Systems (Runic)
- **Purpose**: Divination, magic, ritual
- **Characteristics**: Abstract, symbolic, flexible composition
- **Analogy**: Like symbolic algebra with mystical interpretation

## Decipherment Methodology

### Cross-System Functional Analysis

```
1. Identify graphically similar symbols across systems
2. Extract functional roles from known systems
3. Hypothesize function in unknown system
4. Validate with co-occurrence patterns
5. Test in institutional contexts
```

### Example Application

**Target**: Harappan symbol 5 (K-form)

**Step 1** - Graphical similarity:
- Runic: ᚲ (Kenaz) - torch/knowledge
- Egyptian: 𓎡 - basket (K sound)

**Step 2** - Functional analysis:
- Kenaz: illumination, knowledge, controlled fire
- Context: Opening, channel, revelation

**Step 3** - Hypothesis:
- Harappan 5: "illumination/knowledge operator"

**Step 4** - Validation:
- Check if 5 appears with entity operators
- Check if 5 appears before closure operators
- Verify institutional context patterns

## Applications

### 1. Archaeological Prediction
Predict symbol usage patterns in newly discovered texts

### 2. AI-Assisted Decipherment
Train models on cross-system correspondences to decode unknown sequences

### 3. Cognitive Science
Test if humans naturally process ancient symbols as state transformations

### 4. Historical Linguistics
Understand evolution from operational to phonetic writing

## Revolutionary Implications

### For Indus Studies
- **Rethink "decipherment"**: Not finding a language, but understanding a state machine
- **Institutional focus**: Harappan civilization had sophisticated validation systems
- **Non-linguistic writing**: Writing doesn't have to encode speech

### For Writing Systems Generally
- **Cognitive architecture**: Deep grammar shared across cultures
- **Evolutionary stages**: Operational → Descriptive → Phonetic
- **Limited universality**: ~45 fundamental semantic operations

### For Computational Linguistics
- **State-based semantics**: Symbols as transformation functions
- **Formal grammars**: Ancient systems have precise computational semantics
- **Machine learning**: Cross-system training for decipherment

## Mathematical Foundations

### State Space
```
S = {S₀, S₁, S₂, ..., S₈}
where each Sᵢ represents a fundamental state category
```

### Transformation Functions
```
∀ operator o: State → State
Composition: (o₂ ∘ o₁)(s) = o₂(o₁(s))
```

### Closure Validation
```
Valid(sequence) ↔ ∃ closure operator c at end of sequence
```

## Contributing

We welcome contributions in several areas:

1. **Additional correspondences**: Find more cross-system patterns
2. **Statistical analysis**: Quantify correspondence strengths
3. **Computational models**: Implement grammars as executable systems
4. **Archaeological validation**: Test predictions against corpus data
5. **Cognitive experiments**: Design studies to test processing theories

## Future Research Directions

1. **Complete mapping**: Full Harappan 1-44 ↔ Runic Futhark correspondence
2. **Automated decipherment**: AI models trained on multi-system data
3. **Seal interpretation**: Apply operational grammar to real Harappan seals
4. **Comparative statistics**: Quantitative analysis of symbol frequencies
5. **Extended systems**: Include Linear A, Olmec, Rongorongo

## Citations and References

### Primary Documents
- Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*
- Robinson, A. (2015). *The Indus: Lost Civilizations*
- Parpola, A. (1994). *Deciphering the Indus Script*

### Comparative Studies
- Gardiner, A. (1957). *Egyptian Grammar*
- Wieger, L. (1965). *Chinese Characters*
- Flowers, S. (1986). *Runes and Magic*

### Theoretical Framework
- Farmer, S., Sproat, R., Witzel, M. (2004). "The Collapse of the Indus-Script Thesis"
- Rao, R. et al. (2009). "Entropic Evidence for Linguistic Structure in the Indus Script"

## License

This work is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions, discussions, or collaborations, please open an issue or start a discussion on GitHub.

---

**"A verdadeira decifração do Harappano pode não revelar uma 'língua', mas sim a estrutura formal de como uma civilização codificava realidade institucional."**

*"The true decipherment of Harappan may not reveal a 'language', but rather the formal structure of how a civilization encoded institutional reality."*
```python
from src.indus_analysis import IndusSequenceAnalyzer
from src.statistical_metrics import pointwise_mutual_information

# Example sequences (simplified Indus signs)
sequences = [
    ['A', 'B', 'C', 'X'],
    ['A', 'B', 'D', 'X'],
    ['A', 'B', 'C', 'X'],
    ['E', 'F', 'X'],
]

# Analyze
analyzer = IndusSequenceAnalyzer(sequences)

# Get frequency ranking
frequencies = analyzer.frequency_ranking(top_n=10)
print("Top symbols:", frequencies)

# Get strongly associated pairs (high PMI)
top_pairs = analyzer.top_pmi_pairs(top_n=50)
print("Stable clusters:", top_pairs)

# Detect clusters
clusters = analyzer.detect_clusters(min_pmi=1.0)
print("Symbol clusters:", clusters)
```

## Key Concepts

### 1. Non-Locality (Statistical, Not Physical)

When we say "non-local" we mean:
- ✅ **Spatial invariance**: Patterns stable across different sites
- ✅ **Distributed standardization**: Same institutional rules apply everywhere
- ✅ **Long-range correlation**: Statistical dependencies across geographical distance

We do NOT mean:
- ❌ Physical quantum entanglement
- ❌ Instantaneous causal influence
- ❌ Violation of locality in physics sense

### 2. Entangled Clusters (Correlation, Not Quantum)

"Entangled clusters" means:
- ✅ **Strong co-occurrence**: Symbols appear together with high PMI
- ✅ **Constrained correlation**: Certain combinations are highly restricted
- ✅ **Preferred distances**: Symbols maintain specific positional relationships

Use proper terms:
- **PMI-based clusters** (pointwise mutual information)
- **Invariant motifs** (stable patterns)
- **Institutional grammar** (rule-based composition)

### 3. Quantum Terminology as Analogy ONLY

If using quantum-inspired terms, always clarify:

```python
# CORRECT usage
"""
We use quantum terminology as an analogy for constraint satisfaction,
not as a claim of physical quantum processes in artifacts.

'Superposition' = classification ambiguity before validation
'Measurement' = constraint checking that resolves ambiguity  
'Entanglement' = strong statistical correlation
"""
```

### 4. Testable Metrics

The framework provides rigorous, testable metrics:

1. **PMI (Pointwise Mutual Information)**: Measures symbol association
2. **Mutual Information**: Quantifies information sharing
3. **Lift Ratio**: Measures co-occurrence relative to expectation
4. **Permutation Tests**: Tests significance against null hypothesis
5. **Positional Dependency**: Analyzes preferred distances
6. **Site Variance**: Tests cross-site stability (homogeneity)

## Framework Components

### Statistical Metrics (`src/statistical_metrics.py`)

Pure statistical measures without any quantum claims:
- PMI calculation
- Mutual information
- Lift ratios
- Permutation tests for significance
- Positional dependency analysis
- Site-based variance analysis

### Indus Analysis (`src/indus_analysis.py`)

Core analysis tools:
- Frequency ranking
- Top PMI pairs identification
- Preferred distance histograms
- Site stability testing
- Cluster detection (community detection on PMI graph)
- Compression metrics (information-theoretic)

### Institutional Framework (`src/institutional_framework.py`)

Mixture model for regime classification:

```
P(sequence) = π_A * P_A(sequence) + π_B * P_B(sequence)
```

Where:
- **Regime A**: Administrative (high repetition, stable closers, less variation)
- **Regime B**: Ritual/symbolic (pictograms, animals, symbolic composition)

### Grammar Framework (`src/grammar_framework.py`)

Discrete state grammar (finite automaton):
- State transitions (existential → instanced → delimited → authorized → closed)
- Validation checking
- Constrained configuration analysis

**Important**: Uses quantum terminology ONLY as analogy for constraint satisfaction.

## Academic Usage

### Publishable Statement Template

```
We hypothesize that the Indus sign system encodes validated institutional 
states through a restricted compositional grammar. This is supported by:

(i) Long-range cross-site invariance of motif and sign clusters
(ii) Strong co-occurrence constraints with position-dependent dependencies

We frame 'non-locality' and 'entanglement' strictly as statistical analogies 
for distributed standardization and constrained correlation structure, not as 
claims of physical quantum effects in artifacts.
```

### Recommended Terminology

| Instead of | Use |
|------------|-----|
| Quantum entanglement | Non-local invariance, distributed standardization |
| Quantum superposition | Classification ambiguity, constraint satisfaction |
| Quantum measurement | Validation, closure operation |
| Holographic principle | Information compression, semantic density |
| Akashic fields | Cultural standardization patterns (in interpretive appendix only) |

## Research Workflow

1. **Load data**: Import sequences with site metadata
2. **Compute metrics**: Frequency, PMI, lift ratios
3. **Identify patterns**: Top pairs, clusters, preferred distances
4. **Test stability**: Cross-site variance analysis
5. **Classify regimes**: Administrative vs ritual
6. **Validate grammar**: State transition analysis

Example workflow:

```python
# 1. Initialize
analyzer = IndusSequenceAnalyzer(sequences, site_labels)

# 2. Basic statistics
freq = analyzer.frequency_ranking()
compression = analyzer.compression_metrics()

# 3. Find stable clusters
top_pairs = analyzer.top_pmi_pairs(50)
clusters = analyzer.detect_clusters(min_pmi=1.0)

# 4. Test cross-site stability
for pair in top_pairs[:10]:
    stability = analyzer.site_stability(pair[0])
    print(f"Pair {pair[0]}: {stability}")

# 5. Classify sequences
from src.institutional_framework import InstitutionalRegimeClassifier
classifier = InstitutionalRegimeClassifier(
    pictogram_symbols={'unicorn', 'fish', 'jar'},
    closer_symbols={'X', 'Y', 'Z'}
)
regimes = classifier.batch_classify(sequences)
```

## Interpretive Appendix (Philosophy/Anthropology)

Philosophical and anthropological frameworks should be kept in **separate interpretive sections**, clearly marked as non-empirical:

### Cross-Cultural Analogies

These frameworks offer **interpretive lenses**, not evidence:

- **Platonic Forms**: Universal patterns as idealized templates
- **Akashic Records**: Distributed cultural memory metaphor
- **Dreamtime**: Aboriginal concept of non-linear cultural transmission
- **Li (理)**: Chinese concept of inherent pattern/principle
- **Jungian Archetypes**: Universal symbolic patterns

**Usage**: Present as "epistemological analogies" or "interpretive metaphors"

**Never claim**: "This proves [concept]"

**Instead say**: 
- "This resonates with..."
- "Offers a useful metaphor..."
- "Suggests a vocabulary for discussing..."

### Controversial Sources

- **Rupert Sheldrake**: Cite as "marginal/non-consensual hypothesis, used as metaphor only"
- **Carl Jung**: Acceptable as psychological framework, not as physical mechanism

## Examples

See `examples/` directory for complete examples:
- `basic_analysis.py`: Basic frequency and PMI analysis
- `site_comparison.py`: Cross-site stability testing
- `regime_classification.py`: Administrative vs ritual classification
- `grammar_validation.py`: State grammar validation

## Testing

```bash
python -m pytest tests/
```

## Contributing

Please maintain the separation between:
1. Empirical statistical analysis (main modules)
2. Formal grammar models (as mathematical abstraction)
3. Interpretive frameworks (clearly marked appendices)

## License

See LICENSE file.

## Citation

If using this framework, please cite appropriately and maintain the distinction between statistical analysis and interpretive frameworks.

## Contact

For questions about rigorous application of these methods to Indus script data, please open an issue.
## Usage

```bash
# Run comparative analysis
python src/analysis/compare_distributions.py

# Generate Zipf plots
python src/visualization/plot_zipf.py

# Calculate entropy and compression metrics
python src/models/entropy_model.py
```

## Citation

```
The same statistical signature observed in the Indus corpus—highly skewed 
frequency distribution with a small set of dominant operators—reappears in 
modern algorithmic systems such as social media platforms. This suggests that 
the Indus Script was optimized not for narrative expression, but for efficient 
state activation and institutional validation, a principle that remains 
cognitively and algorithmically stable across millennia.
```

## License

See LICENSE file.
A rigorous, scientifically sound framework for analyzing the Indus Valley script using formal methods, statistical analysis, and computational tools.

## ⚠️ CRITICAL DISCLAIMER

**All references to "non-locality", "entanglement", "quantum", and related terminology in this framework refer STRICTLY to:**

- **Statistical correlations** (NOT quantum entanglement)
- **Distributed standardization** (NOT quantum non-locality)  
- **Long-range dependencies** (classical information theory)
- **Discrete state systems** (formal grammars)

**This is NOT a claim of quantum mechanical processes in archaeological artifacts.**

## What This Framework Provides

1. **Formal Definitions** in Lean 4, Coq, Isabelle/HOL, and Agda
2. **Statistical Analysis Tools** in Python
3. **High-Performance Implementation** in C++
4. **Interactive Calculator** for exploratory analysis
5. **Complete Scientific Methodology** documentation

## Quick Start

### Python Installation

```bash
cd python
pip install -r requirements.txt
pip install -e .
```

### Usage Example

```python
from indus_analysis import Symbol, Sequence, IndusStatisticalAnalysis

# Create symbols
s1 = Symbol(1, 'numeric', 'symbol_1')
s2 = Symbol(2, 'pictographic', 'unicorn')

# Create sequences from different archaeological sites
sequences = [
    Sequence([s1, s2], 'Harappa', 'seal'),
    Sequence([s1, s2], 'Mohenjo-daro', 'seal'),
]

# Analyze statistical correlations (NOT quantum entanglement!)
analyzer = IndusStatisticalAnalysis(sequences)

# Compute PMI (Pointwise Mutual Information)
pmi = analyzer.pmi(s1, s2)
print(f"PMI: {pmi:.4f}")

# Find stable clusters (distributed standardization)
clusters = analyzer.find_stable_clusters(min_pmi=1.0, max_variance=0.5)
```

### C++ Build

```bash
cd cpp
make
./example
```

### Interactive Calculator

```bash
python calculator/indus_calculator.py
```

### Run Tests

```bash
cd tests/python
pytest -v
```

## Key Features

### Scientifically Rigorous Metrics

- **PMI (Pointwise Mutual Information)** - Statistical association strength
- **Mutual Information** - Total correlation measure
- **Lift/Odds Ratio** - Over/under-representation detection
- **Permutation Tests** - Statistical significance
- **Positional Dependency** - Grammatical constraints
- **Cross-Site Variance** - Distributed standardization measure

### Formal Verification

Mathematical proofs in multiple proof assistants ensure correctness:

- **Lean 4**: Discrete state grammar with type safety
- **Coq**: Statistical measures with symmetry proofs
- **Isabelle/HOL**: Non-local invariance properties
- **Agda**: Dependent type constraints

## Documentation

- **[Full Documentation](docs/README.md)** - Complete user guide
- **[Scientific Methodology](docs/METHODOLOGY.md)** - Detailed methodology avoiding pseudoscience
- **[Research Links](docs/RESEARCH_LINKS.md)** - Related studies and resources
- **[Formal Definitions](formal/)** - Proof assistant implementations

## Project Structure

```
indus-operational-mathematics/
├── formal/               # Formal proofs
│   ├── lean/            # Lean 4 definitions
│   ├── coq/             # Coq proofs
│   ├── isabelle/        # Isabelle/HOL theories
│   └── agda/            # Agda formalizations
├── python/              # Python implementation
│   └── indus_analysis/  # Main package
├── cpp/                 # C++ implementation
│   └── src/             # Source files
├── calculator/          # Interactive calculator
├── tests/               # Unit tests
├── docs/                # Documentation
└── README.md           # This file
```

## Scientific Integrity

This framework maintains scientific rigor by:

✅ Clear separation of evidence from interpretation  
✅ Explicit disclaimers on quantum terminology  
✅ Testable hypotheses with empirical metrics  
✅ Reproducible computational methods  
✅ Formal mathematical proofs  
✅ Peer-reviewable methodology  

## Contributing

Contributions welcome! Please:

1. Maintain clear disclaimers on quantum terminology
2. Add formal proofs for new theoretical claims
3. Include unit tests for new implementations
4. Document all statistical assumptions

## License

See [LICENSE](LICENSE) file.

## Citation

```bibtex
@software{indus_operational_math_2026,
  title = {Indus Operational Mathematics: A Formal Framework for Script Analysis},
  year = {2026},
  note = {All "quantum" terminology refers to mathematical analogies, not physical quantum processes},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics}
}
```

## References

This framework is based on the theory that all writing systems are realizations of a universal cognitive grammar:

- The Harappan system is a realization
- The Chinese system is a realization
- The Mayan system is a realization
- The Runic systems are a realization

All are variations on deeply human themes of symbolic representation.
### Formal Methods
- Lean: https://lean-lang.org/
- Coq: https://coq.inria.fr/
- Isabelle: https://isabelle.in.tum.de/
- Agda: https://wiki.portal.chalmers.se/agda/

### Statistical Theory
- Information Theory: Cover & Thomas (2006)
- Association Measures: Church & Hanks (1990)

### Indus Valley Scholarship
- Mahadevan (1977) - Script corpus
- Farmer et al. (2004) - Statistical patterns
- Rao et al. (2009) - Conditional entropy

---

**Remember**: This provides rigorous statistical tools for archaeological analysis. The "quantum" terminology is purely metaphorical. No artifacts exhibit quantum mechanical behavior.
