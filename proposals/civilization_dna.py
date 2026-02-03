"""
DNA of Civilization - Complex Network Analysis

Proposal 3: Model Harappan cities as graphs where:
- Nodes = Symbols (417 types)
- Edges = Co-occurrences
- Communities = Functional families

Algorithm: Apply community detection to discover "administrative organs"
"""

import networkx as nx
from typing import Dict, List, Set, Tuple
from collections import defaultdict
from dataclasses import dataclass
from core.harappan_automaton import ENTITY_MEANINGS, RELATION_MEANINGS, CLOSURE_MEANINGS


@dataclass
class SymbolNode:
    """A node in the civilization graph"""
    symbol_id: int
    symbol_type: str
    frequency: int = 0
    meaning: str = ""


class CivilizationGraph:
    """
    Graph model of Harappan civilization
    
    Analyzes co-occurrence patterns to discover institutional structures
    """
    
    def __init__(self):
        self.graph = nx.Graph()
        self.symbol_nodes: Dict[int, SymbolNode] = {}
        self.inscriptions: List[List[int]] = []
        
    def add_inscription(self, symbols: List[int]):
        """Add an inscription to the graph"""
        self.inscriptions.append(symbols)
        
        # Add nodes for symbols
        for symbol_id in symbols:
            if symbol_id not in self.symbol_nodes:
                meaning = self._get_meaning(symbol_id)
                symbol_type = self._get_symbol_type(symbol_id)
                self.symbol_nodes[symbol_id] = SymbolNode(
                    symbol_id=symbol_id,
                    symbol_type=symbol_type,
                    meaning=meaning,
                    frequency=0
                )
                self.graph.add_node(symbol_id, **self.symbol_nodes[symbol_id].__dict__)
            
            self.symbol_nodes[symbol_id].frequency += 1
            self.graph.nodes[symbol_id]['frequency'] = self.symbol_nodes[symbol_id].frequency
        
        # Add edges for co-occurrences
        for i in range(len(symbols)):
            for j in range(i + 1, len(symbols)):
                if self.graph.has_edge(symbols[i], symbols[j]):
                    self.graph[symbols[i]][symbols[j]]['weight'] += 1
                else:
                    self.graph.add_edge(symbols[i], symbols[j], weight=1)
    
    def _get_symbol_type(self, symbol_id: int) -> str:
        """Determine symbol type from ID"""
        if 342 <= symbol_id <= 348:
            return "closure"
        elif 373 <= symbol_id <= 399:
            return "entity"
        elif 400 <= symbol_id <= 409:
            return "relation"
        else:
            return "unknown"
    
    def _get_meaning(self, symbol_id: int) -> str:
        """Get semantic meaning of symbol"""
        if symbol_id in ENTITY_MEANINGS:
            return ENTITY_MEANINGS[symbol_id]
        elif symbol_id in RELATION_MEANINGS:
            return RELATION_MEANINGS[symbol_id]
        elif symbol_id in CLOSURE_MEANINGS:
            return CLOSURE_MEANINGS[symbol_id]
        return "Unknown"
    
    def detect_communities(self) -> Dict[int, Set[int]]:
        """
        Detect communities (functional families) in the graph
        
        Returns:
            Dictionary mapping community_id to set of symbol_ids
        """
        # Use Louvain method for community detection
        try:
            import community as community_louvain
            partition = community_louvain.best_partition(self.graph, weight='weight')
        except ImportError:
            # Fallback to greedy modularity
            communities = nx.community.greedy_modularity_communities(self.graph, weight='weight')
            partition = {}
            for comm_id, community in enumerate(communities):
                for node in community:
                    partition[node] = comm_id
        
        # Group by community
        communities_dict = defaultdict(set)
        for node, comm_id in partition.items():
            communities_dict[comm_id].add(node)
        
        return dict(communities_dict)
    
    def find_administrative_organs(self) -> List[Dict]:
        """
        Discover administrative organs from communities
        
        Returns:
            List of administrative structures with their characteristics
        """
        communities = self.detect_communities()
        organs = []
        
        for comm_id, symbols in communities.items():
            # Analyze community composition
            entities = [s for s in symbols if 373 <= s <= 399]
            relations = [s for s in symbols if 400 <= s <= 409]
            closures = [s for s in symbols if 342 <= s <= 348]
            
            # Calculate characteristics
            total_freq = sum(self.symbol_nodes[s].frequency for s in symbols if s in self.symbol_nodes)
            
            organ = {
                'id': comm_id,
                'size': len(symbols),
                'entities': entities,
                'relations': relations,
                'closures': closures,
                'total_frequency': total_freq,
                'type': self._classify_organ(entities, relations, closures),
                'symbols': list(symbols),
            }
            organs.append(organ)
        
        return sorted(organs, key=lambda x: x['total_frequency'], reverse=True)
    
    def _classify_organ(self, entities: List[int], relations: List[int], closures: List[int]) -> str:
        """Classify administrative organ type"""
        # Simple classification based on composition
        if not entities:
            return "Unknown"
        
        # Check for specific patterns
        has_authority = 377 in entities
        has_transaction = 376 in entities
        has_trade = 406 in relations
        has_taxation = 407 in relations
        
        if has_authority and has_taxation:
            return "Tax Authority"
        elif has_transaction and has_trade:
            return "Trade Administration"
        elif 375 in entities:  # Goods
            return "Resource Management"
        elif 378 in entities:  # Location
            return "Geographic Administration"
        else:
            return "General Administration"
    
    def get_most_central_symbols(self, n: int = 10) -> List[Tuple[int, float]]:
        """
        Find most central symbols (hubs in the network)
        
        Args:
            n: Number of top symbols to return
        
        Returns:
            List of (symbol_id, centrality_score) tuples
        """
        if len(self.graph) == 0:
            return []
        
        centrality = nx.degree_centrality(self.graph)
        sorted_symbols = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        return sorted_symbols[:n]
    
    def get_network_stats(self) -> Dict:
        """Get overall network statistics"""
        if len(self.graph) == 0:
            return {
                'nodes': 0,
                'edges': 0,
                'density': 0,
                'inscriptions': 0,
            }
        
        return {
            'nodes': self.graph.number_of_nodes(),
            'edges': self.graph.number_of_edges(),
            'density': nx.density(self.graph),
            'avg_clustering': nx.average_clustering(self.graph),
            'inscriptions': len(self.inscriptions),
        }
    
    def reconstruct_institutions(self) -> Dict[str, List[str]]:
        """
        Reconstruct institutional map from network analysis
        
        Returns:
            Dictionary of institution types and their associated symbols
        """
        organs = self.find_administrative_organs()
        institutions = defaultdict(list)
        
        for organ in organs:
            organ_type = organ['type']
            symbol_meanings = [
                self._get_meaning(s) for s in organ['symbols']
                if s in self.symbol_nodes
            ]
            institutions[organ_type].extend(symbol_meanings)
        
        return dict(institutions)
