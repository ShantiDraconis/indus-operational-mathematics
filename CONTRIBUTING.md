# Contributing to Indus Operational Mathematics

Thank you for your interest in contributing to this research project! This document provides guidelines for contributing to the repository.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Issues

- **Security vulnerabilities**: Please see [SECURITY.md](SECURITY.md) for responsible disclosure
- **Bugs in code**: Open an issue with detailed reproduction steps
- **Documentation errors**: Open an issue or submit a pull request
- **Theoretical questions**: Use GitHub Discussions for conceptual questions

### Suggesting Enhancements

- Check existing issues and discussions first
- Provide clear rationale and use cases
- For theoretical contributions, include mathematical justification

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the structure**:
   - Code changes go in `/code/`
   - Formal proofs in `/formal/`
   - Documentation in `/docs/` or `/public/`
   - Book chapters in `/book/`
3. **Test your changes**:
   - Python code: Run tests with `pytest`
   - C++ code: Ensure it compiles and passes tests
   - Formal proofs: Verify they compile in respective proof assistants
   - LaTeX: Ensure `main.tex` compiles without errors
4. **Document your changes**:
   - Update relevant README files
   - Add inline comments for complex logic
   - Update the book if theoretical changes are made
5. **Commit messages**: Use clear, descriptive messages
6. **Pull request description**: Explain what and why, not just how

## Development Setup

### For Python Development

```bash
cd code/
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .  # If using pyproject.toml
```

### For C++ Development

```bash
cd code/cpp/
mkdir build && cd build
cmake ..
make
```

### For Formal Verification

- **Lean 4**: Install via [elan](https://github.com/leanprover/elan)
- **Coq**: Install via [opam](https://opam.ocaml.org/)
- **Isabelle**: Download from [isabelle.in.tum.de](https://isabelle.in.tum.de/)
- **Agda**: Install via [cabal](https://www.haskell.org/cabal/)

### For LaTeX Book

```bash
cd book/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or use the CI pipeline to build automatically.

## Research Integrity

### Non-Claims

This project explicitly does NOT claim to:
- Decipher the Indus script phonetically
- Provide linguistic translations of Indus texts
- Establish historical meanings of specific symbols

### What We DO Claim

- A formal mathematical framework for analyzing symbol operations
- Comparative structural patterns with other ancient writing systems
- Computational models that can be formally verified

### Citing Sources

- All data must include provenance in `/data/provenance/`
- All claims must be backed by references in `bibliography.bib`
- Respect copyright and fair use principles

## Style Guidelines

### Python

- Follow PEP 8
- Use type hints
- Document functions with docstrings
- Maximum line length: 100 characters

### C++

- Follow modern C++ (C++17 or later)
- Use RAII principles
- Document public APIs
- Use `clang-format` with provided `.clang-format`

### LaTeX

- Use semantic commands (e.g., `\newcommand{\operator}[1]{\mathop{#1}}`)
- Keep lines under 80 characters for readability
- One sentence per line for easier diff tracking

### Formal Proofs

- Include comments explaining proof strategy
- Break complex proofs into lemmas
- Use descriptive names for theorems and definitions

## Review Process

1. **Automated checks**: CI must pass (build, tests, linting)
2. **Peer review**: At least one maintainer review required
3. **Formal verification**: If changing axioms/theorems, proofs must verify
4. **Documentation**: Updates to docs/book must be included

## Questions?

- Open a GitHub Discussion for general questions
- Join our [community chat] (if available)
- Email the maintainers for private inquiries

## License

By contributing, you agree that your contributions will be licensed under:
- CC BY 4.0 for documentation and text
- MIT License for code

Thank you for contributing to advancing our understanding of ancient symbolic systems!
