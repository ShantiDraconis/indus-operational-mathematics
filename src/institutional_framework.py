"""
Institutional Framework Models

Models for distinguishing administrative vs ritual/symbolic regimes in Indus sequences.
Implements mixture models to classify sequences based on their structural properties.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from collections import Counter
from dataclasses import dataclass


@dataclass
class RegimeCharacteristics:
    """Characteristics that distinguish different institutional regimes."""
    has_closer: bool
    has_pictogram: bool
    sequence_length: int
    repetition_score: float
    object_type: Optional[str] = None


class InstitutionalRegimeClassifier:
    """
    Classifier for identifying administrative vs ritual regimes.
    
    Based on the mixture model:
    P(sequence) = π_A * P_A(sequence) + π_B * P_B(sequence)
    
    Where:
    - Regime A: Administrative (high repetition, stable closers, less pictographic)
    - Regime B: Ritual/Symbolic (more pictograms, animals, symbolic composition)
    """
    
    def __init__(
        self,
        pictogram_symbols: Optional[set] = None,
        closer_symbols: Optional[set] = None
    ):
        """
        Initialize classifier.
        
        Args:
            pictogram_symbols: Set of symbols considered pictographic (animals, etc.)
            closer_symbols: Set of symbols that commonly close sequences
        """
        self.pictogram_symbols = pictogram_symbols or set()
        self.closer_symbols = closer_symbols or set()
        
        # Model parameters (can be learned from data)
        self.pi_A = 0.5  # Prior for administrative
        self.pi_B = 0.5  # Prior for ritual
    
    def extract_features(
        self,
        sequence: List[str],
        object_type: Optional[str] = None
    ) -> RegimeCharacteristics:
        """
        Extract features from a sequence for classification.
        
        Args:
            sequence: Symbol sequence
            object_type: Type of object (seal, tablet, pottery, etc.)
        
        Returns:
            RegimeCharacteristics object
        """
        # Check for closer
        has_closer = len(sequence) > 0 and sequence[-1] in self.closer_symbols
        
        # Check for pictograms
        has_pictogram = any(s in self.pictogram_symbols for s in sequence)
        
        # Calculate repetition score
        if len(sequence) > 0:
            symbol_counts = Counter(sequence)
            max_count = max(symbol_counts.values())
            repetition_score = max_count / len(sequence)
        else:
            repetition_score = 0.0
        
        return RegimeCharacteristics(
            has_closer=has_closer,
            has_pictogram=has_pictogram,
            sequence_length=len(sequence),
            repetition_score=repetition_score,
            object_type=object_type
        )
    
    def classify(
        self,
        sequence: List[str],
        object_type: Optional[str] = None
    ) -> Tuple[str, float]:
        """
        Classify a sequence as administrative or ritual.
        
        Args:
            sequence: Symbol sequence
            object_type: Optional object type
        
        Returns:
            Tuple of (regime, confidence)
            regime: 'administrative' or 'ritual'
            confidence: probability score
        """
        features = self.extract_features(sequence, object_type)
        
        # Simple heuristic classifier
        # (In practice, this would be learned from labeled data)
        admin_score = 0.0
        ritual_score = 0.0
        
        # Administrative indicators
        if features.has_closer:
            admin_score += 0.3
        if features.repetition_score > 0.3:
            admin_score += 0.2
        if features.sequence_length < 5:
            admin_score += 0.1
        if features.object_type in ['seal', 'tablet']:
            admin_score += 0.2
        
        # Ritual indicators
        if features.has_pictogram:
            ritual_score += 0.4
        if features.sequence_length > 7:
            ritual_score += 0.2
        if features.object_type in ['pottery', 'amulet']:
            ritual_score += 0.1
        
        # Normalize
        total = admin_score + ritual_score
        if total > 0:
            admin_prob = admin_score / total
            ritual_prob = ritual_score / total
        else:
            admin_prob = 0.5
            ritual_prob = 0.5
        
        if admin_prob > ritual_prob:
            return 'administrative', admin_prob
        else:
            return 'ritual', ritual_prob
    
    def batch_classify(
        self,
        sequences: List[List[str]],
        object_types: Optional[List[str]] = None
    ) -> List[Tuple[str, float]]:
        """
        Classify multiple sequences.
        
        Args:
            sequences: List of symbol sequences
            object_types: Optional list of object types
        
        Returns:
            List of (regime, confidence) tuples
        """
        if object_types is None:
            object_types = [None] * len(sequences)
        
        return [
            self.classify(seq, obj_type)
            for seq, obj_type in zip(sequences, object_types)
        ]
    
    def regime_statistics(
        self,
        sequences: List[List[str]],
        object_types: Optional[List[str]] = None
    ) -> Dict[str, Dict[str, float]]:
        """
        Calculate statistics for each regime.
        
        Args:
            sequences: List of symbol sequences
            object_types: Optional list of object types
        
        Returns:
            Dictionary with statistics for each regime
        """
        classifications = self.batch_classify(sequences, object_types)
        
        admin_features = []
        ritual_features = []
        
        for seq, (regime, _) in zip(sequences, classifications):
            features = self.extract_features(seq)
            if regime == 'administrative':
                admin_features.append(features)
            else:
                ritual_features.append(features)
        
        stats = {}
        
        for regime, features_list in [('administrative', admin_features), ('ritual', ritual_features)]:
            if not features_list:
                continue
            
            stats[regime] = {
                'count': len(features_list),
                'avg_length': np.mean([f.sequence_length for f in features_list]),
                'avg_repetition': np.mean([f.repetition_score for f in features_list]),
                'closer_frequency': sum(f.has_closer for f in features_list) / len(features_list),
                'pictogram_frequency': sum(f.has_pictogram for f in features_list) / len(features_list)
            }
        
        return stats


def mixture_model_probability(
    sequence: List[str],
    pi_A: float,
    pi_B: float,
    classifier: InstitutionalRegimeClassifier
) -> Dict[str, float]:
    """
    Calculate probability of sequence under mixture model.
    
    P(sequence) = π_A * P_A(sequence) + π_B * P_B(sequence)
    
    Args:
        sequence: Symbol sequence
        pi_A: Prior probability of administrative regime
        pi_B: Prior probability of ritual regime
        classifier: Trained classifier
    
    Returns:
        Dictionary with probabilities
    """
    regime, confidence = classifier.classify(sequence)
    
    if regime == 'administrative':
        p_A = confidence
        p_B = 1 - confidence
    else:
        p_A = 1 - confidence
        p_B = confidence
    
    p_sequence = pi_A * p_A + pi_B * p_B
    
    return {
        'p_sequence': p_sequence,
        'p_A': p_A,
        'p_B': p_B,
        'posterior_A': (pi_A * p_A) / p_sequence if p_sequence > 0 else 0.5,
        'posterior_B': (pi_B * p_B) / p_sequence if p_sequence > 0 else 0.5
    }
