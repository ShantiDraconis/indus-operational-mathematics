"""
Analysis tools for comparing and analyzing symbolic systems.
"""

from typing import List, Dict, Optional
from ..core.grammar import UniversalGrammar, SymbolicSystem
from ..core.operators import CognitiveAxis, UNIVERSAL_OPERATORS


class ComparativeAnalyzer:
    """
    Tool for comparing symbolic systems and finding universal patterns.
    """
    
    def __init__(self, grammar: UniversalGrammar):
        self.grammar = grammar
    
    def find_man_to_lord_transformations(self) -> List[Dict[str, any]]:
        """
        Find the universal "Man → Lord" transformation across all systems.
        
        Universal pattern: Man + power elements above head = authority
        """
        results = []
        
        for system_name, system in self.grammar.systems.items():
            for base_id, rules in system.transformation_rules.items():
                for modifier, result in rules:
                    if any(keyword in modifier.lower() 
                           for keyword in ['crown', 'power', 'divine', 'adorn']):
                        results.append({
                            'system': system_name,
                            'base': base_id,
                            'modifier': modifier,
                            'result': result,
                            'pattern': 'authority_transformation'
                        })
        
        return results
    
    def find_house_to_temple_transformations(self) -> List[Dict[str, any]]:
        """
        Find the universal "House → Temple → City" transformation.
        
        Pattern: House + divine elements = sacred space
        """
        results = []
        
        for system_name, system in self.grammar.systems.items():
            for base_id, rules in system.transformation_rules.items():
                base_symbol = system.get_symbol(base_id)
                if base_symbol and 'house' in base_symbol.name.lower():
                    for modifier, result in rules:
                        if 'divine' in modifier.lower():
                            results.append({
                                'system': system_name,
                                'base': base_id,
                                'modifier': modifier,
                                'result': result,
                                'pattern': 'sacred_space_transformation'
                            })
        
        return results
    
    def analyze_cognitive_axes_usage(self) -> Dict[str, any]:
        """
        Analyze how different systems use the 7 cognitive axes.
        """
        usage = {axis: [] for axis in CognitiveAxis}
        
        for system_name, system in self.grammar.systems.items():
            axis_counts = {axis: 0 for axis in CognitiveAxis}
            
            for symbol in system.symbols.values():
                for axis in symbol.cognitive_axes:
                    axis_counts[axis] += 1
            
            for axis, count in axis_counts.items():
                if count > 0:
                    usage[axis].append({
                        'system': system_name,
                        'count': count,
                        'percentage': count / len(system.symbols) if system.symbols else 0
                    })
        
        return {
            'axis_usage': usage,
            'summary': {
                axis.value: len(systems)
                for axis, systems in usage.items()
            }
        }
    
    def find_operator_correspondences(self, operator_name: str) -> List[Dict[str, any]]:
        """
        Find how a specific universal operator appears in different systems.
        
        Example: Find all instances of "Point" operator across systems
        """
        results = []
        
        for system_name, system in self.grammar.systems.items():
            for symbol in system.symbols.values():
                if operator_name.lower() in symbol.name.lower():
                    results.append({
                        'system': system_name,
                        'symbol_id': symbol.base_id,
                        'symbol_name': symbol.name,
                        'form': symbol.form,
                        'cognitive_axes': [axis.value for axis in symbol.cognitive_axes]
                    })
        
        return results
    
    def compare_calendar_systems(self) -> Dict[str, any]:
        """
        Compare calendar systems across Mayan and Aztec systems.
        
        Both use base-20 systems with cyclic combinations.
        """
        calendars = {}
        
        for system_name, system in self.grammar.systems.items():
            if hasattr(system, 'calendar'):
                calendars[system_name] = system.calendar
        
        return {
            'systems_with_calendars': list(calendars.keys()),
            'calendars': calendars,
            'common_patterns': {
                'sacred_cycle_260_days': [
                    name for name, cal in calendars.items()
                    if any('260' in str(v) for v in cal.values())
                ],
                'base_20_system': [
                    name for name, cal in calendars.items()
                    if any('20' in str(k) or v == 20 for k, v in cal.items())
                ]
            }
        }
    
    def generate_correspondence_matrix(self) -> Dict[str, any]:
        """
        Generate a matrix showing correspondences between all registered systems.
        
        This implements the "Global Correspondence Matrix" from the theory.
        """
        systems = list(self.grammar.systems.keys())
        matrix = {}
        
        for i, sys1 in enumerate(systems):
            for sys2 in systems[i+1:]:
                comparison = self.grammar.compare_systems(sys1, sys2)
                key = f"{sys1}_vs_{sys2}"
                matrix[key] = {
                    'total_correspondences': comparison.get('total_matches', 0),
                    'correspondences': comparison.get('correspondences', [])
                }
        
        return {
            'systems': systems,
            'total_systems': len(systems),
            'comparisons': matrix,
            'summary': {
                key: data['total_correspondences']
                for key, data in matrix.items()
            }
        }


class StatisticalAnalyzer:
    """
    Tool for statistical analysis of symbolic sequences.
    """
    
    def __init__(self, system: SymbolicSystem):
        self.system = system
    
    def analyze_sequence(self, symbol_ids: List[str]) -> Dict[str, any]:
        """
        Perform statistical analysis on a sequence of symbols.
        
        Returns frequency, co-occurrence patterns, and structural features.
        """
        if not symbol_ids:
            return {'error': 'Empty sequence'}
        
        # Frequency analysis
        frequency = {}
        for sid in symbol_ids:
            frequency[sid] = frequency.get(sid, 0) + 1
        
        # Co-occurrence (bigrams)
        bigrams = {}
        for i in range(len(symbol_ids) - 1):
            bigram = (symbol_ids[i], symbol_ids[i+1])
            bigrams[bigram] = bigrams.get(bigram, 0) + 1
        
        # Cognitive axes used
        axes_used = set()
        for sid in symbol_ids:
            symbol = self.system.get_symbol(sid)
            if symbol:
                axes_used.update(symbol.cognitive_axes)
        
        return {
            'length': len(symbol_ids),
            'unique_symbols': len(set(symbol_ids)),
            'frequency': frequency,
            'bigrams': bigrams,
            'cognitive_axes': [axis.value for axis in axes_used],
            'most_common': max(frequency.items(), key=lambda x: x[1]) if frequency else None
        }
    
    def compare_sequences(self, seq1: List[str], seq2: List[str]) -> Dict[str, any]:
        """
        Compare two sequences for structural similarity.
        """
        analysis1 = self.analyze_sequence(seq1)
        analysis2 = self.analyze_sequence(seq2)
        
        # Find common symbols
        set1 = set(seq1)
        set2 = set(seq2)
        common = set1 & set2
        
        # Calculate Jaccard similarity
        jaccard = len(common) / len(set1 | set2) if (set1 | set2) else 0
        
        return {
            'sequence1_length': len(seq1),
            'sequence2_length': len(seq2),
            'common_symbols': list(common),
            'jaccard_similarity': jaccard,
            'length_ratio': len(seq1) / len(seq2) if seq2 else 0
        }
