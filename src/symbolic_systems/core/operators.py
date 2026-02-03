"""
Core operators and cognitive axes for universal symbolic grammar.

This module defines the 15 universal cognitive operators and 7 fundamental
cognitive axes identified across all human symbolic systems.
"""

from enum import Enum
from typing import List, Optional
from dataclasses import dataclass


class CognitiveAxis(Enum):
    """The 7 fundamental cognitive dimensions found in all symbolic systems."""
    
    PRESENCE = "presence_absence"  # Existence
    QUANTITY = "quantity_measure"  # Cardinality
    QUALITY = "quality_state"      # Attribution
    RELATION = "relation_bond"     # Connectivity
    SPACE = "space_domain"         # Location
    TIME = "time_phase"            # Temporality
    VALIDATION = "validation_closure"  # Completeness


@dataclass
class UniversalOperator:
    """
    Represents one of the 15 universal cognitive operators found across
    all human symbolic systems.
    
    These operators are basic graphical forms that carry consistent
    semantic functions across cultures.
    """
    
    name: str
    form: str
    function: str
    cognitive_axes: List[CognitiveAxis]
    examples: List[str]
    
    def __repr__(self):
        return f"UniversalOperator({self.name}, form='{self.form}')"


# The 15 Universal Cognitive Operators
UNIVERSAL_OPERATORS = [
    UniversalOperator(
        name="Point",
        form="•",
        function="Instance, unit, focus",
        cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUANTITY],
        examples=["Harappan 27", "Mayan numeral dot", "Aztec dot"]
    ),
    UniversalOperator(
        name="Line",
        form="|",
        function="Axis, individual, direction",
        cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.RELATION],
        examples=["Harappan 1", "Runic Isa", "Chinese 一"]
    ),
    UniversalOperator(
        name="Cross",
        form="X",
        function="Relation, exchange, connection",
        cognitive_axes=[CognitiveAxis.RELATION, CognitiveAxis.SPACE],
        examples=["Harappan 4", "Runic Gebo", "Aztec directional cross"]
    ),
    UniversalOperator(
        name="Circle",
        form="○",
        function="Totality, cycle, sun",
        cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.SPACE],
        examples=["Phaistos Disc sun", "Aztec Stone of the Sun"]
    ),
    UniversalOperator(
        name="Triangle",
        form="△",
        function="Power, ascension, fire",
        cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.SPACE],
        examples=["Harappan crowns", "Egyptian pyramid"]
    ),
    UniversalOperator(
        name="Square",
        form="□",
        function="Domain, house, institution",
        cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.VALIDATION],
        examples=["Harappan house", "Chinese 口", "Mayan temple"]
    ),
    UniversalOperator(
        name="Wave",
        form="~",
        function="Water, flow, transformation",
        cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.TIME],
        examples=["Phaistos Disc A12", "Chinese 水"]
    ),
    UniversalOperator(
        name="Spiral",
        form="⦾",
        function="Time, cycle, evolution",
        cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.QUALITY],
        examples=["Phaistos Disc form", "Mayan temporal concept"]
    ),
    UniversalOperator(
        name="Hand",
        form="✋",
        function="Action, possession, power",
        cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.RELATION],
        examples=["Rongorongo hands", "Egyptian hand"]
    ),
    UniversalOperator(
        name="Foot",
        form="👣",
        function="Movement, journey, conquest",
        cognitive_axes=[CognitiveAxis.SPACE, CognitiveAxis.TIME],
        examples=["Aztec footprints", "Egyptian path"]
    ),
    UniversalOperator(
        name="Head",
        form="👤",
        function="Person, identity, lord",
        cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUALITY],
        examples=["Harappan 26", "Mayan head glyph"]
    ),
    UniversalOperator(
        name="Eye",
        form="👁",
        function="Vision, knowledge, vigilance",
        cognitive_axes=[CognitiveAxis.QUALITY, CognitiveAxis.PRESENCE],
        examples=["Egyptian Eye of Horus", "Mesopotamian eye"]
    ),
    UniversalOperator(
        name="Mouth",
        form="👄",
        function="Speech, consumption, portal",
        cognitive_axes=[CognitiveAxis.RELATION, CognitiveAxis.QUALITY],
        examples=["Chinese 口", "Mayan speech glyph"]
    ),
    UniversalOperator(
        name="Heart",
        form="💓",
        function="Life, emotion, center",
        cognitive_axes=[CognitiveAxis.PRESENCE, CognitiveAxis.QUALITY],
        examples=["Egyptian heart", "Mesoamerican sacrificed heart"]
    ),
    UniversalOperator(
        name="Plant",
        form="🌱",
        function="Growth, food, cycle",
        cognitive_axes=[CognitiveAxis.TIME, CognitiveAxis.PRESENCE],
        examples=["Harappan plant", "Mayan maize"]
    ),
]


def get_operator_by_name(name: str) -> Optional[UniversalOperator]:
    """Retrieve an operator by name."""
    for op in UNIVERSAL_OPERATORS:
        if op.name.lower() == name.lower():
            return op
    return None


def get_operators_by_axis(axis: CognitiveAxis) -> List[UniversalOperator]:
    """Get all operators associated with a specific cognitive axis."""
    return [op for op in UNIVERSAL_OPERATORS if axis in op.cognitive_axes]
