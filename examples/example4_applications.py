"""
Example 4: Multi-Application Demonstrations
Demonstrates Proposals 4-15 - Various applications of the Harappa system
"""

from harappa import Symbol, Operator, SymbolType, OperatorType
from harappa.uid import HarappaUID, UIDType
from harappa.applications import (
    ArchaeologicalSimulation, Agent,
    VisualProgrammingInterface,
    EducationalSystem,
    AIMetadata,
    SemanticDatabase, OntologyClass,
    CommunicationSystem, StructuredMessage,
    DAOGovernance, Proposal,
    AncientTextSearchEngine,
    ArtGenerator,
    AuthenticationSystem,
    ServiceChoreography,
    RiskAnalysisTool, Task
)
from harappa.core import Record

def example_archaeological_simulation():
    """Proposal 4: Simulate Harappan trade networks."""
    print("\n=== Archaeological Simulation ===")
    
    sim = ArchaeologicalSimulation()
    
    # Create agents
    agent1_uid = HarappaUID(UIDType.ENTITY, "harappa_city")
    agent1 = Agent(agent1_uid, "trader", {"grain": 100, "pottery": 50})
    
    agent2_uid = HarappaUID(UIDType.ENTITY, "mohenjo_daro")
    agent2 = Agent(agent2_uid, "trader", {"textiles": 75, "beads": 200})
    
    agent1.connections.append(agent2)
    agent2.connections.append(agent1)
    
    sim.add_agent(agent1)
    sim.add_agent(agent2)
    
    # Run simulation
    for _ in range(5):
        sim.simulate_step()
    
    stats = sim.get_network_statistics()
    print(f"Total agents: {stats['total_agents']}")
    print(f"Total transactions: {stats['total_transactions']}")
    print(f"Average connections: {stats['average_connections']:.2f}")

def example_visual_programming():
    """Proposal 5: Visual programming interface."""
    print("\n=== Visual Programming Interface ===")
    
    vpi = VisualProgrammingInterface()
    
    # Create workflow nodes
    input_sym = Symbol("user_input", SymbolType.ENTITY)
    process_sym = Symbol("validate_data", SymbolType.TRANSACTION)
    output_sym = Symbol("store_result", SymbolType.STATE)
    
    node1 = vpi.add_node(input_sym, 0, 0)
    node2 = vpi.add_node(process_sym, 100, 0)
    node3 = vpi.add_node(output_sym, 200, 0)
    
    vpi.connect_nodes(node1, node2)
    vpi.connect_nodes(node2, node3)
    
    code = vpi.generate_code()
    print("Generated workflow:")
    print(code)

def example_ai_metadata():
    """Proposal 7: AI Metadata standard."""
    print("\n=== AI Metadata Standard ===")
    
    uid = HarappaUID(UIDType.DOCUMENT, "ml_dataset")
    metadata = AIMetadata(uid, "ImageNet-Subset-2026")
    metadata.add_provenance("Stanford University")
    metadata.add_provenance("ImageNet Project")
    metadata.set_quality(0.95)
    metadata.licenses.append("CC-BY-4.0")
    metadata.audit_status = "audited"
    
    seal = metadata.to_seal()
    print(f"Dataset: {metadata.dataset_name}")
    print(f"Quality: {metadata.quality_score}")
    print(f"Audit Status: {metadata.audit_status}")
    print(f"Digital Seal: {seal[:16]}...")

def example_semantic_database():
    """Proposal 8: Semantic database with ontology."""
    print("\n=== Semantic Database ===")
    
    db = SemanticDatabase()
    
    # Define ontology
    person_class = OntologyClass(
        name="Person",
        properties={"name": str, "age": int}
    )
    person_class.symbols.append(Symbol("person_entity", SymbolType.ENTITY))
    
    db.define_class(person_class)
    
    # Add instances
    db.add_instance("Person", {"name": "Alice", "age": 30})
    db.add_instance("Person", {"name": "Bob", "age": 25})
    
    # Query
    results = db.query("Person", {"age": 30})
    print(f"Query results: {len(results)} persons found")
    for r in results:
        print(f"  {r['name']}, age {r['age']}")

def example_dao_governance():
    """Proposal 10: DAO Governance system."""
    print("\n=== DAO Governance ===")
    
    dao = DAOGovernance()
    dao.members.add("member1")
    dao.members.add("member2")
    dao.members.add("member3")
    
    # Create proposal
    proposal_uid = HarappaUID(UIDType.DOCUMENT, "dao_proposals")
    proposal_record = Record()
    proposal_record.add_symbol(Symbol("upgrade_protocol", SymbolType.TRANSACTION))
    
    proposal = Proposal(
        uid=proposal_uid,
        title="Upgrade Protocol Version",
        description="Upgrade to v2.0",
        record=proposal_record
    )
    
    dao.create_proposal(proposal)
    
    # Vote
    proposal_id = str(proposal_uid)
    dao.vote(proposal_id, "member1", True)
    dao.vote(proposal_id, "member2", True)
    dao.vote(proposal_id, "member3", False)
    
    dao.finalize_proposal(proposal_id)
    
    print(f"Proposal: {proposal.title}")
    print(f"Votes for: {proposal.votes_for}")
    print(f"Votes against: {proposal.votes_against}")
    print(f"Status: {proposal.status}")
    print(f"Record closed: {proposal.record.has_closure}")

def example_art_generator():
    """Proposal 12: Algorithmic art generation."""
    print("\n=== Algorithmic Art Generator ===")
    
    art_gen = ArtGenerator()
    
    artwork1 = art_gen.generate_artwork(seed=42, complexity=7)
    artwork2 = art_gen.generate_artwork(seed=123, complexity=5)
    
    print(f"Generated {len(art_gen.artworks)} artworks")
    print(f"Artwork 1: {len(artwork1.symbols)} symbols, {len(artwork1.operators)} operators")
    print(f"Artwork 2: {len(artwork2.symbols)} symbols, {len(artwork2.operators)} operators")
    print(f"Both are valid records: {artwork1.validate() and artwork2.validate()}")

def example_authentication():
    """Proposal 13: Authentication without passwords."""
    print("\n=== Authentication System ===")
    
    auth = AuthenticationSystem()
    
    # Register user with Harappa seal
    user_seal = HarappaUID(UIDType.ENTITY, "user_auth")
    user_seal.add_symbol(Symbol("user_alice", SymbolType.ENTITY))
    
    auth.register_user("alice", user_seal)
    auth.grant_permission("alice", "read_data")
    auth.grant_permission("alice", "write_data")
    
    # Authenticate
    is_authenticated = auth.authenticate("alice", user_seal)
    can_read = auth.check_permission("alice", "read_data")
    can_admin = auth.check_permission("alice", "admin")
    
    print(f"User authenticated: {is_authenticated}")
    print(f"Can read data: {can_read}")
    print(f"Can admin: {can_admin}")

def example_risk_analysis():
    """Proposal 15: Risk analysis for projects."""
    print("\n=== Risk Analysis Tool ===")
    
    tool = RiskAnalysisTool()
    
    # Define project tasks
    task1 = Task("Requirements", Symbol("req", SymbolType.STATE), risk_level=0.2)
    task2 = Task("Design", Symbol("design", SymbolType.STATE), risk_level=0.3)
    task3 = Task("Implementation", Symbol("impl", SymbolType.TRANSACTION), risk_level=0.6)
    task4 = Task("Testing", Symbol("test", SymbolType.STATE), risk_level=0.4)
    
    # Set dependencies
    task2.dependencies.append(task1)
    task3.dependencies.append(task2)
    task4.dependencies.append(task3)
    
    tool.add_task(task1)
    tool.add_task(task2)
    tool.add_task(task3)
    tool.add_task(task4)
    
    # Analyze
    analysis = tool.analyze_risks()
    print(f"Total tasks: {analysis['total_tasks']}")
    print(f"Average risk: {analysis['average_risk']:.2f}")
    print(f"Circular dependencies: {analysis['has_circular_dependencies']}")
    print(f"High risk tasks: {analysis['high_risk_tasks']}")

if __name__ == "__main__":
    example_archaeological_simulation()
    example_visual_programming()
    example_ai_metadata()
    example_semantic_database()
    example_dao_governance()
    example_art_generator()
    example_authentication()
    example_risk_analysis()
    
    print("\n=== All Examples Completed ===")
