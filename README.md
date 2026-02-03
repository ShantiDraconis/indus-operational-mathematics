# Indus Operational Mathematics

**A Formal Framework for State-Based Symbol Systems**

[![License: CC BY 4.0](https://img.shields.io/badge/License%20(text)-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License%20(code)-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

---

## What This Is

This repository presents a **formal mathematical framework** for analyzing the Indus Valley (Harappan) script through the lens of **operational mathematics** and **state-based computation**. 

### Core Insight

Rather than treating ancient symbols as fixed phonetic or semantic units, we model them as **state operators** that transform computational contexts through formal compositional rules. The framework draws deep structural parallels with ancient Chinese character transformations, particularly the radical 人 (rén, "person") and its systematic modifications.

### Key Components

1. **Formal Axiomatic System**: Five axioms (A1-A5) governing symbol composition and state transformation
2. **Comparative Analysis**: Structural comparison with ancient Chinese operational semantics
3. **Formal Verification**: Implementations in Lean 4, Coq, Isabelle/HOL, and Agda
4. **Computational Models**: Python and C++ implementations for analysis
5. **Comprehensive Monograph**: LaTeX book documenting the complete theoretical foundation

---

## What This Is NOT

### Non-Claims (Critical)

This work **explicitly does NOT**:

❌ Claim to decipher the Indus script phonetically  
❌ Provide linguistic translations of Indus texts  
❌ Establish historical meanings of specific symbols  
❌ Propose phonetic values for any Harappan signs  
❌ Claim to "solve" or "crack" the Indus script  

### What We DO Claim

✅ A rigorous mathematical framework for analyzing symbol operations  
✅ Identification of structural patterns in compositional rules  
✅ Formal comparison with verified operational patterns in ancient Chinese  
✅ Computational models that are formally verified and reproducible  
✅ A foundation for future research using formal methods  

**Epistemological Stance**: We study the **mathematics of symbol composition**, not historical linguistics. Our claims are about **operational structure**, not **semantic content**.

---

## Repository Structure

```
indus-operational-mathematics/
├── public/              # Public-facing content (safe dissemination)
│   ├── one_pager.md     # Quick overview
│   ├── faq.md           # Frequently asked questions
│   └── glossary_public.md
├── docs/                # GitHub Pages site
├── book/                # LaTeX monograph
│   ├── main.tex
│   ├── chapters/        # 11 chapters + appendices
│   └── bibliography.bib
├── model/               # Formal specifications
│   ├── axioms/          # A1-A5 axiom definitions
│   ├── grammar/         # Compositional rules (BNF)
│   ├── automata/        # State machine definitions
│   └── theorem/         # TCOP theorem & proofs
├── formal/              # Formal verification
│   ├── lean/            # Lean 4 implementation
│   ├── coq/             # Coq implementation
│   ├── isabelle/        # Isabelle/HOL implementation
│   └── agda/            # Agda implementation
├── data/                # Research data
│   ├── derived/         # Processed datasets (CSV/JSON)
│   └── provenance/      # Source attribution
├── code/                # Computational implementations
│   ├── python/          # Python analysis tools
│   ├── cpp/             # C++ implementations
│   └── scripts/         # Reproducibility scripts
└── releases/            # Release management for Zenodo
```

---

## Quick Start

### For Readers (Public Content)

Start with the public-facing materials:

```bash
cd public/
cat one_pager.md
cat faq.md
```

Or visit our **GitHub Pages site**: [https://shantidraconis.github.io/indus-operational-mathematics](https://shantidraconis.github.io/indus-operational-mathematics)

### For Researchers (Full Access)

1. **Read the Book**:
   ```bash
   cd book/
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   
2. **Explore the Formal Model**:
   ```bash
   cd model/
   cat axioms/A1_class_primacy.md
   cat theorem/tcop_statement.md
   ```

3. **Run the Code**:
   ```bash
   cd code/
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python scripts/build_bigrams.py
   ```

### For Formal Methods Practitioners

Verify the proofs in your preferred system:

**Lean 4**:
```bash
cd formal/lean/
lake build
```

**Coq**:
```bash
cd formal/coq/
make
```

**Isabelle**:
```bash
cd formal/isabelle/
isabelle build -D .
```

**Agda**:
```bash
cd formal/agda/
agda --safe IndusOperationalMathematics.agda
```

---

## Methodology: The Base-Operator-State Paradigm

### Central Theorem (TCOP - Total Closure of Operations Principle)

**Informal Statement**: In operational symbol systems, every valid symbol sequence represents a well-defined state transformation, and the composition of these transformations is closed under the system's rules.

**Formal Statement** (see `model/theorem/tcop_statement.md`):

```
∀ system S with symbols Σ, operators Ω, and states Θ:
  (1) ∀ σ ∈ Σ ∃ state(σ) ∈ Θ
  (2) ∀ ω ∈ Ω, ∀ θ ∈ Θ: ω(θ) ∈ Θ
  (3) Composition is closed: (ω₁ ∘ ω₂)(θ) ∈ Θ
  (4) Terminal symbols enforce closure: σ_terminal ⊢ ⊥ (no further ops)
```

### The Five Axioms

1. **A1 (Class Primacy)**: Symbols belong to disjoint semantic classes
2. **A2 (No New Classes)**: Operations preserve class membership
3. **A3 (Restricted Composition)**: Only compatible classes can compose
4. **A4 (Terminal Closure)**: Certain symbols enforce sequence termination
5. **A5 (Hierarchical Superposition)**: Modifiers apply in well-defined layers

See `model/axioms/` for complete formalization.

---

## Comparative Analysis: Harappan vs. Ancient Chinese

### Case Study: "Person" as State Operator

#### Ancient Chinese: 人 (rén)

| Transformation | Result | State Change |
|----------------|--------|--------------|
| 人 (base) | person | Generic entity |
| 人 + 一 → 大 | big | Amplification |
| 人 + 人 → 从 | follow | Binary relation |
| 人 × 3 → 众 | crowd | Collective |
| 人 + □ → 囚 | prisoner | Containment |
| 人 inverted → 入 | enter | Transition |

#### Harappan: Symbol 26 (Hypothesized)

| Transformation | Hypothesized Result | State Change |
|----------------|---------------------|--------------|
| 26 (base) | entity | Generic |
| 26 + dot → 27 | instantiated | Activation |
| 26 + stroke → 28 | qualified | Attribution |
| 26 + bracket → 29 | delimited | Contextualization |
| 26 + crown → 30 | authorized | Elevation |

**Structural Parallel**: Both systems use **graphical modification** as **state transformation**, not phonetic decoration.

---

## Data & Reproducibility

### Data Provenance

All data sources are documented in `/data/provenance/sources.yml` with:
- Source references (papers, catalogs)
- Page numbers and extraction dates
- License information
- Checksums (where applicable)

### Reproducibility Pipeline

Our CI/CD ensures full reproducibility:

```bash
# Run the complete pipeline
cd code/
./scripts/extract_tables.py    # data/raw → data/derived
./scripts/build_bigrams.py      # Generate frequency tables
./scripts/export_figures.py     # book/figures/
```

All figures and tables in the book are **generated from data**, not manually created.

---

## Building the Book

### Prerequisites

- TeX Live (or MiKTeX) with `pdflatex` and `bibtex`
- Required LaTeX packages: `amsmath`, `amsthm`, `graphicx`, `tikz`, `listings`

### Compilation

```bash
cd book/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex  # For cross-references
```

Or use the CI pipeline (see `.github/workflows/build-book.yml`).

### Chapters

1. Introduction & Motivation
2. Methodology & Non-Claims
3. Inventory & Symbol Families (1-44)
4. Operators & Composition Rules
5. Frequency, Position & Bigram Analysis
6. Automata & State-Time Dynamics
7. Mathematical Scope & Limitations
8. Comparative Systems (Ancient Chinese)
9. Modern Equivalents (JSON, Relational Logic)
10. The TCOP Theorem
11. Conclusion & Future Work

---

## Formal Verification

### Why Multiple Proof Assistants?

Different systems offer complementary strengths:

- **Lean 4**: Modern, powerful tactics, good for computation
- **Coq**: Mature ecosystem, extensive libraries
- **Isabelle/HOL**: Strong automation (Sledgehammer)
- **Agda**: Dependent types, constructive mathematics

### Verification Status

| Component | Lean | Coq | Isabelle | Agda |
|-----------|------|-----|----------|------|
| Axioms A1-A5 | ✅ | ✅ | ✅ | ✅ |
| TCOP Theorem | ✅ | ✅ | ✅ | ✅ |
| Corollaries | ✅ | ✅ | ✅ | ✅ |
| Automata Model | ✅ | ✅ | ✅ | ⚠️ (partial) |

### Running Verification

Each proof assistant directory contains:
- `README.md`: Setup instructions
- `Makefile` or build configuration
- Complete formalization of axioms and theorems

---

## Citation

If you use this work, please cite:

```bibtex
@software{draconis2026indus,
  author = {Draconis, Shanti},
  title = {Indus Operational Mathematics: A Formal Framework for State-Based Symbol Systems},
  year = {2026},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics},
  doi = {10.5281/zenodo.XXXXXXX},
  version = {1.0.0}
}
```

Or use the `CITATION.cff` file for automated tools.

---

## Contributing

We welcome contributions! Please see:

- [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards
- [SECURITY.md](SECURITY.md) for security policies

**Key principle**: All claims must be backed by formal mathematics and reproducible analysis.

---

## License

This project uses **dual licensing**:

- **Text/Documentation**: [CC BY 4.0](LICENSE_TEXT.md) - book, papers, docs
- **Code/Software**: [MIT License](LICENSE_CODE.md) - implementations, scripts

---

## Contact & Community

- **GitHub Discussions**: For questions and conceptual discussions
- **Issues**: For bug reports and specific problems
- **Pull Requests**: For contributions

---

## Acknowledgments

This work builds on decades of Indus Valley research by archaeologists, linguists, and computational scholars. While our approach is novel, we stand on the shoulders of giants.

**Special thanks to**:
- The Indus research community for maintaining open data
- The formal methods community for proof assistant development
- Comparative paleography scholars for cross-cultural insights

---

## Roadmap

### Version 1.0 (Current)
- ✅ Core axioms formalized
- ✅ TCOP theorem proven in 4 proof assistants
- ✅ Comparative analysis with ancient Chinese
- ✅ Book chapters 1-11 complete

### Version 1.1 (Planned)
- [ ] Extended symbol catalog (45-200)
- [ ] Additional comparative systems (Sumerian, Egyptian)
- [ ] Machine learning integration for pattern discovery
- [ ] Interactive web demonstrations

### Version 2.0 (Future)
- [ ] Full corpus analysis
- [ ] Cross-site statistical validation
- [ ] Collaboration with archaeological teams
- [ ] Museum partnerships for high-resolution imaging

---

## Frequently Asked Questions

See [public/faq.md](public/faq.md) for detailed answers, including:

- **Is this a decipherment?** No, it's a formal mathematical framework.
- **Can I read Indus texts now?** No, we make no phonetic claims.
- **What's the significance?** We provide tools for rigorous structural analysis.
- **How does this compare to X's work?** See comparative analysis in the book.

---

**Last updated**: 2026-02-03  
**Version**: 1.0.0  
**Status**: Initial Release

---

*"In ancient symbol systems, the symbol is not the name of the thing, but the operator on the state."*