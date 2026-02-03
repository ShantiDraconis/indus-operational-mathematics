"""
Example 1: Formal Specification Language
Demonstrates Proposal 1 - Using Harappa for smart contract specification
"""

from harappa import Symbol, Operator, State, SymbolType, OperatorType
from harappa.spec_lang import HarappaSpec, Transition, TransitionType, ContractMethod

def example_token_contract():
    """Example: ERC-20-like token contract specification."""
    
    # Create the specification system
    spec = HarappaSpec()
    
    # Create state machine for token transfers
    token_sm = spec.create_state_machine("TokenTransfer")
    
    # Define states
    initial = State(is_final=False)
    initial.properties["balance_checked"] = False
    token_sm.add_state("initial", initial)
    
    balance_checked = State()
    balance_checked.properties["balance_checked"] = True
    token_sm.add_state("balance_checked", balance_checked)
    
    transferred = State(is_final=True)
    transferred.properties["transfer_complete"] = True
    token_sm.add_state("transferred", transferred)
    token_sm.add_final_state("transferred")
    
    # Define operators
    check_balance = Operator(
        name="check_balance",
        operator_type=OperatorType.VALIDATION,
        arity=1,
        parameters={"min_balance": 0}
    )
    
    execute_transfer = Operator(
        name="execute_transfer",
        operator_type=OperatorType.TRANSFORMATION,
        arity=2,
        parameters={"amount": 0}
    )
    
    finalize = Operator(
        name="finalize",
        operator_type=OperatorType.CLOSURE,
        arity=1
    )
    
    # Define transitions
    t1 = Transition(
        from_state="initial",
        to_state="balance_checked",
        operator=check_balance,
        condition=lambda s: s.properties.get("balance_checked", False) == False
    )
    token_sm.add_transition(t1)
    
    t2 = Transition(
        from_state="balance_checked",
        to_state="transferred",
        operator=execute_transfer,
        condition=lambda s: s.properties.get("balance_checked", True)
    )
    token_sm.add_transition(t2)
    
    # Create contract
    contract = spec.create_contract("TokenContract", token_sm)
    
    # Add contract method with pre/post conditions
    transfer_method = ContractMethod(name="transfer")
    transfer_method.preconditions.append(
        lambda s: len(s.symbols) >= 2  # Requires sender and receiver
    )
    transfer_method.postconditions.append(
        lambda s: s.is_final  # Must reach final state
    )
    
    contract.add_method(transfer_method)
    
    # Validate
    print("=== Token Contract Specification ===")
    print(f"State Machine: {token_sm}")
    print(f"Is Deterministic: {token_sm.is_deterministic()}")
    print(f"Has Termination Guarantee: {token_sm.has_termination_guarantee()}")
    print(f"Contract Valid: {contract.validate()}")
    print(f"States: {list(token_sm.states.keys())}")
    print(f"Transitions: {len(token_sm.transitions)}")
    
    # Convert to Harappa record
    record = token_sm.to_record()
    print(f"Record Closed: {record.has_closure}")
    print(f"Record Valid: {record.validate()}")
    
    return contract

if __name__ == "__main__":
    example_token_contract()
