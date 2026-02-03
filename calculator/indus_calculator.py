"""
Interactive Calculator for Indus Script Analysis

This provides a user-friendly interface for computing statistical measures
on Indus script data.
"""

import sys
from typing import List, Optional
from dataclasses import dataclass
from indus_analysis import Symbol, Sequence, IndusStatisticalAnalysis


class IndusCalculator:
    """Interactive calculator for Indus script analysis"""
    
    def __init__(self):
        self.sequences: List[Sequence] = []
        self.analyzer: Optional[IndusStatisticalAnalysis] = None
        print("=" * 70)
        print("INDUS SCRIPT STATISTICAL ANALYSIS CALCULATOR")
        print("=" * 70)
        print()
        print("IMPORTANT DISCLAIMER:")
        print("All 'non-locality' and 'entanglement' terminology in this tool")
        print("refers to STATISTICAL correlations and distributed standardization,")
        print("NOT quantum mechanical phenomena in artifacts.")
        print()
        print("=" * 70)
        print()
    
    def load_sample_data(self):
        """Load sample data for demonstration"""
        # Create sample symbols
        s1 = Symbol(1, 'numeric', 'symbol_1')
        s2 = Symbol(2, 'pictographic', 'unicorn')
        s3 = Symbol(3, 'abstract', 'symbol_3')
        s4 = Symbol(4, 'numeric', 'symbol_4')
        s5 = Symbol(5, 'pictographic', 'fish')
        
        # Create sample sequences from different sites
        self.sequences = [
            Sequence([s1, s2, s3], 'Harappa', 'seal'),
            Sequence([s1, s2, s4], 'Harappa', 'seal'),
            Sequence([s2, s3, s1], 'Mohenjo-daro', 'seal'),
            Sequence([s1, s2, s3, s4], 'Dholavira', 'tablet'),
            Sequence([s2, s5, s3], 'Harappa', 'pottery'),
            Sequence([s1, s2, s5], 'Mohenjo-daro', 'seal'),
        ]
        
        self.analyzer = IndusStatisticalAnalysis(self.sequences)
        print(f"✓ Loaded {len(self.sequences)} sample sequences")
        print()
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 70)
        print("MAIN MENU")
        print("=" * 70)
        print("1. Compute PMI (Pointwise Mutual Information)")
        print("2. Compute Mutual Information")
        print("3. Compute Lift (Odds Ratio)")
        print("4. Analyze Positional Dependencies")
        print("5. Run Permutation Test")
        print("6. Compute Cross-Site Variance (Non-Local Invariance)")
        print("7. Find Stable Clusters")
        print("8. Show Top Correlations")
        print("9. Classify Sequence (Administrative vs Ritual)")
        print("0. Exit")
        print("=" * 70)
    
    def run(self):
        """Main calculator loop"""
        self.load_sample_data()
        
        while True:
            self.show_menu()
            choice = input("\nEnter choice (0-9): ").strip()
            print()
            
            if choice == '0':
                print("Exiting calculator. Goodbye!")
                break
            elif choice == '1':
                self.compute_pmi()
            elif choice == '2':
                self.compute_mi()
            elif choice == '3':
                self.compute_lift()
            elif choice == '4':
                self.analyze_positions()
            elif choice == '5':
                self.run_permutation_test()
            elif choice == '6':
                self.compute_variance()
            elif choice == '7':
                self.find_clusters()
            elif choice == '8':
                self.show_top_correlations()
            elif choice == '9':
                self.classify_sequence()
            else:
                print("Invalid choice. Please try again.")
    
    def compute_pmi(self):
        """Compute PMI for a symbol pair"""
        print("COMPUTE PMI (Pointwise Mutual Information)")
        print("-" * 70)
        print("PMI measures association strength between two symbols.")
        print("Positive values = symbols co-occur more than expected by chance")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        # Find symbols
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            pmi = self.analyzer.pmi(sym1, sym2)
            print()
            print(f"Result: PMI({sym1_id}, {sym2_id}) = {pmi:.4f}")
            if pmi > 1:
                print("→ Strong positive association")
            elif pmi > 0:
                print("→ Weak positive association")
            elif pmi < -1:
                print("→ Strong negative association (avoid each other)")
            else:
                print("→ Weak or no association")
        else:
            print("Error: Symbol not found")
    
    def compute_mi(self):
        """Compute Mutual Information"""
        print("COMPUTE MUTUAL INFORMATION")
        print("-" * 70)
        print("MI measures total correlation strength between symbols.")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            mi = self.analyzer.mutual_information(sym1, sym2)
            print()
            print(f"Result: MI({sym1_id}, {sym2_id}) = {mi:.4f} bits")
        else:
            print("Error: Symbol not found")
    
    def compute_lift(self):
        """Compute Lift"""
        print("COMPUTE LIFT (Odds Ratio)")
        print("-" * 70)
        print("Lift > 1: symbols co-occur more than expected")
        print("Lift < 1: symbols co-occur less than expected")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            lift = self.analyzer.lift(sym1, sym2)
            print()
            print(f"Result: Lift({sym1_id}, {sym2_id}) = {lift:.4f}")
        else:
            print("Error: Symbol not found")
    
    def analyze_positions(self):
        """Analyze positional dependencies"""
        print("ANALYZE POSITIONAL DEPENDENCIES")
        print("-" * 70)
        print("Shows preferred distances between symbol pairs.")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            dist_hist = self.analyzer.positional_dependency(sym1, sym2)
            print()
            print("Distance histogram:")
            for dist, count in sorted(dist_hist.items()):
                print(f"  Distance {dist}: {'█' * count} ({count})")
        else:
            print("Error: Symbol not found")
    
    def run_permutation_test(self):
        """Run permutation test"""
        print("PERMUTATION TEST")
        print("-" * 70)
        print("Tests if co-occurrence is statistically significant.")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            print("Running 1000 permutations...")
            p_value = self.analyzer.permutation_test(sym1, sym2, n_permutations=1000)
            print()
            print(f"Result: p-value = {p_value:.4f}")
            if p_value < 0.05:
                print("→ SIGNIFICANT: Co-occurrence is unlikely due to chance")
            else:
                print("→ Not significant: Could be random")
        else:
            print("Error: Symbol not found")
    
    def compute_variance(self):
        """Compute cross-site variance"""
        print("CROSS-SITE VARIANCE (Non-Local Invariance)")
        print("-" * 70)
        print("LOW variance = HIGH standardization across sites")
        print("This is STATISTICAL non-locality, not quantum!")
        print()
        
        sym1_id = int(input("Enter first symbol ID (1-5): "))
        sym2_id = int(input("Enter second symbol ID (1-5): "))
        
        all_symbols = list(self.analyzer.symbol_freq.keys())
        sym1 = next((s for s in all_symbols if s.id == sym1_id), None)
        sym2 = next((s for s in all_symbols if s.id == sym2_id), None)
        
        if sym1 and sym2:
            variance = self.analyzer.cross_site_variance(sym1, sym2)
            print()
            print(f"Result: Cross-site variance = {variance:.4f}")
            if variance < 0.5:
                print("→ LOW variance: Pattern is stable across sites (non-local invariant)")
            else:
                print("→ HIGH variance: Pattern varies significantly by site")
        else:
            print("Error: Symbol not found")
    
    def find_clusters(self):
        """Find stable clusters"""
        print("FIND STABLE CLUSTERS")
        print("-" * 70)
        print("Finding symbol pairs with high PMI and low cross-site variance.")
        print("These are 'entangled' in the STATISTICAL sense only!")
        print()
        
        clusters = self.analyzer.find_stable_clusters(min_pmi=0.5, max_variance=1.0)
        
        if clusters:
            print(f"Found {len(clusters)} stable clusters:")
            print()
            for i, (s1, s2, pmi, var) in enumerate(clusters[:10], 1):
                print(f"{i}. Symbols ({s1.id}, {s2.id}): PMI={pmi:.2f}, Variance={var:.2f}")
        else:
            print("No stable clusters found with current thresholds.")
    
    def show_top_correlations(self):
        """Show top correlations"""
        print("TOP CORRELATIONS")
        print("-" * 70)
        
        from indus_analysis import compute_top_correlations
        results = compute_top_correlations(self.sequences, top_n=10)
        
        print()
        for i, result in enumerate(results, 1):
            print(f"{i}. Symbols ({result['symbol1']}, {result['symbol2']}):")
            print(f"   PMI: {result['pmi']:.4f}")
            print(f"   MI: {result['mutual_information']:.4f}")
            print(f"   Lift: {result['lift']:.4f}")
            print(f"   Variance: {result['cross_site_variance']:.4f}")
            print(f"   Stable: {'Yes' if result['is_stable_cluster'] else 'No'}")
            print()
    
    def classify_sequence(self):
        """Classify a sequence"""
        print("CLASSIFY SEQUENCE")
        print("-" * 70)
        print("Classify as administrative vs ritual based on features.")
        print()
        
        seq_idx = int(input(f"Enter sequence index (1-{len(self.sequences)}): ")) - 1
        
        if 0 <= seq_idx < len(self.sequences):
            seq = self.sequences[seq_idx]
            result = self.analyzer.institutional_vs_ritual_classification(seq)
            
            print()
            print(f"Sequence: {[s.id for s in seq.symbols]}")
            print(f"Site: {seq.site}")
            print(f"Type: {seq.artifact_type}")
            print()
            print(f"Administrative probability: {result['administrative']:.2%}")
            print(f"Ritual probability: {result['ritual']:.2%}")
        else:
            print("Error: Invalid sequence index")


def main():
    """Main entry point"""
    calculator = IndusCalculator()
    calculator.run()


if __name__ == '__main__':
    main()
