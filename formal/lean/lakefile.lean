import Lake
open Lake DSL

package «IndusOperationalMathematics» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4"

@[default_target]
lean_lib «IndusOperationalMathematics» where
  -- add library configuration options here

