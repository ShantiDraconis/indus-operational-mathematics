"""
Indus Operational Mathematics - A framework for analyzing ancient symbolic systems.

This package implements a universal cognitive framework for understanding
and analyzing undeciphered and ancient writing systems through operational
mathematics and state machine models.
"""

__version__ = "0.1.0"

from .core.operators import UniversalOperator, CognitiveAxis
from .core.grammar import UniversalGrammar, SymbolicSystem
from .systems.harappan import HarappanSystem
from .systems.mayan import MayanSystem
from .systems.aztec import AztecSystem

__all__ = [
    "UniversalOperator",
    "CognitiveAxis",
    "UniversalGrammar",
    "SymbolicSystem",
    "HarappanSystem",
    "MayanSystem",
    "AztecSystem",
]
