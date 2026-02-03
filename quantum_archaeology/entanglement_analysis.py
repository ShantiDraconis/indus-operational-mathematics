"""
Entanglement Analysis: Quantum-inspired methods for analyzing symbol correlations.

This module implements algorithms inspired by quantum entanglement to measure
the correlation and interdependence between symbols in the Indus script corpus.
"""

import math
from typing import Dict, List, Tuple, Set
from collections import defaultdict
import numpy as np

from .symbol_system import Symbol, SymbolCorpus, Inscription


class EntanglementAnalyzer:
    """
    Analyzes symbol correlations using quantum-inspired entanglement metrics.
    
    The core idea is that symbols that consistently appear together across
    different contexts and locations demonstrate a form of "entanglement" -
    a deep correlation that transcends simple co-occurrence.
    """
    
    def __init__(self, corpus: SymbolCorpus):
        self.corpus = corpus
        
    def calculate_entanglement_entropy(self, symbol_id: str) -> float:
        """
        Calculate the entanglement entropy for a symbol.
        
        Entanglement entropy measures how "entangled" a symbol is with the rest
        of the corpus. Higher entropy indicates the symbol appears in many
        different contexts with many different partners.
        
        Inspired by von Neumann entropy in quantum mechanics:
        S = -Σ p_i * log(p_i)
        
        Args:
            symbol_id: The symbol to analyze
            
        Returns:
            Entanglement entropy value (higher = more entangled)
        """
        inscriptions = self.corpus.get_inscriptions_with_symbol(symbol_id)
        
        if not inscriptions:
            return 0.0
        
        # Get all symbols that co-occur with this symbol
        neighbors = self.corpus.get_symbol_neighbors(symbol_id, max_distance=5)
        
        if not neighbors:
            return 0.0
        
        # Calculate probability distribution
        total = sum(neighbors.values())
        probabilities = [count / total for count in neighbors.values()]
        
        # Calculate entropy: -Σ p * log(p)
        entropy = -sum(p * math.log(p + 1e-10) for p in probabilities)
        
        return entropy
    
    def calculate_mutual_information(self, symbol_id1: str, symbol_id2: str) -> float:
        """
        Calculate mutual information between two symbols.
        
        Mutual information measures how much knowing about one symbol's presence
        tells us about the other's presence. This is analogous to measuring
        quantum correlations between entangled particles.
        
        I(X;Y) = Σ p(x,y) * log(p(x,y) / (p(x)*p(y)))
        
        Args:
            symbol_id1: First symbol
            symbol_id2: Second symbol
            
        Returns:
            Mutual information value (higher = more correlated)
        """
        total_inscriptions = len(self.corpus.inscriptions)
        
        if total_inscriptions == 0:
            return 0.0
        
        # Count occurrences
        count_s1 = len(self.corpus.get_inscriptions_with_symbol(symbol_id1))
        count_s2 = len(self.corpus.get_inscriptions_with_symbol(symbol_id2))
        
        # Count co-occurrences
        count_both = 0
        for inscription in self.corpus.inscriptions:
            symbol_ids = [s.id for s in inscription.symbols]
            if symbol_id1 in symbol_ids and symbol_id2 in symbol_ids:
                count_both += 1
        
        # Calculate probabilities
        p_s1 = count_s1 / total_inscriptions
        p_s2 = count_s2 / total_inscriptions
        p_both = count_both / total_inscriptions
        p_s1_not = 1 - p_s1
        p_s2_not = 1 - p_s2
        p_s1_not_s2 = (count_s2 - count_both) / total_inscriptions
        p_s1_s2_not = (count_s1 - count_both) / total_inscriptions
        p_neither = 1 - p_s1 - p_s2 + p_both
        
        # Calculate mutual information
        mi = 0.0
        
        if p_both > 0:
            mi += p_both * math.log((p_both / (p_s1 * p_s2)) + 1e-10)
        if p_s1_s2_not > 0 and p_s2_not > 0:
            mi += p_s1_s2_not * math.log((p_s1_s2_not / (p_s1 * p_s2_not)) + 1e-10)
        if p_s1_not_s2 > 0 and p_s1_not > 0:
            mi += p_s1_not_s2 * math.log((p_s1_not_s2 / (p_s1_not * p_s2)) + 1e-10)
        if p_neither > 0:
            mi += p_neither * math.log((p_neither / (p_s1_not * p_s2_not)) + 1e-10)
        
        return max(0.0, mi)
    
    def find_entangled_clusters(self, min_correlation: float = 0.5) -> List[Set[str]]:
        """
        Identify clusters of symbols that are highly entangled with each other.
        
        These clusters represent symbols that almost always appear together,
        similar to how entangled quantum particles maintain correlated states.
        
        Args:
            min_correlation: Minimum mutual information threshold
            
        Returns:
            List of symbol clusters (sets of symbol IDs)
        """
        # Build correlation matrix
        symbol_ids = list(self.corpus.symbols.keys())
        correlations: Dict[Tuple[str, str], float] = {}
        
        for i, sid1 in enumerate(symbol_ids):
            for sid2 in symbol_ids[i+1:]:
                mi = self.calculate_mutual_information(sid1, sid2)
                if mi >= min_correlation:
                    correlations[(sid1, sid2)] = mi
        
        # Find connected components (clusters)
        clusters: List[Set[str]] = []
        processed: Set[str] = set()
        
        for sid1, sid2 in correlations.keys():
            if sid1 not in processed or sid2 not in processed:
                # Start new cluster or extend existing
                cluster = None
                for c in clusters:
                    if sid1 in c or sid2 in c:
                        cluster = c
                        break
                
                if cluster is None:
                    cluster = {sid1, sid2}
                    clusters.append(cluster)
                else:
                    cluster.add(sid1)
                    cluster.add(sid2)
                
                processed.add(sid1)
                processed.add(sid2)
        
        return clusters
    
    def calculate_non_locality_index(self, symbol_id: str) -> float:
        """
        Calculate how "non-local" a symbol is across different sites.
        
        A high non-locality index indicates the symbol appears with similar
        patterns across geographically distant locations, analogous to
        quantum non-locality.
        
        Args:
            symbol_id: The symbol to analyze
            
        Returns:
            Non-locality index (0 to 1, higher = more non-local)
        """
        location_dist = self.corpus.get_location_distribution(symbol_id)
        
        if len(location_dist) <= 1:
            return 0.0  # Only at one location = fully local
        
        # Calculate how evenly distributed across locations
        total = sum(location_dist.values())
        if total == 0:
            return 0.0
        
        probabilities = [count / total for count in location_dist.values()]
        
        # Use entropy as measure of distribution
        # Normalize by max possible entropy
        entropy = -sum(p * math.log(p + 1e-10) for p in probabilities)
        max_entropy = math.log(len(location_dist))
        
        non_locality = entropy / max_entropy if max_entropy > 0 else 0.0
        
        return non_locality
    
    def map_to_hilbert_space(self, symbol_id: str, dimensions: int = 10) -> np.ndarray:
        """
        Map a symbol to a high-dimensional Hilbert space based on its relationships.
        
        In quantum mechanics, quantum states exist in Hilbert spaces. Here, we
        represent each symbol as a vector in a high-dimensional space where
        dimensions correspond to different meaning potentials.
        
        Args:
            symbol_id: The symbol to map
            dimensions: Number of dimensions in the Hilbert space
            
        Returns:
            NumPy array representing the symbol in Hilbert space
        """
        symbol = self.corpus.get_symbol(symbol_id)
        if not symbol:
            return np.zeros(dimensions)
        
        # Initialize vector
        vector = np.zeros(dimensions)
        
        # Dimension 0: Normalized frequency
        max_freq = max((s.frequency for s in self.corpus.symbols.values()), default=1)
        vector[0] = symbol.frequency / max_freq if max_freq > 0 else 0
        
        # Dimension 1: Entanglement entropy (normalized)
        entropy = self.calculate_entanglement_entropy(symbol_id)
        vector[1] = min(entropy / 5.0, 1.0)  # Normalize to [0, 1]
        
        # Dimension 2: Non-locality index
        vector[2] = self.calculate_non_locality_index(symbol_id)
        
        # Dimension 3-4: Context distribution
        inscriptions = self.corpus.get_inscriptions_with_symbol(symbol_id)
        if inscriptions:
            admin_ratio = sum(1 for i in inscriptions if i.context.value == "administrative") / len(inscriptions)
            ritual_ratio = sum(1 for i in inscriptions if i.context.value == "ritual") / len(inscriptions)
            vector[3] = admin_ratio
            vector[4] = ritual_ratio
        
        # Dimensions 5-9: Top neighbor correlations
        neighbors = self.corpus.get_symbol_neighbors(symbol_id, max_distance=2)
        if neighbors:
            top_neighbors = sorted(neighbors.items(), key=lambda x: x[1], reverse=True)[:5]
            for i, (neighbor_id, count) in enumerate(top_neighbors):
                if 5 + i < dimensions:
                    mi = self.calculate_mutual_information(symbol_id, neighbor_id)
                    vector[5 + i] = min(mi, 1.0)
        
        # Normalize vector
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector
    
    def analyze_symbol_superposition(self, symbol_id: str) -> Dict[str, any]:
        """
        Analyze the "superposition" of potential meanings for a symbol.
        
        Before measurement (contextualization), a symbol exists in a superposition
        of potential meanings. This method analyzes the different contexts and
        environments where the symbol appears.
        
        Args:
            symbol_id: The symbol to analyze
            
        Returns:
            Dictionary with superposition analysis
        """
        inscriptions = self.corpus.get_inscriptions_with_symbol(symbol_id)
        
        if not inscriptions:
            return {"error": "Symbol not found in corpus"}
        
        # Analyze contexts (potential meaning states)
        context_counts = defaultdict(int)
        location_counts = defaultdict(int)
        position_stats = []
        
        for inscription in inscriptions:
            context_counts[inscription.context.value] += 1
            location_counts[inscription.location.value] += 1
            
            # Find position of symbol in inscription
            symbol_ids = [s.id for s in inscription.symbols]
            positions = [i for i, sid in enumerate(symbol_ids) if sid == symbol_id]
            position_stats.extend(positions)
        
        total = len(inscriptions)
        
        return {
            "symbol_id": symbol_id,
            "total_occurrences": total,
            "context_probabilities": {
                ctx: count / total for ctx, count in context_counts.items()
            },
            "location_probabilities": {
                loc: count / total for loc, count in location_counts.items()
            },
            "average_position": sum(position_stats) / len(position_stats) if position_stats else 0,
            "entanglement_entropy": self.calculate_entanglement_entropy(symbol_id),
            "non_locality_index": self.calculate_non_locality_index(symbol_id),
        }
    
    def generate_correlation_report(self) -> Dict[str, any]:
        """
        Generate a comprehensive report on symbol correlations in the corpus.
        
        Returns:
            Dictionary containing various correlation metrics
        """
        symbol_ids = list(self.corpus.symbols.keys())
        
        # Calculate entanglement entropies for all symbols
        entropies = {
            sid: self.calculate_entanglement_entropy(sid)
            for sid in symbol_ids
        }
        
        # Find most entangled symbols
        most_entangled = sorted(entropies.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Find symbol pairs with highest mutual information
        strong_correlations = []
        for i, sid1 in enumerate(symbol_ids):
            for sid2 in symbol_ids[i+1:]:
                mi = self.calculate_mutual_information(sid1, sid2)
                if mi > 0.1:  # Threshold
                    strong_correlations.append((sid1, sid2, mi))
        
        strong_correlations.sort(key=lambda x: x[2], reverse=True)
        
        # Find entangled clusters
        clusters = self.find_entangled_clusters(min_correlation=0.3)
        
        return {
            "corpus_stats": self.corpus.get_corpus_statistics(),
            "most_entangled_symbols": most_entangled[:5],
            "strongest_correlations": strong_correlations[:10],
            "entangled_clusters": [list(cluster) for cluster in clusters],
            "average_entanglement_entropy": sum(entropies.values()) / len(entropies) if entropies else 0,
        }
