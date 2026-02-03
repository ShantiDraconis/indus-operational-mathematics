"""
Example: Basic usage of the symbolic systems framework.

This script demonstrates:
- Creating and registering symbolic systems
- Performing comparative analysis
- Finding universal patterns
"""

import sys
sys.path.insert(0, 'src')

from symbolic_systems import UniversalGrammar, HarappanSystem, MayanSystem, AztecSystem
from symbolic_systems.analysis import ComparativeAnalyzer


def main():
    print("=" * 70)
    print("Symbolic Systems Analysis Framework - Basic Example")
    print("=" * 70)
    print()
    
    # Create the universal grammar
    print("1. Creating Universal Grammar...")
    grammar = UniversalGrammar()
    
    # Create and register systems
    print("2. Registering symbolic systems...")
    harappan = HarappanSystem()
    mayan = MayanSystem()
    aztec = AztecSystem()
    
    grammar.register_system(harappan)
    grammar.register_system(mayan)
    grammar.register_system(aztec)
    
    print(f"   - Registered {len(grammar.systems)} systems")
    print()
    
    # Display system statistics
    print("3. System Statistics:")
    print()
    for system_name in grammar.systems:
        system = grammar.get_system(system_name)
        stats = system.get_statistics()
        print(f"   {system_name} System:")
        print(f"      Total symbols: {stats['total_symbols']}")
        print(f"      Primary level: {stats['primary_level']}")
        print(f"      Transformation rules: {stats['transformation_rules']}")
        print()
    
    # Perform comparative analysis
    print("4. Comparative Analysis:")
    print()
    analyzer = ComparativeAnalyzer(grammar)
    
    # Find universal "Man → Lord" transformation
    print("   a) Universal 'Man → Lord' Transformations:")
    man_to_lord = analyzer.find_man_to_lord_transformations()
    for transform in man_to_lord:
        print(f"      - {transform['system']}: {transform['base']} + {transform['modifier']} → {transform['result']}")
    print()
    
    # Find "House → Temple" transformation
    print("   b) Universal 'House → Temple' Transformations:")
    house_to_temple = analyzer.find_house_to_temple_transformations()
    for transform in house_to_temple:
        print(f"      - {transform['system']}: {transform['base']} + {transform['modifier']} → {transform['result']}")
    print()
    
    # Compare systems
    print("   c) System Correspondences:")
    comparison = grammar.compare_systems("Harappan", "Mayan")
    print(f"      Harappan vs Mayan: {comparison['total_matches']} correspondences")
    
    comparison = grammar.compare_systems("Mayan", "Aztec")
    print(f"      Mayan vs Aztec: {comparison['total_matches']} correspondences")
    print()
    
    # Cognitive axes analysis
    print("5. Cognitive Axes Usage:")
    axes_usage = analyzer.analyze_cognitive_axes_usage()
    print("   Systems using each axis:")
    for axis, count in axes_usage['summary'].items():
        print(f"      {axis}: {count} systems")
    print()
    
    # Calendar systems comparison
    print("6. Calendar Systems:")
    calendar_comparison = analyzer.compare_calendar_systems()
    print(f"   Systems with calendars: {calendar_comparison['systems_with_calendars']}")
    print(f"   Common patterns:")
    print(f"      260-day sacred cycle: {calendar_comparison['common_patterns']['sacred_cycle_260_days']}")
    print(f"      Base-20 system: {calendar_comparison['common_patterns']['base_20_system']}")
    print()
    
    print("=" * 70)
    print("Analysis Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
