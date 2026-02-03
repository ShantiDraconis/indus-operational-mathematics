"""
Visualization: Tools for visualizing quantum-like symbol relationships.

This module provides functions to create network graphs and visualizations
of symbol correlations, entanglement patterns, and holographic structures.
"""

from typing import Dict, List, Tuple, Optional
import json

from .symbol_system import SymbolCorpus
from .entanglement_analysis import EntanglementAnalyzer


class QuantumNetworkVisualizer:
    """
    Creates visualizations of symbol networks with quantum-inspired metrics.
    """
    
    def __init__(self, corpus: SymbolCorpus, analyzer: EntanglementAnalyzer):
        self.corpus = corpus
        self.analyzer = analyzer
        
    def generate_network_data(self, min_correlation: float = 0.2) -> Dict[str, any]:
        """
        Generate network data for visualization.
        
        Creates nodes (symbols) and edges (correlations) that can be visualized
        using network visualization tools like D3.js, Gephi, or NetworkX.
        
        Args:
            min_correlation: Minimum mutual information to include edge
            
        Returns:
            Dictionary with nodes and edges data
        """
        nodes = []
        edges = []
        
        symbol_ids = list(self.corpus.symbols.keys())
        
        # Create nodes
        for symbol_id in symbol_ids:
            symbol = self.corpus.get_symbol(symbol_id)
            entropy = self.analyzer.calculate_entanglement_entropy(symbol_id)
            non_locality = self.analyzer.calculate_non_locality_index(symbol_id)
            
            nodes.append({
                "id": symbol_id,
                "label": symbol.name,
                "frequency": symbol.frequency,
                "entanglement_entropy": entropy,
                "non_locality_index": non_locality,
                "size": symbol.frequency,  # For visualization sizing
            })
        
        # Create edges
        for i, sid1 in enumerate(symbol_ids):
            for sid2 in symbol_ids[i+1:]:
                mi = self.analyzer.calculate_mutual_information(sid1, sid2)
                
                if mi >= min_correlation:
                    edges.append({
                        "source": sid1,
                        "target": sid2,
                        "mutual_information": mi,
                        "weight": mi,  # For visualization
                    })
        
        return {
            "nodes": nodes,
            "edges": edges,
            "metadata": {
                "total_nodes": len(nodes),
                "total_edges": len(edges),
                "min_correlation_threshold": min_correlation,
            }
        }
    
    def export_to_json(self, filename: str, min_correlation: float = 0.2) -> None:
        """
        Export network data to JSON file for external visualization.
        
        Args:
            filename: Output filename
            min_correlation: Minimum correlation threshold
        """
        network_data = self.generate_network_data(min_correlation)
        
        with open(filename, 'w') as f:
            json.dump(network_data, f, indent=2)
    
    def generate_ascii_network(self, symbol_id: str, max_neighbors: int = 5) -> str:
        """
        Generate a simple ASCII visualization of a symbol's network.
        
        Args:
            symbol_id: Central symbol to visualize
            max_neighbors: Maximum number of neighbors to show
            
        Returns:
            ASCII art string representation
        """
        symbol = self.corpus.get_symbol(symbol_id)
        if not symbol:
            return f"Symbol {symbol_id} not found"
        
        neighbors = self.corpus.get_symbol_neighbors(symbol_id, max_distance=2)
        
        # Sort by frequency and take top N
        top_neighbors = sorted(neighbors.items(), key=lambda x: x[1], reverse=True)[:max_neighbors]
        
        lines = []
        lines.append(f"\nSymbol Network for: {symbol.name} ({symbol_id})")
        lines.append(f"Frequency: {symbol.frequency}")
        lines.append(f"Entanglement Entropy: {self.analyzer.calculate_entanglement_entropy(symbol_id):.3f}")
        lines.append(f"Non-Locality Index: {self.analyzer.calculate_non_locality_index(symbol_id):.3f}")
        lines.append("\nTop Connected Symbols:")
        lines.append("=" * 60)
        
        for neighbor_id, count in top_neighbors:
            neighbor_symbol = self.corpus.get_symbol(neighbor_id)
            mi = self.analyzer.calculate_mutual_information(symbol_id, neighbor_id)
            
            # Create visual representation of connection strength
            bar_length = int(mi * 20)
            bar = "█" * bar_length
            
            lines.append(f"{neighbor_symbol.name:20} | {bar:20} | MI: {mi:.3f} | Co-occur: {count}")
        
        return "\n".join(lines)
    
    def generate_entanglement_matrix(self, symbol_ids: Optional[List[str]] = None) -> str:
        """
        Generate a text-based matrix showing entanglement between symbols.
        
        Args:
            symbol_ids: List of symbol IDs to include (default: all)
            
        Returns:
            Formatted matrix string
        """
        if symbol_ids is None:
            symbol_ids = list(self.corpus.symbols.keys())[:10]  # Limit to 10 for readability
        
        lines = []
        lines.append("\nMutual Information Matrix:")
        lines.append("=" * 80)
        
        # Header
        header = "        "
        for sid in symbol_ids:
            symbol = self.corpus.get_symbol(sid)
            header += f"{symbol.name[:6]:>8}"
        lines.append(header)
        lines.append("-" * 80)
        
        # Matrix rows
        for sid1 in symbol_ids:
            symbol1 = self.corpus.get_symbol(sid1)
            row = f"{symbol1.name[:6]:8}"
            
            for sid2 in symbol_ids:
                if sid1 == sid2:
                    row += f"{'---':>8}"
                else:
                    mi = self.analyzer.calculate_mutual_information(sid1, sid2)
                    row += f"{mi:>8.3f}"
            
            lines.append(row)
        
        return "\n".join(lines)
    
    def create_visualization_report(self) -> str:
        """
        Create a comprehensive text-based visualization report.
        
        Returns:
            Formatted report string
        """
        lines = []
        lines.append("=" * 80)
        lines.append("QUANTUM ARCHAEOLOGY: SYMBOL NETWORK VISUALIZATION REPORT")
        lines.append("=" * 80)
        
        # Corpus statistics
        stats = self.corpus.get_corpus_statistics()
        lines.append("\nCorpus Statistics:")
        lines.append("-" * 40)
        for key, value in stats.items():
            lines.append(f"  {key.replace('_', ' ').title():30}: {value}")
        
        # Most entangled symbols
        lines.append("\n\nMost Entangled Symbols (High Quantum Correlation):")
        lines.append("-" * 40)
        
        entropies = []
        for symbol_id in list(self.corpus.symbols.keys()):
            entropy = self.analyzer.calculate_entanglement_entropy(symbol_id)
            entropies.append((symbol_id, entropy))
        
        entropies.sort(key=lambda x: x[1], reverse=True)
        
        for i, (symbol_id, entropy) in enumerate(entropies[:10], 1):
            symbol = self.corpus.get_symbol(symbol_id)
            lines.append(f"  {i:2}. {symbol.name:20} | Entropy: {entropy:6.3f} | Freq: {symbol.frequency:4}")
        
        # Most non-local symbols
        lines.append("\n\nMost Non-Local Symbols (Appear Across Sites):")
        lines.append("-" * 40)
        
        non_localities = []
        for symbol_id in list(self.corpus.symbols.keys()):
            nl = self.analyzer.calculate_non_locality_index(symbol_id)
            non_localities.append((symbol_id, nl))
        
        non_localities.sort(key=lambda x: x[1], reverse=True)
        
        for i, (symbol_id, nl) in enumerate(non_localities[:10], 1):
            symbol = self.corpus.get_symbol(symbol_id)
            locations = self.corpus.get_location_distribution(symbol_id)
            lines.append(f"  {i:2}. {symbol.name:20} | Non-Locality: {nl:5.3f} | Sites: {len(locations)}")
        
        # Entangled clusters
        lines.append("\n\nEntangled Symbol Clusters:")
        lines.append("-" * 40)
        
        clusters = self.analyzer.find_entangled_clusters(min_correlation=0.3)
        
        for i, cluster in enumerate(clusters[:5], 1):
            cluster_names = [self.corpus.get_symbol(sid).name for sid in cluster]
            lines.append(f"  Cluster {i}: {', '.join(cluster_names)}")
        
        lines.append("\n" + "=" * 80)
        
        return "\n".join(lines)
