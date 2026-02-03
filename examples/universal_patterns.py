"""
Example: Demonstrating universal patterns across all systems.

This script creates a comprehensive demonstration of the
universal patterns found in the framework.
"""

import sys
sys.path.insert(0, 'src')

from symbolic_systems import UniversalGrammar, HarappanSystem, MayanSystem, AztecSystem
from symbolic_systems.core.operators import UNIVERSAL_OPERATORS, CognitiveAxis
from symbolic_systems.analysis import ComparativeAnalyzer


def print_separator(char="=", length=70):
    """Print a separator line."""
    print(char * length)


def main():
    print_separator()
    print("UNIVERSAL PATTERNS IN ANCIENT SYMBOLIC SYSTEMS")
    print_separator()
    print()
    
    # Setup
    grammar = UniversalGrammar()
    harappan = HarappanSystem()
    mayan = MayanSystem()
    aztec = AztecSystem()
    
    grammar.register_system(harappan)
    grammar.register_system(mayan)
    grammar.register_system(aztec)
    
    analyzer = ComparativeAnalyzer(grammar)
    
    # 1. The 15 Universal Operators
    print("1. THE 15 UNIVERSAL COGNITIVE OPERATORS")
    print()
    print("These are the fundamental graphical forms found across ALL human symbolic systems:")
    print()
    
    for i, op in enumerate(UNIVERSAL_OPERATORS, 1):
        print(f"{i:2d}. {op.name:12s} {op.form:3s} - {op.function}")
        print(f"    Axes: {', '.join(axis.value for axis in op.cognitive_axes)}")
        print(f"    Examples: {', '.join(op.examples[:2])}")
        print()
    
    print_separator("-")
    print()
    
    # 2. The 7 Cognitive Axes
    print("2. THE 7 FUNDAMENTAL COGNITIVE AXES")
    print()
    print("These are the semantic dimensions underlying all symbolic representation:")
    print()
    
    axes_info = [
        (CognitiveAxis.PRESENCE, "Presence/Absence", "Existence, being, instantiation"),
        (CognitiveAxis.QUANTITY, "Quantity/Measure", "Cardinality, counting, measurement"),
        (CognitiveAxis.QUALITY, "Quality/State", "Attribution, properties, characteristics"),
        (CognitiveAxis.RELATION, "Relation/Bond", "Connectivity, links, associations"),
        (CognitiveAxis.SPACE, "Space/Domain", "Location, territory, containment"),
        (CognitiveAxis.TIME, "Time/Phase", "Temporality, cycles, sequences"),
        (CognitiveAxis.VALIDATION, "Validation/Closure", "Completeness, authority, finality"),
    ]
    
    for i, (axis, name, description) in enumerate(axes_info, 1):
        print(f"{i}. {name}")
        print(f"   {description}")
        ops = [op.name for op in UNIVERSAL_OPERATORS if axis in op.cognitive_axes]
        print(f"   Operators using this axis: {', '.join(ops[:5])}")
        print()
    
    print_separator("-")
    print()
    
    # 3. Universal Transformations
    print("3. UNIVERSAL TRANSFORMATION PATTERNS")
    print()
    print("These patterns appear independently across cultures:")
    print()
    
    print("A. MAN → LORD (Authority Transformation)")
    print("   Universal pattern: Person + power elements above head = authority")
    print()
    
    transformations = analyzer.find_man_to_lord_transformations()
    for t in transformations:
        if 'man' in t['base'].lower() or 'person' in t['base'].lower():
            print(f"   {t['system']:12s}: {t['base']} + {t['modifier']} → {t['result']}")
    print()
    
    print("B. HOUSE → TEMPLE (Sacred Space Transformation)")
    print("   Universal pattern: Building + divine elements = sacred space")
    print()
    
    house_transforms = analyzer.find_house_to_temple_transformations()
    for t in house_transforms:
        print(f"   {t['system']:12s}: {t['base']} + {t['modifier']} → {t['result']}")
    print()
    
    print_separator("-")
    print()
    
    # 4. Calendar Systems
    print("4. CALENDAR SYSTEMS AS OPERATIONAL MATHEMATICS")
    print()
    print("Both Mayan and Aztec systems use identical combinatorial structure:")
    print()
    
    print("   Mayan Tzolk'in:  20 day signs × 13 numbers = 260 unique combinations")
    print("   Aztec Tonalpohualli: 20 day signs × 13 numbers = 260 unique combinations")
    print()
    print("   This is isomorphic to:")
    print("   Harappan structure: N base symbols × M modifiers = composite system")
    print()
    
    # Example calculation
    date = mayan.calculate_calendar_date(kin=13, uinal=9, tun=2)
    print(f"   Example Mayan date: 13 K'in + 9 Uinal + 2 Tun = {date['total_days']} days")
    
    aztec_date = aztec.calculate_tonalpohualli(7, 3)
    print(f"   Example Aztec date: {aztec_date['representation']} (position {aztec_date['calendar_position']})")
    print()
    
    print_separator("-")
    print()
    
    # 5. System Correspondences
    print("5. CROSS-SYSTEM CORRESPONDENCES")
    print()
    print("Finding shared cognitive structures across systems:")
    print()
    
    comparisons = [
        ("Harappan", "Mayan"),
        ("Mayan", "Aztec"),
        ("Harappan", "Aztec"),
    ]
    
    for sys1, sys2 in comparisons:
        result = grammar.compare_systems(sys1, sys2)
        print(f"   {sys1} ↔ {sys2}: {result['total_matches']} correspondences")
    print()
    
    print_separator("-")
    print()
    
    # 6. The Theory
    print("6. THE UNIVERSAL GRAMMAR THEORY")
    print()
    print("Key insight: Humanity did not invent writing multiple times.")
    print("We discovered ONCE a deep grammar of symbolic representation,")
    print("and each culture realized it in their particular way.")
    print()
    print("Evidence:")
    print("   • Same 15 operators appear independently across cultures")
    print("   • Same 7 cognitive axes structure all systems")
    print("   • Same transformations (man→lord, house→temple) everywhere")
    print("   • Same numerical bases (5, 10, 20) emerge independently")
    print()
    print("The Harappan system is a realization.")
    print("The Chinese system is a realization.")
    print("The Mayan system is a realization.")
    print("The Runic systems are a realization.")
    print()
    print("All are variations on deeply human themes.")
    print()
    
    print_separator()
    print("Framework demonstration complete!")
    print_separator()


if __name__ == "__main__":
    main()
