# Quick Start Guide

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
