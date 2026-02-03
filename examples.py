#!/usr/bin/env python3
"""
Examples demonstrating the Harappan Operational Mathematics System

This script shows various usage patterns of the system.
"""

from harappan_symbols import (
    create_harappan_system, 
    SymbolFamily, 
    GraphicOperator
)
from harappan_sequence import (
    HarappanSequence, 
    validate_and_convert,
    FiniteAutomaton
)
from harappan_frequency import create_sample_data
import json


def example_1_basic_symbols():
    """Example 1: Criar e consultar símbolos"""
    print("=" * 70)
    print("EXEMPLO 1: Símbolos Básicos")
    print("=" * 70)
    
    registry, composition = create_harappan_system()
    
    # Consultar símbolo base
    symbol_373 = registry.get_symbol(373)
    print(f"\nSímbolo 373 (base oval):")
    print(f"  ID: {symbol_373.id}")
    print(f"  Família: {symbol_373.family.value}")
    print(f"  Forma base: {symbol_373.base_form}")
    print(f"  Descrição: {symbol_373.description}")
    
    # Consultar símbolos com operadores
    symbol_374 = registry.get_symbol(374)
    print(f"\nSímbolo 374 (oval + dot):")
    print(f"  Operadores: {[op.value for op in symbol_374.operators]}")
    print(f"  Descrição: {symbol_374.description}")
    
    # Símbolos por família
    omega_symbols = registry.get_family_symbols(SymbolFamily.OMEGA)
    delta_symbols = registry.get_family_symbols(SymbolFamily.DELTA)
    sigma_symbols = registry.get_family_symbols(SymbolFamily.SIGMA)
    
    print(f"\nTotal de símbolos por família:")
    print(f"  Ω (Entidades): {len(omega_symbols)} símbolos (373-399)")
    print(f"  Δ (Relações): {len(delta_symbols)} símbolos (400-409)")
    print(f"  Σ (Contagens): {len(sigma_symbols)} símbolos (410-417)")


def example_2_composition():
    """Example 2: Sistema de composição"""
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Sistema de Composição")
    print("=" * 70)
    
    registry, composition = create_harappan_system()
    
    # Aplicar operadores ao símbolo base
    print("\nAplicando operadores ao símbolo 373 (oval base):")
    
    operators = [
        (GraphicOperator.DOT, "Dot (instância)"),
        (GraphicOperator.STROKE, "Stroke (qualificação)"),
        (GraphicOperator.BRACKET, "Bracket (escopo)"),
        (GraphicOperator.SIDEBARS, "SideBars (nível)"),
        (GraphicOperator.CROWN, "Crown (multiplexação)"),
        (GraphicOperator.FILL, "Fill (consumação)")
    ]
    
    for operator, name in operators:
        result = composition.get_composition(373, operator)
        if result:
            result_symbol = registry.get_symbol(result)
            print(f"  373 + {name} → {result}: {result_symbol.description}")
    
    # Composição hierárquica (caso crítico)
    print("\nComposição hierárquica (caso crítico do problema):")
    print("  394 = 373 (oval base) + 343 (operador de fechamento U-family)")
    decompositions = composition.get_decomposition(394)
    for base, operator in decompositions:
        print(f"  394 pode ser decomposto em: {base} + {operator.value}")
    
    # Composição entre famílias
    print("\nComposição entre famílias:")
    dup_result = composition.get_composition(373, GraphicOperator.DUP)
    print(f"  373 (Ω) + Dup → {dup_result} (Δ): cria par de entidades")
    
    knot_result = composition.get_composition(400, GraphicOperator.KNOT)
    print(f"  400 (Δ) + Knot → {knot_result} (Δ): vincula par")
    
    stack_result = composition.get_composition(373, GraphicOperator.STACK)
    print(f"  373 (Ω) + Stack → {stack_result} (Σ): contagem de entidades")


def example_3_sequences():
    """Example 3: Sequências e validação"""
    print("\n" + "=" * 70)
    print("EXEMPLO 3: Sequências e Validação")
    print("=" * 70)
    
    # Sequência válida: entidade → relação → contagem
    print("\nSequência 1: [373, 400, 410] (entidade → relação → contagem)")
    result1 = validate_and_convert([373, 400, 410])
    print(f"  Válida: {result1['valid']}")
    print(f"  Notação funcional: {result1['functional_notation']}")
    print(f"  Entidades: {result1.get('entities', [])}")
    print(f"  Relações: {result1.get('relations', [])}")
    print(f"  Contagens: {result1.get('counts', [])}")
    
    # Sequência com registro fechado
    print("\nSequência 2: [373, 410, 394] (entidade → contagem → fechamento)")
    result2 = validate_and_convert([373, 410, 394])
    print(f"  Válida: {result2['valid']}")
    print(f"  Notação funcional: {result2['functional_notation']}")
    
    # Sequência simples
    print("\nSequência 3: [373] (entidade única)")
    result3 = validate_and_convert([373])
    print(f"  Válida: {result3['valid']}")
    print(f"  Notação funcional: {result3['functional_notation']}")


def example_4_json_representation():
    """Example 4: Representação JSON moderna"""
    print("\n" + "=" * 70)
    print("EXEMPLO 4: Representação JSON Moderna")
    print("=" * 70)
    
    registry, _ = create_harappan_system()
    
    # Criar sequência institucional
    sequence = HarappanSequence()
    sequence.object_type = "seal"
    sequence.provenance = "Harappa"
    sequence.add_symbol(373)  # Entidade
    sequence.add_symbol(410)  # Contagem = 2
    sequence.add_symbol(394)  # Registro fechado
    
    # Converter para JSON
    json_repr = sequence.to_json()
    
    print("\nRepresentação JSON (equivalente moderno):")
    print(json.dumps(json_repr, indent=2, ensure_ascii=False))
    
    print("\nNotação funcional:")
    print(f"  {sequence.to_functional_notation(registry)}")


def example_5_frequency_analysis():
    """Example 5: Análise de frequência"""
    print("\n" + "=" * 70)
    print("EXEMPLO 5: Análise de Frequência e Distribuição")
    print("=" * 70)
    
    # Criar analisador com dados de exemplo
    analyzer = create_sample_data()
    
    # Símbolos de alta frequência (operadores centrais)
    high_freq = analyzer.get_high_frequency_symbols(threshold=10)
    print("\nSímbolos de alta frequência (operadores centrais):")
    for symbol_id in sorted(high_freq):
        freq = analyzer.frequency_data[symbol_id]
        print(f"  {symbol_id}: {freq.total_occurrences} ocorrências")
    
    # Símbolos de baixa frequência (instâncias específicas)
    low_freq = analyzer.get_low_frequency_symbols(threshold=5)
    print("\nSímbolos de baixa frequência (instâncias específicas):")
    for symbol_id in sorted(low_freq):
        freq = analyzer.frequency_data[symbol_id]
        print(f"  {symbol_id}: {freq.total_occurrences} ocorrências")
    
    # Padrões de posição para símbolo 373
    patterns = analyzer.get_position_patterns(373)
    print("\nDistribuição de posição do símbolo 373 (oval base):")
    for position, percentage in patterns.items():
        print(f"  {position}: {percentage:.1f}%")
    
    # Pares mais comuns
    print("\nPares mais comuns (Tabela II):")
    common_pairs = analyzer.get_most_common_pairs(n=5)
    for pair in common_pairs:
        print(f"  {pair.first_symbol} → {pair.second_symbol}: {pair.occurrences} vezes")
    
    # Padrões de família
    print("\nPadrões por família:")
    family_patterns = analyzer.analyze_family_patterns()
    for family, positions in family_patterns.items():
        if any(positions.values()):
            total = sum(positions.values())
            print(f"  {family}:")
            for position, count in positions.items():
                if count > 0:
                    print(f"    {position}: {count} ({count/total*100:.1f}%)")


def example_6_automaton():
    """Example 6: Autômato finito"""
    print("\n" + "=" * 70)
    print("EXEMPLO 6: Autômato Finito de Validação")
    print("=" * 70)
    
    registry, _ = create_harappan_system()
    automaton = FiniteAutomaton(registry)
    
    # Testar diferentes sequências
    test_sequences = [
        ([373, 400, 410], "entidade → relação → contagem"),
        ([373, 410], "entidade → contagem"),
        ([410], "contagem direta"),
        ([373], "entidade única"),
        ([373, 373, 410], "múltiplas entidades → contagem"),
    ]
    
    print("\nValidação de sequências:")
    for sequence, description in test_sequences:
        is_valid = automaton.validate_sequence(sequence)
        status = "✓ VÁLIDA" if is_valid else "✗ INVÁLIDA"
        print(f"  {status}: {sequence} ({description})")
        print(f"    Estado final: {automaton.get_state().value}")


def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("SISTEMA OPERACIONAL DE MATEMÁTICA HARAPPANA")
    print("Bloco 373-417: Demonstração de Funcionalidades")
    print("=" * 70)
    
    example_1_basic_symbols()
    example_2_composition()
    example_3_sequences()
    example_4_json_representation()
    example_5_frequency_analysis()
    example_6_automaton()
    
    print("\n" + "=" * 70)
    print("FIM DOS EXEMPLOS")
    print("=" * 70)
    print("\nConclusão:")
    print("  - O sistema harappano é um protocolo operacional")
    print("  - Usa ~45 símbolos principais para gerar ~417 estados válidos")
    print("  - Operadores gráficos são universais")
    print("  - Equivalente moderno: JSON + workflow + autômato finito")
    print()


if __name__ == "__main__":
    main()
