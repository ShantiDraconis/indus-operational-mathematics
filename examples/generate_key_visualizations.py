"""
Generate key visualizations for the research paper.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from analysis.compare_distributions import compare_distributions
from visualization.plot_zipf import plot_zipf_comparison, plot_entropy_comparison
import csv


def load_csv_data(filepath):
    """Load frequency data from CSV file."""
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2 and not row[0].startswith('#'):
                try:
                    data[row[0]] = int(row[1])
                except (ValueError, IndexError):
                    continue
    return data


def main():
    # Load data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    harappa_data = load_csv_data(os.path.join(script_dir, '..', 'data', 'harappa', 'symbol_frequencies.csv'))
    youtube_data = load_csv_data(os.path.join(script_dir, '..', 'data', 'youtube', 'content_frequencies.csv'))
    
    # Run comparison
    comparison = compare_distributions(harappa_data, youtube_data)
    
    # Get frequencies
    harappa_freqs = sorted(harappa_data.values(), reverse=True)
    youtube_freqs = sorted(youtube_data.values(), reverse=True)
    
    # Generate plots
    output_dir = os.path.join(script_dir, '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating Zipf comparison plot...")
    plot_zipf_comparison(
        harappa_freqs,
        youtube_freqs,
        save_path=os.path.join(output_dir, 'zipf_comparison.png'),
        title='Structural Isomorphism: Ancient Script vs Modern Algorithm'
    )
    
    print("Generating entropy comparison plot...")
    plot_entropy_comparison(
        comparison['harappa']['statistics']['entropy'],
        comparison['youtube']['statistics']['entropy'],
        save_path=os.path.join(output_dir, 'entropy_comparison.png')
    )
    
    print("\n✓ Visualizations generated successfully!")
    print(f"  - {output_dir}/zipf_comparison.png")
    print(f"  - {output_dir}/entropy_comparison.png")
    
    print("\nKey Statistics:")
    print(f"  Isomorphism Score: {comparison['comparison']['isomorphism_score']:.1f}/100")
    print(f"  Zipf Exponent Difference: {comparison['comparison']['zipf_exponent_diff']:.3f}")
    print(f"  Entropy Difference: {comparison['comparison']['entropy_diff']:.3f} bits")


if __name__ == "__main__":
    main()
