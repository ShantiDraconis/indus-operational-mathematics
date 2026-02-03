"""
Unit tests for comparative distribution analysis.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from analysis.compare_distributions import compare_distributions, analyze_operator_efficiency


class TestCompareDistributions(unittest.TestCase):
    
    def setUp(self):
        """Set up test data."""
        self.harappa_data = {
            f'symbol_{i}': freq 
            for i, freq in enumerate([100, 50, 33, 25, 20, 16, 14, 12, 11, 10], 1)
        }
        
        self.youtube_data = {
            f'video_{i}': freq 
            for i, freq in enumerate([95, 48, 35, 24, 19, 15, 13, 11, 10, 9], 1)
        }
    
    def test_compare_distributions(self):
        """Test distribution comparison."""
        result = compare_distributions(self.harappa_data, self.youtube_data)
        
        self.assertIn('harappa', result)
        self.assertIn('youtube', result)
        self.assertIn('comparison', result)
        
        # Check comparison metrics
        comp = result['comparison']
        self.assertIn('isomorphism_score', comp)
        self.assertIn('structural_similarity', comp)
        
        # Score should be between 0 and 100
        self.assertGreaterEqual(comp['isomorphism_score'], 0)
        self.assertLessEqual(comp['isomorphism_score'], 100)
    
    def test_operator_efficiency(self):
        """Test operator efficiency analysis."""
        result = analyze_operator_efficiency(self.harappa_data, top_k=5)
        
        self.assertIn('top_k', result)
        self.assertIn('top_k_coverage', result)
        self.assertIn('compression_ratio', result)
        self.assertIn('efficiency_score', result)
        
        # Coverage should be reasonable
        self.assertGreater(result['top_k_coverage'], 30)
        self.assertLessEqual(result['top_k_coverage'], 100)


if __name__ == '__main__':
    unittest.main()
