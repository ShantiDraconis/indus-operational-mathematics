"""
Example: Quantum Symbol Analysis

This example demonstrates how to use the quantum archaeology framework
to analyze Indus script symbols and their correlations.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_archaeology import Symbol, SymbolCorpus, EntanglementAnalyzer, HolographicAnalyzer
from quantum_archaeology.symbol_system import Inscription, SymbolContext, Location
from quantum_archaeology.visualization import QuantumNetworkVisualizer


def create_sample_corpus():
    """Create a sample corpus of Indus script symbols and inscriptions."""
    
    corpus = SymbolCorpus()
    
    # Add some example symbols (these are simplified representations)
    symbols = [
        Symbol("U+01", "Unicorn", "Unicorn-like creature, very common", potential_meanings=["authority", "trade marker"]),
        Symbol("U+02", "Fish", "Fish symbol", potential_meanings=["water", "abundance", "trade"]),
        Symbol("U+03", "Jar", "Storage vessel", potential_meanings=["storage", "goods", "quantity"]),
        Symbol("U+04", "Comb", "Comb-like symbol", potential_meanings=["textile", "crafts"]),
        Symbol("U+05", "Intersecting-circles", "Two intersecting circles", potential_meanings=["unity", "duality", "exchange"]),
        Symbol("U+06", "Man", "Human figure", potential_meanings=["person", "owner", "authority"]),
        Symbol("U+07", "Tree", "Plant or tree", potential_meanings=["nature", "growth", "agriculture"]),
        Symbol("U+08", "Bird", "Bird symbol", potential_meanings=["messenger", "sky", "freedom"]),
        Symbol("U+09", "Wheel", "Wheel or circle with spokes", potential_meanings=["movement", "time", "cosmic order"]),
        Symbol("U+10", "Triangle", "Triangular symbol", potential_meanings=["mountain", "stability", "hierarchy"]),
    ]
    
    for symbol in symbols:
        corpus.add_symbol(symbol)
    
    # Add sample inscriptions from different locations
    inscriptions = [
        # Mohenjo-daro administrative seals
        Inscription("M-001", [symbols[0], symbols[2], symbols[4]], Location.MOHENJO_DARO, SymbolContext.ADMINISTRATIVE,
                   "Found on clay seal, administrative quarter"),
        Inscription("M-002", [symbols[0], symbols[1], symbols[2]], Location.MOHENJO_DARO, SymbolContext.TRADE,
                   "Seal found near granary"),
        Inscription("M-003", [symbols[5], symbols[3], symbols[4]], Location.MOHENJO_DARO, SymbolContext.ADMINISTRATIVE,
                   "Personal seal"),
        Inscription("M-004", [symbols[0], symbols[2], symbols[4], symbols[1]], Location.MOHENJO_DARO, SymbolContext.ADMINISTRATIVE,
                   "Complex administrative seal"),
        
        # Harappa seals
        Inscription("H-001", [symbols[0], symbols[2], symbols[4]], Location.HARAPPA, SymbolContext.ADMINISTRATIVE,
                   "Identical to M-001, showing standardization"),
        Inscription("H-002", [symbols[1], symbols[3], symbols[6]], Location.HARAPPA, SymbolContext.TRADE,
                   "Trade marker"),
        Inscription("H-003", [symbols[7], symbols[8], symbols[9]], Location.HARAPPA, SymbolContext.RITUAL,
                   "Found in ritual context"),
        
        # Dholavira
        Inscription("D-001", [symbols[0], symbols[4], symbols[2]], Location.DHOLAVIRA, SymbolContext.ADMINISTRATIVE,
                   "Similar pattern to M-001"),
        Inscription("D-002", [symbols[8], symbols[9], symbols[7]], Location.DHOLAVIRA, SymbolContext.RITUAL,
                   "Ritual inscription on pottery"),
        
        # Lothal (port city)
        Inscription("L-001", [symbols[1], symbols[2], symbols[0]], Location.LOTHAL, SymbolContext.TRADE,
                   "Port-related seal"),
        Inscription("L-002", [symbols[1], symbols[1], symbols[2]], Location.LOTHAL, SymbolContext.TRADE,
                   "Repeated fish symbol - quantity marker?"),
        
        # More complex inscriptions
        Inscription("M-005", [symbols[0], symbols[5], symbols[2], symbols[4], symbols[1], symbols[3]], 
                   Location.MOHENJO_DARO, SymbolContext.ADMINISTRATIVE,
                   "Very complex seal, high information density"),
        Inscription("H-004", [symbols[8], symbols[9], symbols[0], symbols[4]], Location.HARAPPA, SymbolContext.RITUAL,
                   "Ritual seal combining cosmic and authority symbols"),
    ]
    
    for inscription in inscriptions:
        corpus.add_inscription(inscription)
    
    return corpus


def main():
    """Main analysis function."""
    
    print("=" * 80)
    print("QUANTUM ARCHAEOLOGY: Indus Script Analysis Example")
    print("=" * 80)
    print()
    
    # Create corpus
    print("Creating sample corpus...")
    corpus = create_sample_corpus()
    stats = corpus.get_corpus_statistics()
    
    print(f"\nCorpus loaded:")
    print(f"  - {stats['total_symbols']} unique symbols")
    print(f"  - {stats['total_inscriptions']} inscriptions")
    print(f"  - {stats['locations']} different locations")
    print(f"  - Average inscription length: {stats['average_inscription_length']:.1f} symbols")
    
    # Create analyzers
    print("\n" + "=" * 80)
    print("ENTANGLEMENT ANALYSIS")
    print("=" * 80)
    
    analyzer = EntanglementAnalyzer(corpus)
    
    # Analyze specific symbol
    print("\nAnalyzing the Unicorn symbol (most common)...")
    unicorn_analysis = analyzer.analyze_symbol_superposition("U+01")
    
    print(f"\nUnicorn Symbol Analysis:")
    print(f"  Total occurrences: {unicorn_analysis['total_occurrences']}")
    print(f"  Entanglement entropy: {unicorn_analysis['entanglement_entropy']:.3f}")
    print(f"  Non-locality index: {unicorn_analysis['non_locality_index']:.3f}")
    print(f"\n  Context probabilities:")
    for context, prob in unicorn_analysis['context_probabilities'].items():
        print(f"    {context}: {prob:.2%}")
    print(f"\n  Location distribution:")
    for loc, prob in unicorn_analysis['location_probabilities'].items():
        print(f"    {loc}: {prob:.2%}")
    
    # Calculate mutual information between symbols
    print("\n" + "-" * 80)
    print("Symbol Pair Correlations (Mutual Information):")
    print("-" * 80)
    
    important_pairs = [
        ("U+01", "U+02", "Unicorn-Fish"),
        ("U+01", "U+03", "Unicorn-Jar"),
        ("U+01", "U+05", "Unicorn-Intersecting-circles"),
        ("U+08", "U+09", "Bird-Wheel"),
    ]
    
    for sid1, sid2, name in important_pairs:
        mi = analyzer.calculate_mutual_information(sid1, sid2)
        print(f"  {name:35} MI = {mi:.4f}")
    
    # Find entangled clusters
    print("\n" + "-" * 80)
    print("Entangled Symbol Clusters:")
    print("-" * 80)
    
    clusters = analyzer.find_entangled_clusters(min_correlation=0.2)
    for i, cluster in enumerate(clusters, 1):
        cluster_names = [corpus.get_symbol(sid).name for sid in cluster]
        print(f"  Cluster {i}: {', '.join(cluster_names)}")
    
    # Holographic analysis
    print("\n" + "=" * 80)
    print("HOLOGRAPHIC ANALYSIS")
    print("=" * 80)
    
    holo_analyzer = HolographicAnalyzer(corpus)
    
    print("\nIdentifying holographic patterns (sequences appearing across contexts)...")
    holo_patterns = holo_analyzer.identify_holographic_patterns()
    
    print(f"\nFound {len(holo_patterns['holographic_sequences'])} holographic sequences")
    print("\nTop holographic sequences:")
    for i, seq in enumerate(holo_patterns['holographic_sequences'][:5], 1):
        print(f"\n  {i}. Sequence: {seq['sequence']}")
        print(f"     Contexts: {', '.join(seq['contexts'])}")
        print(f"     Locations: {', '.join(seq['locations'])}")
        print(f"     Context diversity: {seq['context_diversity']}, Location diversity: {seq['location_diversity']}")
    
    # Analyze specific inscription
    print("\n" + "-" * 80)
    print("Detailed Inscription Analysis:")
    print("-" * 80)
    
    inscription = corpus.inscriptions[11]  # The complex one
    insc_analysis = holo_analyzer.analyze_institutional_encoding(inscription)
    
    print(f"\nInscription: {inscription.id}")
    print(f"  Location: {insc_analysis['location']}")
    print(f"  Context: {insc_analysis['context']}")
    print(f"  Length: {insc_analysis['length']} symbols")
    print(f"  Information density: {insc_analysis['information_density']:.3f}")
    print(f"  Holographic score: {insc_analysis['holographic_score']:.3f}")
    print(f"  Institutional inference: {insc_analysis['institutional_inference']}")
    
    # Visualization
    print("\n" + "=" * 80)
    print("NETWORK VISUALIZATION")
    print("=" * 80)
    
    visualizer = QuantumNetworkVisualizer(corpus, analyzer)
    
    # ASCII network for Unicorn symbol
    network = visualizer.generate_ascii_network("U+01", max_neighbors=5)
    print(network)
    
    # Generate full report
    print("\n" + "=" * 80)
    print("COMPREHENSIVE CORRELATION REPORT")
    print("=" * 80)
    
    report = analyzer.generate_correlation_report()
    
    print(f"\nAverage entanglement entropy: {report['average_entanglement_entropy']:.3f}")
    
    print("\nMost entangled symbols:")
    for symbol_id, entropy in report['most_entangled_symbols']:
        symbol = corpus.get_symbol(symbol_id)
        print(f"  {symbol.name:25} Entropy: {entropy:.3f}")
    
    print("\nStrongest correlations:")
    for sid1, sid2, mi in report['strongest_correlations'][:5]:
        s1 = corpus.get_symbol(sid1)
        s2 = corpus.get_symbol(sid2)
        print(f"  {s1.name:15} <-> {s2.name:15}  MI: {mi:.4f}")
    
    # Save network data
    print("\n" + "=" * 80)
    print("Exporting visualization data...")
    visualizer.export_to_json("symbol_network.json", min_correlation=0.1)
    print("  ✓ Saved to symbol_network.json")
    
    print("\n" + "=" * 80)
    print("Analysis complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
