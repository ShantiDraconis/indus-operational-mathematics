"""
Tests for universal operators and cognitive axes.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from symbolic_systems.core.operators import (
    CognitiveAxis,
    UniversalOperator,
    UNIVERSAL_OPERATORS,
    get_operator_by_name,
    get_operators_by_axis
)


def test_cognitive_axes():
    """Test that all 7 cognitive axes are defined."""
    axes = list(CognitiveAxis)
    assert len(axes) == 7
    
    # Check specific axes exist
    assert CognitiveAxis.PRESENCE in axes
    assert CognitiveAxis.QUANTITY in axes
    assert CognitiveAxis.QUALITY in axes
    assert CognitiveAxis.RELATION in axes
    assert CognitiveAxis.SPACE in axes
    assert CognitiveAxis.TIME in axes
    assert CognitiveAxis.VALIDATION in axes


def test_universal_operators_count():
    """Test that all 15 universal operators are defined."""
    assert len(UNIVERSAL_OPERATORS) == 15


def test_universal_operators_structure():
    """Test that each operator has required fields."""
    for op in UNIVERSAL_OPERATORS:
        assert isinstance(op, UniversalOperator)
        assert isinstance(op.name, str)
        assert isinstance(op.form, str)
        assert isinstance(op.function, str)
        assert isinstance(op.cognitive_axes, list)
        assert isinstance(op.examples, list)
        assert len(op.cognitive_axes) > 0
        assert len(op.examples) > 0


def test_get_operator_by_name():
    """Test retrieving operators by name."""
    # Test existing operators
    point = get_operator_by_name("Point")
    assert point is not None
    assert point.name == "Point"
    assert point.form == "•"
    
    line = get_operator_by_name("Line")
    assert line is not None
    assert line.name == "Line"
    
    # Test case insensitivity
    cross = get_operator_by_name("CROSS")
    assert cross is not None
    assert cross.name == "Cross"
    
    # Test non-existent operator
    none_op = get_operator_by_name("NonExistent")
    assert none_op is None


def test_get_operators_by_axis():
    """Test retrieving operators by cognitive axis."""
    # Test QUANTITY axis
    quantity_ops = get_operators_by_axis(CognitiveAxis.QUANTITY)
    assert len(quantity_ops) > 0
    for op in quantity_ops:
        assert CognitiveAxis.QUANTITY in op.cognitive_axes
    
    # Test TIME axis
    time_ops = get_operators_by_axis(CognitiveAxis.TIME)
    assert len(time_ops) > 0
    for op in time_ops:
        assert CognitiveAxis.TIME in op.cognitive_axes
    
    # Test SPACE axis
    space_ops = get_operators_by_axis(CognitiveAxis.SPACE)
    assert len(space_ops) > 0
    for op in space_ops:
        assert CognitiveAxis.SPACE in op.cognitive_axes


def test_operator_names():
    """Test that specific operators exist by name."""
    expected_names = [
        "Point", "Line", "Cross", "Circle", "Triangle",
        "Square", "Wave", "Spiral", "Hand", "Foot",
        "Head", "Eye", "Mouth", "Heart", "Plant"
    ]
    
    operator_names = [op.name for op in UNIVERSAL_OPERATORS]
    
    for expected in expected_names:
        assert expected in operator_names, f"Operator '{expected}' not found"


def test_operator_examples():
    """Test that operators have examples from different systems."""
    point = get_operator_by_name("Point")
    assert "Harappan" in str(point.examples) or "27" in str(point.examples)
    
    cross = get_operator_by_name("Cross")
    assert len(cross.examples) >= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
