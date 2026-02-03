"""
Harappan Symbol Frequency and Distribution Data

This module provides data structures and analysis for symbol frequencies
and distributions (Tables I, II, IV mentioned in the problem statement).
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Set
from collections import Counter, defaultdict

from harappan_symbols import Symbol, SymbolRegistry


@dataclass
class FrequencyData:
    """
    Frequency data for a symbol (Table I)
    """
    symbol_id: int
    total_occurrences: int = 0
    initial_position: int = 0
    medial_position: int = 0
    final_position: int = 0
    
    def get_position_distribution(self) -> Dict[str, float]:
        """Get percentage distribution by position"""
        if self.total_occurrences == 0:
            return {"initial": 0.0, "medial": 0.0, "final": 0.0}
        
        return {
            "initial": (self.initial_position / self.total_occurrences) * 100,
            "medial": (self.medial_position / self.total_occurrences) * 100,
            "final": (self.final_position / self.total_occurrences) * 100
        }


@dataclass
class PairFrequency:
    """
    Frequency of symbol pairs (Table II - recurring pairs)
    """
    first_symbol: int
    second_symbol: int
    occurrences: int = 0
    
    def __hash__(self):
        return hash((self.first_symbol, self.second_symbol))
    
    def __eq__(self, other):
        if not isinstance(other, PairFrequency):
            return False
        return (self.first_symbol == other.first_symbol and 
                self.second_symbol == other.second_symbol)


@dataclass
class ObjectDistribution:
    """
    Distribution of symbols by object type (Table IV)
    """
    symbol_id: int
    seal_count: int = 0
    tablet_count: int = 0
    pottery_count: int = 0
    other_count: int = 0
    
    def get_distribution(self) -> Dict[str, int]:
        """Get distribution by object type"""
        return {
            "seal": self.seal_count,
            "tablet": self.tablet_count,
            "pottery": self.pottery_count,
            "other": self.other_count
        }
    
    def total_occurrences(self) -> int:
        """Get total occurrences across all object types"""
        return (self.seal_count + self.tablet_count + 
                self.pottery_count + self.other_count)


class FrequencyAnalyzer:
    """
    Analyzes frequency and distribution patterns in Harappan texts
    """
    
    def __init__(self, registry: SymbolRegistry):
        self.registry = registry
        self.frequency_data: Dict[int, FrequencyData] = {}
        self.pair_frequencies: List[PairFrequency] = []
        self.object_distributions: Dict[int, ObjectDistribution] = {}
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize data structures with default values"""
        # Initialize frequency data for all symbols
        for symbol_id in range(373, 418):
            self.frequency_data[symbol_id] = FrequencyData(symbol_id)
            self.object_distributions[symbol_id] = ObjectDistribution(symbol_id)
    
    def record_occurrence(self, symbol_id: int, position: str, object_type: str = "other"):
        """
        Record an occurrence of a symbol
        
        Args:
            symbol_id: The symbol ID
            position: "initial", "medial", or "final"
            object_type: "seal", "tablet", "pottery", or "other"
        """
        if symbol_id in self.frequency_data:
            freq = self.frequency_data[symbol_id]
            freq.total_occurrences += 1
            
            if position == "initial":
                freq.initial_position += 1
            elif position == "medial":
                freq.medial_position += 1
            elif position == "final":
                freq.final_position += 1
        
        if symbol_id in self.object_distributions:
            dist = self.object_distributions[symbol_id]
            if object_type == "seal":
                dist.seal_count += 1
            elif object_type == "tablet":
                dist.tablet_count += 1
            elif object_type == "pottery":
                dist.pottery_count += 1
            else:
                dist.other_count += 1
    
    def record_pair(self, first_symbol: int, second_symbol: int):
        """Record a pair of adjacent symbols"""
        pair = PairFrequency(first_symbol, second_symbol, 1)
        
        # Check if pair already exists
        for existing_pair in self.pair_frequencies:
            if (existing_pair.first_symbol == first_symbol and 
                existing_pair.second_symbol == second_symbol):
                existing_pair.occurrences += 1
                return
        
        # Add new pair
        self.pair_frequencies.append(pair)
    
    def get_high_frequency_symbols(self, threshold: int = 10) -> List[int]:
        """
        Get symbols with frequency above threshold
        
        As mentioned in problem statement section 4:
        "Sinais de alta frequência (ex.: 373, 342, 343): operadores centrais"
        """
        return [
            symbol_id for symbol_id, freq in self.frequency_data.items()
            if freq.total_occurrences >= threshold
        ]
    
    def get_low_frequency_symbols(self, threshold: int = 5) -> List[int]:
        """
        Get symbols with frequency below threshold
        
        As mentioned in problem statement section 4:
        "Sinais de baixa frequência: instâncias específicas (ex.: 394, 407)"
        """
        return [
            symbol_id for symbol_id, freq in self.frequency_data.items()
            if 0 < freq.total_occurrences < threshold
        ]
    
    def get_most_common_pairs(self, n: int = 10) -> List[PairFrequency]:
        """Get the n most common symbol pairs"""
        sorted_pairs = sorted(self.pair_frequencies, 
                            key=lambda p: p.occurrences, 
                            reverse=True)
        return sorted_pairs[:n]
    
    def get_position_patterns(self, symbol_id: int) -> Dict[str, float]:
        """Get position distribution for a symbol"""
        if symbol_id in self.frequency_data:
            return self.frequency_data[symbol_id].get_position_distribution()
        return {}
    
    def get_object_preference(self, symbol_id: int) -> str:
        """Get the preferred object type for a symbol"""
        if symbol_id not in self.object_distributions:
            return "unknown"
        
        dist = self.object_distributions[symbol_id]
        counts = dist.get_distribution()
        
        if sum(counts.values()) == 0:
            return "unknown"
        
        return max(counts.items(), key=lambda x: x[1])[0]
    
    def analyze_family_patterns(self) -> Dict[str, any]:
        """
        Analyze patterns across symbol families
        
        From problem statement section 4:
        "Ω (entidades) → posição inicial/média"
        "Δ (relações) → posição média"
        "Σ (contagens) → posição média/final"
        """
        omega_positions = defaultdict(int)
        delta_positions = defaultdict(int)
        sigma_positions = defaultdict(int)
        
        # Omega family (373-399)
        for symbol_id in range(373, 400):
            if symbol_id in self.frequency_data:
                freq = self.frequency_data[symbol_id]
                omega_positions["initial"] += freq.initial_position
                omega_positions["medial"] += freq.medial_position
                omega_positions["final"] += freq.final_position
        
        # Delta family (400-409)
        for symbol_id in range(400, 410):
            if symbol_id in self.frequency_data:
                freq = self.frequency_data[symbol_id]
                delta_positions["initial"] += freq.initial_position
                delta_positions["medial"] += freq.medial_position
                delta_positions["final"] += freq.final_position
        
        # Sigma family (410-417)
        for symbol_id in range(410, 418):
            if symbol_id in self.frequency_data:
                freq = self.frequency_data[symbol_id]
                sigma_positions["initial"] += freq.initial_position
                sigma_positions["medial"] += freq.medial_position
                sigma_positions["final"] += freq.final_position
        
        return {
            "omega": dict(omega_positions),
            "delta": dict(delta_positions),
            "sigma": dict(sigma_positions)
        }
    
    def export_table_i(self) -> Dict[int, Dict[str, any]]:
        """Export frequency data (Table I format)"""
        result = {}
        for symbol_id, freq in self.frequency_data.items():
            if freq.total_occurrences > 0:
                result[symbol_id] = {
                    "total": freq.total_occurrences,
                    "positions": freq.get_position_distribution()
                }
        return result
    
    def export_table_ii(self) -> List[Dict[str, any]]:
        """Export pair frequency data (Table II format)"""
        return [
            {
                "first": pair.first_symbol,
                "second": pair.second_symbol,
                "occurrences": pair.occurrences
            }
            for pair in sorted(self.pair_frequencies, 
                             key=lambda p: p.occurrences, 
                             reverse=True)
        ]
    
    def export_table_iv(self) -> Dict[int, Dict[str, int]]:
        """Export object distribution data (Table IV format)"""
        result = {}
        for symbol_id, dist in self.object_distributions.items():
            if dist.total_occurrences() > 0:
                result[symbol_id] = dist.get_distribution()
        return result


def create_sample_data() -> FrequencyAnalyzer:
    """
    Create sample frequency data based on problem statement insights
    
    From section 4:
    - High frequency: 373, 342, 343 (central operators)
    - Low frequency: 394, 407 (specific instances)
    - Table IV: seals and tablets predominate, never decorative objects
    """
    from harappan_symbols import create_harappan_system
    
    registry, _ = create_harappan_system()
    analyzer = FrequencyAnalyzer(registry)
    
    # High frequency symbols (central operators)
    for _ in range(50):
        analyzer.record_occurrence(373, "initial", "seal")
        analyzer.record_occurrence(373, "medial", "tablet")
    
    # Medium frequency
    for _ in range(15):
        analyzer.record_occurrence(374, "medial", "seal")
        analyzer.record_occurrence(400, "medial", "tablet")
        analyzer.record_occurrence(410, "final", "seal")
    
    # Low frequency (specific instances)
    for _ in range(3):
        analyzer.record_occurrence(394, "medial", "seal")
        analyzer.record_occurrence(407, "medial", "tablet")
    
    # Common pairs (from Table II)
    analyzer.record_pair(373, 410)  # Entity + count
    analyzer.record_pair(373, 400)  # Entity + relation
    analyzer.record_pair(400, 373)  # Relation + entity
    
    return analyzer
