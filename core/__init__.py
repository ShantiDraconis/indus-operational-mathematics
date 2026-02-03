"""
Harappan Operational Mathematics - Core Module

This package contains the foundational implementations for the Harappan
operational mathematics system, including the state machine automaton
and basic symbol processing.
"""

from .harappan_automaton import (
    HarappanAutomaton,
    State,
    Symbol,
    SymbolType,
    ENTITY_MEANINGS,
    CLOSURE_MEANINGS,
    RELATION_MEANINGS,
)

__all__ = [
    'HarappanAutomaton',
    'State',
    'Symbol',
    'SymbolType',
    'ENTITY_MEANINGS',
    'CLOSURE_MEANINGS',
    'RELATION_MEANINGS',
]
