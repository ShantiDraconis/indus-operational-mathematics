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
