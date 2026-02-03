"""
Harappa Formal Specification Language

Implements Proposal 1: Harappa as a formal specification language for
smart contracts and formal protocols.

Features:
- State machine definition using Harappa symbols and operators
- Formal guarantees of termination and non-ambiguity
- Contract specification with invariants and pre/post conditions
"""

from typing import List, Dict, Set, Optional, Callable, Any
from dataclasses import dataclass, field
from enum import Enum

from .core import Symbol, Operator, State, Record, SymbolType, OperatorType


class TransitionType(Enum):
    """Types of state transitions in state machines."""
    DETERMINISTIC = "deterministic"  # Single next state
    NON_DETERMINISTIC = "non_deterministic"  # Multiple possible next states
    CONDITIONAL = "conditional"  # Next state based on condition


@dataclass
class Transition:
    """A state transition in a state machine."""
    from_state: str
    to_state: str
    operator: Operator
    condition: Optional[Callable[[State], bool]] = None
    transition_type: TransitionType = TransitionType.DETERMINISTIC
    
    def can_transition(self, current_state: State) -> bool:
        """Check if transition can occur from current state."""
        if self.condition:
            return self.condition(current_state)
        return True
    
    def __repr__(self):
        return f"Transition({self.from_state} -> {self.to_state})"


@dataclass
class StateMachine:
    """
    A Harappa state machine.
    
    Defines a finite state machine using Harappa symbols and operators.
    Guarantees termination and determinism for formal verification.
    """
    name: str
    states: Dict[str, State] = field(default_factory=dict)
    transitions: List[Transition] = field(default_factory=list)
    initial_state: Optional[str] = None
    final_states: Set[str] = field(default_factory=set)
    invariants: List[Callable[[State], bool]] = field(default_factory=list)
    
    def add_state(self, name: str, state: State) -> None:
        """Add a state to the state machine."""
        self.states[name] = state
        if self.initial_state is None:
            self.initial_state = name
    
    def add_transition(self, transition: Transition) -> None:
        """Add a transition to the state machine."""
        if transition.from_state not in self.states:
            raise ValueError(f"Source state {transition.from_state} not found")
        if transition.to_state not in self.states:
            raise ValueError(f"Target state {transition.to_state} not found")
        self.transitions.append(transition)
    
    def add_final_state(self, state_name: str) -> None:
        """Mark a state as final."""
        if state_name not in self.states:
            raise ValueError(f"State {state_name} not found")
        self.final_states.add(state_name)
    
    def add_invariant(self, invariant: Callable[[State], bool]) -> None:
        """Add a state invariant that must hold in all states."""
        self.invariants.append(invariant)
    
    def get_transitions_from(self, state_name: str) -> List[Transition]:
        """Get all transitions from a given state."""
        return [t for t in self.transitions if t.from_state == state_name]
    
    def is_deterministic(self) -> bool:
        """Check if the state machine is deterministic."""
        for state_name in self.states:
            transitions = self.get_transitions_from(state_name)
            # Check for multiple transitions with same operator
            operators = [t.operator.name for t in transitions]
            if len(operators) != len(set(operators)):
                return False
        return True
    
    def has_termination_guarantee(self) -> bool:
        """
        Check if the state machine guarantees termination.
        
        A simple check: all states must have a path to a final state.
        """
        if not self.final_states:
            return False
        
        # BFS to check reachability of final states from all states
        for state_name in self.states:
            if state_name in self.final_states:
                continue
            
            visited = set()
            queue = [state_name]
            found_final = False
            
            while queue and not found_final:
                current = queue.pop(0)
                if current in visited:
                    continue
                visited.add(current)
                
                if current in self.final_states:
                    found_final = True
                    break
                
                transitions = self.get_transitions_from(current)
                for t in transitions:
                    if t.to_state not in visited:
                        queue.append(t.to_state)
            
            if not found_final:
                return False
        
        return True
    
    def validate(self) -> bool:
        """Validate the state machine structure."""
        if not self.initial_state:
            return False
        if not self.final_states:
            return False
        if not self.has_termination_guarantee():
            return False
        
        # Check all invariants
        for state in self.states.values():
            for invariant in self.invariants:
                if not invariant(state):
                    return False
        
        return True
    
    def to_record(self) -> Record:
        """Convert the state machine to a Harappa record."""
        record = Record()
        record.metadata["name"] = self.name
        record.metadata["type"] = "state_machine"
        
        # Add all states
        for state in self.states.values():
            record.add_state(state)
        
        # Add all transition operators
        for transition in self.transitions:
            record.add_operator(transition.operator)
        
        # Mark as closed if valid
        if self.validate():
            record.close()
        
        return record
    
    def __repr__(self):
        return f"StateMachine({self.name}, states={len(self.states)}, transitions={len(self.transitions)})"


@dataclass
class Contract:
    """
    A formal contract specification using Harappa.
    
    Defines pre-conditions, post-conditions, and invariants for contract methods.
    """
    name: str
    state_machine: StateMachine
    methods: Dict[str, 'ContractMethod'] = field(default_factory=dict)
    global_invariants: List[Callable[[State], bool]] = field(default_factory=list)
    
    def add_method(self, method: 'ContractMethod') -> None:
        """Add a method to the contract."""
        self.methods[method.name] = method
    
    def validate(self) -> bool:
        """Validate the entire contract."""
        if not self.state_machine.validate():
            return False
        
        for method in self.methods.values():
            if not method.validate():
                return False
        
        return True
    
    def __repr__(self):
        return f"Contract({self.name}, methods={len(self.methods)})"


@dataclass
class ContractMethod:
    """A method in a contract with pre/post conditions."""
    name: str
    preconditions: List[Callable[[State], bool]] = field(default_factory=list)
    postconditions: List[Callable[[State], bool]] = field(default_factory=list)
    state_transitions: List[Transition] = field(default_factory=list)
    
    def validate(self) -> bool:
        """Validate the method specification."""
        # Methods must have at least one pre or post condition
        return bool(self.preconditions or self.postconditions)
    
    def __repr__(self):
        return f"ContractMethod({self.name})"


class HarappaSpec:
    """
    Main interface for Harappa specification language.
    
    Provides methods to create and validate formal specifications.
    """
    
    def __init__(self):
        self.contracts: Dict[str, Contract] = {}
        self.state_machines: Dict[str, StateMachine] = {}
    
    def create_state_machine(self, name: str) -> StateMachine:
        """Create a new state machine."""
        sm = StateMachine(name=name)
        self.state_machines[name] = sm
        return sm
    
    def create_contract(self, name: str, state_machine: StateMachine) -> Contract:
        """Create a new contract."""
        contract = Contract(name=name, state_machine=state_machine)
        self.contracts[name] = contract
        return contract
    
    def validate_all(self) -> bool:
        """Validate all specifications."""
        for sm in self.state_machines.values():
            if not sm.validate():
                return False
        
        for contract in self.contracts.values():
            if not contract.validate():
                return False
        
        return True
    
    def get_contract(self, name: str) -> Optional[Contract]:
        """Get a contract by name."""
        return self.contracts.get(name)
    
    def get_state_machine(self, name: str) -> Optional[StateMachine]:
        """Get a state machine by name."""
        return self.state_machines.get(name)
