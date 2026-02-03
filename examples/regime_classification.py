"""
Regime Classification Example

Demonstrates administrative vs ritual regime classification using mixture model.
"""

import sys
sys.path.append('..')

from src.institutional_framework import InstitutionalRegimeClassifier

# Define symbol sets
pictogram_symbols = {'unicorn', 'bull', 'fish', 'elephant', 'tiger', 'jar'}
closer_symbols = {'closer', 'X', 'seal_mark'}

# Example sequences with object types
sequences = [
    # Administrative (short, repetitive, has closer)
    ['mark1', 'mark2', 'closer'],
    ['mark1', 'mark1', 'closer'],
    ['mark2', 'mark3', 'closer'],
    
    # Ritual/symbolic (pictograms, longer, more varied)
    ['unicorn', 'trough', 'plant', 'star', 'fish'],
    ['bull', 'jar', 'man', 'tree', 'symbol'],
    ['elephant', 'tiger', 'fish', 'vessel'],
    
    # Mixed
    ['jar', 'mark1', 'closer'],
    ['unicorn', 'mark1', 'mark2', 'closer'],
]

object_types = [
    'seal', 'seal', 'seal',  # Administrative
    'pottery', 'amulet', 'pottery',  # Ritual
    'tablet', 'seal'  # Mixed
]

def main():
    print("=" * 60)
    print("Institutional Regime Classification")
    print("=" * 60)
    print("\nMixture Model: P(seq) = π_A * P_A(seq) + π_B * P_B(seq)")
    print("  Regime A: Administrative")
    print("  Regime B: Ritual/Symbolic")
    print()
    
    # Initialize classifier
    classifier = InstitutionalRegimeClassifier(
        pictogram_symbols=pictogram_symbols,
        closer_symbols=closer_symbols
    )
    
    # Classify sequences
    print("CLASSIFICATION RESULTS")
    print("-" * 60)
    
    for i, (seq, obj_type) in enumerate(zip(sequences, object_types), 1):
        regime, confidence = classifier.classify(seq, obj_type)
        
        # Get features
        features = classifier.extract_features(seq, obj_type)
        
        print(f"\n{i}. Sequence: {seq}")
        print(f"   Object type: {obj_type}")
        print(f"   Length: {features.sequence_length}")
        print(f"   Has closer: {features.has_closer}")
        print(f"   Has pictogram: {features.has_pictogram}")
        print(f"   Repetition: {features.repetition_score:.2f}")
        print(f"   → Classification: {regime.upper()} (confidence: {confidence:.1%})")
    
    # Batch statistics
    print("\n" + "=" * 60)
    print("REGIME STATISTICS")
    print("=" * 60)
    
    stats = classifier.regime_statistics(sequences, object_types)
    
    for regime, metrics in stats.items():
        print(f"\n{regime.upper()} regime:")
        print(f"  Count: {metrics['count']}")
        print(f"  Avg length: {metrics['avg_length']:.1f}")
        print(f"  Avg repetition: {metrics['avg_repetition']:.2f}")
        print(f"  Closer frequency: {metrics['closer_frequency']:.1%}")
        print(f"  Pictogram frequency: {metrics['pictogram_frequency']:.1%}")
    
    print("\n" + "=" * 60)
    print("Interpretation:")
    print("=" * 60)
    print("Administrative = institutional bureaucracy (trade, ownership)")
    print("Ritual = symbolic/religious function (identity, cosmology)")
    print()
    print("This classification is based on structural features,")
    print("not on quantum or metaphysical properties.")

if __name__ == "__main__":
    main()
