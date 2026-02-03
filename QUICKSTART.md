# Quick Start Guide

## Getting Started with Indus Operational Mathematics

This guide will help you quickly understand and use the Harappan Operational System implementation.

---

## Installation

No installation required! The core implementation uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Verify Python version (3.8+)
python --version
```

---

## 5-Minute Tutorial

### 1. Validate Your First Sequence

```python
# Navigate to the repo root
cd /path/to/indus-operational-mathematics

# Run the automaton
python implementation/parser/indus_automaton.py
```

**Output:**
```
Sequence [373, 342]: VALID
Sequence [373, 410, 342]: VALID
Sequence [373, 410]: INVALID
  Error: Sequence does not end in accepting state
```

### 2. Convert a Sequence to JSON

```python
python implementation/converter/harappan_to_json.py
```

**Output:**
```json
{
  "entity": "basic_token",
  "qualifiers": [],
  "quantity": 3,
  "relations": [],
  "closure": "simple"
}
```

### 3. Use the Validator

```python
python implementation/validator/indus_validator.py
```

See detailed validation results with error messages and state traces.

---

## Understanding the System

### Core Concept

The Indus script is a **finite-state automaton** with 6 states:

```
S0 (Initial) → S1 (Entity) → S2 (Qualified) → S3 (Quantified) 
                                ↓                      ↓
                            S4 (Related) ────────> S5 (Closed) ✓
```

### Valid Sequence Pattern

```
[ENTITY] [QUALIFIERS*] [QUANTITIES*] [RELATIONS*] [CLOSURE]
   ↑                                                   ↑
 Required                                         Required
```

### Example Breakdown

```python
sequence = [373, 410, 411, 400, 342]

# Step by step:
# [373]         → Entity: Basic Token (S0 → S1)
# [410]         → Count: 1 (S1 → S3)
# [411]         → Count: 2 (S3 → S3)  Total: 3
# [400]         → Relation: Pair (S3 → S4)
# [342]         → Closure: Simple (S4 → S5) ✓ Valid!
```

---

## Common Use Cases

### Case 1: Create and Validate a Simple Record

```python
from implementation.parser.indus_automaton import validate_indus_sequence

# Simple administrative record
sequence = [373, 342]  # Entity + Closure
is_valid, error = validate_indus_sequence(sequence)

print(f"Valid: {is_valid}")  # True
```

### Case 2: Create a Quantified Record

```python
# Record with quantity
sequence = [200, 415, 343]  # Unicorn + 10 + Confirmed
is_valid, error = validate_indus_sequence(sequence)

print(f"Valid: {is_valid}")  # True
```

### Case 3: Detailed Validation

```python
from implementation.validator.indus_validator import IndusValidator

validator = IndusValidator()
sequence = [373, 410, 400, 342]

result = validator.validate_with_details(sequence)

print(f"Valid: {result['is_valid']}")
print(f"State: {result['final_state']}")
print(f"Classes: {result['symbol_classes']}")
```

### Case 4: Convert to JSON

```python
from implementation.converter.harappan_to_json import harappan_to_json

sequence = [200, 410, 411, 343]
json_record = harappan_to_json(sequence)

print(json_record)
# {'entity': 'unicorn', 'quantity': 3, 'closure': 'confirmed', ...}
```

---

## Symbol Reference

### Entities (Start of Sequence)

| ID Range | Class | Examples |
|----------|-------|----------|
| 373-399 | Oval | Basic tokens, seals |
| 328-339 | Vessel | Containers |
| 250-260 | Authority | Staffs, scepters |
| 200-210 | Animal | Unicorn, bull, elephant |
| 100-150 | Metric | Measurement units |

### Operators (Middle of Sequence)

| ID Range | Class | Function |
|----------|-------|----------|
| 410-417 | Count | 1, 2, 3, 4, 5, 10, 20, 100 |
| 400-409 | Relation | Pair, hierarchy, exchange, etc. |

### Closures (End of Sequence)

| ID | Type | Meaning |
|----|------|---------|
| 342 | Simple | Basic closure |
| 343 | Confirmed | Validated |
| 344 | Validated | Double-checked |
| 345 | Sealed | Sealed record |
| 346 | Absolute | Highest authority |
| 347 | Hierarchical | Hierarchical validation |
| 348 | Terminal | Final closure |

---

## Testing Your Sequences

### Valid Patterns

```python
# Pattern 1: Entity + Closure
[373, 342]  # ✓ Valid

# Pattern 2: Entity + Count + Closure
[373, 410, 342]  # ✓ Valid

# Pattern 3: Entity + Count + Count + Closure
[373, 410, 411, 342]  # ✓ Valid (quantity = 3)

# Pattern 4: Entity + Relation + Closure
[373, 400, 342]  # ✓ Valid

# Pattern 5: Entity + Count + Relation + Closure
[373, 410, 400, 342]  # ✓ Valid
```

### Invalid Patterns

```python
# No closure
[373, 410]  # ✗ Invalid

# Closure first
[342, 373]  # ✗ Invalid

# No entity
[410, 342]  # ✗ Invalid

# Wrong order
[373, 400, 410, 342]  # ✗ Invalid (relation before count)
```

---

## Visualization

### Generate Diagrams

```python
cd implementation/simulator
python automaton_visualizer.py
```

This generates:
- `automaton.dot` - Graphviz format
- `automaton_diagram.md` - Mermaid diagram
- `transition_table.txt` - Transition matrix

### View ASCII Art

```python
from implementation.simulator.automaton_visualizer import AutomatonVisualizer

viz = AutomatonVisualizer()
print(viz.generate_ascii_art())
```

---

## Data Files

### Signs Catalog
```bash
cat data/signs.csv
```

48 key symbols with IDs, classes, descriptions, and frequencies.

### Bigrams (Co-occurrences)
```bash
cat data/bigrams.csv
```

Symbol pair frequencies showing which symbols commonly appear together.

### Frequencies
```bash
cat data/frequencies.csv
```

Distribution data across different media (seals, tablets, pottery).

---

## Advanced Usage

### Create Custom Sequences Programmatically

```python
from implementation.parser.indus_automaton import IndusAutomaton, SymbolClass

automaton = IndusAutomaton()

# Build sequence step by step
automaton.process_symbol(SymbolClass.ENT_OVAL)
automaton.process_symbol(SymbolClass.OP_COUNT)
automaton.process_symbol(SymbolClass.OP_COUNT)
automaton.process_symbol(SymbolClass.OP_CLOSE)

# Check if valid
if automaton.is_valid_record():
    print("Valid sequence!")
    print(f"Current state: {automaton.get_current_state()}")
```

### Batch Processing

```python
from implementation.converter.harappan_to_json import HarappanToJsonConverter

converter = HarappanToJsonConverter()

sequences = [
    [373, 342],
    [200, 410, 343],
    [328, 415, 346]
]

records = converter.batch_convert(sequences)
for record in records:
    print(record.to_json())
```

---

## Next Steps

1. **Read the Paper**: See `publications/paper/indus_operational_system.md`
2. **Explore Formal Model**: See `formal_model/automata/finite_automaton.md`
3. **Study Comparisons**: See `comparisons/festos/phaistos_comparison.md`
4. **Try Blockchain**: See `implementation/converter/IndusRecord.sol`

---

## Getting Help

- **Documentation**: Read the full README.md
- **Examples**: See `data/example_sequences.md`
- **Issues**: Report problems on GitHub
- **Questions**: Open a discussion on GitHub

---

## Quick Reference Card

```
VALID SEQUENCE STRUCTURE:
[Entity (100-399)] [Operators] [Closure (342-348)]

STATES:
S0 → S1 → S2/S3/S4 → S5
     ENT  OPS       CLOSE

RULES:
1. Must start with entity
2. Must end with closure
3. Operations in order: Qual → Count → Rel
4. Closure is final (no more symbols)

EXAMPLE:
[373, 410, 342] = "1 basic token, simple closure"
```

---

**Happy validating!** 🎉
