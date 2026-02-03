"""
Harappan to JSON Converter
Converts Indus script sequences to structured JSON format.
"""

import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class IndusRecord:
    """Structured representation of an Indus record"""
    entity: Optional[str] = None
    qualifiers: List[str] = None
    quantity: Optional[int] = None
    relations: List[str] = None
    closure: Optional[str] = None
    
    def __post_init__(self):
        if self.qualifiers is None:
            self.qualifiers = []
        if self.relations is None:
            self.relations = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return asdict(self)
    
    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=indent)


class HarappanToJsonConverter:
    """
    Converts Harappan sign sequences to JSON structural format.
    
    Based on the mapping table from the formal model.
    """
    
    def __init__(self):
        self.entity_map = self._create_entity_map()
        self.closure_map = self._create_closure_map()
        self.quantity_map = self._create_quantity_map()
        self.relation_map = self._create_relation_map()
        self.qualifier_map = self._create_qualifier_map()
    
    def _create_entity_map(self) -> Dict[int, str]:
        """Create mapping for entity symbols"""
        mapping = {}
        
        # ENT_OVAL: 373-399
        for i in range(373, 400):
            mapping[i] = f"oval_entity_{i}"
        mapping[373] = "basic_token"
        mapping[374] = "administrative_unit"
        mapping[375] = "institutional_seal"
        
        # ENT_U: 328-339
        for i in range(328, 340):
            mapping[i] = f"container_{i}"
        mapping[328] = "vessel_small"
        mapping[329] = "vessel_medium"
        mapping[330] = "vessel_large"
        
        # ENT_HASTE: 250-260
        for i in range(250, 261):
            mapping[i] = f"authority_{i}"
        mapping[250] = "staff_simple"
        mapping[251] = "staff_decorated"
        
        # ENT_ANIMAL: 200-210
        for i in range(200, 211):
            mapping[i] = f"animal_{i}"
        mapping[200] = "unicorn"
        mapping[201] = "bull"
        mapping[202] = "elephant"
        
        # ENT_METRICA: 100-150
        for i in range(100, 151):
            mapping[i] = f"measure_{i}"
        mapping[100] = "weight_unit"
        mapping[101] = "length_unit"
        
        return mapping
    
    def _create_closure_map(self) -> Dict[int, str]:
        """Create mapping for closure symbols"""
        return {
            342: "simple",
            343: "confirmed",
            344: "validated",
            345: "sealed",
            346: "absolute",
            347: "hierarchical",
            348: "terminal"
        }
    
    def _create_quantity_map(self) -> Dict[int, int]:
        """Create mapping for quantity symbols"""
        return {
            410: 1,
            411: 2,
            412: 3,
            413: 4,
            414: 5,
            415: 10,
            416: 20,
            417: 100
        }
    
    def _create_relation_map(self) -> Dict[int, str]:
        """Create mapping for relation symbols"""
        return {
            400: "pair",
            401: "sequence",
            402: "hierarchy",
            403: "exchange",
            404: "transformation",
            405: "possession",
            406: "containment",
            407: "production",
            408: "distribution",
            409: "validation"
        }
    
    def _create_qualifier_map(self) -> Dict[str, str]:
        """Create mapping for qualifier symbols (non-numeric)"""
        return {
            "dot": "marked",
            "stroke": "counted",
            "crown": "elevated",
            "sidebars": "bounded",
            "fill": "solid"
        }
    
    def convert(self, sign_sequence: List[int]) -> IndusRecord:
        """
        Convert a sequence of Harappan sign IDs to structured JSON.
        
        Args:
            sign_sequence: List of sign IDs
            
        Returns:
            IndusRecord object with structured data
        """
        record = IndusRecord()
        
        for sign in sign_sequence:
            # Check entity
            if sign in self.entity_map:
                if record.entity is None:
                    record.entity = self.entity_map[sign]
            
            # Check closure
            elif sign in self.closure_map:
                record.closure = self.closure_map[sign]
            
            # Check quantity
            elif sign in self.quantity_map:
                if record.quantity is None:
                    record.quantity = 0
                record.quantity += self.quantity_map[sign]
            
            # Check relation
            elif sign in self.relation_map:
                record.relations.append(self.relation_map[sign])
        
        return record
    
    def convert_to_json(self, sign_sequence: List[int], indent: int = 2) -> str:
        """
        Convert sign sequence directly to JSON string.
        
        Args:
            sign_sequence: List of sign IDs
            indent: JSON indentation level
            
        Returns:
            JSON string representation
        """
        record = self.convert(sign_sequence)
        return record.to_json(indent=indent)
    
    def batch_convert(self, sequences: List[List[int]]) -> List[IndusRecord]:
        """
        Convert multiple sequences.
        
        Args:
            sequences: List of sign sequences
            
        Returns:
            List of IndusRecord objects
        """
        return [self.convert(seq) for seq in sequences]


def harappan_to_json(sign_sequence: List[int]) -> Dict[str, Any]:
    """
    Convenience function to convert Harappan sequence to JSON dict.
    
    Args:
        sign_sequence: List of sign IDs
        
    Returns:
        Dictionary representation of the record
    """
    converter = HarappanToJsonConverter()
    record = converter.convert(sign_sequence)
    return record.to_dict()


if __name__ == "__main__":
    # Example usage
    print("Harappan to JSON Converter - Examples")
    print("=" * 50)
    
    converter = HarappanToJsonConverter()
    
    # Example 1: Simple record
    sequence1 = [373, 342]
    record1 = converter.convert(sequence1)
    print(f"\nSequence: {sequence1}")
    print(record1.to_json())
    
    # Example 2: Record with quantity
    sequence2 = [373, 410, 411, 342]
    record2 = converter.convert(sequence2)
    print(f"\nSequence: {sequence2}")
    print(record2.to_json())
    
    # Example 3: Record with relation
    sequence3 = [373, 400, 346]
    record3 = converter.convert(sequence3)
    print(f"\nSequence: {sequence3}")
    print(record3.to_json())
    
    # Example 4: Complex record
    sequence4 = [200, 410, 411, 400, 343]
    record4 = converter.convert(sequence4)
    print(f"\nSequence: {sequence4}")
    print(record4.to_json())
