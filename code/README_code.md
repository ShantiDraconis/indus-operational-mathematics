# Code Directory - Indus Operational Mathematics

This directory contains all computational implementations for reproducible analysis.

## Structure

```
code/
├── python/                 # Python implementation
│   ├── operational_system.py    # Core framework
│   ├── analysis/          # Analysis modules
│   └── tests/             # Unit tests
├── cpp/                    # C++ implementation
│   ├── src/               # Source files
│   ├── include/           # Headers
│   └── CMakeLists.txt     # Build configuration
├── scripts/                # Data processing scripts
│   ├── extract_tables.py
│   ├── build_bigrams.py
│   ├── export_figures.py
│   └── validate_provenance.py
├── notebooks/              # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   └── 02_validation.ipynb
├── lib/                    # Shared utilities
│   ├── io.py
│   ├── graph.py
│   └── stats.py
├── outputs/                # Generated outputs (gitignored)
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Python project config
└── README_code.md          # This file
```

## Installation

### Python

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or install as editable package
pip install -e .
```

### C++

```bash
cd cpp/
mkdir build && cd build
cmake ..
make
```

## Usage

### Python Framework

```python
from operational_system import OperationalSystem, Symbol, SymbolClass

# Create system
sys = OperationalSystem()

# Add symbols with classes
person = Symbol(1, "人")
sys.add_symbol(person, SymbolClass.ENTITY)

# Add composition rules
# ... (see examples in operational_system.py)

# Validate sequences
sequence = [person, modifier, terminal]
is_valid, msg = sys.validate_sequence(sequence)
print(f"Valid: {is_valid}, {msg}")

# Evaluate to state
state = sys.eval(sequence)
print(f"Final state: {state}")
```

### Data Processing Scripts

```bash
# Extract tables from sources
python scripts/extract_tables.py

# Build bigram statistics
python scripts/build_bigrams.py

# Generate figures for book
python scripts/export_figures.py

# Validate data provenance
python scripts/validate_provenance.py
```

### Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

## Testing

### Python Tests

```bash
# Run all tests
pytest

# With coverage
pytest --cov=python --cov-report=html

# Specific test file
pytest python/tests/test_operational_system.py
```

### C++ Tests

```bash
cd cpp/build/
./run_tests
```

## Code Quality

### Linting

```bash
# Black (formatting)
black python/

# MyPy (type checking)
mypy python/

# Pylint (static analysis)
pylint python/
```

### CI/CD

All code quality checks run automatically via GitHub Actions.

See `.github/workflows/lint.yml` and `.github/workflows/reproducibility.yml`

## Python Modules

### operational_system.py

Core implementation of axioms A1-A5 and TCOP validation.

**Classes**:
- `SymbolClass`: Enum of semantic classes
- `Symbol`: Immutable symbol representation
- `State`: State in operational system
- `OperationalSystem`: Main system class

**Key Methods**:
- `add_symbol()`: Register symbol with class (A1)
- `add_composition_rule()`: Define composition (A2, A3)
- `compose()`: Apply composition
- `validate_sequence()`: Check axiom compliance
- `eval()`: Evaluate sequence to state

### analysis/ (Future)

- `frequency.py`: Frequency analysis
- `bigrams.py`: Bigram statistics
- `families.py`: Symbol family detection
- `entropy.py`: Entropy measures

### lib/ (Utilities)

- `io.py`: Data loading/saving
- `graph.py`: Network analysis
- `stats.py`: Statistical functions

## C++ Implementation (Planned)

### Purpose

High-performance implementation for:
- Large-scale corpus analysis
- Real-time validation
- Embedded applications

### Status

🚧 Prototype phase - Python is reference implementation

## Reproducibility

### Deterministic Outputs

All scripts produce deterministic outputs:
- Fixed random seeds
- Sorted outputs
- Documented dependencies

### Version Pinning

All dependencies pinned in `requirements.txt` and `pyproject.toml`

### Data Provenance

All generated data includes:
- Source attribution
- Generation timestamp
- Script version
- Parameters used

## Performance

### Python

- Symbol validation: ~1000 sequences/sec
- Bigram computation: ~10000 pairs/sec
- Full corpus analysis: ~1 minute

### C++ (Target)

- Symbol validation: ~100000 sequences/sec
- Bigram computation: ~1M pairs/sec
- Full corpus analysis: ~1 second

## Examples

See `notebooks/` for complete examples:

1. **01_exploration.ipynb**: Interactive exploration
2. **02_validation.ipynb**: Axiom validation examples

## Contributing

### Adding New Analysis

1. Create module in `analysis/`
2. Add tests in `tests/`
3. Update this README
4. Ensure reproducibility

### Code Standards

- **Python**: Follow PEP 8, use type hints
- **C++**: Follow Google C++ Style Guide
- **Documentation**: Docstrings for all public APIs
- **Tests**: 80%+ coverage

## License

All code: **MIT License** (see `LICENSE_CODE.md`)

## Questions?

- **Usage**: Check docstrings and notebooks
- **Bugs**: Open GitHub issue
- **Features**: GitHub Discussions

---

**Last Updated**: 2026-02-03  
**Version**: 1.0.0
