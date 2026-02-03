"""
Example 2: Harappa-UID System
Demonstrates Proposal 2 - Universal Unique Identification
"""

from harappa import Symbol, SymbolType
from harappa.uid import HarappaUID, UIDType, UIDRegistry, ValidationStatus

def example_supply_chain_uids():
    """Example: Supply chain tracking with hierarchical UIDs."""
    
    # Create registry
    registry = UIDRegistry()
    
    # Create root UID for a shipment
    shipment_uid = HarappaUID(
        uid_type=UIDType.ASSET,
        context="supply_chain"
    )
    shipment_uid.add_symbol(Symbol("SHIPMENT_001", SymbolType.ENTITY))
    shipment_uid.encode_metadata("origin", "Mumbai")
    shipment_uid.encode_metadata("destination", "Delhi")
    shipment_uid.set_validation_status(ValidationStatus.VALIDATED)
    
    shipment_id = registry.register(shipment_uid)
    print("=== Supply Chain UID Example ===")
    print(f"Shipment UID: {shipment_id}")
    print(f"Semantic Info: {shipment_uid.get_semantic_info()}")
    
    # Create child UIDs for packages
    package1_uid = HarappaUID(
        uid_type=UIDType.ASSET,
        context="supply_chain"
    )
    package1_uid.add_symbol(Symbol("PACKAGE_A", SymbolType.RESOURCE))
    package1_uid.set_parent(shipment_uid)
    package1_uid.encode_metadata("weight", "10kg")
    package1_uid.set_validation_status(ValidationStatus.VALIDATED)
    
    package1_id = registry.register(package1_uid)
    print(f"\nPackage 1 UID: {package1_id}")
    print(f"Hierarchy Level: {package1_uid.hierarchy_level}")
    print(f"Is child of shipment: {package1_uid.is_child_of(shipment_uid)}")
    
    package2_uid = HarappaUID(
        uid_type=UIDType.ASSET,
        context="supply_chain"
    )
    package2_uid.add_symbol(Symbol("PACKAGE_B", SymbolType.RESOURCE))
    package2_uid.set_parent(shipment_uid)
    package2_uid.encode_metadata("weight", "5kg")
    package2_uid.set_validation_status(ValidationStatus.PENDING)
    
    package2_id = registry.register(package2_uid)
    print(f"\nPackage 2 UID: {package2_id}")
    
    # Create transaction UID
    transaction_uid = HarappaUID(
        uid_type=UIDType.TRANSACTION,
        context="supply_chain"
    )
    transaction_uid.add_symbol(Symbol("DELIVERY_TX", SymbolType.TRANSACTION))
    transaction_uid.encode_metadata("timestamp", "2026-02-03T15:00:00Z")
    transaction_uid.set_validation_status(ValidationStatus.VALIDATED)
    
    transaction_id = registry.register(transaction_uid)
    print(f"\nTransaction UID: {transaction_id}")
    
    # Query registry
    print("\n=== Registry Statistics ===")
    stats = registry.get_statistics()
    print(f"Total UIDs: {stats['total_uids']}")
    print(f"By Type: {stats['by_type']}")
    print(f"By Hierarchy: {stats['by_hierarchy_level']}")
    
    # Find children
    children = registry.find_children(shipment_uid)
    print(f"\nShipment has {len(children)} packages")
    
    # Validate checksums
    print(f"\nShipment UID valid: {shipment_uid.validate_checksum()}")
    print(f"Package 1 UID valid: {package1_uid.validate_checksum()}")
    
    return registry

if __name__ == "__main__":
    example_supply_chain_uids()
