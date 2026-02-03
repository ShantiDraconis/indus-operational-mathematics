# Indus Operational Mathematics - Public Overview

**Quick Reference for Public Understanding**

---

## One-Page Summary

### What is This?

A **formal mathematical framework** for studying how ancient symbols (specifically from the Indus Valley civilization) work as **computational operators** rather than phonetic letters.

### The Core Idea

Think of ancient symbols like **programming commands** or **JSON keys**:
- They don't "spell sounds"
- They **transform states**
- They **compose according to rules**
- They produce **well-defined outputs**

### Example: The "Person" Operator

In ancient Chinese writing, the symbol 人 (person) transforms:

```
人 (base)           → "generic entity"
人 + 一 (one line)  → 大 (big)        = "amplified state"
人 + 人             → 从 (follow)     = "binary relation"
人 + 人 + 人         → 众 (crowd)      = "collective state"
```

This is NOT phonetic decoration. It's **state transformation through composition**.

### The Harappan Connection

We hypothesize that Harappan symbols work similarly:

```
Symbol 26 (base entity)
Symbol 26 + modifier A → instantiated entity
Symbol 26 + modifier B → qualified entity
Symbol 26 + modifier C → elevated entity
```

### Five Axioms (Simplified)

1. **Class Primacy**: Every symbol belongs to a category (number, entity, modifier, etc.)
2. **No New Classes**: Operations don't create new categories
3. **Restricted Composition**: Only compatible symbols can combine
4. **Terminal Closure**: Some symbols end sequences (like periods)
5. **Hierarchical Superposition**: Modifiers apply in layers

### Modern Analogy: JSON State Machine

```json
{
  "base": "entity",
  "operations": [
    {"operator": "quantify", "value": 3},
    {"operator": "qualify", "value": "authorized"},
    {"operator": "close", "value": true}
  ],
  "result_state": "three_authorized_entities_closed"
}
```

---

## What We DO NOT Claim

🚫 **We do NOT**:
- Decipher the Indus script phonetically
- Provide word-for-word translations
- Claim to "solve" or "crack" the Indus script
- Propose sounds for any symbols
- Make linguistic claims

✅ **We DO**:
- Provide a mathematical framework for analysis
- Identify structural patterns in composition
- Compare operational structures across writing systems
- Formally verify our mathematical models
- Maintain full reproducibility

---

## Why This Matters

### For Researchers
- Rigorous formal methods applied to ancient scripts
- Reproducible computational analysis
- Cross-cultural structural comparisons

### For Mathematicians
- Novel application of state-based computation
- Formal verification in 4 proof assistants
- Interesting compositional algebra

### For the Public
- Scientific approach to ancient mysteries
- No sensationalist claims
- Transparent methodology

---

## Quick Links

- **Full Documentation**: [Main README](../README.md)
- **FAQ**: [faq.md](faq.md)
- **Technical Glossary**: [glossary_public.md](glossary_public.md)
- **Examples**: [examples/](examples/)
- **GitHub Pages**: [Project Website](https://shantidraconis.github.io/indus-operational-mathematics)

---

## How to Read This Project

### 1. Start Here (Public Layer)
- This one-pager
- FAQ
- Basic examples

### 2. Conceptual Layer
- Read `model/axioms/` for the formal rules
- Study `model/theorem/` for the main result

### 3. Verification Layer
- See `formal/lean/`, `formal/coq/`, etc. for proofs

### 4. Research Layer
- Read the book in `book/main.pdf`
- Explore data in `data/derived/`

---

## Contact

- **Issues**: For bugs or questions
- **Discussions**: For conceptual questions
- **Email**: [To be added]

---

## Citation

```
Draconis, S. (2026). Indus Operational Mathematics: A Formal Framework 
for State-Based Symbol Systems. GitHub. 
https://github.com/ShantiDraconis/indus-operational-mathematics
```

---

*"Symbols are not names—they are operators."*

**Version**: 1.0.0  
**Last Updated**: 2026-02-03
