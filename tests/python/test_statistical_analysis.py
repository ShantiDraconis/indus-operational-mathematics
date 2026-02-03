"""
Unit tests for Indus Statistical Analysis
"""

import pytest
import numpy as np
from indus_analysis import Symbol, Sequence, IndusStatisticalAnalysis


class TestSymbol:
    def test_symbol_creation(self):
        sym = Symbol(1, 'numeric', 'test')
        assert sym.id == 1
        assert sym.category == 'numeric'
        assert sym.name == 'test'
    
    def test_symbol_hash(self):
        sym1 = Symbol(1, 'numeric', 'test')
        sym2 = Symbol(1, 'numeric', 'test')
        assert hash(sym1) == hash(sym2)


class TestSequence:
    def test_sequence_creation(self):
        s1 = Symbol(1, 'numeric')
        s2 = Symbol(2, 'pictographic')
        seq = Sequence([s1, s2], 'TestSite', 'seal')
        
        assert len(seq) == 2
        assert seq.site == 'TestSite'
        assert seq.artifact_type == 'seal'


class TestIndusStatisticalAnalysis:
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing"""
        s1 = Symbol(1, 'numeric', 'symbol_1')
        s2 = Symbol(2, 'pictographic', 'unicorn')
        s3 = Symbol(3, 'abstract', 'symbol_3')
        
        sequences = [
            Sequence([s1, s2, s3], 'Harappa', 'seal'),
            Sequence([s1, s2], 'Harappa', 'seal'),
            Sequence([s2, s3], 'Mohenjo-daro', 'seal'),
            Sequence([s1, s2, s3], 'Dholavira', 'tablet'),
        ]
        
        return sequences, (s1, s2, s3)
    
    def test_initialization(self, sample_data):
        sequences, _ = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        assert analyzer.sequences == sequences
        assert len(analyzer.symbol_freq) > 0
    
    def test_pmi_computation(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        # PMI should be a finite number
        pmi = analyzer.pmi(s1, s2)
        assert not np.isinf(pmi)
        
        # PMI is symmetric
        pmi_12 = analyzer.pmi(s1, s2)
        pmi_21 = analyzer.pmi(s2, s1)
        assert abs(pmi_12 - pmi_21) < 1e-10
    
    def test_mutual_information(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        mi = analyzer.mutual_information(s1, s2)
        
        # MI should be non-negative
        assert mi >= 0
        
        # MI is symmetric
        mi_12 = analyzer.mutual_information(s1, s2)
        mi_21 = analyzer.mutual_information(s2, s1)
        assert abs(mi_12 - mi_21) < 1e-10
    
    def test_lift_computation(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        lift = analyzer.lift(s1, s2)
        
        # Lift should be positive
        assert lift >= 0
        
        # Lift is symmetric
        lift_12 = analyzer.lift(s1, s2)
        lift_21 = analyzer.lift(s2, s1)
        assert abs(lift_12 - lift_21) < 1e-10
    
    def test_positional_dependency(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        dist_hist = analyzer.positional_dependency(s1, s2)
        
        # Should return a dictionary
        assert isinstance(dist_hist, dict)
        
        # All distances should be non-negative integers
        for dist, count in dist_hist.items():
            assert dist >= 0
            assert count > 0
    
    def test_cross_site_variance(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        variance = analyzer.cross_site_variance(s1, s2)
        
        # Variance should be non-negative
        assert variance >= 0
    
    def test_find_stable_clusters(self, sample_data):
        sequences, (s1, s2, s3) = sample_data
        analyzer = IndusStatisticalAnalysis(sequences)
        
        clusters = analyzer.find_stable_clusters(min_pmi=-5.0, max_variance=10.0)
        
        # Should return a list
        assert isinstance(clusters, list)
        
        # Each cluster should have 4 elements
        for cluster in clusters:
            assert len(cluster) == 4
            sym1, sym2, pmi, var = cluster
            assert isinstance(sym1, Symbol)
            assert isinstance(sym2, Symbol)
            assert isinstance(pmi, float)
            assert isinstance(var, float)


class TestStatisticalProperties:
    """Test that statistical measures have correct mathematical properties"""
    
    def test_pmi_symmetry(self):
        """PMI should be symmetric: PMI(x,y) = PMI(y,x)"""
        s1 = Symbol(1, 'numeric')
        s2 = Symbol(2, 'numeric')
        
        sequences = [
            Sequence([s1, s2], 'Site1', 'seal'),
            Sequence([s2, s1], 'Site2', 'seal'),
        ]
        
        analyzer = IndusStatisticalAnalysis(sequences)
        
        pmi_12 = analyzer.pmi(s1, s2)
        pmi_21 = analyzer.pmi(s2, s1)
        
        assert abs(pmi_12 - pmi_21) < 1e-10
    
    def test_lift_range(self):
        """Lift should be >= 0"""
        s1 = Symbol(1, 'numeric')
        s2 = Symbol(2, 'numeric')
        
        sequences = [
            Sequence([s1, s2], 'Site1', 'seal'),
        ]
        
        analyzer = IndusStatisticalAnalysis(sequences)
        lift = analyzer.lift(s1, s2)
        
        assert lift >= 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
