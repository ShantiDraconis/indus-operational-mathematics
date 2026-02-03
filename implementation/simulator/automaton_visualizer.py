"""
Automaton Visualizer for Indus Script
Generates visual representations of the finite-state automaton.
"""

from typing import Dict, List, Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser.indus_automaton import State, SymbolClass


class AutomatonVisualizer:
    """Generate visualizations of the Indus automaton"""
    
    def __init__(self):
        self.states = list(State)
    
    def generate_graphviz_dot(self) -> str:
        """
        Generate Graphviz DOT format representation of the automaton.
        
        Returns:
            DOT format string
        """
        dot = []
        dot.append('digraph IndusAutomaton {')
        dot.append('    rankdir=LR;')
        dot.append('    node [shape=circle];')
        dot.append('    ')
        
        # Mark accepting state
        dot.append('    S5 [shape=doublecircle, label="S5\\nFECHADA"];')
        
        # Other states
        dot.append('    S0 [label="S0\\nINICIAL"];')
        dot.append('    S1 [label="S1\\nENTIDADE"];')
        dot.append('    S2 [label="S2\\nQUALIFICADA"];')
        dot.append('    S3 [label="S3\\nQUANTIFICADA"];')
        dot.append('    S4 [label="S4\\nRELACIONADA"];')
        dot.append('    ')
        
        # Initial state indicator
        dot.append('    start [shape=point];')
        dot.append('    start -> S0;')
        dot.append('    ')
        
        # Transitions
        transitions = [
            ('S0', 'S1', 'ENT_*'),
            ('S1', 'S2', 'OP_QUAL'),
            ('S1', 'S3', 'OP_COUNT'),
            ('S1', 'S4', 'OP_REL'),
            ('S1', 'S5', 'OP_CLOSE'),
            ('S2', 'S2', 'OP_QUAL'),
            ('S2', 'S3', 'OP_COUNT'),
            ('S2', 'S4', 'OP_REL'),
            ('S2', 'S5', 'OP_CLOSE'),
            ('S3', 'S4', 'OP_REL'),
            ('S3', 'S5', 'OP_CLOSE'),
            ('S4', 'S5', 'OP_CLOSE'),
        ]
        
        for src, dst, label in transitions:
            dot.append(f'    {src} -> {dst} [label="{label}"];')
        
        dot.append('}')
        
        return '\n'.join(dot)
    
    def generate_mermaid(self) -> str:
        """
        Generate Mermaid diagram format representation.
        
        Returns:
            Mermaid format string
        """
        mermaid = []
        mermaid.append('```mermaid')
        mermaid.append('stateDiagram-v2')
        mermaid.append('    [*] --> S0')
        mermaid.append('    ')
        
        # Transitions
        transitions = [
            ('S0', 'S1', 'ENT_*'),
            ('S1', 'S2', 'OP_QUAL'),
            ('S1', 'S3', 'OP_COUNT'),
            ('S1', 'S4', 'OP_REL'),
            ('S1', 'S5', 'OP_CLOSE'),
            ('S2', 'S2', 'OP_QUAL'),
            ('S2', 'S3', 'OP_COUNT'),
            ('S2', 'S4', 'OP_REL'),
            ('S2', 'S5', 'OP_CLOSE'),
            ('S3', 'S4', 'OP_REL'),
            ('S3', 'S5', 'OP_CLOSE'),
            ('S4', 'S5', 'OP_CLOSE'),
        ]
        
        for src, dst, label in transitions:
            mermaid.append(f'    {src} --> {dst}: {label}')
        
        mermaid.append('    ')
        mermaid.append('    S5 --> [*]')
        mermaid.append('    ')
        
        # State descriptions
        mermaid.append('    note right of S0: Initial State')
        mermaid.append('    note right of S1: Entity Defined')
        mermaid.append('    note right of S2: Qualified')
        mermaid.append('    note right of S3: Quantified')
        mermaid.append('    note right of S4: Related')
        mermaid.append('    note right of S5: Closed (Accepting)')
        
        mermaid.append('```')
        
        return '\n'.join(mermaid)
    
    def generate_ascii_art(self) -> str:
        """
        Generate ASCII art representation of the automaton.
        
        Returns:
            ASCII art string
        """
        art = []
        art.append('┌─────────────────────────────────────────────────────────────────┐')
        art.append('│           Indus Script Finite Automaton (ASCII)                 │')
        art.append('└─────────────────────────────────────────────────────────────────┘')
        art.append('')
        art.append('        ENT_*')
        art.append('   ┌─────────────┐')
        art.append('   │             v')
        art.append(' [*]──> S0       S1 ─────OP_QUAL────> S2')
        art.append('     INICIAL     │  ─────OP_COUNT───> │ │')
        art.append('                 │  ─────OP_REL─────> S3 │')
        art.append('                 │                     │  │')
        art.append('                 └────OP_CLOSE────────┴──┴──> S4 ──OP_CLOSE──> ((S5))')
        art.append('                                              │                FECHADA')
        art.append('                                              └──OP_CLOSE─────> [*]')
        art.append('')
        art.append('Legend:')
        art.append('  [*]    = Start/End')
        art.append('  S0-S4  = States')
        art.append('  ((S5)) = Accepting State')
        art.append('  ENT_*  = Any Entity Class')
        art.append('')
        
        return '\n'.join(art)
    
    def generate_transition_table(self) -> str:
        """
        Generate transition table in text format.
        
        Returns:
            Formatted transition table
        """
        table = []
        table.append('Transition Table δ(state, symbol) → new_state')
        table.append('=' * 70)
        table.append('')
        table.append('State      | ENT  | QUAL | COUNT | REL  | CLOSE ')
        table.append('-----------+------+------+-------+------+-------')
        table.append('S0 (INIT)  | S1   |  -   |   -   |  -   |   -   ')
        table.append('S1 (ENT)   |  -   | S2   |  S3   | S4   |  S5   ')
        table.append('S2 (QUAL)  |  -   | S2   |  S3   | S4   |  S5   ')
        table.append('S3 (QUANT) |  -   |  -   |   -   | S4   |  S5   ')
        table.append('S4 (REL)   |  -   |  -   |   -   |  -   |  S5   ')
        table.append('S5 (CLOSE) |  -   |  -   |   -   |  -   |   -   ')
        table.append('')
        table.append('Legend:')
        table.append('  S#   = State number')
        table.append('  -    = Invalid transition')
        table.append('  S5   = Accepting state (FECHADA/CLOSED)')
        table.append('')
        
        return '\n'.join(table)
    
    def generate_state_diagram_markdown(self) -> str:
        """
        Generate complete state diagram documentation in Markdown.
        
        Returns:
            Markdown formatted documentation
        """
        md = []
        md.append('# Indus Script Automaton State Diagram')
        md.append('')
        md.append('## Visual Representation')
        md.append('')
        md.append(self.generate_mermaid())
        md.append('')
        md.append('## ASCII Representation')
        md.append('')
        md.append('```')
        md.append(self.generate_ascii_art())
        md.append('```')
        md.append('')
        md.append('## Transition Table')
        md.append('')
        md.append('```')
        md.append(self.generate_transition_table())
        md.append('```')
        md.append('')
        md.append('## State Descriptions')
        md.append('')
        md.append('### S0: INICIAL (Initial)')
        md.append('- Entry point of the automaton')
        md.append('- Accepts: Entity symbols to transition to S1')
        md.append('- Rejects: Any non-entity symbol')
        md.append('')
        md.append('### S1: ENTIDADE DEFINIDA (Entity Defined)')
        md.append('- An entity has been recognized')
        md.append('- Accepts: Qualifiers (S2), Counts (S3), Relations (S4), Closure (S5)')
        md.append('- Most versatile state with multiple exit paths')
        md.append('')
        md.append('### S2: QUALIFICADA (Qualified)')
        md.append('- Qualification operators have been applied')
        md.append('- Accepts: More qualifiers (S2), Counts (S3), Relations (S4), Closure (S5)')
        md.append('- Allows iterative qualification')
        md.append('')
        md.append('### S3: QUANTIFICADA (Quantified)')
        md.append('- Quantity has been specified')
        md.append('- Accepts: Relations (S4), Closure (S5)')
        md.append('- Cannot return to qualification')
        md.append('')
        md.append('### S4: RELACIONADA (Related)')
        md.append('- Relations have been established')
        md.append('- Accepts: Only Closure (S5)')
        md.append('- Penultimate state before acceptance')
        md.append('')
        md.append('### S5: FECHADA (Closed) ★ ACCEPTING STATE')
        md.append('- Closure operator applied')
        md.append('- Accepting state - sequence is complete and valid')
        md.append('- No outgoing transitions (absorbing state)')
        md.append('')
        md.append('## Symbol Classes')
        md.append('')
        md.append('- **ENT_***: Entity classes (OVAL, U, HASTE, ANIMAL, METRICA)')
        md.append('- **OP_QUAL**: Qualification operators (Dot, Stroke, etc.)')
        md.append('- **OP_COUNT**: Counting operators (410-417)')
        md.append('- **OP_REL**: Relation operators (400-409)')
        md.append('- **OP_CLOSE**: Closure operators (342-348)')
        md.append('')
        
        return '\n'.join(md)


def generate_all_visualizations(output_dir: str = '.'):
    """
    Generate all visualization formats and save to files.
    
    Args:
        output_dir: Directory to save visualization files
    """
    import os
    
    visualizer = AutomatonVisualizer()
    
    # Generate and save DOT file
    dot_content = visualizer.generate_graphviz_dot()
    with open(os.path.join(output_dir, 'automaton.dot'), 'w') as f:
        f.write(dot_content)
    print(f"Generated: {output_dir}/automaton.dot")
    
    # Generate and save Markdown with Mermaid
    md_content = visualizer.generate_state_diagram_markdown()
    with open(os.path.join(output_dir, 'automaton_diagram.md'), 'w') as f:
        f.write(md_content)
    print(f"Generated: {output_dir}/automaton_diagram.md")
    
    # Generate and save transition table
    table_content = visualizer.generate_transition_table()
    with open(os.path.join(output_dir, 'transition_table.txt'), 'w') as f:
        f.write(table_content)
    print(f"Generated: {output_dir}/transition_table.txt")
    
    print("\nVisualization files generated successfully!")


if __name__ == "__main__":
    print("Indus Automaton Visualizer")
    print("=" * 50)
    print()
    
    visualizer = AutomatonVisualizer()
    
    # Display ASCII art
    print(visualizer.generate_ascii_art())
    print()
    
    # Display transition table
    print(visualizer.generate_transition_table())
    print()
    
    # Generate all visualization files
    print("Generating visualization files...")
    generate_all_visualizations('.')
