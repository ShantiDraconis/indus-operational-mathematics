# Contributing to Harappa Operational Mathematics

Thank you for your interest in contributing to the Harappa Operational Mathematics System!

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request, please create an issue on GitHub with:
- A clear, descriptive title
- Steps to reproduce the issue (for bugs)
- Expected vs actual behavior
- Your environment (OS, Python version)

### Submitting Changes

1. **Fork the repository** and create a new branch for your feature or fix
2. **Make your changes** following the code style guidelines below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/indus-operational-mathematics.git
cd indus-operational-mathematics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest black flake8 mypy
```

## Code Style Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use descriptive variable names

```python
# Good
def create_state_machine(name: str) -> StateMachine:
    """Create a new state machine with the given name."""
    return StateMachine(name=name)

# Avoid
def csm(n):
    return StateMachine(name=n)
```

### Documentation

- All public classes and functions must have docstrings
- Use Google-style docstrings

```python
def validate_record(self, record: Record) -> bool:
    """
    Validate a complete record.
    
    Args:
        record: The record to validate
        
    Returns:
        True if valid, False otherwise
    """
```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for high test coverage

```python
def test_symbol_creation():
    """Test that symbols can be created correctly."""
    symbol = Symbol("test_id", SymbolType.ENTITY)
    assert symbol.id == "test_id"
    assert symbol.validate()
```

## Project Structure

```
indus-operational-mathematics/
├── harappa/              # Main package
│   ├── core.py          # Core components
│   ├── spec_lang.py     # Specification language
│   ├── uid.py           # UID system
│   ├── proof.py         # Proof system
│   └── applications.py  # Application modules
├── examples/            # Usage examples
├── tests/               # Test suite
├── docs/                # Documentation
└── setup.py            # Package configuration
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add state transition validation to ValidationEngine

- Implement validate_state_transition method
- Add tests for state transition validation
- Update documentation
```

## Pull Request Process

1. **Update the README** if you've added functionality
2. **Update the GUIDE** with usage examples
3. **Add tests** for new features
4. **Ensure all tests pass**
5. **Update the version** if needed (in setup.py)

Your PR will be reviewed by maintainers. We may suggest changes or improvements.

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Publishing private information
- Other unprofessional conduct

## Questions?

Feel free to open an issue with the "question" label or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
