/**
 * Indus Script Statistical Analysis - C++ Implementation
 * 
 * High-performance implementation of core statistical measures.
 * 
 * DISCLAIMER: All "non-locality" and "entanglement" terminology refers to
 * STATISTICAL correlations, NOT quantum mechanical phenomena.
 */

#ifndef INDUS_STATS_HPP
#define INDUS_STATS_HPP

#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <numeric>

namespace indus {

/**
 * Represents a symbol in the Indus script
 */
struct Symbol {
    int id;
    std::string category;  // "numeric", "pictographic", "abstract"
    std::string name;
    
    bool operator==(const Symbol& other) const {
        return id == other.id;
    }
    
    bool operator<(const Symbol& other) const {
        return id < other.id;
    }
};

/**
 * Represents a sequence of symbols
 */
struct Sequence {
    std::vector<Symbol> symbols;
    std::string site;
    std::string artifact_type;
};

/**
 * Pair of symbols for correlation analysis
 */
struct SymbolPair {
    Symbol sym1;
    Symbol sym2;
    
    bool operator<(const SymbolPair& other) const {
        if (sym1.id != other.sym1.id) return sym1.id < other.sym1.id;
        return sym2.id < other.sym2.id;
    }
};

/**
 * Core statistical analysis class
 */
class StatisticalAnalyzer {
private:
    std::vector<Sequence> sequences_;
    std::map<Symbol, int> symbol_freq_;
    std::map<SymbolPair, int> pair_freq_;
    std::map<std::string, std::map<Symbol, int>> site_symbol_freq_;
    std::map<std::string, std::map<SymbolPair, int>> site_pair_freq_;
    int total_symbols_;
    int total_pairs_;
    
    void compute_frequencies() {
        total_symbols_ = 0;
        total_pairs_ = 0;
        
        for (const auto& seq : sequences_) {
            const auto& site = seq.site;
            const auto& symbols = seq.symbols;
            
            // Count symbols
            for (const auto& sym : symbols) {
                symbol_freq_[sym]++;
                site_symbol_freq_[site][sym]++;
                total_symbols_++;
            }
            
            // Count pairs (co-occurrences)
            for (size_t i = 0; i < symbols.size(); ++i) {
                for (size_t j = i + 1; j < symbols.size(); ++j) {
                    SymbolPair pair{
                        std::min(symbols[i], symbols[j]),
                        std::max(symbols[i], symbols[j])
                    };
                    pair_freq_[pair]++;
                    site_pair_freq_[site][pair]++;
                    total_pairs_++;
                }
            }
        }
    }

public:
    StatisticalAnalyzer(const std::vector<Sequence>& sequences)
        : sequences_(sequences), total_symbols_(0), total_pairs_(0) {
        compute_frequencies();
    }
    
    /**
     * Compute Pointwise Mutual Information (PMI)
     * 
     * This is a STATISTICAL measure of association, not quantum entanglement.
     * 
     * PMI(x,y) = log(P(x,y) / (P(x) * P(y)))
     */
    double pmi(const Symbol& sym1, const Symbol& sym2) const {
        SymbolPair pair{
            std::min(sym1, sym2),
            std::max(sym1, sym2)
        };
        
        // Joint probability P(x,y)
        auto pair_it = pair_freq_.find(pair);
        if (pair_it == pair_freq_.end() || total_pairs_ == 0) {
            return -std::numeric_limits<double>::infinity();
        }
        double p_xy = static_cast<double>(pair_it->second) / total_pairs_;
        
        // Marginal probabilities
        auto sym1_it = symbol_freq_.find(sym1);
        auto sym2_it = symbol_freq_.find(sym2);
        if (sym1_it == symbol_freq_.end() || sym2_it == symbol_freq_.end() || total_symbols_ == 0) {
            return -std::numeric_limits<double>::infinity();
        }
        
        double p_x = static_cast<double>(sym1_it->second) / total_symbols_;
        double p_y = static_cast<double>(sym2_it->second) / total_symbols_;
        
        if (p_xy == 0 || p_x == 0 || p_y == 0) {
            return -std::numeric_limits<double>::infinity();
        }
        
        return std::log2(p_xy / (p_x * p_y));
    }
    
    /**
     * Compute Lift (Odds Ratio)
     * 
     * Lift = P(x,y) / (P(x) * P(y))
     * 
     * > 1: co-occur more than expected
     * < 1: co-occur less than expected
     * = 1: independent
     */
    double lift(const Symbol& sym1, const Symbol& sym2) const {
        SymbolPair pair{
            std::min(sym1, sym2),
            std::max(sym1, sym2)
        };
        
        auto pair_it = pair_freq_.find(pair);
        if (pair_it == pair_freq_.end() || total_pairs_ == 0) {
            return 0.0;
        }
        double p_xy = static_cast<double>(pair_it->second) / total_pairs_;
        
        auto sym1_it = symbol_freq_.find(sym1);
        auto sym2_it = symbol_freq_.find(sym2);
        if (sym1_it == symbol_freq_.end() || sym2_it == symbol_freq_.end() || total_symbols_ == 0) {
            return 0.0;
        }
        
        double p_x = static_cast<double>(sym1_it->second) / total_symbols_;
        double p_y = static_cast<double>(sym2_it->second) / total_symbols_;
        
        if (p_x == 0 || p_y == 0) {
            return 0.0;
        }
        
        return p_xy / (p_x * p_y);
    }
    
    /**
     * Compute cross-site variance
     * 
     * LOW variance = HIGH standardization = "non-local invariance"
     * (STATISTICAL distributed standardization, NOT quantum non-locality)
     */
    double cross_site_variance(const Symbol& sym1, const Symbol& sym2) const {
        SymbolPair pair{
            std::min(sym1, sym2),
            std::max(sym1, sym2)
        };
        
        std::vector<double> site_pmis;
        
        for (const auto& [site, site_pair_map] : site_pair_freq_) {
            auto pair_it = site_pair_map.find(pair);
            if (pair_it == site_pair_map.end()) continue;
            
            // Compute site-specific PMI
            int site_pair_count = pair_it->second;
            int site_total_pairs = 0;
            for (const auto& [p, count] : site_pair_map) {
                site_total_pairs += count;
            }
            
            if (site_total_pairs == 0) continue;
            
            double p_xy = static_cast<double>(site_pair_count) / site_total_pairs;
            
            // Site marginals
            const auto& site_sym_map = site_symbol_freq_.at(site);
            auto sym1_it = site_sym_map.find(sym1);
            auto sym2_it = site_sym_map.find(sym2);
            
            if (sym1_it == site_sym_map.end() || sym2_it == site_sym_map.end()) continue;
            
            int site_total_symbols = 0;
            for (const auto& [s, count] : site_sym_map) {
                site_total_symbols += count;
            }
            
            if (site_total_symbols == 0) continue;
            
            double p_x = static_cast<double>(sym1_it->second) / site_total_symbols;
            double p_y = static_cast<double>(sym2_it->second) / site_total_symbols;
            
            if (p_xy > 0 && p_x > 0 && p_y > 0) {
                double site_pmi = std::log2(p_xy / (p_x * p_y));
                site_pmis.push_back(site_pmi);
            }
        }
        
        if (site_pmis.size() < 2) {
            return 0.0;
        }
        
        // Compute variance
        double mean = std::accumulate(site_pmis.begin(), site_pmis.end(), 0.0) / site_pmis.size();
        double variance = 0.0;
        for (double pmi : site_pmis) {
            variance += (pmi - mean) * (pmi - mean);
        }
        variance /= site_pmis.size();
        
        return variance;
    }
    
    /**
     * Get positional dependency histogram
     */
    std::map<int, int> positional_dependency(const Symbol& sym1, const Symbol& sym2) const {
        std::map<int, int> distance_hist;
        
        for (const auto& seq : sequences_) {
            // Find positions of each symbol
            std::vector<size_t> pos1, pos2;
            for (size_t i = 0; i < seq.symbols.size(); ++i) {
                if (seq.symbols[i] == sym1) pos1.push_back(i);
                if (seq.symbols[i] == sym2) pos2.push_back(i);
            }
            
            // Compute distances
            for (size_t p1 : pos1) {
                for (size_t p2 : pos2) {
                    int dist = std::abs(static_cast<int>(p1) - static_cast<int>(p2));
                    distance_hist[dist]++;
                }
            }
        }
        
        return distance_hist;
    }
};

} // namespace indus

#endif // INDUS_STATS_HPP
