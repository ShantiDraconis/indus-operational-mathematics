/**
 * Example usage of Indus Statistical Analysis C++ library
 */

#include "indus_stats.hpp"
#include <iostream>
#include <iomanip>

using namespace indus;

int main() {
    std::cout << "======================================================================\n";
    std::cout << "INDUS SCRIPT STATISTICAL ANALYSIS - C++ IMPLEMENTATION\n";
    std::cout << "======================================================================\n";
    std::cout << "\n";
    std::cout << "IMPORTANT DISCLAIMER:\n";
    std::cout << "All 'non-locality' and 'entanglement' terminology in this software\n";
    std::cout << "refers to STATISTICAL correlations and distributed standardization,\n";
    std::cout << "NOT quantum mechanical phenomena in artifacts.\n";
    std::cout << "\n";
    std::cout << "======================================================================\n\n";
    
    // Create sample symbols
    Symbol s1{1, "numeric", "symbol_1"};
    Symbol s2{2, "pictographic", "unicorn"};
    Symbol s3{3, "abstract", "symbol_3"};
    Symbol s4{4, "numeric", "symbol_4"};
    Symbol s5{5, "pictographic", "fish"};
    
    // Create sample sequences
    std::vector<Sequence> sequences = {
        {{s1, s2, s3}, "Harappa", "seal"},
        {{s1, s2, s4}, "Harappa", "seal"},
        {{s2, s3, s1}, "Mohenjo-daro", "seal"},
        {{s1, s2, s3, s4}, "Dholavira", "tablet"},
        {{s2, s5, s3}, "Harappa", "pottery"},
        {{s1, s2, s5}, "Mohenjo-daro", "seal"}
    };
    
    std::cout << "Loaded " << sequences.size() << " sample sequences\n\n";
    
    // Create analyzer
    StatisticalAnalyzer analyzer(sequences);
    
    // Compute PMI
    std::cout << "Computing PMI (Pointwise Mutual Information):\n";
    std::cout << "---------------------------------------------\n";
    double pmi_12 = analyzer.pmi(s1, s2);
    double pmi_23 = analyzer.pmi(s2, s3);
    double pmi_13 = analyzer.pmi(s1, s3);
    
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "PMI(s1, s2) = " << pmi_12 << "\n";
    std::cout << "PMI(s2, s3) = " << pmi_23 << "\n";
    std::cout << "PMI(s1, s3) = " << pmi_13 << "\n\n";
    
    // Compute Lift
    std::cout << "Computing Lift (Odds Ratio):\n";
    std::cout << "----------------------------\n";
    double lift_12 = analyzer.lift(s1, s2);
    double lift_23 = analyzer.lift(s2, s3);
    
    std::cout << "Lift(s1, s2) = " << lift_12 << "\n";
    std::cout << "Lift(s2, s3) = " << lift_23 << "\n\n";
    
    // Compute cross-site variance (non-local invariance)
    std::cout << "Computing Cross-Site Variance (Non-Local Invariance):\n";
    std::cout << "-----------------------------------------------------\n";
    std::cout << "LOW variance = HIGH standardization across sites\n";
    std::cout << "This is STATISTICAL non-locality, not quantum!\n\n";
    
    double variance_12 = analyzer.cross_site_variance(s1, s2);
    double variance_23 = analyzer.cross_site_variance(s2, s3);
    
    std::cout << "Variance(s1, s2) = " << variance_12 << "\n";
    std::cout << "Variance(s2, s3) = " << variance_23 << "\n\n";
    
    // Positional dependencies
    std::cout << "Analyzing Positional Dependencies:\n";
    std::cout << "----------------------------------\n";
    auto dist_hist = analyzer.positional_dependency(s1, s2);
    
    std::cout << "Distance histogram for (s1, s2):\n";
    for (const auto& [dist, count] : dist_hist) {
        std::cout << "  Distance " << dist << ": ";
        for (int i = 0; i < count; ++i) std::cout << "█";
        std::cout << " (" << count << ")\n";
    }
    
    std::cout << "\n";
    std::cout << "Analysis complete.\n";
    
    return 0;
}
