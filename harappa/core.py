"""
Core components of the Harappa Operational Mathematics system.

This module defines the fundamental building blocks:
- Symbols: Basic units representing entities or concepts
- Operators: Transformations and qualifications
- States: Computational states
- Records: Compositions of symbols and operators
- ValidationEngine: Ensures formal correctness
"""

from enum import Enum
from typing import List, Set, Dict, Optional, Any
from dataclasses import dataclass, field


class SymbolType(Enum):
    """Types of symbols in the Harappa system."""
    ENTITY = "entity"  # Represents an object or agent
    RESOURCE = "resource"  # Represents a resource
    TRANSACTION = "transaction"  # Represents an action or transaction
    STATE = "state"  # Represents a state
    QUANTIFIER = "quantifier"  # Represents a quantity or measurement


class OperatorType(Enum):
    """Types of operators in the Harappa system."""
    QUALIFICATION = "qualification"  # Adds properties or constraints
    TRANSFORMATION = "transformation"  # Changes state
    COMPOSITION = "composition"  # Combines symbols
    VALIDATION = "validation"  # Validates correctness
    CLOSURE = "closure"  # Indicates completion


@dataclass
class Symbol:
    """
    A symbol in the Harappa system.
    
    Symbols are the basic units representing entities, resources, or concepts.
    Each symbol has a unique identifier and a type.
    """
    id: str
    symbol_type: SymbolType
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if not isinstance(other, Symbol):
            return False
        return self.id == other.id
    
    def __repr__(self):
        return f"Symbol({self.id}, {self.symbol_type.value})"
    
    def validate(self) -> bool:
        """Validate the symbol structure."""
        return bool(self.id) and isinstance(self.symbol_type, SymbolType)


@dataclass
class Operator:
    """
    An operator in the Harappa system.
    
    Operators perform transformations, qualifications, or validations on symbols.
    """
    name: str
    operator_type: OperatorType
    arity: int  # Number of symbols it operates on
    parameters: Dict[str, Any] = field(default_factory=dict)
    
    def apply(self, symbols: List[Symbol]) -> 'State':
        """
        Apply the operator to a list of symbols.
        
        Args:
            symbols: List of symbols to operate on
            
        Returns:
            New state after applying the operator
        """
        if len(symbols) != self.arity:
            raise ValueError(f"Operator {self.name} expects {self.arity} symbols, got {len(symbols)}")
        
        return State(
            symbols=symbols,
            operator=self,
            properties={"applied": True}
        )
    
    def __repr__(self):
        return f"Operator({self.name}, {self.operator_type.value}, arity={self.arity})"


@dataclass
class State:
    """
    A state in the Harappa system.
    
    States represent computational states with associated symbols and properties.
    """
    symbols: List[Symbol] = field(default_factory=list)
    operator: Optional[Operator] = None
    properties: Dict[str, Any] = field(default_factory=dict)
    is_final: bool = False
    
    def add_symbol(self, symbol: Symbol) -> None:
        """Add a symbol to this state."""
        self.symbols.append(symbol)
    
    def apply_operator(self, operator: Operator, target_symbols: List[Symbol]) -> 'State':
        """
        Apply an operator to specified symbols in this state.
        
        Args:
            operator: The operator to apply
            target_symbols: Symbols to apply the operator to
            
        Returns:
            New state resulting from the operation
        """
        return operator.apply(target_symbols)
    
    def validate(self) -> bool:
        """Validate the state structure."""
        return all(symbol.validate() for symbol in self.symbols)
    
    def __repr__(self):
        return f"State(symbols={len(self.symbols)}, final={self.is_final})"


@dataclass
class Record:
    """
    A Harappa record - a complete composition of symbols and operators.
    
    Records represent complete transactions, proofs, or processes in the system.
    They have a closure indicator showing they are complete and valid.
    """
    symbols: List[Symbol] = field(default_factory=list)
    operators: List[Operator] = field(default_factory=list)
    states: List[State] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    has_closure: bool = False
    
    def add_symbol(self, symbol: Symbol) -> None:
        """Add a symbol to the record."""
        self.symbols.append(symbol)
    
    def add_operator(self, operator: Operator) -> None:
        """Add an operator to the record."""
        self.operators.append(operator)
    
    def add_state(self, state: State) -> None:
        """Add a state to the record."""
        self.states.append(state)
    
    def close(self) -> None:
        """Mark the record as closed/complete."""
        self.has_closure = True
    
    def validate(self) -> bool:
        """Validate the entire record."""
        if not self.has_closure:
            return False
        
        if not all(symbol.validate() for symbol in self.symbols):
            return False
        
        if not all(state.validate() for state in self.states):
            return False
        
        return True
    
    def __repr__(self):
        return f"Record(symbols={len(self.symbols)}, operators={len(self.operators)}, closed={self.has_closure})"


class ValidationEngine:
    """
    Validation engine for Harappa records and states.
    
    Ensures formal correctness and adherence to system rules.
    """
    
    def __init__(self):
        self.rules: List[Any] = []
        self.errors: List[str] = []
    
    def add_rule(self, rule: Any) -> None:
        """Add a validation rule."""
        self.rules.append(rule)
    
    def validate_record(self, record: Record) -> bool:
        """
        Validate a complete record.
        
        Args:
            record: The record to validate
            
        Returns:
            True if valid, False otherwise
        """
        self.errors = []
        
        # Check basic structure
        if not record.validate():
            self.errors.append("Record failed basic validation")
            return False
        
        # Check closure
        if not record.has_closure:
            self.errors.append("Record lacks closure")
            return False
        
        # Check all states
        for i, state in enumerate(record.states):
            if not state.validate():
                self.errors.append(f"State {i} is invalid")
                return False
        
        # Apply custom rules
        for rule in self.rules:
            if callable(rule):
                if not rule(record):
                    self.errors.append(f"Rule {rule.__name__} failed")
                    return False
        
        return True
    
    def validate_state_transition(self, from_state: State, to_state: State, operator: Operator) -> bool:
        """
        Validate a state transition.
        
        Args:
            from_state: Initial state
            to_state: Target state
            operator: Operator performing the transition
            
        Returns:
            True if transition is valid, False otherwise
        """
        # Basic validation
        if not from_state.validate() or not to_state.validate():
            return False
        
        # Check operator compatibility
        if operator.arity > len(from_state.symbols):
            self.errors.append("Not enough symbols for operator")
            return False
        
        return True
    
    def get_errors(self) -> List[str]:
        """Get list of validation errors."""
        return self.errors
