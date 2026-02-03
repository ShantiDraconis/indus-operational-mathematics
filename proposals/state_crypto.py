"""
StateCrypto - State-Based Cryptography

Proposal 2: Cryptography where the key is a valid Harappan sequence 
and messages can only be decrypted when the "inscription" reaches closed state.

Mechanism:
- Encrypt: Message → ENTITY → [Operators] → [Closure]
- Decrypt: Only possible if automaton reaches S5
- Application: Smart contracts that release funds after state validation
"""

import hashlib
import json
from typing import List, Tuple, Optional
from dataclasses import dataclass
from core.harappan_automaton import HarappanAutomaton, State


@dataclass
class StateCryptoKey:
    """A cryptographic key represented as a Harappan sequence"""
    sequence: List[Tuple[str, any]]  # List of (type, value) tuples
    
    def to_bytes(self) -> bytes:
        """Convert key to bytes for cryptographic operations"""
        key_str = json.dumps(self.sequence)
        return hashlib.sha256(key_str.encode()).digest()
    
    def is_valid(self) -> bool:
        """Check if key forms a valid Harappan inscription"""
        automaton = HarappanAutomaton()
        return automaton.validate_sequence(self.sequence)


class StateCrypto:
    """
    State-based cryptographic system using Harappan grammar
    
    Security properties:
    - Key must be a valid Harappan inscription (reaches closure)
    - Invalid sequences cannot be used as keys
    - Decryption requires state machine to reach S5
    """
    
    def __init__(self):
        pass
    
    def encrypt(self, message: bytes, key: StateCryptoKey) -> bytes:
        """
        Encrypt a message using a state-based key
        
        Args:
            message: The plaintext to encrypt
            key: A valid Harappan sequence as key
        
        Returns:
            Encrypted ciphertext
        
        Raises:
            ValueError: If key is not a valid Harappan sequence
        """
        if not key.is_valid():
            raise ValueError("Key must be a valid Harappan inscription (must reach closure)")
        
        # Get key bytes
        key_bytes = key.to_bytes()
        
        # Simple XOR cipher with key derivation (for demonstration)
        # In production, use proper encryption like AES
        ciphertext = bytearray()
        for i, byte in enumerate(message):
            key_byte = key_bytes[i % len(key_bytes)]
            ciphertext.append(byte ^ key_byte)
        
        return bytes(ciphertext)
    
    def decrypt(self, ciphertext: bytes, key: StateCryptoKey) -> bytes:
        """
        Decrypt a message using a state-based key
        
        Args:
            ciphertext: The encrypted message
            key: A valid Harappan sequence as key
        
        Returns:
            Decrypted plaintext
        
        Raises:
            ValueError: If key is not in closed state (S5)
        """
        # Validate that key reaches closed state
        automaton = HarappanAutomaton()
        
        try:
            for symbol_type, value in key.sequence:
                if symbol_type == 'entity':
                    automaton.add_entity(value)
                elif symbol_type == 'operator':
                    automaton.add_operator(value)
                elif symbol_type == 'quantifier':
                    automaton.add_quantifier(value)
                elif symbol_type == 'relation':
                    automaton.add_relation(value)
                elif symbol_type == 'closure':
                    automaton.add_closure(value)
        except:
            raise ValueError("Invalid key sequence")
        
        # Check if automaton reached closed state
        if automaton.current_state != State.S5:
            raise ValueError("Key must reach closed state (S5) for decryption")
        
        # Get key bytes
        key_bytes = key.to_bytes()
        
        # Decrypt using XOR
        plaintext = bytearray()
        for i, byte in enumerate(ciphertext):
            key_byte = key_bytes[i % len(key_bytes)]
            plaintext.append(byte ^ key_byte)
        
        return bytes(plaintext)
    
    def create_key_from_entity(self, entity_id: int, closure_id: int) -> StateCryptoKey:
        """
        Create a simple key from entity and closure
        
        Args:
            entity_id: Entity symbol (373-399)
            closure_id: Closure symbol (342-348)
        
        Returns:
            A valid StateCryptoKey
        """
        sequence = [
            ('entity', entity_id),
            ('closure', closure_id),
        ]
        return StateCryptoKey(sequence=sequence)
    
    def create_complex_key(
        self, 
        entity_id: int,
        operator: str,
        quantifier: int,
        relation_id: int,
        closure_id: int
    ) -> StateCryptoKey:
        """
        Create a complex key with full state transitions
        
        Args:
            entity_id: Entity symbol (373-399)
            operator: Operator name
            quantifier: Quantifier count
            relation_id: Relation symbol (400-409)
            closure_id: Closure symbol (342-348)
        
        Returns:
            A valid StateCryptoKey
        """
        sequence = [
            ('entity', entity_id),
            ('operator', operator),
            ('quantifier', quantifier),
            ('relation', relation_id),
            ('closure', closure_id),
        ]
        return StateCryptoKey(sequence=sequence)


class SmartContract:
    """
    Smart contract that releases funds only after state validation
    
    Use case: Multi-party contract that requires specific state transitions
    before funds are released.
    """
    
    def __init__(self, contract_id: int, required_states: List[int]):
        self.contract_id = contract_id
        self.required_states = required_states  # List of entity IDs
        self.current_state_index = 0
        self.automaton = HarappanAutomaton()
        self.crypto = StateCrypto()
        self.funds_encrypted: Optional[bytes] = None
        self.release_key: Optional[StateCryptoKey] = None
        
    def lock_funds(self, funds_data: bytes, release_key: StateCryptoKey):
        """Lock funds with a state-based key"""
        if not release_key.is_valid():
            raise ValueError("Release key must be valid Harappan sequence")
        
        self.funds_encrypted = self.crypto.encrypt(funds_data, release_key)
        self.release_key = release_key
        
    def progress_state(self, entity_id: int) -> bool:
        """Progress contract through required states"""
        if self.current_state_index >= len(self.required_states):
            return False
        
        if entity_id != self.required_states[self.current_state_index]:
            raise ValueError(f"Expected state {self.required_states[self.current_state_index]}, got {entity_id}")
        
        self.current_state_index += 1
        return True
        
    def can_release_funds(self) -> bool:
        """Check if all required states have been validated"""
        return self.current_state_index >= len(self.required_states)
        
    def release_funds(self) -> bytes:
        """Release funds after all states validated"""
        if not self.can_release_funds():
            raise ValueError("Not all required states validated")
        
        if self.funds_encrypted is None or self.release_key is None:
            raise ValueError("No funds locked")
        
        # Decrypt and release funds
        return self.crypto.decrypt(self.funds_encrypted, self.release_key)
