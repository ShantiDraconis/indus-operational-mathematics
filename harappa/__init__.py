"""
Harappa Operational Mathematics System

A formal system based on Indus Valley civilization principles for
modern computational applications.
"""

__version__ = "0.1.0"
__author__ = "Harappa Project Contributors"

from .core import (
    Symbol,
    Operator,
    State,
    Record,
    ValidationEngine,
    SymbolType,
    OperatorType,
)
from .spec_lang import HarappaSpec, StateMachine, Transition, Contract, ContractMethod
from .uid import HarappaUID, UIDType, UIDRegistry, ValidationStatus
from .proof import ProofSystem, ProofStep, Theorem, Proof, DiagrammaticProofBuilder

__all__ = [
    # Core
    "Symbol",
    "Operator",
    "State",
    "Record",
    "ValidationEngine",
    "SymbolType",
    "OperatorType",
    # Spec Language
    "HarappaSpec",
    "StateMachine",
    "Transition",
    "Contract",
    "ContractMethod",
    # UID System
    "HarappaUID",
    "UIDType",
    "UIDRegistry",
    "ValidationStatus",
    # Proof System
    "ProofSystem",
    "ProofStep",
    "Theorem",
    "Proof",
    "DiagrammaticProofBuilder",
]
