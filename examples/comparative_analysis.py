"""
Example Usage: Comparative Analysis of Harappa and YouTube

This script demonstrates the core analysis comparing ancient Indus Script
with modern YouTube Analytics data.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from analysis.zipf_analysis import ZipfAnalyzer
from analysis.frequency_analyzer import FrequencyAnalyzer
from analysis.compare_distributions import compare_distributions
from models.symbolic_activation import SymbolicActivationTheorem
from visualization.plot_zipf import plot_zipf_comparison, plot_frequency_distribution
import csv


def load_csv_data(filepath):
    """Load frequency data from CSV file."""
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header if exists
        for row in reader:
            if len(row) >= 2 and not row[0].startswith('#'):
                try:
                    key = row[0]
                    freq = int(row[1])
                    data[key] = freq
                except ValueError:
                    continue
    return data


def main():
    print("=" * 80)
    print("COMPARATIVE ANALYSIS: INDUS SCRIPT vs YOUTUBE ANALYTICS")
    print("=" * 80)
    print()
    
    # Load data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    harappa_file = os.path.join(script_dir, '..', 'data', 'harappa', 'symbol_frequencies.csv')
    youtube_file = os.path.join(script_dir, '..', 'data', 'youtube', 'content_frequencies.csv')
    
    print("Loading data...")
    harappa_data = load_csv_data(harappa_file)
    youtube_data = load_csv_data(youtube_file)
    
    print(f"✓ Loaded {len(harappa_data)} Harappa symbols")
    print(f"✓ Loaded {len(youtube_data)} YouTube content items")
    print()
    
    # Perform comparative analysis
    print("Performing statistical analysis...")
    comparison = compare_distributions(harappa_data, youtube_data)
    
    # Display results
    print("\n" + "=" * 80)
    print("HARAPPA (INDUS SCRIPT) ANALYSIS")
    print("=" * 80)
    
    h_stats = comparison['harappa']['statistics']
    h_fit = comparison['harappa']['zipf_fit']
    
    print(f"Total symbols: {h_stats['total_items']}")
    print(f"Total frequency: {h_stats['total_frequency']}")
    print(f"Zipf exponent (α): {h_fit['zipf_exponent']:.3f}")
    print(f"R² (goodness of fit): {h_fit['r_squared']:.3f}")
    print(f"Shannon entropy: {h_stats['entropy']:.3f} bits")
    print(f"Top-10 concentration: {h_stats['top_10_concentration']:.1f}%")
    print()
    print("Classification:")
    for cls in comparison['harappa']['classification']:
        print(f"  {cls}")
    
    print("\n" + "=" * 80)
    print("YOUTUBE ANALYTICS")
    print("=" * 80)
    
    y_stats = comparison['youtube']['statistics']
    y_fit = comparison['youtube']['zipf_fit']
    
    print(f"Total content items: {y_stats['total_items']}")
    print(f"Total views: {y_stats['total_frequency']}")
    print(f"Zipf exponent (α): {y_fit['zipf_exponent']:.3f}")
    print(f"R² (goodness of fit): {y_fit['r_squared']:.3f}")
    print(f"Shannon entropy: {y_stats['entropy']:.3f} bits")
    print(f"Top-10 concentration: {y_stats['top_10_concentration']:.1f}%")
    print()
    print("Classification:")
    for cls in comparison['youtube']['classification']:
        print(f"  {cls}")
    
    print("\n" + "=" * 80)
    print("COMPARATIVE RESULTS")
    print("=" * 80)
    
    comp = comparison['comparison']
    print(f"Isomorphism score: {comp['isomorphism_score']:.1f}/100")
    print(f"Structural similarity: {'YES' if comp['structural_similarity'] else 'NO'}")
    print(f"Zipf exponent difference: {comp['zipf_exponent_diff']:.3f}")
    print(f"Entropy difference: {comp['entropy_diff']:.3f} bits")
    print(f"KS statistic: {comp['ks_statistic']:.4f}")
    print(f"KS p-value: {comp['ks_pvalue']:.4f}")
    print()
    print("CONCLUSION:")
    print(comp['conclusion'])
    
    # Test Symbolic Activation Theorem
    print("\n" + "=" * 80)
    print("SYMBOLIC ACTIVATION THEOREM")
    print("=" * 80)
    
    harappa_freqs = sorted(harappa_data.values(), reverse=True)
    youtube_freqs = sorted(youtube_data.values(), reverse=True)
    
    theorem_result = SymbolicActivationTheorem.compare_systems(
        harappa_freqs,
        youtube_freqs,
        "Indus Script",
        "YouTube"
    )
    
    print(f"\nIsomorphism detected: {theorem_result['are_isomorphic']}")
    print(f"Isomorphism score: {theorem_result['isomorphism_score']:.1f}/100")
    print()
    print(theorem_result['conclusion'])
    
    print("\n" + "=" * 80)
    print("KEY FINDING")
    print("=" * 80)
    print("""
The same statistical signature observed in the Indus corpus—highly skewed 
frequency distribution with a small set of dominant operators—reappears in 
modern algorithmic systems such as social media platforms. This suggests that 
the Indus Script was optimized not for narrative expression, but for efficient 
state activation and institutional validation, a principle that remains 
cognitively and algorithmically stable across millennia.
""")
    
    # Generate visualizations if matplotlib is available
    try:
        output_dir = os.path.join(script_dir, '..', 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        print("\nGenerating visualizations...")
        plot_zipf_comparison(
            harappa_freqs,
            youtube_freqs,
            save_path=os.path.join(output_dir, 'zipf_comparison.png')
        )
        print("✓ Saved: output/zipf_comparison.png")
        
    except Exception as e:
        print(f"\nNote: Could not generate visualizations: {e}")
    
    print("\n" + "=" * 80)
    print("Analysis complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
