"""
Mayan symbolic system implementation.

The Mayan system emphasizes cosmic cycles and temporal computations,
operating primarily at the MACRO (cosmos) and MESO (institution) levels.
"""

from ..core.grammar import SymbolicSystem, Symbol, RealityLevel
from ..core.operators import CognitiveAxis
from typing import List, Dict


class MayanSystem(SymbolicSystem):
    """
    Implementation of the Mayan symbolic system.
    
    The Mayan system is characterized by:
    - Complex calendar systems (Tzolk'in, Haab')
    - Logo-syllabic writing with affixes
    - State automaton structure: [Upper Affix] → [Prefixes] → [Central Logogram] → [Suffixes] → [Lower Affix]
    - Strong focus on temporal and cosmic cycles
    
    Isomorphism with Harappan:
    Base_State → Modifiers → Relators → Closure
    """
    
    def __init__(self):
        super().__init__(name="Mayan", primary_level=RealityLevel.MACRO)
        self._initialize_symbols()
        self._initialize_transformations()
        self._initialize_calendar()
    
    def _initialize_symbols(self):
        """Initialize core Mayan symbols."""
        
        # K'in - Day
        self.add_symbol(Symbol(
            base_id="M_KIN",
            name="K'in",
            form="☀",
            cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.PRESENCE],
            description="Day, sun, basic time unit"
        ))
        
        # Ajaw - Lord
        self.add_symbol(Symbol(
            base_id="M_AJAW",
            name="Ajaw",
            form="👤",
            modifiers=["divine_adornments"],
            cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.VALIDATION],
            description="Lord, ruler, divine authority"
        ))
        
        # K'uhul Ajaw - Divine Lord
        self.add_symbol(Symbol(
            base_id="M_KUHUL_AJAW",
            name="K'uhul Ajaw",
            form="👤",
            modifiers=["divine", "power_elements"],
            cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.VALIDATION, CognitiveAxis.SPACE],
            description="Divine Lord, supreme authority"
        ))
        
        # Na - House
        self.add_symbol(Symbol(
            base_id="M_NA",
            name="Na",
            form="□",
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION],
            description="House, building, domain"
        ))
        
        # Temple (Na + divine)
        self.add_symbol(Symbol(
            base_id="M_TEMPLE",
            name="Temple",
            form="⛩",
            modifiers=["divine_glyphs"],
            cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION, CognitiveAxis.QUALITY],
            description="Temple, sacred building"
        ))
        
        # Numerical dot
        self.add_symbol(Symbol(
            base_id="M_DOT",
            name="Dot",
            form="•",
            cognitive_axes=[CognitiveAxis.QUANTITY, CognitiveAxis.PRESENCE],
            description="Unit, one, numerical marker"
        ))
        
        # Numerical bar
        self.add_symbol(Symbol(
            base_id="M_BAR",
            name="Bar",
            form="—",
            cognitive_axes=[CognitiveAxis.QUANTITY],
            description="Five, group, numerical marker"
        ))
        
        # Maize/Corn
        self.add_symbol(Symbol(
            base_id="M_MAIZE",
            name="Maize",
            form="🌽",
            cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.PRESENCE],
            description="Maize, corn, sacred food"
        ))
    
    def _initialize_transformations(self):
        """Initialize Mayan transformation rules."""
        
        # Man -> +Adornments -> Ajaw
        self.add_transformation_rule("M_PERSON", "divine_adornments", "M_AJAW")
        
        # Ajaw -> Young/Old, Warrior/Priest transformations
        self.add_transformation_rule("M_AJAW", "age_young", "M_AJAW_YOUNG")
        self.add_transformation_rule("M_AJAW", "age_old", "M_AJAW_OLD")
        self.add_transformation_rule("M_AJAW", "warrior", "M_AJAW_WARRIOR")
        self.add_transformation_rule("M_AJAW", "priest", "M_AJAW_PRIEST")
        
        # House -> Temple
        self.add_transformation_rule("M_NA", "divine_glyphs", "M_TEMPLE")
    
    def _initialize_calendar(self):
        """Initialize Mayan calendar system data."""
        self.calendar = {
            'tzolkin_days': 260,  # Sacred calendar
            'haab_days': 365,     # Solar calendar
            'day_signs': 20,      # Day name signs
            'day_numbers': 13,    # Day numbers in Tzolk'in
        }
    
    def calculate_calendar_date(self, kin: int, uinal: int = 0, tun: int = 0) -> Dict[str, int]:
        """
        Calculate a Mayan calendar date.
        
        Date = Kin (day) + Uinal (20 days) + Tun (360 days)
        
        Equivalent to Harappan: Temporal_Entity ⊕ Quantifier ⊕ Cycle ⊕ Closure
        """
        total_days = kin + (uinal * 20) + (tun * 360)
        
        # Calculate position in calendars
        tzolkin_position = total_days % self.calendar['tzolkin_days']
        haab_position = total_days % self.calendar['haab_days']
        
        return {
            'total_days': total_days,
            'tzolkin_day': tzolkin_position,
            'haab_day': haab_position,
            'kin': kin,
            'uinal': uinal,
            'tun': tun,
            'calendar_round_position': (tzolkin_position, haab_position)
        }
    
    def get_statistics(self) -> Dict[str, any]:
        """Get statistics about the Mayan system."""
        return {
            'name': self.name,
            'total_symbols': len(self.symbols),
            'transformation_rules': len(self.transformation_rules),
            'primary_level': self.primary_level.value,
            'calendar_system': self.calendar,
            'cognitive_axes_used': list(set(
                axis for symbol in self.symbols.values()
                for axis in symbol.cognitive_axes
            ))
        }


# Create a default instance
mayan_system = MayanSystem()
