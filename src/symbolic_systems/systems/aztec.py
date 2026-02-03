"""
Aztec symbolic system implementation.

The Aztec pictographic system integrates all three reality levels
(micro, meso, macro) in complex codices.
"""

from ..core.grammar import SymbolicSystem, Symbol, RealityLevel
from ..core.operators import CognitiveAxis
from typing import List, Dict


class AztecSystem(SymbolicSystem):
    """
    Implementation of the Aztec (Nahuatl pictographic) symbolic system.
    
    The Aztec system is characterized by:
    - Three-dimensional structure: Territories + Tributes + History
    - Tonalpohualli calendar (260 days)
    - Circular automaton (Stone of the Sun)
    - Integration of all reality levels
    
    Structure: Σ (Territory_i ⊕ Tribute_ij ⊕ Event_ik)
    """
    
    def __init__(self):
        super().__init__(name="Aztec", primary_level=RealityLevel.MESO)
        self._initialize_symbols()
        self._initialize_transformations()
        self._initialize_calendar()
    
    def _initialize_symbols(self):
        """Initialize core Aztec symbols."""
        
        # Point (numerical)
        self.add_symbol(Symbol(
            base_id="A_DOT",
            name="Point",
            form="•",
            cognitive_axes=[CognitiveAxis.QUANTITY, CognitiveAxis.PRESENCE],
            description="Unit, one, numerical marker"
        ))
        
        # Cross (directional)
        self.add_symbol(Symbol(
            base_id="A_CROSS",
            name="Directional Cross",
            form="✚",
            cognitive_axes=[CognitiveAxis.RELATION, CognitiveAxis.SPACE],
            description="Four directions, cosmic order"
        ))
        
        # Tonatiuh (Sun)
        self.add_symbol(Symbol(
            base_id="A_TONATIUH",
            name="Tonatiuh",
            form="☀",
            cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.QUALITY],
            description="Sun, current era, cosmic center"
        ))
        
        # Calli (House)
        self.add_symbol(Symbol(
            base_id="A_CALLI",
            name="Calli",
            form="□",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION],
            description="House, building, domain"
        ))
        
        # Teocalli (Temple)
        self.add_symbol(Symbol(
            base_id="A_TEOCALLI",
            name="Teocalli",
            form="⛩",
            modifiers=["divine_glyph"],
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION, CognitiveAxis.QUALITY],
            description="Temple, sacred house, divine building"
        ))
        
        # Tlatoani (Speaker/Ruler)
        self.add_symbol(Symbol(
            base_id="A_TLATOANI",
            name="Tlatoani",
            form="👤",
            modifiers=["crown"],
            cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.VALIDATION],
            description="Ruler, speaker, authority"
        ))
        
        # Footprints (movement/conquest)
        self.add_symbol(Symbol(
            base_id="A_FOOTPRINTS",
            name="Footprints",
            form="👣",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.TIME],
            description="Movement, journey, conquest"
        ))
        
        # Heart (sacrificed)
        self.add_symbol(Symbol(
            base_id="A_HEART",
            name="Heart",
            form="💓",
            cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUALITY],
            description="Heart, life force, sacrifice"
        ))
        
        # Mountain (territory marker)
        self.add_symbol(Symbol(
            base_id="A_MOUNTAIN",
            name="Mountain",
            form="⛰",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.PRESENCE],
            description="Mountain, territory, altepetl"
        ))
    
    def _initialize_transformations(self):
        """Initialize Aztec transformation rules."""
        
        # Man + Crown -> Tlatoani
        self.add_transformation_rule("A_MAN", "crown", "A_TLATOANI")
        
        # Calli + Divine -> Teocalli
        self.add_transformation_rule("A_CALLI", "divine_glyph", "A_TEOCALLI")
        
        # Mountain + Conquered Head -> Territory conquest
        self.add_transformation_rule("A_MOUNTAIN", "conquered_head", "A_CONQUERED_TERRITORY")
    
    def _initialize_calendar(self):
        """Initialize Aztec calendar system."""
        self.calendar = {
            'tonalpohualli_days': 260,  # Sacred calendar
            'day_signs': 20,             # Day signs
            'day_numbers': 13,           # Day numbers
            'solar_year': 365,           # Solar year
        }
        
        # 20 day signs
        self.day_signs = [
            "Cipactli", "Ehecatl", "Calli", "Cuetzpalin", "Coatl",
            "Miquiztli", "Mazatl", "Tochtli", "Atl", "Itzcuintli",
            "Ozomatli", "Malinalli", "Acatl", "Ocelotl", "Cuauhtli",
            "Cozcacuauhtli", "Ollin", "Tecpatl", "Quiahuitl", "Xochitl"
        ]
    
    def calculate_tonalpohualli(self, day_number: int, day_sign_index: int) -> Dict[str, any]:
        """
        Calculate a position in the Tonalpohualli calendar.
        
        System: 20 day signs × 13 numbers = 260 unique combinations
        Equivalent to Harappan: 20 base symbols × 13 numeric modifiers
        """
        if not (1 <= day_number <= 13):
            raise ValueError("Day number must be between 1 and 13")
        if not (0 <= day_sign_index < 20):
            raise ValueError("Day sign index must be between 0 and 19")
        
        day_sign = self.day_signs[day_sign_index]
        position = ((day_number - 1) * 20 + day_sign_index) % 260
        
        return {
            'day_number': day_number,
            'day_sign': day_sign,
            'day_sign_index': day_sign_index,
            'calendar_position': position,
            'representation': f"{day_number} {day_sign}"
        }
    
    def parse_codex_entry(self, territories: List[str], tributes: List[Dict],
                          events: List[Dict]) -> Dict[str, any]:
        """
        Parse a Codex Mendoza-style entry.
        
        Structure: Territory glyphs + Tribute lists + Historical timeline
        Isomorphic to: Σ (Territory_i ⊕ Tribute_ij ⊕ Event_ik)
        """
        return {
            'type': 'codex_entry',
            'territories': territories,
            'tributes': tributes,
            'events': events,
            'complexity': len(territories) + len(tributes) + len(events)
        }
    
    def get_statistics(self) -> Dict[str, any]:
        """Get statistics about the Aztec system."""
        return {
            'name': self.name,
            'total_symbols': len(self.symbols),
            'transformation_rules': len(self.transformation_rules),
            'primary_level': self.primary_level.value,
            'calendar_system': self.calendar,
            'day_signs': len(self.day_signs),
            'cognitive_axes_used': list(set(
                axis for symbol in self.symbols.values()
                for axis in symbol.cognitive_axes
            ))
        }


# Create a default instance
aztec_system = AztecSystem()
