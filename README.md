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
```

## References

This framework is based on the theory that all writing systems are realizations of a universal cognitive grammar:

- The Harappan system is a realization
- The Chinese system is a realization
- The Mayan system is a realization
- The Runic systems are a realization

All are variations on deeply human themes of symbolic representation.