(*
  Indus Script Non-Local Invariance - Formal Definition in Isabelle/HOL
  
  This theory formalizes the concept of "non-local invariance" in the Indus script
  as DISTRIBUTED STANDARDIZATION, not quantum mechanical non-locality.
  
  We prove properties about:
  - Spatial distribution of patterns
  - Cross-site consistency
  - Institutional standardization
*)

theory IndusInvariance
  imports Main "HOL-Probability.Probability"
begin

(* Basic types *)
type_synonym symbol = nat
type_synonym site = string
type_synonym sequence = "symbol list"

(* A site contains multiple sequences *)
type_synonym site_data = "site × sequence list"

(* Co-occurrence pattern *)
record cooccurrence_pattern =
  sym1 :: symbol
  sym2 :: symbol
  min_dist :: nat
  max_dist :: nat

(* Check if pattern occurs in sequence *)
definition satisfies_pattern :: "sequence ⇒ cooccurrence_pattern ⇒ bool" where
  "satisfies_pattern seq pat = (∃i j. 
    i < length seq ∧ j < length seq ∧
    seq ! i = sym1 pat ∧ seq ! j = sym2 pat ∧
    min_dist pat ≤ |int i - int j| ∧ |int i - int j| ≤ max_dist pat)"

(* Pattern frequency at a site *)
definition pattern_frequency :: "site_data ⇒ cooccurrence_pattern ⇒ real" where
  "pattern_frequency sd pat = (
    let (_, seqs) = sd in
    let matches = length (filter (λs. satisfies_pattern s pat) seqs) in
    let total = length seqs in
    if total = 0 then 0 else real matches / real total
  )"

(* Cross-site variance (low variance = high standardization) *)
definition cross_site_variance :: "site_data list ⇒ cooccurrence_pattern ⇒ real" where
  "cross_site_variance sites pat = (
    let freqs = map (λsd. pattern_frequency sd pat) sites in
    let n = real (length freqs) in
    let mean = sum_list freqs / n in
    sum_list (map (λf. (f - mean)^2) freqs) / n
  )"

(* Non-local invariance: pattern is stable across sites
   "Non-local" = spatially distributed, NOT quantum non-locality *)
definition non_local_invariant :: "site_data list ⇒ cooccurrence_pattern ⇒ real ⇒ bool" where
  "non_local_invariant sites pat threshold = (
    cross_site_variance sites pat < threshold
  )"

(* Institutional standardization: many patterns are invariant *)
definition institutional_standardization :: "site_data list ⇒ cooccurrence_pattern list ⇒ real ⇒ bool" where
  "institutional_standardization sites patterns threshold = (
    let invariant_patterns = filter (λp. non_local_invariant sites p threshold) patterns in
    real (length invariant_patterns) / real (length patterns) > 0.5
  )"

(* Theorem: If pattern has zero variance, it's invariant for any threshold > 0 *)
lemma zero_variance_is_invariant:
  assumes "cross_site_variance sites pat = 0"
  assumes "threshold > 0"
  shows "non_local_invariant sites pat threshold"
  unfolding non_local_invariant_def
  using assms by simp

(* Theorem: Pattern frequency is bounded *)
lemma pattern_frequency_bounded:
  shows "0 ≤ pattern_frequency sd pat ∧ pattern_frequency sd pat ≤ 1"
proof -
  obtain site seqs where "sd = (site, seqs)" by (cases sd)
  show ?thesis
    unfolding pattern_frequency_def
    by (auto simp: Let_def)
qed

(* Theorem: Cross-site variance is non-negative *)
lemma variance_nonneg:
  shows "cross_site_variance sites pat ≥ 0"
  unfolding cross_site_variance_def
  by (auto simp: Let_def)

end
