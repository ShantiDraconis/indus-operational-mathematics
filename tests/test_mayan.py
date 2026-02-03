"""
Tests for Mayan system implementation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from symbolic_systems.systems.mayan import MayanSystem
from symbolic_systems.core.grammar import RealityLevel


def test_mayan_system_initialization():
    """Test Mayan system is initialized correctly."""
    mayan = MayanSystem()
    
    assert mayan.name == "Mayan"
    assert mayan.primary_level == RealityLevel.MACRO
    assert len(mayan.symbols) > 0


def test_mayan_calendar_parameters():
    """Test Mayan calendar parameters."""
    mayan = MayanSystem()
    
    assert mayan.calendar['tzolkin_days'] == 260
    assert mayan.calendar['haab_days'] == 365
    assert mayan.calendar['day_signs'] == 20
    assert mayan.calendar['day_numbers'] == 13


def test_mayan_calendar_calculation():
    """Test Mayan calendar date calculation."""
    mayan = MayanSystem()
    
    # Test basic calculation
    date = mayan.calculate_calendar_date(kin=5, uinal=0, tun=0)
    assert date['total_days'] == 5
    assert date['kin'] == 5
    assert date['uinal'] == 0
    assert date['tun'] == 0
    
    # Test with uinal
    date2 = mayan.calculate_calendar_date(kin=0, uinal=1, tun=0)
    assert date2['total_days'] == 20
    
    # Test with tun
    date3 = mayan.calculate_calendar_date(kin=0, uinal=0, tun=1)
    assert date3['total_days'] == 360


def test_mayan_symbols():
    """Test that key Mayan symbols exist."""
    mayan = MayanSystem()
    
    assert mayan.get_symbol("M_KIN") is not None  # Day
    assert mayan.get_symbol("M_AJAW") is not None  # Lord
    assert mayan.get_symbol("M_NA") is not None  # House
    assert mayan.get_symbol("M_DOT") is not None  # Numerical dot


def test_mayan_statistics():
    """Test getting Mayan system statistics."""
    mayan = MayanSystem()
    stats = mayan.get_statistics()
    
    assert stats['name'] == 'Mayan'
    assert stats['total_symbols'] > 0
    assert stats['primary_level'] == 'cosmos_cycle'
    assert 'calendar_system' in stats


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
