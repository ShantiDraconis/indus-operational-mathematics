"""
Tensor Network Models for Indus Script Analysis

This module implements tensor network techniques for modeling long-range
correlations in Indus script sequences.

IMPORTANT: These are MATHEMATICAL tensor networks (graphical models), 
NOT quantum tensor networks. We use them to model classical correlations.
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass
import tensorly as tl
from tensorly.decomposition import parafac, tucker


@dataclass
class TensorNetworkModel:
    """
    Tensor network representation of Indus script correlations
    
    This is a GRAPHICAL MODEL using tensor factorization,
    NOT a quantum tensor network.
    """
    
    def __init__(self, max_symbol_id: int, max_sequence_length: int):
        self.max_symbol_id = max_symbol_id
        self.max_sequence_length = max_sequence_length
        
        # 3-way tensor: (sequence_position, symbol, context)
        self.correlation_tensor = None
    
    def build_correlation_tensor(self, sequences: List[List[int]]) -> np.ndarray:
        """
        Build 3-way correlation tensor from sequences
        
        Dimensions:
        - Axis 0: Position in sequence
        - Axis 1: Symbol identity
        - Axis 2: Context (previous symbol)
        
        Returns:
            np.ndarray: The correlation tensor
        """
        shape = (self.max_sequence_length, self.max_symbol_id, self.max_symbol_id)
        tensor = np.zeros(shape)
        
        for seq in sequences:
            for i, symbol in enumerate(seq):
                if i >= self.max_sequence_length:
                    break
                
                # Context is previous symbol (or 0 if first)
                context = seq[i-1] if i > 0 else 0
                
                if symbol < self.max_symbol_id and context < self.max_symbol_id:
                    tensor[i, symbol, context] += 1
        
        # Normalize
        total = tensor.sum()
        if total > 0:
            tensor = tensor / total
        
        self.correlation_tensor = tensor
        return tensor
    
    def factorize_parafac(self, rank: int = 5) -> Tuple:
        """
        PARAFAC/CP decomposition of correlation tensor
        
        This finds latent factors (like "topics" or "states") that
        explain the correlation structure.
        
        Args:
            rank: Number of latent factors
            
        Returns:
            Tuple of factor matrices
        """
        if self.correlation_tensor is None:
            raise ValueError("Must build tensor first")
        
        factors = parafac(self.correlation_tensor, rank=rank)
        return factors
    
    def factorize_tucker(self, ranks: Tuple[int, int, int] = (5, 10, 10)) -> Tuple:
        """
        Tucker decomposition of correlation tensor
        
        More flexible than PARAFAC, allows different ranks per mode.
        
        Args:
            ranks: Tuple of ranks for each mode
            
        Returns:
            Core tensor and factor matrices
        """
        if self.correlation_tensor is None:
            raise ValueError("Must build tensor first")
        
        core, factors = tucker(self.correlation_tensor, ranks=ranks)
        return core, factors
    
    def predict_next_symbol(self, sequence: List[int], position: int, context: int) -> np.ndarray:
        """
        Predict symbol distribution at given position
        
        Uses tensor to model position-symbol-context correlations
        
        Returns:
            np.ndarray: Probability distribution over symbols
        """
        if self.correlation_tensor is None:
            raise ValueError("Must build tensor first")
        
        if position >= self.max_sequence_length:
            position = self.max_sequence_length - 1
        
        if context >= self.max_symbol_id:
            context = 0
        
        # Extract slice from tensor
        probs = self.correlation_tensor[position, :, context]
        
        # Normalize to probability distribution
        total = probs.sum()
        if total > 0:
            probs = probs / total
        else:
            # Uniform distribution if no data
            probs = np.ones(self.max_symbol_id) / self.max_symbol_id
        
        return probs
    
    def compute_long_range_correlation(self, symbol1: int, symbol2: int, distance: int) -> float:
        """
        Compute long-range correlation between symbols at given distance
        
        This measures "non-local" correlation in the STATISTICAL sense
        (correlation at a distance), NOT quantum non-locality.
        
        Returns:
            float: Correlation strength
        """
        if self.correlation_tensor is None:
            raise ValueError("Must build tensor first")
        
        if distance >= self.max_sequence_length:
            return 0.0
        
        # Marginal probabilities
        p1 = self.correlation_tensor[:, symbol1, :].sum()
        p2 = self.correlation_tensor[:, symbol2, :].sum()
        
        if p1 == 0 or p2 == 0:
            return 0.0
        
        # Joint at distance
        joint = 0.0
        for pos in range(self.max_sequence_length - distance):
            if pos + distance < self.max_sequence_length:
                # Approximate joint by looking at position correlation
                joint += self.correlation_tensor[pos, symbol1, :].sum() * \
                         self.correlation_tensor[pos + distance, symbol2, :].sum()
        
        # PMI-like measure
        expected = p1 * p2
        if expected > 0:
            return joint / expected - 1.0
        return 0.0


class MatrixProductState:
    """
    Matrix Product State (MPS) representation
    
    This is a tensor network technique from quantum physics, but here
    used as a CLASSICAL MODEL for sequence compression and generation.
    
    NO quantum mechanical claims are made.
    """
    
    def __init__(self, symbol_dim: int, bond_dim: int):
        """
        Initialize MPS
        
        Args:
            symbol_dim: Number of possible symbols
            bond_dim: Internal bond dimension (controls model complexity)
        """
        self.symbol_dim = symbol_dim
        self.bond_dim = bond_dim
        self.tensors = []
    
    def train(self, sequences: List[List[int]], max_length: int):
        """
        Train MPS on sequences
        
        Uses SVD-based compression to find efficient representation
        """
        # Build full tensor
        shape = tuple([self.symbol_dim] * max_length)
        full_tensor = np.zeros(shape)
        
        for seq in sequences:
            if len(seq) == max_length:
                # Use sequence as index
                idx = tuple(seq)
                full_tensor[idx] += 1
        
        # Normalize
        total = full_tensor.sum()
        if total > 0:
            full_tensor = full_tensor / total
        
        # Convert to MPS using successive SVDs
        self.tensors = []
        remaining = full_tensor
        
        for i in range(max_length - 1):
            # Reshape for SVD
            shape = remaining.shape
            left_dim = shape[0]
            right_dim = np.prod(shape[1:])
            
            matrix = remaining.reshape(left_dim, right_dim)
            
            # SVD with truncation
            U, S, Vh = np.linalg.svd(matrix, full_matrices=False)
            
            # Truncate to bond dimension
            keep = min(self.bond_dim, len(S))
            U = U[:, :keep]
            S = S[:keep]
            Vh = Vh[:keep, :]
            
            # Store left tensor
            self.tensors.append(U)
            
            # Absorb S into remaining tensor
            remaining = (np.diag(S) @ Vh).reshape([keep] + list(shape[1:]))
        
        # Last tensor
        self.tensors.append(remaining)
    
    def probability(self, sequence: List[int]) -> float:
        """
        Compute probability of sequence under MPS model
        
        Returns:
            float: Probability value
        """
        if len(sequence) != len(self.tensors):
            return 0.0
        
        # Contract MPS with sequence
        result = self.tensors[0][sequence[0]]
        
        for i in range(1, len(sequence)):
            tensor = self.tensors[i]
            if len(tensor.shape) == 1:
                result = result * tensor[sequence[i]]
            else:
                result = result @ tensor[:, sequence[i]]
        
        return float(result) if np.isscalar(result) else float(result.sum())


def analyze_tensor_structure(sequences: List[List[int]], max_symbol: int, max_length: int) -> Dict:
    """
    Comprehensive tensor network analysis
    
    Returns insights about correlation structure
    """
    model = TensorNetworkModel(max_symbol, max_length)
    tensor = model.build_correlation_tensor(sequences)
    
    # PARAFAC decomposition
    factors = model.factorize_parafac(rank=5)
    
    # Tucker decomposition  
    core, tucker_factors = model.factorize_tucker(ranks=(5, 10, 10))
    
    results = {
        'tensor_shape': tensor.shape,
        'tensor_density': (tensor > 0).sum() / tensor.size,
        'parafac_rank': 5,
        'tucker_ranks': (5, 10, 10),
        'explained_variance': np.var(tensor),
    }
    
    return results


if __name__ == '__main__':
    print("Tensor Network Models for Indus Script")
    print("=" * 60)
    print()
    print("These are MATHEMATICAL tensor networks (graphical models),")
    print("NOT quantum tensor networks. Used to model classical correlations.")
