# TCOP Examples

This directory contains detailed examples demonstrating the TCOP theorem applied to real-world graphic systems.

## Examples

### 1. harappan_detailed.py

Detailed analysis of Harappan script using TCOP framework.

**Run:**
```bash
python harappan_detailed.py
```

**Features:**
- 10 base symbols across 5 ontological classes (animal, container, botanical, geometric, human)
- 12 systematic operators (strokes, enclosures, positions, terminals)
- Simulated corpus with realistic frequency distribution
- Demonstrates:
  - TCOP validation (all conditions satisfied)
  - Zipf-like frequency distribution (α ≈ 0.96)
  - Terminal sign patterns
  - Short inscription explanation

**Key Results:**
- |B| = 10, |Σ| = 38 (3.8:1 ratio)
- 100% of recorded states are terminal (validation function)
- Frequency pattern matches Zipf distribution
- Supports ledger/administrative interpretation

### 2. chinese_radicals.py

Analysis of Ancient Chinese radical composition using TCOP.

**Run:**
```bash
python chinese_radicals.py
```

**Features:**
- 11 base radicals across 7 ontological classes
- 10 compositional operators (duplication, position, enclosure, etc.)
- Real Chinese character examples (从, 林, 众, 明, etc.)
- Demonstrates:
  - Corollary 1: Radicals as ontological classes
  - Character formation as state transitions
  - Compositional emergence of meaning
  - Non-phonetic operational structure

**Key Results:**
- |B| = 11, |Σ| = 41 (3.7:1 ratio)
- TCOP conditions satisfied
- Validates Corollary 1: 人 (rén) as agent class with variable states
- Shows graphical operators precede phonetic encoding

## Understanding the Output

### TCOP Validation Checklist

Both examples validate TCOP conditions:

✓ **C1: Recurrence** - Base symbols appear consistently
✓ **C2: Systematicity** - Base symbols admit modifications  
✓ **C3: Compositionality** - Modifications are systematic
✓ **C4: Regularity** - Statistical patterns present

✓ **H1: Finiteness** - |B| ≪ |Σ| (ratio > 3:1)
~ **H5: Distribution** - Zipf-like (α may vary by example)

### Frequency Analysis

Examples show realistic frequency distributions:
- Small number of very common combinations
- Long tail of rare combinations
- Characteristic of finite operational systems

### Terminal States

Terminal states marked with ✓ represent:
- Complete/validated symbols
- Accepting states in the automaton
- Closure operators from Hypothesis 4

## Extending the Examples

To create your own TCOP analysis:

1. **Define base symbols** (ontological classes)
```python
base = BaseSymbol("id", "Name", "class_name")
system.add_base_symbol(base)
```

2. **Define operators** (graphical modifications)
```python
op = Operator("id", "Name", OperatorType.MODIFICATION, "Description")
system.add_operator(op)
```

3. **Generate states** (compositions)
```python
state = system.get_state_by_composition("base_id", ["op1", "op2"])
system.record_occurrence(state)
```

4. **Validate TCOP**
```python
results = TCOPValidator.validate_system(system)
```

## Comparative Analysis

| Property | Harappan | Chinese | Expected for TCOP |
|----------|----------|---------|-------------------|
| |B| | 10 | 11 | Finite |
| |Σ| | 38 | 41 | > 3×|B| |
| Ratio | 3.8:1 | 3.7:1 | > 3:1 ✓ |
| Zipf α | 0.958 | 0.313 | [0.8, 1.2] |
| Terminal % | 100% | 100% | High |
| TCOP satisfied | ✓ | ✓ | Yes |

Both systems satisfy core TCOP conditions despite:
- Different historical periods
- Different geographical regions
- Different cultural contexts
- No direct transmission

This supports **Corollary 3**: Cognitive Universal - shared cognitive substrate under common constraints.

## Research Applications

These examples can be extended for:

1. **Corpus Analysis**: Apply to full historical corpora
2. **Comparative Studies**: Cross-system structural comparison
3. **Decipherment Tools**: Structural analysis of undeciphered scripts
4. **Cognitive Research**: Study of graphical cognition
5. **Historical Linguistics**: Pre-phonetic writing systems

## References

- Main theory: `../tcop_theorem.tex`
- Computational model: `../tcop_model.py`
- Proof visualization: `../PROOF_VISUALIZATION.md`

## Contributing

To add new examples:
1. Follow the pattern in existing examples
2. Include real or well-researched corpus data
3. Document all base symbols and operators
4. Run TCOP validation
5. Explain results in context of the theorem

---

**Note:** These examples use simplified corpus data for demonstration. For research purposes, use complete historical corpora with archaeological validation.
