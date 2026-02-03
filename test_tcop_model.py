"""
Unit tests for TCOP computational model
Tests the finite automaton implementation and TCOP validation
"""

import unittest
from tcop_model import (
    BaseSymbol, Operator, OperatorType, State, GraphicSystem,
    TCOPValidator, create_harappan_example, create_ancient_chinese_example
)


class TestBaseSymbol(unittest.TestCase):
    """Test BaseSymbol class"""
    
    def test_creation(self):
        symbol = BaseSymbol("test_id", "Test", "test_class")
        self.assertEqual(symbol.id, "test_id")
        self.assertEqual(symbol.name, "Test")
        self.assertEqual(symbol.ontological_class, "test_class")
    
    def test_immutability(self):
        symbol = BaseSymbol("test_id", "Test", "test_class")
        with self.assertRaises(AttributeError):
            symbol.id = "new_id"


class TestOperator(unittest.TestCase):
    """Test Operator class"""
    
    def test_creation(self):
        op = Operator("op_id", "Op Name", OperatorType.MODIFICATION, "Description")
        self.assertEqual(op.id, "op_id")
        self.assertEqual(op.name, "Op Name")
        self.assertEqual(op.operator_type, OperatorType.MODIFICATION)
    
    def test_terminal_operator(self):
        op = Operator("term", "Terminal", OperatorType.TERMINAL, "Marks end")
        self.assertEqual(op.operator_type, OperatorType.TERMINAL)


class TestState(unittest.TestCase):
    """Test State class"""
    
    def test_creation(self):
        base = BaseSymbol("b1", "Base", "class")
        state = State(base, frozenset(["op1", "op2"]))
        self.assertEqual(state.base, base)
        self.assertEqual(len(state.operators), 2)
    
    def test_empty_operators(self):
        base = BaseSymbol("b1", "Base", "class")
        state = State(base, frozenset())
        self.assertEqual(len(state.operators), 0)
    
    def test_equality(self):
        base = BaseSymbol("b1", "Base", "class")
        state1 = State(base, frozenset(["op1"]))
        state2 = State(base, frozenset(["op1"]))
        self.assertEqual(state1, state2)
    
    def test_hashable(self):
        base = BaseSymbol("b1", "Base", "class")
        state = State(base, frozenset(["op1"]))
        # Should not raise exception
        hash(state)
        states_set = {state}
        self.assertEqual(len(states_set), 1)


class TestGraphicSystem(unittest.TestCase):
    """Test GraphicSystem class"""
    
    def setUp(self):
        self.system = GraphicSystem("Test System")
        self.base = BaseSymbol("b1", "Base1", "class1")
        self.op1 = Operator("op1", "Operator1", OperatorType.MODIFICATION, "Desc1")
        self.op2 = Operator("op2", "Operator2", OperatorType.TERMINAL, "Desc2")
    
    def test_add_base_symbol(self):
        self.system.add_base_symbol(self.base)
        self.assertIn(self.base.id, self.system.base_symbols)
        self.assertEqual(self.system.get_base_count(), 1)
    
    def test_add_operator(self):
        self.system.add_operator(self.op1)
        self.assertIn(self.op1.id, self.system.operators)
        self.assertEqual(len(self.system.operators), 1)
    
    def test_apply_operator(self):
        self.system.add_base_symbol(self.base)
        self.system.add_operator(self.op1)
        
        initial_state = State(self.base, frozenset())
        new_state = self.system.apply_operator(initial_state, self.op1.id)
        
        self.assertIsNotNone(new_state)
        self.assertIn(self.op1.id, new_state.operators)
    
    def test_apply_terminal_operator(self):
        self.system.add_base_symbol(self.base)
        self.system.add_operator(self.op2)
        
        initial_state = State(self.base, frozenset())
        new_state = self.system.apply_operator(initial_state, self.op2.id)
        
        self.assertTrue(self.system.is_accepting_state(new_state))
    
    def test_composition(self):
        self.system.add_base_symbol(self.base)
        self.system.add_operator(self.op1)
        self.system.add_operator(self.op2)
        
        # Test composition: b -> op1 -> op2
        state = self.system.get_state_by_composition(
            self.base.id,
            [self.op1.id, self.op2.id]
        )
        
        self.assertIsNotNone(state)
        self.assertEqual(len(state.operators), 2)
        self.assertIn(self.op1.id, state.operators)
        self.assertIn(self.op2.id, state.operators)
    
    def test_record_occurrence(self):
        self.system.add_base_symbol(self.base)
        state = State(self.base, frozenset())
        
        self.system.record_occurrence(state)
        self.system.record_occurrence(state)
        
        self.assertEqual(self.system.symbol_frequencies[state], 2)
    
    def test_state_space_size(self):
        self.system.add_base_symbol(self.base)
        initial_size = self.system.get_state_space_size()
        
        self.system.add_operator(self.op1)
        initial_state = State(self.base, frozenset())
        self.system.apply_operator(initial_state, self.op1.id)
        
        new_size = self.system.get_state_space_size()
        self.assertGreater(new_size, initial_size)
    
    def test_finiteness_hypothesis(self):
        # Add base symbols
        for i in range(3):
            base = BaseSymbol(f"b{i}", f"Base{i}", "class")
            self.system.add_base_symbol(base)
        
        # Add operators
        for i in range(2):
            op = Operator(f"op{i}", f"Op{i}", OperatorType.MODIFICATION, "Desc")
            self.system.add_operator(op)
        
        # Generate states (should have |B| * more states)
        for base_id in self.system.base_symbols:
            for op_id in self.system.operators:
                state = State(self.system.base_symbols[base_id], frozenset())
                self.system.apply_operator(state, op_id)
        
        # Should satisfy |B| << |Σ|
        self.assertTrue(self.system.verify_finiteness_hypothesis())


class TestTCOPValidator(unittest.TestCase):
    """Test TCOP validation"""
    
    def test_harappan_example(self):
        system = create_harappan_example()
        results = TCOPValidator.validate_system(system)
        
        self.assertTrue(results["recurrence"])
        self.assertTrue(results["systematicity"])
        self.assertTrue(results["compositionality"])
        self.assertTrue(results["regularity"])
        self.assertTrue(results["finiteness"])
        self.assertTrue(results["tcop_satisfied"])
    
    def test_chinese_example(self):
        system = create_ancient_chinese_example()
        results = TCOPValidator.validate_system(system)
        
        self.assertTrue(results["recurrence"])
        self.assertTrue(results["systematicity"])
        self.assertTrue(results["compositionality"])
        self.assertTrue(results["regularity"])
        self.assertTrue(results["finiteness"])
        self.assertTrue(results["tcop_satisfied"])
    
    def test_empty_system(self):
        system = GraphicSystem("Empty")
        results = TCOPValidator.validate_system(system)
        
        self.assertFalse(results["recurrence"])
        self.assertFalse(results["tcop_satisfied"])


class TestSystemExamples(unittest.TestCase):
    """Test example system implementations"""
    
    def test_harappan_structure(self):
        system = create_harappan_example()
        
        # Check base symbols
        self.assertEqual(system.get_base_count(), 4)
        self.assertIn("fish", system.base_symbols)
        self.assertIn("jar", system.base_symbols)
        
        # Check operators
        self.assertGreater(len(system.operators), 0)
        self.assertIn("terminal", system.operators)
        
        # Check states generated
        self.assertGreater(system.get_state_space_size(), system.get_base_count())
    
    def test_chinese_structure(self):
        system = create_ancient_chinese_example()
        
        # Check base symbols (radicals)
        self.assertEqual(system.get_base_count(), 4)
        self.assertIn("person", system.base_symbols)
        
        # Check operators
        self.assertGreater(len(system.operators), 0)
        
        # Check specific composition
        state = system.get_state_by_composition("person", ["double", "terminal"])
        self.assertIsNotNone(state)
        self.assertTrue(system.is_accepting_state(state))
    
    def test_system_export(self):
        system = create_harappan_example()
        export = system.to_dict()
        
        self.assertEqual(export["name"], "Harappan Script (Simplified)")
        self.assertIn("base_symbols", export)
        self.assertIn("operators", export)
        self.assertIn("state_count", export)
        self.assertGreater(export["state_count"], 0)


class TestAutomatonProperties(unittest.TestCase):
    """Test finite automaton properties"""
    
    def setUp(self):
        self.system = GraphicSystem("Test Automaton")
        self.base = BaseSymbol("b1", "Base", "class")
        self.system.add_base_symbol(self.base)
        
        self.op1 = Operator("op1", "Op1", OperatorType.MODIFICATION, "Mod")
        self.op2 = Operator("op2", "Op2", OperatorType.TERMINAL, "Term")
        self.system.add_operator(self.op1)
        self.system.add_operator(self.op2)
    
    def test_transition_function(self):
        """Test δ(state, operator) = new_state"""
        initial = State(self.base, frozenset())
        
        # Apply first operator
        state1 = self.system.apply_operator(initial, "op1")
        self.assertIsNotNone(state1)
        
        # Apply second operator
        state2 = self.system.apply_operator(state1, "op2")
        self.assertIsNotNone(state2)
        
        # Check transition recorded
        self.assertIn((initial, "op1"), self.system.transitions)
        self.assertEqual(self.system.transitions[(initial, "op1")], state1)
    
    def test_accepting_states(self):
        """Test that terminal operators create accepting states"""
        initial = State(self.base, frozenset())
        
        # State without terminal operator
        state1 = self.system.apply_operator(initial, "op1")
        self.assertFalse(self.system.is_accepting_state(state1))
        
        # State with terminal operator
        state2 = self.system.apply_operator(state1, "op2")
        self.assertTrue(self.system.is_accepting_state(state2))
    
    def test_determinism(self):
        """Test that transitions are deterministic"""
        initial = State(self.base, frozenset())
        
        # Apply same operator twice
        state1a = self.system.apply_operator(initial, "op1")
        state1b = self.system.apply_operator(initial, "op1")
        
        # Should get the same state (deterministic)
        self.assertEqual(state1a, state1b)
    
    def test_no_duplicate_operators(self):
        """Test that operators cannot be applied twice"""
        initial = State(self.base, frozenset())
        
        # Apply operator
        state1 = self.system.apply_operator(initial, "op1")
        
        # Try to apply same operator again
        state2 = self.system.apply_operator(state1, "op1")
        
        # Should return None (cannot reapply)
        self.assertIsNone(state2)


if __name__ == "__main__":
    unittest.main()
