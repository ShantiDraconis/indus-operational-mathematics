"""
Indus Script Operator Model

This module provides classes and functions for modeling the operational
structure of Indus script inscriptions according to the five-operator
taxonomy developed in the monograph.
"""

from typing import List, Optional, Dict, Set
from dataclasses import dataclass, field
from enum import Enum


class Operator(Enum):
    """Five primary operators in the Indus operational system."""
    INSTANTIATION = "INST"
    COUNTING = "COUNT"
    RELATION = "REL"
    QUALIFICATION = "QUAL"
    CLOSURE = "CLOSE"


@dataclass
class OperationalSign:
    """
    Represents a sign with its operational function.
    """
    sign_id: str
    operator: Operator
    cardinality: Optional[int] = None  # For counting signs
    qualifier_type: Optional[str] = None  # For qualification signs
    
    def __str__(self) -> str:
        if self.operator == Operator.COUNTING and self.cardinality:
            return f"{self.sign_id}({self.operator.value}:{self.cardinality})"
        elif self.operator == Operator.QUALIFICATION and self.qualifier_type:
            return f"{self.sign_id}({self.operator.value}:{self.qualifier_type})"
        return f"{self.sign_id}({self.operator.value})"


@dataclass
class Inscription:
    """
    Represents a complete Indus inscription with operational structure.
    """
    inscription_id: str
    signs: List[OperationalSign]
    site: Optional[str] = None
    object_type: Optional[str] = None
    
    def __post_init__(self):
        self.operations = [sign.operator for sign in self.signs]
    
    def has_operator(self, operator: Operator) -> bool:
        """Check if inscription contains a specific operator."""
        return operator in self.operations
    
    def get_operators_by_type(self, operator: Operator) -> List[OperationalSign]:
        """Get all signs with a specific operator type."""
        return [sign for sign in self.signs if sign.operator == operator]
    
    def length(self) -> int:
        """Return inscription length."""
        return len(self.signs)
    
    def is_closed(self) -> bool:
        """Check if inscription has closure operator."""
        return self.has_operator(Operator.CLOSURE)
    
    def total_count(self) -> int:
        """Calculate total count from all counting operators."""
        counting_signs = self.get_operators_by_type(Operator.COUNTING)
        return sum(sign.cardinality or 0 for sign in counting_signs)
    
    def operational_pattern(self) -> str:
        """Return the operational pattern as a string."""
        return "-".join(op.value for op in self.operations)


class InscriptionAnalyzer:
    """
    Analyzes collections of inscriptions for operational patterns.
    """
    
    def __init__(self):
        self.inscriptions: List[Inscription] = []
    
    def add_inscription(self, inscription: Inscription):
        """Add an inscription to the analyzer."""
        self.inscriptions.append(inscription)
    
    def count_by_operator(self, operator: Operator) -> int:
        """Count inscriptions containing a specific operator."""
        return sum(1 for insc in self.inscriptions if insc.has_operator(operator))
    
    def average_length(self) -> float:
        """Calculate average inscription length."""
        if not self.inscriptions:
            return 0.0
        return sum(insc.length() for insc in self.inscriptions) / len(self.inscriptions)
    
    def closure_rate(self) -> float:
        """Calculate percentage of inscriptions with closure."""
        if not self.inscriptions:
            return 0.0
        closed = sum(1 for insc in self.inscriptions if insc.is_closed())
        return (closed / len(self.inscriptions)) * 100
    
    def pattern_frequency(self) -> Dict[str, int]:
        """Calculate frequency of operational patterns."""
        patterns = {}
        for insc in self.inscriptions:
            pattern = insc.operational_pattern()
            patterns[pattern] = patterns.get(pattern, 0) + 1
        return dict(sorted(patterns.items(), key=lambda x: x[1], reverse=True))
    
    def operator_statistics(self) -> Dict[str, Dict]:
        """Generate statistics for each operator type."""
        stats = {}
        for operator in Operator:
            count = self.count_by_operator(operator)
            percentage = (count / len(self.inscriptions) * 100) if self.inscriptions else 0
            stats[operator.value] = {
                "count": count,
                "percentage": percentage
            }
        return stats


def create_sample_corpus() -> List[Inscription]:
    """Create a sample corpus for demonstration."""
    corpus = [
        Inscription(
            "H-001",
            [
                OperationalSign("M361", Operator.INSTANTIATION),
                OperationalSign("M328", Operator.COUNTING, cardinality=3),
                OperationalSign("M411", Operator.CLOSURE)
            ],
            site="Harappa",
            object_type="seal"
        ),
        Inscription(
            "M-002",
            [
                OperationalSign("M346", Operator.INSTANTIATION),
                OperationalSign("M329", Operator.COUNTING, cardinality=5)
            ],
            site="Mohenjo-daro",
            object_type="seal"
        ),
        Inscription(
            "H-003",
            [
                OperationalSign("M361", Operator.INSTANTIATION),
                OperationalSign("M347", Operator.QUALIFICATION, qualifier_type="size"),
                OperationalSign("M328", Operator.COUNTING, cardinality=2),
                OperationalSign("M411", Operator.CLOSURE)
            ],
            site="Harappa",
            object_type="tablet"
        ),
    ]
    return corpus


if __name__ == "__main__":
    # Demonstration
    print("Indus Script Operator Model Demonstration\n")
    
    corpus = create_sample_corpus()
    analyzer = InscriptionAnalyzer()
    
    for inscription in corpus:
        analyzer.add_inscription(inscription)
        print(f"Inscription: {inscription.inscription_id}")
        print(f"  Site: {inscription.site}")
        print(f"  Pattern: {inscription.operational_pattern()}")
        print(f"  Length: {inscription.length()}")
        print(f"  Closed: {inscription.is_closed()}")
        print()
    
    print("\nCorpus Statistics:")
    print(f"Average length: {analyzer.average_length():.2f}")
    print(f"Closure rate: {analyzer.closure_rate():.1f}%")
    print("\nOperator statistics:")
    for op, stats in analyzer.operator_statistics().items():
        print(f"  {op}: {stats['count']} ({stats['percentage']:.1f}%)")
    
    print("\nPattern frequency:")
    for pattern, count in analyzer.pattern_frequency().items():
        print(f"  {pattern}: {count}")
