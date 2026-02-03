"""
Harappa Universal Unique Identification System (Harappa-UID)

Implements Proposal 2: Hierarchical, semantically rich unique identifiers
using Harappa symbol composition.

Features:
- Hierarchical structure encoding
- Semantic information in UIDs
- Type, context, and relationship encoding
- Validation state tracking
- Applications in supply chain, legal documents, and digital assets
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import time

from .core import Symbol, SymbolType


class UIDType(Enum):
    """Types of UIDs in the system."""
    ASSET = "asset"
    DOCUMENT = "document"
    TRANSACTION = "transaction"
    ENTITY = "entity"
    RESOURCE = "resource"


class ValidationStatus(Enum):
    """Validation status of a UID."""
    UNVALIDATED = "unvalidated"
    PENDING = "pending"
    VALIDATED = "validated"
    REJECTED = "rejected"
    EXPIRED = "expired"


@dataclass
class HarappaUID:
    """
    A Harappa Universal Unique Identifier.
    
    Encodes hierarchical and semantic information using symbol composition.
    Format: PREFIX-TYPE-CONTEXT-SEQUENCE-CHECKSUM
    """
    uid_type: UIDType
    context: str
    symbols: List[Symbol] = field(default_factory=list)
    hierarchy_level: int = 0
    parent_uid: Optional['HarappaUID'] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    validation_status: ValidationStatus = ValidationStatus.UNVALIDATED
    timestamp: float = field(default_factory=time.time)
    _uid_string: Optional[str] = None
    
    def add_symbol(self, symbol: Symbol) -> None:
        """Add a symbol to the UID composition."""
        self.symbols.append(symbol)
        self._uid_string = None  # Invalidate cached UID string
    
    def set_parent(self, parent: 'HarappaUID') -> None:
        """Set the parent UID in the hierarchy."""
        self.parent_uid = parent
        self.hierarchy_level = parent.hierarchy_level + 1
        self._uid_string = None
    
    def generate_uid_string(self) -> str:
        """
        Generate the UID string representation.
        
        Format: HRPA-{TYPE}-{CONTEXT}-{SYMBOL_HASH}-{CHECKSUM}
        """
        if self._uid_string:
            return self._uid_string
        
        # Build symbol signature
        symbol_sig = "".join([s.id for s in self.symbols])
        symbol_hash = hashlib.sha256(symbol_sig.encode()).hexdigest()[:8]
        
        # Include parent UID if hierarchical
        if self.parent_uid:
            parent_part = f"{self.parent_uid.generate_uid_string()}"
            base = f"HRPA-{self.uid_type.value}-{self.context}-{parent_part}-{symbol_hash}"
        else:
            base = f"HRPA-{self.uid_type.value}-{self.context}-{symbol_hash}"
        
        # Add timestamp component
        ts_component = hashlib.sha256(str(self.timestamp).encode()).hexdigest()[:4]
        base = f"{base}-{ts_component}"
        
        # Calculate checksum
        checksum = self._calculate_checksum(base)
        
        self._uid_string = f"{base}-{checksum}"
        return self._uid_string
    
    def _calculate_checksum(self, data: str) -> str:
        """Calculate checksum for UID validation."""
        return hashlib.sha256(data.encode()).hexdigest()[:4]
    
    def validate_checksum(self) -> bool:
        """Validate the UID checksum."""
        uid_str = self.generate_uid_string()
        parts = uid_str.split('-')
        if len(parts) < 2:
            return False
        
        checksum = parts[-1]
        base = '-'.join(parts[:-1])
        expected_checksum = self._calculate_checksum(base)
        
        return checksum == expected_checksum
    
    def set_validation_status(self, status: ValidationStatus) -> None:
        """Set the validation status of the UID."""
        self.validation_status = status
        self.metadata["validation_timestamp"] = time.time()
    
    def encode_metadata(self, key: str, value: Any) -> None:
        """Encode metadata into the UID."""
        self.metadata[key] = value
        self._uid_string = None
    
    def get_hierarchy_path(self) -> List['HarappaUID']:
        """Get the full hierarchy path from root to this UID."""
        path = []
        current = self
        while current:
            path.insert(0, current)
            current = current.parent_uid
        return path
    
    def is_child_of(self, potential_parent: 'HarappaUID') -> bool:
        """Check if this UID is a child of the given UID."""
        current = self.parent_uid
        while current:
            if current == potential_parent:
                return True
            current = current.parent_uid
        return False
    
    def get_semantic_info(self) -> Dict[str, Any]:
        """Extract semantic information from the UID."""
        return {
            "type": self.uid_type.value,
            "context": self.context,
            "hierarchy_level": self.hierarchy_level,
            "symbol_count": len(self.symbols),
            "validation_status": self.validation_status.value,
            "has_parent": self.parent_uid is not None,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }
    
    def __str__(self):
        return self.generate_uid_string()
    
    def __repr__(self):
        return f"HarappaUID({self.uid_type.value}, level={self.hierarchy_level})"
    
    def __eq__(self, other):
        if not isinstance(other, HarappaUID):
            return False
        return self.generate_uid_string() == other.generate_uid_string()
    
    def __hash__(self):
        return hash(self.generate_uid_string())


class UIDRegistry:
    """
    Registry for managing Harappa UIDs.
    
    Provides lookup, validation, and relationship tracking.
    """
    
    def __init__(self):
        self.uids: Dict[str, HarappaUID] = {}
        self.type_index: Dict[UIDType, List[HarappaUID]] = {t: [] for t in UIDType}
        self.context_index: Dict[str, List[HarappaUID]] = {}
        self.hierarchy_index: Dict[int, List[HarappaUID]] = {}
    
    def register(self, uid: HarappaUID) -> str:
        """
        Register a new UID in the registry.
        
        Returns:
            The UID string
        """
        uid_str = uid.generate_uid_string()
        
        if uid_str in self.uids:
            raise ValueError(f"UID {uid_str} already registered")
        
        self.uids[uid_str] = uid
        
        # Update indexes
        self.type_index[uid.uid_type].append(uid)
        
        if uid.context not in self.context_index:
            self.context_index[uid.context] = []
        self.context_index[uid.context].append(uid)
        
        if uid.hierarchy_level not in self.hierarchy_index:
            self.hierarchy_index[uid.hierarchy_level] = []
        self.hierarchy_index[uid.hierarchy_level].append(uid)
        
        return uid_str
    
    def lookup(self, uid_string: str) -> Optional[HarappaUID]:
        """Lookup a UID by its string representation."""
        return self.uids.get(uid_string)
    
    def find_by_type(self, uid_type: UIDType) -> List[HarappaUID]:
        """Find all UIDs of a given type."""
        return self.type_index.get(uid_type, [])
    
    def find_by_context(self, context: str) -> List[HarappaUID]:
        """Find all UIDs in a given context."""
        return self.context_index.get(context, [])
    
    def find_by_hierarchy_level(self, level: int) -> List[HarappaUID]:
        """Find all UIDs at a given hierarchy level."""
        return self.hierarchy_index.get(level, [])
    
    def find_children(self, parent_uid: HarappaUID) -> List[HarappaUID]:
        """Find all direct children of a UID."""
        return [uid for uid in self.uids.values() if uid.parent_uid == parent_uid]
    
    def validate_uid(self, uid_string: str) -> bool:
        """Validate a UID string."""
        uid = self.lookup(uid_string)
        if not uid:
            return False
        return uid.validate_checksum()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get registry statistics."""
        return {
            "total_uids": len(self.uids),
            "by_type": {t.value: len(uids) for t, uids in self.type_index.items()},
            "by_hierarchy_level": {level: len(uids) for level, uids in self.hierarchy_index.items()},
            "contexts": len(self.context_index)
        }
