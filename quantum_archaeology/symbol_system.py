"""
Symbol System: Data structures for representing Indus script symbols and their relationships.

This module provides classes for representing symbols, their contexts, and the corpus
of inscriptions, enabling quantum-inspired analysis of symbol correlations.
"""

from typing import List, Dict, Set, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class SymbolContext(Enum):
    """Contexts in which symbols appear (measurement contexts in quantum analogy)"""
    ADMINISTRATIVE = "administrative"
    RITUAL = "ritual"
    TRADE = "trade"
    UNKNOWN = "unknown"


class Location(Enum):
    """Major Harappan sites"""
    MOHENJO_DARO = "mohenjo_daro"
    HARAPPA = "harappa"
    DHOLAVIRA = "dholavira"
    LOTHAL = "lothal"
    KALIBANGAN = "kalibangan"
    RAKHIGARHI = "rakhigarhi"
    UNKNOWN = "unknown"


@dataclass
class Symbol:
    """
    Represents a single Indus script symbol.
    
    In the quantum analogy, each symbol exists in a superposition of potential meanings
    until "observed" (contextualized) in a specific inscription.
    """
    id: str
    name: str
    description: str = ""
    frequency: int = 0
    potential_meanings: List[str] = field(default_factory=list)
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.id == other.id
        return False
    
    def __repr__(self):
        return f"Symbol({self.id}, {self.name})"


@dataclass
class Inscription:
    """
    Represents a sequence of symbols (e.g., on a seal or pottery).
    
    The inscription represents a "measurement" that collapses the superposition
    of symbol meanings into a specific institutional function.
    """
    id: str
    symbols: List[Symbol]
    location: Location
    context: SymbolContext
    archaeological_context: str = ""
    
    def get_symbol_sequence(self) -> List[str]:
        """Returns the sequence of symbol IDs"""
        return [s.id for s in self.symbols]
    
    def __repr__(self):
        symbol_ids = '-'.join([s.id for s in self.symbols])
        return f"Inscription({self.id}, [{symbol_ids}], {self.location.value})"


class SymbolCorpus:
    """
    Manages the entire corpus of Indus script symbols and inscriptions.
    
    This class provides methods for querying symbol relationships and patterns
    across the corpus, enabling entanglement-like analysis.
    """
    
    def __init__(self):
        self.symbols: Dict[str, Symbol] = {}
        self.inscriptions: List[Inscription] = []
        self._symbol_co_occurrence: Optional[Dict[Tuple[str, str], int]] = None
        
    def add_symbol(self, symbol: Symbol) -> None:
        """Add a symbol to the corpus"""
        self.symbols[symbol.id] = symbol
        self._symbol_co_occurrence = None  # Invalidate cache
        
    def add_inscription(self, inscription: Inscription) -> None:
        """Add an inscription to the corpus"""
        self.inscriptions.append(inscription)
        
        # Update symbol frequencies
        for symbol in inscription.symbols:
            if symbol.id in self.symbols:
                self.symbols[symbol.id].frequency += 1
        
        self._symbol_co_occurrence = None  # Invalidate cache
        
    def get_symbol(self, symbol_id: str) -> Optional[Symbol]:
        """Retrieve a symbol by ID"""
        return self.symbols.get(symbol_id)
    
    def get_inscriptions_with_symbol(self, symbol_id: str) -> List[Inscription]:
        """Find all inscriptions containing a specific symbol"""
        return [insc for insc in self.inscriptions 
                if any(s.id == symbol_id for s in insc.symbols)]
    
    def get_inscriptions_by_location(self, location: Location) -> List[Inscription]:
        """Find all inscriptions from a specific location"""
        return [insc for insc in self.inscriptions if insc.location == location]
    
    def get_inscriptions_by_context(self, context: SymbolContext) -> List[Inscription]:
        """Find all inscriptions in a specific context"""
        return [insc for insc in self.inscriptions if insc.context == context]
    
    def calculate_co_occurrence(self) -> Dict[Tuple[str, str], int]:
        """
        Calculate co-occurrence matrix for all symbol pairs.
        
        This represents the "entanglement" between symbols - how often they appear
        together in inscriptions.
        """
        if self._symbol_co_occurrence is not None:
            return self._symbol_co_occurrence
        
        co_occurrence: Dict[Tuple[str, str], int] = {}
        
        for inscription in self.inscriptions:
            symbol_ids = [s.id for s in inscription.symbols]
            
            # Count all pairs in this inscription
            for i, sid1 in enumerate(symbol_ids):
                for sid2 in symbol_ids[i+1:]:
                    # Create ordered pair
                    pair = tuple(sorted([sid1, sid2]))
                    co_occurrence[pair] = co_occurrence.get(pair, 0) + 1
        
        self._symbol_co_occurrence = co_occurrence
        return co_occurrence
    
    def get_symbol_neighbors(self, symbol_id: str, max_distance: int = 1) -> Dict[str, int]:
        """
        Find symbols that appear near a given symbol (within max_distance positions).
        
        This identifies "entangled" symbols in the quantum analogy.
        """
        neighbors: Dict[str, int] = {}
        
        for inscription in self.inscriptions:
            symbol_ids = [s.id for s in inscription.symbols]
            
            # Find positions of target symbol
            positions = [i for i, sid in enumerate(symbol_ids) if sid == symbol_id]
            
            for pos in positions:
                # Check symbols within distance
                for i in range(max(0, pos - max_distance), 
                             min(len(symbol_ids), pos + max_distance + 1)):
                    if i != pos:
                        neighbor_id = symbol_ids[i]
                        neighbors[neighbor_id] = neighbors.get(neighbor_id, 0) + 1
        
        return neighbors
    
    def get_location_distribution(self, symbol_id: str) -> Dict[Location, int]:
        """
        Get the distribution of a symbol across different locations.
        
        This demonstrates the "non-local" nature of symbol patterns across
        geographically distant sites.
        """
        distribution: Dict[Location, int] = {}
        
        inscriptions = self.get_inscriptions_with_symbol(symbol_id)
        for inscription in inscriptions:
            loc = inscription.location
            distribution[loc] = distribution.get(loc, 0) + 1
        
        return distribution
    
    def get_corpus_statistics(self) -> Dict[str, any]:
        """Get overall statistics about the corpus"""
        return {
            "total_symbols": len(self.symbols),
            "total_inscriptions": len(self.inscriptions),
            "average_inscription_length": sum(len(i.symbols) for i in self.inscriptions) / len(self.inscriptions) if self.inscriptions else 0,
            "locations": len(set(i.location for i in self.inscriptions)),
            "contexts": len(set(i.context for i in self.inscriptions)),
        }
    
    def __repr__(self):
        return f"SymbolCorpus({len(self.symbols)} symbols, {len(self.inscriptions)} inscriptions)"
