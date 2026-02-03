"""
Comprehensive Test Suite for Harappan Symbol Combination Analysis

This module tests all the combination analysis functionality including:
- Symbol-operator combinations (450 possibilities)
- Symbol pair compositions (2,025 possibilities)
- Sequence validation
- State transitions
- Closure properties
"""

import unittest
from harappan_symbols import SymbolFamily, GraphicOperator, create_harappan_system
from harappan_combinations import (
    SymbolOperatorCombination,
    SymbolPair,
    CombinationMatrix,
    PairMatrix,
    SequenceValidator,
    TransitionAnalyzer,
    create_comprehensive_analysis
)


class TestSymbolOperatorCombination(unittest.TestCase):
    """Test symbol-operator combinations"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
    
    def test_valid_omega_combinations(self):
        """Test that Omega symbols accept appropriate operators"""
        # Test a few Omega symbols
        for sym_id in [373, 374, 380, 390]:
            # Should accept Dot
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.DOT)
            self.assertTrue(comb.is_valid(self.registry))
            
            # Should accept Stroke
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.STROKE)
            self.assertTrue(comb.is_valid(self.registry))
            
            # Should not accept Knot (Delta-specific)
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.KNOT)
            self.assertFalse(comb.is_valid(self.registry))
    
    def test_valid_delta_combinations(self):
        """Test that Delta symbols accept appropriate operators"""
        # Test a few Delta symbols
        for sym_id in [400, 405, 409]:
            # Should accept Knot
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.KNOT)
            self.assertTrue(comb.is_valid(self.registry))
            
            # Should accept Stem
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.STEM)
            self.assertTrue(comb.is_valid(self.registry))
            
            # Should not accept Crown (Omega-specific)
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.CROWN)
            self.assertFalse(comb.is_valid(self.registry))
    
    def test_valid_sigma_combinations(self):
        """Test that Sigma symbols accept appropriate operators"""
        # Test a few Sigma symbols
        for sym_id in [410, 415, 417]:
            # Should accept Stack
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.STACK)
            self.assertTrue(comb.is_valid(self.registry))
            
            # Should not accept Dot
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.DOT)
            self.assertFalse(comb.is_valid(self.registry))
            
            # Should not accept Knot
            comb = SymbolOperatorCombination(sym_id, GraphicOperator.KNOT)
            self.assertFalse(comb.is_valid(self.registry))
    
    def test_invalid_symbol_id(self):
        """Test that invalid symbol IDs raise ValueError"""
        with self.assertRaises(ValueError):
            SymbolOperatorCombination(100, GraphicOperator.DOT)
        
        with self.assertRaises(ValueError):
            SymbolOperatorCombination(500, GraphicOperator.DOT)


class TestSymbolPair(unittest.TestCase):
    """Test symbol pair compositions"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
    
    def test_omega_omega_not_composable(self):
        """Test that Omega+Omega is not composable"""
        pair = SymbolPair(373, 374)  # Both Omega
        self.assertFalse(pair.is_composable(self.registry))
        
        pair = SymbolPair(375, 380)  # Both Omega
        self.assertFalse(pair.is_composable(self.registry))
    
    def test_omega_delta_composable(self):
        """Test that Omega+Delta is composable"""
        pair = SymbolPair(373, 400)  # Omega + Delta
        self.assertTrue(pair.is_composable(self.registry))
        
        pair = SymbolPair(400, 373)  # Delta + Omega
        self.assertTrue(pair.is_composable(self.registry))
    
    def test_omega_sigma_composable(self):
        """Test that Omega+Sigma is composable"""
        pair = SymbolPair(373, 410)  # Omega + Sigma
        self.assertTrue(pair.is_composable(self.registry))
        
        pair = SymbolPair(410, 373)  # Sigma + Omega
        self.assertTrue(pair.is_composable(self.registry))
    
    def test_delta_delta_composable(self):
        """Test that Delta+Delta is composable (for chains)"""
        pair = SymbolPair(400, 401)  # Both Delta
        self.assertTrue(pair.is_composable(self.registry))
    
    def test_sigma_sigma_not_composable(self):
        """Test that Sigma+Sigma is not composable"""
        pair = SymbolPair(410, 411)  # Both Sigma
        self.assertFalse(pair.is_composable(self.registry))
    
    def test_sigma_delta_not_composable(self):
        """Test that Sigma+Delta is not composable"""
        pair = SymbolPair(410, 400)  # Sigma + Delta
        self.assertFalse(pair.is_composable(self.registry))


class TestCombinationMatrix(unittest.TestCase):
    """Test the combination matrix"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
        self.matrix = CombinationMatrix(self.registry)
    
    def test_matrix_size(self):
        """Test that matrix has correct number of combinations"""
        self.assertEqual(len(self.matrix.combinations), 450)  # 45 × 10
    
    def test_statistics(self):
        """Test combination statistics"""
        stats = self.matrix.get_statistics()
        
        self.assertEqual(stats['total_combinations'], 450)
        self.assertGreater(stats['valid_combinations'], 0)
        self.assertGreater(stats['invalid_combinations'], 0)
        self.assertAlmostEqual(
            stats['validity_ratio'],
            stats['valid_combinations'] / 450,
            places=5
        )
    
    def test_family_statistics(self):
        """Test family-specific statistics"""
        fam_stats = self.matrix.get_family_statistics()
        
        # Should have stats for all three families
        self.assertIn('Ω', fam_stats)
        self.assertIn('Δ', fam_stats)
        self.assertIn('Σ', fam_stats)
        
        # Check Omega family (27 symbols, 8 valid operators each = 216 valid)
        omega_stats = fam_stats['Ω']
        self.assertEqual(omega_stats['symbol_count'], 27)
        self.assertEqual(omega_stats['total_combinations'], 270)  # 27 × 10
        
        # Check Sigma family (8 symbols, 1 valid operator each = 8 valid)
        sigma_stats = fam_stats['Σ']
        self.assertEqual(sigma_stats['symbol_count'], 8)
        self.assertEqual(sigma_stats['total_combinations'], 80)  # 8 × 10
    
    def test_valid_operators_for_symbol(self):
        """Test getting valid operators for specific symbols"""
        # Omega symbol should have 8 valid operators
        omega_ops = self.matrix.get_valid_operators(373)
        self.assertEqual(len(omega_ops), 8)
        self.assertIn(GraphicOperator.DOT, omega_ops)
        self.assertIn(GraphicOperator.STACK, omega_ops)
        self.assertNotIn(GraphicOperator.KNOT, omega_ops)
        
        # Delta symbol should have 4 valid operators
        delta_ops = self.matrix.get_valid_operators(400)
        self.assertEqual(len(delta_ops), 4)
        self.assertIn(GraphicOperator.KNOT, delta_ops)
        
        # Sigma symbol should have 1 valid operator
        sigma_ops = self.matrix.get_valid_operators(410)
        self.assertEqual(len(sigma_ops), 1)
        self.assertEqual(sigma_ops[0], GraphicOperator.STACK)


class TestPairMatrix(unittest.TestCase):
    """Test the pair composition matrix"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
        self.matrix = PairMatrix(self.registry)
    
    def test_matrix_size(self):
        """Test that matrix has correct number of pairs"""
        self.assertEqual(len(self.matrix.pairs), 2025)  # 45²
    
    def test_statistics(self):
        """Test pair composition statistics"""
        stats = self.matrix.get_statistics()
        
        self.assertEqual(stats['total_pairs'], 2025)
        self.assertGreater(stats['composable_pairs'], 0)
        self.assertGreater(stats['non_composable_pairs'], 0)
        self.assertEqual(
            stats['composable_pairs'] + stats['non_composable_pairs'],
            2025
        )
    
    def test_composable_partners(self):
        """Test getting composable partners for symbols"""
        # Omega symbol (373) should have Delta and Sigma partners as second
        partners_first = self.matrix.get_composable_partners(373, 'first')
        self.assertGreater(len(partners_first), 0)
        # Should include some Delta symbols
        self.assertTrue(any(400 <= p <= 409 for p in partners_first))
        # Should include some Sigma symbols
        self.assertTrue(any(410 <= p <= 417 for p in partners_first))
        # Should not include other Omega symbols
        self.assertFalse(any(373 <= p <= 399 for p in partners_first))


class TestSequenceValidator(unittest.TestCase):
    """Test sequence validation"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
        self.pair_matrix = PairMatrix(self.registry)
        self.validator = SequenceValidator(
            self.registry, self.composition, self.pair_matrix
        )
    
    def test_empty_sequence(self):
        """Test that empty sequence is invalid"""
        valid, msg = self.validator.validate_sequence([])
        self.assertFalse(valid)
        self.assertIn("Empty", msg)
    
    def test_single_symbol(self):
        """Test that single symbol is valid"""
        valid, msg = self.validator.validate_sequence([373])
        self.assertTrue(valid)
    
    def test_valid_omega_delta_sequence(self):
        """Test valid Omega-Delta sequence"""
        valid, msg = self.validator.validate_sequence([373, 400])
        self.assertTrue(valid)
    
    def test_invalid_omega_omega_sequence(self):
        """Test invalid Omega-Omega sequence"""
        valid, msg = self.validator.validate_sequence([373, 374])
        self.assertFalse(valid)
        self.assertIn("not composable", msg)
    
    def test_valid_delta_chain(self):
        """Test valid Delta-Delta chain"""
        valid, msg = self.validator.validate_sequence([400, 401])
        self.assertTrue(valid)
    
    def test_invalid_symbol_in_sequence(self):
        """Test sequence with invalid symbol ID"""
        valid, msg = self.validator.validate_sequence([373, 999])
        self.assertFalse(valid)
        self.assertIn("not in registry", msg)
    
    def test_sequence_with_operators(self):
        """Test validation of sequences with operators"""
        # Valid: Omega symbol with Dot operator
        seq = [(373, GraphicOperator.DOT), (400, GraphicOperator.KNOT)]
        valid, msg = self.validator.validate_with_operators(seq)
        self.assertTrue(valid)
        
        # Invalid: Omega symbol with Knot operator
        seq = [(373, GraphicOperator.KNOT)]
        valid, msg = self.validator.validate_with_operators(seq)
        self.assertFalse(valid)
        self.assertIn("cannot be applied", msg)
    
    def test_generate_valid_sequences(self):
        """Test generating valid sequences"""
        # Generate sequences starting with Omega
        omega_seqs = self.validator.generate_valid_sequences(
            max_length=2, start_family=SymbolFamily.OMEGA
        )
        
        self.assertGreater(len(omega_seqs), 0)
        
        # All sequences should start with Omega symbols
        for seq in omega_seqs:
            if len(seq) > 0:
                self.assertGreaterEqual(seq[0], 373)
                self.assertLessEqual(seq[0], 399)


class TestTransitionAnalyzer(unittest.TestCase):
    """Test state transition analysis"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
        self.combination_matrix = CombinationMatrix(self.registry)
        self.pair_matrix = PairMatrix(self.registry)
        self.analyzer = TransitionAnalyzer(
            self.registry, self.combination_matrix, self.pair_matrix
        )
    
    def test_build_transition_graph(self):
        """Test building the transition graph"""
        self.analyzer.build_transition_graph()
        
        # Should have transitions for all symbols
        self.assertGreater(len(self.analyzer.transition_map), 0)
    
    def test_reachable_states(self):
        """Test finding reachable states"""
        reachable = self.analyzer.get_reachable_states(373, max_steps=2)
        
        self.assertGreater(len(reachable), 0)
        # Should include the starting symbol
        self.assertIn(373, reachable)
    
    def test_closure_properties(self):
        """Test closure property analysis"""
        closure = self.analyzer.analyze_closure_properties()
        
        # Should have results for all families
        self.assertIn('Ω', closure)
        self.assertIn('Δ', closure)
        self.assertIn('Σ', closure)
        
        # No family should be closed (all can reach outside)
        for family, props in closure.items():
            self.assertFalse(props['is_closed'])


class TestComprehensiveAnalysis(unittest.TestCase):
    """Test the comprehensive analysis function"""
    
    def test_comprehensive_analysis(self):
        """Test that comprehensive analysis returns all expected data"""
        analysis = create_comprehensive_analysis()
        
        # Check top-level keys
        self.assertIn('symbol_count', analysis)
        self.assertIn('operator_count', analysis)
        self.assertIn('combination_statistics', analysis)
        self.assertIn('pair_statistics', analysis)
        self.assertIn('closure_analysis', analysis)
        self.assertIn('sample_valid_sequences', analysis)
        
        # Check values
        self.assertEqual(analysis['symbol_count'], 45)
        self.assertEqual(analysis['operator_count'], 10)
        
        # Check combination statistics
        combo_stats = analysis['combination_statistics']
        self.assertEqual(combo_stats['total_combinations'], 450)
        
        # Check pair statistics
        pair_stats = analysis['pair_statistics']
        self.assertEqual(pair_stats['total_pairs'], 2025)
        
        # Check closure analysis
        closure = analysis['closure_analysis']
        self.assertEqual(len(closure), 3)  # Three families


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""
    
    def setUp(self):
        self.registry, self.composition = create_harappan_system()
    
    def test_boundary_symbols(self):
        """Test symbols at family boundaries"""
        # First Omega (373)
        self.assertEqual(
            self.registry.get_symbol(373).family,
            SymbolFamily.OMEGA
        )
        
        # Last Omega (399)
        self.assertEqual(
            self.registry.get_symbol(399).family,
            SymbolFamily.OMEGA
        )
        
        # First Delta (400)
        self.assertEqual(
            self.registry.get_symbol(400).family,
            SymbolFamily.DELTA
        )
        
        # Last Sigma (417)
        self.assertEqual(
            self.registry.get_symbol(417).family,
            SymbolFamily.SIGMA
        )
    
    def test_all_operators_covered(self):
        """Test that all operators are covered in at least one family"""
        matrix = CombinationMatrix(self.registry)
        
        for op in GraphicOperator:
            symbols = matrix.get_valid_symbols(op)
            self.assertGreater(
                len(symbols), 0,
                f"Operator {op.name} is not valid for any symbol"
            )


if __name__ == '__main__':
    unittest.main()
