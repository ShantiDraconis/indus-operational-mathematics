"""
Harappan OS - Operating System Based on States

Proposal 1: Implement an operating system where processes are represented 
as "Harappan inscriptions" in execution.

Processes = Entities (373-399)
System calls = Graphical operators
Exit codes = Closures (342-348)
Kernel validates state transitions
"""

from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field
import time
from core.harappan_automaton import HarappanAutomaton, State, CLOSURE_MEANINGS


class ProcessState(Enum):
    """OS Process states mapped to Harappan states"""
    NEW = State.S0
    READY = State.S1
    RUNNING = State.S2
    WAITING = State.S3
    ZOMBIE = State.S4
    TERMINATED = State.S5


@dataclass
class HarappanProcess:
    """A process represented as a Harappan inscription"""
    pid: int
    entity_id: int  # Harappan entity representing this process
    automaton: HarappanAutomaton = field(default_factory=HarappanAutomaton)
    created_at: float = field(default_factory=time.time)
    terminated_at: Optional[float] = None
    exit_code: Optional[int] = None  # Closure symbol
    
    def __post_init__(self):
        # Initialize process by loading its entity
        self.automaton.add_entity(self.entity_id)
    
    def get_state(self) -> ProcessState:
        """Get current process state"""
        harappan_state = self.automaton.current_state
        state_map = {
            State.S0: ProcessState.NEW,
            State.S1: ProcessState.READY,
            State.S2: ProcessState.RUNNING,
            State.S3: ProcessState.WAITING,
            State.S4: ProcessState.ZOMBIE,
            State.S5: ProcessState.TERMINATED,
        }
        return state_map[harappan_state]
    
    def execute_syscall(self, operator: str) -> bool:
        """Execute a system call (operator)"""
        return self.automaton.add_operator(operator)
    
    def wait_for_resource(self, count: int) -> bool:
        """Wait for resource (quantifier)"""
        return self.automaton.add_quantifier(count)
    
    def communicate(self, other_pid: int, relation_type: int) -> bool:
        """Communicate with another process (relation)"""
        return self.automaton.add_relation(relation_type)
    
    def terminate(self, exit_code: int) -> bool:
        """Terminate process with exit code (closure)"""
        if self.automaton.add_closure(exit_code):
            self.exit_code = exit_code
            self.terminated_at = time.time()
            return True
        return False
    
    def is_terminated(self) -> bool:
        """Check if process has terminated"""
        return self.automaton.is_valid()


class HarappanKernel:
    """
    Kernel that validates process state transitions
    
    The kernel ensures all processes follow valid Harappan grammar,
    guaranteeing that every process eventually terminates (reaches closure).
    """
    
    def __init__(self):
        self.processes: Dict[int, HarappanProcess] = {}
        self.next_pid = 1
        self.syscall_count = 0
        
    def create_process(self, entity_id: int) -> int:
        """Create a new process from a Harappan entity"""
        pid = self.next_pid
        self.next_pid += 1
        
        process = HarappanProcess(pid=pid, entity_id=entity_id)
        self.processes[pid] = process
        
        return pid
    
    def syscall(self, pid: int, operator: str) -> bool:
        """Execute a system call for a process"""
        if pid not in self.processes:
            raise ValueError(f"Process {pid} not found")
        
        process = self.processes[pid]
        if process.is_terminated():
            raise ValueError(f"Process {pid} already terminated")
        
        self.syscall_count += 1
        return process.execute_syscall(operator)
    
    def wait_resource(self, pid: int, resource_count: int) -> bool:
        """Process waits for resource"""
        if pid not in self.processes:
            raise ValueError(f"Process {pid} not found")
        
        process = self.processes[pid]
        return process.wait_for_resource(resource_count)
    
    def ipc(self, pid1: int, pid2: int, relation_type: int) -> bool:
        """Inter-process communication"""
        if pid1 not in self.processes or pid2 not in self.processes:
            raise ValueError("Process not found")
        
        process1 = self.processes[pid1]
        return process1.communicate(pid2, relation_type)
    
    def exit(self, pid: int, exit_code: int) -> bool:
        """Terminate a process"""
        if pid not in self.processes:
            raise ValueError(f"Process {pid} not found")
        
        process = self.processes[pid]
        return process.terminate(exit_code)
    
    def get_process_state(self, pid: int) -> ProcessState:
        """Get current state of a process"""
        if pid not in self.processes:
            raise ValueError(f"Process {pid} not found")
        
        return self.processes[pid].get_state()
    
    def get_running_processes(self) -> List[int]:
        """Get list of non-terminated process IDs"""
        return [
            pid for pid, proc in self.processes.items()
            if not proc.is_terminated()
        ]
    
    def get_exit_code_meaning(self, exit_code: int) -> str:
        """Get human-readable meaning of exit code"""
        return CLOSURE_MEANINGS.get(exit_code, "Unknown")
    
    def validate_all(self) -> bool:
        """Validate that all processes are in valid states"""
        return all(
            proc.automaton.current_state in State
            for proc in self.processes.values()
        )
    
    def get_stats(self) -> Dict:
        """Get kernel statistics"""
        total = len(self.processes)
        terminated = sum(1 for p in self.processes.values() if p.is_terminated())
        
        return {
            'total_processes': total,
            'terminated': terminated,
            'running': total - terminated,
            'syscall_count': self.syscall_count,
        }


# System call mappings
SYSCALLS = {
    'read': 'dot',
    'write': 'stroke',
    'open': 'vertical',
    'close': 'horizontal',
    'exec': 'oblique',
}

# Exit code mappings  
EXIT_CODES = {
    'SUCCESS': 343,  # Approved
    'ERROR': 342,    # Rejected
    'TIMEOUT': 346,  # Cancelled
    'KILLED': 346,   # Cancelled
    'COMPLETED': 345,  # Completed
}
