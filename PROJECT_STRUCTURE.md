# Project Structure

```
indus-operational-mathematics/
│
├── README.md                          # Main documentation with usage guide
├── IMPLEMENTATION_SUMMARY.md          # Maps implementation to problem requirements
├── requirements.txt                   # Python dependencies (numpy, scipy)
├── LICENSE                           # Project license
├── .gitignore                        # Excludes __pycache__ and build artifacts
│
├── src/                              # Main codebase - EMPIRICAL/STATISTICAL
│   ├── __init__.py
│   ├── statistical_metrics.py        # Pure statistical functions (PMI, MI, lift, etc.)
│   ├── indus_analysis.py             # Core analysis tools (frequency, clusters, etc.)
│   ├── institutional_framework.py    # Regime classification (admin vs ritual)
│   └── grammar_framework.py          # Discrete state grammar (finite automaton)
│
├── examples/                         # Working examples (all tested)
│   ├── basic_analysis.py             # Frequency, PMI, cluster detection
│   ├── site_comparison.py            # Cross-site stability analysis
│   ├── regime_classification.py      # Administrative vs ritual classification
│   └── grammar_validation.py         # State grammar validation
│
└── docs/                             # Documentation
    ├── api_reference.md              # Complete API documentation
    ├── research_paper_template.md    # Academic paper structure
    └── interpretive_frameworks.md    # SEPARATE: Philosophy/anthropology appendix

```

## Key Design Principles

### 1. Separation of Concerns ("Firewalls")

```
┌─────────────────────────────────────────────────────────────┐
│                    EMPIRICAL LAYER                          │
│  src/statistical_metrics.py + src/indus_analysis.py        │
│  • PMI, MI, lift ratios                                     │
│  • Permutation tests                                        │
│  • Site variance analysis                                   │
│  • Cluster detection                                        │
│  ✓ TESTABLE, REPRODUCIBLE                                  │
└─────────────────────────────────────────────────────────────┘
                           ↕
            Clear boundary maintained
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                    FORMAL MODEL LAYER                       │
│  src/institutional_framework.py + src/grammar_framework.py │
│  • Mixture models                                           │
│  • Finite automata                                          │
│  • Discrete state grammars                                  │
│  ✓ MATHEMATICAL ABSTRACTIONS                               │
└─────────────────────────────────────────────────────────────┘
                           ↕
            Clear boundary maintained
                           ↕
┌─────────────────────────────────────────────────────────────┐
│                  INTERPRETIVE LAYER                         │
│  docs/interpretive_frameworks.md                           │
│  • Platonic Forms (metaphor)                                │
│  • Li, Dreamtime, Jung (analogies)                         │
│  • Akashic, Sheldrake (flagged as controversial)           │
│  ✓ CLEARLY MARKED AS NON-EMPIRICAL                        │
└─────────────────────────────────────────────────────────────┘
```

### 2. Terminology Mapping

**Quantum/Physics Terms → Statistical/Mathematical Terms**

```
┌────────────────────────┬─────────────────────────────────────┐
│ AVOID (or use as       │ USE (rigorous)                      │
│ explicit metaphor)     │                                     │
├────────────────────────┼─────────────────────────────────────┤
│ Quantum entanglement   │ • Non-local invariance              │
│                        │ • Distributed standardization       │
│                        │ • Long-range correlation            │
├────────────────────────┼─────────────────────────────────────┤
│ Quantum superposition  │ • Classification ambiguity          │
│                        │ • Constraint satisfaction           │
│                        │ • Pre-validation uncertainty        │
├────────────────────────┼─────────────────────────────────────┤
│ Quantum measurement    │ • Validation operation              │
│                        │ • Closure/finalization              │
│                        │ • Constraint checking               │
├────────────────────────┼─────────────────────────────────────┤
│ Holographic principle  │ • Information compression           │
│                        │ • Semantic density                  │
│                        │ • High information per symbol       │
├────────────────────────┼─────────────────────────────────────┤
│ Akashic fields         │ • Cultural memory                   │
│                        │ • Institutional knowledge           │
│                        │ (in interpretive appendix only)     │
└────────────────────────┴─────────────────────────────────────┘
```

### 3. Data Flow

```
Input Data (Indus sequences)
        ↓
┌───────────────────────┐
│ IndusSequenceAnalyzer │
└───────────────────────┘
        ↓
┌─────────────────┬──────────────────┬─────────────────────┐
│                 │                  │                     │
│ Frequency       │ Co-occurrence    │ Compression         │
│ Analysis        │ Patterns         │ Metrics             │
│                 │                  │                     │
│ • Ranking       │ • PMI pairs      │ • Entropy           │
│ • Closers       │ • Clusters       │ • Redundancy        │
│                 │ • Distances      │ • Bits/symbol       │
└─────────────────┴──────────────────┴─────────────────────┘
                           ↓
                    ┌─────────────┐
                    │ Site        │
                    │ Stability   │
                    │ Analysis    │
                    └─────────────┘
                           ↓
        ┌──────────────────────────────────┐
        │ Regime Classification            │
        │ (Administrative vs Ritual)       │
        └──────────────────────────────────┘
                           ↓
                ┌──────────────────────┐
                │ Grammar Validation   │
                │ (State Transitions)  │
                └──────────────────────┘
                           ↓
                    Results + Metrics
```

### 4. Example Usage Flow

```python
# Step 1: Load data
sequences = [
    ['jar', 'fish', 'man', 'closer'],
    ['unicorn', 'trough', 'closer'],
    # ...
]
site_labels = ['Harappa', 'Mohenjo-daro', ...]

# Step 2: Analyze
analyzer = IndusSequenceAnalyzer(sequences, site_labels)

# Step 3: Get metrics (EMPIRICAL)
frequencies = analyzer.frequency_ranking()
top_pairs = analyzer.top_pmi_pairs(50)
clusters = analyzer.detect_clusters()
compression = analyzer.compression_metrics()

# Step 4: Test stability (SUPRA-REGIONAL STANDARDIZATION)
for pair, pmi in top_pairs[:10]:
    stability = analyzer.site_stability(pair)
    # Low variance = "non-local invariance"

# Step 5: Classify regimes (FORMAL MODEL)
classifier = InstitutionalRegimeClassifier(...)
regimes = classifier.batch_classify(sequences)

# Step 6: Validate grammar (FORMAL MODEL)
grammar = DiscreteStateGrammar()
validity = grammar.constrained_configurations(sequences)
```

## Documentation Hierarchy

```
1. Quick Start
   └─ README.md (overview, key concepts, examples)

2. Technical Reference
   └─ docs/api_reference.md (function signatures, parameters)

3. Academic Writing
   └─ docs/research_paper_template.md (proper structure)

4. Philosophical Context
   └─ docs/interpretive_frameworks.md (SEPARATE, clearly labeled)

5. Implementation Details
   └─ IMPLEMENTATION_SUMMARY.md (maps to requirements)
```

## Testing & Validation

All examples produce working output:

```bash
# Test statistical analysis
python examples/basic_analysis.py
# → Frequency ranking, PMI pairs, clusters, compression metrics

# Test cross-site stability
python examples/site_comparison.py
# → Site-specific PMI, coefficient of variation, stability

# Test regime classification
python examples/regime_classification.py
# → Administrative vs ritual classification with confidence

# Test grammar validation
python examples/grammar_validation.py
# → State paths, validity checks, explanations of analogies
```

## Key Features

### ✓ Rigorous Statistics
- PMI, MI, lift ratios
- Permutation tests for significance
- Site variance with homogeneity testing
- Information-theoretic compression

### ✓ Formal Models
- Mixture model (administrative vs ritual)
- Discrete state grammar (finite automaton)
- Constrained configuration validation

### ✓ Clear Boundaries
- Physics terminology as explicit metaphor only
- Statistical analysis in main codebase
- Philosophical frameworks in separate appendix
- All disclaimers prominently displayed

### ✓ Academic Integrity
- Proper terminology recommendations
- Template for publishable papers
- Warnings about controversial sources
- Citation guidelines

## Result

A complete, working framework that:
1. Maintains scientific rigor
2. Enables interdisciplinary research
3. Avoids pseudoscience
4. Provides publishable structure
5. Includes working, tested code
