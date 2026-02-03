# Indus Operational Mathematics

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