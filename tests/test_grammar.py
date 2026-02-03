"""
Tests for universal grammar and symbolic systems.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from symbolic_systems.core.grammar import (
    Symbol,
    SymbolState,
    RealityLevel,
    SymbolicSystem,
    UniversalGrammar
)
from symbolic_systems.core.operators import CognitiveAxis


def test_symbol_creation():
    """Test creating a symbol."""
    symbol = Symbol(
        base_id="TEST1",
        name="Test Symbol",
        form="T",
        cognitive_axes=[CognitiveAxis.PRESENCE],
        description="A test symbol"
    )
    
    assert symbol.base_id == "TEST1"
    assert symbol.name == "Test Symbol"
    assert symbol.form == "T"
    assert len(symbol.modifiers) == 0
    assert CognitiveAxis.PRESENCE in symbol.cognitive_axes


def test_symbol_composition():
    """Test composing symbols with modifiers."""
    base = Symbol(
        base_id="BASE",
        name="Base",
        form="B",
        cognitive_axes=[CognitiveAxis.PRESENCE]
    )
    
    modified = base.compose_with("modifier1")
    assert len(modified.modifiers) == 1
    assert "modifier1" in modified.modifiers
    assert modified.base_id == "BASE"
    
    double_modified = modified.compose_with("modifier2")
    assert len(double_modified.modifiers) == 2


def test_reality_levels():
    """Test the 3 reality levels."""
    levels = list(RealityLevel)
    assert len(levels) == 3
    assert RealityLevel.MICRO in levels
    assert RealityLevel.MESO in levels
    assert RealityLevel.MACRO in levels


def test_symbolic_system_creation():
    """Test creating a symbolic system."""
    system = SymbolicSystem("TestSystem", RealityLevel.MESO)
    assert system.name == "TestSystem"
    assert system.primary_level == RealityLevel.MESO
    assert len(system.symbols) == 0


def test_symbolic_system_add_symbol():
    """Test adding symbols to a system."""
    system = SymbolicSystem("TestSystem", RealityLevel.MESO)
    
    symbol = Symbol(
        base_id="S1",
        name="Symbol1",
        form="S",
        cognitive_axes=[CognitiveAxis.PRESENCE]
    )
    
    system.add_symbol(symbol)
    assert len(system.symbols) == 1
    assert system.get_symbol("S1") == symbol


def test_transformation_rules():
    """Test transformation rules."""
    system = SymbolicSystem("TestSystem", RealityLevel.MESO)
    
    system.add_transformation_rule("base", "modifier", "result")
    assert "base" in system.transformation_rules
    
    result = system.transform("base", "modifier")
    assert result == "result"
    
    # Test non-existent transformation
    result = system.transform("base", "nonexistent")
    assert result is None


def test_parse_sequence():
    """Test parsing symbol sequences."""
    system = SymbolicSystem("TestSystem", RealityLevel.MESO)
    
    s1 = Symbol(base_id="S1", name="Symbol1", form="1", cognitive_axes=[CognitiveAxis.PRESENCE])
    s2 = Symbol(base_id="S2", name="Symbol2", form="2", cognitive_axes=[CognitiveAxis.QUANTITY])
    
    system.add_symbol(s1)
    system.add_symbol(s2)
    
    states = system.parse_sequence(["S1", "S2", "S1"])
    assert len(states) == 3
    assert all(isinstance(state, SymbolState) for state in states)
    assert states[0].symbol.base_id == "S1"
    assert states[1].symbol.base_id == "S2"
    assert states[2].symbol.base_id == "S1"


def test_universal_grammar():
    """Test universal grammar functionality."""
    grammar = UniversalGrammar()
    
    assert len(grammar.cognitive_axes) == 7
    assert len(grammar.reality_levels) == 3


def test_universal_grammar_register_system():
    """Test registering systems with universal grammar."""
    grammar = UniversalGrammar()
    
    system1 = SymbolicSystem("System1", RealityLevel.MICRO)
    system2 = SymbolicSystem("System2", RealityLevel.MACRO)
    
    grammar.register_system(system1)
    grammar.register_system(system2)
    
    assert len(grammar.systems) == 2
    assert grammar.get_system("System1") == system1
    assert grammar.get_system("System2") == system2


def test_compare_systems():
    """Test comparing two systems."""
    grammar = UniversalGrammar()
    
    # Create first system
    sys1 = SymbolicSystem("Sys1", RealityLevel.MESO)
    s1 = Symbol(base_id="S1", name="Point", form="•", 
                cognitive_axes=[CognitiveAxis.QUANTITY, CognitiveAxis.PRESENCE])
    sys1.add_symbol(s1)
    
    # Create second system
    sys2 = SymbolicSystem("Sys2", RealityLevel.MESO)
    s2 = Symbol(base_id="S2", name="Dot", form="•", 
                cognitive_axes=[CognitiveAxis.QUANTITY, CognitiveAxis.PRESENCE])
    sys2.add_symbol(s2)
    
    grammar.register_system(sys1)
    grammar.register_system(sys2)
    
    comparison = grammar.compare_systems("Sys1", "Sys2")
    
    assert comparison['system1'] == "Sys1"
    assert comparison['system2'] == "Sys2"
    assert comparison['total_matches'] > 0  # Should find correspondence


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
