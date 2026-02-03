"""
Indus Script Deterministic Finite Automaton (DFA) Model

This module implements a DFA-based model of the Indus script operational system.
It can validate inscription sequences and analyze their operational structure.
"""

from enum import Enum
from typing import List, Optional, Set
from dataclasses import dataclass


class OperationType(Enum):
    """Enumeration of operational sign types."""
    INSTANTIATION = "INST"
    COUNTING = "COUNT"
    RELATION = "REL"
    QUALIFICATION = "QUAL"
    CLOSURE = "CLOSE"


class State(Enum):
    """States in the Indus DFA."""
    INITIAL = "q0"
    INSTANTIATED = "q1"
    COUNTED = "q2"
    RELATED = "q3"
    QUALIFIED = "q4"
    CLOSED = "q5"


@dataclass
class Sign:
    """Represents an Indus sign."""
    mahadevan_number: str
    operation_type: OperationType
    description: str = ""


class IndusDFA:
    """
    Deterministic Finite Automaton model of the Indus script.
    
    This class implements the formal model described in the monograph,
    recognizing valid Indus inscription sequences.
    """
    
    def __init__(self):
        """Initialize the DFA with states and transitions."""
        self.current_state = State.INITIAL
        self.accepting_states: Set[State] = {
            State.INSTANTIATED,
            State.COUNTED,
            State.RELATED,
            State.QUALIFIED,
            State.CLOSED
        }
        
        # Define transition function
        self.transitions = {
            (State.INITIAL, OperationType.INSTANTIATION): State.INSTANTIATED,
            (State.INSTANTIATED, OperationType.COUNTING): State.COUNTED,
            (State.INSTANTIATED, OperationType.RELATION): State.RELATED,
            (State.INSTANTIATED, OperationType.QUALIFICATION): State.QUALIFIED,
            (State.INSTANTIATED, OperationType.CLOSURE): State.CLOSED,
            (State.COUNTED, OperationType.COUNTING): State.COUNTED,
            (State.COUNTED, OperationType.QUALIFICATION): State.QUALIFIED,
            (State.COUNTED, OperationType.CLOSURE): State.CLOSED,
            (State.RELATED, OperationType.COUNTING): State.COUNTED,
            (State.RELATED, OperationType.QUALIFICATION): State.QUALIFIED,
            (State.RELATED, OperationType.CLOSURE): State.CLOSED,
            (State.QUALIFIED, OperationType.COUNTING): State.COUNTED,
            (State.QUALIFIED, OperationType.QUALIFICATION): State.QUALIFIED,
            (State.QUALIFIED, OperationType.CLOSURE): State.CLOSED,
        }
    
    def reset(self):
        """Reset the automaton to initial state."""
        self.current_state = State.INITIAL
    
    def transition(self, operation: OperationType) -> bool:
        """
        Attempt to transition to next state based on operation.
        
        Args:
            operation: The operation type of the current sign
            
        Returns:
            True if transition is valid, False otherwise
        """
        key = (self.current_state, operation)
        if key in self.transitions:
            self.current_state = self.transitions[key]
            return True
        return False
    
    def is_accepting(self) -> bool:
        """Check if current state is accepting."""
        return self.current_state in self.accepting_states
    
    def validate_inscription(self, signs: List[Sign]) -> bool:
        """
        Validate a complete inscription sequence.
        
        Args:
            signs: List of Sign objects representing the inscription
            
        Returns:
            True if the inscription is valid, False otherwise
        """
        self.reset()
        
        for sign in signs:
            if not self.transition(sign.operation_type):
                return False
        
        return self.is_accepting()
    
    def analyze_inscription(self, signs: List[Sign]) -> dict:
        """
        Analyze an inscription and return detailed information.
        
        Args:
            signs: List of Sign objects representing the inscription
            
        Returns:
            Dictionary containing analysis results
        """
        self.reset()
        trace = [State.INITIAL]
        
        for sign in signs:
            if self.transition(sign.operation_type):
                trace.append(self.current_state)
            else:
                return {
                    "valid": False,
                    "error": f"Invalid transition at sign {sign.mahadevan_number}",
                    "state_trace": trace,
                    "failed_operation": sign.operation_type
                }
        
        return {
            "valid": self.is_accepting(),
            "final_state": self.current_state,
            "state_trace": trace,
            "length": len(signs),
            "operations": [s.operation_type for s in signs]
        }


def create_example_signs() -> List[Sign]:
    """Create example sign sequences for testing."""
    # Example 1: [FISH][STROKE][TERMINAL]
    example1 = [
        Sign("M361", OperationType.INSTANTIATION, "Fish"),
        Sign("M328", OperationType.COUNTING, "Single stroke"),
        Sign("M411", OperationType.CLOSURE, "Terminal enclosure")
    ]
    
    # Example 2: [JAR][DOUBLE_STROKE]
    example2 = [
        Sign("M346", OperationType.INSTANTIATION, "Jar"),
        Sign("M329", OperationType.COUNTING, "Double stroke")
    ]
    
    # Example 3: [FISH] alone
    example3 = [
        Sign("M361", OperationType.INSTANTIATION, "Fish")
    ]
    
    return [example1, example2, example3]


if __name__ == "__main__":
    # Demonstration
    dfa = IndusDFA()
    examples = create_example_signs()
    
    for i, inscription in enumerate(examples, 1):
        print(f"\nExample {i}:")
        print(f"Signs: {[s.mahadevan_number for s in inscription]}")
        result = dfa.analyze_inscription(inscription)
        print(f"Valid: {result['valid']}")
        print(f"State trace: {[s.value for s in result['state_trace']]}")
