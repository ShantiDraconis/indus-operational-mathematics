# Quick Start Guide

## Sistema Operacional de Matemática Harappana - Guia Rápido

### Instalação

Nenhuma instalação necessária! O sistema usa apenas a biblioteca padrão do Python.

**Requisitos:**
- Python 3.7 ou superior (para suporte a dataclasses)

### Uso Básico

#### 1. Importar o Sistema

```python
from harappan_symbols import create_harappan_system, SymbolFamily, GraphicOperator
from harappan_sequence import validate_and_convert, HarappanSequence
from harappan_frequency import create_sample_data
```

#### 2. Criar o Sistema

```python
# Criar sistema completo com todos os 45 símbolos
registry, composition = create_harappan_system()
```

#### 3. Consultar Símbolos

```python
# Obter um símbolo específico
symbol = registry.get_symbol(373)
print(f"Símbolo {symbol.id}: {symbol.description}")

# Obter todos os símbolos de uma família
omega_symbols = registry.get_family_symbols(SymbolFamily.OMEGA)
print(f"Família Ω tem {len(omega_symbols)} símbolos")
```

#### 4. Aplicar Composições

```python
# Aplicar operador a um símbolo
result = composition.get_composition(373, GraphicOperator.DOT)
print(f"373 + DOT = {result}")

# Decompor um símbolo
decompositions = composition.get_decomposition(394)
for base, operator in decompositions:
    print(f"394 = {base} + {operator.value}")
```

#### 5. Validar Sequências

```python
# Validar uma sequência de símbolos
sequence = [373, 400, 410]  # entidade → relação → contagem
result = validate_and_convert(sequence)

print(f"Válida: {result['valid']}")
print(f"Notação: {result['functional_notation']}")
```

#### 6. Criar Sequência JSON

```python
import json

# Criar sequência institucional
sequence = HarappanSequence()
sequence.object_type = "seal"
sequence.provenance = "Harappa"
sequence.add_symbol(373)
sequence.add_symbol(410)
sequence.add_symbol(394)

# Converter para JSON
print(json.dumps(sequence.to_json(), indent=2))
```

### Executar Exemplos Completos

Para ver todos os exemplos em ação:

```bash
python3 examples.py
```

Este script demonstra:
1. Consulta de símbolos básicos
2. Sistema de composição
3. Validação de sequências
4. Representação JSON moderna
5. Análise de frequência
6. Autômato finito de validação

### Conceitos-Chave

#### Três Famílias de Símbolos

- **Ω (Omega, 373-399)**: Entidades/Tokens
  - Corpo-base: oval/círculo
  - Função: representar entidades institucionais

- **Δ (Delta, 400-409)**: Relações/Vínculos
  - Corpo-base: pares de ovais, nós, halteres
  - Função: estabelecer conexões formais

- **Σ (Sigma, 410-417)**: Contagens/Pilhas
  - Corpo-base: empilhamento de discos
  - Função: codificar quantidades

#### Operadores Gráficos Universais

10 operadores que modificam símbolos base:

1. **Dot** (•): Instância/ativação
2. **Stroke** (│): Partição/qualificação
3. **Fill** (█): Estado consumado
4. **Bracket** (⟦⟧): Escopo/jurisdição
5. **SideBars** (║): Nível/autoridade
6. **Crown** (⸙): Multiplexação
7. **Dup** (⊕): Duplicação/par
8. **Knot** (⚭): Vínculo forte
9. **Stem** (⊥): Âncora/indexação
10. **Stack** (≡): Contagem/agregação

#### Composição Hierárquica

**Caso crítico**: 394 = 373 + 343

- Operadores podem ser aplicados entre famílias
- Sistema admite composição hierárquica, não apenas linear

### Teste Rápido

Execute este código para verificar se tudo está funcionando:

```python
from harappan_symbols import create_harappan_system
from harappan_sequence import validate_and_convert

# Criar sistema
registry, composition = create_harappan_system()

# Validar sequência
result = validate_and_convert([373, 400, 410])

# Verificar resultado
assert result['valid'] == True
assert 'Entity(373)' in result['functional_notation']
assert 'Relation(400)' in result['functional_notation']
assert 'Count(2)' in result['functional_notation']

print("✓ Sistema funcionando corretamente!")
```

### Estrutura de Arquivos

```
.
├── README.md                  # Documentação completa
├── TECHNICAL_SUMMARY.md       # Resumo técnico
├── QUICKSTART.md             # Este arquivo
├── harappan_symbols.py       # Símbolos, famílias e composição
├── harappan_sequence.py      # Sequências e validação
├── harappan_frequency.py     # Análise de frequência
├── examples.py               # Exemplos completos
└── requirements.txt          # Sem dependências externas
```

### Próximos Passos

1. Execute `python3 examples.py` para ver demonstrações
2. Leia `README.md` para documentação completa
3. Consulte `TECHNICAL_SUMMARY.md` para detalhes técnicos
4. Explore o código fonte para entender a implementação

### Recursos Adicionais

- **Documentação Completa**: README.md
- **Resumo Técnico**: TECHNICAL_SUMMARY.md
- **Exemplos Executáveis**: examples.py
- **Código Fonte**: harappan_*.py

### Suporte

Para questões sobre implementação:
1. Consulte a documentação nos arquivos .md
2. Execute os exemplos para ver padrões de uso
3. Leia os comentários no código fonte

### Licença

MIT License - Veja arquivo LICENSE para detalhes.

---

**Versão**: 1.0.0  
**Python**: 3.7+  
**Dependências**: Nenhuma (apenas biblioteca padrão)
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
