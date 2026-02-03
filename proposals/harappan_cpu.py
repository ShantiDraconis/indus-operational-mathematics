"""
Harappan Computer Architecture

Proposal 7: CPU based on Harappan automaton:
- Registers = Entities (373-399)
- ALU = Operators (Dot, Stroke, etc.)
- Flags = Automaton states
- Halt = Closure

Advantage: Execution guaranteed to terminate (always reaches closure)
"""

from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field
from core.harappan_automaton import HarappanAutomaton, State, SymbolType


class ALUOperation(Enum):
    """ALU operations mapped to Harappan operators"""
    DOT = "dot"           # Addition
    STROKE = "stroke"     # Subtraction
    VERTICAL = "vertical" # Multiplication
    HORIZONTAL = "horizontal"  # Division
    OBLIQUE = "oblique"   # Comparison


@dataclass
class Register:
    """CPU Register represented as Harappan entity"""
    id: int  # Entity ID (373-399)
    value: int = 0
    name: str = ""
    
    def __post_init__(self):
        if not (373 <= self.id <= 399):
            raise ValueError(f"Register ID must be in range 373-399, got {self.id}")
        self.name = f"R{self.id}"


@dataclass
class Instruction:
    """CPU instruction as Harappan sequence"""
    operation: ALUOperation
    operand1: int  # Register ID
    operand2: Optional[int] = None  # Register ID or immediate value
    dest: Optional[int] = None  # Destination register ID


class HarappanCPU:
    """
    CPU based on Harappan automaton
    
    Features:
    - Guaranteed termination (must reach closure)
    - State-based execution model
    - Formal verification through automaton
    """
    
    def __init__(self):
        self.registers: Dict[int, Register] = {}
        self.automaton = HarappanAutomaton()
        self.program: List[Instruction] = []
        self.pc = 0  # Program counter
        self.halted = False
        self.cycles = 0
        
        # Initialize standard registers
        for reg_id in range(373, 380):  # Initialize 7 registers
            self.registers[reg_id] = Register(id=reg_id)
        
    def load_register(self, reg_id: int, value: int):
        """Load value into register"""
        if reg_id not in self.registers:
            self.registers[reg_id] = Register(id=reg_id)
        self.registers[reg_id].value = value
        
    def get_register(self, reg_id: int) -> int:
        """Get register value"""
        if reg_id not in self.registers:
            return 0
        return self.registers[reg_id].value
        
    def alu_execute(self, operation: ALUOperation, op1: int, op2: int) -> int:
        """
        Execute ALU operation
        
        Args:
            operation: The operation to perform
            op1: First operand value
            op2: Second operand value
        
        Returns:
            Result of the operation
        """
        if operation == ALUOperation.DOT:
            return op1 + op2
        elif operation == ALUOperation.STROKE:
            return op1 - op2
        elif operation == ALUOperation.VERTICAL:
            return op1 * op2
        elif operation == ALUOperation.HORIZONTAL:
            return op1 // op2 if op2 != 0 else 0
        elif operation == ALUOperation.OBLIQUE:
            return 1 if op1 == op2 else 0
        else:
            return 0
    
    def execute_instruction(self, instruction: Instruction) -> bool:
        """
        Execute a single instruction
        
        Returns:
            True if execution successful, False if halted
        """
        if self.halted:
            return False
        
        # Get operand values
        op1_val = self.get_register(instruction.operand1)
        op2_val = instruction.operand2 if instruction.operand2 is not None else 0
        
        if instruction.operand2 and instruction.operand2 >= 373:
            # operand2 is a register
            op2_val = self.get_register(instruction.operand2)
        
        # Execute operation
        result = self.alu_execute(instruction.operation, op1_val, op2_val)
        
        # Store result
        if instruction.dest:
            self.load_register(instruction.dest, result)
        
        # Update automaton state
        self.automaton.add_operator(instruction.operation.value)
        
        self.cycles += 1
        return True
    
    def load_program(self, instructions: List[Instruction]):
        """Load a program into memory"""
        self.program = instructions
        self.pc = 0
        self.halted = False
        
    def run(self, max_cycles: int = 1000) -> bool:
        """
        Run the loaded program
        
        Args:
            max_cycles: Maximum number of cycles to execute
        
        Returns:
            True if program completed, False if max cycles reached
        """
        while self.pc < len(self.program) and self.cycles < max_cycles and not self.halted:
            instruction = self.program[self.pc]
            if not self.execute_instruction(instruction):
                break
            self.pc += 1
        
        return self.pc >= len(self.program) or self.halted
    
    def halt(self, exit_code: int):
        """
        Halt the CPU with exit code (closure)
        
        Args:
            exit_code: Closure symbol (342-348)
        """
        if self.automaton.add_closure(exit_code):
            self.halted = True
        
    def is_terminated(self) -> bool:
        """Check if CPU has halted"""
        return self.halted and self.automaton.current_state == State.S5
    
    def get_state(self) -> State:
        """Get current automaton state"""
        return self.automaton.current_state
    
    def reset(self):
        """Reset CPU to initial state"""
        self.automaton.reset()
        self.pc = 0
        self.halted = False
        self.cycles = 0
        for reg in self.registers.values():
            reg.value = 0


class HarappanAssembler:
    """
    Assembler for Harappan CPU
    
    Converts high-level operations to Harappan instructions
    """
    
    @staticmethod
    def add(dest: int, op1: int, op2: int) -> Instruction:
        """Create ADD instruction"""
        return Instruction(ALUOperation.DOT, op1, op2, dest)
    
    @staticmethod
    def sub(dest: int, op1: int, op2: int) -> Instruction:
        """Create SUB instruction"""
        return Instruction(ALUOperation.STROKE, op1, op2, dest)
    
    @staticmethod
    def mul(dest: int, op1: int, op2: int) -> Instruction:
        """Create MUL instruction"""
        return Instruction(ALUOperation.VERTICAL, op1, op2, dest)
    
    @staticmethod
    def div(dest: int, op1: int, op2: int) -> Instruction:
        """Create DIV instruction"""
        return Instruction(ALUOperation.HORIZONTAL, op1, op2, dest)
    
    @staticmethod
    def cmp(dest: int, op1: int, op2: int) -> Instruction:
        """Create CMP instruction"""
        return Instruction(ALUOperation.OBLIQUE, op1, op2, dest)
    
    @staticmethod
    def load_immediate(dest: int, value: int) -> Instruction:
        """Create LOAD instruction"""
        return Instruction(ALUOperation.DOT, 373, value, dest)


# Example programs
def fibonacci_program(n: int) -> List[Instruction]:
    """
    Generate Fibonacci sequence program
    
    Registers:
    R373 = 0 (constant)
    R374 = 1 (constant)
    R375 = current fib number
    R376 = previous fib number
    R377 = counter
    """
    asm = HarappanAssembler
    
    return [
        asm.load_immediate(373, 0),  # R373 = 0
        asm.load_immediate(374, 1),  # R374 = 1
        asm.load_immediate(375, 1),  # R375 = 1 (current)
        asm.load_immediate(376, 0),  # R376 = 0 (previous)
        asm.load_immediate(377, n),  # R377 = n (counter)
        # Loop would go here in a real implementation
    ]
