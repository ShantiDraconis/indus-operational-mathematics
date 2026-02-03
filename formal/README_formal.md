# Formal Verification - Indus Operational Mathematics

This directory contains formal verification of the axioms A1-A5 and the TCOP theorem in multiple proof assistants.

## Why Multiple Proof Assistants?

Different proof assistants offer complementary strengths:

| System | Strength | Use Case |
|--------|----------|----------|
| **Lean 4** | Modern syntax, tactics, computation | Main development, algorithms |
| **Coq** | Mature ecosystem, large libraries | Validation, established techniques |
| **Isabelle/HOL** | Powerful automation (Sledgehammer) | Exploration, discovery |
| **Agda** | Dependent types, constructive | Constructive proofs, type theory |

Using **all four** increases confidence in our formalization—if all independently verify the same theorems, we have strong evidence of correctness.

## Directory Structure

```
formal/
├── lean/                   # Lean 4 implementation
│   ├── IndusOperationalMathematics.lean
│   ├── lakefile.lean       # Build configuration
│   └── lean-toolchain      # Version specification
├── coq/                    # Coq implementation
│   ├── IndusOperationalMathematics.v
│   ├── _CoqProject         # Project configuration
│   └── Makefile            # Build automation
├── isabelle/               # Isabelle/HOL implementation
│   ├── IndusOperationalMathematics.thy
│   └── ROOT                # Session configuration
├── agda/                   # Agda implementation
│   ├── IndusOperationalMathematics.agda
│   └── IndusOperationalMathematics.agda-lib
└── README_formal.md        # This file
```

## Installation & Setup

### Lean 4

**Install**: Via [elan](https://github.com/leanprover/elan)
```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
cd formal/lean/
lake build
```

**Documentation**: https://leanprover.github.io/lean4/doc/

### Coq

**Install**: Via [opam](https://opam.ocaml.org/)
```bash
opam install coq
cd formal/coq/
make
```

**Documentation**: https://coq.inria.fr/

### Isabelle

**Install**: Download from [isabelle.in.tum.de](https://isabelle.in.tum.de/)
```bash
# After download and extraction:
export PATH=$PATH:/path/to/Isabelle2023/bin
cd formal/isabelle/
isabelle build -D .
```

**Documentation**: https://isabelle.in.tum.de/documentation.html

### Agda

**Install**: Via [cabal](https://www.haskell.org/cabal/)
```bash
cabal update
cabal install Agda
cd formal/agda/
agda --safe IndusOperationalMathematics.agda
```

**Documentation**: https://agda.readthedocs.io/

## Verification Status

| Component | Lean | Coq | Isabelle | Agda |
|-----------|------|-----|----------|------|
| Axiom A1 | ✅ | ✅ | ✅ | ✅ |
| Axiom A2 | ✅ | ✅ | ✅ | ✅ |
| Axiom A3 | ✅ | ✅ | ✅ | ✅ |
| Axiom A4 | ✅ | ✅ | ✅ | ✅ |
| Axiom A5 | ✅ | ✅ | ✅ | ✅ |
| TCOP Theorem | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Corollaries | ⚠️ | ⚠️ | ⚠️ | ⚠️ |

**Legend**:
- ✅ Fully verified
- ⚠️ Stated, partial proof (some `sorry`/`admit`/`sorry`)
- ❌ Not yet implemented

## Key Definitions

### Symbol Classes (A1)

All implementations define:
```
SymbolClass = Quantifier | Entity | Modifier | Operator | Terminal
```

### Composition (A2, A3)

Partial function:
```
compose : Symbol → Symbol → Option Symbol
```

### Compatibility (A3)

```
compatible(Quantifier, Entity) = true
compatible(Entity, Modifier) = true
compatible(Entity, Operator) = true
compatible(Entity, Terminal) = true
compatible(_, _) = false
```

### Terminal Closure (A4)

```
∀ t s. class(t) = Terminal ⟹ compose(t, s) = None
```

### Layering (A5)

```
layer(Quantifier) = 0
layer(Entity) = 0
layer(Modifier) = 1
layer(Operator) = 2
layer(Terminal) = 3
```

## TCOP Theorem Statement

In all systems:

```
∀ sys : OperationalSystem,
∀ seq : List Symbol,
  ValidSequence(sys, seq) ⟹
  (1) ∃! st : State. eval(sys, seq) = Some st
  (2) ∀ s1 s2. compose(s1, s2) defined ⟹ result ∈ symbols
  (3) Composition is closed
  (4) Terminal enforcement
```

## Proof Strategy

### Part 1: State Well-Definedness

**Key Lemma**: Evaluation is deterministic.

**Proof**: By induction on sequence length, using A1-A5 to show each step is unique.

### Part 2: Operational Closure

**Key Lemma**: A2 ensures composed symbols remain in system.

**Proof**: Direct from axiom A2.

### Part 3: Compositional Closure

**Key Lemma**: Composition is associative where defined.

**Proof**: By case analysis on symbol classes and A3 compatibility.

### Part 4: Terminal Enforcement

**Key Lemma**: A4 prevents composition after terminals.

**Proof**: Direct from axiom A4.

## Current Limitations

### Partial Proofs

Some theorems use:
- Lean: `sorry`
- Coq: `Admitted`
- Isabelle: `sorry`
- Agda: `postulate`

These indicate **statements we believe true** but haven't fully proven yet.

### Why Partial?

1. **Time constraints**: Full mechanization is time-intensive
2. **Library gaps**: Some needed lemmas not in standard libraries
3. **Complexity**: Full TCOP proof requires extensive case analysis

### Future Work

- Complete TCOP proofs in all systems
- Add corollaries (decidability, parsing, etc.)
- Formalize extended symbol catalog (45-417)
- Prove equivalence between implementations

## Running Verification

### Continuous Integration

GitHub Actions automatically verifies all proof assistants on push:

See `.github/workflows/formal-verification.yml`

### Local Testing

**All systems**:
```bash
cd formal/
./verify_all.sh  # Runs all verifiers
```

**Individual systems**:
```bash
# Lean
cd lean/ && lake build

# Coq
cd coq/ && make

# Isabelle
cd isabelle/ && isabelle build -D .

# Agda
cd agda/ && agda --safe IndusOperationalMathematics.agda
```

## Extending the Formalization

### Adding New Axioms

1. Add to all four implementations
2. Update interdependencies
3. Verify CI passes
4. Document in model/axioms/

### Adding New Theorems

1. State in all systems
2. Prove in at least one (preferably all)
3. Add to documentation
4. Update verification status table

## Resources

### Learning Proof Assistants

- **Lean**: *Theorem Proving in Lean 4* (online book)
- **Coq**: *Software Foundations* series
- **Isabelle**: *Concrete Semantics*
- **Agda**: *Programming Language Foundations in Agda*

### Community

- **Lean**: Zulip chat
- **Coq**: Discourse forum
- **Isabelle**: Mailing list
- **Agda**: IRC channel

## Questions?

- **Technical issues**: Open GitHub issue
- **Proof strategies**: GitHub Discussions
- **Contributions**: See CONTRIBUTING.md

---

**Maintained By**: Project maintainers  
**Last Updated**: 2026-02-03  
**Verification Version**: 1.0.0
