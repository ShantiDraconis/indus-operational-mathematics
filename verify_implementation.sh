#!/bin/bash

echo "=================================================="
echo "VERIFICATION: Indus Operational Mathematics"
echo "=================================================="
echo ""

echo "1. Checking project structure..."
echo "---"
ls -la
echo ""

echo "2. Checking Python modules..."
echo "---"
ls -la src/
echo ""

echo "3. Checking documentation..."
echo "---"
ls -la docs/
echo ""

echo "4. Checking examples..."
echo "---"
ls -la examples/
echo ""

echo "5. Running basic_analysis.py..."
echo "---"
PYTHONPATH=. python examples/basic_analysis.py | head -40
echo "... [truncated for brevity]"
echo ""

echo "6. Verifying key files exist..."
echo "---"
files=(
    "README.md"
    "IMPLEMENTATION_SUMMARY.md"
    "PROJECT_STRUCTURE.md"
    "requirements.txt"
    "src/statistical_metrics.py"
    "src/indus_analysis.py"
    "src/institutional_framework.py"
    "src/grammar_framework.py"
    "docs/api_reference.md"
    "docs/research_paper_template.md"
    "docs/interpretive_frameworks.md"
    "examples/basic_analysis.py"
    "examples/site_comparison.py"
    "examples/regime_classification.py"
    "examples/grammar_validation.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file"
    else
        echo "✗ $file MISSING"
    fi
done

echo ""
echo "=================================================="
echo "VERIFICATION COMPLETE"
echo "=================================================="
