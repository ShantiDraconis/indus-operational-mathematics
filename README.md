# Indus Operational Mathematics

## A Formal Reconstruction of the Harappan Operational System: Mathematics, States, and Validation

This repository contains the complete monograph and formal model of the
Indus (Harappan) script as an operational symbolic system implementing
finite mathematics, relational logic, and state-based validation.

**This work does NOT propose a phonetic decipherment.**

## Overview

This research analyzes the Indus script as a formal system of operational notation used for administrative and institutional validation. The work reconstructs:

- **Finite arithmetic** and cardinal operations
- **Relational logic** and state transitions
- **Institutional validation** mechanisms
- **Formal equivalents** in modern computational terms

## Repository Structure

```
indus-operational-mathematics/
├── book/                      # Complete monograph source (LaTeX)
│   ├── 00_frontmatter/       # Title, abstract, notation
│   ├── 01_introduction/      # Scope, methodology, limits
│   ├── 02_sign_system/       # Sign inventory and families
│   ├── 03_operators/         # Operational classifications
│   ├── 04_mathematics/       # Mathematical framework
│   ├── 05_comparative_systems/ # Cross-cultural comparisons
│   ├── 06_modern_equivalents/ # Contemporary parallels
│   ├── 07_formal_model/      # Axioms and formal proofs
│   ├── 08_conclusion/        # Synthesis and implications
│   └── main.tex              # Main document file
├── data/                      # Empirical datasets (CSV)
├── figures/                   # Diagrams and visualizations
├── code/                      # Computational models (Python)
├── appendix/                  # Supplementary materials (LaTeX)
├── LICENSE                    # Licensing information
└── CITATION.cff              # Citation metadata
```

## Title

**Operational Mathematics in the Indus Script: Finite Arithmetic, State Logic, and Institutional Validation**

## Licensing

- **Text and Documentation**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code**: MIT License
- **Data**: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain Dedication)

## Scientific Registry

This repository serves as the development version. Immutable releases are archived on [Zenodo](https://zenodo.org) with permanent DOIs for scientific citation and priority claims.

## Citation

To cite this work, please use the information provided in `CITATION.cff` or refer to the Zenodo DOI for the specific version.

## Building the Monograph

Requirements:
- LaTeX distribution (TeX Live or MiKTeX)
- Python 3.8+ (for computational models)
- Standard LaTeX packages

To compile the book:
```bash
cd book/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Contributing

This is a research monograph repository. For questions or academic discussion, please open an issue.

## Contact

For academic inquiries, please use the GitHub issue tracker or contact information provided in the monograph.