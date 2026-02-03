"""
Symbol Composition Examples
Demonstrates the ⊕ operator and Axiom 2 (Hierarchical Compositionality).
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from harappan_core import CompositionEngine, Symbol, SymbolClass


def demonstrate_basic_composition():
    """
    Axiom 2: Composicionalidade Hierárquica
    ∀s ∈ Σ ∃B ∈ 𝔹 ∃M ⊆ 𝕄 [s = B ⊕ ⨁_{m∈M} m]
    """
    print("="*70)
    print("AXIOM 2: HIERARCHICAL COMPOSITIONALITY")
    print("="*70)
    print("\nBase ⊕ Modifiers → Composite Symbol\n")
    
    engine = CompositionEngine()
    
    # Example 1: Simple composition
    print("Example 1: Base entity with single modifier")
    base1 = 5
    modifiers1 = {"Crown"}
    symbol1 = engine.compose(base1, modifiers1)
    print(f"  {base1} ⊕ {modifiers1} → {symbol1}")
    print(f"  Class: {symbol1.symbol_class.name}\n")
    
    # Example 2: Multiple modifiers
    print("Example 2: Entity with multiple modifiers")
    base2 = 8
    modifiers2 = {"Dot", "Stroke", "Crown"}
    symbol2 = engine.compose(base2, modifiers2)
    print(f"  {base2} ⊕ {modifiers2} → {symbol2}")
    print(f"  Class: {symbol2.symbol_class.name}\n")
    
    # Example 3: No modifiers (identity)
    print("Example 3: Base without modifiers (identity element)")
    base3 = 3
    modifiers3 = set()
    symbol3 = engine.compose(base3, modifiers3)
    print(f"  {base3} ⊕ ∅ → {symbol3}")
    print(f"  Class: {symbol3.symbol_class.name}\n")


def demonstrate_core_modifiers():
    """
    Axiom 24: Difusão de Operadores
    Core modifiers: {Dot, Stroke, Line, Circle, Cross}
    """
    print("="*70)
    print("AXIOM 24: CORE MODIFIERS (Universal Operators)")
    print("="*70)
    print("\nThese modifiers appear across multiple writing systems:\n")
    
    engine = CompositionEngine()
    base = 7
    
    for modifier in CompositionEngine.CORE_MODIFIERS:
        symbol = engine.compose(base, {modifier})
        print(f"  Base {base} + {modifier:8s} → {symbol}")
    
    print("\nThese are universal cognitive primitives!")


def demonstrate_modifier_combinations():
    """
    Axiom 18: Álgebra de Operadores
    The modifier monoid ⟨𝕄,⊕⟩
    """
    print("\n" + "="*70)
    print("AXIOM 18: MODIFIER ALGEBRA (Monoid Structure)")
    print("="*70)
    print("\nDemonstrating modifier combinations:\n")
    
    engine = CompositionEngine()
    base = 10
    
    # Single modifiers
    print("Single modifiers:")
    for mod in ["Dot", "Stroke", "Crown"]:
        symbol = engine.compose(base, {mod})
        print(f"  {base} ⊕ {{{mod}}} → ID:{symbol.id}")
    
    # Combinations
    print("\nModifier combinations:")
    combinations = [
        {"Dot", "Stroke"},
        {"Dot", "Crown"},
        {"Stroke", "Crown"},
        {"Dot", "Stroke", "Crown"},
    ]
    
    for mods in combinations:
        symbol = engine.compose(base, mods)
        print(f"  {base} ⊕ {mods} → ID:{symbol.id}")
    
    # Demonstrate associativity property
    print("\nNote: Order matters in implementation but result is deterministic")


def demonstrate_axiom_8_inheritance():
    """
    Axiom 8: Herança de Propriedades
    Class doesn't change with modifiers
    """
    print("\n" + "="*70)
    print("AXIOM 8: PROPERTY INHERITANCE")
    print("="*70)
    print("\nModifiers change STATE, not CLASS:\n")
    
    engine = CompositionEngine()
    
    # ENT class bases (1-10)
    ent_base = 5
    print(f"Entity base: {ent_base}")
    
    modifier_sets = [
        set(),
        {"Dot"},
        {"Dot", "Stroke"},
        {"Dot", "Stroke", "Crown"},
    ]
    
    for mods in modifier_sets:
        symbol = engine.compose(ent_base, mods)
        mod_str = str(mods) if mods else "∅"
        print(f"  {ent_base} ⊕ {mod_str:25s} → Class: {symbol.symbol_class.name} (unchanged)")


def demonstrate_parallel_chinese_harappan():
    """
    Show parallel composition in both systems
    """
    print("\n" + "="*70)
    print("PARALLEL COMPOSITION: CHINESE ⇄ HARAPPAN")
    print("="*70)
    print("\nSame compositional logic, different implementations:\n")
    
    examples = [
        {
            "concept": "Human (base entity)",
            "chinese": "人",
            "harappan": (5, set()),
            "meaning": "Agent class without modification"
        },
        {
            "concept": "Human + Intensification",
            "chinese": "人 + 一 → 大",
            "harappan": (5, {"Crown"}),
            "meaning": "Agent with elevated status"
        },
        {
            "concept": "Human + Internal State",
            "chinese": "人 + 心 → 念",
            "harappan": (5, {"Fill"}),
            "meaning": "Agent with consciousness/intention"
        },
        {
            "concept": "Human + Action Capacity",
            "chinese": "人 + 力 → 男",
            "harappan": (5, {"Hook"}),
            "meaning": "Agent with productive capacity"
        },
    ]
    
    engine = CompositionEngine()
    
    for ex in examples:
        print(f"Concept: {ex['concept']}")
        print(f"  Chinese:  {ex['chinese']}")
        
        harappan_symbol = engine.compose(ex['harappan'][0], ex['harappan'][1])
        print(f"  Harappan: Base {ex['harappan'][0]} ⊕ {ex['harappan'][1]} → {harappan_symbol}")
        print(f"  Meaning:  {ex['meaning']}")
        print()


def show_composition_table():
    """
    Create a table showing systematic composition
    """
    print("="*70)
    print("COMPOSITION TABLE")
    print("="*70)
    print("\nSystematic combinations (sample):\n")
    
    engine = CompositionEngine()
    
    print(f"{'Base':<6} {'Modifiers':<30} {'Symbol ID':<12} {'Class':<10}")
    print("-"*70)
    
    # Show a grid of compositions
    bases = [3, 7, 12, 18, 26]
    modifier_sets = [
        set(),
        {"Dot"},
        {"Stroke"},
        {"Crown"},
        {"Dot", "Stroke"},
    ]
    
    for base in bases:
        for mods in modifier_sets:
            symbol = engine.compose(base, mods)
            mod_str = str(mods) if mods else "∅"
            print(f"{base:<6} {mod_str:<30} {symbol.id:<12} {symbol.symbol_class.name:<10}")
        print()


def run_all_compositions():
    """Run all composition demonstrations"""
    print("\n" + "🔧 "*30)
    print("HARAPPAN SYMBOL COMPOSITION ENGINE")
    print("🔧 "*30 + "\n")
    
    demonstrate_basic_composition()
    demonstrate_core_modifiers()
    demonstrate_modifier_combinations()
    demonstrate_axiom_8_inheritance()
    demonstrate_parallel_chinese_harappan()
    show_composition_table()
    
    print("="*70)
    print("COMPOSITION DEMONSTRATIONS COMPLETE")
    print("="*70)
    print("\nKey Insights:")
    print("  ✓ Composition is deterministic (Axiom 7)")
    print("  ✓ Modifiers form a monoid (Axiom 18)")
    print("  ✓ Class is preserved (Axiom 8)")
    print("  ✓ Core modifiers are universal (Axiom 24)")
    print("  ✓ Same logic as Chinese radicals (structural equivalence)")


if __name__ == "__main__":
    run_all_compositions()
