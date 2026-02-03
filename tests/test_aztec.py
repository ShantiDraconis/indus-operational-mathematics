"""
Tests for Aztec system implementation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from symbolic_systems.systems.aztec import AztecSystem
from symbolic_systems.core.grammar import RealityLevel


def test_aztec_system_initialization():
    """Test Aztec system is initialized correctly."""
    aztec = AztecSystem()
    
    assert aztec.name == "Aztec"
    assert aztec.primary_level == RealityLevel.MESO
    assert len(aztec.symbols) > 0


def test_aztec_calendar_parameters():
    """Test Aztec calendar parameters."""
    aztec = AztecSystem()
    
    assert aztec.calendar['tonalpohualli_days'] == 260
    assert aztec.calendar['day_signs'] == 20
    assert aztec.calendar['day_numbers'] == 13


def test_aztec_day_signs():
    """Test Aztec day signs."""
    aztec = AztecSystem()
    
    assert len(aztec.day_signs) == 20
    assert "Cipactli" in aztec.day_signs
    assert "Xochitl" in aztec.day_signs


def test_aztec_tonalpohualli_calculation():
    """Test Tonalpohualli calculation."""
    aztec = AztecSystem()
    
    # Test valid calculation
    result = aztec.calculate_tonalpohualli(day_number=1, day_sign_index=0)
    assert result['day_number'] == 1
    assert result['day_sign'] == "Cipactli"
    assert result['calendar_position'] == 0
    
    # Test another date
    result2 = aztec.calculate_tonalpohualli(day_number=13, day_sign_index=19)
    assert result2['day_number'] == 13
    assert result2['day_sign'] == "Xochitl"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        aztec.calculate_tonalpohualli(day_number=0, day_sign_index=0)
    
    with pytest.raises(ValueError):
        aztec.calculate_tonalpohualli(day_number=14, day_sign_index=0)
    
    with pytest.raises(ValueError):
        aztec.calculate_tonalpohualli(day_number=1, day_sign_index=20)


def test_aztec_symbols():
    """Test that key Aztec symbols exist."""
    aztec = AztecSystem()
    
    assert aztec.get_symbol("A_DOT") is not None  # Point
    assert aztec.get_symbol("A_CROSS") is not None  # Directional cross
    assert aztec.get_symbol("A_TONATIUH") is not None  # Sun
    assert aztec.get_symbol("A_CALLI") is not None  # House


def test_aztec_parse_codex_entry():
    """Test parsing Codex Mendoza-style entry."""
    aztec = AztecSystem()
    
    territories = ["Territory1", "Territory2"]
    tributes = [{"item": "Jade", "quantity": 20}]
    events = [{"event": "Conquest", "date": "1-Cipactli"}]
    
    entry = aztec.parse_codex_entry(territories, tributes, events)
    
    assert entry['type'] == 'codex_entry'
    assert len(entry['territories']) == 2
    assert len(entry['tributes']) == 1
    assert len(entry['events']) == 1
    assert entry['complexity'] == 4


def test_aztec_statistics():
    """Test getting Aztec system statistics."""
    aztec = AztecSystem()
    stats = aztec.get_statistics()
    
    assert stats['name'] == 'Aztec'
    assert stats['total_symbols'] > 0
    assert stats['primary_level'] == 'institution_transaction'
    assert stats['day_signs'] == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
