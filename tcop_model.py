"""
TCOP: Theorem of Primitive Operational Composition
Computational Model Implementation

This module implements a finite automaton with attributes representing
primitive graphic systems as described by the TCOP theorem.
"""

from typing import Set, Dict, List, Tuple, Optional, FrozenSet
from dataclasses import dataclass, field
from enum import Enum
import json


class OperatorType(Enum):
    """Types of graphical operators"""
    MODIFICATION = "modification"  # Modifies the base symbol
    ADDITION = "addition"  # Adds elements to the symbol
    POSITION = "position"  # Changes position/orientation
    DUPLICATION = "duplication"  # Duplicates elements
    ENCLOSURE = "enclosure"  # Encloses in container
    TERMINAL = "terminal"  # Marks completion/validation


@dataclass(frozen=True)
class BaseSymbol:
    """Represents a base symbol (ontological class)"""
    id: str
    name: str
    ontological_class: str
    
    def __str__(self):
        return f"{self.name} ({self.ontological_class})"


@dataclass(frozen=True)
class Operator:
    """Represents a graphical operator"""
    id: str
    name: str
    operator_type: OperatorType
    description: str
    
    def __str__(self):
        return f"{self.name} [{self.operator_type.value}]"


@dataclass(frozen=True)
class State:
    """Represents a state in the automaton (base + applied operators)"""
    base: BaseSymbol
    operators: FrozenSet[str]  # Set of operator IDs
    
    def __str__(self):
        ops = ", ".join(sorted(self.operators)) if self.operators else "none"
        return f"{self.base.name} + [{ops}]"
    
    def __hash__(self):
        return hash((self.base.id, self.operators))


@dataclass
class GraphicSystem:
    """
    Represents a primitive graphic system S = (B, O, Σ)
    Implements a finite automaton with attributes
    """
    name: str
    base_symbols: Dict[str, BaseSymbol] = field(default_factory=dict)
    operators: Dict[str, Operator] = field(default_factory=dict)
    states: Set[State] = field(default_factory=set)
    transitions: Dict[Tuple[State, str], State] = field(default_factory=dict)
    initial_states: Set[State] = field(default_factory=set)
    accepting_states: Set[State] = field(default_factory=set)
    
    # Statistical properties
    symbol_frequencies: Dict[State, int] = field(default_factory=dict)
    
    def add_base_symbol(self, symbol: BaseSymbol) -> None:
        """Add a base symbol to the system"""
        self.base_symbols[symbol.id] = symbol
        # Create initial state for this base
        initial_state = State(base=symbol, operators=frozenset())
        self.states.add(initial_state)
        self.initial_states.add(initial_state)
    
    def add_operator(self, operator: Operator) -> None:
        """Add an operator to the system"""
        self.operators[operator.id] = operator
    
    def apply_operator(self, state: State, operator_id: str) -> Optional[State]:
        """
        Apply an operator to a state, creating a new state
        Returns None if the operator cannot be applied
        """
        if operator_id not in self.operators:
            return None
        
        operator = self.operators[operator_id]
        
        # Check if operator already applied (avoid duplicates)
        if operator_id in state.operators:
            return None
        
        # Create new state with added operator
        new_operators = frozenset(state.operators | {operator_id})
        new_state = State(base=state.base, operators=new_operators)
        
        # Add to states and transitions
        self.states.add(new_state)
        self.transitions[(state, operator_id)] = new_state
        
        # Mark as accepting if it's a terminal operator
        if operator.operator_type == OperatorType.TERMINAL:
            self.accepting_states.add(new_state)
        
        return new_state
    
    def is_accepting_state(self, state: State) -> bool:
        """Check if a state is an accepting (terminal) state"""
        return state in self.accepting_states
    
    def get_state_by_composition(self, base_id: str, operator_ids: List[str]) -> Optional[State]:
        """
        Get or create a state by applying operators sequentially to a base
        This demonstrates the composition property from Hypothesis 2:
        s = o_n ∘ o_{n-1} ∘ ... ∘ o_1(b)
        """
        if base_id not in self.base_symbols:
            return None
        
        base = self.base_symbols[base_id]
        current_state = State(base=base, operators=frozenset())
        
        for op_id in operator_ids:
            next_state = self.apply_operator(current_state, op_id)
            if next_state is None:
                return None
            current_state = next_state
        
        return current_state
    
    def record_occurrence(self, state: State) -> None:
        """Record an occurrence of a state (for statistical analysis)"""
        if state not in self.symbol_frequencies:
            self.symbol_frequencies[state] = 0
        self.symbol_frequencies[state] += 1
    
    def get_state_space_size(self) -> int:
        """
        Get the size of the state space |Σ|
        Demonstrates Hypothesis 1: |B| << |Σ|
        """
        return len(self.states)
    
    def get_base_count(self) -> int:
        """Get the number of base symbols |B|"""
        return len(self.base_symbols)
    
    def verify_finiteness_hypothesis(self) -> bool:
        """
        Verify Hypothesis 1: |B| << |Σ|
        Returns True if the state space is significantly larger than base space
        """
        base_count = self.get_base_count()
        state_count = self.get_state_space_size()
        
        if base_count == 0:
            return False
        
        # Consider "much less than" as at least 3x difference
        return state_count >= 3 * base_count
    
    def verify_distribution_hypothesis(self, alpha_min: float = 0.8, 
                                      alpha_max: float = 1.2) -> Tuple[bool, float]:
        """
        Verify Hypothesis 5: Zipf-like distribution
        Returns (is_valid, estimated_alpha)
        """
        if not self.symbol_frequencies:
            return False, 0.0
        
        # Sort by frequency
        frequencies = sorted(self.symbol_frequencies.values(), reverse=True)
        
        if len(frequencies) < 3:
            return False, 0.0
        
        # Estimate alpha using first and last non-zero frequencies
        import math
        n = len(frequencies)
        f1 = frequencies[0]
        fn = frequencies[-1]
        
        if fn == 0:
            return False, 0.0
        
        # f(r) ∝ 1/r^alpha, so log(f1/fn) ≈ alpha * log(n)
        alpha = math.log(f1 / fn) / math.log(n)
        
        return alpha_min <= alpha <= alpha_max, alpha
    
    def to_dict(self) -> Dict:
        """Export system to dictionary format"""
        return {
            "name": self.name,
            "base_symbols": {
                k: {
                    "id": v.id,
                    "name": v.name,
                    "class": v.ontological_class
                }
                for k, v in self.base_symbols.items()
            },
            "operators": {
                k: {
                    "id": v.id,
                    "name": v.name,
                    "type": v.operator_type.value,
                    "description": v.description
                }
                for k, v in self.operators.items()
            },
            "state_count": len(self.states),
            "transition_count": len(self.transitions),
            "accepting_states_count": len(self.accepting_states)
        }
    
    def __str__(self):
        return (f"GraphicSystem('{self.name}': "
                f"|B|={self.get_base_count()}, "
                f"|O|={len(self.operators)}, "
                f"|Σ|={self.get_state_space_size()})")


class TCOPValidator:
    """
    Validates that a graphic system satisfies TCOP conditions
    """
    
    @staticmethod
    def validate_system(system: GraphicSystem) -> Dict[str, bool]:
        """
        Validate all TCOP conditions for a graphic system
        Returns a dictionary of condition -> satisfied (bool)
        """
        results = {}
        
        # Condition 1: Recurrence - base symbols are finite and recurrent
        results["recurrence"] = system.get_base_count() > 0
        
        # Condition 2: Systematicity - base symbols admit modifications
        results["systematicity"] = len(system.operators) > 0
        
        # Condition 3: Compositionality - modifications are finite and compositional
        results["compositionality"] = (
            len(system.operators) > 0 and 
            len(system.transitions) > 0
        )
        
        # Condition 4: Regularity - statistical regularities exist
        # (simplified check: multiple occurrences recorded)
        results["regularity"] = len(system.symbol_frequencies) > 0
        
        # Hypothesis 1: Finiteness |B| << |Σ|
        results["finiteness"] = system.verify_finiteness_hypothesis()
        
        # Hypothesis 5: Distribution follows Zipf-like pattern
        is_zipf, alpha = system.verify_distribution_hypothesis()
        results["distribution"] = is_zipf
        results["zipf_alpha"] = alpha
        
        # Overall satisfaction
        results["tcop_satisfied"] = all([
            results["recurrence"],
            results["systematicity"],
            results["compositionality"],
            results["regularity"],
            results["finiteness"]
        ])
        
        return results


def create_harappan_example() -> GraphicSystem:
    """
    Create a simplified example of Harappan script as a TCOP system
    """
    system = GraphicSystem(name="Harappan Script (Simplified)")
    
    # Add base symbols (ontological classes)
    base_symbols = [
        BaseSymbol("fish", "Fish", "animal"),
        BaseSymbol("jar", "Jar", "container"),
        BaseSymbol("person", "Person", "human"),
        BaseSymbol("plant", "Plant", "botanical"),
    ]
    
    for symbol in base_symbols:
        system.add_base_symbol(symbol)
    
    # Add operators
    operators = [
        Operator("stroke1", "Single Stroke", OperatorType.MODIFICATION, 
                "Adds single stroke modifier"),
        Operator("stroke2", "Double Stroke", OperatorType.MODIFICATION,
                "Adds double stroke modifier"),
        Operator("encircle", "Encircle", OperatorType.ENCLOSURE,
                "Encloses symbol in circle"),
        Operator("duplicate", "Duplicate", OperatorType.DUPLICATION,
                "Duplicates the symbol"),
        Operator("terminal", "Terminal Mark", OperatorType.TERMINAL,
                "Marks completion/validation"),
    ]
    
    for operator in operators:
        system.add_operator(operator)
    
    # Generate some example states and record frequencies
    # Simulate corpus statistics
    examples = [
        ("fish", ["stroke1", "terminal"], 15),
        ("fish", ["stroke2", "terminal"], 8),
        ("jar", ["encircle", "terminal"], 12),
        ("jar", ["terminal"], 20),
        ("person", ["duplicate", "terminal"], 6),
        ("person", ["stroke1", "terminal"], 10),
        ("plant", ["terminal"], 5),
    ]
    
    for base_id, ops, freq in examples:
        state = system.get_state_by_composition(base_id, ops)
        if state:
            for _ in range(freq):
                system.record_occurrence(state)
    
    return system


def create_ancient_chinese_example() -> GraphicSystem:
    """
    Create a simplified example of Ancient Chinese radicals as a TCOP system
    """
    system = GraphicSystem(name="Ancient Chinese Radicals (Simplified)")
    
    # Add base symbols (radicals as ontological classes)
    base_symbols = [
        BaseSymbol("person", "人 (rén)", "agent"),
        BaseSymbol("water", "水 (shuǐ)", "element"),
        BaseSymbol("mouth", "口 (kǒu)", "opening"),
        BaseSymbol("tree", "木 (mù)", "plant"),
    ]
    
    for symbol in base_symbols:
        system.add_base_symbol(symbol)
    
    # Add operators representing modifications to radicals
    operators = [
        Operator("double", "Duplication", OperatorType.DUPLICATION,
                "Doubles the radical (e.g., 从 = 人+人)"),
        Operator("force", "Force Radical", OperatorType.ADDITION,
                "Adds force/power component"),
        Operator("enclose", "Enclosure", OperatorType.ENCLOSURE,
                "Encloses in a container radical"),
        Operator("inside", "Inside Position", OperatorType.POSITION,
                "Places inside another component"),
        Operator("terminal", "Character Complete", OperatorType.TERMINAL,
                "Marks complete character"),
    ]
    
    for operator in operators:
        system.add_operator(operator)
    
    # Generate example states with frequencies
    examples = [
        ("person", ["double", "terminal"], 18),  # 从 (follow)
        ("person", ["force", "terminal"], 14),
        ("water", ["double", "terminal"], 10),
        ("mouth", ["enclose", "terminal"], 16),
        ("tree", ["double", "terminal"], 12),  # 林 (forest)
    ]
    
    for base_id, ops, freq in examples:
        state = system.get_state_by_composition(base_id, ops)
        if state:
            for _ in range(freq):
                system.record_occurrence(state)
    
    return system


def main():
    """Demonstrate the TCOP computational model"""
    print("=" * 70)
    print("TCOP: Theorem of Primitive Operational Composition")
    print("Computational Model Demonstration")
    print("=" * 70)
    print()
    
    # Create Harappan example
    print("1. HARAPPAN SCRIPT EXAMPLE")
    print("-" * 70)
    harappan = create_harappan_example()
    print(harappan)
    print()
    
    # Validate TCOP conditions
    print("TCOP Validation:")
    results = TCOPValidator.validate_system(harappan)
    for condition, satisfied in results.items():
        if isinstance(satisfied, bool):
            status = "✓" if satisfied else "✗"
            print(f"  {status} {condition}: {satisfied}")
        else:
            print(f"    {condition}: {satisfied:.3f}")
    print()
    
    # Show example states
    print("Example States (first 5):")
    for i, state in enumerate(list(harappan.states)[:5], 1):
        freq = harappan.symbol_frequencies.get(state, 0)
        accepting = "✓" if harappan.is_accepting_state(state) else " "
        print(f"  {i}. [{accepting}] {state} (freq: {freq})")
    print()
    
    # Create Ancient Chinese example
    print("2. ANCIENT CHINESE EXAMPLE")
    print("-" * 70)
    chinese = create_ancient_chinese_example()
    print(chinese)
    print()
    
    # Validate TCOP conditions
    print("TCOP Validation:")
    results = TCOPValidator.validate_system(chinese)
    for condition, satisfied in results.items():
        if isinstance(satisfied, bool):
            status = "✓" if satisfied else "✗"
            print(f"  {status} {condition}: {satisfied}")
        else:
            print(f"    {condition}: {satisfied:.3f}")
    print()
    
    # Show example states
    print("Example States (first 5):")
    for i, state in enumerate(list(chinese.states)[:5], 1):
        freq = chinese.symbol_frequencies.get(state, 0)
        accepting = "✓" if chinese.is_accepting_state(state) else " "
        print(f"  {i}. [{accepting}] {state} (freq: {freq})")
    print()
    
    # Export to JSON
    print("3. SYSTEM EXPORT")
    print("-" * 70)
    harappan_dict = harappan.to_dict()
    print("Harappan system exported to dictionary:")
    print(json.dumps(harappan_dict, indent=2))
    print()
    
    print("=" * 70)
    print("Demonstration complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
