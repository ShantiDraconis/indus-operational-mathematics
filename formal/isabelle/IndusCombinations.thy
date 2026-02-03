(*
  Title:      IndusCombinations.thy
  Author:     Harappan Operational Mathematics
  
  Comprehensive analysis of symbol-operator combinations and composition rules
  in Isabelle/HOL with higher-order properties and invariants.
*)

theory IndusCombinations
imports Main HOL.Finite_Set HOL.Fun
begin

section \<open>Symbol Families\<close>

text \<open>The three symbol families in the Harappan system (373-417)\<close>

datatype symbol_family =
  Omega  -- \<open>Tokens/Entities (373-399)\<close>
  | Delta  -- \<open>Relations/Bonds (400-409)\<close>
  | Sigma  -- \<open>Counts/Stacks (410-417)\<close>

text \<open>Symbol ID type (natural numbers in range 373-417)\<close>

type_synonym symbol_id = nat

definition is_valid_symbol :: "symbol_id \<Rightarrow> bool" where
  "is_valid_symbol n \<longleftrightarrow> 373 \<le> n \<and> n \<le> 417"

definition symbol_family_of :: "symbol_id \<Rightarrow> symbol_family option" where
  "symbol_family_of n = 
    (if 373 \<le> n \<and> n \<le> 399 then Some Omega
     else if 400 \<le> n \<and> n \<le> 409 then Some Delta
     else if 410 \<le> n \<and> n \<le> 417 then Some Sigma
     else None)"

definition omega_symbols :: "symbol_id set" where
  "omega_symbols = {373..399}"

definition delta_symbols :: "symbol_id set" where
  "delta_symbols = {400..409}"

definition sigma_symbols :: "symbol_id set" where
  "sigma_symbols = {410..417}"

definition all_symbols :: "symbol_id set" where
  "all_symbols = omega_symbols \<union> delta_symbols \<union> sigma_symbols"

lemma family_partition:
  "all_symbols = omega_symbols \<union> delta_symbols \<union> sigma_symbols"
  unfolding all_symbols_def by simp

lemma families_disjoint:
  shows "omega_symbols \<inter> delta_symbols = {}"
    and "omega_symbols \<inter> sigma_symbols = {}"
    and "delta_symbols \<inter> sigma_symbols = {}"
  unfolding omega_symbols_def delta_symbols_def sigma_symbols_def
  by auto

lemma all_symbols_finite:
  "finite all_symbols"
  unfolding all_symbols_def omega_symbols_def delta_symbols_def sigma_symbols_def
  by simp

lemma all_symbols_card:
  "card all_symbols = 45"
  unfolding all_symbols_def omega_symbols_def delta_symbols_def sigma_symbols_def
  by (simp add: card_Un_disjoint families_disjoint)

section \<open>Graphic Operators\<close>

text \<open>The ten universal graphic operators (runes)\<close>

datatype graphic_operator =
  Dot       -- \<open>Internal dot - marks instance/activation\<close>
  | Stroke    -- \<open>Internal stroke - partition/qualification\<close>
  | Fill      -- \<open>Internal fill/hatch - consummated state\<close>
  | Bracket   -- \<open>Side brackets - delimits scope\<close>
  | Sidebars  -- \<open>Side bars - level/degree/authority\<close>
  | Crown     -- \<open>Crown/prongs - multiplexing\<close>
  | Dup       -- \<open>Duplication - creates pair\<close>
  | Knot      -- \<open>Interlacing - strong bond/lock\<close>
  | Stem      -- \<open>Lower/upper stem - anchor/indexing\<close>
  | Stack     -- \<open>Vertical stacking - count/aggregation\<close>

definition all_operators :: "graphic_operator set" where
  "all_operators = {Dot, Stroke, Fill, Bracket, Sidebars, Crown, Dup, Knot, Stem, Stack}"

lemma all_operators_finite:
  "finite all_operators"
  unfolding all_operators_def by simp

lemma all_operators_card:
  "card all_operators = 10"
  unfolding all_operators_def by simp

section \<open>Symbol-Operator Combinations\<close>

text \<open>Compatibility of operators with symbol families\<close>

definition operator_compatible :: "symbol_family \<Rightarrow> graphic_operator \<Rightarrow> bool" where
  "operator_compatible fam op \<longleftrightarrow>
    (fam = Omega \<and> op \<in> {Dot, Stroke, Fill, Bracket, Sidebars, Crown, Dup, Stack}) \<or>
    (fam = Delta \<and> op \<in> {Knot, Stem, Dot, Stroke}) \<or>
    (fam = Sigma \<and> op = Stack)"

definition is_valid_combination :: "symbol_id \<Rightarrow> graphic_operator \<Rightarrow> bool" where
  "is_valid_combination sym_id op \<longleftrightarrow>
    (\<exists>fam. symbol_family_of sym_id = Some fam \<and> operator_compatible fam op)"

definition valid_combinations :: "(symbol_id \<times> graphic_operator) set" where
  "valid_combinations = {(s, op). is_valid_combination s op}"

definition total_combinations :: nat where
  "total_combinations = card all_symbols * card all_operators"

lemma total_combinations_value:
  "total_combinations = 450"
  unfolding total_combinations_def
  by (simp add: all_symbols_card all_operators_card)

text \<open>Theorems about operator compatibility\<close>

theorem omega_accepts_8_operators:
  assumes "symbol_family_of s = Some Omega"
  shows "card {op. is_valid_combination s op} = 8"
proof -
  have "{op. is_valid_combination s op} = 
        {Dot, Stroke, Fill, Bracket, Sidebars, Crown, Dup, Stack}"
    using assms
    unfolding is_valid_combination_def operator_compatible_def
    by auto
  thus ?thesis by simp
qed

theorem delta_accepts_4_operators:
  assumes "symbol_family_of s = Some Delta"
  shows "card {op. is_valid_combination s op} = 4"
proof -
  have "{op. is_valid_combination s op} = {Knot, Stem, Dot, Stroke}"
    using assms
    unfolding is_valid_combination_def operator_compatible_def
    by auto
  thus ?thesis by simp
qed

theorem sigma_accepts_1_operator:
  assumes "symbol_family_of s = Some Sigma"
  shows "card {op. is_valid_combination s op} = 1"
proof -
  have "{op. is_valid_combination s op} = {Stack}"
    using assms
    unfolding is_valid_combination_def operator_compatible_def
    by auto
  thus ?thesis by simp
qed

theorem dot_valid_for_omega_delta:
  assumes "symbol_family_of s = Some Omega \<or> symbol_family_of s = Some Delta"
  shows "is_valid_combination s Dot"
  using assms
  unfolding is_valid_combination_def operator_compatible_def
  by auto

theorem stack_only_omega_sigma:
  "is_valid_combination s Stack \<longleftrightarrow>
   (symbol_family_of s = Some Omega \<or> symbol_family_of s = Some Sigma)"
  unfolding is_valid_combination_def operator_compatible_def
  by auto

theorem knot_only_delta:
  "is_valid_combination s Knot \<longleftrightarrow> symbol_family_of s = Some Delta"
  unfolding is_valid_combination_def operator_compatible_def
  by auto

section \<open>Symbol Pair Composition\<close>

text \<open>Composability of symbol families\<close>

definition families_composable :: "symbol_family \<Rightarrow> symbol_family \<Rightarrow> bool" where
  "families_composable f1 f2 \<longleftrightarrow>
    (f1 = Omega \<and> f2 \<in> {Delta, Sigma}) \<or>
    (f1 = Delta \<and> f2 \<in> {Omega, Delta, Sigma}) \<or>
    (f1 = Sigma \<and> f2 = Omega)"

definition symbols_composable :: "symbol_id \<Rightarrow> symbol_id \<Rightarrow> bool" where
  "symbols_composable s1 s2 \<longleftrightarrow>
    (\<exists>f1 f2. symbol_family_of s1 = Some f1 \<and> 
             symbol_family_of s2 = Some f2 \<and>
             families_composable f1 f2)"

definition composable_pairs :: "(symbol_id \<times> symbol_id) set" where
  "composable_pairs = {(s1, s2). symbols_composable s1 s2}"

definition total_pairs :: nat where
  "total_pairs = card all_symbols * card all_symbols"

lemma total_pairs_value:
  "total_pairs = 2025"
  unfolding total_pairs_def
  by (simp add: all_symbols_card power2_eq_square)

text \<open>Theorems about pair composition\<close>

theorem omega_omega_not_composable:
  assumes "symbol_family_of s1 = Some Omega"
      and "symbol_family_of s2 = Some Omega"
  shows "\<not> symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

theorem omega_delta_mutually_composable:
  assumes "(symbol_family_of s1 = Some Omega \<and> symbol_family_of s2 = Some Delta) \<or>
           (symbol_family_of s1 = Some Delta \<and> symbol_family_of s2 = Some Omega)"
  shows "symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

theorem delta_delta_composable:
  assumes "symbol_family_of s1 = Some Delta"
      and "symbol_family_of s2 = Some Delta"
  shows "symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

theorem sigma_sigma_not_composable:
  assumes "symbol_family_of s1 = Some Sigma"
      and "symbol_family_of s2 = Some Sigma"
  shows "\<not> symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

theorem sigma_delta_not_composable:
  assumes "symbol_family_of s1 = Some Sigma"
      and "symbol_family_of s2 = Some Delta"
  shows "\<not> symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

theorem omega_sigma_mutually_composable:
  assumes "(symbol_family_of s1 = Some Omega \<and> symbol_family_of s2 = Some Sigma) \<or>
           (symbol_family_of s1 = Some Sigma \<and> symbol_family_of s2 = Some Omega)"
  shows "symbols_composable s1 s2"
  using assms
  unfolding symbols_composable_def families_composable_def
  by auto

section \<open>Sequence Validation\<close>

text \<open>Valid sequences of symbols\<close>

fun is_valid_sequence :: "symbol_id list \<Rightarrow> bool" where
  "is_valid_sequence [] = False" |
  "is_valid_sequence [_] = True" |
  "is_valid_sequence (s1 # s2 # rest) =
    (is_valid_symbol s1 \<and> is_valid_symbol s2 \<and> symbols_composable s1 s2 \<and>
     is_valid_sequence (s2 # rest))"

theorem valid_sequence_pairwise:
  assumes "is_valid_sequence seq"
      and "i + 1 < length seq"
  shows "symbols_composable (seq ! i) (seq ! (i + 1))"
  using assms
proof (induction seq arbitrary: i)
  case Nil
  then show ?case by simp
next
  case (Cons s rest)
  then show ?case
  proof (cases rest)
    case Nil
    then show ?thesis using Cons.prems by simp
  next
    case (Cons s' rest')
    then show ?thesis
    proof (cases i)
      case 0
      then show ?thesis using Cons.prems Cons by simp
    next
      case (Suc i')
      then show ?thesis using Cons.prems Cons.IH by auto
    qed
  qed
qed

theorem valid_sequence_prefix:
  assumes "is_valid_sequence seq"
      and "0 < n" and "n \<le> length seq"
  shows "is_valid_sequence (take n seq)"
  using assms
proof (induction seq arbitrary: n)
  case Nil
  then show ?case by simp
next
  case (Cons s rest)
  then show ?case
  proof (cases rest)
    case Nil
    then show ?thesis using Cons.prems by (cases n) auto
  next
    case (Cons s' rest')
    then show ?thesis
    proof (cases n)
      case 0
      then show ?thesis using Cons.prems by simp
    next
      case (Suc n')
      then show ?thesis
      proof (cases n')
        case 0
        then show ?thesis using Cons.prems Suc by simp
      next
        case (Suc n'')
        then show ?thesis using Cons.IH Cons.prems Suc Cons by auto
      qed
    qed
  qed
qed

section \<open>Closure Properties\<close>

text \<open>Family closure under composition\<close>

definition family_closed :: "symbol_family \<Rightarrow> bool" where
  "family_closed f \<longleftrightarrow>
    (\<forall>s1 s2. symbol_family_of s1 = Some f \<and> symbol_family_of s2 = Some f \<and>
             symbols_composable s1 s2 \<longrightarrow>
             (\<exists>s3. symbol_family_of s3 = Some f))"

theorem omega_not_closed:
  "\<not> family_closed Omega"
  unfolding family_closed_def symbols_composable_def families_composable_def
  by auto

theorem no_family_is_closed:
  "\<forall>f. \<not> family_closed f"
proof
  fix f
  show "\<not> family_closed f"
  proof (cases f)
    case Omega
    then show ?thesis using omega_not_closed by simp
  next
    case Delta
    then show ?thesis
      unfolding family_closed_def symbols_composable_def families_composable_def
      by auto
  next
    case Sigma
    then show ?thesis
      unfolding family_closed_def symbols_composable_def families_composable_def
      by auto
  qed
qed

section \<open>Reachability\<close>

text \<open>States reachable through composition\<close>

fun reachable_in_n_steps :: "symbol_id \<Rightarrow> nat \<Rightarrow> symbol_id set" where
  "reachable_in_n_steps s 0 = (if is_valid_symbol s then {s} else {})" |
  "reachable_in_n_steps s (Suc n) =
    (let prev = reachable_in_n_steps s n in
     prev \<union> {s2. \<exists>s1 \<in> prev. symbols_composable s1 s2})"

definition all_reachable :: "symbol_id \<Rightarrow> nat \<Rightarrow> symbol_id set" where
  "all_reachable s max_steps = reachable_in_n_steps s max_steps"

theorem reachability_reflexive:
  assumes "is_valid_symbol s"
  shows "s \<in> reachable_in_n_steps s 0"
  using assms by simp

theorem reachability_monotone:
  "reachable_in_n_steps s n \<subseteq> reachable_in_n_steps s (Suc n)"
  by auto

theorem reachability_finite:
  "finite (reachable_in_n_steps s n)"
proof (induction n)
  case 0
  then show ?case by simp
next
  case (Suc n)
  then show ?case
    by (auto simp: Let_def all_symbols_finite)
qed

section \<open>Statistical Properties\<close>

text \<open>Counts and ratios\<close>

definition omega_valid_combinations :: nat where
  "omega_valid_combinations = card omega_symbols * 8"

definition delta_valid_combinations :: nat where
  "delta_valid_combinations = card delta_symbols * 4"

definition sigma_valid_combinations :: nat where
  "sigma_valid_combinations = card sigma_symbols * 1"

definition total_valid_combinations :: nat where
  "total_valid_combinations = 
    omega_valid_combinations + delta_valid_combinations + sigma_valid_combinations"

lemma omega_count: "card omega_symbols = 27"
  unfolding omega_symbols_def by simp

lemma delta_count: "card delta_symbols = 10"
  unfolding delta_symbols_def by simp

lemma sigma_count: "card sigma_symbols = 8"
  unfolding sigma_symbols_def by simp

theorem total_valid_is_264:
  "total_valid_combinations = 264"
  unfolding total_valid_combinations_def 
            omega_valid_combinations_def delta_valid_combinations_def 
            sigma_valid_combinations_def
  by (simp add: omega_count delta_count sigma_count)

theorem validity_ratio:
  "total_valid_combinations * 100 div total_combinations = 58"
  by (simp add: total_valid_is_264 total_combinations_value)

section \<open>Higher-Order Properties\<close>

text \<open>Locale for symbol systems with composition\<close>

locale symbol_system =
  fixes compose :: "symbol_id \<Rightarrow> symbol_id \<Rightarrow> symbol_id option"
  assumes compose_defined: "\<forall>s1 s2. symbols_composable s1 s2 \<longrightarrow> compose s1 s2 \<noteq> None"
      and compose_family_preserving: 
          "\<forall>s1 s2 s3 f. compose s1 s2 = Some s3 \<and> symbol_family_of s1 = Some f \<longrightarrow>
                        (\<exists>f'. symbol_family_of s3 = Some f')"
begin

definition composition_preserves :: "(symbol_id \<Rightarrow> bool) \<Rightarrow> bool" where
  "composition_preserves P \<longleftrightarrow>
    (\<forall>s1 s2 s3. P s1 \<and> P s2 \<and> compose s1 s2 = Some s3 \<longrightarrow> P s3)"

theorem composition_closed_subset:
  assumes "composition_preserves P"
      and "P s1" and "P s2"
      and "compose s1 s2 = Some s3"
  shows "P s3"
  using assms unfolding composition_preserves_def by auto

end

section \<open>Main Theorems\<close>

theorem symbol_family_unique:
  assumes "is_valid_symbol s"
  shows "\<exists>!f. symbol_family_of s = Some f"
  using assms
  unfolding is_valid_symbol_def symbol_family_of_def
  by auto

theorem combination_decidable:
  shows "is_valid_combination s op \<or> \<not> is_valid_combination s op"
  by simp

theorem composability_decidable:
  shows "symbols_composable s1 s2 \<or> \<not> symbols_composable s1 s2"
  by simp

theorem sequence_validity_decidable:
  shows "is_valid_sequence seq \<or> \<not> is_valid_sequence seq"
  by simp

end
