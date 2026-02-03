// SPDX-License-Identifier: CC-BY-4.0
pragma solidity ^0.8.0;

/**
 * @title IndusRecord
 * @dev Smart contract implementing Harappan operational logic for blockchain validation
 * 
 * This contract translates the 2600 BCE Indus script validation protocol into
 * a modern blockchain implementation, demonstrating the timeless nature of
 * operational mathematics.
 */
contract IndusRecord {
    
    // ====================================================================
    // STATE DEFINITIONS (Based on Indus Automaton)
    // ====================================================================
    
    enum State {
        Initial,        // S0: No entity defined
        EntityDefined,  // S1: Entity recognized
        Qualified,      // S2: Qualifications applied
        Quantified,     // S3: Quantity specified
        Related,        // S4: Relations established
        Closed          // S5: Record closed (accepting state)
    }
    
    // ====================================================================
    // SYMBOL CLASS DEFINITIONS
    // ====================================================================
    
    enum EntityClass {
        Oval,      // 373-399: Institutional entities
        Vessel,    // 328-339: Containers
        Authority, // 250-260: Hierarchical markers
        Animal,    // 200-210: Functional agents
        Metric     // 100-150: Measurement units
    }
    
    enum ClosureType {
        Simple,       // 342: Basic validation
        Confirmed,    // 343: Confirmed validation
        Validated,    // 344: Double-checked
        Sealed,       // 345: Sealed record
        Absolute,     // 346: Absolute authority
        Hierarchical, // 347: Hierarchical validation
        Terminal      // 348: Final closure
    }
    
    // ====================================================================
    // RECORD STRUCTURE
    // ====================================================================
    
    struct Record {
        uint256 id;
        address creator;
        EntityClass entity;
        uint256 entityId;
        address[] qualifiers;
        uint256 quantity;
        uint256[] relations;
        ClosureType closure;
        State state;
        uint256 timestamp;
        bool exists;
    }
    
    // ====================================================================
    // STORAGE
    // ====================================================================
    
    mapping(uint256 => Record) public records;
    uint256 public recordCount;
    
    // ====================================================================
    // EVENTS (Transition Logging)
    // ====================================================================
    
    event RecordCreated(uint256 indexed recordId, address creator, EntityClass entity);
    event QualifierAdded(uint256 indexed recordId, address qualifier);
    event QuantitySet(uint256 indexed recordId, uint256 quantity);
    event RelationAdded(uint256 indexed recordId, uint256 relationId);
    event RecordClosed(uint256 indexed recordId, ClosureType closureType);
    event StateTransition(uint256 indexed recordId, State from, State to);
    
    // ====================================================================
    // MODIFIERS (State Guards)
    // ====================================================================
    
    modifier recordExists(uint256 recordId) {
        require(records[recordId].exists, "Record does not exist");
        _;
    }
    
    modifier onlyCreator(uint256 recordId) {
        require(records[recordId].creator == msg.sender, "Not record creator");
        _;
    }
    
    modifier inState(uint256 recordId, State requiredState) {
        require(records[recordId].state == requiredState, "Invalid state");
        _;
    }
    
    modifier notClosed(uint256 recordId) {
        require(records[recordId].state != State.Closed, "Record already closed");
        _;
    }
    
    // ====================================================================
    // CORE FUNCTIONS (Automaton Transitions)
    // ====================================================================
    
    /**
     * @dev Create new record (S0 → S1: Initial → EntityDefined)
     * @param entityClass The entity class for this record
     * @param entityId The specific entity identifier (e.g., 373, 200)
     */
    function createRecord(EntityClass entityClass, uint256 entityId) 
        external 
        returns (uint256) 
    {
        // Validate entity ID ranges (simplified)
        require(entityId >= 100 && entityId <= 399, "Invalid entity ID");
        
        recordCount++;
        uint256 recordId = recordCount;
        
        Record storage record = records[recordId];
        record.id = recordId;
        record.creator = msg.sender;
        record.entity = entityClass;
        record.entityId = entityId;
        record.state = State.EntityDefined;
        record.timestamp = block.timestamp;
        record.exists = true;
        
        emit RecordCreated(recordId, msg.sender, entityClass);
        emit StateTransition(recordId, State.Initial, State.EntityDefined);
        
        return recordId;
    }
    
    /**
     * @dev Add qualifier (S1 → S2: EntityDefined → Qualified)
     * @param recordId The record to qualify
     * @param qualifier Address acting as qualifier
     */
    function addQualifier(uint256 recordId, address qualifier)
        external
        recordExists(recordId)
        onlyCreator(recordId)
        notClosed(recordId)
    {
        Record storage record = records[recordId];
        
        // Valid from EntityDefined or Qualified states
        require(
            record.state == State.EntityDefined || 
            record.state == State.Qualified,
            "Cannot add qualifier in this state"
        );
        
        record.qualifiers.push(qualifier);
        
        State oldState = record.state;
        record.state = State.Qualified;
        
        emit QualifierAdded(recordId, qualifier);
        if (oldState != State.Qualified) {
            emit StateTransition(recordId, oldState, State.Qualified);
        }
    }
    
    /**
     * @dev Set quantity (S1/S2 → S3: → Quantified)
     * @param recordId The record to quantify
     * @param quantity The quantity value (1-100)
     */
    function setQuantity(uint256 recordId, uint256 quantity)
        external
        recordExists(recordId)
        onlyCreator(recordId)
        notClosed(recordId)
    {
        Record storage record = records[recordId];
        
        // Valid from EntityDefined, Qualified states
        require(
            record.state == State.EntityDefined || 
            record.state == State.Qualified,
            "Cannot set quantity in this state"
        );
        
        require(quantity > 0 && quantity <= 100, "Invalid quantity");
        
        record.quantity = quantity;
        
        State oldState = record.state;
        record.state = State.Quantified;
        
        emit QuantitySet(recordId, quantity);
        emit StateTransition(recordId, oldState, State.Quantified);
    }
    
    /**
     * @dev Add relation (S1/S2/S3 → S4: → Related)
     * @param recordId The record to relate
     * @param relationId The relation identifier (400-409)
     */
    function addRelation(uint256 recordId, uint256 relationId)
        external
        recordExists(recordId)
        onlyCreator(recordId)
        notClosed(recordId)
    {
        Record storage record = records[recordId];
        
        // Valid from EntityDefined, Qualified, Quantified states
        require(
            record.state == State.EntityDefined || 
            record.state == State.Qualified ||
            record.state == State.Quantified,
            "Cannot add relation in this state"
        );
        
        require(relationId >= 400 && relationId <= 409, "Invalid relation ID");
        
        record.relations.push(relationId);
        
        State oldState = record.state;
        record.state = State.Related;
        
        emit RelationAdded(recordId, relationId);
        emit StateTransition(recordId, oldState, State.Related);
    }
    
    /**
     * @dev Close record (Any valid state → S5: → Closed)
     * @param recordId The record to close
     * @param closureType The type of closure (342-348)
     */
    function closeRecord(uint256 recordId, ClosureType closureType)
        external
        recordExists(recordId)
        onlyCreator(recordId)
        notClosed(recordId)
    {
        Record storage record = records[recordId];
        
        // Must be in a valid state (not Initial)
        require(record.state != State.Initial, "Cannot close uninitialized record");
        
        State oldState = record.state;
        record.closure = closureType;
        record.state = State.Closed;
        
        emit RecordClosed(recordId, closureType);
        emit StateTransition(recordId, oldState, State.Closed);
    }
    
    // ====================================================================
    // VIEW FUNCTIONS
    // ====================================================================
    
    /**
     * @dev Check if record is valid (in accepting state)
     */
    function isValidRecord(uint256 recordId) 
        external 
        view 
        recordExists(recordId)
        returns (bool) 
    {
        return records[recordId].state == State.Closed;
    }
    
    /**
     * @dev Get record details
     */
    function getRecord(uint256 recordId)
        external
        view
        recordExists(recordId)
        returns (
            EntityClass entity,
            uint256 entityId,
            uint256 qualifierCount,
            uint256 quantity,
            uint256 relationCount,
            ClosureType closure,
            State state
        )
    {
        Record storage record = records[recordId];
        return (
            record.entity,
            record.entityId,
            record.qualifiers.length,
            record.quantity,
            record.relations.length,
            record.closure,
            record.state
        );
    }
    
    /**
     * @dev Get all qualifiers for a record
     */
    function getQualifiers(uint256 recordId)
        external
        view
        recordExists(recordId)
        returns (address[] memory)
    {
        return records[recordId].qualifiers;
    }
    
    /**
     * @dev Get all relations for a record
     */
    function getRelations(uint256 recordId)
        external
        view
        recordExists(recordId)
        returns (uint256[] memory)
    {
        return records[recordId].relations;
    }
}

/**
 * USAGE EXAMPLE:
 * 
 * // Create a record (Entity: Basic Token, ID: 373)
 * uint256 recordId = indusRecord.createRecord(EntityClass.Oval, 373);
 * 
 * // Add a qualifier (optional)
 * indusRecord.addQualifier(recordId, qualifierAddress);
 * 
 * // Set quantity (optional)
 * indusRecord.setQuantity(recordId, 3);
 * 
 * // Add a relation (optional)
 * indusRecord.addRelation(recordId, 400); // Pair relation
 * 
 * // Close the record (required)
 * indusRecord.closeRecord(recordId, ClosureType.Confirmed);
 * 
 * // Verify record is valid
 * bool valid = indusRecord.isValidRecord(recordId); // true
 */

/**
 * NOTES:
 * 
 * 1. This contract implements the same finite automaton as the Indus script
 * 2. State transitions are enforced by modifiers
 * 3. Invalid transitions are rejected (just like invalid Indus sequences)
 * 4. Records must be closed to be considered valid
 * 5. The closure is immutable (absorbing state)
 * 
 * The Harappan civilization used this logic 4,500 years ago for clay seals.
 * We're using it now for blockchain transactions.
 * 
 * The mathematics is eternal.
 */
