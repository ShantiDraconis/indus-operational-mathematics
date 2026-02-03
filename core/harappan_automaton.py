"""
Harappan Automaton - Core State Machine Implementation

This module implements the foundational automaton for Harappan operational mathematics,
based on the analysis of Indus Valley Civilization inscriptions.

The system models:
- Entities (symbols 373-399): Initial states
- Operators (Dot, Stroke, etc.): State transitions
- Closures (symbols 342-348): Terminal states
- Relations (symbols 400-409): Inter-entity connections
"""

from typing import List, Set, Tuple, Optional, Dict
from enum import Enum
from dataclasses import dataclass


class State(Enum):
    """States in the Harappan automaton"""
    S0 = "INITIAL"
    S1 = "ENTITY_LOADED"
    S2 = "OPERATOR_APPLIED"
    S3 = "QUANTIFIED"
    S4 = "RELATED"
    S5 = "CLOSED"


class SymbolType(Enum):
    """Types of Harappan symbols"""
    ENTITY = "entity"  # 373-399
    OPERATOR = "operator"  # Graphical operators (dot, stroke, etc.)
    QUANTIFIER = "quantifier"  # |, ||, |||, etc.
    RELATION = "relation"  # 400-409
    CLOSURE = "closure"  # 342-348


@dataclass
class Symbol:
    """Represents a Harappan symbol"""
    id: int
    type: SymbolType
    graphical_form: str
    
    def __repr__(self):
        return f"Symbol({self.id}, {self.type.value}, '{self.graphical_form}')"


class HarappanAutomaton:
    """
    Finite state automaton for validating Harappan inscriptions.
    
    Transition rules:
    S0 -> S1: Load Entity (373-399)
    S1 -> S2: Apply Operator (Dot, Stroke, etc.)
    S2 -> S3: Add Quantifier (|, ||, |||)
    S3 -> S4: Add Relation (400-409)
    S4 -> S5: Apply Closure (342-348)
    S1 -> S5: Direct closure (simple validation)
    """
    
    def __init__(self):
        self.current_state = State.S0
        self.inscription: List[Symbol] = []
        self.entity_count = 0
        
        # Define valid symbol sets
        self.entities = set(range(373, 400))  # 373-399
        self.closures = set(range(342, 349))  # 342-348
        self.relations = set(range(400, 410))  # 400-409
        
    def reset(self):
        """Reset automaton to initial state"""
        self.current_state = State.S0
        self.inscription = []
        self.entity_count = 0
        
    def add_entity(self, entity_id: int) -> bool:
        """
        Add an entity symbol (373-399)
        Transition: S0 -> S1
        """
        if entity_id not in self.entities:
            raise ValueError(f"Invalid entity ID: {entity_id}. Must be in range 373-399")
        
        if self.current_state != State.S0:
            return False
            
        symbol = Symbol(entity_id, SymbolType.ENTITY, f"E{entity_id}")
        self.inscription.append(symbol)
        self.current_state = State.S1
        self.entity_count += 1
        return True
        
    def add_operator(self, operator_name: str) -> bool:
        """
        Add an operator (dot, stroke, etc.)
        Transition: S1 -> S2
        """
        valid_operators = {'dot', 'stroke', 'vertical', 'horizontal', 'oblique'}
        
        if operator_name not in valid_operators:
            raise ValueError(f"Invalid operator: {operator_name}")
            
        if self.current_state != State.S1:
            return False
            
        symbol = Symbol(0, SymbolType.OPERATOR, operator_name)
        self.inscription.append(symbol)
        self.current_state = State.S2
        return True
        
    def add_quantifier(self, count: int) -> bool:
        """
        Add quantifier (|, ||, |||, etc.)
        Transition: S2 -> S3
        """
        if count < 1:
            raise ValueError("Quantifier count must be >= 1")
            
        if self.current_state != State.S2:
            return False
            
        graphical = '|' * count
        symbol = Symbol(count, SymbolType.QUANTIFIER, graphical)
        self.inscription.append(symbol)
        self.current_state = State.S3
        return True
        
    def add_relation(self, relation_id: int) -> bool:
        """
        Add relation symbol (400-409)
        Transition: S3 -> S4
        """
        if relation_id not in self.relations:
            raise ValueError(f"Invalid relation ID: {relation_id}. Must be in range 400-409")
            
        if self.current_state != State.S3:
            return False
            
        symbol = Symbol(relation_id, SymbolType.RELATION, f"R{relation_id}")
        self.inscription.append(symbol)
        self.current_state = State.S4
        return True
        
    def add_closure(self, closure_id: int) -> bool:
        """
        Add closure symbol (342-348)
        Transition: S1/S4 -> S5
        """
        if closure_id not in self.closures:
            raise ValueError(f"Invalid closure ID: {closure_id}. Must be in range 342-348")
            
        if self.current_state not in {State.S1, State.S4}:
            return False
            
        symbol = Symbol(closure_id, SymbolType.CLOSURE, f"C{closure_id}")
        self.inscription.append(symbol)
        self.current_state = State.S5
        return True
        
    def is_valid(self) -> bool:
        """Check if inscription is in valid closed state"""
        return self.current_state == State.S5
        
    def get_inscription(self) -> List[Symbol]:
        """Get current inscription sequence"""
        return self.inscription.copy()
        
    def validate_sequence(self, symbols: List[Tuple[str, int]]) -> bool:
        """
        Validate a sequence of symbols
        
        Args:
            symbols: List of tuples (type, value) where type is 'entity', 'operator', etc.
        
        Returns:
            True if sequence is valid, False otherwise
        """
        self.reset()
        
        try:
            for symbol_type, value in symbols:
                if symbol_type == 'entity':
                    if not self.add_entity(value):
                        return False
                elif symbol_type == 'operator':
                    if not self.add_operator(value):
                        return False
                elif symbol_type == 'quantifier':
                    if not self.add_quantifier(value):
                        return False
                elif symbol_type == 'relation':
                    if not self.add_relation(value):
                        return False
                elif symbol_type == 'closure':
                    if not self.add_closure(value):
                        return False
                else:
                    return False
                    
            return self.is_valid()
        except ValueError:
            return False
            
    def __repr__(self):
        symbols_str = ' → '.join([s.graphical_form for s in self.inscription])
        return f"HarappanAutomaton(state={self.current_state.value}, inscription=[{symbols_str}])"


# Pre-defined symbol mappings
ENTITY_MEANINGS = {
    373: "Person/Individual",
    374: "Group/Community",
    375: "Goods/Commodity",
    376: "Transaction",
    377: "Authority",
    378: "Location",
    379: "Time/Period",
    380: "Quantity/Measure",
}

CLOSURE_MEANINGS = {
    342: "Rejected",
    343: "Approved",
    344: "Pending",
    345: "Completed",
    346: "Cancelled",
    347: "Verified",
    348: "Archived",
}

RELATION_MEANINGS = {
    400: "Ownership",
    401: "Transfer",
    402: "Payment",
    403: "Debt",
    404: "Contract",
    405: "Inheritance",
    406: "Trade",
    407: "Taxation",
    408: "Service",
    409: "Alliance",
}
