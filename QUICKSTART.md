# Quick Start Guide

## Getting Started with Indus Operational Mathematics

This guide will help you quickly understand and use the Harappan Operational System implementation.

---

## Installation

No installation required! The core implementation uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Verify Python version (3.8+)
python --version
```

---

## 5-Minute Tutorial

### 1. Validate Your First Sequence

```python
# Navigate to the repo root
cd /path/to/indus-operational-mathematics

# Run the automaton
python implementation/parser/indus_automaton.py
```

**Output:**
```
Sequence [373, 342]: VALID
Sequence [373, 410, 342]: VALID
Sequence [373, 410]: INVALID
  Error: Sequence does not end in accepting state
```

### 2. Convert a Sequence to JSON

```python
python implementation/converter/harappan_to_json.py
```

**Output:**
```json
{
  "entity": "basic_token",
  "qualifiers": [],
  "quantity": 3,
  "relations": [],
  "closure": "simple"
}
```

### 3. Use the Validator

```python
python implementation/validator/indus_validator.py
```

See detailed validation results with error messages and state traces.

---

## Understanding the System

### Core Concept

The Indus script is a **finite-state automaton** with 6 states:

```
S0 (Initial) → S1 (Entity) → S2 (Qualified) → S3 (Quantified) 
                                ↓                      ↓
                            S4 (Related) ────────> S5 (Closed) ✓
```

### Valid Sequence Pattern

```
[ENTITY] [QUALIFIERS*] [QUANTITIES*] [RELATIONS*] [CLOSURE]
   ↑                                                   ↑
 Required                                         Required
```

### Example Breakdown

```python
sequence = [373, 410, 411, 400, 342]

# Step by step:
# [373]         → Entity: Basic Token (S0 → S1)
# [410]         → Count: 1 (S1 → S3)
# [411]         → Count: 2 (S3 → S3)  Total: 3
# [400]         → Relation: Pair (S3 → S4)
# [342]         → Closure: Simple (S4 → S5) ✓ Valid!
```

---

## Common Use Cases

### Case 1: Create and Validate a Simple Record

```python
from implementation.parser.indus_automaton import validate_indus_sequence

# Simple administrative record
sequence = [373, 342]  # Entity + Closure
is_valid, error = validate_indus_sequence(sequence)

print(f"Valid: {is_valid}")  # True
```

### Case 2: Create a Quantified Record

```python
# Record with quantity
sequence = [200, 415, 343]  # Unicorn + 10 + Confirmed
is_valid, error = validate_indus_sequence(sequence)

print(f"Valid: {is_valid}")  # True
```

### Case 3: Detailed Validation

```python
from implementation.validator.indus_validator import IndusValidator

validator = IndusValidator()
sequence = [373, 410, 400, 342]

result = validator.validate_with_details(sequence)

print(f"Valid: {result['is_valid']}")
print(f"State: {result['final_state']}")
print(f"Classes: {result['symbol_classes']}")
```

### Case 4: Convert to JSON

```python
from implementation.converter.harappan_to_json import harappan_to_json

sequence = [200, 410, 411, 343]
json_record = harappan_to_json(sequence)

print(json_record)
# {'entity': 'unicorn', 'quantity': 3, 'closure': 'confirmed', ...}
```

---

## Symbol Reference

### Entities (Start of Sequence)

| ID Range | Class | Examples |
|----------|-------|----------|
| 373-399 | Oval | Basic tokens, seals |
| 328-339 | Vessel | Containers |
| 250-260 | Authority | Staffs, scepters |
| 200-210 | Animal | Unicorn, bull, elephant |
| 100-150 | Metric | Measurement units |

### Operators (Middle of Sequence)

| ID Range | Class | Function |
|----------|-------|----------|
| 410-417 | Count | 1, 2, 3, 4, 5, 10, 20, 100 |
| 400-409 | Relation | Pair, hierarchy, exchange, etc. |

### Closures (End of Sequence)

| ID | Type | Meaning |
|----|------|---------|
| 342 | Simple | Basic closure |
| 343 | Confirmed | Validated |
| 344 | Validated | Double-checked |
| 345 | Sealed | Sealed record |
| 346 | Absolute | Highest authority |
| 347 | Hierarchical | Hierarchical validation |
| 348 | Terminal | Final closure |

---

## Testing Your Sequences

### Valid Patterns

```python
# Pattern 1: Entity + Closure
[373, 342]  # ✓ Valid

# Pattern 2: Entity + Count + Closure
[373, 410, 342]  # ✓ Valid

# Pattern 3: Entity + Count + Count + Closure
[373, 410, 411, 342]  # ✓ Valid (quantity = 3)

# Pattern 4: Entity + Relation + Closure
[373, 400, 342]  # ✓ Valid

# Pattern 5: Entity + Count + Relation + Closure
[373, 410, 400, 342]  # ✓ Valid
```

### Invalid Patterns

```python
# No closure
[373, 410]  # ✗ Invalid

# Closure first
[342, 373]  # ✗ Invalid

# No entity
[410, 342]  # ✗ Invalid

# Wrong order
[373, 400, 410, 342]  # ✗ Invalid (relation before count)
```

---

## Visualization

### Generate Diagrams

```python
cd implementation/simulator
python automaton_visualizer.py
```

This generates:
- `automaton.dot` - Graphviz format
- `automaton_diagram.md` - Mermaid diagram
- `transition_table.txt` - Transition matrix

### View ASCII Art

```python
from implementation.simulator.automaton_visualizer import AutomatonVisualizer

viz = AutomatonVisualizer()
print(viz.generate_ascii_art())
```

---

## Data Files

### Signs Catalog
```bash
cat data/signs.csv
```

48 key symbols with IDs, classes, descriptions, and frequencies.

### Bigrams (Co-occurrences)
```bash
cat data/bigrams.csv
```

Symbol pair frequencies showing which symbols commonly appear together.

### Frequencies
```bash
cat data/frequencies.csv
```

Distribution data across different media (seals, tablets, pottery).

---

## Advanced Usage

### Create Custom Sequences Programmatically

```python
from implementation.parser.indus_automaton import IndusAutomaton, SymbolClass

automaton = IndusAutomaton()

# Build sequence step by step
automaton.process_symbol(SymbolClass.ENT_OVAL)
automaton.process_symbol(SymbolClass.OP_COUNT)
automaton.process_symbol(SymbolClass.OP_COUNT)
automaton.process_symbol(SymbolClass.OP_CLOSE)

# Check if valid
if automaton.is_valid_record():
    print("Valid sequence!")
    print(f"Current state: {automaton.get_current_state()}")
```

### Batch Processing

```python
from implementation.converter.harappan_to_json import HarappanToJsonConverter

converter = HarappanToJsonConverter()

sequences = [
    [373, 342],
    [200, 410, 343],
    [328, 415, 346]
]

records = converter.batch_convert(sequences)
for record in records:
    print(record.to_json())
```

---

## Next Steps

1. **Read the Paper**: See `publications/paper/indus_operational_system.md`
2. **Explore Formal Model**: See `formal_model/automata/finite_automaton.md`
3. **Study Comparisons**: See `comparisons/festos/phaistos_comparison.md`
4. **Try Blockchain**: See `implementation/converter/IndusRecord.sol`

---

## Getting Help

- **Documentation**: Read the full README.md
- **Examples**: See `data/example_sequences.md`
- **Issues**: Report problems on GitHub
- **Questions**: Open a discussion on GitHub

---

## Quick Reference Card

```
VALID SEQUENCE STRUCTURE:
[Entity (100-399)] [Operators] [Closure (342-348)]

STATES:
S0 → S1 → S2/S3/S4 → S5
     ENT  OPS       CLOSE

RULES:
1. Must start with entity
2. Must end with closure
3. Operations in order: Qual → Count → Rel
4. Closure is final (no more symbols)

EXAMPLE:
[373, 410, 342] = "1 basic token, simple closure"
```

---

**Happy validating!** 🎉
Welcome to the Quantum Archaeology Framework! This guide will help you get started quickly.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics
pip install -r requirements.txt
```

## Running Examples

### 1. Quantum Symbol Analysis

This example demonstrates the core functionality of the framework:

```bash
python examples/quantum_symbol_analysis.py
```

**What it does:**
- Creates a sample corpus of Indus script symbols
- Calculates entanglement entropy for symbols
- Measures mutual information between symbol pairs
- Identifies entangled symbol clusters
- Performs holographic analysis
- Generates network visualizations

**Expected output:**
- Detailed analysis of symbol correlations
- Entanglement metrics
- Holographic patterns
- ASCII network visualization
- JSON export of network data

### 2. Consciousness Interface Demo

This example shows the experimental framework for consciousness studies:

```bash
python examples/consciousness_interface_demo.py
```

**What it does:**
- Designs meditation protocols for symbol study
- Analyzes brainwave-symbol correlations
- Maps symbols to archetypal patterns
- Proposes consciousness research studies
- Displays the research manifesto

**Expected output:**
- Meditation protocol design
- Brainwave analysis framework
- Study designs
- Ethical guidelines

## Basic Usage

### Creating a Symbol Corpus

```python
from quantum_archaeology import Symbol, SymbolCorpus
from quantum_archaeology.symbol_system import Inscription, SymbolContext, Location

# Create corpus
corpus = SymbolCorpus()

# Add symbols
unicorn = Symbol("U+01", "Unicorn", "Authority symbol")
fish = Symbol("U+02", "Fish", "Trade symbol")
corpus.add_symbol(unicorn)
corpus.add_symbol(fish)

# Add inscriptions
inscription = Inscription(
    id="M-001",
    symbols=[unicorn, fish],
    location=Location.MOHENJO_DARO,
    context=SymbolContext.ADMINISTRATIVE
)
corpus.add_inscription(inscription)

# Get statistics
stats = corpus.get_corpus_statistics()
print(stats)
```

### Analyzing Entanglement

```python
from quantum_archaeology import EntanglementAnalyzer

# Create analyzer
analyzer = EntanglementAnalyzer(corpus)

# Calculate entanglement entropy
entropy = analyzer.calculate_entanglement_entropy("U+01")
print(f"Entanglement entropy: {entropy}")

# Calculate mutual information
mi = analyzer.calculate_mutual_information("U+01", "U+02")
print(f"Mutual information: {mi}")

# Find entangled clusters
clusters = analyzer.find_entangled_clusters(min_correlation=0.3)
print(f"Found {len(clusters)} clusters")
```

### Holographic Analysis

```python
from quantum_archaeology import HolographicAnalyzer

# Create analyzer
holo = HolographicAnalyzer(corpus)

# Identify holographic patterns
patterns = holo.identify_holographic_patterns()
print(f"Found {len(patterns['holographic_sequences'])} sequences")

# Analyze specific inscription
analysis = holo.analyze_institutional_encoding(inscription)
print(f"Information density: {analysis['information_density']}")
```

### Visualization

```python
from quantum_archaeology.visualization import QuantumNetworkVisualizer

# Create visualizer
viz = QuantumNetworkVisualizer(corpus, analyzer)

# Generate ASCII network
network = viz.generate_ascii_network("U+01")
print(network)

# Export to JSON
viz.export_to_json("network.json", min_correlation=0.2)

# Generate full report
report = viz.create_visualization_report()
print(report)
```

## Key Concepts

### Entanglement Entropy
Measures how "connected" a symbol is to other symbols in the corpus. Higher entropy indicates more diverse connections.

**Formula:** `S = -Σ p(s') * log(p(s'))`

**Use case:** Identify hub symbols that bridge different semantic domains.

### Mutual Information
Quantifies the correlation between two symbols beyond simple co-occurrence.

**Formula:** `I(X;Y) = Σ p(x,y) * log(p(x,y) / (p(x)*p(y)))`

**Use case:** Find symbol pairs with strong dependencies.

### Non-Locality Index
Measures how consistently a symbol appears across different geographical locations.

**Range:** 0 (local) to 1 (perfectly distributed)

**Use case:** Identify standardized administrative symbols.

### Holographic Score
Indicates how much a short sequence encodes about larger institutional structures.

**Calculation:** `information_density * cross_context_appearances`

**Use case:** Find compact institutional signatures.

## Understanding the Output

### Entanglement Entropy Values
- **< 1.0**: Low entanglement, specialized symbol
- **1.0 - 2.0**: Moderate entanglement, common symbol
- **> 2.0**: High entanglement, hub symbol

### Mutual Information Values
- **< 0.1**: Weak correlation
- **0.1 - 0.3**: Moderate correlation
- **> 0.3**: Strong correlation, likely functional relationship

### Information Density Values
- **< 1.0**: Simple, low-information inscription
- **1.0 - 2.0**: Standard inscription
- **> 2.0**: Complex, high-information inscription

## Next Steps

### Explore the Documentation
- **README.md**: Overview and conceptual framework
- **METHODOLOGIES.md**: Detailed research methods
- **QUANTUM_MANIFESTO.md**: Vision and philosophy
- **CONTRIBUTING.md**: How to contribute

### Experiment with the Code
- Modify the example scripts
- Add your own symbols and inscriptions
- Adjust analysis parameters
- Create custom visualizations

### Apply to Your Research
- Load your own corpus data
- Adapt methods to other scripts
- Combine with archaeological data
- Design consciousness experiments

## Common Issues

### Import Errors
If you get import errors, make sure you're running from the correct directory:

```bash
cd indus-operational-mathematics
python examples/quantum_symbol_analysis.py
```

### NumPy Installation
If NumPy fails to install, try:

```bash
pip install --upgrade pip
pip install numpy
```

### Data Loading
When creating your own corpus, ensure:
- Symbol IDs are unique
- Inscriptions reference existing symbols
- Location and context enums are used correctly

## Getting Help

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Read the comprehensive docs
- **Examples**: Study the example scripts

## Additional Resources

### Academic Papers
- Information theory and quantum mechanics
- Indus Valley Civilization archaeology
- Consciousness studies and meditation research
- Undeciphered scripts methodology

### Datasets
- Harappa Archaeological Research Project (HARP)
- Indus Script Concordance
- Cross-cultural symbol databases

### Tools
- NetworkX for network analysis
- D3.js for web visualization
- Gephi for network visualization
- Jupyter notebooks for exploration

## Join the Community

This is an open, collaborative project. We welcome:
- Archaeologists and historians
- Physicists and mathematicians
- Computer scientists and AI researchers
- Consciousness researchers
- Anyone passionate about ancient mysteries

**Start exploring, stay curious, and help us bridge ancient wisdom and modern science!**

---

*"The voyage of discovery is not in seeking new landscapes but in having new eyes." - Marcel Proust*
## Installation

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Install dependencies
pip install -r requirements.txt
```

## Run the Analysis

```bash
# Run the full comparative analysis
python examples/comparative_analysis.py

# Generate visualizations for research paper
python examples/generate_key_visualizations.py
```

## Expected Output

The analysis will show:

```
COMPARATIVE ANALYSIS: INDUS SCRIPT vs YOUTUBE ANALYTICS

Isomorphism score: 98.7/100
Structural similarity: YES

CONCLUSION:
Strong structural isomorphism detected. Both systems exhibit nearly identical 
Zipfian distributions, suggesting the same operational principle: efficient 
state activation through few dominant operators.
```

## Key Files

- **Examples**: `examples/comparative_analysis.py` - Full working example
- **Data**: `data/harappa/` and `data/youtube/` - Example datasets
- **Documentation**: `docs/research_paper.md` - Complete research paper structure
- **Tests**: `tests/` - Unit test suite
- **Output**: `output/` - Generated visualizations

## What This Proves

The analysis demonstrates that ancient Indus Script and modern YouTube Analytics exhibit the same statistical signature:

1. **Zipfian Distribution**: f(r) ∝ 1/r^α where α ≈ 1.7-1.8
2. **High Compression**: ~73% of activity in top 10% of items
3. **Low Entropy**: Highly predictable, structured information flow
4. **Functional Differentiation**: High-frequency items activate states; low-frequency provide depth

This suggests Indus Script was optimized for **operational efficiency** (validation, activation) rather than **narrative expression** (storytelling, literature).

## Citation

```
The same statistical signature observed in the Indus corpus—highly skewed 
frequency distribution with a small set of dominant operators—reappears in 
modern algorithmic systems such as social media platforms. This suggests that 
the Indus Script was optimized not for narrative expression, but for efficient 
state activation and institutional validation, a principle that remains 
cognitively and algorithmically stable across millennia.
```

## Next Steps

1. Replace example data with your own YouTube Analytics
2. Add additional ancient script corpora for comparison
3. Extend to other modern platforms (TikTok, Twitter, etc.)
4. Publish findings in academic journals

## Support

For questions or issues, please open a GitHub issue.

## License

See LICENSE file.
