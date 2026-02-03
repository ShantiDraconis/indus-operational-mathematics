"""
Indus Script Analysis Tools

Core functionality for analyzing Indus script sequences, including frequency analysis,
co-occurrence patterns, and cluster detection. All methods are grounded in
information theory and statistical analysis.
"""

import numpy as np
from typing import Dict, List, Tuple, Set, Optional
from collections import Counter, defaultdict
import itertools
from .statistical_metrics import (
    pointwise_mutual_information,
    mutual_information,
    lift_ratio,
    positional_dependency
)


class IndusSequenceAnalyzer:
    """
    Main analyzer for Indus script sequences.
    
    This class provides methods for:
    - Frequency ranking
    - Co-occurrence analysis
    - Cluster detection
    - Cross-site invariance testing
    """
    
    def __init__(self, sequences: List[List[str]], site_labels: Optional[List[str]] = None):
        """
        Initialize analyzer with sequences.
        
        Args:
            sequences: List of symbol sequences
            site_labels: Optional list of site labels for each sequence
        """
        self.sequences = sequences
        self.site_labels = site_labels or ['unknown'] * len(sequences)
        
        # Build indices
        self._build_indices()
    
    def _build_indices(self):
        """Build internal indices for efficient querying."""
        self.symbol_counts = Counter()
        self.pair_counts = Counter()
        self.total_symbols = 0
        
        for seq in self.sequences:
            for symbol in seq:
                self.symbol_counts[symbol] += 1
                self.total_symbols += 1
            
            # Count adjacent pairs
            for i in range(len(seq) - 1):
                self.pair_counts[(seq[i], seq[i+1])] += 1
    
    def frequency_ranking(self, top_n: Optional[int] = None) -> List[Tuple[str, int, float]]:
        """
        Get frequency ranking of symbols.
        
        Args:
            top_n: Return only top N symbols (None for all)
        
        Returns:
            List of (symbol, count, frequency) tuples, sorted by count
        """
        ranking = [
            (symbol, count, count / self.total_symbols)
            for symbol, count in self.symbol_counts.most_common(top_n)
        ]
        return ranking
    
    def top_pmi_pairs(self, top_n: int = 50) -> List[Tuple[Tuple[str, str], float]]:
        """
        Get top N symbol pairs by PMI.
        
        High PMI indicates strong association between symbols.
        These are the "stable clusters" mentioned in the problem statement.
        
        Args:
            top_n: Number of top pairs to return
        
        Returns:
            List of ((symbol_a, symbol_b), pmi) tuples
        """
        pmi_scores = []
        
        for (a, b), count in self.pair_counts.items():
            pmi = pointwise_mutual_information(
                count,
                self.total_symbols,
                self.symbol_counts[a],
                self.symbol_counts[b]
            )
            pmi_scores.append(((a, b), pmi))
        
        # Sort by PMI descending
        pmi_scores.sort(key=lambda x: x[1], reverse=True)
        
        return pmi_scores[:top_n]
    
    def preferred_distances(
        self,
        symbol_a: str,
        symbol_b: str,
        max_distance: int = 10
    ) -> Dict[int, int]:
        """
        Get histogram of preferred distances between two symbols.
        
        This reveals structural constraints: "separated by specific distances".
        
        Args:
            symbol_a: First symbol
            symbol_b: Second symbol
            max_distance: Maximum distance to consider
        
        Returns:
            Dictionary mapping distance to count
        """
        return positional_dependency(self.sequences, symbol_a, symbol_b, max_distance)
    
    def site_stability(
        self,
        pair: Tuple[str, str]
    ) -> Dict[str, float]:
        """
        Measure stability of pair association across sites.
        
        Low variance = supra-regional standardization.
        High variance = site-specific patterns.
        
        Args:
            pair: Symbol pair to analyze
        
        Returns:
            Dictionary mapping site to PMI value
        """
        # Group sequences by site
        sequences_by_site = defaultdict(list)
        for seq, site in zip(self.sequences, self.site_labels):
            sequences_by_site[site].append(seq)
        
        # Calculate PMI for each site
        site_pmis = {}
        for site, seqs in sequences_by_site.items():
            # Count for this site
            symbol_counts = Counter()
            pair_count = 0
            total = 0
            
            for seq in seqs:
                for symbol in seq:
                    symbol_counts[symbol] += 1
                    total += 1
                
                for i in range(len(seq) - 1):
                    if (seq[i], seq[i+1]) == pair:
                        pair_count += 1
            
            if total > 0 and pair_count > 0:
                pmi = pointwise_mutual_information(
                    pair_count,
                    total,
                    symbol_counts[pair[0]],
                    symbol_counts[pair[1]]
                )
                site_pmis[site] = pmi
        
        return site_pmis
    
    def detect_clusters(
        self,
        min_pmi: float = 1.0,
        min_support: int = 5
    ) -> List[Set[str]]:
        """
        Detect symbol clusters using PMI-based community detection.
        
        Symbols that frequently co-occur form clusters. These represent
        "constrained configurations" or "validated states".
        
        Args:
            min_pmi: Minimum PMI to consider symbols related
            min_support: Minimum co-occurrence count
        
        Returns:
            List of symbol sets (clusters)
        """
        # Build graph of high-PMI pairs
        edges = set()
        for (a, b), count in self.pair_counts.items():
            if count >= min_support:
                pmi = pointwise_mutual_information(
                    count,
                    self.total_symbols,
                    self.symbol_counts[a],
                    self.symbol_counts[b]
                )
                if pmi >= min_pmi:
                    edges.add((a, b))
        
        # Find connected components (simple clustering)
        clusters = []
        visited = set()
        
        def dfs(node, cluster):
            if node in visited:
                return
            visited.add(node)
            cluster.add(node)
            
            # Find neighbors
            for (a, b) in edges:
                if a == node:
                    dfs(b, cluster)
                elif b == node:
                    dfs(a, cluster)
        
        # Find all clusters
        all_nodes = set()
        for (a, b) in edges:
            all_nodes.add(a)
            all_nodes.add(b)
        
        for node in all_nodes:
            if node not in visited:
                cluster = set()
                dfs(node, cluster)
                if len(cluster) > 1:  # Only keep multi-symbol clusters
                    clusters.append(cluster)
        
        return clusters
    
    def compression_metrics(self) -> Dict[str, float]:
        """
        Calculate information-theoretic compression metrics.
        
        High compression = "holographic principle" effect
        (small sequences carry much institutional information).
        
        Returns:
            Dictionary with entropy, redundancy, and compressibility metrics
        """
        # Calculate entropy
        probabilities = [count / self.total_symbols for count in self.symbol_counts.values()]
        entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
        
        # Maximum possible entropy
        n_symbols = len(self.symbol_counts)
        max_entropy = np.log2(n_symbols) if n_symbols > 0 else 0
        
        # Redundancy
        redundancy = 1 - (entropy / max_entropy) if max_entropy > 0 else 0
        
        # Average sequence length
        avg_length = np.mean([len(seq) for seq in self.sequences])
        
        return {
            'entropy': entropy,
            'max_entropy': max_entropy,
            'redundancy': redundancy,
            'avg_sequence_length': avg_length,
            'bits_per_symbol': entropy,
            'compression_ratio': max_entropy / entropy if entropy > 0 else 1.0
        }


def identify_closers(
    sequences: List[List[str]],
    position: str = 'end',
    min_frequency: float = 0.1
) -> List[Tuple[str, float]]:
    """
    Identify common "closer" symbols (symbols that end sequences).
    
    High frequency of specific closers indicates administrative/institutional function.
    
    Args:
        sequences: List of symbol sequences
        position: 'start' or 'end'
        min_frequency: Minimum frequency threshold
    
    Returns:
        List of (symbol, frequency) tuples
    """
    position_symbols = Counter()
    
    for seq in sequences:
        if len(seq) == 0:
            continue
        
        if position == 'end':
            position_symbols[seq[-1]] += 1
        elif position == 'start':
            position_symbols[seq[0]] += 1
    
    total = sum(position_symbols.values())
    
    closers = [
        (symbol, count / total)
        for symbol, count in position_symbols.most_common()
        if count / total >= min_frequency
    ]
    
    return closers
