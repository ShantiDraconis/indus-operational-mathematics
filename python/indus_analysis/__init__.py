"""
Python package initialization for Indus Analysis
"""

from .statistical_analysis import (
    Symbol,
    Sequence,
    IndusStatisticalAnalysis,
    compute_top_correlations
)

from .tensor_models import (
    TensorNetworkModel,
    MatrixProductState,
    analyze_tensor_structure
)

__version__ = '0.1.0'
__all__ = [
    'Symbol',
    'Sequence',
    'IndusStatisticalAnalysis',
    'compute_top_correlations',
    'TensorNetworkModel',
    'MatrixProductState',
    'analyze_tensor_structure',
]
