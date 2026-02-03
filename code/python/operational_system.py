"""
Indus Operational Mathematics - Python Implementation
Core operational system for symbol analysis
"""

from enum import Enum, auto
from typing import List, Optional, Set, Tuple, Dict
from dataclasses import dataclass


class SymbolClass(Enum):
    """Semantic classes for symbols (Axiom A1)"""
    QUANTIFIER = auto()
    ENTITY = auto()
    MODIFIER = auto()
    OPERATOR = auto()
    TERMINAL = auto()


@dataclass(frozen=True)
class Symbol:
    """Immutable symbol representation"""
    id: int
    name: str = ""
    
    def __hash__(self):
        return hash(self.id)


@dataclass
class State:
    """State in the operational system"""
    value: str
    is_final: bool = False
    properties: Dict[str, any] = None
    
    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


class OperationalSystem:
    """
    Operational symbol system implementing axioms A1-A5
    """
    
    def __init__(self):
        self.symbols: Set[Symbol] = set()
        self.class_assignment: Dict[Symbol, SymbolClass] = {}
        self.composition_rules: Dict[Tuple[Symbol, Symbol], Symbol] = {}
        self.init_state: State = State("initial", False)
        self.accept_states: Set[State] = set()
        
    def add_symbol(self, symbol: Symbol, symbol_class: SymbolClass) -> None:
        """
        Add a symbol to the system with its semantic class (A1)
        """
        self.symbols.add(symbol)
        self.class_assignment[symbol] = symbol_class
        
    def get_class(self, symbol: Symbol) -> SymbolClass:
        """
        Get the semantic class of a symbol (A1)
        """
        if symbol not in self.class_assignment:
            raise ValueError(f"Symbol {symbol} not in system")
        return self.class_assignment[symbol]
        
    @staticmethod
    def compatible(c1: SymbolClass, c2: SymbolClass) -> bool:
        """
        Check if two classes can compose (A3)
        """
        compatibility_matrix = {
            (SymbolClass.QUANTIFIER, SymbolClass.ENTITY): True,
            (SymbolClass.ENTITY, SymbolClass.MODIFIER): True,
            (SymbolClass.ENTITY, SymbolClass.OPERATOR): True,
            (SymbolClass.ENTITY, SymbolClass.TERMINAL): True,
        }
        return compatibility_matrix.get((c1, c2), False)
        
    def add_composition_rule(self, s1: Symbol, s2: Symbol, result: Symbol) -> None:
        """
        Add a composition rule (A2, A3)
        
        Validates:
        - Both symbols are in system
        - Classes are compatible (A3)
        - Result is in system (A2)
        - Result class is preserved (A2)
        """
        if s1 not in self.symbols or s2 not in self.symbols:
            raise ValueError("Symbols must be in system")
            
        c1 = self.get_class(s1)
        c2 = self.get_class(s2)
        
        if not self.compatible(c1, c2):
            raise ValueError(f"Incompatible classes: {c1} and {c2}")
            
        if result not in self.symbols:
            raise ValueError("Result symbol must be in system (A2)")
            
        result_class = self.get_class(result)
        if result_class not in {c1, c2}:
            raise ValueError(f"Result class {result_class} not in operand classes (A2)")
            
        self.composition_rules[(s1, s2)] = result
        
    def compose(self, s1: Symbol, s2: Symbol) -> Optional[Symbol]:
        """
        Compose two symbols if compatible
        """
        # A4: Terminal symbols accept no composition
        if self.get_class(s1) == SymbolClass.TERMINAL:
            return None
            
        return self.composition_rules.get((s1, s2))
        
    @staticmethod
    def modifier_layer(symbol_class: SymbolClass) -> int:
        """
        Get the hierarchical layer of a symbol class (A5)
        """
        layers = {
            SymbolClass.QUANTIFIER: 0,
            SymbolClass.ENTITY: 0,
            SymbolClass.MODIFIER: 1,
            SymbolClass.OPERATOR: 2,
            SymbolClass.TERMINAL: 3,
        }
        return layers[symbol_class]
        
    def validate_sequence(self, sequence: List[Symbol]) -> Tuple[bool, str]:
        """
        Validate a symbol sequence according to axioms A1-A5
        
        Returns:
            (is_valid, error_message)
        """
        if not sequence:
            return False, "Empty sequence"
            
        # Check all symbols are in system (A1)
        for symbol in sequence:
            if symbol not in self.symbols:
                return False, f"Symbol {symbol} not in system"
                
        # Check pairwise compatibility (A3)
        for i in range(len(sequence) - 1):
            s1, s2 = sequence[i], sequence[i + 1]
            c1, c2 = self.get_class(s1), self.get_class(s2)
            
            if not self.compatible(c1, c2):
                return False, f"Incompatible symbols at position {i}: {c1} and {c2}"
                
        # Check hierarchical layering (A5)
        prev_layer = 0
        for i, symbol in enumerate(sequence):
            current_layer = self.modifier_layer(self.get_class(symbol))
            if current_layer < prev_layer:
                return False, f"Layer violation at position {i}: {current_layer} < {prev_layer}"
            prev_layer = current_layer
            
        # Check terminal placement (A4)
        for i, symbol in enumerate(sequence[:-1]):  # All but last
            if self.get_class(symbol) == SymbolClass.TERMINAL:
                return False, f"Terminal symbol at non-final position {i}"
                
        # Valid sequence should end with terminal
        if sequence and self.get_class(sequence[-1]) != SymbolClass.TERMINAL:
            return False, "Sequence does not end with terminal symbol"
            
        return True, "Valid sequence"
        
    def eval(self, sequence: List[Symbol]) -> Optional[State]:
        """
        Evaluate a sequence to produce a state (TCOP Part 1)
        """
        is_valid, error_msg = self.validate_sequence(sequence)
        if not is_valid:
            return None
            
        # Build state by composing symbols
        current_value = "init"
        properties = {}
        
        for symbol in sequence:
            symbol_class = self.get_class(symbol)
            current_value += f"_{symbol.name or symbol.id}"
            properties[f"step_{symbol.id}"] = symbol_class.name
            
        # Check if final state
        is_final = (sequence and 
                   self.get_class(sequence[-1]) == SymbolClass.TERMINAL)
        
        return State(current_value, is_final, properties)


def demonstrate_chinese_parallel():
    """
    Demonstrate operational semantics using ancient Chinese examples
    """
    sys = OperationalSystem()
    
    # Create symbols (mimicking Chinese transformations)
    ren = Symbol(1, "人")  # person base
    yi = Symbol(2, "一")   # one (horizontal stroke)
    da = Symbol(3, "大")   # big (composed)
    terminal = Symbol(999, "terminal")
    
    # Add to system
    sys.add_symbol(ren, SymbolClass.ENTITY)
    sys.add_symbol(yi, SymbolClass.MODIFIER)
    sys.add_symbol(da, SymbolClass.ENTITY)
    sys.add_symbol(terminal, SymbolClass.TERMINAL)
    
    # Add composition rule: 人 + 一 → 大
    sys.add_composition_rule(ren, yi, da)
    
    # Validate sequences
    valid_seq = [ren, yi, terminal]
    print(f"Sequence {[s.name for s in valid_seq]}:")
    is_valid, msg = sys.validate_sequence(valid_seq)
    print(f"  Valid: {is_valid}, Message: {msg}")
    
    if is_valid:
        state = sys.eval(valid_seq)
        print(f"  Final state: {state}")
        
    # Try invalid sequence (terminal in middle)
    invalid_seq = [ren, terminal, yi]
    print(f"\nSequence {[s.name for s in invalid_seq]}:")
    is_valid, msg = sys.validate_sequence(invalid_seq)
    print(f"  Valid: {is_valid}, Message: {msg}")


if __name__ == "__main__":
    demonstrate_chinese_parallel()
