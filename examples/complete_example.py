"""
Example: Complete demonstration of all Harappan proposals

This example shows how to use all 15 proposals together in the Universe 0/0 system.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import HarappanAutomaton
from proposals import (
    HarappanKernel,
    StateCrypto,
    StateCryptoKey,
    SmartContract,
    CivilizationGraph,
    HarappanCPU,
    HarappanAssembler,
    Universe00,
    HarappanGenerativeArt,
    AlgorithmicLaw,
    HarappanBCI,
    InformationPhysics,
)


def example_1_basic_automaton():
    """Example 1: Basic Harappan Automaton"""
    print("=" * 60)
    print("Example 1: Basic Harappan Automaton")
    print("=" * 60)
    
    automaton = HarappanAutomaton()
    
    # Simple validation: Entity -> Closure
    automaton.add_entity(373)  # Person/Individual
    automaton.add_closure(343)  # Approved
    
    print(f"Simple inscription: {automaton}")
    print(f"Is valid: {automaton.is_valid()}")
    print()
    
    # Complex validation: Full path
    automaton.reset()
    automaton.add_entity(376)  # Transaction
    automaton.add_operator('dot')  # Addition
    automaton.add_quantifier(3)  # |||
    automaton.add_relation(402)  # Payment
    automaton.add_closure(347)  # Verified
    
    print(f"Complex inscription: {automaton}")
    print(f"Is valid: {automaton.is_valid()}")
    print()


def example_2_harappan_os():
    """Example 2: Harappan Operating System"""
    print("=" * 60)
    print("Example 2: Harappan Operating System")
    print("=" * 60)
    
    kernel = HarappanKernel()
    
    # Create processes
    pid1 = kernel.create_process(373)  # User process
    pid2 = kernel.create_process(374)  # System process
    
    print(f"Created process {pid1}: {kernel.get_process_state(pid1)}")
    print(f"Created process {pid2}: {kernel.get_process_state(pid2)}")
    
    # Execute system calls
    kernel.syscall(pid1, 'dot')  # read
    print(f"After syscall, process {pid1}: {kernel.get_process_state(pid1)}")
    
    # Terminate processes
    kernel.exit(pid1, 343)  # Success
    print(f"Process {pid1} exit code: 343 ({kernel.get_exit_code_meaning(343)})")
    
    # Get statistics
    stats = kernel.get_stats()
    print(f"Kernel stats: {stats}")
    print()


def example_3_state_crypto():
    """Example 3: State-Based Cryptography"""
    print("=" * 60)
    print("Example 3: State-Based Cryptography")
    print("=" * 60)
    
    crypto = StateCrypto()
    
    # Create a key (must be valid Harappan sequence)
    key = crypto.create_key_from_entity(373, 343)
    print(f"Key is valid: {key.is_valid()}")
    
    # Encrypt a message
    message = b"Secret Harappan data"
    ciphertext = crypto.encrypt(message, key)
    print(f"Original message: {message}")
    print(f"Encrypted: {ciphertext[:20]}...")
    
    # Decrypt the message
    decrypted = crypto.decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Match: {message == decrypted}")
    print()


def example_4_smart_contract():
    """Example 4: Smart Contract with State Validation"""
    print("=" * 60)
    print("Example 4: Smart Contract with State Validation")
    print("=" * 60)
    
    # Create a contract requiring 3 state validations
    contract = SmartContract(
        contract_id=1,
        required_states=[373, 374, 375]  # Person, Group, Goods
    )
    
    # Lock funds
    crypto = StateCrypto()
    key = crypto.create_key_from_entity(375, 347)
    funds = b"1000 Harappan tokens"
    contract.lock_funds(funds, key)
    print(f"Funds locked: {funds}")
    
    # Progress through states
    contract.progress_state(373)
    print(f"State 1 validated. Can release: {contract.can_release_funds()}")
    
    contract.progress_state(374)
    print(f"State 2 validated. Can release: {contract.can_release_funds()}")
    
    contract.progress_state(375)
    print(f"State 3 validated. Can release: {contract.can_release_funds()}")
    
    # Release funds
    if contract.can_release_funds():
        released = contract.release_funds()
        print(f"Funds released: {released}")
    print()


def example_5_civilization_network():
    """Example 5: Civilization Network Analysis"""
    print("=" * 60)
    print("Example 5: Civilization Network Analysis")
    print("=" * 60)
    
    graph = CivilizationGraph()
    
    # Add sample inscriptions
    inscriptions = [
        [373, 343],  # Person approved
        [374, 343],  # Group approved
        [375, 400, 343],  # Goods ownership approved
        [376, 401, 347],  # Transaction transfer verified
        [377, 407, 343],  # Authority taxation approved
    ]
    
    for inscription in inscriptions:
        graph.add_inscription(inscription)
    
    print(f"Network stats: {graph.get_network_stats()}")
    
    # Detect communities
    institutions = graph.reconstruct_institutions()
    print(f"Discovered institutions:")
    for inst_type, symbols in institutions.items():
        print(f"  {inst_type}: {symbols}")
    
    # Find central symbols
    central = graph.get_most_central_symbols(5)
    print(f"Most central symbols: {central}")
    print()


def example_6_harappan_cpu():
    """Example 6: Harappan CPU Architecture"""
    print("=" * 60)
    print("Example 6: Harappan CPU Architecture")
    print("=" * 60)
    
    cpu = HarappanCPU()
    asm = HarappanAssembler()
    
    # Simple program: Add two numbers
    program = [
        asm.load_immediate(373, 5),   # R373 = 5
        asm.load_immediate(374, 10),  # R374 = 10
        asm.add(375, 373, 374),       # R375 = R373 + R374
    ]
    
    cpu.load_program(program)
    cpu.run()
    
    print(f"R373 = {cpu.get_register(373)}")
    print(f"R374 = {cpu.get_register(374)}")
    print(f"R375 = {cpu.get_register(375)} (expected: 15)")
    print(f"CPU state: {cpu.get_state()}")
    print(f"Cycles: {cpu.cycles}")
    print()


def example_7_generative_art():
    """Example 7: Generative Art"""
    print("=" * 60)
    print("Example 7: Generative Art")
    print("=" * 60)
    
    art = HarappanGenerativeArt()
    
    # Generate random valid inscriptions
    for i in range(3):
        inscription = art.generate_random_inscription()
        print(f"Inscription {i+1}: {inscription}")
        
        # Convert to 3D blueprint
        blueprint = art.inscription_to_3d_blueprint(inscription)
        print(f"  Blueprint foundations: {blueprint['foundations']}")
        print(f"  Blueprint structures: {blueprint['structures']}")
    print()


def example_8_algorithmic_law():
    """Example 8: Algorithmic Law System"""
    print("=" * 60)
    print("Example 8: Algorithmic Law System")
    print("=" * 60)
    
    law = AlgorithmicLaw()
    
    # File legal cases
    case1 = [('entity', 373), ('closure', 343)]  # Valid
    case2 = [('entity', 374), ('closure', 342)]  # Valid
    case3 = [('operator', 'dot')]  # Invalid (no entity)
    
    cid1 = law.file_case(case1)
    cid2 = law.file_case(case2)
    cid3 = law.file_case(case3)
    
    # Judge cases
    judgment1 = law.judge_case(cid1)
    judgment2 = law.judge_case(cid2)
    judgment3 = law.judge_case(cid3)
    
    print(f"Case {cid1}: {judgment1}")
    print(f"Case {cid2}: {judgment2}")
    print(f"Case {cid3}: {judgment3}")
    print()


def example_9_bci():
    """Example 9: Brain-Computer Interface"""
    print("=" * 60)
    print("Example 9: Brain-Computer Interface")
    print("=" * 60)
    
    bci = HarappanBCI()
    
    # Think a thought sequence
    print("Thinking: Approved")
    bci.think_approved()
    
    result = bci.complete_thought()
    print(f"Thought completed successfully: {result}")
    
    # Think another sequence
    print("Thinking: Quantity 3")
    bci.think_quantity(3)
    
    result = bci.complete_thought()
    print(f"Thought completed successfully: {result}")
    print()


def example_10_information_physics():
    """Example 10: Information Physics"""
    print("=" * 60)
    print("Example 10: Information Physics")
    print("=" * 60)
    
    physics = InformationPhysics(k=1.0)
    
    # Calculate entropy for inscriptions of different lengths
    for n in [1, 2, 3, 5]:
        entropy = physics.calculate_entropy(n)
        print(f"Entropy for {n} symbols: {entropy:.2f}")
    
    # Calculate energy for an inscription
    inscription = [('entity', 373), ('operator', 'dot'), ('quantifier', 3), ('closure', 343)]
    energy = physics.calculate_energy(inscription)
    print(f"Energy for inscription: {energy:.2f}")
    
    # Calculate institutional pressure
    pressure = physics.calculate_institutional_pressure('ENTITY_LOADED', 'CLOSED')
    print(f"Institutional pressure: {pressure:.2f}")
    print()


def example_11_universe_00():
    """Example 11: Universe 0/0 - The Complete System"""
    print("=" * 60)
    print("Example 11: Universe 0/0 - The Complete System")
    print("=" * 60)
    
    universe = Universe00()
    
    # Bootstrap the system
    universe.bootstrap()
    print("Universe 0/0 bootstrapped")
    
    # Get system state
    state = universe.get_system_state()
    print(f"System state: {state}")
    
    # Create computational processes
    pid = universe.create_computational_process(373, [])
    print(f"Created process: {pid}")
    
    # Analyze civilization patterns
    analysis = universe.analyze_civilization_patterns()
    print(f"Civilization analysis: {analysis}")
    
    # Check coherence
    coherent = universe.verify_system_coherence()
    print(f"System coherent: {coherent}")
    
    # Check for civilizational closure
    closed = universe.civilizational_closure()
    print(f"Civilizational closure achieved: {closed}")
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("HARAPPAN OPERATIONAL MATHEMATICS")
    print("Complete Example Suite")
    print("=" * 60 + "\n")
    
    example_1_basic_automaton()
    example_2_harappan_os()
    example_3_state_crypto()
    example_4_smart_contract()
    example_5_civilization_network()
    example_6_harappan_cpu()
    example_7_generative_art()
    example_8_algorithmic_law()
    example_9_bci()
    example_10_information_physics()
    example_11_universe_00()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
