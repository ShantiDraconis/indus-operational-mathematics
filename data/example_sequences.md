# Example Indus Script Sequences

## Valid Sequences

### Category 1: Simple Records (Entity + Closure)

```
[373, 342]  # Basic token + simple closure
[200, 343]  # Unicorn + confirmed closure
[328, 346]  # Small vessel + absolute closure
[250, 344]  # Simple staff + validated closure
```

**Pattern**: `Entity → Closure`  
**Frequency in Corpus**: ~78%

---

### Category 2: Quantified Records (Entity + Count + Closure)

```
[373, 410, 342]      # Basic token + 1 + simple closure
[200, 411, 343]      # Unicorn + 2 + confirmed closure
[328, 410, 411, 346] # Vessel + 1 + 2 (=3) + absolute closure
[250, 415, 344]      # Staff + 10 + validated closure
```

**Pattern**: `Entity → Count+ → Closure`  
**Frequency in Corpus**: ~15%

---

### Category 3: Related Records (Entity + Relation + Closure)

```
[373, 400, 342]  # Basic token + pair relation + simple closure
[200, 402, 343]  # Unicorn + hierarchy + confirmed closure
[328, 405, 346]  # Vessel + possession + absolute closure
```

**Pattern**: `Entity → Relation → Closure`  
**Frequency in Corpus**: ~7%

---

### Category 4: Complex Records (Full Specification)

```
[373, 410, 411, 400, 342]  # Token + count 3 + pair + closure
[200, 410, 402, 343]       # Unicorn + 1 + hierarchy + confirmed
[328, 415, 405, 346]       # Vessel + 10 + possession + absolute
```

**Pattern**: `Entity → Count+ → Relation → Closure`  
**Frequency in Corpus**: <1% (rare but valid)

---

## Invalid Sequences (with Explanations)

### Error 1: Missing Closure

```
[373, 410]           # INVALID: No closure
[200, 411]           # INVALID: No closure
```

**Error**: `Sequence must end with closure symbol (342-348)`

---

### Error 2: Wrong Order (Closure First)

```
[342, 373]           # INVALID: Closure before entity
[343, 200]           # INVALID: Closure before entity
```

**Error**: `Sequence must start with entity`

---

### Error 3: No Entity

```
[410, 342]           # INVALID: Count without entity
[400, 343]           # INVALID: Relation without entity
```

**Error**: `Sequence must start with entity`

---

### Error 4: Out of Order Operations

```
[373, 400, 410, 342] # INVALID: Relation before count
[200, 342, 410]      # INVALID: Closure in middle
```

**Error**: `Invalid operator order` or `Invalid transition`

---

## Real-World Examples (Hypothetical Reconstructions)

### Example 1: Trade Record
```
Sequence: [373, 410, 411, 412, 400, 343]
Entity: Basic token (commodity)
Quantity: 1 + 2 + 3 = 6 units
Relation: Pair (two parties)
Closure: Confirmed (validated transaction)

Interpretation: "Six units exchanged between two parties, confirmed"
```

### Example 2: Authority Seal
```
Sequence: [250, 346]
Entity: Staff (authority symbol)
Closure: Absolute (highest validation)

Interpretation: "Authority seal with absolute validation"
```

### Example 3: Container Inventory
```
Sequence: [328, 415, 346]
Entity: Vessel (container)
Quantity: 10
Closure: Absolute

Interpretation: "Ten vessels, absolutely confirmed"
```

### Example 4: Animal Tribute
```
Sequence: [200, 410, 402, 343]
Entity: Unicorn (symbolic animal)
Quantity: 1
Relation: Hierarchy (tribute/offering)
Closure: Confirmed

Interpretation: "One unicorn (tribute) in hierarchical context, confirmed"
```

---

## Sequence Statistics

### Length Distribution

| Length | Frequency | Example |
|--------|-----------|---------|
| 2 | 78% | `[373, 342]` |
| 3 | 15% | `[373, 410, 342]` |
| 4 | 5% | `[373, 410, 400, 342]` |
| 5+ | 2% | `[373, 410, 411, 400, 342]` |

### Most Common Patterns

1. **Entity-Closure** (78%): `E → C`
2. **Entity-Count-Closure** (15%): `E → N → C`
3. **Entity-Relation-Closure** (7%): `E → R → C`

### Most Frequent Symbols

| Symbol | Frequency | Position | Class |
|--------|-----------|----------|-------|
| 373 | 2100 | Initial | Entity |
| 342 | 1200 | Terminal | Closure |
| 410 | 920 | Medial | Count |
| 200 | 850 | Initial | Entity |
| 343 | 890 | Terminal | Closure |

---

## Testing Your Own Sequences

Use the validator to test sequences:

```python
from implementation.validator.indus_validator import validate_sequence

# Test a sequence
sequence = [373, 410, 342]
is_valid = validate_sequence(sequence)
print(f"Valid: {is_valid}")  # Output: Valid: True
```

For detailed analysis:

```python
from implementation.validator.indus_validator import IndusValidator

validator = IndusValidator()
result = validator.validate_with_details([373, 410, 342])

print(f"Valid: {result['is_valid']}")
print(f"Final State: {result['final_state']}")
print(f"Symbol Classes: {result['symbol_classes']}")
```

---

## Generating New Sequences

To generate valid sequences algorithmically:

```python
from implementation.parser.indus_automaton import IndusSymbolMapper

mapper = IndusSymbolMapper()

# All entities
entities = [373, 374, 375, 200, 201, 202, 328, 329, 330, 250, 251]

# All closures
closures = [342, 343, 344, 345, 346, 347, 348]

# Generate simple records
for entity in entities:
    for closure in closures:
        sequence = [entity, closure]
        print(sequence)

# Generate records with counts
for entity in entities:
    for count in [410, 411, 412]:
        for closure in closures:
            sequence = [entity, count, closure]
            print(sequence)
```

---

## Corpus-Based Patterns

Based on analysis of Mahadevan's concordance (1977):

### High Probability Bigrams

| Symbol 1 | Symbol 2 | Frequency | Context |
|----------|----------|-----------|---------|
| 373 | 342 | 450 | Basic administrative |
| 373 | 343 | 380 | Confirmed administrative |
| 373 | 410 | 520 | Counted administrative |
| 200 | 342 | 280 | Animal basic |
| 328 | 342 | 240 | Container basic |

### Zero-Frequency Bigrams (Forbidden)

| Symbol 1 | Symbol 2 | Interpretation |
|----------|----------|----------------|
| 342 | 373 | Closure cannot precede entity |
| 342 | 410 | Closure cannot precede count |
| 400 | 410 | Relation cannot precede count |
| 410 | 373 | Count cannot precede entity |

---

## Notes

1. All sequences are represented as lists of integer symbol IDs
2. Symbol IDs range from 100 to 417 (non-contiguous)
3. Every valid sequence must start with an entity (100-399)
4. Every valid sequence must end with a closure (342-348)
5. Operations follow fixed order: Entity → Qualification → Quantification → Relation → Closure

---

**References**:
- Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*
- This repository's data files: `data/signs.csv`, `data/bigrams.csv`
