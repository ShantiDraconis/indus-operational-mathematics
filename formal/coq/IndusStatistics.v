(*
  Indus Script Statistical Analysis - Formal Definition in Coq
  
  This module provides formal definitions for statistical measures used in
  analyzing Indus script correlations.
  
  IMPORTANT DISCLAIMER: All "entanglement" and "non-locality" terminology
  refers to STATISTICAL correlations and distributed standardization, NOT
  to quantum mechanical phenomena. This is strictly classical information theory.
*)

Require Import Reals.
Require Import List.
Require Import Arith.
Import ListNotations.

Module IndusStatistics.

  (* Basic types *)
  Definition Symbol := nat.
  Definition Site := nat.
  Definition Sequence := list Symbol.
  
  (* Position in sequence *)
  Record Position := {
    seq_id : nat;
    index : nat
  }.

  (* Co-occurrence data *)
  Record Cooccurrence := {
    symbol_a : Symbol;
    symbol_b : Symbol;
    distance : nat;
    site : Site
  }.

  (* Frequency counts *)
  Definition frequency (s : Symbol) (seqs : list Sequence) : nat :=
    fold_left (fun acc seq => acc + count_occ Nat.eq_dec seq s) seqs 0.

  (* Joint frequency for pair *)
  Definition joint_frequency (a b : Symbol) (seqs : list Sequence) : nat :=
    fold_left (fun acc seq => 
      if existsb (Nat.eqb a) seq && existsb (Nat.eqb b) seq 
      then S acc 
      else acc
    ) seqs 0.

  (* Probability from frequency *)
  Definition probability (freq total : nat) : R :=
    match total with
    | 0 => R0
    | S _ => INR freq / INR total
    end.

  (* Pointwise Mutual Information (PMI)
     This is a STATISTICAL measure of association, not quantum entanglement *)
  Definition pmi (p_xy p_x p_y : R) : R :=
    if Req_EM_T p_xy R0 then R0
    else if Req_EM_T p_x R0 then R0
    else if Req_EM_T p_y R0 then R0
    else ln (p_xy / (p_x * p_y)).

  (* Lift (odds ratio) - another statistical correlation measure *)
  Definition lift (p_xy p_x p_y : R) : R :=
    if Req_EM_T (p_x * p_y) R0 then R0
    else p_xy / (p_x * p_y).

  (* Non-local invariance: statistical property preserved across sites
     "Non-local" here means SPATIALLY DISTRIBUTED, not quantum non-locality *)
  Record NonLocalInvariance := {
    property : Sequence -> Prop;
    sites : list Site;
    preserved : forall s, In s sites -> exists seq, property seq
  }.

  (* Cross-site variance: measure of standardization
     Low variance = high standardization = distributed institutional pattern *)
  Definition cross_site_variance (values : list R) : R :=
    let n := INR (length values) in
    let mean := fold_left Rplus values R0 / n in
    fold_left (fun acc v => acc + ((v - mean) * (v - mean))) values R0 / n.

  (* Theorem: PMI is symmetric *)
  Theorem pmi_symmetric : forall p_xy p_x p_y,
    pmi p_xy p_x p_y = pmi p_xy p_y p_x.
  Proof.
    intros.
    unfold pmi.
    destruct (Req_EM_T p_xy R0); [reflexivity|].
    destruct (Req_EM_T p_x R0); destruct (Req_EM_T p_y R0); try reflexivity.
    (* Both denominators non-zero *)
    rewrite Rmult_comm.
    reflexivity.
  Qed.

  (* Theorem: Lift is symmetric *)
  Theorem lift_symmetric : forall p_xy p_x p_y,
    lift p_xy p_x p_y = lift p_xy p_y p_x.
  Proof.
    intros.
    unfold lift.
    destruct (Req_EM_T (p_x * p_y) R0).
    - destruct (Req_EM_T (p_y * p_x) R0); [reflexivity|].
      exfalso. apply n. rewrite Rmult_comm. exact r.
    - destruct (Req_EM_T (p_y * p_x) R0).
      + exfalso. apply n. rewrite Rmult_comm. exact r.
      + rewrite Rmult_comm. reflexivity.
  Qed.

  (* Distance-dependent correlation *)
  Definition distance_correlation (coocc : list Cooccurrence) (d : nat) : R :=
    let at_distance := filter (fun c => Nat.eqb c.(distance) d) coocc in
    INR (length at_distance) / INR (length coocc).

End IndusStatistics.
