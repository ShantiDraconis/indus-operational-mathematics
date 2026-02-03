"""
Harappan Operational Mathematics System
Comprehensive Symbol Combination Analysis

This module provides detailed analysis of all possible combinations
of Harappan symbols (373-417) with graphic operators, including:
- Symbol-operator combinations (45 × 10 = 450 possibilities)
- Symbol pair compositions (45 × 45 = 2,025 possibilities)  
- State transition validation
- Composition rule verification
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple, FrozenSet, Any
from itertools import product, combinations, combinations_with_replacement
import json

from harappan_symbols import (
    SymbolFamily, GraphicOperator, Symbol, SymbolRegistry,
    CompositionRule, CompositionSystem, create_harappan_system
)


@dataclass(frozen=True)
class SymbolOperatorCombination:
    """
    Represents a specific combination of a symbol with an operator.
    
    This encodes one of the 450 possible symbol-operator pairs.
    """
    symbol_id: int  # 373-417
    operator: GraphicOperator
    
    def __post_init__(self):
        if not (373 <= self.symbol_id <= 417):
            raise ValueError(f"Symbol ID {self.symbol_id} out of range")
    
    def is_valid(self, registry: SymbolRegistry) -> bool:
        """Check if this combination is valid in the Harappan system"""
        symbol = registry.get_symbol(self.symbol_id)
        if not symbol:
            return False
        
        # Check family-operator compatibility
        if symbol.family == SymbolFamily.OMEGA:
            # Omega family accepts most operators
            return self.operator in {
                GraphicOperator.DOT, GraphicOperator.STROKE,
                GraphicOperator.FILL, GraphicOperator.BRACKET,
                GraphicOperator.SIDEBARS, GraphicOperator.CROWN,
                GraphicOperator.DUP, GraphicOperator.STACK
            }
        elif symbol.family == SymbolFamily.DELTA:
            # Delta family (relations) accepts knots and stems
            return self.operator in {
                GraphicOperator.KNOT, GraphicOperator.STEM,
                GraphicOperator.DOT, GraphicOperator.STROKE
            }
        elif symbol.family == SymbolFamily.SIGMA:
            # Sigma family (counts) primarily uses stack operator
            return self.operator == GraphicOperator.STACK
        
        return False
    
    def apply(self, registry: SymbolRegistry, 
              composition: CompositionSystem) -> Optional[int]:
        """
        Apply this operator to the symbol and return resulting symbol ID.
        Returns None if combination is invalid.
        """
        if not self.is_valid(registry):
            return None
        return composition.get_composition(self.symbol_id, self.operator)
    
    def __str__(self) -> str:
        return f"Symbol({self.symbol_id}) + {self.operator.name}"


@dataclass(frozen=True)
class SymbolPair:
    """
    Represents a pair of symbols that can be composed.
    
    This encodes one of the 2,025 possible symbol pairs (45²).
    """
    first_id: int  # 373-417
    second_id: int  # 373-417
    
    def __post_init__(self):
        if not (373 <= self.first_id <= 417):
            raise ValueError(f"First symbol ID {self.first_id} out of range")
        if not (373 <= self.second_id <= 417):
            raise ValueError(f"Second symbol ID {self.second_id} out of range")
    
    def is_composable(self, registry: SymbolRegistry) -> bool:
        """Check if these two symbols can be composed"""
        s1 = registry.get_symbol(self.first_id)
        s2 = registry.get_symbol(self.second_id)
        
        if not (s1 and s2):
            return False
        
        # Family composition rules
        # Omega + Omega → invalid (entities don't directly compose)
        if s1.family == SymbolFamily.OMEGA and s2.family == SymbolFamily.OMEGA:
            return False
        
        # Omega + Delta → valid (entity + relation)
        if s1.family == SymbolFamily.OMEGA and s2.family == SymbolFamily.DELTA:
            return True
        
        # Omega + Sigma → valid (entity + count)
        if s1.family == SymbolFamily.OMEGA and s2.family == SymbolFamily.SIGMA:
            return True
        
        # Delta + Omega → valid (relation + entity)
        if s1.family == SymbolFamily.DELTA and s2.family == SymbolFamily.OMEGA:
            return True
        
        # Delta + Delta → valid (relation + relation for chains)
        if s1.family == SymbolFamily.DELTA and s2.family == SymbolFamily.DELTA:
            return True
        
        # Delta + Sigma → valid (counted relations)
        if s1.family == SymbolFamily.DELTA and s2.family == SymbolFamily.SIGMA:
            return True
        
        # Sigma + Omega → valid (count applied to entity)
        if s1.family == SymbolFamily.SIGMA and s2.family == SymbolFamily.OMEGA:
            return True
        
        # Other combinations are generally invalid
        return False
    
    def compose(self, registry: SymbolRegistry,
                composition: CompositionSystem) -> Optional[Symbol]:
        """
        Attempt to compose these two symbols.
        Returns the resulting symbol or None if not composable.
        """
        if not self.is_composable(registry):
            return None
        
        # This would require extending CompositionSystem to handle pairs
        # For now, return None as a placeholder
        return None
    
    def __str__(self) -> str:
        return f"({self.first_id}, {self.second_id})"


class CombinationMatrix:
    """
    Comprehensive matrix of all symbol-operator combinations.
    
    This class analyzes all 450 possible symbol-operator pairs and
    categorizes them as valid or invalid.
    """
    
    def __init__(self, registry: SymbolRegistry):
        self.registry = registry
        self.combinations: Dict[Tuple[int, GraphicOperator], bool] = {}
        self.valid_combinations: List[SymbolOperatorCombination] = []
        self.invalid_combinations: List[SymbolOperatorCombination] = []
        self._build_matrix()
    
    def _build_matrix(self):
        """Build the complete combination matrix"""
        all_symbols = range(373, 418)  # 373-417 inclusive
        all_operators = list(GraphicOperator)
        
        for sym_id in all_symbols:
            for operator in all_operators:
                comb = SymbolOperatorCombination(sym_id, operator)
                is_valid = comb.is_valid(self.registry)
                
                self.combinations[(sym_id, operator)] = is_valid
                
                if is_valid:
                    self.valid_combinations.append(comb)
                else:
                    self.invalid_combinations.append(comb)
    
    def is_valid(self, symbol_id: int, operator: GraphicOperator) -> bool:
        """Check if a symbol-operator combination is valid"""
        return self.combinations.get((symbol_id, operator), False)
    
    def get_valid_operators(self, symbol_id: int) -> List[GraphicOperator]:
        """Get all valid operators for a given symbol"""
        return [op for op in GraphicOperator 
                if self.is_valid(symbol_id, op)]
    
    def get_valid_symbols(self, operator: GraphicOperator) -> List[int]:
        """Get all symbols that accept a given operator"""
        return [sym_id for sym_id in range(373, 418) 
                if self.is_valid(sym_id, operator)]
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about the combination matrix"""
        return {
            'total_combinations': len(self.combinations),
            'valid_combinations': len(self.valid_combinations),
            'invalid_combinations': len(self.invalid_combinations),
            'validity_ratio': len(self.valid_combinations) / len(self.combinations)
        }
    
    def get_family_statistics(self) -> Dict[str, Dict[str, int]]:
        """Get combination statistics by symbol family"""
        stats = {}
        
        for family in SymbolFamily:
            family_symbols = self.registry.get_family_symbols(family)
            family_symbol_ids = [s.id for s in family_symbols]
            
            valid_count = sum(
                1 for comb in self.valid_combinations 
                if comb.symbol_id in family_symbol_ids
            )
            
            total_count = len(family_symbol_ids) * len(list(GraphicOperator))
            
            stats[family.value] = {
                'symbol_count': len(family_symbols),
                'total_combinations': total_count,
                'valid_combinations': valid_count,
                'invalid_combinations': total_count - valid_count,
                'validity_ratio': valid_count / total_count if total_count > 0 else 0
            }
        
        return stats
    
    def to_json(self) -> str:
        """Export combination matrix as JSON"""
        data = {
            'statistics': self.get_statistics(),
            'family_statistics': self.get_family_statistics(),
            'valid_combinations': [
                {
                    'symbol_id': comb.symbol_id,
                    'operator': comb.operator.name,
                    'operator_value': comb.operator.value
                }
                for comb in self.valid_combinations
            ],
            'matrix': {
                f"{sym_id}_{op.name}": valid
                for (sym_id, op), valid in self.combinations.items()
            }
        }
        return json.dumps(data, indent=2)


class PairMatrix:
    """
    Comprehensive matrix of all symbol pair compositions.
    
    Analyzes all 2,025 possible symbol pairs (45²) for composability.
    """
    
    def __init__(self, registry: SymbolRegistry):
        self.registry = registry
        self.pairs: Dict[Tuple[int, int], bool] = {}
        self.composable_pairs: List[SymbolPair] = []
        self.non_composable_pairs: List[SymbolPair] = []
        self._build_matrix()
    
    def _build_matrix(self):
        """Build the complete pair matrix"""
        all_symbols = range(373, 418)
        
        for s1_id in all_symbols:
            for s2_id in all_symbols:
                pair = SymbolPair(s1_id, s2_id)
                is_composable = pair.is_composable(self.registry)
                
                self.pairs[(s1_id, s2_id)] = is_composable
                
                if is_composable:
                    self.composable_pairs.append(pair)
                else:
                    self.non_composable_pairs.append(pair)
    
    def is_composable(self, first_id: int, second_id: int) -> bool:
        """Check if two symbols can be composed"""
        return self.pairs.get((first_id, second_id), False)
    
    def get_composable_partners(self, symbol_id: int, 
                                position: str = 'first') -> List[int]:
        """
        Get all symbols that can be composed with the given symbol.
        
        Args:
            symbol_id: The symbol ID to check
            position: 'first' for (symbol_id, ?) or 'second' for (?, symbol_id)
        """
        if position == 'first':
            return [s2 for s2 in range(373, 418) 
                    if self.is_composable(symbol_id, s2)]
        else:  # position == 'second'
            return [s1 for s1 in range(373, 418) 
                    if self.is_composable(s1, symbol_id)]
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about the pair matrix"""
        return {
            'total_pairs': len(self.pairs),
            'composable_pairs': len(self.composable_pairs),
            'non_composable_pairs': len(self.non_composable_pairs),
            'composability_ratio': len(self.composable_pairs) / len(self.pairs)
        }
    
    def get_family_pair_statistics(self) -> Dict[str, Dict[str, int]]:
        """Get pair statistics organized by symbol family pairs"""
        stats = {}
        
        for f1 in SymbolFamily:
            for f2 in SymbolFamily:
                key = f"{f1.value}_{f2.value}"
                
                f1_symbols = {s.id for s in self.registry.get_family_symbols(f1)}
                f2_symbols = {s.id for s in self.registry.get_family_symbols(f2)}
                
                composable_count = sum(
                    1 for pair in self.composable_pairs 
                    if pair.first_id in f1_symbols and pair.second_id in f2_symbols
                )
                
                total_count = len(f1_symbols) * len(f2_symbols)
                
                stats[key] = {
                    'total_pairs': total_count,
                    'composable_pairs': composable_count,
                    'non_composable_pairs': total_count - composable_count,
                    'composability_ratio': composable_count / total_count if total_count > 0 else 0
                }
        
        return stats
    
    def to_json(self) -> str:
        """Export pair matrix as JSON"""
        data = {
            'statistics': self.get_statistics(),
            'family_statistics': self.get_family_pair_statistics(),
            'composable_pairs': [
                {'first': pair.first_id, 'second': pair.second_id}
                for pair in self.composable_pairs
            ]
        }
        return json.dumps(data, indent=2)


class SequenceValidator:
    """
    Validates sequences of symbols according to Harappan composition rules.
    
    This class checks:
    - Symbol sequence validity
    - Proper family transitions
    - Operator application order
    - Terminal state enforcement
    """
    
    def __init__(self, registry: SymbolRegistry, 
                 composition: CompositionSystem,
                 pair_matrix: PairMatrix):
        self.registry = registry
        self.composition = composition
        self.pair_matrix = pair_matrix
    
    def validate_sequence(self, symbol_ids: List[int]) -> Tuple[bool, str]:
        """
        Validate a sequence of symbol IDs.
        
        Returns:
            (is_valid, error_message) tuple
        """
        if not symbol_ids:
            return False, "Empty sequence"
        
        # Check all symbols exist
        for sym_id in symbol_ids:
            if not self.registry.get_symbol(sym_id):
                return False, f"Symbol {sym_id} not in registry"
        
        # Check sequential composability
        for i in range(len(symbol_ids) - 1):
            s1_id = symbol_ids[i]
            s2_id = symbol_ids[i + 1]
            
            if not self.pair_matrix.is_composable(s1_id, s2_id):
                s1 = self.registry.get_symbol(s1_id)
                s2 = self.registry.get_symbol(s2_id)
                return False, (f"Symbols {s1_id} ({s1.family.value}) and "
                              f"{s2_id} ({s2.family.value}) are not composable "
                              f"at position {i}")
        
        return True, "Valid sequence"
    
    def validate_with_operators(self, 
                                sequence: List[Tuple[int, Optional[GraphicOperator]]]
                                ) -> Tuple[bool, str]:
        """
        Validate a sequence where each symbol may have an operator applied.
        
        Args:
            sequence: List of (symbol_id, operator) tuples
        
        Returns:
            (is_valid, error_message) tuple
        """
        if not sequence:
            return False, "Empty sequence"
        
        for i, (sym_id, operator) in enumerate(sequence):
            # Check symbol exists
            symbol = self.registry.get_symbol(sym_id)
            if not symbol:
                return False, f"Symbol {sym_id} not in registry at position {i}"
            
            # Check operator validity if present
            if operator is not None:
                comb = SymbolOperatorCombination(sym_id, operator)
                if not comb.is_valid(self.registry):
                    return False, (f"Operator {operator.name} cannot be applied "
                                  f"to symbol {sym_id} at position {i}")
        
        # Check sequential composability (using base symbol IDs)
        symbol_ids = [sym_id for sym_id, _ in sequence]
        seq_valid, seq_msg = self.validate_sequence(symbol_ids)
        if not seq_valid:
            return False, seq_msg
        
        return True, "Valid sequence with operators"
    
    def generate_valid_sequences(self, max_length: int = 3, 
                                 start_family: Optional[SymbolFamily] = None
                                 ) -> List[List[int]]:
        """
        Generate all valid sequences up to max_length.
        
        Args:
            max_length: Maximum sequence length
            start_family: Optional family to start sequences with
        
        Returns:
            List of valid symbol ID sequences
        """
        valid_sequences = []
        
        # Get starting symbols
        if start_family:
            start_symbols = [s.id for s in 
                           self.registry.get_family_symbols(start_family)]
        else:
            start_symbols = list(range(373, 418))
        
        # Generate sequences of each length
        for start_id in start_symbols:
            # Length 1 sequences
            valid_sequences.append([start_id])
            
            if max_length >= 2:
                # Length 2 sequences
                partners = self.pair_matrix.get_composable_partners(start_id, 'first')
                for partner_id in partners:
                    valid_sequences.append([start_id, partner_id])
                    
                    if max_length >= 3:
                        # Length 3 sequences
                        next_partners = self.pair_matrix.get_composable_partners(
                            partner_id, 'first')
                        for next_id in next_partners:
                            seq = [start_id, partner_id, next_id]
                            if self.validate_sequence(seq)[0]:
                                valid_sequences.append(seq)
        
        return valid_sequences


class TransitionAnalyzer:
    """
    Analyzes state transitions in the Harappan operational system.
    
    Maps how symbols and operators cause transitions between states.
    """
    
    def __init__(self, registry: SymbolRegistry,
                 combination_matrix: CombinationMatrix,
                 pair_matrix: PairMatrix):
        self.registry = registry
        self.combination_matrix = combination_matrix
        self.pair_matrix = pair_matrix
        self.transition_map: Dict[str, Set[str]] = {}
    
    def build_transition_graph(self):
        """
        Build a graph of all possible state transitions.
        
        States are represented as symbol IDs, and edges represent
        valid compositions.
        """
        for sym_id in range(373, 418):
            state_key = f"S{sym_id}"
            self.transition_map[state_key] = set()
            
            # Add transitions via symbol composition
            partners = self.pair_matrix.get_composable_partners(sym_id, 'first')
            for partner_id in partners:
                target_key = f"S{partner_id}"
                self.transition_map[state_key].add(target_key)
            
            # Add transitions via operator application
            valid_ops = self.combination_matrix.get_valid_operators(sym_id)
            for op in valid_ops:
                # Operator creates a modified version of the same state
                op_key = f"S{sym_id}_{op.name}"
                self.transition_map[state_key].add(op_key)
    
    def get_reachable_states(self, start_id: int, max_steps: int = 3) -> Set[int]:
        """
        Get all states reachable from a starting symbol within max_steps.
        
        Args:
            start_id: Starting symbol ID
            max_steps: Maximum number of composition steps
        
        Returns:
            Set of reachable symbol IDs
        """
        if max_steps == 0:
            return {start_id}
        
        reachable = {start_id}
        current_level = {start_id}
        
        for _ in range(max_steps):
            next_level = set()
            for sym_id in current_level:
                partners = self.pair_matrix.get_composable_partners(sym_id, 'first')
                next_level.update(partners)
            
            reachable.update(next_level)
            current_level = next_level
            
            if not current_level:
                break
        
        return reachable
    
    def analyze_closure_properties(self) -> Dict[str, Any]:
        """
        Analyze closure properties of symbol families under composition.
        
        Returns:
            Dictionary with closure analysis results
        """
        results = {}
        
        for family in SymbolFamily:
            family_symbols = {s.id for s in 
                            self.registry.get_family_symbols(family)}
            
            # Check if composing within family stays in family
            internal_closure = True
            external_reachable = set()
            
            for sym_id in family_symbols:
                partners = self.pair_matrix.get_composable_partners(sym_id, 'first')
                for partner_id in partners:
                    if partner_id not in family_symbols:
                        internal_closure = False
                        external_reachable.add(partner_id)
            
            results[family.value] = {
                'is_closed': internal_closure,
                'symbol_count': len(family_symbols),
                'external_reachable_count': len(external_reachable),
                'external_reachable': list(external_reachable)
            }
        
        return results


def create_comprehensive_analysis() -> Dict[str, Any]:
    """
    Create a comprehensive analysis of all Harappan symbol combinations.
    
    Returns:
        Dictionary containing all analysis results
    """
    # Initialize system
    registry, composition = create_harappan_system()
    
    # Build analysis matrices
    combination_matrix = CombinationMatrix(registry)
    pair_matrix = PairMatrix(registry)
    validator = SequenceValidator(registry, composition, pair_matrix)
    analyzer = TransitionAnalyzer(registry, combination_matrix, pair_matrix)
    
    # Build transition graph
    analyzer.build_transition_graph()
    
    # Gather statistics
    results = {
        'symbol_count': len(registry.symbols),
        'operator_count': len(list(GraphicOperator)),
        'family_count': len(list(SymbolFamily)),
        
        'combination_statistics': combination_matrix.get_statistics(),
        'combination_family_statistics': combination_matrix.get_family_statistics(),
        
        'pair_statistics': pair_matrix.get_statistics(),
        'pair_family_statistics': pair_matrix.get_family_pair_statistics(),
        
        'closure_analysis': analyzer.analyze_closure_properties(),
        
        'sample_valid_sequences': {
            'omega_start': validator.generate_valid_sequences(3, SymbolFamily.OMEGA)[:10],
            'delta_start': validator.generate_valid_sequences(3, SymbolFamily.DELTA)[:10],
            'sigma_start': validator.generate_valid_sequences(3, SymbolFamily.SIGMA)[:10],
        }
    }
    
    return results


if __name__ == "__main__":
    # Run comprehensive analysis
    print("Harappan Symbol Combination Analysis")
    print("=" * 60)
    
    analysis = create_comprehensive_analysis()
    
    print(f"\nSymbol System Overview:")
    print(f"  Total Symbols: {analysis['symbol_count']}")
    print(f"  Total Operators: {analysis['operator_count']}")
    print(f"  Symbol Families: {analysis['family_count']}")
    
    print(f"\nSymbol-Operator Combinations:")
    combo_stats = analysis['combination_statistics']
    print(f"  Total Combinations: {combo_stats['total_combinations']}")
    print(f"  Valid: {combo_stats['valid_combinations']}")
    print(f"  Invalid: {combo_stats['invalid_combinations']}")
    print(f"  Validity Ratio: {combo_stats['validity_ratio']:.2%}")
    
    print(f"\nSymbol Pair Compositions:")
    pair_stats = analysis['pair_statistics']
    print(f"  Total Pairs: {pair_stats['total_pairs']}")
    print(f"  Composable: {pair_stats['composable_pairs']}")
    print(f"  Non-Composable: {pair_stats['non_composable_pairs']}")
    print(f"  Composability Ratio: {pair_stats['composability_ratio']:.2%}")
    
    print(f"\nClosure Analysis:")
    for family, closure_info in analysis['closure_analysis'].items():
        print(f"  {family}: Closed={closure_info['is_closed']}, "
              f"External Reachable={closure_info['external_reachable_count']}")
    
    print("\n" + "=" * 60)
    print("Analysis complete. Use functions for detailed exploration.")
