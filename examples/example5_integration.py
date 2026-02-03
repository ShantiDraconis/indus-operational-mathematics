"""
Example 5: Integrated Multi-Proposal Demonstration

This example demonstrates how multiple Harappa proposals work together
in a real-world scenario: a decentralized supply chain management system
with formal verification, unique identification, and DAO governance.
"""

from harappa import Symbol, Operator, State, SymbolType, OperatorType
from harappa.spec_lang import HarappaSpec, Transition, Contract, ContractMethod
from harappa.uid import HarappaUID, UIDType, UIDRegistry, ValidationStatus
from harappa.applications import DAOGovernance, Proposal
from harappa.core import Record


def integrated_supply_chain_example():
    """
    Integrated example: Decentralized supply chain with formal verification.
    
    Combines:
    - Proposal 1: Formal specification of supply chain contract
    - Proposal 2: Unique identification for shipments and products
    - Proposal 10: DAO governance for supply chain decisions
    """
    
    print("=" * 70)
    print("INTEGRATED SUPPLY CHAIN MANAGEMENT SYSTEM")
    print("=" * 70)
    
    # ========================================================================
    # Part 1: Define Formal Specification (Proposal 1)
    # ========================================================================
    print("\n[1] Defining Formal Specification...")
    
    spec = HarappaSpec()
    shipment_sm = spec.create_state_machine("ShipmentLifecycle")
    
    # Define states
    states = {
        "created": State(),
        "in_transit": State(),
        "customs_check": State(),
        "delivered": State(is_final=True)
    }
    
    for name, state in states.items():
        shipment_sm.add_state(name, state)
    
    shipment_sm.add_final_state("delivered")
    
    # Define operators
    dispatch_op = Operator("dispatch", OperatorType.TRANSFORMATION, 1)
    customs_op = Operator("customs_verify", OperatorType.VALIDATION, 1)
    deliver_op = Operator("deliver", OperatorType.CLOSURE, 1)
    
    # Define transitions
    transitions = [
        Transition("created", "in_transit", dispatch_op),
        Transition("in_transit", "customs_check", customs_op),
        Transition("customs_check", "delivered", deliver_op)
    ]
    
    for t in transitions:
        shipment_sm.add_transition(t)
    
    # Create contract with invariants
    contract = spec.create_contract("ShipmentContract", shipment_sm)
    
    # Add contract methods
    dispatch_method = ContractMethod("dispatch")
    dispatch_method.preconditions.append(
        lambda s: not s.is_final  # Can only dispatch if not delivered
    )
    contract.add_method(dispatch_method)
    
    print(f"  ✓ State Machine: {shipment_sm.name}")
    print(f"  ✓ States: {list(shipment_sm.states.keys())}")
    print(f"  ✓ Deterministic: {shipment_sm.is_deterministic()}")
    print(f"  ✓ Terminates: {shipment_sm.has_termination_guarantee()}")
    print(f"  ✓ Contract Valid: {contract.validate()}")
    
    # ========================================================================
    # Part 2: Create Unique Identifiers (Proposal 2)
    # ========================================================================
    print("\n[2] Creating Unique Identifiers...")
    
    registry = UIDRegistry()
    
    # Create shipment UID
    shipment_uid = HarappaUID(UIDType.ASSET, "global_supply_chain")
    shipment_uid.add_symbol(Symbol("SHIPMENT_SC001", SymbolType.ENTITY))
    shipment_uid.encode_metadata("origin", "Shanghai")
    shipment_uid.encode_metadata("destination", "New York")
    shipment_uid.encode_metadata("carrier", "GlobalShip Inc")
    shipment_uid.set_validation_status(ValidationStatus.VALIDATED)
    
    shipment_id = registry.register(shipment_uid)
    
    # Create product UIDs as children
    products = []
    for i in range(3):
        product_uid = HarappaUID(UIDType.ASSET, "global_supply_chain")
        product_uid.add_symbol(Symbol(f"PRODUCT_{i+1:03d}", SymbolType.RESOURCE))
        product_uid.set_parent(shipment_uid)
        product_uid.encode_metadata("sku", f"PROD-{i+1:04d}")
        product_uid.encode_metadata("quantity", 100 * (i + 1))
        product_uid.set_validation_status(ValidationStatus.VALIDATED)
        
        product_id = registry.register(product_uid)
        products.append((product_uid, product_id))
    
    print(f"  ✓ Shipment UID: {shipment_id[:50]}...")
    print(f"  ✓ Products: {len(products)} items")
    
    for i, (uid, uid_str) in enumerate(products):
        semantic_info = uid.get_semantic_info()
        print(f"    - Product {i+1}: {semantic_info['metadata']['sku']}, "
              f"qty={semantic_info['metadata']['quantity']}")
    
    # Validate hierarchy
    children = registry.find_children(shipment_uid)
    print(f"  ✓ Hierarchy validated: {len(children)} children of shipment")
    
    # ========================================================================
    # Part 3: DAO Governance for Supply Chain Decisions (Proposal 10)
    # ========================================================================
    print("\n[3] Setting up DAO Governance...")
    
    dao = DAOGovernance()
    
    # Add members (different stakeholders in the supply chain)
    stakeholders = [
        "manufacturer",
        "logistics_provider",
        "customs_authority",
        "retailer",
        "quality_inspector"
    ]
    
    for stakeholder in stakeholders:
        dao.members.add(stakeholder)
    
    print(f"  ✓ DAO Members: {len(dao.members)}")
    
    # Create proposal for shipment route change
    proposal_uid = HarappaUID(UIDType.DOCUMENT, "dao_proposals")
    proposal_uid.add_symbol(Symbol("ROUTE_CHANGE_001", SymbolType.TRANSACTION))
    
    proposal_record = Record()
    proposal_record.add_symbol(Symbol("route_change", SymbolType.TRANSACTION))
    proposal_record.add_symbol(Symbol("cost_optimization", SymbolType.QUANTIFIER))
    proposal_record.metadata["shipment_id"] = shipment_id
    proposal_record.metadata["new_route"] = "via_panama_canal"
    proposal_record.metadata["cost_saving"] = "15%"
    
    proposal = Proposal(
        uid=proposal_uid,
        title="Optimize Route via Panama Canal",
        description="Change route to reduce shipping costs by 15%",
        record=proposal_record
    )
    
    dao.create_proposal(proposal)
    print(f"  ✓ Proposal Created: {proposal.title}")
    
    # Voting process
    votes = {
        "manufacturer": True,      # Approves (cost saving)
        "logistics_provider": True,  # Approves (feasible)
        "customs_authority": False,  # Rejects (more inspections needed)
        "retailer": True,           # Approves (faster delivery)
        "quality_inspector": True   # Approves (no quality impact)
    }
    
    proposal_id = str(proposal_uid)
    for member, vote in votes.items():
        dao.vote(proposal_id, member, vote)
        vote_text = "FOR" if vote else "AGAINST"
        print(f"    - {member}: {vote_text}")
    
    # Finalize proposal
    dao.finalize_proposal(proposal_id)
    
    print(f"  ✓ Voting Complete:")
    print(f"    Votes FOR: {proposal.votes_for}")
    print(f"    Votes AGAINST: {proposal.votes_against}")
    print(f"    Status: {proposal.status.upper()}")
    print(f"    Record Closed: {proposal.record.has_closure}")
    
    # ========================================================================
    # Part 4: Execute Shipment with Approved Route (Integration)
    # ========================================================================
    print("\n[4] Executing Shipment...")
    
    # Create shipment execution record
    execution_record = Record()
    execution_record.metadata["shipment_uid"] = shipment_id
    execution_record.metadata["route"] = "via_panama_canal"  # Approved route
    execution_record.metadata["proposal_id"] = proposal_id
    
    # Add all products to shipment
    for product_uid, _ in products:
        execution_record.add_symbol(product_uid.symbols[0])
    
    # Execute state transitions according to formal spec
    current_state_name = "created"
    
    for transition in shipment_sm.transitions:
        execution_record.add_operator(transition.operator)
        current_state_name = transition.to_state
        print(f"  → State: {current_state_name}")
    
    # Close the execution record
    execution_record.close()
    
    print(f"  ✓ Shipment executed successfully")
    print(f"  ✓ Final state: {current_state_name}")
    print(f"  ✓ Execution record valid: {execution_record.validate()}")
    
    # ========================================================================
    # Part 5: Summary and Statistics
    # ========================================================================
    print("\n" + "=" * 70)
    print("SYSTEM SUMMARY")
    print("=" * 70)
    
    print("\nFormal Verification:")
    print(f"  Contract: {contract.name}")
    print(f"  State Machine Valid: {shipment_sm.validate()}")
    print(f"  Deterministic: {shipment_sm.is_deterministic()}")
    print(f"  Guarantees Termination: {shipment_sm.has_termination_guarantee()}")
    
    print("\nUnique Identification:")
    stats = registry.get_statistics()
    print(f"  Total UIDs: {stats['total_uids']}")
    print(f"  By Type: {stats['by_type']}")
    print(f"  Hierarchy Levels: {stats['by_hierarchy_level']}")
    
    print("\nDAO Governance:")
    print(f"  Members: {len(dao.members)}")
    print(f"  Proposals: {len(dao.proposals)}")
    print(f"  Approved: {sum(1 for p in dao.proposals.values() if p.status == 'approved')}")
    
    print("\nExecution:")
    print(f"  Symbols in execution: {len(execution_record.symbols)}")
    print(f"  Operators applied: {len(execution_record.operators)}")
    print(f"  Record closed: {execution_record.has_closure}")
    print(f"  Record valid: {execution_record.validate()}")
    
    print("\n" + "=" * 70)
    print("Integration demonstrates:")
    print("  ✓ Formal specification ensures correct state transitions")
    print("  ✓ Unique IDs provide traceable, hierarchical identification")
    print("  ✓ DAO governance enables transparent decision-making")
    print("  ✓ All components work together seamlessly")
    print("=" * 70)
    
    return {
        "spec": spec,
        "contract": contract,
        "registry": registry,
        "dao": dao,
        "execution_record": execution_record
    }


if __name__ == "__main__":
    result = integrated_supply_chain_example()
    print("\n✓ Integration example completed successfully!")
