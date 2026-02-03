"""
Frequency Analyzer

Analyzes symbol/content frequency patterns and categorizes by frequency classes.
"""

import numpy as np
from typing import List, Dict, Tuple
from collections import Counter


class FrequencyAnalyzer:
    """
    Analyzes frequency patterns in symbolic systems.
    
    This class handles the analysis of both ancient symbols (Harappa)
    and modern content (YouTube videos) using the same framework.
    """
    
    def __init__(self, data: Dict[str, int]):
        """
        Initialize analyzer with frequency data.
        
        Args:
            data: Dictionary mapping symbols/items to their frequencies
        """
        self.data = data
        self.sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
    def get_frequencies(self) -> List[int]:
        """Get list of frequencies in descending order."""
        return [freq for _, freq in self.sorted_items]
    
    def get_items(self) -> List[str]:
        """Get list of items sorted by frequency."""
        return [item for item, _ in self.sorted_items]
    
    def identify_dominant_operators(self, threshold: float = 0.5) -> List[Tuple[str, int]]:
        """
        Identify dominant operators (Class A items).
        
        Dominant operators are items that together account for a significant
        portion of total frequency (default: 50%).
        
        Args:
            threshold: Cumulative frequency threshold (0.0 to 1.0)
            
        Returns:
            List of (item, frequency) tuples for dominant operators
        """
        total_freq = sum(self.data.values())
        cumulative = 0
        dominant = []
        
        for item, freq in self.sorted_items:
            cumulative += freq
            dominant.append((item, freq))
            if cumulative / total_freq >= threshold:
                break
                
        return dominant
    
    def analyze_modifier_patterns(self, modifiers: List[str], 
                                  items: List[str]) -> Dict[str, Dict]:
        """
        Analyze which modifiers work with which base items (strong typing).
        
        This implements the "barras e aspas" (bars and quotes) rule:
        certain modifiers only work with certain content types.
        
        Args:
            modifiers: List of modifier symbols/keywords
            items: List of base items to check against
            
        Returns:
            Dictionary mapping each modifier to compatible items and statistics
        """
        results = {}
        
        for modifier in modifiers:
            compatible = []
            incompatible = []
            
            for item in items:
                # Check if modifier appears with item
                combined_key = f"{modifier}_{item}"
                if combined_key in self.data or modifier in item:
                    compatible.append(item)
                else:
                    incompatible.append(item)
            
            results[modifier] = {
                'compatible': compatible,
                'incompatible': incompatible,
                'compatibility_rate': len(compatible) / len(items) if items else 0
            }
            
        return results
    
    def measure_non_locality(self, item: str, contexts: List[str]) -> Dict[str, any]:
        """
        Measure non-locality of a symbol/item across different contexts.
        
        Non-locality means the same pattern activates consistently across
        different populations/contexts without translation or deep cultural context.
        
        Args:
            item: The symbol/item to analyze
            contexts: List of different contexts (e.g., geographic regions)
            
        Returns:
            Dictionary with non-locality metrics
        """
        # For this implementation, we assume context-specific data
        # would be provided in the format: "item_context"
        
        context_frequencies = {}
        for context in contexts:
            key = f"{item}_{context}"
            context_frequencies[context] = self.data.get(key, 0)
        
        if not context_frequencies:
            return {'non_local': False, 'variance': None}
        
        # Calculate coefficient of variation
        freqs = list(context_frequencies.values())
        mean = np.mean(freqs)
        std = np.std(freqs)
        cv = std / mean if mean > 0 else float('inf')
        
        # Low CV indicates invariance (non-locality)
        return {
            'non_local': cv < 0.5,  # Threshold for considering non-local
            'coefficient_variation': cv,
            'context_frequencies': context_frequencies,
            'mean_frequency': mean,
            'std_frequency': std
        }
    
    def compare_symbol_classes(self, class_a_size: int = 10,
                               class_b_size: int = 40) -> Dict[str, Dict]:
        """
        Compare characteristics of different frequency classes.
        
        Args:
            class_a_size: Number of items in Class A (dominant)
            class_b_size: Number of items in Class B (medium)
            
        Returns:
            Dictionary with statistics for each class
        """
        total = sum(self.data.values())
        
        class_a = self.sorted_items[:class_a_size]
        class_b = self.sorted_items[class_a_size:class_a_size + class_b_size]
        class_c = self.sorted_items[class_a_size + class_b_size:]
        
        def class_stats(items):
            if not items:
                return {'count': 0, 'total_freq': 0, 'percentage': 0}
            freqs = [f for _, f in items]
            total_freq = sum(freqs)
            return {
                'count': len(items),
                'total_freq': total_freq,
                'percentage': (total_freq / total) * 100,
                'mean_freq': np.mean(freqs),
                'max_freq': max(freqs),
                'min_freq': min(freqs)
            }
        
        return {
            'class_a': class_stats(class_a),
            'class_b': class_stats(class_b),
            'class_c': class_stats(class_c),
            'total_frequency': total
        }
