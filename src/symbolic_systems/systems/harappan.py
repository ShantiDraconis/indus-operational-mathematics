"""
Harappan (Indus Valley) symbolic system implementation.

The Harappan system is considered the purest form of the universal grammar,
focused on institutional validation and transactions.
"""

from typing import List, Dict
from ..core.grammar import SymbolicSystem, Symbol, RealityLevel
from ..core.operators import CognitiveAxis


class HarappanSystem(SymbolicSystem):
    """
    Implementation of the Harappan/Indus Valley symbolic system.
    
    The Harappan system is characterized by:
    - Focus on institutional transactions (MESO level)
    - Short inscriptions (average 5 symbols)
    - Clear compositional structure
    - State-based operational logic
    
    Structure: Origin ⊕ Destination ⊕ Commodity ⊕ Quantity ⊕ Date? ⊕ Validation
    """
    
    def __init__(self):
        super().__init__(name="Harappan", primary_level=RealityLevel.MESO)
        self._initialize_symbols()
        self._initialize_transformations()
    
    def _initialize_symbols(self):
        """Initialize known Harappan symbols."""
        
        # Symbol 1: Line/Individual
        self.add_symbol(Symbol(
            base_id="H1",
            name="Line",
            form="|",
            cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.SPACE],
            description="Individual, axis, direction"
        ))
        
        # Symbol 4: Cross
        self.add_symbol(Symbol(
            base_id="H4",
            name="Cross",
            form="X",
            cognitive_axes=[CognitiveAxis.RELATION, CognitiveAxis.SPACE],
            description="Relation, exchange, connection"
        ))
        
        # Symbol 26: Man/Person
        self.add_symbol(Symbol(
            base_id="H26",
            name="Man",
            form="👤",
            cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUALITY],
            description="Person, individual, human figure"
        ))
        
        # Symbol 27: Point/Unit
        self.add_symbol(Symbol(
            base_id="H27",
            name="Point",
            form="•",
            cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUANTITY],
            description="Unit, instance, singular"
        ))
        
        # Symbol 30: Lord/Authority (Man + Crown)
        self.add_symbol(Symbol(
            base_id="H30",
            name="Lord",
            form="👑",
            modifiers=["crown"],
            cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.VALIDATION],
            description="Authority figure, lord, institutional power"
        ))
        
        # House symbol
        self.add_symbol(Symbol(
            base_id="H_HOUSE",
            name="House",
            form="□",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION],
            description="House, domain, institution"
        ))
        
        # Plant symbol
        self.add_symbol(Symbol(
            base_id="H_PLANT",
            name="Plant",
            form="🌱",
            cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.PRESENCE],
            description="Plant, growth, agricultural product"
        ))
        
        # Jar/Container
        self.add_symbol(Symbol(
            base_id="H_JAR",
            name="Jar",
            form="⚱",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.QUANTITY],
            description="Container, storage, commodity"
        ))
        
        # Fish
        self.add_symbol(Symbol(
            base_id="H_FISH",
            name="Fish",
            form="🐟",
            cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUANTITY],
            description="Fish, aquatic resource"
        ))
    
    def _initialize_transformations(self):
        """Initialize transformation rules for Harappan symbols."""
        
        # Man + Crown -> Lord (authority transformation)
        self.add_transformation_rule("H26", "crown", "H30")
        
        # House + Divine elements -> Temple (institutional elevation)
        self.add_transformation_rule("H_HOUSE", "divine", "H_TEMPLE")
    
    def parse_inscription(self, symbol_ids: List[str]) -> Dict[str, any]:
        """
        Parse a Harappan inscription as a transaction record.
        
        Returns a structured interpretation of the inscription.
        """
        states = self.parse_sequence(symbol_ids)
        
        # Attempt to interpret as transaction
        interpretation = {
            'length': len(states),
            'states': states,
            'type': 'unknown'
        }
        
        # Simple heuristic: look for person + commodity + quantity pattern
        has_person = any(s.symbol.base_id in ["H26", "H30"] for s in states)
        has_commodity = any(s.symbol.base_id in ["H_JAR", "H_FISH", "H_PLANT"] for s in states)
        has_quantity = any(s.symbol.base_id == "H27" for s in states)
        
        if has_person and has_commodity:
            interpretation['type'] = 'transaction'
            interpretation['has_quantity'] = has_quantity
        elif has_person:
            interpretation['type'] = 'person_reference'
        
        return interpretation
    
    def get_statistics(self) -> Dict[str, any]:
        """Get statistics about the Harappan system."""
        return {
            'name': self.name,
            'total_symbols': len(self.symbols),
            'transformation_rules': len(self.transformation_rules),
            'primary_level': self.primary_level.value,
            'cognitive_axes_used': list(set(
                axis for symbol in self.symbols.values()
                for axis in symbol.cognitive_axes
            ))
        }


# Create a default instance
harappan_system = HarappanSystem()
