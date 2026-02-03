"""
Comparative Distribution Analysis

Compares frequency distributions between ancient (Harappa) and modern (YouTube) systems.
"""

import numpy as np
from scipy import stats
from typing import Dict, List, Tuple
from .zipf_analysis import ZipfAnalyzer


def compare_distributions(harappa_data: Dict[str, int], 
                          youtube_data: Dict[str, int]) -> Dict[str, any]:
    """
    Compare statistical signatures between Harappa and YouTube distributions.
    
    This function tests the core hypothesis: both systems exhibit the same
    statistical patterns (Zipfian distribution, high compression, etc.)
    
    Args:
        harappa_data: Dictionary of Harappa symbol frequencies
        youtube_data: Dictionary of YouTube content frequencies
        
    Returns:
        Comprehensive comparison results
    """
    # Create analyzers for both datasets
    harappa_analyzer = ZipfAnalyzer()
    youtube_analyzer = ZipfAnalyzer()
    
    # Extract frequencies
    harappa_freqs = sorted(harappa_data.values(), reverse=True)
    youtube_freqs = sorted(youtube_data.values(), reverse=True)
    
    # Fit Zipf distributions
    harappa_fit = harappa_analyzer.fit(harappa_freqs)
    youtube_fit = youtube_analyzer.fit(youtube_freqs)
    
    # Get summary statistics
    harappa_stats = harappa_analyzer.get_summary_statistics()
    youtube_stats = youtube_analyzer.get_summary_statistics()
    
    # Calculate similarity metrics
    exponent_diff = abs(harappa_fit['zipf_exponent'] - youtube_fit['zipf_exponent'])
    entropy_diff = abs(harappa_stats['entropy'] - youtube_stats['entropy'])
    
    # Test if distributions are significantly different
    # Using Kolmogorov-Smirnov test
    ks_statistic, ks_pvalue = stats.ks_2samp(
        np.array(harappa_freqs) / sum(harappa_freqs),
        np.array(youtube_freqs) / sum(youtube_freqs)
    )
    
    # Structural isomorphism score (0-100)
    # Based on similarity of Zipf exponent, entropy, and top-k concentration
    exponent_similarity = 100 * (1 - min(exponent_diff / 2, 1))
    entropy_similarity = 100 * (1 - min(entropy_diff / 10, 1))
    concentration_similarity = 100 * (1 - abs(
        harappa_stats['top_10_concentration'] - 
        youtube_stats['top_10_concentration']
    ) / 100)
    
    isomorphism_score = (exponent_similarity + entropy_similarity + 
                         concentration_similarity) / 3
    
    return {
        'harappa': {
            'zipf_fit': harappa_fit,
            'statistics': harappa_stats,
            'classification': harappa_analyzer.classify_distribution()
        },
        'youtube': {
            'zipf_fit': youtube_fit,
            'statistics': youtube_stats,
            'classification': youtube_analyzer.classify_distribution()
        },
        'comparison': {
            'zipf_exponent_diff': exponent_diff,
            'entropy_diff': entropy_diff,
            'ks_statistic': ks_statistic,
            'ks_pvalue': ks_pvalue,
            'isomorphism_score': isomorphism_score,
            'structural_similarity': isomorphism_score > 70,
            'conclusion': _generate_conclusion(isomorphism_score, exponent_diff)
        }
    }


def _generate_conclusion(isomorphism_score: float, exponent_diff: float) -> str:
    """
    Generate textual conclusion based on comparison metrics.
    
    Args:
        isomorphism_score: Overall similarity score (0-100)
        exponent_diff: Difference in Zipf exponents
        
    Returns:
        Textual conclusion
    """
    if isomorphism_score > 80 and exponent_diff < 0.2:
        return (
            "Strong structural isomorphism detected. Both systems exhibit "
            "nearly identical Zipfian distributions, suggesting the same "
            "operational principle: efficient state activation through "
            "few dominant operators."
        )
    elif isomorphism_score > 60:
        return (
            "Moderate structural similarity detected. Both systems show "
            "Zipfian patterns with comparable compression efficiency, "
            "supporting the hypothesis of convergent optimization."
        )
    else:
        return (
            "Limited structural similarity. Distributions differ significantly, "
            "suggesting different underlying operational principles."
        )


def analyze_operator_efficiency(data: Dict[str, int], 
                                top_k: int = 10) -> Dict[str, any]:
    """
    Analyze the efficiency of top-k operators in a system.
    
    This measures how well the system compresses information into
    few high-frequency operators (the "activation" principle).
    
    Args:
        data: Frequency data
        top_k: Number of top operators to analyze
        
    Returns:
        Efficiency metrics
    """
    frequencies = sorted(data.values(), reverse=True)
    total = sum(frequencies)
    
    top_k_sum = sum(frequencies[:top_k])
    top_k_percentage = (top_k_sum / total) * 100
    
    # Compression ratio: how much content is handled by top-k items
    compression_ratio = len(frequencies) / top_k
    
    # Efficiency score: high when few items do most work
    efficiency_score = top_k_percentage * np.log(compression_ratio)
    
    return {
        'top_k': top_k,
        'top_k_coverage': top_k_percentage,
        'compression_ratio': compression_ratio,
        'efficiency_score': efficiency_score,
        'interpretation': (
            f"Top {top_k} operators handle {top_k_percentage:.1f}% of total "
            f"activity, with {compression_ratio:.1f}:1 compression ratio."
        )
    }
