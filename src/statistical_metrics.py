"""
Statistical Metrics for Indus Script Analysis

This module provides rigorous statistical measures for analyzing co-occurrence patterns,
correlations, and dependencies in symbolic sequences. These are purely statistical
methods without any quantum mechanical claims.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from collections import Counter, defaultdict
import itertools


def pointwise_mutual_information(
    pair_count: int,
    total_count: int,
    symbol_a_count: int,
    symbol_b_count: int
) -> float:
    """
    Calculate Pointwise Mutual Information (PMI) for a symbol pair.
    
    PMI measures the association between two symbols by comparing their
    joint probability to their independent probabilities.
    
    PMI(a,b) = log2(P(a,b) / (P(a) * P(b)))
    
    Args:
        pair_count: Number of times symbols a and b co-occur
        total_count: Total number of observations
        symbol_a_count: Total count of symbol a
        symbol_b_count: Total count of symbol b
    
    Returns:
        PMI value (positive = attraction, negative = repulsion, 0 = independence)
    """
    if pair_count == 0 or symbol_a_count == 0 or symbol_b_count == 0:
        return float('-inf')
    
    p_ab = pair_count / total_count
    p_a = symbol_a_count / total_count
    p_b = symbol_b_count / total_count
    
    return np.log2(p_ab / (p_a * p_b))


def mutual_information(
    sequences: List[List[str]]
) -> Dict[Tuple[str, str], float]:
    """
    Calculate Mutual Information for all symbol pairs in sequences.
    
    MI measures the reduction in uncertainty about one symbol
    when the other is known.
    
    Args:
        sequences: List of symbol sequences
    
    Returns:
        Dictionary mapping symbol pairs to their MI values
    """
    # Count all symbols and pairs
    symbol_counts = Counter()
    pair_counts = Counter()
    total = 0
    
    for seq in sequences:
        for symbol in seq:
            symbol_counts[symbol] += 1
            total += 1
        
        # Count adjacent pairs
        for i in range(len(seq) - 1):
            pair_counts[(seq[i], seq[i+1])] += 1
    
    # Calculate MI for each pair
    mi_scores = {}
    for (a, b), count in pair_counts.items():
        p_ab = count / (total - len(sequences))  # Adjust for sequence boundaries
        p_a = symbol_counts[a] / total
        p_b = symbol_counts[b] / total
        
        if p_ab > 0 and p_a > 0 and p_b > 0:
            mi_scores[(a, b)] = p_ab * np.log2(p_ab / (p_a * p_b))
    
    return mi_scores


def lift_ratio(
    pair_count: int,
    total_count: int,
    symbol_a_count: int,
    symbol_b_count: int
) -> float:
    """
    Calculate lift (odds ratio) for a symbol pair.
    
    Lift measures how much more likely symbols co-occur than expected by chance.
    Lift > 1: positive association
    Lift < 1: negative association
    Lift = 1: independence
    
    Args:
        pair_count: Number of times symbols a and b co-occur
        total_count: Total number of observations
        symbol_a_count: Total count of symbol a
        symbol_b_count: Total count of symbol b
    
    Returns:
        Lift ratio
    """
    if symbol_a_count == 0 or symbol_b_count == 0:
        return 0.0
    
    expected = (symbol_a_count * symbol_b_count) / total_count
    if expected == 0:
        return 0.0
    
    return pair_count / expected


def permutation_test(
    sequences: List[List[str]],
    pair: Tuple[str, str],
    n_permutations: int = 1000,
    random_seed: Optional[int] = None
) -> Tuple[float, float]:
    """
    Perform permutation test to assess if pair co-occurrence is significant.
    
    Tests the null hypothesis that the observed co-occurrence pattern
    could arise from random chance.
    
    Args:
        sequences: List of symbol sequences
        pair: Symbol pair to test (a, b)
        n_permutations: Number of random permutations to generate
        random_seed: Random seed for reproducibility
    
    Returns:
        Tuple of (observed_count, p_value)
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Calculate observed count
    observed = sum(
        sum(1 for i in range(len(seq) - 1) if (seq[i], seq[i+1]) == pair)
        for seq in sequences
    )
    
    # Generate null distribution
    null_counts = []
    for _ in range(n_permutations):
        # Shuffle each sequence independently
        shuffled = [list(seq) for seq in sequences]
        for seq in shuffled:
            np.random.shuffle(seq)
        
        count = sum(
            sum(1 for i in range(len(seq) - 1) if (seq[i], seq[i+1]) == pair)
            for seq in shuffled
        )
        null_counts.append(count)
    
    # Calculate p-value
    p_value = sum(1 for c in null_counts if c >= observed) / n_permutations
    
    return observed, p_value


def positional_dependency(
    sequences: List[List[str]],
    symbol_a: str,
    symbol_b: str,
    max_distance: int = 10
) -> Dict[int, int]:
    """
    Analyze positional dependency between two symbols.
    
    Measures how often symbol b appears at various distances from symbol a.
    This reveals preferred distances and structural constraints.
    
    Args:
        sequences: List of symbol sequences
        symbol_a: First symbol
        symbol_b: Second symbol
        max_distance: Maximum distance to consider
    
    Returns:
        Dictionary mapping distance to occurrence count
    """
    distance_counts = defaultdict(int)
    
    for seq in sequences:
        # Find all positions of symbol_a
        a_positions = [i for i, s in enumerate(seq) if s == symbol_a]
        b_positions = [i for i, s in enumerate(seq) if s == symbol_b]
        
        # Calculate distances
        for a_pos in a_positions:
            for b_pos in b_positions:
                distance = b_pos - a_pos
                if 0 < distance <= max_distance:
                    distance_counts[distance] += 1
    
    return dict(distance_counts)


def site_variance_analysis(
    sequences_by_site: Dict[str, List[List[str]]],
    pair: Tuple[str, str]
) -> Dict[str, Dict[str, float]]:
    """
    Analyze variance of pair co-occurrence across different sites.
    
    Tests whether symbol pair associations are stable across geographical locations,
    which would indicate supra-regional standardization.
    
    Args:
        sequences_by_site: Dictionary mapping site names to sequences
        pair: Symbol pair to analyze
    
    Returns:
        Dictionary with PMI and counts for each site
    """
    results = {}
    
    for site, sequences in sequences_by_site.items():
        # Count symbols and pairs
        symbol_counts = Counter()
        pair_count = 0
        total = 0
        
        for seq in sequences:
            for symbol in seq:
                symbol_counts[symbol] += 1
                total += 1
            
            # Count this specific pair
            for i in range(len(seq) - 1):
                if (seq[i], seq[i+1]) == pair:
                    pair_count += 1
        
        # Calculate PMI for this site
        if total > 0:
            pmi = pointwise_mutual_information(
                pair_count,
                total,
                symbol_counts[pair[0]],
                symbol_counts[pair[1]]
            )
            
            results[site] = {
                'pmi': pmi,
                'pair_count': pair_count,
                'total': total
            }
    
    return results


def homogeneity_test(
    site_results: Dict[str, Dict[str, float]],
    metric: str = 'pmi'
) -> Tuple[float, float]:
    """
    Test homogeneity of a metric across sites.
    
    Uses coefficient of variation to assess stability.
    Low CV indicates stable pattern across sites (supra-regional standardization).
    
    Args:
        site_results: Results from site_variance_analysis
        metric: Which metric to test ('pmi', 'pair_count', etc.)
    
    Returns:
        Tuple of (mean, coefficient_of_variation)
    """
    values = [site[metric] for site in site_results.values() if metric in site]
    
    if not values:
        return 0.0, 0.0
    
    mean = np.mean(values)
    std = np.std(values)
    
    cv = std / mean if mean != 0 else float('inf')
    
    return mean, cv
