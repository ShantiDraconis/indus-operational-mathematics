"""
Holographic Analysis: Implementing the holographic principle for symbol analysis.

This module explores how Indus inscriptions might encode information about larger
institutional systems in a holographic manner - where the part contains information
about the whole.
"""

from typing import Dict, List, Set, Optional
import numpy as np
from collections import defaultdict

from .symbol_system import Symbol, SymbolCorpus, Inscription, SymbolContext


class HolographicAnalyzer:
    """
    Analyzes how small inscriptions might encode information about larger systems.
    
    The holographic principle suggests that information about a volume can be
    encoded on its boundary. Applied to Indus script, a seal inscription might
    encode information about the entire institutional context.
    """
    
    def __init__(self, corpus: SymbolCorpus):
        self.corpus = corpus
        
    def calculate_information_density(self, inscription: Inscription) -> float:
        """
        Calculate the information density of an inscription.
        
        Information density measures how much institutional information is
        encoded per symbol - analogous to the holographic principle where
        surface area limits the information content of a volume.
        
        Args:
            inscription: The inscription to analyze
            
        Returns:
            Information density value
        """
        if not inscription.symbols:
            return 0.0
        
        # Count unique symbols
        unique_symbols = len(set(s.id for s in inscription.symbols))
        
        # Calculate entropy of symbol sequence
        symbol_counts = defaultdict(int)
        for symbol in inscription.symbols:
            symbol_counts[symbol.id] += 1
        
        total = len(inscription.symbols)
        entropy = 0.0
        for count in symbol_counts.values():
            p = count / total
            entropy -= p * np.log2(p + 1e-10)
        
        # Information density: entropy per symbol position
        density = entropy * unique_symbols / len(inscription.symbols)
        
        return density
    
    def identify_holographic_patterns(self) -> Dict[str, any]:
        """
        Identify patterns that appear to encode larger institutional structures.
        
        Looks for short symbol sequences that consistently appear across
        different contexts and locations, suggesting they encode general
        institutional information.
        
        Returns:
            Dictionary with holographic pattern analysis
        """
        # Find symbol sequences (n-grams) that appear in multiple contexts
        sequence_contexts: Dict[str, Set[SymbolContext]] = defaultdict(set)
        sequence_locations: Dict[str, Set[str]] = defaultdict(set)
        sequence_counts: Dict[str, int] = defaultdict(int)
        
        for inscription in self.corpus.inscriptions:
            symbol_ids = [s.id for s in inscription.symbols]
            
            # Extract bigrams and trigrams
            for n in [2, 3]:
                for i in range(len(symbol_ids) - n + 1):
                    sequence = tuple(symbol_ids[i:i+n])
                    sequence_str = '-'.join(sequence)
                    
                    sequence_contexts[sequence_str].add(inscription.context)
                    sequence_locations[sequence_str].add(inscription.location.value)
                    sequence_counts[sequence_str] += 1
        
        # Find sequences that appear in multiple contexts and locations
        holographic_sequences = []
        
        for seq_str, contexts in sequence_contexts.items():
            if len(contexts) >= 2 and len(sequence_locations[seq_str]) >= 2:
                holographic_sequences.append({
                    "sequence": seq_str,
                    "contexts": [c.value for c in contexts],
                    "locations": list(sequence_locations[seq_str]),
                    "occurrences": sequence_counts[seq_str],
                    "context_diversity": len(contexts),
                    "location_diversity": len(sequence_locations[seq_str]),
                })
        
        # Sort by diversity and frequency
        holographic_sequences.sort(
            key=lambda x: (x["context_diversity"] * x["location_diversity"], x["occurrences"]),
            reverse=True
        )
        
        return {
            "total_sequences_analyzed": len(sequence_contexts),
            "holographic_sequences": holographic_sequences[:20],
            "average_context_diversity": np.mean([len(c) for c in sequence_contexts.values()]),
            "average_location_diversity": np.mean([len(l) for l in sequence_locations.values()]),
        }
    
    def analyze_institutional_encoding(self, inscription: Inscription) -> Dict[str, any]:
        """
        Analyze how an inscription might encode institutional information.
        
        Examines the inscription's symbols, their relationships, and context
        to infer what larger institutional structure it might represent.
        
        Args:
            inscription: The inscription to analyze
            
        Returns:
            Analysis of institutional encoding
        """
        if not inscription.symbols:
            return {"error": "Empty inscription"}
        
        # Calculate various metrics
        info_density = self.calculate_information_density(inscription)
        
        # Analyze symbol diversity
        unique_symbols = len(set(s.id for s in inscription.symbols))
        diversity_ratio = unique_symbols / len(inscription.symbols)
        
        # Check if symbols appear in other contexts
        cross_context_symbols = []
        for symbol in inscription.symbols:
            other_inscriptions = self.corpus.get_inscriptions_with_symbol(symbol.id)
            other_contexts = set(i.context for i in other_inscriptions if i.id != inscription.id)
            
            if len(other_contexts) > 0:
                cross_context_symbols.append({
                    "symbol_id": symbol.id,
                    "other_contexts": [c.value for c in other_contexts],
                })
        
        # Infer institutional function based on patterns
        institutional_inference = self._infer_institutional_function(inscription)
        
        return {
            "inscription_id": inscription.id,
            "length": len(inscription.symbols),
            "unique_symbols": unique_symbols,
            "diversity_ratio": diversity_ratio,
            "information_density": info_density,
            "context": inscription.context.value,
            "location": inscription.location.value,
            "cross_context_symbols": cross_context_symbols,
            "holographic_score": info_density * len(cross_context_symbols),
            "institutional_inference": institutional_inference,
        }
    
    def _infer_institutional_function(self, inscription: Inscription) -> str:
        """
        Infer the institutional function based on inscription characteristics.
        
        This is a simplified inference based on patterns. In a full implementation,
        this would use machine learning and more sophisticated analysis.
        """
        info_density = self.calculate_information_density(inscription)
        length = len(inscription.symbols)
        
        if inscription.context == SymbolContext.ADMINISTRATIVE:
            if info_density > 1.5:
                return "High-authority administrative seal (possibly royal or central authority)"
            elif length <= 5:
                return "Standard administrative transaction record"
            else:
                return "Complex administrative document (possibly accounting or inventory)"
        
        elif inscription.context == SymbolContext.RITUAL:
            if info_density > 1.5:
                return "Sacred or ceremonial object with complex symbolic meaning"
            else:
                return "Ritual marker or offering inscription"
        
        elif inscription.context == SymbolContext.TRADE:
            if length <= 4:
                return "Simple trade marker or ownership stamp"
            else:
                return "Trade agreement or complex transaction record"
        
        else:
            return "Unknown function - requires further analysis"
    
    def calculate_boundary_entropy(self, inscriptions: Optional[List[Inscription]] = None) -> float:
        """
        Calculate the boundary entropy of a set of inscriptions.
        
        In holographic principle, the entropy of a volume is proportional to
        the area of its boundary. Here, we calculate how much information is
        encoded in the "boundary" (unique symbols) vs. the "volume" (all symbols).
        
        Args:
            inscriptions: List of inscriptions to analyze (default: all in corpus)
            
        Returns:
            Boundary entropy value
        """
        if inscriptions is None:
            inscriptions = self.corpus.inscriptions
        
        if not inscriptions:
            return 0.0
        
        # Collect all symbols (volume)
        all_symbols = []
        for inscription in inscriptions:
            all_symbols.extend([s.id for s in inscription.symbols])
        
        # Collect unique symbols (boundary)
        unique_symbols = set(all_symbols)
        
        # Calculate entropy of unique symbol distribution
        symbol_counts = defaultdict(int)
        for symbol_id in all_symbols:
            symbol_counts[symbol_id] += 1
        
        total = len(all_symbols)
        boundary_entropy = 0.0
        
        for symbol_id in unique_symbols:
            p = symbol_counts[symbol_id] / total
            boundary_entropy -= p * np.log2(p + 1e-10)
        
        # Normalize by boundary size
        boundary_entropy = boundary_entropy / len(unique_symbols) if unique_symbols else 0
        
        return boundary_entropy
    
    def find_holographic_correspondences(self) -> Dict[str, List[str]]:
        """
        Find correspondences between small inscriptions and larger patterns.
        
        Identifies cases where short inscriptions seem to encode information
        about larger institutional structures, as evidenced by their appearance
        across different scales.
        
        Returns:
            Dictionary mapping inscription patterns to larger contexts
        """
        correspondences: Dict[str, List[str]] = defaultdict(list)
        
        # Group inscriptions by length
        short_inscriptions = [i for i in self.corpus.inscriptions if len(i.symbols) <= 5]
        long_inscriptions = [i for i in self.corpus.inscriptions if len(i.symbols) > 5]
        
        # Find short sequences that appear in longer contexts
        for short_insc in short_inscriptions:
            short_seq = tuple(s.id for s in short_insc.symbols)
            
            for long_insc in long_inscriptions:
                long_seq = tuple(s.id for s in long_insc.symbols)
                
                # Check if short sequence is contained in long sequence
                short_str = '-'.join(short_seq)
                long_str = '-'.join(long_seq)
                
                if short_str in long_str:
                    correspondence = f"{short_insc.location.value} ({short_insc.context.value}) -> {long_insc.location.value} ({long_insc.context.value})"
                    correspondences[short_str].append(correspondence)
        
        return dict(correspondences)
    
    def generate_holographic_report(self) -> Dict[str, any]:
        """
        Generate a comprehensive report on holographic properties of the corpus.
        
        Returns:
            Dictionary with holographic analysis results
        """
        # Analyze holographic patterns
        patterns = self.identify_holographic_patterns()
        
        # Calculate boundary entropy for entire corpus
        total_boundary_entropy = self.calculate_boundary_entropy()
        
        # Find correspondences
        correspondences = self.find_holographic_correspondences()
        
        # Analyze information density distribution
        densities = [
            self.calculate_information_density(insc)
            for insc in self.corpus.inscriptions
        ]
        
        # Find inscriptions with highest holographic potential
        holographic_inscriptions = []
        for inscription in self.corpus.inscriptions:
            analysis = self.analyze_institutional_encoding(inscription)
            holographic_inscriptions.append({
                "id": inscription.id,
                "holographic_score": analysis["holographic_score"],
                "info_density": analysis["information_density"],
                "institutional_function": analysis["institutional_inference"],
            })
        
        holographic_inscriptions.sort(key=lambda x: x["holographic_score"], reverse=True)
        
        return {
            "holographic_patterns": patterns,
            "boundary_entropy": total_boundary_entropy,
            "correspondences_found": len(correspondences),
            "top_holographic_inscriptions": holographic_inscriptions[:10],
            "average_information_density": np.mean(densities) if densities else 0,
            "information_density_std": np.std(densities) if densities else 0,
        }
