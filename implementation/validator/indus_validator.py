"""
Indus Script Validator
Complete validation system with BNF grammar rules.
"""

from typing import List, Dict, Tuple, Optional
from enum import Enum
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser.indus_automaton import (
    IndusAutomaton, 
    IndusSymbolMapper, 
    SymbolClass,
    State
)


class ValidationRule:
    """Represents a validation rule for Indus sequences"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def validate(self, sequence: List[int], mapper: IndusSymbolMapper) -> Tuple[bool, Optional[str]]:
        """
        Validate a sequence against this rule.
        
        Returns:
            (is_valid, error_message)
        """
        raise NotImplementedError("Subclasses must implement validate()")


class ClosureRule(ValidationRule):
    """Rule: Every valid record must end with a closure symbol (342-348)"""
    
    def __init__(self):
        super().__init__(
            "closure_required",
            "Sequence must end with closure symbol (342-348)"
        )
    
    def validate(self, sequence: List[int], mapper: IndusSymbolMapper) -> Tuple[bool, Optional[str]]:
        if not sequence:
            return False, "Empty sequence"
        
        last_symbol = sequence[-1]
        if 342 <= last_symbol <= 348:
            return True, None
        else:
            return False, f"Sequence must end with closure symbol (342-348), found {last_symbol}"


class EntityFirstRule(ValidationRule):
    """Rule: Sequence must start with an entity symbol"""
    
    def __init__(self):
        super().__init__(
            "entity_first",
            "Sequence must start with an entity symbol"
        )
    
    def validate(self, sequence: List[int], mapper: IndusSymbolMapper) -> Tuple[bool, Optional[str]]:
        if not sequence:
            return False, "Empty sequence"
        
        first_class = mapper.get_symbol_class(sequence[0])
        if first_class is None:
            return False, f"Unknown symbol ID: {sequence[0]}"
        
        entity_classes = [
            SymbolClass.ENT_OVAL,
            SymbolClass.ENT_U,
            SymbolClass.ENT_HASTE,
            SymbolClass.ENT_ANIMAL,
            SymbolClass.ENT_METRICA
        ]
        
        if first_class in entity_classes:
            return True, None
        else:
            return False, f"Sequence must start with entity, found {first_class.value}"


class OperatorOrderRule(ValidationRule):
    """Rule: Operators must follow proper order (qual -> count -> rel -> close)"""
    
    def __init__(self):
        super().__init__(
            "operator_order",
            "Operators must follow order: qualification -> quantification -> relation -> closure"
        )
    
    def validate(self, sequence: List[int], mapper: IndusSymbolMapper) -> Tuple[bool, Optional[str]]:
        # Define operator precedence
        precedence = {
            SymbolClass.OP_QUAL: 1,
            SymbolClass.OP_COUNT: 2,
            SymbolClass.OP_REL: 3,
            SymbolClass.OP_CLOSE: 4
        }
        
        last_precedence = 0
        
        for symbol_id in sequence:
            symbol_class = mapper.get_symbol_class(symbol_id)
            if symbol_class in precedence:
                current_precedence = precedence[symbol_class]
                
                # Allow same precedence (e.g., multiple qualifiers)
                if symbol_class == SymbolClass.OP_QUAL and last_precedence == 1:
                    continue
                
                if current_precedence < last_precedence:
                    return False, f"Invalid operator order at symbol {symbol_id}"
                
                last_precedence = current_precedence
        
        return True, None


class IndusValidator:
    """
    Complete validator for Indus script sequences.
    
    Implements:
    - Finite automaton validation
    - BNF grammar rules
    - Compositional constraints
    - Compatibility matrix (simplified version)
    """
    
    def __init__(self):
        self.automaton = IndusAutomaton()
        self.mapper = IndusSymbolMapper()
        
        # Register validation rules
        self.rules: List[ValidationRule] = [
            ClosureRule(),
            EntityFirstRule(),
            OperatorOrderRule()
        ]
    
    def validate(self, sequence: List[int]) -> Tuple[bool, List[str]]:
        """
        Validate a complete Indus sequence.
        
        Args:
            sequence: List of symbol IDs
            
        Returns:
            (is_valid, list_of_errors)
        """
        errors = []
        
        # Check if sequence is empty
        if not sequence:
            errors.append("Empty sequence is invalid")
            return False, errors
        
        # Validate against each rule
        for rule in self.rules:
            is_valid, error = rule.validate(sequence, self.mapper)
            if not is_valid:
                errors.append(f"[{rule.name}] {error}")
        
        # Validate using automaton
        symbol_classes = self.mapper.classify_sequence(sequence)
        if symbol_classes is None:
            errors.append("Sequence contains unknown symbol IDs")
        else:
            self.automaton.reset()
            if not self.automaton.process_sequence(symbol_classes):
                if not self.automaton.is_valid_record():
                    errors.append(
                        f"Automaton validation failed: ended in state {self.automaton.get_current_state().value}"
                    )
                else:
                    errors.append("Invalid transition in automaton")
        
        return len(errors) == 0, errors
    
    def validate_with_details(self, sequence: List[int]) -> Dict:
        """
        Validate sequence and return detailed information.
        
        Returns:
            Dictionary with validation results and details
        """
        is_valid, errors = self.validate(sequence)
        
        # Get symbol classifications
        symbol_classes = self.mapper.classify_sequence(sequence)
        
        # Process through automaton for state trace
        self.automaton.reset()
        if symbol_classes:
            self.automaton.process_sequence(symbol_classes)
        
        return {
            "sequence": sequence,
            "is_valid": is_valid,
            "errors": errors,
            "symbol_classes": [sc.value for sc in symbol_classes] if symbol_classes else None,
            "final_state": self.automaton.get_current_state().value,
            "state_history": [
                {"from_state": state.value, "symbol": sc.value}
                for state, sc in self.automaton.get_history()
            ]
        }
    
    def get_bnf_grammar(self) -> str:
        """
        Return the BNF grammar as a formatted string.
        
        Returns:
            BNF grammar specification
        """
        return """
BNF Grammar for Indus Script
=============================

<registro> ::= <entidade> <qualificador>* <quantificador>? <relacionador>? <fechamento>

<entidade> ::= ENT_OVAL | ENT_U | ENT_HASTE | ENT_ANIMAL | ENT_METRICA

<qualificador> ::= OP_QUAL | OP_SCOPE | <intensificador>

<intensificador> ::= Crown | SideBars | Fill

<quantificador> ::= OP_COUNT | "|||" | "||||" | ...

<relacionador> ::= OP_REL | Knot | Dup

<fechamento> ::= OP_CLOSE(342-348) | [composição hierárquica]

Positional Rules:
-----------------
START: ENTITY [required]
MIDDLE: QUALIFIERS, QUANTIFIERS, RELATIONS [optional, fixed order]
END: CLOSURE [required]

Compatibility Rules:
--------------------
- Allowed edge: freq(s1, s2) > empirical_threshold
- Forbidden edge: freq(s1, s2) = 0 in corpus
- Directionality: grapheme → suffix/closer (never reverse)
"""


def validate_sequence(sequence: List[int]) -> bool:
    """
    Convenience function to validate a sequence.
    
    Args:
        sequence: List of symbol IDs
        
    Returns:
        True if valid, False otherwise
    """
    validator = IndusValidator()
    is_valid, _ = validator.validate(sequence)
    return is_valid


if __name__ == "__main__":
    print("Indus Script Validator - Examples")
    print("=" * 60)
    
    validator = IndusValidator()
    
    # Print BNF grammar
    print(validator.get_bnf_grammar())
    print("\n" + "=" * 60)
    print("Validation Examples:")
    print("=" * 60)
    
    # Test sequences
    test_sequences = [
        ([373, 342], "Simple: entity + closure"),
        ([373, 410, 342], "Entity + quantity + closure"),
        ([200, 410, 411, 343], "Animal + quantities + confirmed closure"),
        ([373, 400, 346], "Entity + relation + absolute closure"),
        ([373, 410], "Invalid: missing closure"),
        ([342, 373], "Invalid: closure before entity"),
        ([410, 342], "Invalid: no entity"),
    ]
    
    for sequence, description in test_sequences:
        print(f"\n{description}")
        print(f"Sequence: {sequence}")
        
        result = validator.validate_with_details(sequence)
        print(f"Valid: {result['is_valid']}")
        
        if result['errors']:
            print("Errors:")
            for error in result['errors']:
                print(f"  - {error}")
        
        if result['symbol_classes']:
            print(f"Classes: {result['symbol_classes']}")
        print(f"Final State: {result['final_state']}")
