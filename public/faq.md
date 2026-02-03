# Frequently Asked Questions

---

## General Questions

### Q1: What is this project about?

This project presents a **formal mathematical framework** for analyzing the Indus Valley (Harappan) script. We treat symbols as **state operators** that transform computational contexts, rather than as phonetic units.

### Q2: Have you deciphered the Indus script?

**No.** We explicitly do NOT claim to:
- Decipher the script phonetically
- Provide word-for-word translations
- Determine what specific symbols "mean" historically

We provide a **mathematical framework** for understanding how symbols might **compose and transform states**.

### Q3: Then what's the point?

We offer:
1. **Rigorous formal methods** for structural analysis
2. **Comparative insights** from other ancient writing systems (esp. Chinese)
3. **Reproducible computational tools** for researchers
4. **Formal verification** of our mathematical claims

This is foundational work for **future research**, not a complete solution.

---

## Methodology Questions

### Q4: What do you mean by "state operators"?

Instead of thinking "this symbol means X", think "this symbol transforms the computational state from A to B".

**Example**: In ancient Chinese:
- 人 (person) is not just a "word"
- 人 + 一 → 大 (big) is a **transformation**
- The **operation** of adding 一 **changes the state** of 人

This is similar to:
- Programming: `state = state.apply(operator)`
- Mathematics: `f(x) → y`

### Q5: How is this different from traditional decipherment?

**Traditional approach**:
- Find sound values for symbols
- Build a dictionary
- Translate texts

**Our approach**:
- Find compositional rules
- Build a state algebra
- Model transformations

We're doing **formal mathematics**, not **historical linguistics**.

### Q6: Why compare with ancient Chinese?

Ancient Chinese oracle bone script (甲骨文) is:
1. **Well-documented** (we know it worked)
2. **Highly compositional** (symbols transform systematically)
3. **Non-alphabetic** (not phonetic spelling)

It provides a **proven example** of operational symbol composition.

---

## Technical Questions

### Q7: What are the five axioms?

Simplified:
1. **A1**: Symbols belong to semantic classes (quantifier, entity, modifier, etc.)
2. **A2**: Operations preserve class membership
3. **A3**: Only compatible classes can compose
4. **A4**: Terminal symbols force closure
5. **A5**: Modifiers apply hierarchically

See `model/axioms/` for formal definitions.

### Q8: What is the TCOP theorem?

**TCOP** = **Total Closure of Operations Principle**

**Informal**: Every valid symbol sequence represents a well-defined state transformation, and compositions are closed under the system's rules.

**Significance**: This provides a **mathematical criterion** for distinguishing valid from invalid sequences—without knowing phonetic values.

### Q9: Why use multiple proof assistants?

Different proof assistants offer different strengths:
- **Lean 4**: Modern, good for computation
- **Coq**: Mature ecosystem
- **Isabelle**: Powerful automation (Sledgehammer)
- **Agda**: Strong dependent types

Using **all four** increases confidence in our proofs.

### Q10: Is this reproducible?

**Yes.** Every figure and table in the book is **generated from data** using scripts in `code/scripts/`. Our CI pipeline automatically:
- Rebuilds the book
- Recompiles proofs
- Regenerates figures
- Validates data provenance

---

## Comparison Questions

### Q11: How does Symbol 26 relate to 人 (rén)?

**Structural parallel**:

| Transformation | Chinese | Hypothesized Harappan |
|----------------|---------|------------------------|
| Base | 人 (person) | Symbol 26 (entity) |
| + One element | 大 (big) | Symbol 27 (instantiated) |
| + Two elements | 从 (follow) | Symbol 28 (qualified) |
| + Container | 囚 (prisoner) | Symbol 29 (delimited) |

We're NOT saying "Symbol 26 means person". We're saying "Symbol 26 transforms like 人 does".

### Q12: Couldn't this be coincidence?

Possibly! That's why we:
1. Use **formal mathematics** to make claims precise
2. Provide **statistical analysis** of patterns
3. Include **multiple proof systems** for verification
4. Maintain **transparent data provenance**

Our claims are **falsifiable** and **reproducible**.

---

## Interpretation Questions

### Q13: If not phonetic, what were the Indus inscriptions for?

We **don't claim to know**. Possibilities include:
- Administrative records
- Ritual markers
- Ownership labels
- State-based computations (our framework)

Our work is **agnostic** about historical function.

### Q14: Does this prove the Indus script was "real writing"?

**No.** The debate over whether the Indus script is "writing" depends on definitions of writing. We show it has **compositional structure**, which is compatible with various interpretations.

### Q15: Could this framework apply to other scripts?

**Yes!** We believe state-based operational analysis could apply to:
- Sumerian cuneiform (proto-cuneiform phase)
- Egyptian hieroglyphs (early dynastic)
- Linear A (Minoan)
- Rongorongo (Easter Island)

This is a **general framework**, not Indus-specific.

---

## Practical Questions

### Q16: Can I use this to translate an Indus seal?

**No.** We do not provide:
- Phonetic values
- Word meanings
- Translation methods

We provide **structural analysis tools** for researchers.

### Q17: How can I contribute?

See [CONTRIBUTING.md](../CONTRIBUTING.md). We welcome:
- Bug reports
- Documentation improvements
- Code contributions (with tests)
- Formal verification extensions
- Comparative analyses with other systems

### Q18: Is this peer-reviewed?

The repository itself is **not peer-reviewed** (it's a preprint). However:
- All proofs are **machine-checked** (by proof assistants)
- Code is **open source** and reproducible
- We invite **community review** via GitHub

We plan to submit the book as a monograph to academic publishers.

### Q19: What license is this under?

**Dual licensing**:
- **Text/Documentation**: CC BY 4.0 (open access, requires attribution)
- **Code**: MIT License (permissive open source)

See `LICENSE_TEXT.md` and `LICENSE_CODE.md`.

---

## Philosophical Questions

### Q20: Why formalize ancient scripts?

**Reasons**:
1. **Rigor**: Formal methods force precise claims
2. **Reproducibility**: Others can verify our work
3. **Generality**: Frameworks apply beyond one script
4. **Honesty**: Math doesn't allow overclaiming

### Q21: Isn't this too abstract to be useful?

**No.** Abstraction is **useful** because:
- It reveals **structural patterns** across systems
- It provides **falsifiable predictions**
- It enables **computational analysis**
- It avoids **speculative phonetic claims**

### Q22: Will this ever lead to "reading" the Indus script?

**Unknown.** Our framework could:
- Help identify **structural patterns** that constrain interpretations
- Provide **computational tools** for testing hypotheses
- Offer **comparative insights** from other systems

But phonetic decipherment requires **bilingual texts** or other evidence we lack.

---

## Data Questions

### Q23: Where does your data come from?

All sources are documented in `data/provenance/sources.yml`. Primary sources include:
- Archaeological catalogs
- Published sign lists
- Frequency analyses from academic papers

We respect copyright and fair use.

### Q24: Can I use your data?

**Yes**, with attribution. Derived data in `data/derived/` is licensed under **CC BY 4.0**. See provenance files for original source restrictions.

### Q25: How accurate is your data?

We document:
- Source accuracy (catalog vs. excavation)
- Processing methods (scripts in `code/scripts/`)
- Uncertainty levels (where applicable)

We **do not claim perfect data**. All limitations are documented.

---

## Future Work

### Q26: What's next?

**Version 1.1** (planned):
- Extended symbol catalog (45-200)
- Additional comparative systems (Sumerian, Egyptian)
- Machine learning pattern discovery

**Version 2.0** (future):
- Full corpus analysis
- Cross-site statistical validation
- Collaboration with archaeological teams

### Q27: Can I collaborate?

**Yes!** Open an issue or discussion to propose:
- Extensions to other scripts
- Improved formal models
- Additional proof assistant implementations
- Data quality improvements

---

## Misunderstandings

### Q28: So you've "solved" the Indus script?

**NO.** We've developed a **formal framework** for analysis. We have **not solved, cracked, or deciphered** the script phonetically.

### Q29: Can I now read what Indus seals say?

**NO.** We cannot provide:
- Phonetic readings
- Word-by-word meanings
- Historical interpretations

### Q30: Is this "just" mathematics, with no real-world application?

The mathematics is **foundational** for:
- Future computational analysis
- Rigorous hypothesis testing
- Cross-cultural comparisons
- Falsifiable predictions

It's not "just" math—it's **necessary** math for responsible research.

---

## Contact

Still have questions?

- **GitHub Discussions**: For conceptual questions
- **Issues**: For specific technical questions
- **Email**: [To be added]

---

**Last Updated**: 2026-02-03  
**Version**: 1.0.0
