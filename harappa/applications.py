"""
Harappa Applications Module

Implements proposals 4-15 with practical applications of the Harappa system:
- Archaeological simulations
- Visual programming
- Educational systems
- AI metadata
- Semantic databases
- Communication protocols
- DAO governance
- Ancient text search
- Art generation
- Authentication
- Service choreography
- Risk analysis
"""

from typing import List, Dict, Set, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import random

from .core import Symbol, Operator, State, Record, SymbolType, OperatorType
from .uid import HarappaUID, UIDType


# ============================================================================
# Proposal 4: Archaeological Simulation
# ============================================================================

@dataclass
class Agent:
    """An agent in the archaeological simulation."""
    uid: HarappaUID
    agent_type: str
    resources: Dict[str, int] = field(default_factory=dict)
    connections: List['Agent'] = field(default_factory=list)
    
    def trade(self, other: 'Agent', resource: str, amount: int) -> 'Transaction':
        """Execute a trade with another agent."""
        if self.resources.get(resource, 0) < amount:
            raise ValueError("Insufficient resources")
        
        self.resources[resource] = self.resources.get(resource, 0) - amount
        other.resources[resource] = other.resources.get(resource, 0) + amount
        
        return Transaction(
            from_agent=self,
            to_agent=other,
            resource=resource,
            amount=amount
        )


@dataclass
class Transaction:
    """A transaction between agents."""
    from_agent: Agent
    to_agent: Agent
    resource: str
    amount: int


class ArchaeologicalSimulation:
    """
    Simulation of Harappan trade networks.
    
    Uses Harappa records to model economic and social structures.
    """
    
    def __init__(self):
        self.agents: List[Agent] = []
        self.transactions: List[Transaction] = []
        self.network: Dict[str, List[str]] = {}
    
    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the simulation."""
        self.agents.append(agent)
    
    def simulate_step(self) -> None:
        """Simulate one time step of trade."""
        # Random trades between connected agents
        for agent in self.agents:
            if agent.connections and agent.resources:
                partner = random.choice(agent.connections)
                resource = random.choice(list(agent.resources.keys()))
                max_amount = agent.resources[resource]
                
                if max_amount > 0:
                    amount = random.randint(1, max(1, max_amount))
                    
                    try:
                        transaction = agent.trade(partner, resource, amount)
                        self.transactions.append(transaction)
                    except ValueError:
                        pass  # Trade failed
    
    def get_network_statistics(self) -> Dict[str, Any]:
        """Get statistics about the trade network."""
        return {
            "total_agents": len(self.agents),
            "total_transactions": len(self.transactions),
            "average_connections": sum(len(a.connections) for a in self.agents) / len(self.agents) if self.agents else 0
        }


# ============================================================================
# Proposal 5: Visual Programming Interface
# ============================================================================

@dataclass
class VisualNode:
    """A node in the visual programming interface."""
    symbol: Symbol
    position: tuple[int, int]
    connections: List['VisualNode'] = field(default_factory=list)


class VisualProgrammingInterface:
    """
    Visual programming using Harappa symbols.
    
    Drag-and-drop interface for creating workflows and algorithms.
    """
    
    def __init__(self):
        self.nodes: List[VisualNode] = []
        self.operators: List[Operator] = []
    
    def add_node(self, symbol: Symbol, x: int, y: int) -> VisualNode:
        """Add a node to the canvas."""
        node = VisualNode(symbol=symbol, position=(x, y))
        self.nodes.append(node)
        return node
    
    def connect_nodes(self, from_node: VisualNode, to_node: VisualNode) -> None:
        """Connect two nodes."""
        from_node.connections.append(to_node)
    
    def generate_code(self) -> str:
        """Generate executable code from the visual representation."""
        code_lines = []
        for i, node in enumerate(self.nodes):
            code_lines.append(f"# Node {i}: {node.symbol.id}")
            for conn in node.connections:
                code_lines.append(f"#   -> connects to {conn.symbol.id}")
        return "\n".join(code_lines)


# ============================================================================
# Proposal 6: Educational Logic System
# ============================================================================

class EducationalSystem:
    """
    Educational system for teaching logic and mathematics.
    
    Uses Harappa symbols for visual and intuitive learning.
    """
    
    def __init__(self):
        self.lessons: List[Dict[str, Any]] = []
        self.student_progress: Dict[str, int] = {}
    
    def create_lesson(self, name: str, concepts: List[Symbol]) -> None:
        """Create a new lesson."""
        self.lessons.append({
            "name": name,
            "concepts": concepts,
            "exercises": []
        })
    
    def add_exercise(self, lesson_name: str, exercise: Dict[str, Any]) -> None:
        """Add an exercise to a lesson."""
        for lesson in self.lessons:
            if lesson["name"] == lesson_name:
                lesson["exercises"].append(exercise)
                break


# ============================================================================
# Proposal 7: AI Metadata Standard
# ============================================================================

@dataclass
class AIMetadata:
    """Metadata for AI datasets and models using Harappa."""
    uid: HarappaUID
    dataset_name: str
    provenance: List[str] = field(default_factory=list)
    quality_score: float = 0.0
    licenses: List[str] = field(default_factory=list)
    audit_status: str = "unaudited"
    
    def add_provenance(self, source: str) -> None:
        """Add provenance information."""
        self.provenance.append(source)
    
    def set_quality(self, score: float) -> None:
        """Set quality score (0-1)."""
        self.quality_score = max(0.0, min(1.0, score))
    
    def to_seal(self) -> str:
        """Generate a digital Harappa seal."""
        data = f"{self.uid}{self.dataset_name}{self.quality_score}{self.audit_status}"
        return hashlib.sha256(data.encode()).hexdigest()


# ============================================================================
# Proposal 8: Semantic Database Schema
# ============================================================================

@dataclass
class OntologyClass:
    """A class in the semantic database ontology."""
    name: str
    symbols: List[Symbol] = field(default_factory=list)
    properties: Dict[str, Any] = field(default_factory=dict)
    relations: List['OntologyRelation'] = field(default_factory=list)


@dataclass
class OntologyRelation:
    """A relation between ontology classes."""
    from_class: str
    to_class: str
    relation_type: str
    operator: Operator


class SemanticDatabase:
    """
    Semantic database using Harappa ontology schema.
    
    Compact, non-ambiguous representation of facts.
    """
    
    def __init__(self):
        self.classes: Dict[str, OntologyClass] = {}
        self.instances: List[Dict[str, Any]] = []
    
    def define_class(self, onto_class: OntologyClass) -> None:
        """Define a new ontology class."""
        self.classes[onto_class.name] = onto_class
    
    def add_instance(self, class_name: str, instance_data: Dict[str, Any]) -> None:
        """Add an instance of a class."""
        if class_name not in self.classes:
            raise ValueError(f"Class {class_name} not defined")
        
        instance_data["_class"] = class_name
        self.instances.append(instance_data)
    
    def query(self, class_name: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Query instances of a class."""
        results = [inst for inst in self.instances if inst.get("_class") == class_name]
        
        if filters:
            results = [inst for inst in results if all(inst.get(k) == v for k, v in filters.items())]
        
        return results


# ============================================================================
# Proposal 9: Low-Bandwidth Communication
# ============================================================================

@dataclass
class StructuredMessage:
    """A structured message using Harappa symbols."""
    message_type: str
    symbols: List[Symbol]
    priority: int = 0
    
    def encode(self) -> bytes:
        """Encode message for transmission."""
        # Compact binary encoding
        data = f"{self.message_type}:{''.join(s.id for s in self.symbols)}"
        return data.encode()
    
    def decode(self, data: bytes) -> None:
        """Decode received message."""
        decoded = data.decode()
        parts = decoded.split(':')
        if len(parts) == 2:
            self.message_type = parts[0]


class CommunicationSystem:
    """
    Low-bandwidth communication using Harappa symbols.
    
    Efficient transmission for remote/emergency scenarios.
    """
    
    def __init__(self):
        self.message_queue: List[StructuredMessage] = []
    
    def send_message(self, message: StructuredMessage) -> None:
        """Queue a message for transmission."""
        self.message_queue.append(message)
    
    def get_next_message(self) -> Optional[StructuredMessage]:
        """Get the next message to transmit (highest priority)."""
        if not self.message_queue:
            return None
        
        self.message_queue.sort(key=lambda m: m.priority, reverse=True)
        return self.message_queue.pop(0)


# ============================================================================
# Proposal 10: DAO Governance
# ============================================================================

@dataclass
class Proposal:
    """A DAO proposal using Harappa."""
    uid: HarappaUID
    title: str
    description: str
    record: Record
    votes_for: int = 0
    votes_against: int = 0
    status: str = "pending"


class DAOGovernance:
    """
    Decentralized governance using Harappa.
    
    Voting and decision-making with transparency.
    """
    
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
        self.members: Set[str] = set()
    
    def create_proposal(self, proposal: Proposal) -> None:
        """Create a new proposal."""
        uid_str = str(proposal.uid)
        self.proposals[uid_str] = proposal
    
    def vote(self, proposal_uid: str, member_id: str, vote: bool) -> None:
        """Cast a vote on a proposal."""
        if member_id not in self.members:
            raise ValueError("Not a member")
        
        if proposal_uid not in self.proposals:
            raise ValueError("Proposal not found")
        
        proposal = self.proposals[proposal_uid]
        if vote:
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1
    
    def finalize_proposal(self, proposal_uid: str) -> None:
        """Finalize a proposal based on votes."""
        if proposal_uid not in self.proposals:
            raise ValueError("Proposal not found")
        
        proposal = self.proposals[proposal_uid]
        if proposal.votes_for > proposal.votes_against:
            proposal.status = "approved"
            proposal.record.close()
        else:
            proposal.status = "rejected"


# ============================================================================
# Proposal 11: Ancient Text Search
# ============================================================================

class AncientTextSearchEngine:
    """
    Semantic search for ancient texts.
    
    Index and search based on structure, not words.
    """
    
    def __init__(self):
        self.corpus: List[Record] = []
        self.index: Dict[str, List[int]] = {}
    
    def index_text(self, record: Record) -> None:
        """Index a text record."""
        idx = len(self.corpus)
        self.corpus.append(record)
        
        # Index by symbol types
        for symbol in record.symbols:
            key = symbol.symbol_type.value
            if key not in self.index:
                self.index[key] = []
            self.index[key].append(idx)
    
    def search(self, pattern: List[SymbolType]) -> List[Record]:
        """Search for records matching a pattern."""
        results = []
        for record in self.corpus:
            if self._matches_pattern(record, pattern):
                results.append(record)
        return results
    
    def _matches_pattern(self, record: Record, pattern: List[SymbolType]) -> bool:
        """Check if a record matches a pattern."""
        record_types = [s.symbol_type for s in record.symbols]
        return all(p in record_types for p in pattern)


# ============================================================================
# Proposal 12: Algorithmic Art Generator
# ============================================================================

class ArtGenerator:
    """
    Algorithmic art using Harappa composition rules.
    
    Generates visual art with structural meaning.
    """
    
    def __init__(self):
        self.artworks: List[Record] = []
    
    def generate_artwork(self, seed: int, complexity: int = 5) -> Record:
        """Generate a new artwork."""
        random.seed(seed)
        record = Record()
        
        # Generate symbols
        for i in range(complexity):
            symbol = Symbol(
                id=f"art_symbol_{i}",
                symbol_type=random.choice(list(SymbolType))
            )
            record.add_symbol(symbol)
        
        # Add composition operators
        for i in range(complexity - 1):
            operator = Operator(
                name=f"compose_{i}",
                operator_type=OperatorType.COMPOSITION,
                arity=2
            )
            record.add_operator(operator)
        
        record.close()
        self.artworks.append(record)
        return record


# ============================================================================
# Proposal 13: Authentication Protocol
# ============================================================================

class AuthenticationSystem:
    """
    Password-less authentication using Harappa seals.
    
    Digital seals for identity and permissions.
    """
    
    def __init__(self):
        self.user_seals: Dict[str, HarappaUID] = {}
        self.permissions: Dict[str, Set[str]] = {}
    
    def register_user(self, user_id: str, seal: HarappaUID) -> None:
        """Register a user with their Harappa seal."""
        self.user_seals[user_id] = seal
        self.permissions[user_id] = set()
    
    def authenticate(self, user_id: str, presented_seal: HarappaUID) -> bool:
        """Authenticate a user."""
        if user_id not in self.user_seals:
            return False
        return self.user_seals[user_id] == presented_seal
    
    def grant_permission(self, user_id: str, permission: str) -> None:
        """Grant a permission to a user."""
        if user_id in self.permissions:
            self.permissions[user_id].add(permission)
    
    def check_permission(self, user_id: str, permission: str) -> bool:
        """Check if a user has a permission."""
        return permission in self.permissions.get(user_id, set())


# ============================================================================
# Proposal 14: Web Service Choreography
# ============================================================================

@dataclass
class ServiceCall:
    """A web service call in choreography."""
    service_name: str
    operation: str
    operator: Operator
    input_state: State
    output_state: Optional[State] = None


class ServiceChoreography:
    """
    Web service choreography using Harappa notation.
    
    Specifies message flows and service orchestration.
    """
    
    def __init__(self):
        self.services: Dict[str, List[ServiceCall]] = {}
        self.flows: List[Record] = []
    
    def define_service(self, service_name: str, operations: List[ServiceCall]) -> None:
        """Define a service with its operations."""
        self.services[service_name] = operations
    
    def create_flow(self, calls: List[ServiceCall]) -> Record:
        """Create a choreography flow."""
        record = Record()
        
        for call in calls:
            record.add_operator(call.operator)
            if call.input_state:
                record.add_state(call.input_state)
        
        record.close()
        self.flows.append(record)
        return record


# ============================================================================
# Proposal 15: Risk Analysis
# ============================================================================

@dataclass
class Task:
    """A task in a project."""
    name: str
    symbol: Symbol
    dependencies: List['Task'] = field(default_factory=list)
    risk_level: float = 0.0
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.name == other.name


class RiskAnalysisTool:
    """
    Risk analysis for complex projects.
    
    Represents projects as Harappa sequences.
    """
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.project_record: Optional[Record] = None
    
    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
    
    def analyze_risks(self) -> Dict[str, Any]:
        """Analyze project risks."""
        total_risk = sum(task.risk_level for task in self.tasks)
        avg_risk = total_risk / len(self.tasks) if self.tasks else 0
        
        # Check for circular dependencies
        circular_deps = self._check_circular_dependencies()
        
        # Check for missing closure (incomplete tasks)
        record = self._build_project_record()
        missing_closure = not record.has_closure
        
        return {
            "total_tasks": len(self.tasks),
            "average_risk": avg_risk,
            "has_circular_dependencies": circular_deps,
            "missing_closure": missing_closure,
            "high_risk_tasks": [t.name for t in self.tasks if t.risk_level > 0.7]
        }
    
    def _check_circular_dependencies(self) -> bool:
        """Check for circular task dependencies."""
        visited = set()
        rec_stack = set()
        
        def has_cycle(task):
            visited.add(task)
            rec_stack.add(task)
            
            for dep in task.dependencies:
                if dep not in visited:
                    if has_cycle(dep):
                        return True
                elif dep in rec_stack:
                    return True
            
            rec_stack.remove(task)
            return False
        
        for task in self.tasks:
            if task not in visited:
                if has_cycle(task):
                    return True
        
        return False
    
    def _build_project_record(self) -> Record:
        """Build a Harappa record representing the project."""
        record = Record()
        
        for task in self.tasks:
            record.add_symbol(task.symbol)
        
        # Check if all tasks are complete (simplified)
        if all(task.risk_level < 0.5 for task in self.tasks):
            record.close()
        
        self.project_record = record
        return record
