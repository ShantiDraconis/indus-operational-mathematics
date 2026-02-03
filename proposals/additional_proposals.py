"""
Additional Harappan Proposals

This module contains implementations for the remaining proposals:
- Generative Art (Proposal 13)
- Algorithmic Law (Proposal 14)
- Brain-Computer Interface (Proposal 6)
- Information Physics (Proposal 12)
"""

from typing import List, Tuple, Dict, Optional
import random
from dataclasses import dataclass
from core.harappan_automaton import HarappanAutomaton, CLOSURE_MEANINGS


# Proposal 13: Generative Art
class HarappanGenerativeArt:
    """
    Generate valid Harappan inscriptions as architectural blueprints
    
    Algorithm:
    1. Generate valid inscriptions randomly
    2. Project to 3D as architecture
    3. Use as blueprint for construction
    """
    
    def __init__(self):
        self.automaton = HarappanAutomaton()
        
    def generate_random_inscription(self) -> List[Tuple[str, any]]:
        """Generate a random valid Harappan inscription"""
        inscription = []
        
        # Start with entity
        entity = random.randint(373, 399)
        inscription.append(('entity', entity))
        
        # Randomly choose simple or complex path
        if random.random() < 0.5:
            # Simple: entity -> closure
            closure = random.randint(342, 348)
            inscription.append(('closure', closure))
        else:
            # Complex: entity -> operator -> quantifier -> relation -> closure
            operators = ['dot', 'stroke', 'vertical', 'horizontal', 'oblique']
            inscription.append(('operator', random.choice(operators)))
            inscription.append(('quantifier', random.randint(1, 5)))
            inscription.append(('relation', random.randint(400, 409)))
            inscription.append(('closure', random.randint(342, 348)))
        
        return inscription
    
    def inscription_to_3d_blueprint(
        self, 
        inscription: List[Tuple[str, any]]
    ) -> Dict[str, any]:
        """
        Convert inscription to 3D architectural blueprint
        
        Mapping:
        - Entities → Building foundations
        - Operators → Structural elements
        - Quantifiers → Repetition count
        - Relations → Connections between buildings
        - Closures → Roof/completion elements
        """
        blueprint = {
            'foundations': [],
            'structures': [],
            'connections': [],
            'completions': [],
        }
        
        for symbol_type, value in inscription:
            if symbol_type == 'entity':
                # Map entity to foundation type
                foundation_type = f"Foundation_Type_{value % 10}"
                blueprint['foundations'].append({
                    'type': foundation_type,
                    'entity_id': value,
                })
            elif symbol_type == 'operator':
                # Map operator to structural element
                structure_map = {
                    'dot': 'Column',
                    'stroke': 'Beam',
                    'vertical': 'Wall',
                    'horizontal': 'Floor',
                    'oblique': 'Diagonal_Support',
                }
                blueprint['structures'].append(structure_map.get(value, 'Generic'))
            elif symbol_type == 'quantifier':
                # Repetition count for last structure
                if blueprint['structures']:
                    blueprint['structures'][-1] = {
                        'type': blueprint['structures'][-1],
                        'count': value,
                    }
            elif symbol_type == 'relation':
                # Connection type between buildings
                blueprint['connections'].append({
                    'relation_id': value,
                    'type': f"Connection_{value}",
                })
            elif symbol_type == 'closure':
                # Completion element
                blueprint['completions'].append({
                    'closure_id': value,
                    'meaning': CLOSURE_MEANINGS.get(value, 'Unknown'),
                })
        
        return blueprint
    
    def generate_city_layout(self, num_buildings: int = 10) -> List[Dict]:
        """Generate a city layout with multiple buildings"""
        city = []
        for _ in range(num_buildings):
            inscription = self.generate_random_inscription()
            blueprint = self.inscription_to_3d_blueprint(inscription)
            city.append({
                'inscription': inscription,
                'blueprint': blueprint,
            })
        return city


# Proposal 14: Algorithmic Law
@dataclass
class LegalCase:
    """A legal case represented as a symbol sequence"""
    case_id: int
    symbols: List[Tuple[str, any]]
    
    
class AlgorithmicLaw:
    """
    Legal system where:
    - Laws = Harappan grammar
    - Cases = Symbol sequences
    - Judgments = Validation by automaton
    - Precedents = Closed records
    
    Advantage: 100% consistent and predictable decisions
    """
    
    def __init__(self):
        self.precedents: Dict[int, LegalCase] = {}
        self.next_case_id = 1
        
    def file_case(self, symbols: List[Tuple[str, any]]) -> int:
        """File a new legal case"""
        case_id = self.next_case_id
        self.next_case_id += 1
        
        case = LegalCase(case_id=case_id, symbols=symbols)
        self.precedents[case_id] = case
        
        return case_id
    
    def judge_case(self, case_id: int) -> Dict[str, any]:
        """
        Judge a case using Harappan validation
        
        Returns:
            Judgment with validity, closure state, and reasoning
        """
        if case_id not in self.precedents:
            raise ValueError(f"Case {case_id} not found")
        
        case = self.precedents[case_id]
        automaton = HarappanAutomaton()
        
        # Validate the case
        is_valid = automaton.validate_sequence(case.symbols)
        
        # Get final state and closure
        final_state = automaton.current_state
        closure_symbol = None
        
        if automaton.inscription:
            last_symbol = automaton.inscription[-1]
            if last_symbol.type.value == 'closure':
                closure_symbol = last_symbol.id
        
        judgment = {
            'case_id': case_id,
            'valid': is_valid,
            'final_state': final_state.value,
            'closure': closure_symbol,
            'ruling': CLOSURE_MEANINGS.get(closure_symbol, 'Invalid') if closure_symbol else 'Incomplete',
            'precedent': is_valid,  # Valid cases become precedents
        }
        
        return judgment
    
    def find_similar_precedents(
        self, 
        symbols: List[Tuple[str, any]]
    ) -> List[int]:
        """Find similar precedents based on symbol patterns"""
        similar = []
        
        # Simple similarity: check if first entity matches
        if not symbols:
            return similar
        
        first_entity = symbols[0][1] if symbols[0][0] == 'entity' else None
        
        for case_id, case in self.precedents.items():
            if case.symbols and case.symbols[0][0] == 'entity':
                if case.symbols[0][1] == first_entity:
                    similar.append(case_id)
        
        return similar
    
    def get_consistent_rulings(self, entity_id: int) -> List[Dict]:
        """Get all rulings for a specific entity type"""
        rulings = []
        
        for case_id, case in self.precedents.items():
            if case.symbols and case.symbols[0][0] == 'entity':
                if case.symbols[0][1] == entity_id:
                    judgment = self.judge_case(case_id)
                    rulings.append(judgment)
        
        return rulings


# Proposal 6: Brain-Computer Interface
class HarappanBCI:
    """
    Brain-Computer Interface using Harappan symbols as "thought language"
    
    Protocol:
    - Thought "Approved" = Symbol 343
    - Thought "Rejected" = Symbol 346
    - Thought "Quantity 3" = |||
    
    Advantages:
    - Visual and symbolic
    - Direct state encoding
    - Finite and predictable structure
    """
    
    def __init__(self):
        self.thought_buffer: List[Tuple[str, any]] = []
        self.automaton = HarappanAutomaton()
        
    def think_symbol(self, symbol_type: str, value: any):
        """Register a thought symbol"""
        self.thought_buffer.append((symbol_type, value))
        
    def think_approved(self):
        """Think 'Approved'"""
        self.think_symbol('closure', 343)
        
    def think_rejected(self):
        """Think 'Rejected'"""
        self.think_symbol('closure', 342)
        
    def think_quantity(self, count: int):
        """Think a quantity"""
        self.think_symbol('quantifier', count)
        
    def complete_thought(self) -> bool:
        """Complete and validate current thought"""
        if not self.thought_buffer:
            return False
        
        # Ensure thought starts with entity if not present
        if self.thought_buffer[0][0] != 'entity':
            # Add default entity
            self.thought_buffer.insert(0, ('entity', 373))
        
        is_valid = self.automaton.validate_sequence(self.thought_buffer)
        
        if is_valid:
            self.thought_buffer = []  # Clear buffer
            self.automaton.reset()
        
        return is_valid
    
    def get_thought_state(self) -> str:
        """Get current thought state"""
        return self.automaton.current_state.value


# Proposal 12: Information Physics
class InformationPhysics:
    """
    Treat Harappan information as physical field
    
    - Entropy = Number of possible states (417^n)
    - Energy = Effort to reach closure
    - Force = Institutional pressure for validation
    
    Law: ΔS_harappan ≥ k * ln(N_states)
    """
    
    def __init__(self, k: float = 1.0):
        self.k = k  # Harappan constant
        
    def calculate_entropy(self, num_symbols: int, symbol_types: int = 417) -> float:
        """
        Calculate entropy for a Harappan inscription
        
        S = k * ln(N) where N = possible states
        """
        import math
        N = symbol_types ** num_symbols
        return self.k * math.log(N)
    
    def calculate_energy(self, inscription: List[Tuple[str, any]]) -> float:
        """
        Calculate energy (effort) to reach closure
        
        Energy increases with path length and complexity
        """
        base_energy = len(inscription)
        
        # Add complexity penalties
        complexity_factor = 1.0
        for symbol_type, _ in inscription:
            if symbol_type == 'relation':
                complexity_factor += 0.5
            elif symbol_type == 'quantifier':
                complexity_factor += 0.2
        
        return base_energy * complexity_factor
    
    def calculate_institutional_pressure(
        self, 
        current_state: str,
        target_state: str = 'CLOSED'
    ) -> float:
        """
        Calculate force (pressure) toward validation
        
        Pressure increases as we approach closure
        """
        state_order = ['INITIAL', 'ENTITY_LOADED', 'OPERATOR_APPLIED', 
                      'QUANTIFIED', 'RELATED', 'CLOSED']
        
        try:
            current_idx = state_order.index(current_state)
            target_idx = state_order.index(target_state)
            distance = target_idx - current_idx
            
            if distance <= 0:
                return 0.0
            
            # Force inversely proportional to distance
            return 1.0 / distance
        except ValueError:
            return 0.0
