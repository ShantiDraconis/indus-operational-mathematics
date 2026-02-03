{- 
  Indus Script Type-Theoretic Formalization in Agda
  
  This module uses dependent types to express constraints and invariants
  in the Indus script system.
  
  DISCLAIMER: This is a type-theoretic model of constraint satisfaction,
  NOT a quantum mechanical system. "Superposition" is used as a metaphor
  for ambiguity before constraint resolution.
-}

module IndusTypeTheory where

open import Data.Nat using (ℕ; zero; suc; _+_; _*_; _≤_; _<_)
open import Data.List using (List; []; _∷_; length; filter; map)
open import Data.Bool using (Bool; true; false; _∧_; _∨_)
open import Data.Product using (_×_; _,_; proj₁; proj₂)
open import Relation.Binary.PropositionalEquality using (_≡_; refl; cong)

-- Basic symbol type
data Symbol : Set where
  numeric : ℕ → Symbol
  pictographic : ℕ → Symbol  -- Using ℕ as identifier
  abstract : ℕ → Symbol

-- Grammatical state (discrete states, not quantum states)
data GrammaticalState : Set where
  existential : GrammaticalState
  instanced : GrammaticalState
  delimited : GrammaticalState
  authorized : GrammaticalState
  closed : GrammaticalState

-- Valid state transitions
data ValidTransition : GrammaticalState → GrammaticalState → Set where
  exist→instance : ValidTransition existential instanced
  instance→delimited : ValidTransition instanced delimited
  delimited→authorized : ValidTransition delimited authorized
  authorized→closed : ValidTransition authorized closed

-- Position in sequence
Position : Set
Position = ℕ

-- Symbol in context
record SymbolInContext : Set where
  field
    symbol : Symbol
    position : Position
    state : GrammaticalState

-- Sequence with well-formed state transitions
data WellFormedSequence : List SymbolInContext → Set where
  empty : WellFormedSequence []
  single : (s : SymbolInContext) → WellFormedSequence (s ∷ [])
  cons : {s1 s2 : SymbolInContext} {rest : List SymbolInContext}
       → ValidTransition (SymbolInContext.state s1) (SymbolInContext.state s2)
       → WellFormedSequence (s2 ∷ rest)
       → WellFormedSequence (s1 ∷ s2 ∷ rest)

-- Co-occurrence constraint with distance bounds
record CooccurrenceConstraint : Set where
  field
    symbol1 : Symbol
    symbol2 : Symbol
    minDistance : ℕ
    maxDistance : ℕ

-- Distance between positions
distance : Position → Position → ℕ
distance p1 p2 with p1 <? p2
... | true = p2 - p1
... | false = p1 - p2
  where
  _<?_ : ℕ → ℕ → Bool
  zero <? zero = false
  zero <? suc n = true
  suc m <? zero = false
  suc m <? suc n = m <? n

  _-_ : ℕ → ℕ → ℕ
  m - zero = m
  zero - suc n = zero
  suc m - suc n = m - n

-- Satisfaction of co-occurrence constraint
SatisfiesConstraint : CooccurrenceConstraint → Position → Position → Set
SatisfiesConstraint c p1 p2 = 
  let d = distance p1 p2 in
  (CooccurrenceConstraint.minDistance c ≤ d) × 
  (d ≤ CooccurrenceConstraint.maxDistance c)

-- Non-local invariance: property preserved across multiple sites
-- "Non-local" means SPATIALLY DISTRIBUTED, not quantum non-locality
record NonLocalInvariance (Property : List SymbolInContext → Set) : Set where
  field
    sites : List ℕ  -- Site identifiers
    preservation : (siteId : ℕ) → (seq : List SymbolInContext) → Property seq

-- Statistical analogy structure (NOT quantum mechanics)
record StatisticalCorrelation : Set where
  field
    symbol1 : Symbol
    symbol2 : Symbol
    jointProbability : ℕ  -- Represented as rational (numerator, total fixed)
    marginal1Probability : ℕ
    marginal2Probability : ℕ
    total : ℕ

-- Theorem: Well-formed sequences preserve state ordering property
stateOrderingPreserved : {s1 s2 : SymbolInContext} {rest : List SymbolInContext}
                       → WellFormedSequence (s1 ∷ s2 ∷ rest)
                       → ValidTransition (SymbolInContext.state s1) (SymbolInContext.state s2)
stateOrderingPreserved (cons trans _) = trans

-- Composition of valid transitions (path in state space)
data TransitionPath : GrammaticalState → GrammaticalState → Set where
  single-step : {s1 s2 : GrammaticalState} 
              → ValidTransition s1 s2 
              → TransitionPath s1 s2
  multi-step : {s1 s2 s3 : GrammaticalState}
             → ValidTransition s1 s2
             → TransitionPath s2 s3
             → TransitionPath s1 s3
