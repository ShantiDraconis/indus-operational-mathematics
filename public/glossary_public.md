# Public Glossary - Indus Operational Mathematics

**Simplified terminology for public understanding**

---

## Core Concepts

### State
A **configuration** or **context** in which a symbol or sequence exists. Think of it like a variable's value in programming.

**Example**: "The state is 'three entities authorized'" vs. "The state is 'one entity pending'".

### Operator
A **symbol or modification** that transforms one state into another. Like a function in mathematics: `f(x) = y`.

**Example**: The Chinese character 人 (person) can be transformed by adding 一 (one line) to create 大 (big). The operation "add 一" is the operator.

### Composition
The **combination** of multiple symbols or operations according to rules.

**Example**: 人 + 人 → 从 ("person" composed with "person" yields "follow")

### Closure
The property that **all valid operations stay within the system**—you never get an "undefined" result.

**Example**: In arithmetic with natural numbers, addition is closed (2 + 3 = 5, still a natural number), but subtraction is not (2 - 3 = -1, not a natural number). We claim symbol operations in operational systems are closed.

---

## Axiomatic System

### Axiom
A **fundamental rule** that we accept as true without proof. All other claims build on axioms.

**Example**: "Axiom A1: Every symbol belongs to exactly one semantic class."

### Theorem
A **claim** that can be **proven** from axioms using logical reasoning.

**Example**: "TCOP Theorem: All valid sequences produce well-defined states."

### Proof
A **step-by-step demonstration** that a theorem follows logically from axioms.

### Proof Assistant
A **computer program** that checks mathematical proofs for correctness. We use four: Lean, Coq, Isabelle, and Agda.

---

## Symbol Classes

### Quantifier
A symbol that specifies **how many** of something. Similar to numbers.

**Example**: In Harappan, symbols 1-10 might be quantifiers (one stroke, two strokes, etc.).

### Entity
A symbol representing a **thing** or **object** in some domain.

**Example**: Symbol 26 in Harappan (hypothesized to be like "person" in Chinese).

### Modifier
A symbol that **changes the property** of an entity without changing what it is.

**Example**: In Chinese, adding a "crown" element to 人 (person) creates a modified but still person-related concept.

### Terminal
A symbol that **ends a sequence**, like a period ends a sentence.

**Example**: In Harappan inscriptions, certain symbols appear exclusively at the end.

### Operator
A symbol that **combines or transforms** other symbols.

**Example**: In programming, `+` is an operator. In ancient scripts, graphical modifications play this role.

---

## Comparative Terms

### Radical (Chinese)
A **core component** of a Chinese character that often indicates meaning category.

**Example**: 人 (person radical) appears in many person-related characters.

### Determinative (Egyptian)
A symbol that **clarifies the category** of a word in Egyptian hieroglyphs, without being pronounced.

**Example**: A seated man determinative after a word indicates the word refers to a person or profession.

### Compositional
Describes a system where **complex meanings arise from combining simpler parts** according to rules.

**Example**: LEGO is compositional—you build complex structures from simple bricks following connection rules.

---

## Mathematical Terms (Simplified)

### State Space (Θ)
The **set of all possible states** in a system.

**Example**: If analyzing traffic lights, the state space is {red, yellow, green}.

### Transition
A **change** from one state to another.

**Example**: Traffic light transitions: red → green → yellow → red.

### Closed under Composition
If you **combine any two elements** using an operation, the result is **still in the system**.

**Example**: Natural numbers are closed under addition (1 + 2 = 3, still a natural number), but not subtraction (1 - 2 = -1, not a natural number).

### Finite State Automaton (FSA)
A **mathematical model** of computation with:
- A finite set of states
- Rules for transitioning between states
- An initial state and accepting states

**Example**: A vending machine is an FSA—it has states (idle, coin inserted, dispensing) and transitions (insert coin, select item).

---

## Operational Terms

### Base Symbol
The **simplest form** of a symbol, before any modifications.

**Example**: 人 (person) in Chinese is the base. 大 (big) is a modification of it.

### Graphical Modification
A **visual change** to a symbol that changes its meaning or function.

**Example**: Adding a horizontal stroke to 人 creates 大.

### State Transformation
The **process** of changing from one state to another via an operation.

**Example**: 
- Initial state: "generic entity"
- Apply operator: "add quantifier 3"
- Final state: "three entities"

---

## Research Terms

### Corpus
The **complete collection** of texts or inscriptions being studied.

**Example**: The Indus corpus consists of ~4,000 inscriptions on seals, pottery, etc.

### Provenance
The **origin and history** of data—where it came from, who collected it, when.

**Example**: "This frequency table comes from Table II of Farmer (2004), pages 45-47."

### Reproducibility
The ability for **others to repeat your analysis** and get the same results.

**Example**: Our code + data + instructions → anyone can regenerate our figures.

### Formal Verification
Using **computer programs** to mathematically prove claims are correct.

**Example**: We use proof assistants to verify our theorems are logically sound.

---

## Non-Technical Comparisons

### Like JSON
**JSON** is a data format where you have:
- Keys (like symbol classes)
- Values (like states)
- Nested structures (like composition)

Our framework models symbols similarly—as structured data, not phonetic strings.

### Like State Machines
A **state machine** (like a vending machine or traffic light) has:
- States (idle, active, etc.)
- Transitions (insert coin, timer expires)
- Rules (can't go from red to yellow directly)

Ancient symbol systems might work this way.

### Like LEGO
**LEGO bricks**:
- Have types (2x2, 2x4, etc.)
- Follow connection rules (studs fit into tubes)
- Compose into complex structures
- Are closed (any valid assembly is still LEGO)

Our axioms formalize similar ideas for symbols.

---

## What We DON'T Mean

### ❌ "Decipherment"
We do **NOT** mean:
- Finding phonetic values (sounds)
- Translating inscriptions word-by-word
- Revealing historical meanings

### ❌ "Language"
We do **NOT** necessarily mean:
- A spoken language
- Grammar in the linguistic sense
- Phonemes, morphemes, syntax

We use "language" loosely to mean "a system with rules."

### ❌ "Reading"
We do **NOT** mean:
- Pronouncing symbols aloud
- Understanding what ancient people "said"

We mean "analyzing structural patterns."

---

## Technical Abbreviations

### TCOP
**Total Closure of Operations Principle** - Our main theorem that all valid symbol sequences produce well-defined states.

### FSA
**Finite State Automaton** - A mathematical model with states and transitions.

### BNF
**Backus-Naur Form** - A notation for describing grammar rules.

### DFA
**Deterministic Finite Automaton** - An FSA where each state has exactly one transition per input.

### HOL
**Higher-Order Logic** - A formal logic system used in Isabelle/HOL.

---

## For Mathematicians

If you're already familiar with formal methods, here's the quick mapping:

- **State**: Element of a set Θ
- **Operator**: Function ω: Θ → Θ
- **Composition**: Function composition (ω₁ ∘ ω₂)
- **Closure**: ∀ ω ∈ Ω, ∀ θ ∈ Θ: ω(θ) ∈ Θ
- **Axioms**: First-order logic statements
- **TCOP**: Closure theorem + terminal enforcement

---

## Questions?

See [faq.md](faq.md) for more detailed explanations, or open a GitHub Discussion for conceptual questions.

---

**Last Updated**: 2026-02-03  
**Version**: 1.0.0
