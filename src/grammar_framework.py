"""
Discrete State Grammar Framework

Models Indus script as a discrete state grammar (finite automaton) rather than
making claims about quantum processes. Uses quantum terminology ONLY as analogies
for constraint satisfaction and state transitions.

Note: This is NOT a claim of physical quantum processes in artifacts.
We use quantum-inspired terminology as mathematical analogies for:
- "Superposition" = ambiguity of classification before validation
- "Measurement" = validation/closure that resolves ambiguity
- "Entanglement" = strong statistical correlation (not physical entanglement)
"""

from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class SymbolState(Enum):
    """
    Discrete states a symbol or sequence can occupy.
    
    These represent validation stages in institutional communication.
    """
    EXISTENTIAL = "existential"  # Symbol exists
    INSTANCED = "instanced"  # Symbol instantiated in context
    DELIMITED = "delimited"  # Symbol within boundaries
    AUTHORIZED = "authorized"  # Symbol validated by authority
    CLOSED = "closed"  # Sequence finalized/sealed


@dataclass
class StateTransition:
    """Represents a transition between states."""
    from_state: SymbolState
    to_state: SymbolState
    operator: str  # Symbol or operation that triggers transition
    condition: Optional[str] = None  # Additional constraint


class DiscreteStateGrammar:
    """
    Finite automaton model for Indus script sequences.
    
    Each sequence follows a path through discrete states, with transitions
    governed by symbols and structural rules.
    """
    
    def __init__(self):
        self.states = set(SymbolState)
        self.transitions: List[StateTransition] = []
        self.initial_state = SymbolState.EXISTENTIAL
        self.final_states = {SymbolState.CLOSED}
        
        # Define default transitions
        self._initialize_transitions()
    
    def _initialize_transitions(self):
        """Initialize default state transitions."""
        # Example transitions (would be learned from data)
        self.add_transition(
            SymbolState.EXISTENTIAL,
            SymbolState.INSTANCED,
            "any_symbol",
            "symbol_appears"
        )
        self.add_transition(
            SymbolState.INSTANCED,
            SymbolState.DELIMITED,
            "structural_marker",
            "context_established"
        )
        self.add_transition(
            SymbolState.DELIMITED,
            SymbolState.AUTHORIZED,
            "authority_marker",
            "validation_performed"
        )
        self.add_transition(
            SymbolState.AUTHORIZED,
            SymbolState.CLOSED,
            "closer_symbol",
            "sequence_finalized"
        )
    
    def add_transition(
        self,
        from_state: SymbolState,
        to_state: SymbolState,
        operator: str,
        condition: Optional[str] = None
    ):
        """Add a state transition to the grammar."""
        transition = StateTransition(from_state, to_state, operator, condition)
        self.transitions.append(transition)
    
    def get_valid_transitions(self, current_state: SymbolState) -> List[StateTransition]:
        """Get all valid transitions from current state."""
        return [t for t in self.transitions if t.from_state == current_state]
    
    def is_valid_sequence(
        self,
        sequence: List[str],
        symbol_to_operator: Optional[Dict[str, str]] = None
    ) -> Tuple[bool, List[SymbolState]]:
        """
        Check if a sequence follows valid state transitions.
        
        Args:
            sequence: Symbol sequence to validate
            symbol_to_operator: Mapping from symbols to operators
        
        Returns:
            Tuple of (is_valid, state_path)
        """
        if symbol_to_operator is None:
            symbol_to_operator = {s: "any_symbol" for s in sequence}
        
        current_state = self.initial_state
        state_path = [current_state]
        
        for symbol in sequence:
            operator = symbol_to_operator.get(symbol, "any_symbol")
            
            # Find valid transition
            valid_transitions = [
                t for t in self.get_valid_transitions(current_state)
                if t.operator == operator or t.operator == "any_symbol"
            ]
            
            if not valid_transitions:
                return False, state_path
            
            # Take first valid transition (could be more sophisticated)
            transition = valid_transitions[0]
            current_state = transition.to_state
            state_path.append(current_state)
        
        # Check if ended in final state
        is_valid = current_state in self.final_states
        
        return is_valid, state_path
    
    def constrained_configurations(
        self,
        sequences: List[List[str]],
        symbol_to_operator: Optional[Dict[str, str]] = None
    ) -> Dict[str, int]:
        """
        Identify sequences that follow constrained configurations.
        
        Returns statistics on valid vs invalid sequences.
        
        Args:
            sequences: List of sequences to analyze
            symbol_to_operator: Mapping from symbols to operators
        
        Returns:
            Dictionary with statistics
        """
        valid_count = 0
        invalid_count = 0
        state_distribution = {}
        
        for seq in sequences:
            is_valid, state_path = self.is_valid_sequence(seq, symbol_to_operator)
            
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1
            
            # Track final states
            final_state = state_path[-1] if state_path else self.initial_state
            state_distribution[final_state.value] = state_distribution.get(final_state.value, 0) + 1
        
        return {
            'valid': valid_count,
            'invalid': invalid_count,
            'total': len(sequences),
            'validity_rate': valid_count / len(sequences) if sequences else 0,
            'state_distribution': state_distribution
        }


class ConstraintSatisfactionAnalogy:
    """
    Quantum-inspired terminology as analogy for constraint satisfaction.
    
    IMPORTANT: This is purely analogical. No claim of physical quantum processes.
    
    Terminology mapping:
    - "Superposition" → Ambiguous classification before constraints applied
    - "Measurement" → Constraint satisfaction / validation that resolves ambiguity
    - "Collapse" → Transition to definite state
    - "Entanglement" → Strong statistical correlation between symbols
    """
    
    @staticmethod
    def explain_superposition_analogy() -> str:
        """Explain superposition as constraint ambiguity."""
        return """
        ANALOGY: "Superposition" in this context means:
        
        Before a sequence is validated (before "measurement"), a symbol may 
        belong to multiple possible classes or roles. The validation process
        (constraint satisfaction) resolves this ambiguity.
        
        Mathematical: A symbol s has possible classifications {c1, c2, ..., cn}
        with probabilities {p1, p2, ..., pn}. After constraint checking,
        one classification is selected.
        
        This is NOT quantum superposition. It's classical uncertainty resolved
        by validation.
        """
    
    @staticmethod
    def explain_measurement_analogy() -> str:
        """Explain measurement as validation."""
        return """
        ANALOGY: "Measurement" in this context means:
        
        The validation or closure operation that determines whether a sequence
        satisfies institutional constraints. Like measurement "collapses"
        quantum superposition, validation "collapses" classification ambiguity.
        
        Mathematical: Apply constraint function C to sequence S:
        - If C(S) = True, sequence is validated (enters "closed" state)
        - If C(S) = False, sequence is invalid
        
        This is NOT quantum measurement. It's constraint checking.
        """
    
    @staticmethod
    def explain_entanglement_analogy() -> str:
        """Explain entanglement as correlation."""
        return """
        ANALOGY: "Entanglement" in this context means:
        
        Strong statistical correlation between symbols that cannot be explained
        by their individual frequencies alone. When symbol A appears, symbol B
        is much more likely to appear than chance would predict.
        
        Mathematical: PMI(A,B) >> 0, indicating positive association.
        
        This is NOT quantum entanglement. It's statistical correlation /
        co-occurrence constraint.
        
        Better terms:
        - "Non-local invariance" (pattern stable across sites)
        - "Distributed standardization" (same rules apply everywhere)
        - "Long-range correlation" (symbols far apart still correlated)
        """


def create_default_grammar() -> DiscreteStateGrammar:
    """
    Create default grammar with common Indus script patterns.
    
    Returns:
        Configured DiscreteStateGrammar
    """
    grammar = DiscreteStateGrammar()
    
    # Could add more sophisticated transitions based on data
    # For now, returns basic grammar
    
    return grammar
