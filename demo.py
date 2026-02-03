#!/usr/bin/env python3
"""
Comprehensive Demo of Indus Operational Mathematics Framework

This demonstrates all major features with sample data.

CRITICAL DISCLAIMER: All "quantum" and "non-locality" terminology
refers to STATISTICAL measures, NOT quantum mechanical phenomena.
"""

import sys
sys.path.insert(0, 'python')

from indus_analysis import Symbol, Sequence, IndusStatisticalAnalysis
from indus_analysis import TensorNetworkModel, compute_top_correlations

def print_section(title):
    """Print formatted section header"""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def main():
    print_section("INDUS OPERATIONAL MATHEMATICS FRAMEWORK - DEMONSTRATION")
    
    print("\n⚠️  IMPORTANT DISCLAIMER:")
    print("All 'non-locality' and 'entanglement' terminology refers to")
    print("STATISTICAL correlations, NOT quantum mechanical phenomena.")
    print()
    
    # Create sample symbols
    print_section("1. Creating Sample Symbols")
    symbols = {
        1: Symbol(1, 'numeric', 'numeral_1'),
        2: Symbol(2, 'pictographic', 'unicorn'),
        3: Symbol(3, 'abstract', 'geometric_3'),
        4: Symbol(4, 'numeric', 'numeral_4'),
        5: Symbol(5, 'pictographic', 'fish'),
        6: Symbol(6, 'abstract', 'geometric_6'),
    }
    
    print(f"Created {len(symbols)} symbols:")
    for s in symbols.values():
        print(f"  - Symbol {s.id}: {s.category} ({s.name})")
    
    # Create sample sequences from different sites
    print_section("2. Creating Sample Sequences (Archaeological Sites)")
    sequences = [
        # Harappa
        Sequence([symbols[1], symbols[2], symbols[3]], 'Harappa', 'seal'),
        Sequence([symbols[1], symbols[2], symbols[4]], 'Harappa', 'seal'),
        Sequence([symbols[2], symbols[5], symbols[3]], 'Harappa', 'pottery'),
        
        # Mohenjo-daro
        Sequence([symbols[2], symbols[3], symbols[1]], 'Mohenjo-daro', 'seal'),
        Sequence([symbols[1], symbols[2], symbols[5]], 'Mohenjo-daro', 'seal'),
        Sequence([symbols[2], symbols[6], symbols[3]], 'Mohenjo-daro', 'tablet'),
        
        # Dholavira
        Sequence([symbols[1], symbols[2], symbols[3], symbols[4]], 'Dholavira', 'tablet'),
        Sequence([symbols[2], symbols[3]], 'Dholavira', 'seal'),
        
        # Lothal
        Sequence([symbols[1], symbols[2]], 'Lothal', 'seal'),
        Sequence([symbols[2], symbols[3], symbols[1]], 'Lothal', 'seal'),
    ]
    
    print(f"Created {len(sequences)} sequences from 4 sites:")
    sites = {}
    for seq in sequences:
        sites[seq.site] = sites.get(seq.site, 0) + 1
    for site, count in sites.items():
        print(f"  - {site}: {count} sequences")
    
    # Initialize analyzer
    print_section("3. Statistical Analysis")
    analyzer = IndusStatisticalAnalysis(sequences)
    
    print("\n3.1 Pointwise Mutual Information (PMI)")
    print("PMI measures statistical association between symbol pairs.")
    print("Positive = co-occur more than expected by chance\n")
    
    test_pairs = [(1, 2), (2, 3), (1, 3)]
    for s1_id, s2_id in test_pairs:
        pmi = analyzer.pmi(symbols[s1_id], symbols[s2_id])
        print(f"  PMI(s{s1_id}, s{s2_id}) = {pmi:7.4f}", end="")
        if pmi > 1.0:
            print("  ← Strong association")
        elif pmi > 0:
            print("  ← Weak association")
        else:
            print()
    
    print("\n3.2 Lift (Odds Ratio)")
    print("Lift > 1 means symbols co-occur more than expected\n")
    
    for s1_id, s2_id in test_pairs:
        lift = analyzer.lift(symbols[s1_id], symbols[s2_id])
        print(f"  Lift(s{s1_id}, s{s2_id}) = {lift:7.4f}")
    
    print("\n3.3 Cross-Site Variance (Non-Local Invariance)")
    print("LOW variance = HIGH standardization = distributed pattern")
    print("This is STATISTICAL 'non-locality', not quantum!\n")
    
    for s1_id, s2_id in test_pairs:
        variance = analyzer.cross_site_variance(symbols[s1_id], symbols[s2_id])
        print(f"  Variance(s{s1_id}, s{s2_id}) = {variance:7.4f}", end="")
        if variance < 0.5:
            print("  ← Stable across sites (non-local invariant)")
        else:
            print("  ← Varies by site")
    
    print("\n3.4 Positional Dependencies")
    print("Distance preferences reveal grammatical constraints\n")
    
    dist_hist = analyzer.positional_dependency(symbols[1], symbols[2])
    if dist_hist:
        print("  Distance histogram for symbols (1, 2):")
        for dist, count in sorted(dist_hist.items())[:5]:
            bar = "█" * count
            print(f"    Distance {dist}: {bar} ({count})")
    
    # Find stable clusters
    print_section("4. Finding 'Entangled' Clusters")
    print("These are symbol pairs with:")
    print("  - High PMI (strong correlation)")
    print("  - Low cross-site variance (distributed standardization)")
    print("\n'Entangled' is a STATISTICAL metaphor, not quantum entanglement!\n")
    
    clusters = analyzer.find_stable_clusters(min_pmi=0.5, max_variance=1.0)
    
    if clusters:
        print(f"Found {len(clusters)} stable clusters:\n")
        for i, (s1, s2, pmi, var) in enumerate(clusters[:5], 1):
            print(f"  {i}. Symbols ({s1.id}, {s2.id}):")
            print(f"     PMI = {pmi:.4f}, Variance = {var:.4f}")
            print(f"     Interpretation: Strong correlation, stable across sites")
    else:
        print("No clusters found (adjust thresholds)")
    
    # Regime classification
    print_section("5. Institutional vs Ritual Classification")
    print("Classify sequences based on features:\n")
    
    for i, seq in enumerate(sequences[:3], 1):
        result = analyzer.institutional_vs_ritual_classification(seq)
        print(f"  Sequence {i}: {[s.id for s in seq.symbols]}")
        print(f"    Site: {seq.site}, Type: {seq.artifact_type}")
        print(f"    Administrative: {result['administrative']:.1%}")
        print(f"    Ritual:         {result['ritual']:.1%}")
        print()
    
    # Tensor network analysis
    print_section("6. Tensor Network Analysis")
    print("Using tensor factorization to model correlations")
    print("(CLASSICAL tensor networks, not quantum!)\n")
    
    # Convert to numeric sequences
    numeric_seqs = [[s.id for s in seq.symbols] for seq in sequences]
    
    model = TensorNetworkModel(max_symbol_id=7, max_sequence_length=5)
    tensor = model.build_correlation_tensor(numeric_seqs)
    
    print(f"  Correlation tensor shape: {tensor.shape}")
    print(f"  Tensor density: {(tensor > 0).sum() / tensor.size:.2%}")
    print(f"  (Proportion of non-zero entries)")
    
    # Top correlations
    print_section("7. Top Correlations Summary")
    results = compute_top_correlations(sequences, top_n=5)
    
    print("\nTop 5 symbol pairs by PMI:\n")
    for i, result in enumerate(results[:5], 1):
        print(f"  {i}. Symbols ({result['symbol1']}, {result['symbol2']}):")
        print(f"     PMI: {result['pmi']:.4f}")
        print(f"     MI:  {result['mutual_information']:.4f} bits")
        print(f"     Variance: {result['cross_site_variance']:.4f}")
        stable = "Yes (non-local invariant)" if result['is_stable_cluster'] else "No"
        print(f"     Stable: {stable}")
        print()
    
    # Conclusion
    print_section("8. Conclusion")
    print("""
This framework provides:

✓ Rigorous statistical measures (PMI, MI, Lift)
✓ Cross-site analysis (distributed standardization)
✓ Formal mathematical definitions (Lean, Coq, Isabelle, Agda)
✓ High-performance implementation (C++)
✓ Complete transparency about terminology

KEY REMINDERS:
• "Non-locality" = spatial distribution of patterns
• "Entanglement" = strong statistical correlation
• "Quantum" = metaphor for discrete state systems

NO quantum mechanical phenomena are claimed in artifacts.

This is scientifically rigorous archaeology + statistics.
    """)
    
    print("\n" + "=" * 70)
    print("Demo complete. See docs/ for full documentation.")
    print("=" * 70)

if __name__ == '__main__':
    main()
