"""
Harappan Sequence Representation and Validation

This module implements the sequence representation and validation system
for Harappan texts, including JSON schema and finite automaton validation.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum
import json

from harappan_symbols import (
    Symbol, SymbolFamily, SymbolRegistry, CompositionSystem,
    create_harappan_system
)


class PositionType(Enum):
    """Syntactic position of a symbol in a sequence"""
    INITIAL = "initial"     # Start of text
    MEDIAL = "medial"       # Middle of text
    FINAL = "final"         # End of text
    STANDALONE = "standalone"  # Single symbol text


@dataclass
class SequenceElement:
    """
    A single element in a Harappan sequence
    """
    symbol_id: int
    position: PositionType
    
    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON representation"""
        return {
            "symbol": self.symbol_id,
            "position": self.position.value
        }


@dataclass
class HarappanSequence:
    """
    Represents a complete Harappan text sequence
    """
    elements: List[SequenceElement] = field(default_factory=list)
    object_type: Optional[str] = None  # seal, tablet, etc.
    provenance: Optional[str] = None
    
    def add_symbol(self, symbol_id: int):
        """Add a symbol to the sequence"""
        # Determine position
        if not self.elements:
            position = PositionType.INITIAL
        else:
            # Update previous final to medial
            if self.elements[-1].position == PositionType.INITIAL:
                self.elements[-1].position = PositionType.MEDIAL
            elif self.elements[-1].position == PositionType.FINAL:
                self.elements[-1].position = PositionType.MEDIAL
            position = PositionType.FINAL
        
        self.elements.append(SequenceElement(symbol_id, position))
    
    def to_json(self) -> Dict[str, Any]:
        """
        Convert sequence to modern JSON representation
        (as described in problem statement section 6)
        """
        result = {
            "sequence": [elem.to_json() for elem in self.elements],
            "length": len(self.elements)
        }
        
        if self.object_type:
            result["object_type"] = self.object_type
        if self.provenance:
            result["provenance"] = self.provenance
        
        # Extract functional components if recognizable
        entities = []
        relations = []
        counts = []
        
        for elem in self.elements:
            if 373 <= elem.symbol_id <= 399:
                entities.append(elem.symbol_id)
            elif 400 <= elem.symbol_id <= 409:
                relations.append(elem.symbol_id)
            elif 410 <= elem.symbol_id <= 417:
                counts.append(elem.symbol_id)
        
        if entities:
            result["entities"] = entities
        if relations:
            result["relations"] = relations
        if counts:
            result["counts"] = counts
        
        return result
    
    def to_functional_notation(self, registry: SymbolRegistry) -> str:
        """
        Convert to functional notation (section 6 of problem statement)
        Example: ∃x (Entity(x, 373) ∧ Count(x, 3) ∧ Linked(x, y) ∧ Closed(x))
        """
        parts = []
        
        for elem in self.elements:
            symbol = registry.get_symbol(elem.symbol_id)
            if symbol:
                if symbol.family == SymbolFamily.OMEGA:
                    parts.append(f"Entity({elem.symbol_id})")
                elif symbol.family == SymbolFamily.DELTA:
                    parts.append(f"Relation({elem.symbol_id})")
                elif symbol.family == SymbolFamily.SIGMA:
                    # Extract count from symbol
                    count = elem.symbol_id - 408  # 410 = 2, 411 = 3, etc.
                    parts.append(f"Count({count})")
        
        if len(parts) > 1:
            return "∃x (" + " ∧ ".join(parts) + ")"
        elif len(parts) == 1:
            return parts[0]
        else:
            return "∅"


class SyntacticRule:
    """
    Defines syntactic rules for valid symbol sequences
    """
    
    @staticmethod
    def validate_position(symbol_id: int, position: PositionType) -> bool:
        """
        Validate if a symbol can appear in a given position
        Based on frequency/distribution data (Table I from problem statement)
        """
        # Omega (entities) - can appear initial or medial
        if 373 <= symbol_id <= 399:
            return position in [PositionType.INITIAL, PositionType.MEDIAL, PositionType.STANDALONE]
        
        # Delta (relations) - typically medial
        elif 400 <= symbol_id <= 409:
            return position in [PositionType.MEDIAL]
        
        # Sigma (counts) - medial or final
        elif 410 <= symbol_id <= 417:
            return position in [PositionType.MEDIAL, PositionType.FINAL, PositionType.STANDALONE]
        
        # Closure operators (342-348 from U-family, mentioned in problem)
        # would typically be final
        elif 342 <= symbol_id <= 348:
            return position in [PositionType.FINAL]
        
        return True


class FiniteAutomaton:
    """
    Finite automaton for validating Harappan sequences
    (Section 7: "equivalente moderno: JSON + workflow + autômato finito")
    """
    
    class State(Enum):
        START = "start"
        ENTITY = "entity"
        RELATION = "relation"
        COUNT = "count"
        CLOSED = "closed"
        ERROR = "error"
    
    def __init__(self, registry: SymbolRegistry):
        self.registry = registry
        self.current_state = self.State.START
        self.sequence: List[int] = []
    
    def reset(self):
        """Reset automaton to initial state"""
        self.current_state = self.State.START
        self.sequence = []
    
    def transition(self, symbol_id: int) -> bool:
        """
        Process a symbol and transition to next state
        Returns True if transition is valid, False otherwise
        """
        symbol = self.registry.get_symbol(symbol_id)
        if not symbol:
            # Symbol not in 373-417 range, might be from other families
            # For now, accept it
            self.sequence.append(symbol_id)
            return True
        
        family = symbol.family
        
        # State transition logic
        if self.current_state == self.State.START:
            # Can start with entity
            if family == SymbolFamily.OMEGA:
                self.current_state = self.State.ENTITY
                self.sequence.append(symbol_id)
                return True
            # Or directly with count
            elif family == SymbolFamily.SIGMA:
                self.current_state = self.State.COUNT
                self.sequence.append(symbol_id)
                return True
        
        elif self.current_state == self.State.ENTITY:
            # Entity can be followed by relation
            if family == SymbolFamily.DELTA:
                self.current_state = self.State.RELATION
                self.sequence.append(symbol_id)
                return True
            # Or by count
            elif family == SymbolFamily.SIGMA:
                self.current_state = self.State.COUNT
                self.sequence.append(symbol_id)
                return True
            # Or by another entity
            elif family == SymbolFamily.OMEGA:
                self.sequence.append(symbol_id)
                return True
        
        elif self.current_state == self.State.RELATION:
            # Relation can be followed by entity
            if family == SymbolFamily.OMEGA:
                self.current_state = self.State.ENTITY
                self.sequence.append(symbol_id)
                return True
            # Or by count
            elif family == SymbolFamily.SIGMA:
                self.current_state = self.State.COUNT
                self.sequence.append(symbol_id)
                return True
        
        elif self.current_state == self.State.COUNT:
            # Count typically ends sequence or can be followed by closure
            self.current_state = self.State.CLOSED
            self.sequence.append(symbol_id)
            return True
        
        elif self.current_state == self.State.CLOSED:
            # Closed state is terminal
            return False
        
        # Invalid transition
        self.current_state = self.State.ERROR
        return False
    
    def validate_sequence(self, symbol_ids: List[int]) -> bool:
        """
        Validate an entire sequence
        Returns True if sequence is valid, False otherwise
        """
        self.reset()
        for symbol_id in symbol_ids:
            if not self.transition(symbol_id):
                return False
        # Accept if we're in a valid terminal state
        return self.current_state in [self.State.ENTITY, self.State.COUNT, self.State.CLOSED]
    
    def get_state(self) -> State:
        """Get current state"""
        return self.current_state


def create_sequence_from_json(json_data: Dict[str, Any], 
                              registry: SymbolRegistry) -> HarappanSequence:
    """
    Create a HarappanSequence from JSON representation
    """
    sequence = HarappanSequence()
    
    if "object_type" in json_data:
        sequence.object_type = json_data["object_type"]
    if "provenance" in json_data:
        sequence.provenance = json_data["provenance"]
    
    # Add symbols from sequence
    if "sequence" in json_data:
        for elem in json_data["sequence"]:
            symbol_id = elem["symbol"]
            sequence.add_symbol(symbol_id)
    
    return sequence


def validate_and_convert(symbol_ids: List[int]) -> Dict[str, Any]:
    """
    Convenience function to validate a sequence and convert to JSON
    """
    registry, composition = create_harappan_system()
    automaton = FiniteAutomaton(registry)
    
    is_valid = automaton.validate_sequence(symbol_ids)
    
    sequence = HarappanSequence()
    for symbol_id in symbol_ids:
        sequence.add_symbol(symbol_id)
    
    result = sequence.to_json()
    result["valid"] = is_valid
    result["functional_notation"] = sequence.to_functional_notation(registry)
    
    return result
