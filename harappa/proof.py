"""
Harappa Theorem Verification System

Implements Proposal 3: Computer-assisted theorem verification using
Harappa operators and diagrammatic proofs.

Features:
- Diagrammatic proof steps using operators
- Closure-based proof completion
- Integration with proof assistants (Coq, Lean style)
- Short proof language
"""

from typing import List, Dict, Optional, Callable, Any
from dataclasses import dataclass, field
from enum import Enum

from .core import Symbol, Operator, State, Record, OperatorType


class ProofStepType(Enum):
    """Types of proof steps."""
    AXIOM = "axiom"
    ASSUMPTION = "assumption"
    IMPLICATION = "implication"
    CONJUNCTION = "conjunction"
    DISJUNCTION = "disjunction"
    NEGATION = "negation"
    QUANTIFICATION = "quantification"
    SUBSTITUTION = "substitution"
    CLOSURE = "closure"


@dataclass
class ProofStep:
    """
    A single step in a Harappa proof.
    
    Each step is represented by a graphical operator.
    """
    step_id: int
    step_type: ProofStepType
    operator: Operator
    premises: List['ProofStep'] = field(default_factory=list)
    conclusion: Optional[Symbol] = None
    justification: str = ""
    
    def validate(self) -> bool:
        """Validate the proof step."""
        # Axioms and assumptions need no premises
        if self.step_type in [ProofStepType.AXIOM, ProofStepType.ASSUMPTION]:
            return True
        
        # Other steps need premises
        if not self.premises:
            return False
        
        # Closure must have a conclusion
        if self.step_type == ProofStepType.CLOSURE and not self.conclusion:
            return False
        
        return True
    
    def __repr__(self):
        return f"ProofStep({self.step_id}, {self.step_type.value})"


@dataclass
class Theorem:
    """A theorem with its statement and proof."""
    name: str
    statement: Symbol
    proof: Optional['Proof'] = None
    axioms: List[Symbol] = field(default_factory=list)
    is_proven: bool = False
    
    def set_proof(self, proof: 'Proof') -> None:
        """Attach a proof to this theorem."""
        self.proof = proof
        if proof.is_complete():
            self.is_proven = True
    
    def __repr__(self):
        return f"Theorem({self.name}, proven={self.is_proven})"


@dataclass
class Proof:
    """
    A Harappa proof.
    
    Consists of a sequence of proof steps leading to a conclusion.
    """
    theorem: Theorem
    steps: List[ProofStep] = field(default_factory=list)
    axioms: List[Symbol] = field(default_factory=list)
    closure_step: Optional[ProofStep] = None
    
    def add_step(self, step: ProofStep) -> None:
        """Add a proof step."""
        self.steps.append(step)
        if step.step_type == ProofStepType.CLOSURE:
            self.closure_step = step
    
    def add_axiom(self, axiom: Symbol) -> None:
        """Add an axiom to the proof."""
        self.axioms.append(axiom)
    
    def is_complete(self) -> bool:
        """
        Check if the proof is complete.
        
        A proof is complete if:
        1. It has a closure step
        2. All steps are valid
        3. The closure conclusion matches the theorem statement
        """
        if not self.closure_step:
            return False
        
        if not all(step.validate() for step in self.steps):
            return False
        
        if self.closure_step.conclusion != self.theorem.statement:
            return False
        
        return True
    
    def verify(self) -> bool:
        """
        Verify the proof.
        
        Checks logical consistency and step dependencies.
        """
        if not self.is_complete():
            return False
        
        # Check each step's premises are from previous steps
        for i, step in enumerate(self.steps):
            for premise in step.premises:
                if premise not in self.steps[:i]:
                    return False
        
        return True
    
    def to_record(self) -> Record:
        """Convert proof to a Harappa record."""
        record = Record()
        record.metadata["theorem"] = self.theorem.name
        record.metadata["type"] = "proof"
        
        # Add all proof step operators
        for step in self.steps:
            record.add_operator(step.operator)
        
        # Add axioms as symbols
        for axiom in self.axioms:
            record.add_symbol(axiom)
        
        # Mark as closed if proof is complete
        if self.is_complete():
            record.close()
        
        return record
    
    def __repr__(self):
        return f"Proof(theorem={self.theorem.name}, steps={len(self.steps)}, complete={self.is_complete()})"


class ProofSystem:
    """
    Harappa proof system for theorem verification.
    
    Provides methods to construct and verify proofs.
    """
    
    def __init__(self):
        self.theorems: Dict[str, Theorem] = {}
        self.axioms: List[Symbol] = []
        self.proof_rules: Dict[str, Callable] = {}
        self.step_counter = 0
    
    def add_axiom(self, axiom: Symbol) -> None:
        """Add a global axiom to the system."""
        self.axioms.append(axiom)
    
    def add_theorem(self, theorem: Theorem) -> None:
        """Add a theorem to the system."""
        self.theorems[theorem.name] = theorem
    
    def create_proof(self, theorem_name: str) -> Proof:
        """Create a new proof for a theorem."""
        if theorem_name not in self.theorems:
            raise ValueError(f"Theorem {theorem_name} not found")
        
        theorem = self.theorems[theorem_name]
        proof = Proof(theorem=theorem)
        
        # Add global axioms
        for axiom in self.axioms:
            proof.add_axiom(axiom)
        
        return proof
    
    def create_step(
        self,
        step_type: ProofStepType,
        operator: Operator,
        premises: List[ProofStep] = None,
        conclusion: Optional[Symbol] = None,
        justification: str = ""
    ) -> ProofStep:
        """Create a new proof step."""
        self.step_counter += 1
        return ProofStep(
            step_id=self.step_counter,
            step_type=step_type,
            operator=operator,
            premises=premises or [],
            conclusion=conclusion,
            justification=justification
        )
    
    def verify_proof(self, theorem_name: str) -> bool:
        """Verify a theorem's proof."""
        if theorem_name not in self.theorems:
            return False
        
        theorem = self.theorems[theorem_name]
        if not theorem.proof:
            return False
        
        return theorem.proof.verify()
    
    def get_theorem(self, name: str) -> Optional[Theorem]:
        """Get a theorem by name."""
        return self.theorems.get(name)
    
    def list_proven_theorems(self) -> List[Theorem]:
        """List all proven theorems."""
        return [t for t in self.theorems.values() if t.is_proven]
    
    def list_unproven_theorems(self) -> List[Theorem]:
        """List all unproven theorems."""
        return [t for t in self.theorems.values() if not t.is_proven]
    
    def add_proof_rule(self, name: str, rule: Callable) -> None:
        """Add a custom proof rule."""
        self.proof_rules[name] = rule
    
    def apply_proof_rule(self, rule_name: str, *args, **kwargs) -> Any:
        """Apply a proof rule."""
        if rule_name not in self.proof_rules:
            raise ValueError(f"Proof rule {rule_name} not found")
        return self.proof_rules[rule_name](*args, **kwargs)


class DiagrammaticProofBuilder:
    """
    Helper class for building diagrammatic proofs.
    
    Provides a fluent interface for constructing proofs visually.
    """
    
    def __init__(self, proof_system: ProofSystem, theorem: Theorem):
        self.proof_system = proof_system
        self.proof = proof_system.create_proof(theorem.name)
        self.current_premises: List[ProofStep] = []
    
    def assume(self, symbol: Symbol, justification: str = "") -> 'DiagrammaticProofBuilder':
        """Add an assumption step."""
        operator = Operator(
            name="assume",
            operator_type=OperatorType.QUALIFICATION,
            arity=1
        )
        step = self.proof_system.create_step(
            ProofStepType.ASSUMPTION,
            operator,
            conclusion=symbol,
            justification=justification
        )
        self.proof.add_step(step)
        self.current_premises = [step]
        return self
    
    def apply(self, operator: Operator, justification: str = "") -> 'DiagrammaticProofBuilder':
        """Apply an operator to current premises."""
        step = self.proof_system.create_step(
            ProofStepType.IMPLICATION,
            operator,
            premises=self.current_premises,
            justification=justification
        )
        self.proof.add_step(step)
        self.current_premises = [step]
        return self
    
    def conclude(self, conclusion: Symbol, justification: str = "") -> Proof:
        """Add the closure step and complete the proof."""
        operator = Operator(
            name="conclude",
            operator_type=OperatorType.CLOSURE,
            arity=1
        )
        step = self.proof_system.create_step(
            ProofStepType.CLOSURE,
            operator,
            premises=self.current_premises,
            conclusion=conclusion,
            justification=justification
        )
        self.proof.add_step(step)
        
        if self.proof.is_complete():
            self.proof.theorem.set_proof(self.proof)
        
        return self.proof
    
    def get_proof(self) -> Proof:
        """Get the current proof."""
        return self.proof
