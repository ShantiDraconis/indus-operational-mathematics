"""
Unit tests for Zipf analysis module.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from analysis.zipf_analysis import ZipfAnalyzer
import numpy as np


class TestZipfAnalyzer(unittest.TestCase):
    
    def setUp(self):
        """Set up test data."""
        # Create a known Zipfian distribution
        self.zipf_data = [100, 50, 33, 25, 20, 16, 14, 12, 11, 10,
                         9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        self.analyzer = ZipfAnalyzer()
    
    def test_fit_zipf(self):
        """Test fitting Zipf distribution."""
        result = self.analyzer.fit(self.zipf_data)
        
        self.assertIn('zipf_exponent', result)
        self.assertIn('r_squared', result)
        self.assertIn('p_value', result)
        
        # Zipf exponent should be around 1.0 for ideal Zipf
        self.assertGreater(result['zipf_exponent'], 0.5)
        self.assertLess(result['zipf_exponent'], 2.0)
        
        # R² should be high for good fit
        self.assertGreater(result['r_squared'], 0.7)
    
    def test_top_k_concentration(self):
        """Test top-k concentration calculation."""
        self.analyzer.fit(self.zipf_data)
        
        concentration = self.analyzer.get_top_k_concentration(10)
        
        self.assertGreater(concentration, 0)
        self.assertLessEqual(concentration, 100)
        
        # Top 10 should account for significant portion
        self.assertGreater(concentration, 50)
    
    def test_classify_distribution(self):
        """Test distribution classification."""
        self.analyzer.fit(self.zipf_data)
        
        classification = self.analyzer.classify_distribution()
        
        self.assertEqual(len(classification), 3)
        self.assertIn('Class A', classification[0])
        self.assertIn('Class B', classification[1])
        self.assertIn('Class C', classification[2])
    
    def test_calculate_entropy(self):
        """Test entropy calculation."""
        self.analyzer.fit(self.zipf_data)
        
        entropy = self.analyzer.calculate_entropy()
        
        self.assertGreater(entropy, 0)
        # Entropy should be less than log2(n) for skewed distribution
        max_entropy = np.log2(len(self.zipf_data))
        self.assertLess(entropy, max_entropy)
    
    def test_summary_statistics(self):
        """Test summary statistics."""
        self.analyzer.fit(self.zipf_data)
        
        stats = self.analyzer.get_summary_statistics()
        
        required_keys = ['total_items', 'total_frequency', 'max_frequency',
                        'entropy', 'top_10_concentration', 'zipf_exponent']
        
        for key in required_keys:
            self.assertIn(key, stats)


if __name__ == '__main__':
    unittest.main()
