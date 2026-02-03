#!/usr/bin/env python3
"""
Comprehensive Test Suite for Indus Operational Mathematics
Tests all core functionality of the system.
"""

import sys
import os

# Add implementation directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'implementation'))

from parser.indus_automaton import (
    IndusAutomaton, 
    IndusSymbolMapper, 
    SymbolClass, 
    State,
    validate_indus_sequence
)
from validator.indus_validator import IndusValidator, validate_sequence
from converter.harappan_to_json import HarappanToJsonConverter, harappan_to_json


def test_automaton():
    """Test the finite automaton"""
    print("=" * 60)
    print("TEST 1: Finite Automaton")
    print("=" * 60)
    
    automaton = IndusAutomaton()
    
    # Test 1.1: Simple valid sequence
    automaton.reset()
    assert automaton.process_symbol(SymbolClass.ENT_OVAL)
    assert automaton.process_symbol(SymbolClass.OP_CLOSE)
    assert automaton.is_valid_record()
    print("✓ Test 1.1: Simple sequence (Entity + Closure)")
    
    # Test 1.2: Complex valid sequence
    automaton.reset()
    assert automaton.process_symbol(SymbolClass.ENT_ANIMAL)
    assert automaton.process_symbol(SymbolClass.OP_COUNT)
    assert automaton.process_symbol(SymbolClass.OP_COUNT)
    assert automaton.process_symbol(SymbolClass.OP_REL)
    assert automaton.process_symbol(SymbolClass.OP_CLOSE)
    assert automaton.is_valid_record()
    print("✓ Test 1.2: Complex sequence (Animal + Count + Count + Rel + Close)")
    
    # Test 1.3: Invalid sequence (no closure)
    automaton.reset()
    automaton.process_symbol(SymbolClass.ENT_OVAL)
    automaton.process_symbol(SymbolClass.OP_COUNT)
    assert not automaton.is_valid_record()
    print("✓ Test 1.3: Invalid sequence correctly rejected (no closure)")
    
    # Test 1.4: Invalid transition
    automaton.reset()
    automaton.process_symbol(SymbolClass.ENT_OVAL)
    automaton.process_symbol(SymbolClass.OP_CLOSE)
    assert not automaton.process_symbol(SymbolClass.OP_COUNT)  # Can't add after closure
    print("✓ Test 1.4: Invalid transition correctly rejected (after closure)")
    
    print()


def test_symbol_mapper():
    """Test symbol classification"""
    print("=" * 60)
    print("TEST 2: Symbol Mapper")
    print("=" * 60)
    
    mapper = IndusSymbolMapper()
    
    # Test 2.1: Entity symbols
    assert mapper.get_symbol_class(373) == SymbolClass.ENT_OVAL
    assert mapper.get_symbol_class(200) == SymbolClass.ENT_ANIMAL
    assert mapper.get_symbol_class(328) == SymbolClass.ENT_U
    print("✓ Test 2.1: Entity symbols classified correctly")
    
    # Test 2.2: Operator symbols
    assert mapper.get_symbol_class(410) == SymbolClass.OP_COUNT
    assert mapper.get_symbol_class(400) == SymbolClass.OP_REL
    assert mapper.get_symbol_class(342) == SymbolClass.OP_CLOSE
    print("✓ Test 2.2: Operator symbols classified correctly")
    
    # Test 2.3: Sequence classification
    sequence = [373, 410, 342]
    classes = mapper.classify_sequence(sequence)
    assert classes == [SymbolClass.ENT_OVAL, SymbolClass.OP_COUNT, SymbolClass.OP_CLOSE]
    print("✓ Test 2.3: Sequence classified correctly")
    
    print()


def test_validator():
    """Test the validator"""
    print("=" * 60)
    print("TEST 3: Validator")
    print("=" * 60)
    
    validator = IndusValidator()
    
    # Test 3.1: Valid simple sequence
    is_valid, errors = validator.validate([373, 342])
    assert is_valid
    assert len(errors) == 0
    print("✓ Test 3.1: Valid simple sequence accepted")
    
    # Test 3.2: Valid complex sequence
    is_valid, errors = validator.validate([200, 410, 411, 343])
    assert is_valid
    assert len(errors) == 0
    print("✓ Test 3.2: Valid complex sequence accepted")
    
    # Test 3.3: Invalid - no closure
    is_valid, errors = validator.validate([373, 410])
    assert not is_valid
    assert len(errors) > 0
    print("✓ Test 3.3: Invalid sequence rejected (no closure)")
    
    # Test 3.4: Invalid - wrong order
    is_valid, errors = validator.validate([342, 373])
    assert not is_valid
    assert len(errors) > 0
    print("✓ Test 3.4: Invalid sequence rejected (wrong order)")
    
    # Test 3.5: Detailed validation
    result = validator.validate_with_details([373, 410, 342])
    assert result['is_valid']
    assert result['final_state'] == 'FECHADA'
    assert len(result['symbol_classes']) == 3
    print("✓ Test 3.5: Detailed validation provides correct info")
    
    print()


def test_converter():
    """Test the JSON converter"""
    print("=" * 60)
    print("TEST 4: JSON Converter")
    print("=" * 60)
    
    converter = HarappanToJsonConverter()
    
    # Test 4.1: Simple conversion
    record = converter.convert([373, 342])
    assert record.entity == "basic_token"
    assert record.closure == "simple"
    print("✓ Test 4.1: Simple sequence converted correctly")
    
    # Test 4.2: Conversion with quantity
    record = converter.convert([373, 410, 411, 342])
    assert record.entity == "basic_token"
    assert record.quantity == 3  # 410 (1) + 411 (2)
    assert record.closure == "simple"
    print("✓ Test 4.2: Quantified sequence converted correctly")
    
    # Test 4.3: Conversion with relation
    record = converter.convert([373, 400, 346])
    assert record.entity == "basic_token"
    assert "pair" in record.relations
    assert record.closure == "absolute"
    print("✓ Test 4.3: Related sequence converted correctly")
    
    # Test 4.4: JSON output
    json_str = converter.convert_to_json([200, 410, 343])
    assert '"entity"' in json_str
    assert '"unicorn"' in json_str
    assert '"closure"' in json_str
    print("✓ Test 4.4: JSON string generated correctly")
    
    # Test 4.5: Batch conversion
    sequences = [[373, 342], [200, 343], [328, 346]]
    records = converter.batch_convert(sequences)
    assert len(records) == 3
    assert all(r.closure is not None for r in records)
    print("✓ Test 4.5: Batch conversion works correctly")
    
    print()


def test_integration():
    """Test integrated workflow"""
    print("=" * 60)
    print("TEST 5: Integration")
    print("=" * 60)
    
    # Test 5.1: Validate and convert
    sequence = [200, 410, 411, 400, 343]
    
    is_valid, error = validate_indus_sequence(sequence)
    assert is_valid
    print("✓ Test 5.1a: Sequence validated")
    
    record = harappan_to_json(sequence)
    assert record['entity'] == 'unicorn'
    assert record['quantity'] == 3
    assert 'pair' in record['relations']
    assert record['closure'] == 'confirmed'
    print("✓ Test 5.1b: Sequence converted to JSON")
    
    # Test 5.2: Full pipeline
    test_sequences = [
        [373, 342],
        [200, 343],
        [328, 410, 346],
        [250, 415, 344],
    ]
    
    for seq in test_sequences:
        valid, _ = validate_indus_sequence(seq)
        if valid:
            record = harappan_to_json(seq)
            assert record['entity'] is not None
            assert record['closure'] is not None
    
    print("✓ Test 5.2: Full pipeline (validate + convert) works")
    
    print()


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("=" * 60)
    print("TEST 6: Edge Cases")
    print("=" * 60)
    
    validator = IndusValidator()
    
    # Test 6.1: Empty sequence
    is_valid, errors = validator.validate([])
    assert not is_valid
    print("✓ Test 6.1: Empty sequence rejected")
    
    # Test 6.2: Single symbol
    is_valid, errors = validator.validate([373])
    assert not is_valid
    print("✓ Test 6.2: Single symbol rejected (no closure)")
    
    # Test 6.3: Multiple qualifications
    is_valid, errors = validator.validate([373, 342])
    assert is_valid
    print("✓ Test 6.3: Minimal valid sequence accepted")
    
    # Test 6.4: Multiple counts
    is_valid, errors = validator.validate([373, 410, 411, 412, 342])
    assert is_valid
    print("✓ Test 6.4: Multiple counts accepted")
    
    # Test 6.5: All closure types valid
    for closure in [342, 343, 344, 345, 346, 347, 348]:
        is_valid, _ = validator.validate([373, closure])
        assert is_valid
    print("✓ Test 6.5: All closure types accepted")
    
    print()


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("INDUS OPERATIONAL MATHEMATICS - TEST SUITE")
    print("=" * 60)
    print()
    
    try:
        test_automaton()
        test_symbol_mapper()
        test_validator()
        test_converter()
        test_integration()
        test_edge_cases()
        
        print("=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        print()
        print("Summary:")
        print("  - Automaton: Working")
        print("  - Symbol Mapper: Working")
        print("  - Validator: Working")
        print("  - Converter: Working")
        print("  - Integration: Working")
        print("  - Edge Cases: Handled")
        print()
        print("The Harappan Operational System is fully functional!")
        print()
        
        return 0
        
    except AssertionError as e:
        print()
        print("=" * 60)
        print("TEST FAILED! ✗")
        print("=" * 60)
        print(f"Error: {e}")
        return 1
    
    except Exception as e:
        print()
        print("=" * 60)
        print("TEST ERROR! ✗")
        print("=" * 60)
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
