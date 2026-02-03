"""
Test tensor network models
"""

import pytest
import numpy as np
from indus_analysis import TensorNetworkModel, MatrixProductState


class TestTensorNetworkModel:
    def test_initialization(self):
        model = TensorNetworkModel(max_symbol_id=10, max_sequence_length=5)
        assert model.max_symbol_id == 10
        assert model.max_sequence_length == 5
        assert model.correlation_tensor is None
    
    def test_build_correlation_tensor(self):
        model = TensorNetworkModel(max_symbol_id=5, max_sequence_length=3)
        
        sequences = [
            [1, 2, 3],
            [1, 2, 4],
            [2, 3, 1],
        ]
        
        tensor = model.build_correlation_tensor(sequences)
        
        assert tensor.shape == (3, 5, 5)
        assert np.allclose(tensor.sum(), 1.0)  # Normalized
        assert (tensor >= 0).all()  # Non-negative
    
    def test_predict_next_symbol(self):
        model = TensorNetworkModel(max_symbol_id=5, max_sequence_length=3)
        
        sequences = [
            [1, 2, 3],
            [1, 2, 3],
        ]
        
        tensor = model.build_correlation_tensor(sequences)
        probs = model.predict_next_symbol([1, 2], position=2, context=2)
        
        assert len(probs) == 5
        assert np.allclose(probs.sum(), 1.0)  # Probability distribution
        assert (probs >= 0).all()


class TestMatrixProductState:
    def test_initialization(self):
        mps = MatrixProductState(symbol_dim=5, bond_dim=3)
        assert mps.symbol_dim == 5
        assert mps.bond_dim == 3
        assert len(mps.tensors) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
