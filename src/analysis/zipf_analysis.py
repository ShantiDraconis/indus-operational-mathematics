"""
Zipf Distribution Analyzer

Analyzes frequency distributions and tests for Zipfian patterns
in symbolic systems (both ancient scripts and modern content).
"""

import numpy as np
from scipy import stats
from typing import List, Tuple, Dict


class ZipfAnalyzer:
    """
    Analyzes whether a frequency distribution follows Zipf's law.
    
    Zipf's law states that the frequency of an item is inversely proportional
    to its rank: f(r) ∝ 1/r^α, where α is the Zipf exponent.
    """
    
    def __init__(self):
        self.frequencies = None
        self.ranks = None
        self.zipf_exponent = None
        
    def fit(self, frequencies: List[int]) -> Dict[str, float]:
        """
        Fit Zipf distribution to observed frequencies.
        
        Args:
            frequencies: List of frequencies (should be sorted in descending order)
            
        Returns:
            Dictionary with statistics including Zipf exponent, R², and p-value
        """
        # Sort frequencies in descending order
        self.frequencies = np.array(sorted(frequencies, reverse=True))
        self.ranks = np.arange(1, len(self.frequencies) + 1)
        
        # Filter out zero frequencies for log-log analysis
        mask = self.frequencies > 0
        log_ranks = np.log(self.ranks[mask])
        log_freqs = np.log(self.frequencies[mask])
        
        # Perform linear regression on log-log scale
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_ranks, log_freqs)
        
        self.zipf_exponent = -slope  # Zipf exponent is negative of the slope
        
        return {
            'zipf_exponent': self.zipf_exponent,
            'r_squared': r_value ** 2,
            'p_value': p_value,
            'intercept': intercept,
            'std_error': std_err
        }
    
    def get_top_k_concentration(self, k: int = 10) -> float:
        """
        Calculate what percentage of total frequency is concentrated in top k items.
        
        This measures the dominance of high-frequency operators.
        
        Args:
            k: Number of top items to consider
            
        Returns:
            Percentage (0-100) of total frequency in top k items
        """
        if self.frequencies is None:
            raise ValueError("Must call fit() before get_top_k_concentration()")
            
        total = np.sum(self.frequencies)
        top_k_sum = np.sum(self.frequencies[:k])
        return (top_k_sum / total) * 100
    
    def classify_distribution(self) -> Tuple[str, str, str]:
        """
        Classify items into Class A (dominant), B (medium), and C (long tail).
        
        Based on the Harappan analysis:
        - Class A: Top ~10 items that dominate
        - Class B: Middle ~30-50 items with moderate performance
        - Class C: Long tail with low individual performance
        
        Returns:
            Tuple of (class_a_range, class_b_range, class_c_range) as strings
        """
        if self.frequencies is None:
            raise ValueError("Must call fit() before classify_distribution()")
            
        n = len(self.frequencies)
        
        # Class A: Top 10 or top 10%
        class_a_end = min(10, max(1, n // 10))
        
        # Class B: Next 30-50 items or next 30%
        class_b_end = min(class_a_end + 50, class_a_end + n // 3)
        
        return (
            f"Class A: ranks 1-{class_a_end} (dominant operators)",
            f"Class B: ranks {class_a_end+1}-{class_b_end} (stable medium)",
            f"Class C: ranks {class_b_end+1}-{n} (long tail)"
        )
    
    def calculate_entropy(self) -> float:
        """
        Calculate Shannon entropy of the distribution.
        
        Lower entropy indicates higher compression efficiency.
        
        Returns:
            Shannon entropy in bits
        """
        if self.frequencies is None:
            raise ValueError("Must call fit() before calculate_entropy()")
            
        # Normalize to probabilities
        probabilities = self.frequencies / np.sum(self.frequencies)
        
        # Filter out zeros
        probabilities = probabilities[probabilities > 0]
        
        # Calculate entropy
        entropy = -np.sum(probabilities * np.log2(probabilities))
        
        return entropy
    
    def get_summary_statistics(self) -> Dict[str, any]:
        """
        Get comprehensive summary statistics of the distribution.
        
        Returns:
            Dictionary with various distribution statistics
        """
        if self.frequencies is None:
            raise ValueError("Must call fit() before get_summary_statistics()")
            
        return {
            'total_items': len(self.frequencies),
            'total_frequency': np.sum(self.frequencies),
            'max_frequency': np.max(self.frequencies),
            'min_frequency': np.min(self.frequencies),
            'mean_frequency': np.mean(self.frequencies),
            'median_frequency': np.median(self.frequencies),
            'std_frequency': np.std(self.frequencies),
            'top_10_concentration': self.get_top_k_concentration(10),
            'entropy': self.calculate_entropy(),
            'zipf_exponent': self.zipf_exponent
        }
