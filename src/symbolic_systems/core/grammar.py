"""
Universal grammar and symbolic system base classes.

This module implements the core theory of a universal deep grammar
underlying all human symbolic systems.
"""

from typing import List, Set, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from .operators import CognitiveAxis, UniversalOperator


@dataclass
class Symbol:
    """
    Represents a symbol in a symbolic system.
    
    A symbol can be a base form or a composite of base + modifiers.
    """
    
    base_id: str
    name: str
    form: str
    modifiers: List[str] = field(default_factory=list)
    cognitive_axes: List[CognitiveAxis] = field(default_factory=list)
    description: str = ""
    
    def __repr__(self):
        mod_str = f"+{'+'.join(self.modifiers)}" if self.modifiers else ""
        return f"Symbol({self.name}{mod_str})"
    
    def compose_with(self, modifier: str) -> 'Symbol':
        """Create a new symbol by composing with a modifier."""
        return Symbol(
            base_id=self.base_id,
            name=self.name,
            form=self.form,
            modifiers=self.modifiers + [modifier],
            cognitive_axes=self.cognitive_axes,
            description=f"{self.description} + {modifier}"
        )


@dataclass
class SymbolState:
    """
    Represents a state in the automaton model of a symbolic system.
    
    Each inscription or text is modeled as a sequence of states,
    where each state represents a symbol and its relationships.
    """
    
    symbol: Symbol
    position: int
    context: Dict[str, any] = field(default_factory=dict)
    
    def __repr__(self):
        return f"SymbolState({self.symbol}, pos={self.position})"


class RealityLevel(Enum):
    """The 3 levels of reality in symbolic representation."""
    
    MICRO = "individual_object"     # Individual/object level
    MESO = "institution_transaction"  # Institution/transaction level
    MACRO = "cosmos_cycle"          # Cosmos/cycle level


class SymbolicSystem:
    """
    Base class for all symbolic systems.
    
    Each system (Harappan, Mayan, Aztec, etc.) is a realization of
    the universal deep grammar.
    """
    
    def __init__(self, name: str, primary_level: RealityLevel):
        self.name = name
        self.primary_level = primary_level
        self.symbols: Dict[str, Symbol] = {}
        self.transformation_rules: Dict[str, List[Tuple[str, str]]] = {}
        
    def add_symbol(self, symbol: Symbol):
        """Add a symbol to the system."""
        self.symbols[symbol.base_id] = symbol
        
    def get_symbol(self, symbol_id: str) -> Optional[Symbol]:
        """Retrieve a symbol by ID."""
        return self.symbols.get(symbol_id)
    
    def add_transformation_rule(self, base: str, modifier: str, result: str):
        """
        Add a transformation rule: base + modifier -> result
        
        Example: "man" + "crown" -> "lord"
        """
        if base not in self.transformation_rules:
            self.transformation_rules[base] = []
        self.transformation_rules[base].append((modifier, result))
    
    def transform(self, base_id: str, modifier: str) -> Optional[str]:
        """Apply a transformation rule."""
        if base_id in self.transformation_rules:
            for mod, result in self.transformation_rules[base_id]:
                if mod == modifier:
                    return result
        return None
    
    def parse_sequence(self, sequence: List[str]) -> List[SymbolState]:
        """
        Parse a sequence of symbol IDs into states.
        
        This is the automaton interpretation of an inscription.
        """
        states = []
        for i, symbol_id in enumerate(sequence):
            symbol = self.get_symbol(symbol_id)
            if symbol:
                states.append(SymbolState(symbol=symbol, position=i))
        return states
    
    def __repr__(self):
        return f"SymbolicSystem({self.name}, symbols={len(self.symbols)})"


class UniversalGrammar:
    """
    The universal deep grammar underlying all symbolic systems.
    
    This implements the theory that all human symbolic systems share
    a common cognitive structure with:
    - 45 basic operators (graphical forms)
    - 7 semantic dimensions (cognitive axes)
    - 3 levels of application (micro, meso, macro)
    - Systematic transformation rules
    """
    
    def __init__(self):
        self.systems: Dict[str, SymbolicSystem] = {}
        self.cognitive_axes = list(CognitiveAxis)
        self.reality_levels = list(RealityLevel)
        
    def register_system(self, system: SymbolicSystem):
        """Register a symbolic system with the universal grammar."""
        self.systems[system.name] = system
        
    def get_system(self, name: str) -> Optional[SymbolicSystem]:
        """Retrieve a registered system."""
        return self.systems.get(name)
    
    def compare_systems(self, system1_name: str, system2_name: str) -> Dict[str, any]:
        """
        Compare two symbolic systems to find correspondences.
        
        Returns a dictionary with similarity metrics and mappings.
        """
        sys1 = self.get_system(system1_name)
        sys2 = self.get_system(system2_name)
        
        if not sys1 or not sys2:
            return {}
        
        # Find symbols with overlapping cognitive axes
        correspondences = []
        for s1_id, s1 in sys1.symbols.items():
            for s2_id, s2 in sys2.symbols.items():
                overlap = set(s1.cognitive_axes) & set(s2.cognitive_axes)
                if overlap:
                    correspondences.append({
                        'system1_symbol': s1,
                        'system2_symbol': s2,
                        'shared_axes': list(overlap),
                        'similarity': len(overlap) / max(len(s1.cognitive_axes), len(s2.cognitive_axes))
                    })
        
        return {
            'system1': system1_name,
            'system2': system2_name,
            'correspondences': correspondences,
            'total_matches': len(correspondences)
        }
    
    def find_universal_pattern(self, pattern_type: str) -> List[Dict[str, any]]:
        """
        Find instances of a universal pattern across all registered systems.
        
        Examples: "man_to_lord", "house_to_temple", "numeric_progression"
        """
        patterns = []
        
        if pattern_type == "man_to_lord":
            # Find the "man + crown -> lord" transformation in all systems
            for system_name, system in self.systems.items():
                for base_id, rules in system.transformation_rules.items():
                    for modifier, result in rules:
                        if "crown" in modifier.lower() or "power" in modifier.lower():
                            patterns.append({
                                'system': system_name,
                                'base': base_id,
                                'modifier': modifier,
                                'result': result,
                                'type': 'authority_transformation'
                            })
        
        return patterns
    
    def __repr__(self):
        return f"UniversalGrammar(systems={len(self.systems)})"
