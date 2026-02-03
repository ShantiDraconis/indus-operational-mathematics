"""
Basic Analysis Example

Demonstrates frequency ranking, PMI calculation, and cluster detection.
"""

import sys
sys.path.append('..')

from src.indus_analysis import IndusSequenceAnalyzer

# Example sequences (simplified representation of Indus seals)
# In real usage, these would come from archaeological data
sequences = [
    ['jar', 'fish', 'man', 'closer'],
    ['jar', 'fish', 'star', 'closer'],
    ['jar', 'fish', 'man', 'closer'],
    ['unicorn', 'trough', 'closer'],
    ['unicorn', 'trough', 'closer'],
    ['bull', 'man', 'closer'],
    ['jar', 'fish', 'closer'],
    ['unicorn', 'trough', 'plant', 'closer'],
]

def main():
    print("=" * 60)
    print("Indus Script Basic Analysis")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = IndusSequenceAnalyzer(sequences)
    
    # 1. Frequency ranking
    print("\n1. FREQUENCY RANKING")
    print("-" * 60)
    frequencies = analyzer.frequency_ranking(top_n=10)
    for symbol, count, freq in frequencies:
        print(f"  {symbol:15s}: {count:3d} occurrences ({freq:.1%})")
    
    # 2. Top PMI pairs (stable clusters)
    print("\n2. TOP PMI PAIRS (Stable Clusters)")
    print("-" * 60)
    print("High PMI = strong association between symbols")
    print()
    top_pairs = analyzer.top_pmi_pairs(top_n=10)
    for (a, b), pmi in top_pairs:
        if pmi > float('-inf'):
            print(f"  ({a:10s}, {b:10s}): PMI = {pmi:6.2f}")
    
    # 3. Cluster detection
    print("\n3. DETECTED CLUSTERS")
    print("-" * 60)
    print("Symbols that frequently co-occur (PMI-based)")
    print()
    clusters = analyzer.detect_clusters(min_pmi=1.0, min_support=2)
    for i, cluster in enumerate(clusters, 1):
        print(f"  Cluster {i}: {cluster}")
    
    # 4. Compression metrics
    print("\n4. INFORMATION-THEORETIC METRICS")
    print("-" * 60)
    print("'Holographic principle' as information compression:")
    print()
    metrics = analyzer.compression_metrics()
    print(f"  Entropy: {metrics['entropy']:.2f} bits/symbol")
    print(f"  Max entropy: {metrics['max_entropy']:.2f} bits/symbol")
    print(f"  Redundancy: {metrics['redundancy']:.1%}")
    print(f"  Avg sequence length: {metrics['avg_sequence_length']:.1f} symbols")
    print(f"  Compression ratio: {metrics['compression_ratio']:.2f}x")
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)
    print("\nNOTE: We use 'non-local invariance' and 'entanglement' as")
    print("statistical terms, NOT as claims of physical quantum processes.")

if __name__ == "__main__":
    main()
