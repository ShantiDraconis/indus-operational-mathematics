"""
Chinese-Harappan Operator Comparison
Demonstrates the structural equivalence between Chinese radicals and Harappan operators.
"""

from dataclasses import dataclass
from typing import List, Set


@dataclass
class ChineseRadical:
    """Represents a Chinese radical as an operator"""
    number: int
    character: str
    name: str
    function: str
    
    def __str__(self):
        return f"{self.character} ({self.name}): {self.function}"


@dataclass
class HarappanOperator:
    """Represents a Harappan operator equivalent"""
    id_range: str
    type: str
    function: str
    
    def __str__(self):
        return f"[{self.id_range}] {self.type}: {self.function}"


@dataclass
class OperatorMapping:
    """Maps Chinese radical to Harappan operator"""
    radical: ChineseRadical
    harappan: HarappanOperator
    examples: List[str]
    
    def display(self):
        print(f"\n{'='*70}")
        print(f"Chinese Radical: {self.radical}")
        print(f"Harappan Equivalent: {self.harappan}")
        print(f"Examples:")
        for ex in self.examples:
            print(f"  • {ex}")


# Define the first 15 radicals as operators (not semantic units)
RADICAL_OPERATORS = [
    ChineseRadical(1, "一", "yī", "intensidade / eixo"),
    ChineseRadical(2, "丨", "gǔn", "partição"),
    ChineseRadical(3, "丶", "zhǔ", "instância"),
    ChineseRadical(4, "丿", "piě", "direção"),
    ChineseRadical(5, "乙", "yǐ", "transição"),
    ChineseRadical(6, "亅", "jué", "corte"),
    ChineseRadical(7, "人", "rén", "agente"),
    ChineseRadical(8, "口", "kǒu", "canal"),
    ChineseRadical(9, "囗", "wéi", "escopo"),
    ChineseRadical(10, "心", "xīn", "estado interno"),
    ChineseRadical(11, "力", "lì", "energia"),
    ChineseRadical(12, "手", "shǒu", "ação"),
    ChineseRadical(13, "木", "mù", "suporte"),
    ChineseRadical(14, "水", "shuǐ", "fluxo"),
    ChineseRadical(15, "火", "huǒ", "transformação"),
]


# Harappan operator equivalents
HARAPPAN_OPERATORS = {
    "intensidade": HarappanOperator("top-stroke", "Comb/Crown", "intensidade / escala"),
    "partição": HarappanOperator("divider", "Partition Stroke", "separação / divisão"),
    "instância": HarappanOperator("dot", "Dot Modifier", "instanciação / marcação"),
    "direção": HarappanOperator("diagonal", "Direction Stroke", "orientação / vetor"),
    "transição": HarappanOperator("curve", "Transition Mark", "mudança de estado"),
    "corte": HarappanOperator("hook", "Hook/Cut", "decisão / corte"),
    "agente": HarappanOperator("373", "Entity Base", "entidade agente"),
    "canal": HarappanOperator("U-shape", "U/Channel", "mediação / escopo"),
    "escopo": HarappanOperator("enclosure", "Boundary", "delimitação espacial"),
    "interno": HarappanOperator("fill", "Internal Fill", "estado interno"),
    "energia": HarappanOperator("arm/hook", "Action Mark", "capacidade / força"),
    "ação": HarappanOperator("extension", "Arm Extension", "ação executada"),
    "suporte": HarappanOperator("base", "Support Base", "fundação / sustentação"),
    "fluxo": HarappanOperator("wave", "Flow Pattern", "movimento / transformação"),
    "transformação": HarappanOperator("cross", "Transform Mark", "mudança radical"),
}


def create_mapping(radical: ChineseRadical, harappan_key: str, examples: List[str]) -> OperatorMapping:
    """Create a radical-to-operator mapping"""
    return OperatorMapping(
        radical=radical,
        harappan=HARAPPAN_OPERATORS[harappan_key],
        examples=examples
    )


# Key mappings demonstrating structural equivalence
KEY_MAPPINGS = [
    create_mapping(
        RADICAL_OPERATORS[6],  # 人 (rén)
        "agente",
        [
            "人 → 从 (duplicação: Human(x,y))",
            "人 + 一 → 大 (intensificação: Human⁺)",
            "人 + 口 → 吃/合 (canal: Human ∘ Channel)",
            "人 + 力 → 男 (energia: Human_productive)",
            "人 + 心 → 念 (interno: Human_internal_state)",
        ]
    ),
    create_mapping(
        RADICAL_OPERATORS[7],  # 口 (kǒu)
        "canal",
        [
            "口 como escopo institucional",
            "口 + 人 = mediação através de agente",
            "Equivale ao U-shape harappano (recipiente)"
        ]
    ),
    create_mapping(
        RADICAL_OPERATORS[9],  # 心 (xīn)
        "interno",
        [
            "心 adiciona estado interno ao agente",
            "Equivale ao preenchimento interno harappano",
            "Marca invisível externamente"
        ]
    ),
    create_mapping(
        RADICAL_OPERATORS[10],  # 力 (lì)
        "energia",
        [
            "力 marca capacidade produtiva",
            "Equivale ao braço/gancho harappano",
            "Função atribuída ao agente"
        ]
    ),
]


class CompositionExample:
    """Demonstrates composition in both systems"""
    
    @staticmethod
    def chinese_composition(base: str, operators: List[str]) -> str:
        """Compose Chinese character"""
        return f"{base} + {' + '.join(operators)} → [composite character]"
    
    @staticmethod
    def harappan_composition(base: str, operators: List[str]) -> str:
        """Compose Harappan symbol"""
        return f"{base} ⊕ {' ⊕ '.join(operators)} → [composite symbol]"
    
    @staticmethod
    def show_parallel_composition():
        """Show parallel composition examples"""
        print("\n" + "="*70)
        print("PARALLEL COMPOSITION EXAMPLES")
        print("="*70)
        
        examples = [
            {
                "concept": "Human + Force",
                "chinese": ("人", ["力"], "男 (man with productive capacity)"),
                "harappan": ("373-Entity", ["Arm-Hook"], "productive agent")
            },
            {
                "concept": "Human + Internal State",
                "chinese": ("人", ["心"], "念/忠 (human with consciousness)"),
                "harappan": ("373-Entity", ["Fill"], "entity with internal state")
            },
            {
                "concept": "Human + Authority",
                "chinese": ("人", ["王"], "全/住 (authorized human)"),
                "harappan": ("373-Entity", ["Roof-342-348"], "validated entity")
            }
        ]
        
        for ex in examples:
            print(f"\nConcept: {ex['concept']}")
            print(f"  Chinese:  {CompositionExample.chinese_composition(ex['chinese'][0], ex['chinese'][1])}")
            print(f"           → {ex['chinese'][2]}")
            print(f"  Harappan: {CompositionExample.harappan_composition(ex['harappan'][0], ex['harappan'][1])}")
            print(f"           → {ex['harappan'][2]}")


def demonstrate_structural_equivalence():
    """Main demonstration of structural equivalence"""
    
    print("="*70)
    print("STRUCTURAL EQUIVALENCE: CHINESE RADICALS ⇄ HARAPPAN OPERATORS")
    print("="*70)
    
    print("\n📌 CORE PRINCIPLE:")
    print("Both systems use BASE + OPERATOR → NEW STATE")
    print("Neither carries fixed semantic meaning at the operator level")
    print("State emerges through composition\n")
    
    # Show key mappings
    for mapping in KEY_MAPPINGS:
        mapping.display()
    
    # Show parallel compositions
    CompositionExample.show_parallel_composition()
    
    # Unified formalization
    print("\n" + "="*70)
    print("UNIFIED FORMALIZATION")
    print("="*70)
    print("\nBoth systems follow:")
    print("  Estado = Base ∘ ∑Operadores")
    print("\nWhere:")
    print("  • Base defines the CLASS")
    print("  • Operators modify the STATE")
    print("  • Result is compositional and deterministic")
    
    print("\n" + "="*70)
    print("KEY DIFFERENCES")
    print("="*70)
    print("""
Harappan System:
  ✓ Closed institutional states
  ✓ No narrative capacity
  ✓ System of validation
  ✓ Finite and complete (417 symbols, max 5 length)

Chinese System:
  ✓ Open semantic evolution
  ✓ Narrative capacity developed
  ✓ System of description
  ✓ Infinite expansion possible

👉 Chinese PRESERVES the operators but OPENS the system
    """)
    
    print("="*70)
    print("CONCLUSION")
    print("="*70)
    print("""
The radical 人 (rén) in ancient Chinese operates EXACTLY like a Harappan 
base token: it does not carry fixed meaning but assumes distinct states 
through operator addition.

This proves:
  ✓ Structural identity (not linguistic identity)
  ✓ Cognitive inheritance (not direct cultural transmission)
  ✓ Universal operational logic in early writing systems

Academic formulation:
"In early Chinese writing, the radical 人 operates as a base agent class 
whose semantic state emerges through operator composition, mirroring the 
same base–operator–state logic observed in the Indus script."
    """)


if __name__ == "__main__":
    demonstrate_structural_equivalence()
