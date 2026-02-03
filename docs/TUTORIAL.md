# Harappan Operational Mathematics Tutorial

## Introduction

Welcome to the Harappan Operational Mathematics framework! This tutorial will guide you through the core concepts and show you how to use the system.

## Part 1: Understanding the Harappan Automaton

### What is a Harappan Inscription?

A Harappan inscription is a sequence of symbols that represents an administrative validation. Think of it as an ancient "smart contract" or "process validation".

Every inscription follows a strict grammar that ensures it reaches a valid "closed" state.

### The Six States

The automaton has six states:

1. **S0 - INITIAL**: Starting point
2. **S1 - ENTITY_LOADED**: An entity has been specified
3. **S2 - OPERATOR_APPLIED**: An operation has been applied
4. **S3 - QUANTIFIED**: A quantity has been specified
5. **S4 - RELATED**: A relationship has been established
6. **S5 - CLOSED**: Validation complete (terminal state)

### Your First Inscription

Let's create the simplest valid inscription:

```python
from core import HarappanAutomaton

# Create the automaton
automaton = HarappanAutomaton()

# Add an entity (373 = Person/Individual)
automaton.add_entity(373)

# Add a closure (343 = Approved)
automaton.add_closure(343)

# Check if valid
print(f"Is valid: {automaton.is_valid()}")  # True
print(f"Inscription: {automaton}")
```

**Output**:
```
Is valid: True
Inscription: HarappanAutomaton(state=CLOSED, inscription=[E373 → C343])
```

This inscription means: "Individual approved"

### A More Complex Inscription

Now let's create a complex validation:

```python
automaton = HarappanAutomaton()

# Transaction (376) with payment (402) operation
automaton.add_entity(376)      # Transaction
automaton.add_operator('dot')  # Addition/processing
automaton.add_quantifier(3)    # Quantity: 3 units
automaton.add_relation(402)    # Payment relation
automaton.add_closure(347)     # Verified

print(f"Complex inscription: {automaton}")
```

This means: "Transaction of 3 units with payment relationship - Verified"

---

## Part 2: Building a Simple OS

### Creating Processes

Let's use the Harappan OS to manage processes:

```python
from proposals import HarappanKernel

# Create kernel
kernel = HarappanKernel()

# Create a user process
user_pid = kernel.create_process(373)  # Person entity

# Create a system process
sys_pid = kernel.create_process(377)   # Authority entity

print(f"User process: {user_pid}")
print(f"System process: {sys_pid}")
```

### Running System Calls

```python
# User process performs a read
kernel.syscall(user_pid, 'dot')

# Check process state
state = kernel.get_process_state(user_pid)
print(f"Process {user_pid} is in state: {state}")

# Terminate with success
kernel.exit(user_pid, 343)  # 343 = Approved/Success

print(f"Exit code meaning: {kernel.get_exit_code_meaning(343)}")
```

### Kernel Statistics

```python
stats = kernel.get_stats()
print(f"Total processes: {stats['total_processes']}")
print(f"Running: {stats['running']}")
print(f"System calls executed: {stats['syscall_count']}")
```

---

## Part 3: Cryptography and Smart Contracts

### State-Based Encryption

```python
from proposals import StateCrypto

crypto = StateCrypto()

# Create a key (must be valid Harappan sequence!)
key = crypto.create_key_from_entity(373, 343)

# Verify key is valid
print(f"Key is valid: {key.is_valid()}")

# Encrypt a message
secret = b"Transfer 100 tokens to account 42"
ciphertext = crypto.encrypt(secret, key)

print(f"Encrypted: {ciphertext[:30]}...")

# Decrypt
plaintext = crypto.decrypt(ciphertext, key)
print(f"Decrypted: {plaintext}")
```

**Key Point**: Only valid Harappan sequences can be used as keys! This ensures cryptographic operations follow institutional grammar.

### Smart Contract with Multi-State Validation

```python
from proposals import SmartContract, StateCrypto

# Create a contract requiring 3 approvals
contract = SmartContract(
    contract_id=1,
    required_states=[373, 374, 377]  # Person, Group, Authority
)

# Create release key
crypto = StateCrypto()
key = crypto.create_key_from_entity(375, 347)

# Lock funds
funds = b"1000 Harappan tokens"
contract.lock_funds(funds, key)
print("Funds locked!")

# Simulate approval process
print("\n--- Approval Process ---")

# First approval: Person
contract.progress_state(373)
print(f"Person approved. Can release: {contract.can_release_funds()}")

# Second approval: Group
contract.progress_state(374)
print(f"Group approved. Can release: {contract.can_release_funds()}")

# Final approval: Authority
contract.progress_state(377)
print(f"Authority approved. Can release: {contract.can_release_funds()}")

# Release funds
if contract.can_release_funds():
    released = contract.release_funds()
    print(f"\nFunds released: {released}")
```

---

## Part 4: Civilization Network Analysis

### Discovering Institutional Structures

```python
from proposals import CivilizationGraph

graph = CivilizationGraph()

# Add sample inscriptions (from archaeological record)
inscriptions = [
    [373, 343],           # Person approved
    [374, 343],           # Group approved
    [375, 400, 343],      # Goods ownership approved
    [376, 401, 347],      # Transaction transfer verified
    [377, 407, 343],      # Authority taxation approved
    [378, 406, 347],      # Location trade verified
]

for inscription in inscriptions:
    graph.add_inscription(inscription)

print("Network added 6 inscriptions")
```

### Analyzing the Network

```python
# Get statistics
stats = graph.get_network_stats()
print(f"\nNetwork Statistics:")
print(f"  Nodes: {stats['nodes']}")
print(f"  Edges: {stats['edges']}")
print(f"  Density: {stats['density']:.3f}")

# Find most important symbols
central = graph.get_most_central_symbols(5)
print(f"\nMost central symbols:")
for symbol_id, centrality in central:
    print(f"  Symbol {symbol_id}: {centrality:.3f}")

# Discover institutions
institutions = graph.reconstruct_institutions()
print(f"\nDiscovered Institutions:")
for inst_type, symbols in institutions.items():
    print(f"  {inst_type}:")
    for symbol in symbols[:3]:  # Show first 3
        print(f"    - {symbol}")
```

---

## Part 5: Building with Harappan CPU

### Simple Arithmetic Program

```python
from proposals import HarappanCPU, HarappanAssembler

cpu = HarappanCPU()
asm = HarappanAssembler()

# Program: Calculate (5 + 10) * 2
program = [
    asm.load_immediate(373, 5),    # R373 = 5
    asm.load_immediate(374, 10),   # R374 = 10
    asm.add(375, 373, 374),        # R375 = R373 + R374 = 15
    asm.load_immediate(376, 2),    # R376 = 2
    asm.mul(377, 375, 376),        # R377 = R375 * R376 = 30
]

cpu.load_program(program)
cpu.run()

print(f"R373 = {cpu.get_register(373)}")  # 5
print(f"R374 = {cpu.get_register(374)}")  # 10
print(f"R375 = {cpu.get_register(375)}")  # 15
print(f"R377 = {cpu.get_register(377)}")  # 30
print(f"CPU executed {cpu.cycles} cycles")
```

---

## Part 6: Universe 0/0 - The Complete System

### Bootstrapping the Universe

```python
from proposals import Universe00

# Create the meta-system
universe = Universe00()
universe.bootstrap()

print("Universe 0/0 initialized!")
```

### Creating Computational Processes

```python
# Create a process
from proposals import HarappanAssembler

asm = HarappanAssembler()
simple_program = [
    asm.load_immediate(373, 42)
]

pid = universe.create_computational_process(373, simple_program)
print(f"Created process {pid}")
```

### System Analysis

```python
# Get complete system state
state = universe.get_system_state()

print(f"\n--- System State ---")
print(f"OS Processes: {state['os']['processes']}")
print(f"CPU Cycles: {state['cpu']['cycles']}")
print(f"System Coherent: {state['coherent']}")

# Analyze civilization patterns
analysis = universe.analyze_civilization_patterns()
print(f"\nNetwork Stats: {analysis['network_stats']}")
```

### Checking for Civilizational Closure

```python
# Have all processes reached closure?
closed = universe.civilizational_closure()
print(f"\nCivilizational closure achieved: {closed}")
```

---

## Part 7: Advanced Topics

### Generative Art

```python
from proposals import HarappanGenerativeArt

art = HarappanGenerativeArt()

# Generate random valid inscriptions
for i in range(3):
    inscription = art.generate_random_inscription()
    print(f"\nInscription {i+1}: {inscription}")
    
    # Convert to architectural blueprint
    blueprint = art.inscription_to_3d_blueprint(inscription)
    print(f"  Foundations: {len(blueprint['foundations'])}")
    print(f"  Structures: {len(blueprint['structures'])}")
```

### Algorithmic Law

```python
from proposals import AlgorithmicLaw

law = AlgorithmicLaw()

# File a case
case_symbols = [
    ('entity', 373),    # Person
    ('closure', 343),   # Approved
]

case_id = law.file_case(case_symbols)

# Judge the case
judgment = law.judge_case(case_id)

print(f"\n--- Legal Judgment ---")
print(f"Case ID: {judgment['case_id']}")
print(f"Valid: {judgment['valid']}")
print(f"Ruling: {judgment['ruling']}")
print(f"Sets precedent: {judgment['precedent']}")
```

### Brain-Computer Interface

```python
from proposals import HarappanBCI

bci = HarappanBCI()

# Think approval
bci.think_approved()
success = bci.complete_thought()
print(f"Approval thought completed: {success}")

# Think quantity
bci.think_quantity(5)
success = bci.complete_thought()
print(f"Quantity thought completed: {success}")
```

### Information Physics

```python
from proposals import InformationPhysics

physics = InformationPhysics(k=1.0)

# Calculate entropy for different inscription lengths
for n in [1, 2, 3, 5, 10]:
    entropy = physics.calculate_entropy(n)
    print(f"Entropy for {n} symbols: {entropy:.2f} bits")

# Calculate energy for a specific inscription
inscription = [
    ('entity', 373),
    ('operator', 'dot'),
    ('quantifier', 3),
    ('closure', 343)
]
energy = physics.calculate_energy(inscription)
print(f"\nEnergy required: {energy:.2f} units")
```

---

## Part 8: Best Practices

### 1. Always Validate Sequences

```python
# Good
automaton = HarappanAutomaton()
sequence = [('entity', 373), ('closure', 343)]
if automaton.validate_sequence(sequence):
    print("Sequence is valid")
```

### 2. Handle Invalid States

```python
# Good
try:
    automaton.add_entity(999)  # Invalid entity ID
except ValueError as e:
    print(f"Error: {e}")
```

### 3. Use Meaningful Entities

```python
from core import ENTITY_MEANINGS

# Choose entities that match your domain
entity_id = 376  # Transaction
print(f"Using entity: {ENTITY_MEANINGS[entity_id]}")
```

### 4. Check System Coherence

```python
# After operations, verify system is coherent
if universe.verify_system_coherence():
    print("All subsystems coherent")
else:
    print("Warning: System incoherent!")
```

---

## Conclusion

You now understand:
- ✅ Harappan automaton and inscriptions
- ✅ State-based OS and processes
- ✅ Cryptography and smart contracts
- ✅ Network analysis and institutions
- ✅ CPU architecture and programs
- ✅ The Universe 0/0 meta-system
- ✅ All 15 revolutionary proposals

### Next Steps

1. **Experiment**: Try creating your own inscriptions
2. **Extend**: Implement proposals 4, 5, 8, 9, 10, 11, 15
3. **Research**: Study the theoretical foundations in `docs/THEORY.md`
4. **Contribute**: Help build the Harappan computational revolution!

### The Radical Question

> What if the Harappan Civilization didn't "disappear" but rather "completed" its civilizational project, achieving complete institutional closure?

Explore this hypothesis using the tools you've learned!

---

**Happy coding with Harappan Operational Mathematics!** 🏛️
