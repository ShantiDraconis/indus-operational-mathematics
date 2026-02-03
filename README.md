# Indus Operational Mathematics

**A Formal Framework for State-Based Symbol Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License%20(text)-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License%20(code)-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

---

## What This Is

This repository presents a **formal mathematical framework** for analyzing the Indus Valley (Harappan) script through the lens of **operational mathematics** and **state-based computation**. 

### Core Insight

Rather than treating ancient symbols as fixed phonetic or semantic units, we model them as **state operators** that transform computational contexts through formal compositional rules. The framework draws deep structural parallels with ancient Chinese character transformations, particularly the radical 人 (rén, "person") and its systematic modifications.

### Key Components

1. **Formal Axiomatic System**: Five axioms (A1-A5) governing symbol composition and state transformation
2. **Comparative Analysis**: Structural comparison with ancient Chinese operational semantics
3. **Formal Verification**: Implementations in Lean 4, Coq, Isabelle/HOL, and Agda
4. **Computational Models**: Python and C++ implementations for analysis
5. **Comprehensive Monograph**: LaTeX book documenting the complete theoretical foundation

---

## What This Is NOT

### Non-Claims (Critical)

This work **explicitly does NOT**:

❌ Claim to decipher the Indus script phonetically  
❌ Provide linguistic translations of Indus texts  
❌ Establish historical meanings of specific symbols  
❌ Propose phonetic values for any Harappan signs  
❌ Claim to "solve" or "crack" the Indus script  

### What We DO Claim

✅ A rigorous mathematical framework for analyzing symbol operations  
✅ Identification of structural patterns in compositional rules  
✅ Formal comparison with verified operational patterns in ancient Chinese  
✅ Computational models that are formally verified and reproducible  
✅ A foundation for future research using formal methods  

**Epistemological Stance**: We study the **mathematics of symbol composition**, not historical linguistics. Our claims are about **operational structure**, not **semantic content**.

---

## Repository Structure

```
indus-operational-mathematics/
├── public/              # Public-facing content (safe dissemination)
│   ├── one_pager.md     # Quick overview
│   ├── faq.md           # Frequently asked questions
│   └── glossary_public.md
├── docs/                # GitHub Pages site
├── book/                # LaTeX monograph
│   ├── main.tex
│   ├── chapters/        # 11 chapters + appendices
│   └── bibliography.bib
├── model/               # Formal specifications
│   ├── axioms/          # A1-A5 axiom definitions
│   ├── grammar/         # Compositional rules (BNF)
│   ├── automata/        # State machine definitions
│   └── theorem/         # TCOP theorem & proofs
├── formal/              # Formal verification
│   ├── lean/            # Lean 4 implementation
│   ├── coq/             # Coq implementation
│   ├── isabelle/        # Isabelle/HOL implementation
│   └── agda/            # Agda implementation
├── data/                # Research data
│   ├── derived/         # Processed datasets (CSV/JSON)
│   └── provenance/      # Source attribution
├── code/                # Computational implementations
│   ├── python/          # Python analysis tools
│   ├── cpp/             # C++ implementations
│   └── scripts/         # Reproducibility scripts
└── releases/            # Release management for Zenodo
```

---

## Quick Start

### For Readers (Public Content)

Start with the public-facing materials:

```bash
cd public/
cat one_pager.md
cat faq.md
```

Or visit our **GitHub Pages site**: [https://shantidraconis.github.io/indus-operational-mathematics](https://shantidraconis.github.io/indus-operational-mathematics)

### For Researchers (Full Access)

1. **Read the Book**:
   ```bash
   cd book/
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   
2. **Explore the Formal Model**:
   ```bash
   cd model/
   cat axioms/A1_class_primacy.md
   cat theorem/tcop_statement.md
   ```

3. **Run the Code**:
   ```bash
   cd code/
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python scripts/build_bigrams.py
   ```

### For Formal Methods Practitioners

Verify the proofs in your preferred system:

**Lean 4**:
```bash
cd formal/lean/
lake build
```

**Coq**:
```bash
cd formal/coq/
make
```

**Isabelle**:
```bash
cd formal/isabelle/
isabelle build -D .
```

**Agda**:
```bash
cd formal/agda/
agda --safe IndusOperationalMathematics.agda
```

---

## Methodology: The Base-Operator-State Paradigm

### Central Theorem (TCOP - Total Closure of Operations Principle)

**Informal Statement**: In operational symbol systems, every valid symbol sequence represents a well-defined state transformation, and the composition of these transformations is closed under the system's rules.

**Formal Statement** (see `model/theorem/tcop_statement.md`):

```
∀ system S with symbols Σ, operators Ω, and states Θ:
  (1) ∀ σ ∈ Σ ∃ state(σ) ∈ Θ
  (2) ∀ ω ∈ Ω, ∀ θ ∈ Θ: ω(θ) ∈ Θ
  (3) Composition is closed: (ω₁ ∘ ω₂)(θ) ∈ Θ
  (4) Terminal symbols enforce closure: σ_terminal ⊢ ⊥ (no further ops)
```

### The Five Axioms

1. **A1 (Class Primacy)**: Symbols belong to disjoint semantic classes
2. **A2 (No New Classes)**: Operations preserve class membership
3. **A3 (Restricted Composition)**: Only compatible classes can compose
4. **A4 (Terminal Closure)**: Certain symbols enforce sequence termination
5. **A5 (Hierarchical Superposition)**: Modifiers apply in well-defined layers

See `model/axioms/` for complete formalization.

---

## Comparative Analysis: Harappan vs. Ancient Chinese

### Case Study: "Person" as State Operator

#### Ancient Chinese: 人 (rén)

| Transformation | Result | State Change |
|----------------|--------|--------------|
| 人 (base) | person | Generic entity |
| 人 + 一 → 大 | big | Amplification |
| 人 + 人 → 从 | follow | Binary relation |
| 人 × 3 → 众 | crowd | Collective |
| 人 + □ → 囚 | prisoner | Containment |
| 人 inverted → 入 | enter | Transition |

#### Harappan: Symbol 26 (Hypothesized)

| Transformation | Hypothesized Result | State Change |
|----------------|---------------------|--------------|
| 26 (base) | entity | Generic |
| 26 + dot → 27 | instantiated | Activation |
| 26 + stroke → 28 | qualified | Attribution |
| 26 + bracket → 29 | delimited | Contextualization |
| 26 + crown → 30 | authorized | Elevation |

**Structural Parallel**: Both systems use **graphical modification** as **state transformation**, not phonetic decoration.

---

## Data & Reproducibility

### Data Provenance

All data sources are documented in `/data/provenance/sources.yml` with:
- Source references (papers, catalogs)
- Page numbers and extraction dates
- License information
- Checksums (where applicable)

### Reproducibility Pipeline

Our CI/CD ensures full reproducibility:

```bash
# Run the complete pipeline
cd code/
./scripts/extract_tables.py    # data/raw → data/derived
./scripts/build_bigrams.py      # Generate frequency tables
./scripts/export_figures.py     # book/figures/
```

All figures and tables in the book are **generated from data**, not manually created.

---

## Building the Book

### Prerequisites

- TeX Live (or MiKTeX) with `pdflatex` and `bibtex`
- Required LaTeX packages: `amsmath`, `amsthm`, `graphicx`, `tikz`, `listings`

### Compilation

```bash
cd book/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex  # For cross-references
```

Or use the CI pipeline (see `.github/workflows/build-book.yml`).

### Chapters

1. Introduction & Motivation
2. Methodology & Non-Claims
3. Inventory & Symbol Families (1-44)
4. Operators & Composition Rules
5. Frequency, Position & Bigram Analysis
6. Automata & State-Time Dynamics
7. Mathematical Scope & Limitations
8. Comparative Systems (Ancient Chinese)
9. Modern Equivalents (JSON, Relational Logic)
10. The TCOP Theorem
11. Conclusion & Future Work

---

## Formal Verification

### Why Multiple Proof Assistants?

Different systems offer complementary strengths:

- **Lean 4**: Modern, powerful tactics, good for computation
- **Coq**: Mature ecosystem, extensive libraries
- **Isabelle/HOL**: Strong automation (Sledgehammer)
- **Agda**: Dependent types, constructive mathematics

### Verification Status

| Component | Lean | Coq | Isabelle | Agda |
|-----------|------|-----|----------|------|
| Axioms A1-A5 | ✅ | ✅ | ✅ | ✅ |
| TCOP Theorem | ✅ | ✅ | ✅ | ✅ |
| Corollaries | ✅ | ✅ | ✅ | ✅ |
| Automata Model | ✅ | ✅ | ✅ | ⚠️ (partial) |

### Running Verification

Each proof assistant directory contains:
- `README.md`: Setup instructions
- `Makefile` or build configuration
- Complete formalization of axioms and theorems

---

## Citation

If you use this work, please cite:

```bibtex
@software{draconis2026indus,
  author = {Draconis, Shanti},
  title = {Indus Operational Mathematics: A Formal Framework for State-Based Symbol Systems},
  year = {2026},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics},
  doi = {10.5281/zenodo.XXXXXXX},
  version = {1.0.0}
}
```

Or use the `CITATION.cff` file for automated tools.

---

## Contributing

We welcome contributions! Please see:

- [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards
- [SECURITY.md](SECURITY.md) for security policies

**Key principle**: All claims must be backed by formal mathematics and reproducible analysis.

---

## License

This project uses **dual licensing**:

- **Text/Documentation**: [CC BY 4.0](LICENSE_TEXT.md) - book, papers, docs
- **Code/Software**: [MIT License](LICENSE_CODE.md) - implementations, scripts

---

## Contact & Community

- **GitHub Discussions**: For questions and conceptual discussions
- **Issues**: For bug reports and specific problems
- **Pull Requests**: For contributions

---

## Acknowledgments

This work builds on decades of Indus Valley research by archaeologists, linguists, and computational scholars. While our approach is novel, we stand on the shoulders of giants.

**Special thanks to**:
- The Indus research community for maintaining open data
- The formal methods community for proof assistant development
- Comparative paleography scholars for cross-cultural insights

---

## Roadmap

### Version 1.0 (Current)
- ✅ Core axioms formalized
- ✅ TCOP theorem proven in 4 proof assistants
- ✅ Comparative analysis with ancient Chinese
- ✅ Book chapters 1-11 complete

### Version 1.1 (Planned)
- [ ] Extended symbol catalog (45-200)
- [ ] Additional comparative systems (Sumerian, Egyptian)
- [ ] Machine learning integration for pattern discovery
- [ ] Interactive web demonstrations

### Version 2.0 (Future)
- [ ] Full corpus analysis
- [ ] Cross-site statistical validation
- [ ] Collaboration with archaeological teams
- [ ] Museum partnerships for high-resolution imaging

---

## Frequently Asked Questions

See [public/faq.md](public/faq.md) for detailed answers, including:

- **Is this a decipherment?** No, it's a formal mathematical framework.
- **Can I read Indus texts now?** No, we make no phonetic claims.
- **What's the significance?** We provide tools for rigorous structural analysis.
- **How does this compare to X's work?** See comparative analysis in the book.

---

**Last updated**: 2026-02-03  
**Version**: 1.0.0  
**Status**: Initial Release

---

*"In ancient symbol systems, the symbol is not the name of the thing, but the operator on the state."*
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
