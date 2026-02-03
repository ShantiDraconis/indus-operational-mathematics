# Quick Start Guide

Welcome to the Indus Operational Mathematics repository!

## What is This?

This repository contains a complete monograph analyzing the Indus (Harappan) script as a formal operational system. **This is NOT a phonetic decipherment attempt.**

## Repository Structure

```
indus-operational-mathematics/
├── book/          # LaTeX source for the monograph
├── data/          # Corpus data (CSV files)
├── code/          # Python implementations
├── figures/       # Diagrams and visualizations
├── appendix/      # Supplementary materials
├── README.md      # Main documentation
├── LICENSE        # Licensing information
└── CITATION.cff   # Citation metadata
```

## Quick Access

### Read the Book
Navigate to `book/main.tex` to see the complete monograph structure. Each chapter is in its own subdirectory with individual `.tex` files.

**Chapters:**
1. Introduction (scope, methodology, limits)
2. Sign System (inventory, families, variants)
3. Operational Classification (5 operators)
4. Mathematical Framework (arithmetic, logic, automata)
5. Comparative Systems (Egyptian, Chinese, Phaistos, runic)
6. Modern Equivalents (workflows, ledgers, JSON)
7. Formal Model (axioms, grammar, proofs)
8. Conclusion (synthesis, implications)

### Explore the Data
CSV files in `data/` directory:
- `sign_list.csv` - Complete sign inventory
- `frequencies.csv` - Sign frequency distribution
- `bigrams.csv` - Two-sign sequence patterns
- `site_distribution.csv` - Geographic distribution
- `object_distribution.csv` - Distribution by object type

### Run the Code
Python implementations in `code/`:
- `indus_dfa.py` - Finite automaton model
- `operator_model.py` - Operator classification system
- `frequency_analysis.ipynb` - Jupyter notebook for statistical analysis

**Test it:**
```bash
cd code/
python indus_dfa.py
python operator_model.py
```

## Key Concepts

### The Five Operators
1. **Instantiation** (INST): Introduces entities
2. **Counting** (COUNT): Assigns quantities
3. **Relation** (REL): Connects entities
4. **Qualification** (QUAL): Adds attributes
5. **Closure** (CLOSE): Validates/finalizes

### The Formal Model
The Indus script is modeled as a Deterministic Finite Automaton (DFA):
- States represent operational contexts
- Transitions represent sign placements
- Valid inscriptions are recognized by the automaton
- Computational power equivalent to regular languages

### Not a Decipherment
This work:
- ✅ Analyzes operational structure
- ✅ Demonstrates mathematical properties
- ✅ Provides formal model
- ❌ Does NOT claim to "read" the script
- ❌ Does NOT provide phonetic values
- ❌ Does NOT translate inscriptions

## For Different Audiences

### For Archaeologists
- See `data/` for corpus statistics
- See Chapter 5 for comparative systems
- See Appendix B for sample inscriptions
- Focus on distributional evidence

### For Computer Scientists
- See Chapter 4 for automata theory
- See Chapter 7 for formal proofs
- See `code/` for implementations
- Focus on computational model

### For Mathematicians
- See Chapter 4 for mathematical framework
- See Chapter 7 for axioms and proofs
- Focus on formal properties and limitations

### For Linguists
- See Chapter 2 for sign system
- See Chapter 5 for comparative analysis
- See Chapter 8 for implications
- Note: This is NOT a linguistic decipherment

## Build the Book

### Requirements
- LaTeX distribution (TeX Live or MiKTeX)
- Standard LaTeX packages

### Compile
```bash
cd book/
pdflatex main.tex
pdflatex main.tex  # Run twice for ToC
```

See `BUILD.md` for detailed instructions.

## Contributing

We welcome:
- Academic discussion and critique
- Additional data and analyses
- Code improvements
- Documentation clarifications

See `CONTRIBUTING.md` for guidelines.

## Citation

To cite this work:
```bibtex
@software{indus_operational_math,
  author = {Draconis, Shanti},
  title = {Operational Mathematics in the Indus Script},
  year = {2026},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics}
}
```

Or use the `CITATION.cff` file.

## License

- Text/Documentation: CC BY 4.0
- Code: MIT
- Data: CC0 1.0 (Public Domain)

## Learn More

- **README.md**: Complete overview
- **Book chapters**: Detailed exposition
- **Code documentation**: Implementation details
- **Issues**: Ongoing discussions

## Questions?

Open an issue on GitHub or see the documentation in individual directories.

---

**Remember**: This is a formal reconstruction of operational structure, NOT a phonetic decipherment!
