# API Reference

## Module: `statistical_metrics`

Pure statistical functions for analyzing symbol sequences.

### Functions

#### `pointwise_mutual_information(pair_count, total_count, symbol_a_count, symbol_b_count) -> float`

Calculate PMI for a symbol pair.

**Parameters:**
- `pair_count` (int): Number of times symbols a and b co-occur
- `total_count` (int): Total number of observations
- `symbol_a_count` (int): Total count of symbol a
- `symbol_b_count` (int): Total count of symbol b

**Returns:** 
- `float`: PMI value (positive = attraction, negative = repulsion, 0 = independence)

**Formula:** `PMI(a,b) = log2(P(a,b) / (P(a) * P(b)))`

---

#### `mutual_information(sequences) -> Dict[Tuple[str, str], float]`

Calculate Mutual Information for all symbol pairs.

**Parameters:**
- `sequences` (List[List[str]]): List of symbol sequences

**Returns:**
- `Dict[Tuple[str, str], float]`: Dictionary mapping symbol pairs to MI values

---

#### `lift_ratio(pair_count, total_count, symbol_a_count, symbol_b_count) -> float`

Calculate lift (odds ratio) for a symbol pair.

**Parameters:**
- Same as `pointwise_mutual_information`

**Returns:**
- `float`: Lift ratio (>1 = positive association, <1 = negative, =1 = independence)

---

#### `permutation_test(sequences, pair, n_permutations=1000, random_seed=None) -> Tuple[float, float]`

Test significance of pair co-occurrence against null hypothesis.

**Parameters:**
- `sequences` (List[List[str]]): List of symbol sequences
- `pair` (Tuple[str, str]): Symbol pair to test
- `n_permutations` (int): Number of random permutations (default: 1000)
- `random_seed` (Optional[int]): Random seed for reproducibility

**Returns:**
- `Tuple[float, float]`: (observed_count, p_value)

---

#### `positional_dependency(sequences, symbol_a, symbol_b, max_distance=10) -> Dict[int, int]`

Analyze positional dependency between two symbols.

**Parameters:**
- `sequences` (List[List[str]]): List of symbol sequences
- `symbol_a` (str): First symbol
- `symbol_b` (str): Second symbol  
- `max_distance` (int): Maximum distance to consider (default: 10)

**Returns:**
- `Dict[int, int]`: Dictionary mapping distance to occurrence count

---

#### `site_variance_analysis(sequences_by_site, pair) -> Dict[str, Dict[str, float]]`

Analyze variance of pair co-occurrence across sites.

**Parameters:**
- `sequences_by_site` (Dict[str, List[List[str]]]): Sequences grouped by site
- `pair` (Tuple[str, str]): Symbol pair to analyze

**Returns:**
- `Dict[str, Dict[str, float]]`: PMI and counts for each site

---

#### `homogeneity_test(site_results, metric='pmi') -> Tuple[float, float]`

Test homogeneity of a metric across sites.

**Parameters:**
- `site_results` (Dict[str, Dict[str, float]]): Results from site_variance_analysis
- `metric` (str): Which metric to test (default: 'pmi')

**Returns:**
- `Tuple[float, float]`: (mean, coefficient_of_variation)

---

## Module: `indus_analysis`

Core analysis tools for Indus script sequences.

### Class: `IndusSequenceAnalyzer`

Main analyzer for Indus script sequences.

#### `__init__(sequences, site_labels=None)`

Initialize analyzer.

**Parameters:**
- `sequences` (List[List[str]]): List of symbol sequences
- `site_labels` (Optional[List[str]]): Optional site labels for each sequence

---

#### `frequency_ranking(top_n=None) -> List[Tuple[str, int, float]]`

Get frequency ranking of symbols.

**Parameters:**
- `top_n` (Optional[int]): Return only top N symbols (None for all)

**Returns:**
- `List[Tuple[str, int, float]]`: List of (symbol, count, frequency) tuples

---

#### `top_pmi_pairs(top_n=50) -> List[Tuple[Tuple[str, str], float]]`

Get top N symbol pairs by PMI (stable clusters).

**Parameters:**
- `top_n` (int): Number of top pairs to return (default: 50)

**Returns:**
- `List[Tuple[Tuple[str, str], float]]`: List of ((symbol_a, symbol_b), pmi) tuples

---

#### `preferred_distances(symbol_a, symbol_b, max_distance=10) -> Dict[int, int]`

Get histogram of preferred distances between two symbols.

**Parameters:**
- `symbol_a` (str): First symbol
- `symbol_b` (str): Second symbol
- `max_distance` (int): Maximum distance to consider (default: 10)

**Returns:**
- `Dict[int, int]`: Dictionary mapping distance to count

---

#### `site_stability(pair) -> Dict[str, float]`

Measure stability of pair association across sites.

**Parameters:**
- `pair` (Tuple[str, str]): Symbol pair to analyze

**Returns:**
- `Dict[str, float]`: Dictionary mapping site to PMI value

---

#### `detect_clusters(min_pmi=1.0, min_support=5) -> List[Set[str]]`

Detect symbol clusters using PMI-based community detection.

**Parameters:**
- `min_pmi` (float): Minimum PMI to consider symbols related (default: 1.0)
- `min_support` (int): Minimum co-occurrence count (default: 5)

**Returns:**
- `List[Set[str]]`: List of symbol sets (clusters)

---

#### `compression_metrics() -> Dict[str, float]`

Calculate information-theoretic compression metrics.

**Returns:**
- `Dict[str, float]`: Dictionary with entropy, redundancy, and compressibility metrics

**Keys:**
- `entropy`: Shannon entropy in bits/symbol
- `max_entropy`: Maximum possible entropy
- `redundancy`: Fraction of max entropy not used
- `avg_sequence_length`: Average sequence length
- `bits_per_symbol`: Information content per symbol
- `compression_ratio`: Ratio of max to actual entropy

---

### Function: `identify_closers(sequences, position='end', min_frequency=0.1) -> List[Tuple[str, float]]`

Identify common closer symbols.

**Parameters:**
- `sequences` (List[List[str]]): List of sequences
- `position` (str): 'start' or 'end' (default: 'end')
- `min_frequency` (float): Minimum frequency threshold (default: 0.1)

**Returns:**
- `List[Tuple[str, float]]`: List of (symbol, frequency) tuples

---

## Module: `institutional_framework`

Models for institutional regime classification.

### Class: `InstitutionalRegimeClassifier`

Classifier for administrative vs ritual regimes.

#### `__init__(pictogram_symbols=None, closer_symbols=None)`

Initialize classifier.

**Parameters:**
- `pictogram_symbols` (Optional[set]): Set of pictographic symbols
- `closer_symbols` (Optional[set]): Set of closer symbols

---

#### `classify(sequence, object_type=None) -> Tuple[str, float]`

Classify a sequence.

**Parameters:**
- `sequence` (List[str]): Symbol sequence
- `object_type` (Optional[str]): Optional object type

**Returns:**
- `Tuple[str, float]`: (regime, confidence) where regime is 'administrative' or 'ritual'

---

#### `batch_classify(sequences, object_types=None) -> List[Tuple[str, float]]`

Classify multiple sequences.

**Parameters:**
- `sequences` (List[List[str]]): List of sequences
- `object_types` (Optional[List[str]]): Optional list of object types

**Returns:**
- `List[Tuple[str, float]]`: List of (regime, confidence) tuples

---

#### `regime_statistics(sequences, object_types=None) -> Dict[str, Dict[str, float]]`

Calculate statistics for each regime.

**Parameters:**
- `sequences` (List[List[str]]): List of sequences
- `object_types` (Optional[List[str]]): Optional list of object types

**Returns:**
- `Dict[str, Dict[str, float]]`: Statistics for each regime

---

## Module: `grammar_framework`

Discrete state grammar models (NOT quantum mechanics).

### Enum: `SymbolState`

Discrete states in institutional validation.

**Values:**
- `EXISTENTIAL`: Symbol exists
- `INSTANCED`: Symbol instantiated in context
- `DELIMITED`: Symbol within boundaries
- `AUTHORIZED`: Symbol validated by authority
- `CLOSED`: Sequence finalized/sealed

---

### Class: `DiscreteStateGrammar`

Finite automaton model for sequences.

#### `__init__()`

Initialize grammar with default transitions.

---

#### `add_transition(from_state, to_state, operator, condition=None)`

Add a state transition.

**Parameters:**
- `from_state` (SymbolState): Source state
- `to_state` (SymbolState): Target state
- `operator` (str): Symbol or operation that triggers transition
- `condition` (Optional[str]): Additional constraint

---

#### `is_valid_sequence(sequence, symbol_to_operator=None) -> Tuple[bool, List[SymbolState]]`

Check if a sequence follows valid state transitions.

**Parameters:**
- `sequence` (List[str]): Symbol sequence
- `symbol_to_operator` (Optional[Dict[str, str]]): Mapping from symbols to operators

**Returns:**
- `Tuple[bool, List[SymbolState]]`: (is_valid, state_path)

---

#### `constrained_configurations(sequences, symbol_to_operator=None) -> Dict[str, int]`

Identify sequences following constrained configurations.

**Parameters:**
- `sequences` (List[List[str]]): List of sequences
- `symbol_to_operator` (Optional[Dict[str, str]]): Symbol to operator mapping

**Returns:**
- `Dict[str, int]`: Statistics on valid vs invalid sequences

---

### Class: `ConstraintSatisfactionAnalogy`

Explains quantum terminology as constraint satisfaction analogy.

**IMPORTANT**: These are analogies only, NOT claims of physical quantum processes.

#### Static Methods:

- `explain_superposition_analogy() -> str`: Explains "superposition" as classification ambiguity
- `explain_measurement_analogy() -> str`: Explains "measurement" as validation
- `explain_entanglement_analogy() -> str`: Explains "entanglement" as correlation

---

## Usage Examples

### Basic Analysis

```python
from src.indus_analysis import IndusSequenceAnalyzer

sequences = [
    ['A', 'B', 'C', 'X'],
    ['A', 'B', 'D', 'X'],
]

analyzer = IndusSequenceAnalyzer(sequences)
frequencies = analyzer.frequency_ranking()
pairs = analyzer.top_pmi_pairs(50)
clusters = analyzer.detect_clusters()
```

### Site Comparison

```python
sequences = [...]
site_labels = ['Site1', 'Site1', 'Site2', 'Site2']

analyzer = IndusSequenceAnalyzer(sequences, site_labels)
stability = analyzer.site_stability(('A', 'B'))
```

### Regime Classification

```python
from src.institutional_framework import InstitutionalRegimeClassifier

classifier = InstitutionalRegimeClassifier(
    pictogram_symbols={'unicorn', 'bull'},
    closer_symbols={'X', 'Y'}
)

regime, confidence = classifier.classify(['A', 'B', 'X'])
```

### Grammar Validation

```python
from src.grammar_framework import DiscreteStateGrammar

grammar = DiscreteStateGrammar()
is_valid, path = grammar.is_valid_sequence(['A', 'B', 'C'])
```
