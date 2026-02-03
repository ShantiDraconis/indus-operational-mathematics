# Glossary of Terms

## Core Concepts

### Operational System
A writing system optimized for encoding state transformations and institutional validation rather than phonetic transcription of speech. Characterized by:
- Mandatory closure operators
- Limited symbol vocabulary
- Focus on entities and their transformations
- Administrative/institutional contexts

**Example**: Harappan script, Phaistos Disc

### Descriptive System
A writing system that combines operational and phonetic elements to create narrative texts. Characterized by:
- Optional closure
- Large symbol vocabulary
- Phonetic components
- Narrative capability

**Example**: Egyptian hieroglyphs, ancient Chinese

### Magical System
A writing system used primarily for ritual, divination, or mystical purposes. Characterized by:
- Abstract symbolic forms
- Flexible composition
- Mystical interpretation
- Non-institutional contexts

**Example**: Nordic Runes

## Theoretical Terms

### Functional Isomorphism
The phenomenon where different systems develop similar functional structures to solve similar cognitive problems, even without historical contact.

**Example**: All systems use vertical strokes for counting (1, 2, 3) because it's cognitively natural.

### State Transformation
The fundamental operation in operational writing where a symbol acts as a function that transforms a previous state into a new state.

**Mathematical notation**: `f: State_n → State_n+1`

**Example**: Human(exists) + dot → Human(instantiated)

### Closure Operator
A symbol or set of symbols that terminates a sequence and validates its contents, similar to a seal or signature on a document.

**Harappan**: Symbols 341, 342, 343
**Egyptian**: Cartouche boundary
**Digital analogy**: Database COMMIT statement

### Universal Grammar
The proposed set of ~45 fundamental semantic operations that underlie all ancient writing systems, based on cognitive constraints and common institutional needs.

**Not to be confused with**: Chomsky's universal grammar for spoken language

## Symbol Categories

### Cardinal Operator
A symbol representing quantity or counting. Usually formed by repetition of a basic mark.

**Examples**: 
- Harappan: 1 (│), 2 (││), 3 (│││)
- Chinese: 一, 二, 三
- Runic: ᚠ, ᚢ, ᚦ (numerological values)

### Entity Operator
A symbol representing a concrete object, being, or concept that can undergo transformations.

**Examples**:
- Human: 26, 人, 𓀾, ᛗ
- Fish: Harappan fish, 魚, 𓆛
- House: Harappan house, 家, 𓉐, ᛟ

### Modifier Operator
A symbol or graphical element that transforms an entity's state by adding attributes, constraints, or qualities.

**Types**:
- **Instantiation**: Dot (•) - makes specific
- **Qualification**: Stroke (—) - adds attribute
- **Elevation**: Crown (△) - adds authority
- **Containment**: Enclosure (□) - restricts/bounds

### Relational Operator
A symbol that creates connections or relationships between entities.

**Examples**:
- Cross (X): Exchange, intersection
- Duplication: Two of same symbol
- Adjacency: Sequential placement

## Grammatical Terms

### Base State
The initial, unmarked form of an entity operator, representing pure existence without modifications.

**Example**: Harappan 26 = "Human exists" (before any transformations)

### Compound Symbol
A symbol formed by combining a base symbol with modifiers, creating a new semantic unit.

**Examples**:
- Harappan 27: 26 (human) + dot
- Chinese 囚: 人 (person) + 口 (enclosure)
- Runic Bindrune: ᛗ + ᚠ (Mannaz + Fehu)

### Sequence
An ordered series of symbols that encodes a complete statement or validation.

**Structure**: `Entity → Modifier* → Relational* → Closure?`

**Example**: `26 - 1 - 343` = "Human + unity + validated"

### Compositional Semantics
The principle that the meaning of a sequence is computed by applying each symbol's transformation function in order.

**Formula**: `Meaning(s₁⊕s₂⊕s₃) = f₃(f₂(f₁(State₀)))`

## State Categories

### Existential State (S₁)
The state where an entity exists but has no additional attributes or specifications.

**Symbol**: Base entity operators (26, 人, ᛗ)
**Meaning**: "An X exists"

### Instantiated State (S₂)
The state where an entity is specified as a particular instance.

**Transformation**: Entity + dot/mark
**Examples**: 26→27, 人→个, ᛗ→ᛗ+ᚠ
**Meaning**: "A specific X"

### Qualified State (S₃)
The state where an entity has acquired attributes or qualities.

**Transformation**: Entity + stroke/qualifier
**Examples**: 26→28, 人→大, ᛗ→ᛗ+ᚢ
**Meaning**: "An X with property Y"

### Quantified State (S₄)
The state where an entity is associated with a specific quantity.

**Transformation**: Entity + cardinal
**Examples**: 26+3, 三人, ᛗ+ᚦ
**Meaning**: "N instances of X"

### Related State (S₅)
The state where an entity is in relation to another entity.

**Transformation**: Entity + Entity + relation_marker
**Examples**: 26+26+4, 人+人→从, ᛗ+ᛗ
**Meaning**: "X in relation to Y"

### Contextualized State (S₆)
The state where an entity is placed within boundaries or context.

**Transformation**: Entity + enclosure
**Examples**: 26+□→29, 人+口→囚, ᛗ+ᚺ
**Meaning**: "X within boundary/context"

### Authorized State (S₇)
The state where an entity is granted authority or elevated status.

**Transformation**: Entity + authority_marker
**Examples**: 26→30, 人→王, ᛗ+ᚨ
**Meaning**: "X with authority/power"

### Transcendent State (S₈)
The state where an entity is elevated to a divine or transcendent level.

**Transformation**: Entity + divine_marker
**Examples**: 26+△, 人→天, ᛗ+ᛋ
**Meaning**: "X in divine/elevated state"

## Analytical Methods

### Morphological Analysis
The study of symbol forms by breaking them into primitive graphical components.

**Primitives**: Point (•), line (—, │), diagonal (/, \), square (□), circle (○), triangle (△)

### Functional Analysis
The study of what symbols **do** in sequences rather than what they might "mean" semantically or phonetically.

**Question**: "How does this symbol transform the state?"

### Correspondence Analysis
The systematic comparison of symbols across different systems based on multiple dimensions (form, function, position, frequency, context).

**Scoring**: Weighted sum of dimension similarities → confidence level

### Co-occurrence Analysis
Statistical analysis of which symbols commonly appear together, revealing grammatical and semantic patterns.

**Method**: Count symbol pairs, compare to expected frequency, test significance

### Positional Analysis
Study of where symbols appear in sequences (initial, medial, final) to determine grammatical roles.

**Roles**: Entity markers (initial), modifiers (medial), closures (final)

## Symbol-Specific Terms

### Harappan 26
The "human base" operator in Harappan script, represented as an R-like or stick-figure form.

**Correspondences**: Chinese 人, Runic ᛗ, Egyptian 𓀾
**Function**: Entity operator for human beings
**Transformations**: 26→27 (instantiated), 26→28 (qualified), 26→30 (authorized)

### Harappan 343
The final closure/validation operator in Harappan script.

**Function**: Seals and validates institutional statements
**Context**: Appears at end of administrative sequences
**Analogy**: Digital signature, database commit

### Elder Futhark
The oldest form of the runic alphabet, consisting of 24 runes divided into three groups (ættir).

**Period**: 2nd-8th century CE
**Systems**: Germanic peoples of Northern Europe
**Characteristics**: Geometric, magical, flexible

### Bindrune
A ligature or compound symbol in runic writing where two or more runes are graphically combined.

**Function**: Combines the powers/meanings of component runes
**Example**: ᛗ + ᚠ overlaid → Man with wealth
**Harappan parallel**: Compound symbols like 29

### Cartouche
An oval/rectangular enclosure in Egyptian hieroglyphs used to surround royal names.

**Function**: Protection and validation of royal identity
**Parallel**: Harappan closure operators
**Symbol**: Rope loop - eternal protection

### Determinative
A non-phonetic symbol in Egyptian hieroglyphs that clarifies the semantic category of preceding phonetic signs.

**Function**: Context/category marker
**Example**: 𓀾 after name → human person
**Parallel**: Harappan modifiers?

## Historical/Archaeological Terms

### Indus Valley Civilization
Bronze Age civilization (3300-1300 BCE) in modern Pakistan and northwest India.

**Also called**: Harappan Civilization
**Major sites**: Harappa, Mohenjo-daro, Dholavira
**Script**: Undeciphered, ~400 unique signs

### Phaistos Disc
A disk of fired clay from Minoan Crete (~1700 BCE) with 45 unique symbols arranged in a spiral.

**Status**: Undeciphered
**Characteristics**: Stamped symbols, spiral pattern
**Theory**: Possible operational validation system

### Seal
A small carved object (typically stone) used to make impressions in clay for authentication.

**Harappan seals**: Typically square, ~2-3cm, with animal and script
**Function**: Administrative validation, property marking
**Modern parallel**: Signature, stamp

## Technical Terms

### Autómato (State Machine)
A computational model consisting of states and transitions between states triggered by inputs.

**Application**: Ancient scripts as state machines where symbols are transition functions

**Example**:
```
State₀ → [Symbol₁] → State₁ → [Symbol₂] → State₂ → [Closure] → Final
```

### Semântica Operacional (Operational Semantics)
A formal framework for defining the meaning of symbols as operations that transform program/system states.

**Application**: Define meaning of ancient symbols through their transformational effects

### BNF (Backus-Naur Form)
A notation for expressing formal grammars, showing the structure of valid sequences.

**Example**:
```
<sequence> ::= <entity> <modifier>* <closure>
```

### Type System
A formal system for categorizing symbols by the kinds of inputs they accept and outputs they produce.

**Application**: Ensuring grammatical correctness (e.g., modifiers must follow entities)

## Comparative Terms

### Cross-System Validation
The process of confirming a hypothesis about one system by checking for similar patterns in other systems.

**Strength**: Multiple independent systems showing same pattern → high confidence

### Triangulation
Using three or more systems to converge on a functional interpretation.

**Example**: If Harappan, Chinese, AND Runic all show human + dot → specific human, confidence is very high

### Correspondence Score
A numerical measure (0-1) of how well two symbols from different systems match across multiple dimensions.

**Interpretation**:
- >0.75: Strong correspondence
- 0.50-0.75: Moderate correspondence
- <0.50: Weak/coincidental

## Methodological Terms

### Corpus Analysis
Systematic study of all available texts in a writing system.

**Harappan corpus**: ~4000 inscriptions, mostly seals
**Methods**: Frequency analysis, pattern mining, co-occurrence

### Decipherment
The process of understanding a writing system.

**Traditional**: Finding phonetic values, translating to known language
**Operational**: Understanding functional grammar and state transformations

### Validation Context
The institutional or social setting where administrative validation occurs.

**Examples**: Trade agreements, property rights, official appointments, ritual authorization

## Symbols Reference

### Runic Alphabet (Selected)
- **ᚠ Fehu**: Cattle, wealth, prosperity
- **ᚢ Uruz**: Aurochs, strength, force
- **ᚦ Thurisaz**: Giant, thorn, conflict
- **ᚨ Ansuz**: God, divine power, communication
- **ᚱ Raidō**: Ride, journey, movement
- **ᚲ Kenaz**: Torch, knowledge, illumination
- **ᚷ Gebo**: Gift, exchange, partnership
- **ᚺ Hagalaz**: Hail, structure, containment
- **ᛁ Isa**: Ice, stagnation, isolation
- **ᛃ Jera**: Year, harvest, cycle
- **ᛉ Algiz**: Elk, protection, defense
- **ᛗ Mannaz**: Man, humanity, self
- **ᛋ Sowilo**: Sun, victory, success
- **ᛟ Othala**: Inheritance, home, property

### Chinese Characters (Selected)
- **一 (yī)**: One
- **二 (èr)**: Two
- **三 (sān)**: Three
- **人 (rén)**: Person, human
- **个 (gè)**: Individual, measure word
- **大 (dà)**: Big, great
- **王 (wáng)**: King, monarch
- **天 (tiān)**: Heaven, sky, day
- **囚 (qiú)**: Prisoner, confined
- **从 (cóng)**: Follow, accompany
- **众 (zhòng)**: Crowd, multitude
- **交 (jiāo)**: Exchange, intersect
- **之 (zhī)**: Of, to go, connection

### Egyptian Hieroglyphs (Selected)
- **𓏤**: Stroke (1)
- **𓏥**: Stroke (10)
- **𓀾**: Man standing
- **𓀿**: Man sitting
- **𓁂**: Man with hand to mouth
- **𓆛**: Fish
- **𓅃**: Bird
- **𓉐**: House/estate
- **𓈗**: Water ripple
- **𓇳**: Sun/Ra

## Abbreviations

- **H**: Harappan (e.g., H26 = Harappan symbol 26)
- **R**: Runic (e.g., R-Mannaz = Runic Mannaz)
- **Ch**: Chinese (e.g., Ch-人 = Chinese character for person)
- **Eg**: Egyptian (e.g., Eg-𓀾 = Egyptian man glyph)
- **Ph**: Phaistos (e.g., Ph-A19 = Phaistos symbol A19)
- **BNF**: Backus-Naur Form
- **PMI**: Pointwise Mutual Information
- **MW**: Measure Word (Chinese grammar)

---

## Usage Note

This glossary provides technical definitions for terms used throughout the comparative analysis. For practical examples of these concepts in action, see EXAMPLES.md. For methodology details, see METHODOLOGY.md.
