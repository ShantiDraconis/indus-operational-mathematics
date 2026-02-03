"""
Harappan Operational Mathematics System
Block 373-417: Symbol Families and Operators

This module implements the symbolic system for Harappan writing as described
in the operational mathematics framework.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple


class SymbolFamily(Enum):
    """Three functional families of Harappan symbols (373-417)"""
    OMEGA = "Ω"  # Tokens/Entities (373-399)
    DELTA = "Δ"  # Relations/Bonds (400-409)
    SIGMA = "Σ"  # Counts/Stacks (410-417)


class GraphicOperator(Enum):
    """Universal graphic operators (runes) that modify base forms"""
    DOT = "•"           # Internal dot - marks instance/activation
    STROKE = "│"        # Internal stroke - partition/qualification
    FILL = "█"          # Internal fill/hatch - consummated/executed state
    BRACKET = "⟦⟧"      # Side brackets - delimits scope/jurisdiction
    SIDEBARS = "║"      # Side bars - defines level/degree/authority
    CROWN = "⸙"         # Crown/prongs - multiplexing/multiple channels
    DUP = "⊕"           # Duplication - creates pair/binary relation
    KNOT = "⚭"          # Interlacing - establishes strong bond/lock
    STEM = "⊥"          # Lower/upper stem - anchor/external indexing
    STACK = "≡"         # Vertical stacking - count/aggregation


@dataclass
class Symbol:
    """
    Represents a Harappan symbol with its properties
    """
    id: int  # Symbol number (373-417)
    family: SymbolFamily
    base_form: str  # Description of base shape
    operators: List[GraphicOperator] = field(default_factory=list)
    description: str = ""
    
    def __post_init__(self):
        """Validate symbol ID is in correct range"""
        if not (373 <= self.id <= 417):
            raise ValueError(f"Symbol ID {self.id} outside valid range (373-417)")
    
    def has_operator(self, operator: GraphicOperator) -> bool:
        """Check if symbol has a specific operator applied"""
        return operator in self.operators
    
    def to_json(self) -> Dict:
        """Convert to JSON representation"""
        return {
            "id": self.id,
            "family": self.family.value,
            "base_form": self.base_form,
            "operators": [op.value for op in self.operators],
            "description": self.description
        }


class SymbolRegistry:
    """
    Registry of all symbols in the 373-417 block
    """
    
    def __init__(self):
        self.symbols: Dict[int, Symbol] = {}
        self._initialize_omega_family()
        self._initialize_delta_family()
        self._initialize_sigma_family()
    
    def _initialize_omega_family(self):
        """Initialize Ω family (373-399): Tokens/Entities"""
        # Base oval/circle
        self.symbols[373] = Symbol(373, SymbolFamily.OMEGA, "oval", [], "Base entity token")
        
        # Oval with dot variants
        self.symbols[374] = Symbol(374, SymbolFamily.OMEGA, "oval", [GraphicOperator.DOT], 
                                   "Entity instance (1 dot)")
        self.symbols[375] = Symbol(375, SymbolFamily.OMEGA, "oval", [GraphicOperator.DOT], 
                                   "Entity instance (2 dots)")
        self.symbols[376] = Symbol(376, SymbolFamily.OMEGA, "oval", [GraphicOperator.DOT], 
                                   "Entity instance (3 dots)")
        
        # Oval with stroke variants
        self.symbols[377] = Symbol(377, SymbolFamily.OMEGA, "oval", [GraphicOperator.STROKE], 
                                   "Qualified entity (1 stroke)")
        self.symbols[378] = Symbol(378, SymbolFamily.OMEGA, "oval", [GraphicOperator.STROKE], 
                                   "Qualified entity (2 strokes)")
        
        # Oval with brackets
        self.symbols[379] = Symbol(379, SymbolFamily.OMEGA, "oval", [GraphicOperator.BRACKET], 
                                   "Entity with delimited scope (left bracket)")
        self.symbols[380] = Symbol(380, SymbolFamily.OMEGA, "oval", [GraphicOperator.BRACKET], 
                                   "Entity with delimited scope (right bracket)")
        
        # Oval with sidebars
        self.symbols[381] = Symbol(381, SymbolFamily.OMEGA, "oval", [GraphicOperator.SIDEBARS], 
                                   "Entity with level/authority (1 sidebar)")
        self.symbols[382] = Symbol(382, SymbolFamily.OMEGA, "oval", [GraphicOperator.SIDEBARS], 
                                   "Entity with level/authority (2 sidebars)")
        self.symbols[383] = Symbol(383, SymbolFamily.OMEGA, "oval", [GraphicOperator.SIDEBARS], 
                                   "Entity with level/authority (3 sidebars)")
        
        # Oval with crown
        self.symbols[384] = Symbol(384, SymbolFamily.OMEGA, "oval", [GraphicOperator.CROWN], 
                                   "Entity with multiplexing (3 prongs)")
        self.symbols[385] = Symbol(385, SymbolFamily.OMEGA, "oval", [GraphicOperator.CROWN], 
                                   "Entity with multiplexing (5 prongs)")
        
        # Oval with fill
        self.symbols[386] = Symbol(386, SymbolFamily.OMEGA, "oval", [GraphicOperator.FILL], 
                                   "Consummated entity (partial fill)")
        self.symbols[387] = Symbol(387, SymbolFamily.OMEGA, "oval", [GraphicOperator.FILL], 
                                   "Consummated entity (full fill)")
        
        # Complex compositions (e.g., 394 = 373 + closure operator from U-family)
        self.symbols[394] = Symbol(394, SymbolFamily.OMEGA, "oval+closure", 
                                   [GraphicOperator.FILL], 
                                   "Closed institutional record (373 + 343 closure)")
        
        # Placeholder for remaining Omega symbols (388-399)
        for i in range(388, 400):
            if i not in self.symbols:
                self.symbols[i] = Symbol(i, SymbolFamily.OMEGA, "oval", [], 
                                        f"Entity variant {i}")
    
    def _initialize_delta_family(self):
        """Initialize Δ family (400-409): Relations/Bonds"""
        # Duplicated ovals (pairs)
        self.symbols[400] = Symbol(400, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair (horizontal)")
        self.symbols[401] = Symbol(401, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair (vertical)")
        self.symbols[402] = Symbol(402, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair with dot")
        self.symbols[403] = Symbol(403, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair with stroke")
        self.symbols[404] = Symbol(404, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair with brackets")
        self.symbols[405] = Symbol(405, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair with sidebars")
        self.symbols[406] = Symbol(406, SymbolFamily.DELTA, "double-oval", [GraphicOperator.DUP], 
                                   "Entity pair with crown")
        
        # Knots (strong bonds)
        self.symbols[407] = Symbol(407, SymbolFamily.DELTA, "knot", [GraphicOperator.KNOT], 
                                   "Bound pair (knot)")
        
        # Dumbbells with stems
        self.symbols[408] = Symbol(408, SymbolFamily.DELTA, "dumbbell", [GraphicOperator.STEM], 
                                   "Anchored relation (lower stem)")
        self.symbols[409] = Symbol(409, SymbolFamily.DELTA, "dumbbell", [GraphicOperator.STEM], 
                                   "Anchored relation (upper stem)")
    
    def _initialize_sigma_family(self):
        """Initialize Σ family (410-417): Counts/Stacks"""
        # Vertical stacks
        self.symbols[410] = Symbol(410, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 2 (2 discs)")
        self.symbols[411] = Symbol(411, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 3 (3 discs)")
        self.symbols[412] = Symbol(412, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 4 (4 discs)")
        self.symbols[413] = Symbol(413, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 5 (5 discs)")
        self.symbols[414] = Symbol(414, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 6 (6 discs)")
        self.symbols[415] = Symbol(415, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 7 (7 discs)")
        self.symbols[416] = Symbol(416, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 8 (8 discs)")
        self.symbols[417] = Symbol(417, SymbolFamily.SIGMA, "stack", [GraphicOperator.STACK], 
                                   "Count = 9 (9 discs)")
    
    def get_symbol(self, symbol_id: int) -> Optional[Symbol]:
        """Get a symbol by ID"""
        return self.symbols.get(symbol_id)
    
    def get_family_symbols(self, family: SymbolFamily) -> List[Symbol]:
        """Get all symbols in a family"""
        return [s for s in self.symbols.values() if s.family == family]
    
    def get_symbols_with_operator(self, operator: GraphicOperator) -> List[Symbol]:
        """Get all symbols that use a specific operator"""
        return [s for s in self.symbols.values() if s.has_operator(operator)]


@dataclass
class CompositionRule:
    """
    Represents a composition rule for combining symbols or operators
    """
    base_symbol: int  # Base symbol ID
    operator: GraphicOperator  # Applied operator
    result_symbol: int  # Resulting symbol ID
    description: str = ""
    
    def apply(self, registry: SymbolRegistry) -> bool:
        """Validate that this composition rule is correct"""
        base = registry.get_symbol(self.base_symbol)
        result = registry.get_symbol(self.result_symbol)
        if base and result:
            return self.operator in result.operators
        return False


class CompositionSystem:
    """
    Manages composition rules showing how symbols are connected
    """
    
    def __init__(self, registry: SymbolRegistry):
        self.registry = registry
        self.rules: List[CompositionRule] = []
        self._initialize_rules()
    
    def _initialize_rules(self):
        """Initialize known composition rules"""
        # Within Omega family
        self.rules.append(CompositionRule(373, GraphicOperator.DOT, 374, 
                                         "Base oval + dot → instance"))
        self.rules.append(CompositionRule(373, GraphicOperator.STROKE, 377, 
                                         "Base oval + stroke → qualified"))
        self.rules.append(CompositionRule(373, GraphicOperator.BRACKET, 379, 
                                         "Base oval + bracket → scoped"))
        self.rules.append(CompositionRule(373, GraphicOperator.SIDEBARS, 381, 
                                         "Base oval + sidebars → leveled"))
        self.rules.append(CompositionRule(373, GraphicOperator.CROWN, 384, 
                                         "Base oval + crown → multiplexed"))
        self.rules.append(CompositionRule(373, GraphicOperator.FILL, 386, 
                                         "Base oval + fill → consummated"))
        
        # Cross-family composition (critical case from problem statement)
        # 394 = 373 (oval base) + 343 (closure operator from U-family)
        self.rules.append(CompositionRule(373, GraphicOperator.FILL, 394, 
                                         "Oval + U-family closure → institutional record"))
        
        # Omega to Delta (via Dup operator)
        self.rules.append(CompositionRule(373, GraphicOperator.DUP, 400, 
                                         "Oval + dup → pair"))
        
        # Delta to Delta (via Knot)
        self.rules.append(CompositionRule(400, GraphicOperator.KNOT, 407, 
                                         "Pair + knot → bound pair"))
        
        # Omega to Sigma (via Stack)
        self.rules.append(CompositionRule(373, GraphicOperator.STACK, 410, 
                                         "Oval + stack(2) → count 2"))
        self.rules.append(CompositionRule(373, GraphicOperator.STACK, 411, 
                                         "Oval + stack(3) → count 3"))
    
    def get_composition(self, base_id: int, operator: GraphicOperator) -> Optional[int]:
        """Get the result symbol ID for a base symbol + operator"""
        for rule in self.rules:
            if rule.base_symbol == base_id and rule.operator == operator:
                return rule.result_symbol
        return None
    
    def get_decomposition(self, symbol_id: int) -> List[Tuple[int, GraphicOperator]]:
        """Get all possible decompositions of a symbol"""
        decompositions = []
        for rule in self.rules:
            if rule.result_symbol == symbol_id:
                decompositions.append((rule.base_symbol, rule.operator))
        return decompositions


def create_harappan_system() -> Tuple[SymbolRegistry, CompositionSystem]:
    """
    Factory function to create a complete Harappan symbol system
    """
    registry = SymbolRegistry()
    composition = CompositionSystem(registry)
    return registry, composition
