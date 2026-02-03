"""
Indus Script Automaton Implementation
A finite-state automaton for validating Harappan administrative notation sequences.
"""

from enum import Enum
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass


class State(Enum):
    """States of the Indus automaton"""
    S0 = "INICIAL"  # Initial state - no symbol processed
    S1 = "ENTIDADE_DEFINIDA"  # Entity recognized
    S2 = "QUALIFICADA"  # Qualification operators applied
    S3 = "QUANTIFICADA"  # Quantity specified
    S4 = "RELACIONADA"  # Relation established
    S5 = "FECHADA"  # Closure applied - ACCEPTING STATE


class SymbolClass(Enum):
    """Symbol classes for the Indus script"""
    ENT_OVAL = "ENT_OVAL"  # 373-399: Basic institutional entities
    ENT_U = "ENT_U"  # 328-339: Containers/vessels
    ENT_HASTE = "ENT_HASTE"  # 250-260: Authority/hierarchy
    ENT_ANIMAL = "ENT_ANIMAL"  # 200-210: Functional agents
    ENT_METRICA = "ENT_METRICA"  # 100-150: Measures/quantities
    OP_QUAL = "OP_QUAL"  # Dot, Stroke: Qualification
    OP_COUNT = "OP_COUNT"  # 410-417: Counting/aggregation
    OP_REL = "OP_REL"  # 400-409: Binary relations
    OP_CLOSE = "OP_CLOSE"  # 342-348: Terminal closure
    OP_SCOPE = "OP_SCOPE"  # Bracket: Scope delimitation


@dataclass
class Symbol:
    """Represents a Harappan symbol"""
    id: int
    symbol_class: SymbolClass
    description: str
    frequency: Optional[int] = None


class IndusAutomaton:
    """
    Finite-state automaton for validating Indus script sequences.
    
    The automaton implements the formal model:
    S = (B, O, Σ, R, F)
    where:
    - B: Base bodies (≈30 ontological classes)
    - O: Graphic operators (≈15 universal modifiers)
    - Σ: Valid states (417 catalogued symbols)
    - R: Composition rules (from tables II-IV)
    - F: Final states (family 342-348 + specialized closers)
    """
    
    def __init__(self):
        self.states = list(State)
        self.current_state = State.S0
        self.history: List[Tuple[State, SymbolClass]] = []
        
        # Define transition table δ(state, symbol_class) -> new_state
        self.transitions: Dict[Tuple[State, SymbolClass], State] = {
            # From S0 (initial) - any entity starts the sequence
            (State.S0, SymbolClass.ENT_OVAL): State.S1,
            (State.S0, SymbolClass.ENT_U): State.S1,
            (State.S0, SymbolClass.ENT_HASTE): State.S1,
            (State.S0, SymbolClass.ENT_ANIMAL): State.S1,
            (State.S0, SymbolClass.ENT_METRICA): State.S1,
            
            # From S1 (entity defined)
            (State.S1, SymbolClass.OP_QUAL): State.S2,
            (State.S1, SymbolClass.OP_COUNT): State.S3,
            (State.S1, SymbolClass.OP_REL): State.S4,
            (State.S1, SymbolClass.OP_CLOSE): State.S5,
            
            # From S2 (qualified)
            (State.S2, SymbolClass.OP_COUNT): State.S3,
            (State.S2, SymbolClass.OP_REL): State.S4,
            (State.S2, SymbolClass.OP_CLOSE): State.S5,
            (State.S2, SymbolClass.OP_QUAL): State.S2,  # Allow multiple qualifications
            
            # From S3 (quantified)
            (State.S3, SymbolClass.OP_COUNT): State.S3,  # Allow multiple counts
            (State.S3, SymbolClass.OP_REL): State.S4,
            (State.S3, SymbolClass.OP_CLOSE): State.S5,
            
            # From S4 (related)
            (State.S4, SymbolClass.OP_CLOSE): State.S5,
        }
    
    def reset(self):
        """Reset the automaton to initial state"""
        self.current_state = State.S0
        self.history.clear()
    
    def process_symbol(self, symbol_class: SymbolClass) -> bool:
        """
        Process a single symbol through the automaton.
        
        Args:
            symbol_class: The class of the symbol to process
            
        Returns:
            True if transition is valid, False otherwise
        """
        key = (self.current_state, symbol_class)
        
        if key in self.transitions:
            old_state = self.current_state
            self.current_state = self.transitions[key]
            self.history.append((old_state, symbol_class))
            return True
        
        return False
    
    def process_sequence(self, symbol_classes: List[SymbolClass]) -> bool:
        """
        Process a sequence of symbols.
        
        Args:
            symbol_classes: List of symbol classes to process
            
        Returns:
            True if entire sequence is valid and reaches accepting state
        """
        self.reset()
        
        for symbol_class in symbol_classes:
            if not self.process_symbol(symbol_class):
                return False
        
        return self.is_valid_record()
    
    def is_valid_record(self) -> bool:
        """
        Check if current state is an accepting state.
        
        Returns:
            True if in state S5 (FECHADA/CLOSED)
        """
        return self.current_state == State.S5
    
    def get_current_state(self) -> State:
        """Get the current state of the automaton"""
        return self.current_state
    
    def get_history(self) -> List[Tuple[State, SymbolClass]]:
        """Get the processing history"""
        return self.history.copy()
    
    def get_possible_transitions(self) -> List[SymbolClass]:
        """
        Get list of symbol classes that can be processed from current state.
        
        Returns:
            List of valid symbol classes for next transition
        """
        possible = []
        for (state, symbol_class), _ in self.transitions.items():
            if state == self.current_state and symbol_class not in possible:
                possible.append(symbol_class)
        return possible


class IndusSymbolMapper:
    """Maps Indus symbol IDs to their classes and properties"""
    
    def __init__(self):
        # Symbol ID ranges mapped to classes
        self.symbol_map: Dict[int, SymbolClass] = {}
        self._initialize_mappings()
    
    def _initialize_mappings(self):
        """Initialize the symbol ID to class mappings"""
        # ENT_OVAL: 373-399
        for i in range(373, 400):
            self.symbol_map[i] = SymbolClass.ENT_OVAL
        
        # ENT_U: 328-339
        for i in range(328, 340):
            self.symbol_map[i] = SymbolClass.ENT_U
        
        # ENT_HASTE: 250-260
        for i in range(250, 261):
            self.symbol_map[i] = SymbolClass.ENT_HASTE
        
        # ENT_ANIMAL: 200-210
        for i in range(200, 211):
            self.symbol_map[i] = SymbolClass.ENT_ANIMAL
        
        # ENT_METRICA: 100-150
        for i in range(100, 151):
            self.symbol_map[i] = SymbolClass.ENT_METRICA
        
        # OP_REL: 400-409
        for i in range(400, 410):
            self.symbol_map[i] = SymbolClass.OP_REL
        
        # OP_COUNT: 410-417
        for i in range(410, 418):
            self.symbol_map[i] = SymbolClass.OP_COUNT
        
        # OP_CLOSE: 342-348
        for i in range(342, 349):
            self.symbol_map[i] = SymbolClass.OP_CLOSE
    
    def get_symbol_class(self, symbol_id: int) -> Optional[SymbolClass]:
        """
        Get the class for a given symbol ID.
        
        Args:
            symbol_id: The numeric ID of the symbol
            
        Returns:
            The SymbolClass if found, None otherwise
        """
        return self.symbol_map.get(symbol_id)
    
    def classify_sequence(self, symbol_ids: List[int]) -> Optional[List[SymbolClass]]:
        """
        Classify a sequence of symbol IDs into symbol classes.
        
        Args:
            symbol_ids: List of symbol IDs
            
        Returns:
            List of SymbolClass objects if all IDs are valid, None otherwise
        """
        classes = []
        for symbol_id in symbol_ids:
            symbol_class = self.get_symbol_class(symbol_id)
            if symbol_class is None:
                return None
            classes.append(symbol_class)
        return classes


def validate_indus_sequence(symbol_ids: List[int]) -> Tuple[bool, Optional[str]]:
    """
    Validate a sequence of Indus symbol IDs.
    
    Args:
        symbol_ids: List of symbol IDs to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    mapper = IndusSymbolMapper()
    automaton = IndusAutomaton()
    
    # Classify symbols
    symbol_classes = mapper.classify_sequence(symbol_ids)
    if symbol_classes is None:
        return False, "Invalid symbol ID in sequence"
    
    # Process through automaton
    is_valid = automaton.process_sequence(symbol_classes)
    
    if not is_valid:
        if not automaton.is_valid_record():
            return False, f"Sequence does not end in accepting state. Current state: {automaton.get_current_state().value}"
        else:
            return False, "Invalid transition in sequence"
    
    return True, None


if __name__ == "__main__":
    # Example usage
    print("Indus Script Automaton - Example Validation")
    print("=" * 50)
    
    # Valid sequence: Entity -> Qualification -> Closure
    sequence1 = [373, 342]  # Basic entity + simple closure
    valid, error = validate_indus_sequence(sequence1)
    print(f"Sequence {sequence1}: {'VALID' if valid else 'INVALID'}")
    if error:
        print(f"  Error: {error}")
    
    # Valid sequence with qualification
    sequence2 = [373, 410, 342]  # Entity + count + closure
    valid, error = validate_indus_sequence(sequence2)
    print(f"Sequence {sequence2}: {'VALID' if valid else 'INVALID'}")
    if error:
        print(f"  Error: {error}")
    
    # Invalid sequence (no closure)
    sequence3 = [373, 410]  # Entity + count (no closure)
    valid, error = validate_indus_sequence(sequence3)
    print(f"Sequence {sequence3}: {'VALID' if valid else 'INVALID'}")
    if error:
        print(f"  Error: {error}")
