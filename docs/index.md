---
layout: default
title: Indus Operational Mathematics
---

# Indus Operational Mathematics

**A Formal Framework for State-Based Symbol Systems**

---

## What This Is

This project presents a **formal mathematical framework** for analyzing the Indus Valley (Harappan) script through **operational mathematics** and **state-based computation**.

Rather than treating ancient symbols as phonetic letters, we model them as **state operators** that transform computational contexts through formal compositional rules.

### Core Insight

> In ancient symbol systems, the symbol is not the name of the thing, but the operator on the state.

---

## Quick Links

- [One-Page Overview](one_pager.html)
- [Frequently Asked Questions](faq.html)
- [GitHub Repository](https://github.com/ShantiDraconis/indus-operational-mathematics)
- [Download the Book (PDF)](#) *(Coming soon)*

---

## What We Do NOT Claim

❌ We do NOT claim to decipher the Indus script phonetically  
❌ We do NOT provide word-by-word translations  
❌ We do NOT claim to know what ancient texts "say"  
❌ We do NOT propose sounds for any symbols  

✅ We DO provide a rigorous mathematical framework for structural analysis  
✅ We DO compare operational patterns across writing systems  
✅ We DO verify all claims in four proof assistants  

---

## The Framework

### Five Axioms

1. **A1 (Class Primacy)**: Symbols belong to semantic classes
2. **A2 (No New Classes)**: Operations preserve class membership
3. **A3 (Restricted Composition)**: Only compatible classes compose
4. **A4 (Terminal Closure)**: Terminal symbols enforce boundaries
5. **A5 (Hierarchical Superposition)**: Modifiers apply in layers

### Main Theorem (TCOP)

**Total Closure of Operations Principle**: Every valid symbol sequence represents a well-defined state transformation, closed under the system's rules.

**Status**: Formally verified in Lean 4, Coq, Isabelle/HOL, and Agda.

---

## Example: Ancient Chinese Parallel

The Chinese character 人 (rén, "person") demonstrates operational semantics:

| Transformation | Result | State Change |
|----------------|--------|--------------|
| 人 (base) | person | Generic entity |
| 人 + 一 → 大 | big | Amplification |
| 人 + 人 → 从 | follow | Binary relation |
| 人 + 人 + 人 → 众 | crowd | Collective |

This is NOT phonetic decoration—it's **state transformation**.

We hypothesize Harappan symbols work similarly.

---

## For Different Audiences

### General Public
- [One-Page Overview](one_pager.html)
- [FAQ](faq.html)
- [Glossary](glossary.html)

### Researchers
- [Full Repository](https://github.com/ShantiDraconis/indus-operational-mathematics)
- [Formal Models](/model/)
- [Data & Provenance](/data/)

### Developers
- [Python Implementation](/code/python/)
- [C++ Implementation](/code/cpp/)
- [Formal Verification](/formal/)

---

## Project Status

**Version**: 1.0.0  
**Last Updated**: 2026-02-03  
**Status**: Initial Release

### Completion Status

| Component | Status |
|-----------|--------|
| Axioms A1-A5 | ✅ Complete |
| TCOP Theorem | ✅ Proven |
| Lean Verification | ✅ Complete |
| Coq Verification | ✅ Complete |
| Isabelle Verification | ✅ Complete |
| Agda Verification | ✅ Complete |
| Python Implementation | ✅ Complete |
| Book (LaTeX) | 🚧 In Progress |

---

## License

- **Text/Documentation**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code**: [MIT License](https://opensource.org/licenses/MIT)

---

## Citation

```bibtex
@software{draconis2026indus,
  author = {Draconis, Shanti},
  title = {Indus Operational Mathematics},
  year = {2026},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics},
  version = {1.0.0}
}
```

---

## Contact

- **Issues**: [GitHub Issues](https://github.com/ShantiDraconis/indus-operational-mathematics/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ShantiDraconis/indus-operational-mathematics/discussions)

---

*Last updated: 2026-02-03*
