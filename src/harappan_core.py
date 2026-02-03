"""
Harappan Operational Mathematics - Core Implementation
This module implements the formal axiomatic system for Harappan mathematics.
"""

from enum import Enum
from typing import Set, List, Optional, Tuple
from dataclasses import dataclass


class SymbolClass(Enum):
    """Fundamental symbol classes (Axiom 1)"""
    ENT = "Entity"           # Entidade
    QUAL = "Qualifier"       # Qualificador
    COUNT = "Counter"        # Contador
    REL = "Relation"         # Relação
    CLOSE = "Closure"        # Fechamento
    SCOPE = "Scope"          # Escopo
    INT = "Internal"         # Interno


class State(Enum):
    """Automaton states (Axiom 9)"""
    Q0 = "Initial"
    Q1 = "Entity_Loaded"
    Q2 = "Qualified"
    Q3 = "Counted"
    Q4 = "Related"
    Q5 = "Closed"


@dataclass
class Symbol:
    """
    A Harappan symbol with form and function.
    Implements Axiom 1: Dualidade Forma-Função
    """
    id: int                          # Symbol identifier (1-417)
    symbol_class: SymbolClass        # Functional class
    base: Optional[int] = None       # Base body (if composite)
    modifiers: Set[str] = None       # Applied modifiers
    
    def __post_init__(self):
        if self.modifiers is None:
            self.modifiers = set()
    
    def __str__(self):
        mod_str = f"+{','.join(self.modifiers)}" if self.modifiers else ""
        return f"Symbol({self.id}{mod_str}:{self.symbol_class.name})"


@dataclass
class Inscription:
    """
    A sequence of symbols forming a valid inscription.
    Implements Axiom 4-6: Composition axioms
    """
    symbols: List[Symbol]
    
    def __str__(self):
        return " → ".join(str(s) for s in self.symbols)
    
    def is_valid(self) -> bool:
        """Check if inscription follows composition rules"""
        if not self.symbols:
            return True  # Empty inscription is valid (Axiom 4)
        
        # Axiom 4: First symbol must be ENT
        if self.symbols[0].symbol_class != SymbolClass.ENT:
            return False
        
        # Axiom 6: Last symbol must be CLOSE
        if self.symbols[-1].symbol_class != SymbolClass.CLOSE:
            return False
        
        # Axiom 5: Check linear order
        order = [SymbolClass.ENT, SymbolClass.QUAL, SymbolClass.COUNT, 
                 SymbolClass.REL, SymbolClass.CLOSE]
        
        prev_idx = -1
        for symbol in self.symbols:
            try:
                curr_idx = order.index(symbol.symbol_class)
                if curr_idx < prev_idx:
                    return False  # Order violation
                prev_idx = curr_idx
            except ValueError:
                # Symbol class not in strict order (SCOPE, INT allowed anywhere)
                pass
        
        # Axiom 3: Maximum length is 5
        if len(self.symbols) > 5:
            return False
        
        return True


class HarappanAutomaton:
    """
    Deterministic Finite Automaton for Harappan script validation.
    Implements Axioms 9-11: Dynamic axioms
    """
    
    def __init__(self):
        self.state = State.Q0
        self.processed_symbols: List[Symbol] = []
    
    def reset(self):
        """Reset automaton to initial state"""
        self.state = State.Q0
        self.processed_symbols = []
    
    def transition(self, symbol: Symbol) -> bool:
        """
        Execute state transition based on symbol class.
        Implements Axiom 9: Determinismo do Sistema
        Returns True if transition is valid, False otherwise.
        """
        # Axiom 11: Absorção do Fechamento
        if self.state == State.Q5:
            return True  # Absorbing state
        
        # Axiom 10: Progressão Monótona
        transitions = {
            State.Q0: {SymbolClass.ENT: State.Q1},
            State.Q1: {
                SymbolClass.QUAL: State.Q2,
                SymbolClass.COUNT: State.Q3,
                SymbolClass.REL: State.Q4,
                SymbolClass.CLOSE: State.Q5
            },
            State.Q2: {
                SymbolClass.COUNT: State.Q3,
                SymbolClass.REL: State.Q4,
                SymbolClass.CLOSE: State.Q5
            },
            State.Q3: {
                SymbolClass.REL: State.Q4,
                SymbolClass.CLOSE: State.Q5
            },
            State.Q4: {
                SymbolClass.CLOSE: State.Q5
            }
        }
        
        if self.state in transitions and symbol.symbol_class in transitions[self.state]:
            self.state = transitions[self.state][symbol.symbol_class]
            self.processed_symbols.append(symbol)
            return True
        
        return False
    
    def process_inscription(self, inscription: Inscription) -> bool:
        """
        Process entire inscription and validate.
        Implements Theorem 2: Decidibilidade
        """
        self.reset()
        
        for symbol in inscription.symbols:
            if not self.transition(symbol):
                return False
        
        # Must end in closed state
        return self.state == State.Q5


class CompositionEngine:
    """
    Symbol composition engine implementing the ⊕ operator.
    Implements Axiom 2: Composicionalidade Hierárquica
    """
    
    # Core modifiers (Axiom 24)
    CORE_MODIFIERS = {"Dot", "Stroke", "Line", "Circle", "Cross"}
    
    # All 15 modifiers
    ALL_MODIFIERS = {
        "Dot", "Stroke", "Line", "Circle", "Cross",
        "Comb", "Crown", "U-Shape", "Hook", "Fill",
        "Partition", "Roof", "Internal", "Direction", "Transition"
    }
    
    # 30 base bodies (simplified representation)
    BASE_BODIES = set(range(1, 31))
    
    @staticmethod
    def compose(base: int, modifiers: Set[str]) -> Symbol:
        """
        Compose a symbol from base and modifiers.
        Implements Axiom 2 and Axiom 18 (monoid structure)
        """
        # Validate base
        if base not in CompositionEngine.BASE_BODIES:
            raise ValueError(f"Invalid base body: {base}")
        
        # Validate modifiers
        if not modifiers.issubset(CompositionEngine.ALL_MODIFIERS):
            invalid = modifiers - CompositionEngine.ALL_MODIFIERS
            raise ValueError(f"Invalid modifiers: {invalid}")
        
        # Determine class based on base and modifiers (simplified)
        # In real implementation, this would use a lookup table
        symbol_class = CompositionEngine._determine_class(base, modifiers)
        
        # Create composite symbol
        # ID is computed from base and modifier combination
        symbol_id = base * 100 + len(modifiers)  # Simplified ID scheme
        
        return Symbol(
            id=symbol_id,
            symbol_class=symbol_class,
            base=base,
            modifiers=modifiers
        )
    
    @staticmethod
    def _determine_class(base: int, modifiers: Set[str]) -> SymbolClass:
        """
        Determine symbol class from base and modifiers.
        Implements Axiom 8: Herança de Propriedades
        """
        # Simplified class determination
        # In reality, this would be based on archaeological analysis
        if base <= 10:
            return SymbolClass.ENT
        elif base <= 15:
            return SymbolClass.QUAL
        elif base <= 20:
            return SymbolClass.COUNT
        elif base <= 25:
            return SymbolClass.REL
        else:
            return SymbolClass.CLOSE


class SemanticInterpreter:
    """
    Maps valid inscriptions to institutional world states.
    Implements Axiom 13-15: Semantic axioms
    """
    
    def __init__(self):
        self.institutional_world = {}  # Maps inscription to world state
    
    def interpret(self, inscription: Inscription) -> Optional[dict]:
        """
        Interpret a valid inscription as an institutional state.
        Implements Axiom 13: Correspondência Estado-Mundo
        """
        if not inscription.is_valid():
            return None
        
        # Create unique world state representation
        state = {
            "type": "institutional_state",
            "entity": inscription.symbols[0].id if inscription.symbols else None,
            "qualifiers": [s.id for s in inscription.symbols 
                          if s.symbol_class == SymbolClass.QUAL],
            "count": [s.id for s in inscription.symbols 
                     if s.symbol_class == SymbolClass.COUNT],
            "relations": [s.id for s in inscription.symbols 
                         if s.symbol_class == SymbolClass.REL],
            "closure": inscription.symbols[-1].id if inscription.symbols else None,
            "is_closed": True
        }
        
        # Store in institutional world (Axiom 14: no ambiguity)
        key = str(inscription)
        if key in self.institutional_world:
            # Check for ambiguity violation
            if self.institutional_world[key] != state:
                raise ValueError("Axiom 14 violation: Ambiguous interpretation")
        else:
            self.institutional_world[key] = state
        
        return state


def create_example_inscription() -> Inscription:
    """Create an example valid inscription"""
    # Entity + Qualifier + Closure
    entity = Symbol(id=373, symbol_class=SymbolClass.ENT)
    qualifier = Symbol(id=150, symbol_class=SymbolClass.QUAL, 
                      base=12, modifiers={"Crown"})
    closure = Symbol(id=342, symbol_class=SymbolClass.CLOSE)
    
    return Inscription(symbols=[entity, qualifier, closure])


if __name__ == "__main__":
    # Demonstrate the system
    print("=== Harappan Operational Mathematics Demo ===\n")
    
    # Create and validate inscription
    inscription = create_example_inscription()
    print(f"Inscription: {inscription}")
    print(f"Valid: {inscription.is_valid()}\n")
    
    # Process with automaton
    automaton = HarappanAutomaton()
    result = automaton.process_inscription(inscription)
    print(f"Automaton accepts: {result}")
    print(f"Final state: {automaton.state}\n")
    
    # Interpret semantically
    interpreter = SemanticInterpreter()
    state = interpreter.interpret(inscription)
    print(f"Institutional state: {state}")
