"""
Site Comparison Example

Demonstrates cross-site stability analysis (supra-regional standardization).
"""

import sys
sys.path.append('..')

from src.indus_analysis import IndusSequenceAnalyzer

# Sequences with site labels
sequences = [
    # Harappa site
    ['jar', 'fish', 'man', 'closer'],
    ['jar', 'fish', 'star', 'closer'],
    ['jar', 'fish', 'man', 'closer'],
    ['unicorn', 'trough', 'closer'],
    
    # Mohenjo-daro site
    ['jar', 'fish', 'man', 'closer'],
    ['jar', 'fish', 'closer'],
    ['unicorn', 'trough', 'closer'],
    ['unicorn', 'trough', 'plant', 'closer'],
    
    # Dholavira site
    ['jar', 'fish', 'man', 'closer'],
    ['unicorn', 'trough', 'closer'],
    ['bull', 'man', 'closer'],
]

site_labels = [
    'Harappa', 'Harappa', 'Harappa', 'Harappa',
    'Mohenjo-daro', 'Mohenjo-daro', 'Mohenjo-daro', 'Mohenjo-daro',
    'Dholavira', 'Dholavira', 'Dholavira'
]

def main():
    print("=" * 60)
    print("Cross-Site Stability Analysis")
    print("=" * 60)
    print("\nTests for 'non-local invariance' = spatial invariance")
    print("(patterns stable across geographical sites)")
    print()
    
    # Initialize analyzer with site labels
    analyzer = IndusSequenceAnalyzer(sequences, site_labels)
    
    # Get top pairs
    top_pairs = analyzer.top_pmi_pairs(top_n=5)
    
    print("SITE STABILITY FOR TOP PAIRS")
    print("-" * 60)
    
    for i, (pair, global_pmi) in enumerate(top_pairs, 1):
        if global_pmi == float('-inf'):
            continue
            
        print(f"\n{i}. Pair: ({pair[0]}, {pair[1]})")
        print(f"   Global PMI: {global_pmi:.2f}")
        print()
        
        # Get PMI for each site
        site_pmis = analyzer.site_stability(pair)
        
        if not site_pmis:
            print("   No data across sites")
            continue
        
        print("   Site-specific PMI:")
        for site, pmi in sorted(site_pmis.items()):
            print(f"     {site:15s}: {pmi:6.2f}")
        
        # Calculate stability (coefficient of variation)
        import numpy as np
        values = list(site_pmis.values())
        mean_pmi = np.mean(values)
        std_pmi = np.std(values)
        cv = std_pmi / mean_pmi if mean_pmi != 0 else 0
        
        print(f"\n   Stability metrics:")
        print(f"     Mean PMI: {mean_pmi:.2f}")
        print(f"     Std Dev: {std_pmi:.2f}")
        print(f"     CV (coefficient of variation): {cv:.2f}")
        
        if cv < 0.3:
            print(f"     → LOW variance: STABLE across sites")
            print(f"     → Evidence of supra-regional standardization")
        else:
            print(f"     → HIGH variance: site-specific pattern")
    
    print("\n" + "=" * 60)
    print("Interpretation:")
    print("=" * 60)
    print("Low CV = 'Non-local invariance' = Distributed standardization")
    print("NOT quantum non-locality, but spatial pattern stability")
    print()
    print("This suggests institutional protocols shared across")
    print("the Indus civilization's geographical extent.")

if __name__ == "__main__":
    main()
