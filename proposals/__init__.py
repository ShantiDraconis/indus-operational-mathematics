"""
Proposals Package

Contains all 15 revolutionary proposals for Harappan operational mathematics.
"""

# Import all proposals
from .harappan_os import (
    HarappanKernel,
    HarappanProcess,
    ProcessState,
    SYSCALLS,
    EXIT_CODES,
)

from .state_crypto import (
    StateCrypto,
    StateCryptoKey,
    SmartContract,
)

from .civilization_dna import (
    CivilizationGraph,
    SymbolNode,
)

from .harappan_cpu import (
    HarappanCPU,
    HarappanAssembler,
    Register,
    Instruction,
    ALUOperation,
    fibonacci_program,
)

from .universe_00 import (
    Universe00,
    UniverseState,
    INCOMPLETENESS_THEOREM,
    UNIVERSALITY_THEOREM,
    CLOSURE_HYPOTHESIS,
)

from .additional_proposals import (
    HarappanGenerativeArt,
    AlgorithmicLaw,
    HarappanBCI,
    InformationPhysics,
    LegalCase,
)

__all__ = [
    # Proposal 1: Harappan OS
    'HarappanKernel',
    'HarappanProcess',
    'ProcessState',
    'SYSCALLS',
    'EXIT_CODES',
    
    # Proposal 2: StateCrypto
    'StateCrypto',
    'StateCryptoKey',
    'SmartContract',
    
    # Proposal 3: DNA of Civilization
    'CivilizationGraph',
    'SymbolNode',
    
    # Proposal 7: Harappan CPU
    'HarappanCPU',
    'HarappanAssembler',
    'Register',
    'Instruction',
    'ALUOperation',
    'fibonacci_program',
    
    # Master Proposal: Universe 0/0
    'Universe00',
    'UniverseState',
    'INCOMPLETENESS_THEOREM',
    'UNIVERSALITY_THEOREM',
    'CLOSURE_HYPOTHESIS',
    
    # Additional Proposals
    'HarappanGenerativeArt',
    'AlgorithmicLaw',
    'HarappanBCI',
    'InformationPhysics',
    'LegalCase',
]
