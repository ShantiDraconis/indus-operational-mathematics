"""
Unit tests for Symbolic Activation Theorem.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.symbolic_activation import SymbolicActivationTheorem


class TestSymbolicActivationTheorem(unittest.TestCase):
    
    def setUp(self):
        """Set up test data."""
        # Create a more realistic Zipfian distribution
        self.zipf_data = [482, 391, 332, 287, 245, 198, 176, 154, 142, 128,
                         98, 87, 76, 68, 59, 52, 47, 43, 39, 36]
        self.uniform_data = [10] * 20
    
    def test_validate_system(self):
        """Test system validation."""
        result = SymbolicActivationTheorem.validate_system(self.zipf_data)
        
        self.assertIn('is_activation_system', result)
        self.assertIn('validation', result)
        self.assertIn('metrics', result)
        
        # Zipfian data should be validated as activation system
        self.assertTrue(result['is_activation_system'])
    
    def test_validate_non_zipfian(self):
        """Test validation of non-Zipfian system."""
        result = SymbolicActivationTheorem.validate_system(self.uniform_data)
        
        # Uniform data should not be activation system
        self.assertFalse(result['is_activation_system'])
    
    def test_compare_systems(self):
        """Test system comparison."""
        # Use similar realistic data
        similar_data = [450, 380, 320, 270, 240, 190, 170, 150, 138, 125,
                       95, 85, 74, 66, 57, 50, 45, 41, 37, 35]
        
        result = SymbolicActivationTheorem.compare_systems(
            self.zipf_data,
            similar_data,
            "System1",
            "System2"
        )
        
        self.assertIn('are_isomorphic', result)
        self.assertIn('isomorphism_score', result)
        self.assertIn('conclusion', result)
        
        # Similar Zipfian distributions should have good isomorphism score
        self.assertGreater(result['isomorphism_score'], 60)
    
    def test_activation_law(self):
        """Test activation law statement."""
        law = SymbolicActivationTheorem.activation_law()
        
        self.assertIsInstance(law, str)
        self.assertIn('SYMBOLIC ACTIVATION', law)
        self.assertIn('Zipfian', law)


if __name__ == '__main__':
    unittest.main()
