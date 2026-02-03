"""
Indus Script Statistical Analysis Framework

This module provides rigorous statistical tools for analyzing the Indus Valley script,
implementing measures discussed in the formalization document.

IMPORTANT DISCLAIMER:
All references to "non-locality", "entanglement", and "quantum" terminology are
STRICTLY METAPHORICAL and refer to:
- Statistical correlation
- Distributed standardization
- Long-range dependencies

This is NOT a claim of quantum mechanical processes in archaeological artifacts.
"""

import numpy as np
from typing import List, Tuple, Dict, Set, Optional
from dataclasses import dataclass
from collections import Counter, defaultdict
import math
from scipy.stats import chi2_contingency, permutation_test
from itertools import combinations


@dataclass
class Symbol:
    """Represents an Indus script symbol"""
    id: int
    category: str  # 'numeric', 'pictographic', 'abstract'
    name: str = ""
    
    def __hash__(self):
        return hash((self.id, self.category))


@dataclass
class Sequence:
    """Represents a sequence of symbols (e.g., from one seal)"""
    symbols: List[Symbol]
    site: str  # Archaeological site identifier
    artifact_type: str  # 'seal', 'tablet', 'pottery', etc.
    
    def __len__(self):
        return len(self.symbols)


class IndusStatisticalAnalysis:
    """
    Core statistical analysis tools for Indus script.
    
    Implements:
    - PMI (Pointwise Mutual Information)
    - Mutual Information
    - Lift / Odds Ratio
    - Permutation tests
    - Positional dependency analysis
    - Cross-site variance (distributed standardization measure)
    """
    
    def __init__(self, sequences: List[Sequence]):
        self.sequences = sequences
        self._compute_frequency_tables()
    
    def _compute_frequency_tables(self):
        """Compute frequency tables for symbols and pairs"""
        # Single symbol frequencies
        self.symbol_freq = Counter()
        self.total_symbols = 0
        
        # Pair frequencies
        self.pair_freq = Counter()
        self.total_pairs = 0
        
        # Site-specific frequencies
        self.site_symbol_freq = defaultdict(Counter)
        self.site_pair_freq = defaultdict(Counter)
        
        for seq in self.sequences:
            site = seq.site
            symbols = seq.symbols
            
            # Count symbols
            for sym in symbols:
                self.symbol_freq[sym] += 1
                self.site_symbol_freq[site][sym] += 1
                self.total_symbols += 1
            
            # Count pairs (co-occurrences in same sequence)
            for i, sym1 in enumerate(symbols):
                for j, sym2 in enumerate(symbols):
                    if i < j:  # Only count each pair once
                        pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
                        self.pair_freq[pair] += 1
                        self.site_pair_freq[site][pair] += 1
                        self.total_pairs += 1
    
    def pmi(self, sym1: Symbol, sym2: Symbol) -> float:
        """
        Pointwise Mutual Information (PMI)
        
        PMI measures association strength between two symbols.
        This is a STATISTICAL measure, NOT quantum entanglement.
        
        PMI(x,y) = log(P(x,y) / (P(x) * P(y)))
        
        Returns:
            float: PMI value. Positive = symbols co-occur more than expected by chance
        """
        pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
        
        # Joint probability P(x,y)
        p_xy = self.pair_freq[pair] / self.total_pairs if self.total_pairs > 0 else 0
        
        # Marginal probabilities
        p_x = self.symbol_freq[sym1] / self.total_symbols if self.total_symbols > 0 else 0
        p_y = self.symbol_freq[sym2] / self.total_symbols if self.total_symbols > 0 else 0
        
        # Avoid log(0)
        if p_xy == 0 or p_x == 0 or p_y == 0:
            return float('-inf')
        
        return math.log2(p_xy / (p_x * p_y))
    
    def mutual_information(self, sym1: Symbol, sym2: Symbol) -> float:
        """
        Mutual Information between two symbols
        
        This is a STATISTICAL measure of correlation strength.
        
        Returns:
            float: MI value in bits
        """
        pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
        
        # Get frequencies
        n_xy = self.pair_freq[pair]
        n_x = self.symbol_freq[sym1]
        n_y = self.symbol_freq[sym2]
        n_total = len(self.sequences)
        
        # Create contingency table
        # [both present, x only, y only, neither]
        n_x_only = n_x - n_xy
        n_y_only = n_y - n_xy
        n_neither = n_total - n_x - n_y + n_xy
        
        contingency = np.array([
            [n_xy, n_x_only],
            [n_y_only, n_neither]
        ])
        
        # Compute MI from contingency table
        mi = 0.0
        total = contingency.sum()
        
        for i in range(2):
            for j in range(2):
                if contingency[i, j] > 0:
                    p_ij = contingency[i, j] / total
                    p_i = contingency[i, :].sum() / total
                    p_j = contingency[:, j].sum() / total
                    mi += p_ij * math.log2(p_ij / (p_i * p_j))
        
        return mi
    
    def lift(self, sym1: Symbol, sym2: Symbol) -> float:
        """
        Lift (Odds Ratio)
        
        Lift = P(x,y) / (P(x) * P(y))
        
        Lift > 1: symbols co-occur more than expected
        Lift < 1: symbols co-occur less than expected
        Lift = 1: independent
        
        Returns:
            float: Lift value
        """
        pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
        
        p_xy = self.pair_freq[pair] / self.total_pairs if self.total_pairs > 0 else 0
        p_x = self.symbol_freq[sym1] / self.total_symbols if self.total_symbols > 0 else 0
        p_y = self.symbol_freq[sym2] / self.total_symbols if self.total_symbols > 0 else 0
        
        if p_x == 0 or p_y == 0:
            return 0.0
        
        return p_xy / (p_x * p_y)
    
    def positional_dependency(self, sym1: Symbol, sym2: Symbol) -> Dict[int, int]:
        """
        Analyze positional dependency between symbols
        
        Returns histogram of distances when both symbols co-occur.
        This reveals "preferred distances" in the grammar.
        
        Returns:
            Dict[int, int]: Distance -> frequency mapping
        """
        distance_hist = Counter()
        
        for seq in self.sequences:
            # Find all positions of each symbol
            pos1 = [i for i, s in enumerate(seq.symbols) if s == sym1]
            pos2 = [i for i, s in enumerate(seq.symbols) if s == sym2]
            
            # Compute all pairwise distances
            for p1 in pos1:
                for p2 in pos2:
                    dist = abs(p1 - p2)
                    distance_hist[dist] += 1
        
        return dict(distance_hist)
    
    def permutation_test(self, sym1: Symbol, sym2: Symbol, n_permutations: int = 1000) -> float:
        """
        Permutation test for co-occurrence significance
        
        Tests null hypothesis: symbols co-occur by chance
        
        Returns:
            float: p-value
        """
        # Observed co-occurrence count
        pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
        observed = self.pair_freq[pair]
        
        # Create random permutations and count co-occurrences
        random_counts = []
        
        for _ in range(n_permutations):
            # Shuffle symbols within each sequence
            shuffled_count = 0
            for seq in self.sequences:
                shuffled_symbols = np.random.permutation(seq.symbols)
                # Check if both symbols present
                if sym1 in shuffled_symbols and sym2 in shuffled_symbols:
                    shuffled_count += 1
            
            random_counts.append(shuffled_count)
        
        # Compute p-value
        random_counts = np.array(random_counts)
        p_value = (random_counts >= observed).sum() / n_permutations
        
        return p_value
    
    def cross_site_variance(self, sym1: Symbol, sym2: Symbol) -> float:
        """
        Cross-site variance of co-occurrence pattern
        
        LOW variance = HIGH standardization = "non-local invariance"
        (STATISTICAL distributed standardization, NOT quantum non-locality)
        
        Returns:
            float: Variance of PMI across sites
        """
        site_pmis = []
        
        for site in set(seq.site for seq in self.sequences):
            # Compute site-specific PMI
            pair = (sym1, sym2) if sym1.id <= sym2.id else (sym2, sym1)
            
            site_pair_freq = self.site_pair_freq[site][pair]
            site_total_pairs = sum(self.site_pair_freq[site].values())
            
            site_sym1_freq = self.site_symbol_freq[site][sym1]
            site_sym2_freq = self.site_symbol_freq[site][sym2]
            site_total_symbols = sum(self.site_symbol_freq[site].values())
            
            if site_total_pairs > 0 and site_total_symbols > 0:
                p_xy = site_pair_freq / site_total_pairs
                p_x = site_sym1_freq / site_total_symbols
                p_y = site_sym2_freq / site_total_symbols
                
                if p_xy > 0 and p_x > 0 and p_y > 0:
                    site_pmi = math.log2(p_xy / (p_x * p_y))
                    site_pmis.append(site_pmi)
        
        if len(site_pmis) < 2:
            return 0.0
        
        return np.var(site_pmis)
    
    def find_stable_clusters(self, min_pmi: float = 1.0, max_variance: float = 0.5) -> List[Tuple[Symbol, Symbol, float, float]]:
        """
        Find symbol pairs that form "stable clusters" (non-local invariants)
        
        Criteria:
        1. High PMI (strong co-occurrence)
        2. Low cross-site variance (distributed standardization)
        
        These are "entangled clusters" in the STATISTICAL sense.
        
        Returns:
            List of (sym1, sym2, pmi, variance) tuples
        """
        clusters = []
        
        # Get all unique symbols
        all_symbols = set(self.symbol_freq.keys())
        
        # Test all pairs
        for sym1, sym2 in combinations(all_symbols, 2):
            pmi_val = self.pmi(sym1, sym2)
            if pmi_val >= min_pmi:
                variance = self.cross_site_variance(sym1, sym2)
                if variance <= max_variance:
                    clusters.append((sym1, sym2, pmi_val, variance))
        
        # Sort by PMI (strongest first)
        clusters.sort(key=lambda x: x[2], reverse=True)
        
        return clusters
    
    def institutional_vs_ritual_classification(self, seq: Sequence) -> Dict[str, float]:
        """
        Classify sequence as administrative vs ritual
        
        Based on features:
        - Administrative: high repetition, stable closers, less pictographic
        - Ritual: more pictographic motifs, more symbolic composition
        
        Returns:
            Dict with regime probabilities
        """
        # Feature extraction
        has_closer = False  # Would check for known closing symbols
        repetition_rate = len(seq.symbols) / len(set(seq.symbols)) if seq.symbols else 1.0
        pictographic_ratio = sum(1 for s in seq.symbols if s.category == 'pictographic') / len(seq.symbols) if seq.symbols else 0
        
        # Simple heuristic model (would be trained on labeled data)
        admin_score = repetition_rate * (1 - pictographic_ratio)
        ritual_score = pictographic_ratio * (2 - repetition_rate)
        
        total = admin_score + ritual_score
        if total == 0:
            return {'administrative': 0.5, 'ritual': 0.5}
        
        return {
            'administrative': admin_score / total,
            'ritual': ritual_score / total
        }


def compute_top_correlations(sequences: List[Sequence], top_n: int = 50) -> List[Dict]:
    """
    Compute top N symbol pair correlations
    
    Returns list of dicts with correlation metrics for each pair
    """
    analyzer = IndusStatisticalAnalysis(sequences)
    
    # Get all pairs from frequency table
    all_pairs = list(analyzer.pair_freq.keys())
    
    results = []
    for sym1, sym2 in all_pairs[:top_n]:
        pmi_val = analyzer.pmi(sym1, sym2)
        mi_val = analyzer.mutual_information(sym1, sym2)
        lift_val = analyzer.lift(sym1, sym2)
        variance = analyzer.cross_site_variance(sym1, sym2)
        
        results.append({
            'symbol1': sym1.id,
            'symbol2': sym2.id,
            'pmi': pmi_val,
            'mutual_information': mi_val,
            'lift': lift_val,
            'cross_site_variance': variance,
            'is_stable_cluster': pmi_val >= 1.0 and variance <= 0.5
        })
    
    return sorted(results, key=lambda x: x['pmi'], reverse=True)


if __name__ == '__main__':
    # Example usage
    print("Indus Script Statistical Analysis Framework")
    print("=" * 60)
    print()
    print("DISCLAIMER: All 'non-locality' and 'entanglement' terminology")
    print("refers to STATISTICAL correlations and distributed standardization,")
    print("NOT quantum mechanical phenomena.")
    print()
    print("This module provides rigorous statistical tools for analyzing")
    print("the Indus Valley script.")
