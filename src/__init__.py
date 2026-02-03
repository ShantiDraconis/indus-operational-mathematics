"""
Harappan Operational Mathematics
A formal implementation of the Harappan axiomatic system.

This package provides:
- Core symbol and inscription classes
- Deterministic finite automaton for validation
- Composition engine implementing the ⊕ operator
- Semantic interpreter for institutional states
"""

from .harappan_core import (
    Symbol,
    SymbolClass,
    Inscription,
    HarappanAutomaton,
    State,
    CompositionEngine,
    SemanticInterpreter,
    create_example_inscription
)

__all__ = [
    'Symbol',
    'SymbolClass',
    'Inscription',
    'HarappanAutomaton',
    'State',
    'CompositionEngine',
    'SemanticInterpreter',
    'create_example_inscription'
]

__version__ = '1.0.0'
__author__ = 'Harappan Operational Mathematics Project'
Indus Operational Mathematics
A rigorous framework for analyzing Indus script patterns using statistical methods,
with clear separation between physics, statistics, and philosophy.

A comparative analysis framework for studying symbolic systems
across ancient and modern contexts.
"""

__version__ = "0.1.0"
