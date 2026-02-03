# Harappa Operational Mathematics System

A comprehensive formal system based on Indus Valley (Harappan) civilization principles for modern computational applications.

## Overview

The Harappa Operational Mathematics System is a novel formal framework inspired by the symbolic and structural properties of the ancient Indus script. It provides a mathematically rigorous foundation for various modern applications, from smart contract specification to theorem proving, authentication systems, and beyond.

## Core Concepts

### Symbols
Basic units representing entities, resources, transactions, states, or quantifiers. Each symbol has a unique identifier and type.

### Operators
Transformations and qualifications that operate on symbols, including:
- **Qualification**: Adding properties or constraints
- **Transformation**: Changing states
- **Composition**: Combining symbols
- **Validation**: Ensuring correctness
- **Closure**: Indicating completion

### States
Computational states with associated symbols and properties, representing points in a computation or process.

### Records
Complete compositions of symbols and operators, representing transactions, proofs, or processes. Records have a closure indicator showing completion and validity.

## Implemented Proposals

This system implements 15 innovative proposals:

### 1. Formal Specification Language
Use Harappa for specifying smart contracts and formal protocols with guaranteed termination and non-ambiguity.
- State machine definition
- Formal verification
- Contract specification with pre/post conditions

### 2. Universal Unique Identification (Harappa-UID)
Hierarchical, semantically rich unique identifiers using symbol composition.
- Hierarchical structure
- Semantic encoding
- Applications in supply chain, legal documents, digital assets

### 3. Theorem Verification
Computer-assisted theorem proving with diagrammatic proofs.
- Proof step operators
- Closure-based proof completion
- Integration with proof assistants (Coq/Lean style)

### 4. Archaeological Simulation
Simulate Harappan trade networks and administrative structures.
- Agent-based modeling
- Network analysis
- Economic reconstruction

### 5. Visual Programming Interface
Drag-and-drop programming using Harappa symbols.
- Visual workflow creation
- Code generation
- Business process modeling

### 6. Educational System
Teach logic and mathematics using visual Harappa symbols.
- Interactive learning
- Visual state representation
- Historical context

### 7. AI Metadata Standard
Annotate AI datasets and models with provenance and quality information.
- Digital seals
- Provenance tracking
- Quality metrics

### 8. Semantic Database
Knowledge representation using Harappa ontology schema.
- Compact representation
- Non-ambiguous facts
- Structured queries

### 9. Low-Bandwidth Communication
Efficient communication for remote/emergency scenarios.
- Compact encoding
- Structured messages
- Priority queuing

### 10. DAO Governance
Decentralized decision-making with transparency.
- Proposal management
- Voting mechanisms
- Immutable records

### 11. Ancient Text Search
Semantic search for ancient texts based on structure.
- Pattern matching
- Structural indexing
- Cross-corpus analysis

### 12. Algorithmic Art Generation
Generate art using Harappa composition rules.
- Rule-based generation
- Structural meaning
- Valid records as artworks

### 13. Authentication Protocol
Password-less authentication using Harappa seals.
- Digital seals
- Permission encoding
- Identity verification

### 14. Web Service Choreography
Specify service orchestration using Harappa notation.
- Message flow specification
- Service composition
- Formal verification

### 15. Risk Analysis
Analyze complex projects using Harappa sequences.
- Dependency analysis
- Risk quantification
- Completion validation

## Installation

```bash
# Clone the repository
git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
cd indus-operational-mathematics

# Install in development mode
pip install -e .

# Or install from PyPI (when published)
pip install harappa
```

## Quick Start

### Example 1: Formal Specification

```python
from harappa import Symbol, Operator, State, SymbolType, OperatorType
from harappa.spec_lang import HarappaSpec, Transition

# Create a state machine for a token transfer
spec = HarappaSpec()
token_sm = spec.create_state_machine("TokenTransfer")

# Define states
initial = State(is_final=False)
token_sm.add_state("initial", initial)

transferred = State(is_final=True)
token_sm.add_state("transferred", transferred)
token_sm.add_final_state("transferred")

# Validate
print(f"Valid: {token_sm.validate()}")
print(f"Deterministic: {token_sm.is_deterministic()}")
print(f"Terminates: {token_sm.has_termination_guarantee()}")
```

### Example 2: Unique Identifiers

```python
from harappa import Symbol, SymbolType
from harappa.uid import HarappaUID, UIDType, UIDRegistry

# Create a UID for a supply chain asset
uid = HarappaUID(uid_type=UIDType.ASSET, context="supply_chain")
uid.add_symbol(Symbol("SHIPMENT_001", SymbolType.ENTITY))
uid.encode_metadata("origin", "Mumbai")

# Register in a registry
registry = UIDRegistry()
uid_string = registry.register(uid)
print(f"UID: {uid_string}")
```

### Example 3: Theorem Proving

```python
from harappa import Symbol, Operator, SymbolType, OperatorType
from harappa.proof import ProofSystem, Theorem, DiagrammaticProofBuilder

# Create proof system
ps = ProofSystem()

# Define theorem
theorem = Theorem(name="Transitivity", statement=Symbol("A_implies_C", SymbolType.STATE))
ps.add_theorem(theorem)

# Build proof
builder = DiagrammaticProofBuilder(ps, theorem)
builder.assume(Symbol("A", SymbolType.STATE), "Assumption")
# ... add more steps
proof = builder.conclude(theorem.statement, "By transitivity")

print(f"Proof complete: {proof.is_complete()}")
print(f"Proof valid: {proof.verify()}")
```

## Examples

The `examples/` directory contains comprehensive demonstrations:

- `example1_specification.py` - Smart contract specification
- `example2_uid.py` - Supply chain tracking with UIDs
- `example3_proof.py` - Logical theorem proving
- `example4_applications.py` - All 12 application domains

Run examples:
```bash
cd examples
python example1_specification.py
python example2_uid.py
python example3_proof.py
python example4_applications.py
```

## Project Structure

```
indus-operational-mathematics/
├── harappa/
│   ├── __init__.py          # Main package
│   ├── core.py              # Core symbols, operators, states
│   ├── spec_lang.py         # Formal specification language
│   ├── uid.py               # Unique identification system
│   ├── proof.py             # Theorem verification
│   └── applications.py      # Applications (proposals 4-15)
├── examples/
│   ├── example1_specification.py
│   ├── example2_uid.py
│   ├── example3_proof.py
│   └── example4_applications.py
├── tests/                   # Test suite
├── docs/                    # Documentation
├── setup.py                 # Package setup
└── README.md               # This file
```

## Documentation

Comprehensive documentation is available in the `docs/` directory:
- **Core Concepts**: Detailed explanation of symbols, operators, and states
- **API Reference**: Complete API documentation
- **Tutorials**: Step-by-step guides for each proposal
- **Theory**: Mathematical foundations and formal semantics

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_core.py

# Run with coverage
python -m pytest --cov=harappa tests/
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This system is inspired by the remarkable achievements of the Indus Valley civilization and their sophisticated symbolic systems. It demonstrates how ancient principles can inspire modern computational frameworks.

## Citation

If you use this system in academic work, please cite:

```bibtex
@software{harappa2026,
  title={Harappa Operational Mathematics System},
  author={Harappa Project Contributors},
  year={2026},
  url={https://github.com/ShantiDraconis/indus-operational-mathematics}
}
```

## Contact

- GitHub: [ShantiDraconis/indus-operational-mathematics](https://github.com/ShantiDraconis/indus-operational-mathematics)
- Issues: [GitHub Issues](https://github.com/ShantiDraconis/indus-operational-mathematics/issues)

## Roadmap

- [ ] Complete documentation for all proposals
- [ ] Add visualization tools for symbols and states
- [ ] Implement Coq/Lean integration for proof system
- [ ] Create web-based visual programming interface
- [ ] Develop blockchain integration for DAO governance
- [ ] Build reference implementation for each application domain
- [ ] Performance optimization for large-scale simulations
- [ ] Multi-language bindings (JavaScript, Rust, Go)