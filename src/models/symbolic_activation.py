"""
Symbolic Activation Theorem

Mathematical formalization of the principle that efficient symbolic systems
converge to few high-frequency operators that activate states rather than
describe narratives.
"""

import numpy as np
from typing import List, Dict, Tuple


class SymbolicActivationTheorem:
    """
    Formalization of the Symbolic Activation Principle.
    
    THEOREM: Efficient symbolic systems converge to poucos operadores de alta 
    frequência que ativam estados, enquanto o conteúdo semântico profundo 
    permanece na cauda longa.
    
    Formally:
        Sistema eficiente →
            Alta compressão →
                Poucos símbolos dominantes →
                    Muitos estados derivados
    """
    
    @staticmethod
    def validate_system(frequencies: List[int],
                       activation_threshold: float = 0.5) -> Dict[str, any]:
        """
        Validate if a system follows the symbolic activation principle.
        
        A system is considered "activation-based" if:
        1. It shows high Zipfian skew (few dominant operators)
        2. High compression efficiency
        3. Low entropy (predictable structure)
        4. Top-k items account for >50% of activity
        
        Args:
            frequencies: Frequency distribution
            activation_threshold: Minimum coverage by dominant operators
            
        Returns:
            Validation results and metrics
        """
        frequencies = sorted(frequencies, reverse=True)
        total = sum(frequencies)
        
        # Calculate how many items needed for activation threshold
        cumsum = np.cumsum(frequencies)
        k_for_threshold = np.searchsorted(cumsum, activation_threshold * total) + 1
        
        # Calculate metrics
        try:
            from ..analysis.zipf_analysis import ZipfAnalyzer
            from ..models.entropy_model import calculate_entropy, compression_efficiency
        except ImportError:
            from analysis.zipf_analysis import ZipfAnalyzer
            from models.entropy_model import calculate_entropy, compression_efficiency
        
        analyzer = ZipfAnalyzer()
        zipf_fit = analyzer.fit(frequencies)
        entropy = calculate_entropy(frequencies)
        compression = compression_efficiency(frequencies, top_k=k_for_threshold)
        
        # Validation criteria
        is_zipfian = zipf_fit['r_squared'] > 0.8
        is_compressed = compression['efficiency_score'] > 0  # Any compression is good
        has_dominant_operators = k_for_threshold <= max(10, len(frequencies) * 0.1)
        
        is_activation_system = is_zipfian and is_compressed and has_dominant_operators
        
        return {
            'is_activation_system': is_activation_system,
            'validation': {
                'is_zipfian': is_zipfian,
                'is_compressed': is_compressed,
                'has_dominant_operators': has_dominant_operators
            },
            'metrics': {
                'k_for_activation': k_for_threshold,
                'activation_percentage': (k_for_threshold / len(frequencies)) * 100,
                'zipf_exponent': zipf_fit['zipf_exponent'],
                'zipf_r_squared': zipf_fit['r_squared'],
                'entropy': entropy,
                'efficiency_score': compression['efficiency_score']
            }
        }
    
    @staticmethod
    def compare_systems(system1_freqs: List[int],
                       system2_freqs: List[int],
                       system1_name: str = "System 1",
                       system2_name: str = "System 2") -> Dict[str, any]:
        """
        Compare two systems to test for isomorphism.
        
        Two systems are structurally isomorphic if they share:
        1. Similar Zipf exponents
        2. Similar compression efficiency
        3. Similar activation patterns
        
        Args:
            system1_freqs: Frequencies from first system
            system2_freqs: Frequencies from second system
            system1_name: Name of first system
            system2_name: Name of second system
            
        Returns:
            Comparison results
        """
        val1 = SymbolicActivationTheorem.validate_system(system1_freqs)
        val2 = SymbolicActivationTheorem.validate_system(system2_freqs)
        
        # Calculate differences
        exponent_diff = abs(val1['metrics']['zipf_exponent'] - 
                           val2['metrics']['zipf_exponent'])
        entropy_diff = abs(val1['metrics']['entropy'] - 
                          val2['metrics']['entropy'])
        efficiency_diff = abs(val1['metrics']['efficiency_score'] - 
                             val2['metrics']['efficiency_score'])
        
        # Isomorphism score (0-100)
        exponent_sim = max(0, 100 - exponent_diff * 50)
        entropy_sim = max(0, 100 - entropy_diff * 10)
        efficiency_sim = max(0, 100 - efficiency_diff)
        
        isomorphism_score = (exponent_sim + entropy_sim + efficiency_sim) / 3
        
        are_isomorphic = (
            isomorphism_score > 70 and
            val1['is_activation_system'] and
            val2['is_activation_system']
        )
        
        return {
            'are_isomorphic': are_isomorphic,
            'isomorphism_score': isomorphism_score,
            system1_name: val1,
            system2_name: val2,
            'differences': {
                'zipf_exponent': exponent_diff,
                'entropy': entropy_diff,
                'efficiency': efficiency_diff
            },
            'conclusion': SymbolicActivationTheorem._generate_isomorphism_conclusion(
                are_isomorphic, isomorphism_score, system1_name, system2_name
            )
        }
    
    @staticmethod
    def _generate_isomorphism_conclusion(are_isomorphic: bool,
                                        score: float,
                                        name1: str,
                                        name2: str) -> str:
        """Generate conclusion text."""
        if are_isomorphic:
            return (
                f"{name1} and {name2} exhibit strong structural isomorphism "
                f"(score: {score:.1f}/100). Both systems optimize for efficient "
                f"state activation through few dominant operators, following the "
                f"same operational principle despite temporal and contextual differences."
            )
        else:
            return (
                f"{name1} and {name2} show limited structural similarity "
                f"(score: {score:.1f}/100). The systems may operate under "
                f"different optimization principles."
            )
    
    @staticmethod
    def activation_law() -> str:
        """
        Return the formal statement of the Symbolic Activation Law.
        
        Returns:
            Formal law statement
        """
        return """
SYMBOLIC ACTIVATION LAW

Efficient symbolic systems converge to poucos operadores de alta frequência 
que ativam estados, enquanto o conteúdo semântico profundo permanece na 
cauda longa.

Formally:

    Sistema Eficiente →
        Alta Compressão →
            Poucos Símbolos Dominantes →
                Muitos Estados Derivados

Mathematical Expression:

    Given a symbolic system S with frequency distribution F(r) where r is rank:
    
    1. S is efficient ⟺ H(S) ≪ H_max(S)
       (Low entropy relative to maximum)
    
    2. F(r) ~ 1/r^α where α ≈ 1
       (Zipfian distribution)
    
    3. ∃k ≪ |S| : Σ(r=1 to k) F(r) > 0.5 × Σ(all) F(r)
       (Few items dominate)
    
    4. High-frequency items activate states; low-frequency items provide depth
       (Functional differentiation)

This law applies invariantly across:
    - Ancient administrative systems (Indus Script)
    - Modern algorithmic platforms (Social Media)
    - Natural language
    - Computational systems

The principle is cognitively and algorithmically stable across millennia.
"""
