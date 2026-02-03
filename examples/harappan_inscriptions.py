"""
Example: Analyzing Harappan inscriptions.

This script demonstrates how to parse and interpret
Harappan inscriptions using the operational framework.
"""

import sys
sys.path.insert(0, 'src')

from symbolic_systems import HarappanSystem
from symbolic_systems.analysis import StatisticalAnalyzer


def main():
    print("=" * 70)
    print("Harappan Inscription Analysis")
    print("=" * 70)
    print()
    
    # Create Harappan system
    harappan = HarappanSystem()
    
    # Display available symbols
    print("1. Available Harappan Symbols:")
    print()
    for symbol_id, symbol in harappan.symbols.items():
        mod_str = f" (+{', '.join(symbol.modifiers)})" if symbol.modifiers else ""
        print(f"   {symbol_id}: {symbol.name}{mod_str}")
        print(f"      Form: {symbol.form}")
        print(f"      Description: {symbol.description}")
        print()
    
    # Example inscriptions
    print("2. Analyzing Example Inscriptions:")
    print()
    
    inscriptions = [
        {
            'id': 'INS-001',
            'symbols': ['H30', 'H_JAR', 'H27', 'H27', 'H27'],
            'description': 'Lord + Jar + 3 units'
        },
        {
            'id': 'INS-002',
            'symbols': ['H26', 'H_FISH', 'H27'],
            'description': 'Man + Fish + 1 unit'
        },
        {
            'id': 'INS-003',
            'symbols': ['H_HOUSE', 'H_PLANT', 'H27', 'H27'],
            'description': 'House + Plant + 2 units'
        }
    ]
    
    analyzer = StatisticalAnalyzer(harappan)
    
    for inscription in inscriptions:
        print(f"   Inscription {inscription['id']}: {inscription['description']}")
        interpretation = harappan.parse_inscription(inscription['symbols'])
        stats = analyzer.analyze_sequence(inscription['symbols'])
        
        print(f"      Type: {interpretation['type']}")
        print(f"      Length: {stats['length']} symbols")
        print(f"      Unique symbols: {stats['unique_symbols']}")
        print(f"      Cognitive axes: {', '.join(stats['cognitive_axes'])}")
        
        if interpretation.get('has_quantity'):
            print(f"      Has quantity marker: Yes")
        print()
    
    # Compare inscriptions
    print("3. Comparing Inscriptions:")
    print()
    comparison = analyzer.compare_sequences(
        inscriptions[0]['symbols'],
        inscriptions[1]['symbols']
    )
    print(f"   INS-001 vs INS-002:")
    print(f"      Jaccard similarity: {comparison['jaccard_similarity']:.2f}")
    print(f"      Common symbols: {comparison['common_symbols']}")
    print()
    
    # Demonstrate transformation
    print("4. Symbol Transformations:")
    print()
    man_symbol = harappan.get_symbol('H26')
    print(f"   Base: {man_symbol.name} ({man_symbol.base_id})")
    
    lord_result = harappan.transform('H26', 'crown')
    if lord_result:
        lord_symbol = harappan.get_symbol(lord_result)
        print(f"   + crown modifier →")
        print(f"   Result: {lord_symbol.name} ({lord_symbol.base_id})")
        print(f"   This demonstrates the universal 'Man → Lord' transformation")
    print()
    
    print("=" * 70)
    print("Analysis Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
