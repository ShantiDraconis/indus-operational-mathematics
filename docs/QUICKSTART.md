# Quick Start Guide

Get up and running with the Indus Operational Mathematics Framework in 5 minutes.

## ⚠️ First: Read the Disclaimer

**CRITICAL**: All "quantum" and "non-locality" terminology in this framework refers to:
- **Statistical correlations** (NOT quantum entanglement)
- **Distributed patterns** (NOT quantum non-locality)
- **Discrete state systems** (NOT quantum mechanics)

This is classical statistics and formal methods applied to archaeology.

## Installation

### Python (Recommended for beginners)

```bash
# Clone repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Install Python package
cd python
pip install -r requirements.txt
pip install -e .
```

### C++ (For performance)

```bash
cd cpp
make
./example
```

## Quick Examples

### 1. Run the Demo (2 minutes)

```bash
python demo.py
```

This shows all features with sample data.

### 2. Interactive Calculator (5 minutes)

```bash
python calculator/indus_calculator.py
```

Follow the menu to:
- Compute PMI (statistical correlation)
- Find stable clusters
- Analyze cross-site patterns
- Classify sequences

### 3. Python Code (10 minutes)

```python
from indus_analysis import Symbol, Sequence, IndusStatisticalAnalysis

# Step 1: Create symbols
s1 = Symbol(1, 'numeric', 'symbol_1')
s2 = Symbol(2, 'pictographic', 'unicorn')
s3 = Symbol(3, 'abstract', 'symbol_3')

# Step 2: Create sequences (from different sites)
sequences = [
    Sequence([s1, s2, s3], 'Harappa', 'seal'),
    Sequence([s1, s2], 'Mohenjo-daro', 'seal'),
    Sequence([s2, s3, s1], 'Dholavira', 'tablet'),
]

# Step 3: Analyze
analyzer = IndusStatisticalAnalysis(sequences)

# Compute statistical measures
pmi = analyzer.pmi(s1, s2)
print(f"PMI (statistical correlation): {pmi:.4f}")

lift = analyzer.lift(s1, s2)
print(f"Lift (odds ratio): {lift:.4f}")

# Check cross-site stability
variance = analyzer.cross_site_variance(s1, s2)
print(f"Cross-site variance: {variance:.4f}")
if variance < 0.5:
    print("→ Pattern is stable across sites (non-local invariant)")
    print("   (This means distributed standardization, NOT quantum!)")

# Find all stable clusters
clusters = analyzer.find_stable_clusters(min_pmi=1.0, max_variance=0.5)
print(f"\nFound {len(clusters)} stable clusters")
```

### 4. C++ Code (for performance)

```cpp
#include "indus_stats.hpp"
using namespace indus;

// Create symbols
Symbol s1{1, "numeric", "symbol_1"};
Symbol s2{2, "pictographic", "unicorn"};

// Create sequences
std::vector<Sequence> sequences = {
    {{s1, s2}, "Harappa", "seal"},
    {{s1, s2}, "Mohenjo-daro", "seal"}
};

// Analyze
StatisticalAnalyzer analyzer(sequences);

double pmi = analyzer.pmi(s1, s2);
double lift = analyzer.lift(s1, s2);
double variance = analyzer.cross_site_variance(s1, s2);

std::cout << "PMI: " << pmi << "\n";
std::cout << "Lift: " << lift << "\n";
std::cout << "Variance: " << variance << "\n";
```

## Understanding the Output

### PMI (Pointwise Mutual Information)
- **Positive** = symbols co-occur more than expected
- **Negative** = symbols avoid each other
- **Zero** = independent
- **> 1.0** = strong association

### Lift (Odds Ratio)
- **> 1** = over-represented together
- **< 1** = under-represented together
- **= 1** = independent

### Cross-Site Variance
- **Low (< 0.5)** = stable pattern across sites
- **High (> 0.5)** = site-specific pattern
- **Low variance** = "non-local invariant" (distributed standardization)

### What "Non-Local Invariant" Means
- ✅ Pattern appears across multiple sites
- ✅ Statistically stable distribution
- ✅ Evidence of shared cultural practice
- ❌ NOT quantum non-locality
- ❌ NOT spooky action at a distance

## Common Use Cases

### 1. Find Strongly Correlated Pairs

```python
from indus_analysis import compute_top_correlations

results = compute_top_correlations(sequences, top_n=10)
for result in results:
    print(f"Symbols ({result['symbol1']}, {result['symbol2']})")
    print(f"  PMI: {result['pmi']:.2f}")
    print(f"  Stable: {result['is_stable_cluster']}")
```

### 2. Analyze Positional Patterns

```python
dist_hist = analyzer.positional_dependency(sym1, sym2)
for distance, count in dist_hist.items():
    print(f"Distance {distance}: appears {count} times")
```

### 3. Test Statistical Significance

```python
p_value = analyzer.permutation_test(sym1, sym2, n_permutations=1000)
if p_value < 0.05:
    print("Correlation is statistically significant")
```

### 4. Classify Sequences

```python
result = analyzer.institutional_vs_ritual_classification(sequence)
print(f"Administrative: {result['administrative']:.1%}")
print(f"Ritual: {result['ritual']:.1%}")
```

## Running Tests

```bash
cd tests/python
pytest test_statistical_analysis.py -v
pytest test_tensor_models.py -v
```

All tests should pass ✓

## Next Steps

1. **Read the methodology**: `docs/METHODOLOGY.md`
2. **Explore formal proofs**: `formal/` directory
3. **Check research links**: `docs/RESEARCH_LINKS.md`
4. **Adapt to your data**: Replace sample data with real corpus

## Getting Help

### Documentation
- Full docs: `docs/README.md`
- Methodology: `docs/METHODOLOGY.md`
- Implementation: `docs/IMPLEMENTATION_SUMMARY.md`

### Code Examples
- Python demo: `demo.py`
- Calculator: `calculator/indus_calculator.py`
- C++ example: `cpp/src/example.cpp`

### Key Reminders

1. **Always include disclaimers** when presenting results
2. **Use correct terminology**: "statistical correlation", not "quantum entanglement"
3. **Separate evidence from interpretation**
4. **Test significance** before claiming patterns
5. **Be transparent** about methods and assumptions

## Troubleshooting

### Import Error
```bash
# Make sure package is installed
cd python
pip install -e .
```

### C++ Compilation Error
```bash
# Requires C++17
g++ --version  # Should be >= 7.0
```

### Test Failures
```bash
# Install test dependencies
pip install pytest
```

## Summary

You now have a complete, scientifically rigorous framework for analyzing the Indus script:

✓ Formal mathematical foundations  
✓ Statistical analysis tools  
✓ High-performance implementation  
✓ Interactive exploration  
✓ Clear scientific methodology  

**Remember**: This is about **patterns in data**, not quantum mysticism. The framework is powerful precisely because it's scientifically sound.

---

**Ready to analyze?** Run `python demo.py` and explore!
