# Harappa Operational Mathematics - Complete Guide

## Introduction

The Harappa Operational Mathematics System is a formal framework inspired by the Indus Valley civilization's sophisticated symbolic systems. It provides a mathematically rigorous foundation for modern computational applications.

## Core Concepts

### 1. Symbols

Symbols are the basic building blocks representing entities, resources, transactions, states, or quantifiers.

**Symbol Types:**
- `ENTITY`: Represents an object or agent
- `RESOURCE`: Represents a resource
- `TRANSACTION`: Represents an action or transaction
- `STATE`: Represents a state
- `QUANTIFIER`: Represents a quantity or measurement

**Example:**
```python
from harappa import Symbol, SymbolType

# Create an entity symbol
user_symbol = Symbol(
    id="user_001",
    symbol_type=SymbolType.ENTITY,
    attributes={"name": "Alice", "role": "admin"}
)

# Validate the symbol
assert user_symbol.validate()
```

### 2. Operators

Operators perform transformations, qualifications, or validations on symbols.

**Operator Types:**
- `QUALIFICATION`: Adds properties or constraints
- `TRANSFORMATION`: Changes state
- `COMPOSITION`: Combines symbols
- `VALIDATION`: Validates correctness
- `CLOSURE`: Indicates completion

**Example:**
```python
from harappa import Operator, OperatorType

# Create a transformation operator
transfer_op = Operator(
    name="transfer",
    operator_type=OperatorType.TRANSFORMATION,
    arity=2,  # Operates on 2 symbols
    parameters={"amount": 100}
)
```

### 3. States

States represent computational states with associated symbols and properties.

**Example:**
```python
from harappa import State, Symbol, SymbolType

# Create a state
state = State()
state.add_symbol(Symbol("resource_1", SymbolType.RESOURCE))
state.properties["balance"] = 1000
state.properties["locked"] = False

# Validate the state
assert state.validate()
```

### 4. Records

Records are complete compositions of symbols and operators representing transactions, proofs, or processes.

**Example:**
```python
from harappa import Record, Symbol, Operator, SymbolType, OperatorType

# Create a record
record = Record()
record.add_symbol(Symbol("item_1", SymbolType.RESOURCE))
record.add_operator(Operator("process", OperatorType.TRANSFORMATION, 1))
record.close()  # Mark as complete

# Validate
assert record.validate()
assert record.has_closure
```

### 5. Validation Engine

Ensures formal correctness and adherence to system rules.

**Example:**
```python
from harappa import ValidationEngine, Record

engine = ValidationEngine()

# Add custom validation rule
def check_minimum_symbols(record):
    return len(record.symbols) >= 1

engine.add_rule(check_minimum_symbols)

# Validate a record
is_valid = engine.validate_record(record)
if not is_valid:
    print(f"Errors: {engine.get_errors()}")
```

## Application Domains

### Proposal 1: Formal Specification Language

Create formal specifications for smart contracts and protocols.

**Key Features:**
- State machine definition
- Determinism checking
- Termination guarantees
- Pre/post conditions

**Example: Token Transfer Contract**
```python
from harappa.spec_lang import HarappaSpec, Transition

spec = HarappaSpec()
sm = spec.create_state_machine("TokenTransfer")

# Define states
sm.add_state("initial", State())
sm.add_state("verified", State())
sm.add_state("completed", State())
sm.add_final_state("completed")

# Define transitions
sm.add_transition(Transition("initial", "verified", verify_op))
sm.add_transition(Transition("verified", "completed", execute_op))

# Validate
print(f"Deterministic: {sm.is_deterministic()}")
print(f"Terminates: {sm.has_termination_guarantee()}")
```

### Proposal 2: Universal Unique Identification

Create hierarchical, semantically rich identifiers.

**Key Features:**
- Hierarchical structure
- Semantic metadata encoding
- Checksum validation
- Parent-child relationships

**Example: Supply Chain UID**
```python
from harappa.uid import HarappaUID, UIDType, UIDRegistry

registry = UIDRegistry()

# Create shipment UID
shipment = HarappaUID(UIDType.ASSET, "supply_chain")
shipment.add_symbol(Symbol("SHIP_001", SymbolType.ENTITY))
shipment.encode_metadata("origin", "Mumbai")
shipment_id = registry.register(shipment)

# Create child package UID
package = HarappaUID(UIDType.ASSET, "supply_chain")
package.set_parent(shipment)
package_id = registry.register(package)

# Query
children = registry.find_children(shipment)
print(f"Shipment has {len(children)} packages")
```

### Proposal 3: Theorem Verification

Computer-assisted theorem proving with diagrammatic steps.

**Key Features:**
- Diagrammatic proof steps
- Closure-based completion
- Proof verification
- Axiom management

**Example: Simple Proof**
```python
from harappa.proof import ProofSystem, Theorem, DiagrammaticProofBuilder

ps = ProofSystem()

# Define theorem
theorem = Theorem(
    name="Transitivity",
    statement=Symbol("A_implies_C", SymbolType.STATE)
)
ps.add_theorem(theorem)

# Build proof
builder = DiagrammaticProofBuilder(ps, theorem)
builder.assume(Symbol("A", SymbolType.STATE), "Assumption")
builder.apply(modus_ponens_op, "Apply modus ponens")
proof = builder.conclude(theorem.statement, "Conclusion")

print(f"Proof valid: {proof.verify()}")
```

### Proposals 4-15: Additional Applications

The `harappa.applications` module provides implementations for:

- **Archaeological Simulation**: Agent-based modeling of trade networks
- **Visual Programming**: Drag-and-drop programming interface
- **Educational System**: Logic and mathematics education
- **AI Metadata**: Dataset and model annotation
- **Semantic Database**: Knowledge representation
- **Communication System**: Low-bandwidth messaging
- **DAO Governance**: Decentralized decision-making
- **Ancient Text Search**: Structural pattern matching
- **Art Generator**: Rule-based art generation
- **Authentication**: Password-less authentication
- **Service Choreography**: Web service orchestration
- **Risk Analysis**: Project risk assessment

See the examples directory for detailed usage of each application.

## Best Practices

### 1. Always Close Records

```python
record = Record()
# ... add symbols and operators
record.close()  # Mark as complete
assert record.validate()
```

### 2. Validate State Transitions

```python
engine = ValidationEngine()
valid = engine.validate_state_transition(from_state, to_state, operator)
```

### 3. Use Type Checking

```python
from harappa import SymbolType, OperatorType

# Always use enum types
symbol = Symbol("id", SymbolType.ENTITY)  # Good
# symbol = Symbol("id", "entity")  # Bad - string instead of enum
```

### 4. Implement Custom Rules

```python
engine = ValidationEngine()

def custom_rule(record):
    # Your validation logic
    return len(record.symbols) > 0

engine.add_rule(custom_rule)
```

## API Reference

See the inline documentation in each module for complete API details:

- `harappa.core`: Core components
- `harappa.spec_lang`: Specification language
- `harappa.uid`: UID system
- `harappa.proof`: Proof system
- `harappa.applications`: Application modules

## Performance Considerations

### Symbol Lookups
- Symbols use hash-based equality for O(1) lookup
- Use sets for collections of symbols

### State Machines
- State transition checking is O(n) where n is the number of transitions
- Consider caching transition lookups for frequently used state machines

### UID Registry
- Uses indexed lookups for O(1) retrieval by UID string
- Type and context indexes provide O(1) filtering

## Troubleshooting

### Common Issues

**Issue**: `ImportError: cannot import name 'SymbolType'`
**Solution**: Import from the correct module:
```python
from harappa import SymbolType  # Correct
# from harappa.core import SymbolType  # Also works
```

**Issue**: Record validation fails
**Solution**: Ensure the record has closure:
```python
record.close()  # Don't forget this!
```

**Issue**: State machine termination check fails
**Solution**: Add final states:
```python
sm.add_final_state("completed")
```

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for guidelines.

## License

MIT License - see LICENSE file for details.
