# API Reference

## Core Module

### `HarappanAutomaton`

Main state machine for Harappan inscriptions.

```python
from core import HarappanAutomaton

automaton = HarappanAutomaton()
```

#### Methods

##### `add_entity(entity_id: int) -> bool`

Add an entity symbol (373-399) to start the inscription.

**Parameters**:
- `entity_id`: Integer in range 373-399

**Returns**: `True` if successful, `False` if invalid state

**Raises**: `ValueError` if entity_id out of range

**Example**:
```python
automaton.add_entity(373)  # Person/Individual
```

##### `add_operator(operator_name: str) -> bool`

Add a graphical operator.

**Parameters**:
- `operator_name`: One of 'dot', 'stroke', 'vertical', 'horizontal', 'oblique'

**Returns**: `True` if successful

**Example**:
```python
automaton.add_operator('dot')
```

##### `add_quantifier(count: int) -> bool`

Add a quantifier (|, ||, |||, etc.).

**Parameters**:
- `count`: Number of strokes (≥1)

**Returns**: `True` if successful

##### `add_relation(relation_id: int) -> bool`

Add a relation symbol (400-409).

**Parameters**:
- `relation_id`: Integer in range 400-409

**Returns**: `True` if successful

##### `add_closure(closure_id: int) -> bool`

Add a closure symbol (342-348) to complete the inscription.

**Parameters**:
- `closure_id`: Integer in range 342-348

**Returns**: `True` if successful

##### `is_valid() -> bool`

Check if inscription is in valid closed state (S5).

**Returns**: `True` if in state S5

##### `validate_sequence(symbols: List[Tuple[str, int]]) -> bool`

Validate a complete symbol sequence.

**Parameters**:
- `symbols`: List of (type, value) tuples

**Returns**: `True` if sequence is valid

**Example**:
```python
sequence = [
    ('entity', 373),
    ('closure', 343)
]
is_valid = automaton.validate_sequence(sequence)
```

---

## Proposals Module

### `HarappanKernel`

Operating system kernel managing processes as Harappan inscriptions.

```python
from proposals import HarappanKernel

kernel = HarappanKernel()
```

#### Methods

##### `create_process(entity_id: int) -> int`

Create a new process from an entity.

**Returns**: Process ID (PID)

##### `syscall(pid: int, operator: str) -> bool`

Execute system call for a process.

**Parameters**:
- `pid`: Process ID
- `operator`: System call name (maps to Harappan operator)

##### `exit(pid: int, exit_code: int) -> bool`

Terminate process with exit code (closure symbol).

##### `get_process_state(pid: int) -> ProcessState`

Get current state of a process.

##### `get_stats() -> Dict`

Get kernel statistics.

---

### `StateCrypto`

State-based cryptographic system.

```python
from proposals import StateCrypto, StateCryptoKey

crypto = StateCrypto()
```

#### Methods

##### `encrypt(message: bytes, key: StateCryptoKey) -> bytes`

Encrypt a message using state-based key.

**Raises**: `ValueError` if key is invalid

##### `decrypt(ciphertext: bytes, key: StateCryptoKey) -> bytes`

Decrypt using state-based key.

**Raises**: `ValueError` if key doesn't reach closure state

##### `create_key_from_entity(entity_id: int, closure_id: int) -> StateCryptoKey`

Create simple key from entity and closure.

##### `create_complex_key(...) -> StateCryptoKey`

Create complex key with full state transitions.

---

### `SmartContract`

Smart contract with state validation.

```python
from proposals import SmartContract

contract = SmartContract(
    contract_id=1,
    required_states=[373, 374, 375]
)
```

#### Methods

##### `lock_funds(funds_data: bytes, release_key: StateCryptoKey)`

Lock funds with state-based key.

##### `progress_state(entity_id: int) -> bool`

Progress contract through required states.

##### `can_release_funds() -> bool`

Check if all required states validated.

##### `release_funds() -> bytes`

Release funds after validation.

---

### `CivilizationGraph`

Network analysis of Harappan civilization.

```python
from proposals import CivilizationGraph

graph = CivilizationGraph()
```

#### Methods

##### `add_inscription(symbols: List[int])`

Add an inscription to the graph.

##### `detect_communities() -> Dict[int, Set[int]]`

Detect communities (functional families).

**Returns**: Dictionary mapping community_id to symbol set

##### `find_administrative_organs() -> List[Dict]`

Discover administrative organs from communities.

##### `get_most_central_symbols(n: int = 10) -> List[Tuple[int, float]]`

Find most central symbols (network hubs).

##### `get_network_stats() -> Dict`

Get overall network statistics.

##### `reconstruct_institutions() -> Dict[str, List[str]]`

Reconstruct institutional map.

---

### `HarappanCPU`

CPU based on Harappan automaton.

```python
from proposals import HarappanCPU, HarappanAssembler

cpu = HarappanCPU()
asm = HarappanAssembler()
```

#### Methods

##### `load_register(reg_id: int, value: int)`

Load value into register.

##### `get_register(reg_id: int) -> int`

Get register value.

##### `load_program(instructions: List[Instruction])`

Load program into memory.

##### `run(max_cycles: int = 1000) -> bool`

Run loaded program.

##### `halt(exit_code: int)`

Halt CPU with exit code.

#### HarappanAssembler Methods

##### `add(dest: int, op1: int, op2: int) -> Instruction`

Create ADD instruction.

##### `sub(dest: int, op1: int, op2: int) -> Instruction`

Create SUB instruction.

##### `mul(dest: int, op1: int, op2: int) -> Instruction`

Create MUL instruction.

---

### `Universe00`

The complete meta-system.

```python
from proposals import Universe00

universe = Universe00()
```

#### Methods

##### `bootstrap()`

Bootstrap the Universe 0/0 system.

##### `create_computational_process(entity_id: int, program: List) -> int`

Create process that runs on Harappan CPU.

##### `secure_communication(pid1: int, pid2: int, message: bytes, key: StateCryptoKey) -> bytes`

Secure inter-process communication.

##### `analyze_civilization_patterns() -> Dict`

Analyze patterns across all inscriptions.

##### `verify_system_coherence() -> bool`

Verify all subsystems are coherent.

##### `get_system_state() -> Dict[str, Any]`

Get complete system state.

##### `civilizational_closure() -> bool`

Check if civilization has reached complete closure.

---

### `HarappanGenerativeArt`

Generative art system.

```python
from proposals import HarappanGenerativeArt

art = HarappanGenerativeArt()
```

#### Methods

##### `generate_random_inscription() -> List[Tuple[str, any]]`

Generate random valid Harappan inscription.

##### `inscription_to_3d_blueprint(inscription) -> Dict`

Convert inscription to 3D architectural blueprint.

##### `generate_city_layout(num_buildings: int = 10) -> List[Dict]`

Generate city layout with multiple buildings.

---

### `AlgorithmicLaw`

Algorithmic law system.

```python
from proposals import AlgorithmicLaw

law = AlgorithmicLaw()
```

#### Methods

##### `file_case(symbols: List[Tuple[str, any]]) -> int`

File a new legal case.

**Returns**: Case ID

##### `judge_case(case_id: int) -> Dict`

Judge a case using Harappan validation.

**Returns**: Judgment with validity and ruling

##### `find_similar_precedents(symbols) -> List[int]`

Find similar precedents.

---

### `HarappanBCI`

Brain-computer interface.

```python
from proposals import HarappanBCI

bci = HarappanBCI()
```

#### Methods

##### `think_symbol(symbol_type: str, value: any)`

Register a thought symbol.

##### `think_approved()`

Think 'Approved' (closure 343).

##### `think_rejected()`

Think 'Rejected' (closure 342).

##### `think_quantity(count: int)`

Think a quantity.

##### `complete_thought() -> bool`

Complete and validate current thought.

---

### `InformationPhysics`

Information physics model.

```python
from proposals import InformationPhysics

physics = InformationPhysics(k=1.0)
```

#### Methods

##### `calculate_entropy(num_symbols: int) -> float`

Calculate entropy for inscription.

**Formula**: S = k * ln(417^n)

##### `calculate_energy(inscription) -> float`

Calculate energy (effort) to reach closure.

##### `calculate_institutional_pressure(current_state: str, target_state: str) -> float`

Calculate force (pressure) toward validation.

---

## Constants and Enumerations

### States

```python
from core import State

State.S0  # INITIAL
State.S1  # ENTITY_LOADED
State.S2  # OPERATOR_APPLIED
State.S3  # QUANTIFIED
State.S4  # RELATED
State.S5  # CLOSED
```

### Symbol Mappings

```python
from core import ENTITY_MEANINGS, CLOSURE_MEANINGS, RELATION_MEANINGS

ENTITY_MEANINGS[373]   # "Person/Individual"
CLOSURE_MEANINGS[343]  # "Approved"
RELATION_MEANINGS[400] # "Ownership"
```

### Process States

```python
from proposals import ProcessState

ProcessState.NEW
ProcessState.READY
ProcessState.RUNNING
ProcessState.WAITING
ProcessState.ZOMBIE
ProcessState.TERMINATED
```

### System Calls

```python
from proposals import SYSCALLS, EXIT_CODES

SYSCALLS['read']      # 'dot'
EXIT_CODES['SUCCESS'] # 343
```

---

## Error Handling

All methods raise standard Python exceptions:

- `ValueError`: Invalid parameter values
- `KeyError`: Missing keys in dictionaries
- `TypeError`: Wrong type for parameters

Always wrap critical operations in try-except blocks:

```python
try:
    automaton.add_entity(373)
    automaton.add_closure(343)
except ValueError as e:
    print(f"Validation error: {e}")
```
