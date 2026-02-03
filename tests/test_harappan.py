"""
Tests for Harappan system implementation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from symbolic_systems.systems.harappan import HarappanSystem
from symbolic_systems.core.grammar import RealityLevel


def test_harappan_system_initialization():
    """Test Harappan system is initialized correctly."""
    harappan = HarappanSystem()
    
    assert harappan.name == "Harappan"
    assert harappan.primary_level == RealityLevel.MESO
    assert len(harappan.symbols) > 0


def test_harappan_symbols():
    """Test that key Harappan symbols exist."""
    harappan = HarappanSystem()
    
    # Test key symbols
    assert harappan.get_symbol("H1") is not None  # Line
    assert harappan.get_symbol("H4") is not None  # Cross
    assert harappan.get_symbol("H26") is not None  # Man
    assert harappan.get_symbol("H27") is not None  # Point
    assert harappan.get_symbol("H30") is not None  # Lord


def test_harappan_man_to_lord_transformation():
    """Test the Man → Lord transformation."""
    harappan = HarappanSystem()
    
    # Test transformation rule exists
    result = harappan.transform("H26", "crown")
    assert result == "H30"
    
    # Verify the symbols
    man = harappan.get_symbol("H26")
    lord = harappan.get_symbol("H30")
    
    assert man is not None
    assert lord is not None
    assert man.name == "Man"
    assert lord.name == "Lord"


def test_harappan_parse_inscription():
    """Test parsing Harappan inscriptions."""
    harappan = HarappanSystem()
    
    # Transaction-like inscription: Lord + Jar + units
    inscription = ["H30", "H_JAR", "H27"]
    interpretation = harappan.parse_inscription(inscription)
    
    assert interpretation['length'] == 3
    assert interpretation['type'] == 'transaction'
    
    # Person reference
    inscription2 = ["H26"]
    interpretation2 = harappan.parse_inscription(inscription2)
    assert interpretation2['type'] == 'person_reference'


def test_harappan_statistics():
    """Test getting system statistics."""
    harappan = HarappanSystem()
    stats = harappan.get_statistics()
    
    assert stats['name'] == 'Harappan'
    assert stats['total_symbols'] > 0
    assert stats['primary_level'] == 'institution_transaction'
    assert isinstance(stats['cognitive_axes_used'], list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
