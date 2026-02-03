"""
Example: Consciousness-Archaeology Interface

This example demonstrates the experimental framework for studying
consciousness and symbol perception.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_archaeology import Symbol
from quantum_archaeology.consciousness_interface import (
    ConsciousnessInterface, 
    ConsciousnessState,
    PerceptionExperiment
)


def main():
    """Demonstrate consciousness interface capabilities."""
    
    print("=" * 80)
    print("CONSCIOUSNESS-ARCHAEOLOGY INTERFACE: Experimental Framework")
    print("=" * 80)
    print()
    
    interface = ConsciousnessInterface()
    
    # Create sample symbols
    symbols = [
        Symbol("U+01", "Unicorn", "Authority symbol"),
        Symbol("U+08", "Bird", "Messenger symbol"),
        Symbol("U+09", "Wheel", "Cosmic order symbol"),
    ]
    
    # Design meditation protocol
    print("1. MEDITATION PROTOCOL DESIGN")
    print("-" * 80)
    
    protocol = interface.design_meditation_protocol(symbols)
    
    print(f"\nProtocol: {protocol['title']}")
    print(f"Duration: {protocol['duration_minutes']} minutes")
    print(f"\nPhases:")
    for phase in protocol['phases']:
        print(f"\n  {phase['phase']} ({phase['duration_minutes']} min):")
        for instruction in phase['instructions']:
            print(f"    • {instruction}")
    
    print(f"\n  Measurement Protocols:")
    for measurement in protocol['measurement_protocols']:
        print(f"    • {measurement}")
    
    # Analyze brainwave patterns
    print("\n\n2. BRAINWAVE-SYMBOL CORRELATION ANALYSIS")
    print("-" * 80)
    
    # Simulated brainwave data
    brainwave_data = {
        "delta": 2.5,
        "theta": 6.2,
        "alpha": 9.8,
        "beta": 15.3,
        "gamma": 35.2,
    }
    
    analysis = interface.analyze_brainwave_symbol_correlation(
        brainwave_data,
        [s.id for s in symbols]
    )
    
    print("\nBrainwave Profile:")
    for band, value in brainwave_data.items():
        print(f"  {band.capitalize():10}: {value:6.2f} Hz")
    
    print("\nObservations:")
    for obs in analysis['observations']:
        print(f"  • {obs}")
    
    print("\nHypotheses:")
    for hyp in analysis['hypotheses']:
        print(f"  • {hyp}")
    
    # Archetypal mapping
    print("\n\n3. ARCHETYPAL SYMBOL MAPPING")
    print("-" * 80)
    
    for symbol in symbols:
        mapping = interface.create_archetypal_mapping(symbol)
        print(f"\n{symbol.name} ({symbol.id}):")
        print(f"  Potential Archetypes: {', '.join(mapping['potential_archetypes'])}")
    
    # Comparative study design
    print("\n\n4. COMPARATIVE CONSCIOUSNESS STUDY DESIGN")
    print("-" * 80)
    
    study = interface.design_comparative_consciousness_study()
    
    print(f"\nTitle: {study['title']}")
    print(f"\nObjective: {study['objective']}")
    
    print(f"\nParticipants: {study['methodology']['participants']}")
    
    print("\nExperimental Conditions:")
    for condition in study['methodology']['conditions']:
        print(f"\n  {condition['name']}:")
        print(f"    Protocol: {condition['protocol']}")
        print(f"    Measures: {', '.join(condition['measures'])}")
    
    print("\nEthical Considerations:")
    for consideration in study['ethical_considerations']:
        print(f"  • {consideration}")
    
    # Propose specific experiment
    print("\n\n5. SPECIFIC EXPERIMENT PROPOSAL")
    print("-" * 80)
    
    experiment = interface.propose_experiment(
        "meditation",
        {
            "duration_days": 30,
            "daily_practice": "20 minutes",
            "symbol_set": "Indus unicorn sequences",
        }
    )
    
    print(f"\nTitle: {experiment['title']}")
    print(f"Description: {experiment['description']}")
    
    print("\nRequired Resources:")
    for resource in experiment['required_resources']:
        print(f"  • {resource}")
    
    print("\nExpected Outcomes:")
    for outcome in experiment['expected_outcomes']:
        print(f"  • {outcome}")
    
    # Display manifesto
    print("\n\n6. CONSCIOUSNESS-ARCHAEOLOGY RESEARCH MANIFESTO")
    print("=" * 80)
    
    manifesto = interface.generate_consciousness_research_manifesto()
    print(manifesto)
    
    print("\n" + "=" * 80)
    print("Consciousness interface demonstration complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
