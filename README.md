# Indus Operational Mathematics

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
