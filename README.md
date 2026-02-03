# Indus Operational Mathematics

## Sistema Operacional Harappano: Modelo Formal Completo

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> A complete formal reconstruction of the Indus script as a finite-state operational system for institutional validation.

## Overview

The Harappan Operational System is a formal mathematical model that reconstructs the Indus script not as a phonetic language, but as a **finite-state automaton** designed for administrative validation and institutional record-keeping. This repository contains the complete implementation, data, and documentation.

### Key Discovery

The Indus script operates as:
- **Not a language** → A validation protocol
- **417 catalogued states** derived from ~45 fundamental elements
- **Universal operators** → Reappear in Festos, Egyptian, and Chinese scripts
- **Modern equivalent** → Workflows, automata, JSON schemas, blockchain validation

## System Architecture

```
S = (B, O, Σ, R, F)

B = Base bodies (≈30 ontological classes)
O = Graphic operators (≈15 universal modifiers)
Σ = Valid states (417 catalogued symbols)
R = Composition rules (extracted from Tables II-IV)
F = Final states (family 342-348 + specialized closers)
```

### The Finite Automaton

The system has **6 states**:

```
S₀: INICIAL        → No symbol processed
S₁: ENTIDADE       → Entity recognized
S₂: QUALIFICADA    → Qualification applied
S₃: QUANTIFICADA   → Quantity specified
S₄: RELACIONADA    → Relation established
S₅: FECHADA        → Closure applied ★ ACCEPTING STATE
```

### BNF Grammar

```bnf
<registro> ::= <entidade> <qualificador>* <quantificador>? <relacionador>? <fechamento>

<entidade>      ::= ENT_OVAL | ENT_U | ENT_HASTE | ENT_ANIMAL | ENT_METRICA
<qualificador>  ::= OP_QUAL | OP_SCOPE | <intensificador>
<quantificador> ::= OP_COUNT | ||| | |||| | ...
<relacionador>  ::= OP_REL | Knot | Dup
<fechamento>    ::= OP_CLOSE (342-348)
```

## Repository Structure

```
indus-operational-mathematics/
├── formal_model/          # Mathematical model
│   ├── automata/          # Finite automaton specification
│   ├── algebra/           # Operator algebra
│   └── proofs/            # Formal proofs
├── data/                  # Corpus data
│   ├── signs.csv          # 417 symbols + attributes
│   ├── bigrams.csv        # Co-occurrence data (Table II)
│   ├── frequencies.csv    # Frequency distribution (Table I)
│   └── indus-record-schema.json  # JSON Schema specification
├── implementation/        # Executable code
│   ├── parser/            # Syntax parser
│   │   └── indus_automaton.py
│   ├── validator/         # Sequence validator
│   │   └── indus_validator.py
│   ├── converter/         # Format converters
│   │   └── harappan_to_json.py
│   └── simulator/         # Automaton simulator
├── comparisons/           # Comparative systems
│   ├── festos/            # Phaistos Disc
│   ├── egyptian/          # Egyptian hieroglyphs
│   └── chinese/           # Early Chinese
└── publications/          # Academic documentation
    ├── paper/             # Research paper
    ├── book/              # Full monograph
    └── presentations/     # Presentation materials
```

## Installation

### Requirements

- Python 3.8 or higher
- No external dependencies for core functionality

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Run the automaton
python implementation/parser/indus_automaton.py

# Run the validator
python implementation/validator/indus_validator.py

# Convert sequences to JSON
python implementation/converter/harappan_to_json.py
```

## Usage Examples

### Example 1: Validate a Sequence

```python
from implementation.parser.indus_automaton import validate_indus_sequence

# Simple record: entity + closure
sequence = [373, 342]  # basic_token + simple_closure
is_valid, error = validate_indus_sequence(sequence)
print(f"Valid: {is_valid}")  # Output: Valid: True
```

### Example 2: Convert to JSON

```python
from implementation.converter.harappan_to_json import harappan_to_json

# Record with quantity
sequence = [373, 410, 411, 342]  # entity + count(1) + count(2) + closure
record = harappan_to_json(sequence)
print(record)
# Output: {'entity': 'basic_token', 'quantity': 3, 'closure': 'simple', ...}
```

### Example 3: Use the Automaton

```python
from implementation.parser.indus_automaton import IndusAutomaton, SymbolClass

automaton = IndusAutomaton()

# Process a sequence
automaton.process_symbol(SymbolClass.ENT_OVAL)
automaton.process_symbol(SymbolClass.OP_COUNT)
automaton.process_symbol(SymbolClass.OP_CLOSE)

print(automaton.is_valid_record())  # Output: True
print(automaton.get_current_state())  # Output: State.S5 (FECHADA)
```

### Example 4: Detailed Validation

```python
from implementation.validator.indus_validator import IndusValidator

validator = IndusValidator()

sequence = [200, 410, 411, 343]  # unicorn + count + count + confirmed_closure
result = validator.validate_with_details(sequence)

print(f"Valid: {result['is_valid']}")
print(f"Final State: {result['final_state']}")
print(f"Symbol Classes: {result['symbol_classes']}")
```

## The 30 Ontological Classes

| Class | Symbol Range | Function | Examples |
|-------|--------------|----------|----------|
| ENT_OVAL | 373-399 | Institutional entities | Basic token, seals |
| ENT_U | 328-339 | Containers/vessels | Small, medium, large |
| ENT_HASTE | 250-260 | Authority/hierarchy | Staffs, scepters |
| ENT_ANIMAL | 200-210 | Functional agents | Unicorn, bull, elephant |
| ENT_METRICA | 100-150 | Measures/quantities | Weight, length, volume |
| OP_CLOSE | 342-348 | Terminal closure | Simple, confirmed, absolute |
| OP_QUAL | Various | Qualification | Dot, stroke, crown |
| OP_REL | 400-409 | Binary relations | Pair, hierarchy, exchange |
| OP_COUNT | 410-417 | Counting | 1, 2, 3, 4, 5, 10, 20, 100 |
| OP_SCOPE | Bracket | Scope delimitation | Context boundaries |

## Key Theorems

### Theorem 1: Syntactic Completeness
```
∀ valid record r, ∃ sequence s ∈ Σ* such that
  s ⊢ r ∧ s ends with closure symbol
```

### Theorem 2: Operational Consistency
```
If s₁ → s₂ and s₁ ∈ Class_X, then s₂ ∈ Class_X
(Operators don't change ontological classes)
```

### Theorem 3: Terminal Closure
```
If s ∈ OP_CLOSE, then ∄ t such that s → t
(Closure is an absorbing state)
```

## Comparison with Other Systems

| System | Entity | Qualification | Quantification | Closure |
|--------|--------|---------------|----------------|---------|
| Harappa | 373-399 | Dot, Stroke | 410-417 | 342-348 |
| Phaistos | Ovals | Dots | Strokes | Spiral end |
| Egyptian | Cartouche | Determinatives | Strokes | Serekh |
| Chinese | Radical | Markers | 一,二,三 | 終 |

## Modern Applications

### As a Validation Framework

```yaml
# YAML specification based on Harappan principles
validation_schema:
  entity: required
  qualifiers: optional
  quantity: optional
  relations: optional
  closure: required
  
  rules:
    - "closure must be last"
    - "quantity requires entity"
    - "relation requires at least two entities"
```

### As a DSL (Domain-Specific Language)

```
# DSL for institutional records
record {
  entity 373
  qualified by dot, stroke
  quantity 3
  related to 400 via knot
  closed with 346
}
```

### As a Smart Contract

```solidity
// Ethereum smart contract inspired by Harappan logic
contract IndusRecord {
    enum State { Open, Qualified, Counted, Related, Closed }
    
    struct Record {
        uint256 entity;
        address[] qualifiers;
        uint256 quantity;
        uint256[] relations;
        State state;
    }
    
    function closeRecord(uint256 recordId, uint256 closureType) public {
        require(closureType >= 342 && closureType <= 348, "Invalid closure");
        records[recordId].state = State.Closed;
    }
}
```

## Data Files

### signs.csv
Complete catalog of 417 symbols with:
- Symbol ID
- Ontological class
- Description
- Frequency counts
- Position preferences

### bigrams.csv
Co-occurrence matrix (Table II) showing:
- Symbol pair frequencies
- Contextual usage
- Positional relationships

### frequencies.csv
Distribution data (Table I) including:
- Total frequencies
- Position distributions
- Medium-specific counts (seals, tablets, pottery)

## Contributing

We welcome contributions in:
- Additional formal proofs
- Comparative analysis with other ancient scripts
- Modern applications and implementations
- Visualization tools
- Documentation improvements

## Citation

If you use this work in academic research, please cite:

```bibtex
@software{indus_operational_mathematics_2026,
  title = {Indus Operational Mathematics: A Formal Model of Harappan Administrative Notation},
  author = {ShantiDraconis},
  year = {2026},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics},
  license = {CC-BY-4.0}
}
```

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit

## Acknowledgments

This work builds upon:
- Parpola, A. (1994). *Deciphering the Indus Script*
- Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*
- Wells, B. (2011). "Epigraphic Approaches to Indus Writing"

## Status

✅ **Complete**: The formal model is fully specified  
✅ **Implemented**: Core automaton and validator are functional  
✅ **Documented**: Mathematical proofs and usage examples provided  
🚧 **In Progress**: Visualization tools and web interface  
📋 **Planned**: Academic publication and conference presentations

## Contact

For questions, collaborations, or feedback:
- GitHub Issues: [Report an issue](https://github.com/ShantiDraconis/indus-operational-mathematics/issues)
- Discussions: [Join the discussion](https://github.com/ShantiDraconis/indus-operational-mathematics/discussions)

---

**The system is closed. The model is complete. The implementation is direct.**