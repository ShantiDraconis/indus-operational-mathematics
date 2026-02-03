"""
Example 3: Proof System
Demonstrates Proposal 3 - Theorem verification with diagrammatic proofs
"""

from harappa import Symbol, Operator, SymbolType, OperatorType
from harappa.proof import ProofSystem, Theorem, DiagrammaticProofBuilder, ProofStepType

def example_simple_proof():
    """Example: Simple logical proof using Harappa."""
    
    # Create proof system
    ps = ProofSystem()
    
    # Define axioms
    axiom1 = Symbol("A_implies_B", SymbolType.STATE)
    axiom1.attributes["formula"] = "A → B"
    ps.add_axiom(axiom1)
    
    axiom2 = Symbol("B_implies_C", SymbolType.STATE)
    axiom2.attributes["formula"] = "B → C"
    ps.add_axiom(axiom2)
    
    # Define theorem: A → C (transitivity)
    theorem_statement = Symbol("A_implies_C", SymbolType.STATE)
    theorem_statement.attributes["formula"] = "A → C"
    
    theorem = Theorem(
        name="Transitivity",
        statement=theorem_statement,
        axioms=[axiom1, axiom2]
    )
    ps.add_theorem(theorem)
    
    print("=== Theorem Proving Example ===")
    print(f"Theorem: {theorem.name}")
    print(f"Statement: {theorem.statement.attributes['formula']}")
    print(f"Axioms: {[a.attributes['formula'] for a in theorem.axioms]}")
    
    # Build proof using diagrammatic builder
    builder = DiagrammaticProofBuilder(ps, theorem)
    
    # Proof steps
    # 1. Assume A
    assumption_A = Symbol("A", SymbolType.STATE)
    assumption_A.attributes["formula"] = "A"
    builder.assume(assumption_A, "Assumption")
    
    # 2. Apply A → B to get B
    implies_operator = Operator(
        name="modus_ponens_1",
        operator_type=OperatorType.TRANSFORMATION,
        arity=1
    )
    builder.apply(implies_operator, "From A and A→B, derive B")
    
    # 3. Apply B → C to get C
    implies_operator2 = Operator(
        name="modus_ponens_2",
        operator_type=OperatorType.TRANSFORMATION,
        arity=1
    )
    builder.apply(implies_operator2, "From B and B→C, derive C")
    
    # 4. Conclude A → C
    proof = builder.conclude(theorem_statement, "By transitivity")
    
    # Validate proof
    print(f"\nProof complete: {proof.is_complete()}")
    print(f"Proof valid: {proof.verify()}")
    print(f"Number of steps: {len(proof.steps)}")
    print(f"Theorem proven: {theorem.is_proven}")
    
    # Show proof steps
    print("\n=== Proof Steps ===")
    for i, step in enumerate(proof.steps):
        print(f"Step {i+1}: {step.step_type.value} - {step.justification}")
    
    # Convert to record
    record = proof.to_record()
    print(f"\nProof as Record:")
    print(f"  Closed: {record.has_closure}")
    print(f"  Valid: {record.validate()}")
    print(f"  Operators: {len(record.operators)}")
    
    return ps

if __name__ == "__main__":
    example_simple_proof()
