"""
Entropy and Compression Models

Mathematical formalization of information-theoretic properties
of symbolic systems.
"""

import numpy as np
from typing import List, Dict


def calculate_entropy(frequencies: List[int]) -> float:
    """
    Calculate Shannon entropy of a frequency distribution.
    
    H(X) = -Σ p(x) log₂ p(x)
    
    Lower entropy indicates higher compression efficiency and
    more predictable/structured information flow.
    
    Args:
        frequencies: List of frequencies
        
    Returns:
        Shannon entropy in bits
    """
    frequencies = np.array(frequencies)
    total = np.sum(frequencies)
    
    if total == 0:
        return 0.0
    
    # Convert to probabilities
    probabilities = frequencies / total
    
    # Filter out zeros (0 * log(0) = 0 by convention)
    probabilities = probabilities[probabilities > 0]
    
    # Calculate entropy
    entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return float(entropy)


def compression_efficiency(frequencies: List[int], 
                          top_k: int = 10) -> Dict[str, float]:
    """
    Calculate compression efficiency metrics.
    
    Systems that compress well use few symbols to represent much information.
    
    Args:
        frequencies: List of frequencies (sorted descending)
        top_k: Number of top items to analyze
        
    Returns:
        Dictionary with compression metrics
    """
    frequencies = sorted(frequencies, reverse=True)
    total = sum(frequencies)
    
    if total == 0:
        return {
            'compression_ratio': 0,
            'top_k_coverage': 0,
            'efficiency_score': 0
        }
    
    # Top-k coverage: percentage of total handled by top-k items
    top_k_sum = sum(frequencies[:top_k])
    top_k_coverage = (top_k_sum / total) * 100
    
    # Compression ratio: total items / top-k items
    compression_ratio = len(frequencies) / top_k
    
    # Efficiency score: combines coverage and compression
    # High score means few items do most work
    entropy = calculate_entropy(frequencies)
    max_entropy = np.log2(len(frequencies))  # Maximum possible entropy
    
    # Normalized efficiency (0-100)
    efficiency_score = (1 - entropy / max_entropy) * 100 if max_entropy > 0 else 0
    
    return {
        'compression_ratio': compression_ratio,
        'top_k_coverage': top_k_coverage,
        'efficiency_score': efficiency_score,
        'entropy': entropy,
        'max_entropy': max_entropy,
        'normalized_entropy': entropy / max_entropy if max_entropy > 0 else 0
    }


def calculate_redundancy(frequencies: List[int]) -> float:
    """
    Calculate redundancy in the system.
    
    Redundancy = 1 - (H / H_max)
    
    High redundancy means the system is highly predictable and compressed.
    
    Args:
        frequencies: List of frequencies
        
    Returns:
        Redundancy (0-1)
    """
    n = len(frequencies)
    if n <= 1:
        return 0.0
    
    entropy = calculate_entropy(frequencies)
    max_entropy = np.log2(n)
    
    redundancy = 1 - (entropy / max_entropy) if max_entropy > 0 else 0
    
    return float(redundancy)


def mutual_information(joint_frequencies: Dict[tuple, int],
                      marginal_x: Dict[str, int],
                      marginal_y: Dict[str, int]) -> float:
    """
    Calculate mutual information between two variables.
    
    I(X;Y) = H(X) + H(Y) - H(X,Y)
    
    Measures how much knowing one variable reduces uncertainty about the other.
    Useful for analyzing modifier-base relationships.
    
    Args:
        joint_frequencies: Joint frequency distribution {(x,y): count}
        marginal_x: Marginal frequencies for X
        marginal_y: Marginal frequencies for Y
        
    Returns:
        Mutual information in bits
    """
    # Calculate entropies
    h_x = calculate_entropy(list(marginal_x.values()))
    h_y = calculate_entropy(list(marginal_y.values()))
    h_xy = calculate_entropy(list(joint_frequencies.values()))
    
    # Mutual information
    mi = h_x + h_y - h_xy
    
    return float(mi)


def zipf_mandelbrot_fit(frequencies: List[int]) -> Dict[str, float]:
    """
    Fit Zipf-Mandelbrot distribution.
    
    f(r) = C / (r + β)^α
    
    This is a generalization of Zipf's law with an offset parameter β.
    
    Args:
        frequencies: List of frequencies (sorted descending)
        
    Returns:
        Dictionary with fitted parameters
    """
    from scipy.optimize import curve_fit
    
    frequencies = np.array(sorted(frequencies, reverse=True))
    ranks = np.arange(1, len(frequencies) + 1)
    
    # Define Zipf-Mandelbrot function
    def zipf_mandelbrot(r, C, alpha, beta):
        return C / np.power(r + beta, alpha)
    
    try:
        # Fit the model
        popt, pcov = curve_fit(
            zipf_mandelbrot, 
            ranks, 
            frequencies,
            p0=[frequencies[0], 1.0, 0.0],  # Initial guess
            maxfev=10000
        )
        
        C, alpha, beta = popt
        
        # Calculate R²
        predicted = zipf_mandelbrot(ranks, C, alpha, beta)
        ss_res = np.sum((frequencies - predicted) ** 2)
        ss_tot = np.sum((frequencies - np.mean(frequencies)) ** 2)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        return {
            'C': C,
            'alpha': alpha,
            'beta': beta,
            'r_squared': r_squared
        }
    except:
        # If fitting fails, return simple Zipf parameters
        return {
            'C': frequencies[0],
            'alpha': 1.0,
            'beta': 0.0,
            'r_squared': 0.0
        }
