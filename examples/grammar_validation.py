"""
Grammar Validation Example

Demonstrates discrete state grammar (finite automaton) for sequence validation.
"""

import sys
sys.path.append('..')

from src.grammar_framework import (
    DiscreteStateGrammar,
    SymbolState,
    ConstraintSatisfactionAnalogy
)

# Example sequences
sequences = [
    ['init', 'content', 'auth', 'closer'],  # Valid
    ['init', 'content', 'closer'],  # Missing auth
    ['init', 'auth', 'closer'],  # Valid (shorter)
    ['content', 'closer'],  # Missing init
    ['init', 'content', 'auth'],  # No closer
]

def main():
    print("=" * 60)
    print("Discrete State Grammar Validation")
    print("=" * 60)
    print("\nNOTE: We use 'quantum' terminology as ANALOGY ONLY")
    print("Not a claim of physical quantum processes!")
    print()
    
    # Print analogy explanations
    print("QUANTUM TERMINOLOGY AS ANALOGY")
    print("-" * 60)
    print(ConstraintSatisfactionAnalogy.explain_superposition_analogy())
    print()
    print(ConstraintSatisfactionAnalogy.explain_measurement_analogy())
    print()
    print(ConstraintSatisfactionAnalogy.explain_entanglement_analogy())
    
    # Create grammar
    grammar = DiscreteStateGrammar()
    
    # Define symbol-to-operator mapping
    symbol_to_operator = {
        'init': 'any_symbol',
        'content': 'any_symbol',
        'auth': 'authority_marker',
        'closer': 'closer_symbol'
    }
    
    print("\n" + "=" * 60)
    print("SEQUENCE VALIDATION")
    print("=" * 60)
    
    for i, seq in enumerate(sequences, 1):
        is_valid, state_path = grammar.is_valid_sequence(seq, symbol_to_operator)
        
        print(f"\n{i}. Sequence: {seq}")
        print(f"   State path: {[s.value for s in state_path]}")
        print(f"   Valid: {'✓ YES' if is_valid else '✗ NO'}")
        
        if not is_valid:
            print(f"   Reason: Did not reach 'closed' state")
    
    # Statistics
    print("\n" + "=" * 60)
    print("CONSTRAINED CONFIGURATIONS")
    print("=" * 60)
    
    stats = grammar.constrained_configurations(sequences, symbol_to_operator)
    
    print(f"\nTotal sequences: {stats['total']}")
    print(f"Valid: {stats['valid']}")
    print(f"Invalid: {stats['invalid']}")
    print(f"Validity rate: {stats['validity_rate']:.1%}")
    print(f"\nFinal state distribution:")
    for state, count in stats['state_distribution'].items():
        print(f"  {state:15s}: {count}")
    
    print("\n" + "=" * 60)
    print("Interpretation:")
    print("=" * 60)
    print("Valid sequences = those following institutional grammar")
    print("Invalid sequences = violations of compositional rules")
    print()
    print("This is a FINITE AUTOMATON model, not quantum mechanics.")
    print("'Superposition' = classification ambiguity")
    print("'Measurement' = validation check")
    print("'Collapse' = transition to definite state")

if __name__ == "__main__":
    main()
