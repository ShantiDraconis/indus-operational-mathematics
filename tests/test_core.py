"""
Test suite for Harappa core components
"""

import pytest
from harappa import Symbol, Operator, State, Record, ValidationEngine, SymbolType, OperatorType


class TestSymbol:
    """Test Symbol class."""
    
    def test_create_symbol(self):
        """Test symbol creation."""
        symbol = Symbol("test_id", SymbolType.ENTITY)
        assert symbol.id == "test_id"
        assert symbol.symbol_type == SymbolType.ENTITY
        assert symbol.validate()
    
    def test_symbol_with_attributes(self):
        """Test symbol with attributes."""
        symbol = Symbol("test_id", SymbolType.RESOURCE, {"weight": 10})
        assert symbol.attributes["weight"] == 10
        assert symbol.validate()
    
    def test_symbol_equality(self):
        """Test symbol equality."""
        s1 = Symbol("id1", SymbolType.ENTITY)
        s2 = Symbol("id1", SymbolType.ENTITY)
        s3 = Symbol("id2", SymbolType.ENTITY)
        
        assert s1 == s2
        assert s1 != s3
    
    def test_symbol_hashable(self):
        """Test that symbols can be used in sets."""
        s1 = Symbol("id1", SymbolType.ENTITY)
        s2 = Symbol("id2", SymbolType.ENTITY)
        
        symbol_set = {s1, s2}
        assert len(symbol_set) == 2


class TestOperator:
    """Test Operator class."""
    
    def test_create_operator(self):
        """Test operator creation."""
        op = Operator("test_op", OperatorType.TRANSFORMATION, 2)
        assert op.name == "test_op"
        assert op.operator_type == OperatorType.TRANSFORMATION
        assert op.arity == 2
    
    def test_operator_apply(self):
        """Test operator application."""
        op = Operator("test_op", OperatorType.TRANSFORMATION, 2)
        s1 = Symbol("s1", SymbolType.ENTITY)
        s2 = Symbol("s2", SymbolType.ENTITY)
        
        result = op.apply([s1, s2])
        assert isinstance(result, State)
        assert len(result.symbols) == 2
    
    def test_operator_arity_check(self):
        """Test that operator checks arity."""
        op = Operator("test_op", OperatorType.TRANSFORMATION, 2)
        s1 = Symbol("s1", SymbolType.ENTITY)
        
        with pytest.raises(ValueError):
            op.apply([s1])  # Wrong arity


class TestState:
    """Test State class."""
    
    def test_create_state(self):
        """Test state creation."""
        state = State()
        assert state.validate()
        assert not state.is_final
    
    def test_state_with_symbols(self):
        """Test state with symbols."""
        state = State()
        s1 = Symbol("s1", SymbolType.ENTITY)
        state.add_symbol(s1)
        
        assert len(state.symbols) == 1
        assert state.validate()
    
    def test_state_properties(self):
        """Test state properties."""
        state = State()
        state.properties["key"] = "value"
        assert state.properties["key"] == "value"


class TestRecord:
    """Test Record class."""
    
    def test_create_record(self):
        """Test record creation."""
        record = Record()
        assert not record.has_closure
        assert not record.validate()  # Not closed yet
    
    def test_record_with_closure(self):
        """Test record with closure."""
        record = Record()
        s1 = Symbol("s1", SymbolType.ENTITY)
        record.add_symbol(s1)
        record.close()
        
        assert record.has_closure
        assert record.validate()
    
    def test_record_validation_requires_closure(self):
        """Test that validation requires closure."""
        record = Record()
        s1 = Symbol("s1", SymbolType.ENTITY)
        record.add_symbol(s1)
        
        assert not record.validate()  # No closure
        
        record.close()
        assert record.validate()  # Now valid


class TestValidationEngine:
    """Test ValidationEngine class."""
    
    def test_validate_valid_record(self):
        """Test validation of valid record."""
        engine = ValidationEngine()
        record = Record()
        s1 = Symbol("s1", SymbolType.ENTITY)
        record.add_symbol(s1)
        record.close()
        
        assert engine.validate_record(record)
    
    def test_validate_invalid_record(self):
        """Test validation of invalid record."""
        engine = ValidationEngine()
        record = Record()
        s1 = Symbol("s1", SymbolType.ENTITY)
        record.add_symbol(s1)
        # No closure
        
        assert not engine.validate_record(record)
    
    def test_custom_validation_rule(self):
        """Test custom validation rule."""
        engine = ValidationEngine()
        
        def min_symbols_rule(record):
            return len(record.symbols) >= 2
        
        engine.add_rule(min_symbols_rule)
        
        # Record with 1 symbol
        record1 = Record()
        record1.add_symbol(Symbol("s1", SymbolType.ENTITY))
        record1.close()
        assert not engine.validate_record(record1)
        
        # Record with 2 symbols
        record2 = Record()
        record2.add_symbol(Symbol("s1", SymbolType.ENTITY))
        record2.add_symbol(Symbol("s2", SymbolType.ENTITY))
        record2.close()
        assert engine.validate_record(record2)
    
    def test_state_transition_validation(self):
        """Test state transition validation."""
        engine = ValidationEngine()
        
        from_state = State()
        from_state.add_symbol(Symbol("s1", SymbolType.ENTITY))
        
        to_state = State()
        to_state.add_symbol(Symbol("s2", SymbolType.ENTITY))
        
        op = Operator("transform", OperatorType.TRANSFORMATION, 1)
        
        assert engine.validate_state_transition(from_state, to_state, op)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
