"""
Zipf Distribution Plotting

Creates publication-quality visualizations of Zipf distributions
comparing ancient and modern symbolic systems.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Optional
import seaborn as sns


def plot_zipf_comparison(harappa_freqs: List[int], 
                         youtube_freqs: List[int],
                         save_path: Optional[str] = None,
                         title: str = "Zipf Distribution: Harappa vs YouTube") -> None:
    """
    Create log-log plot comparing Zipf distributions.
    
    Args:
        harappa_freqs: List of Harappa symbol frequencies (sorted descending)
        youtube_freqs: List of YouTube content frequencies (sorted descending)
        save_path: Optional path to save the figure
        title: Plot title
    """
    # Set style
    sns.set_style("whitegrid")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Harappa plot
    ranks_h = np.arange(1, len(harappa_freqs) + 1)
    ax1.loglog(ranks_h, harappa_freqs, 'o-', color='#8B4513', 
               linewidth=2, markersize=6, label='Harappa Symbols')
    ax1.set_xlabel('Rank (log scale)', fontsize=12)
    ax1.set_ylabel('Frequency (log scale)', fontsize=12)
    ax1.set_title('Indus Script Corpus', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Add reference line for ideal Zipf (slope = -1)
    ideal_zipf = harappa_freqs[0] / ranks_h
    ax1.loglog(ranks_h, ideal_zipf, '--', color='gray', 
               alpha=0.5, label='Ideal Zipf (α=1)')
    ax1.legend()
    
    # YouTube plot
    ranks_y = np.arange(1, len(youtube_freqs) + 1)
    ax2.loglog(ranks_y, youtube_freqs, 'o-', color='#FF0000', 
               linewidth=2, markersize=6, label='YouTube Content')
    ax2.set_xlabel('Rank (log scale)', fontsize=12)
    ax2.set_ylabel('Frequency (log scale)', fontsize=12)
    ax2.set_title('YouTube Analytics', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Add reference line for ideal Zipf
    ideal_zipf_y = youtube_freqs[0] / ranks_y
    ax2.loglog(ranks_y, ideal_zipf_y, '--', color='gray', 
               alpha=0.5, label='Ideal Zipf (α=1)')
    ax2.legend()
    
    plt.suptitle(title, fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_frequency_distribution(data: Dict[str, int],
                                title: str = "Frequency Distribution",
                                save_path: Optional[str] = None,
                                highlight_top_k: int = 10) -> None:
    """
    Plot frequency distribution with class annotations.
    
    Args:
        data: Dictionary of item frequencies
        title: Plot title
        save_path: Optional path to save the figure
        highlight_top_k: Number of top items to highlight
    """
    # Sort by frequency
    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    items = [item for item, _ in sorted_items[:30]]  # Show top 30
    freqs = [freq for _, freq in sorted_items[:30]]
    
    # Set style
    sns.set_style("whitegrid")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create color array (highlight top-k)
    colors = ['#FF6B6B' if i < highlight_top_k else '#4ECDC4' 
              for i in range(len(items))]
    
    # Create bar plot
    bars = ax.bar(range(len(items)), freqs, color=colors, alpha=0.8)
    
    # Customize
    ax.set_xlabel('Item Rank', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(items)))
    ax.set_xticklabels(items, rotation=45, ha='right', fontsize=8)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#FF6B6B', alpha=0.8, label=f'Class A (Top {highlight_top_k})'),
        Patch(facecolor='#4ECDC4', alpha=0.8, label='Class B/C')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_class_comparison(class_stats: Dict[str, Dict],
                         title: str = "Frequency Class Comparison",
                         save_path: Optional[str] = None) -> None:
    """
    Plot comparison of frequency classes (A, B, C).
    
    Args:
        class_stats: Dictionary with statistics for each class
        title: Plot title
        save_path: Optional path to save the figure
    """
    classes = ['Class A\n(Dominant)', 'Class B\n(Medium)', 'Class C\n(Long Tail)']
    percentages = [
        class_stats['class_a']['percentage'],
        class_stats['class_b']['percentage'],
        class_stats['class_c']['percentage']
    ]
    counts = [
        class_stats['class_a']['count'],
        class_stats['class_b']['count'],
        class_stats['class_c']['count']
    ]
    
    # Set style
    sns.set_style("whitegrid")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Pie chart for frequency percentage
    colors = ['#FF6B6B', '#4ECDC4', '#95E1D3']
    ax1.pie(percentages, labels=classes, autopct='%1.1f%%', 
            colors=colors, startangle=90)
    ax1.set_title('Frequency Distribution by Class', fontsize=12, fontweight='bold')
    
    # Bar chart for item counts
    ax2.bar(classes, counts, color=colors, alpha=0.8)
    ax2.set_ylabel('Number of Items', fontsize=12)
    ax2.set_title('Item Count by Class', fontsize=12, fontweight='bold')
    
    plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_entropy_comparison(harappa_entropy: float,
                           youtube_entropy: float,
                           save_path: Optional[str] = None) -> None:
    """
    Plot entropy comparison between systems.
    
    Lower entropy indicates higher compression efficiency.
    
    Args:
        harappa_entropy: Entropy of Harappa system
        youtube_entropy: Entropy of YouTube system
        save_path: Optional path to save the figure
    """
    systems = ['Indus Script', 'YouTube']
    entropies = [harappa_entropy, youtube_entropy]
    
    # Set style
    sns.set_style("whitegrid")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    colors = ['#8B4513', '#FF0000']
    bars = ax.bar(systems, entropies, color=colors, alpha=0.8)
    
    ax.set_ylabel('Shannon Entropy (bits)', fontsize=12)
    ax.set_title('Information Entropy Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(entropies) * 1.2)
    
    # Add value labels on bars
    for bar, entropy in zip(bars, entropies):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{entropy:.2f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()
