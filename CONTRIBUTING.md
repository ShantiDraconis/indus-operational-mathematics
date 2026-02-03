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
# Contributing to Quantum Archaeology Framework

Thank you for your interest in contributing to the Quantum Archaeology Framework for Indus Script Analysis! This project bridges archaeology, quantum physics, consciousness studies, and computer science in a unique interdisciplinary endeavor.

## 🌟 Ways to Contribute

### 1. Code Contributions

- **Algorithm Development**: Improve or add new quantum-inspired analysis methods
- **Visualization Tools**: Create better ways to visualize symbol networks and correlations
- **Performance Optimization**: Optimize computational efficiency
- **Testing**: Add unit tests and integration tests
- **Documentation**: Improve code documentation and examples

### 2. Data Contributions

- **Symbol Databases**: Contribute verified Indus script symbol data
- **Archaeological Context**: Add location and context information
- **Cross-Cultural Comparisons**: Contribute comparative symbol data from other cultures
- **Experimental Data**: Share results from consciousness experiments

### 3. Research Contributions

- **Theoretical Frameworks**: Propose new theoretical models
- **Experimental Designs**: Design and conduct experiments
- **Literature Reviews**: Contribute comprehensive reviews
- **Methodological Critiques**: Provide constructive criticism

### 4. Community Building

- **Educational Materials**: Create tutorials, workshops, presentations
- **Outreach**: Connect with descendant communities and indigenous knowledge keepers
- **Collaboration**: Facilitate interdisciplinary partnerships
- **Translation**: Translate documentation to other languages

## 🔬 Areas of Expertise Welcome

We welcome contributors with backgrounds in:

- **Archaeology & Ancient History**: Harappan civilization, ancient scripts
- **Physics**: Quantum mechanics, information theory
- **Computer Science**: AI/ML, data visualization, algorithms
- **Neuroscience**: Consciousness studies, brain imaging, cognitive science
- **Mathematics**: Graph theory, information theory, statistics
- **Linguistics**: Undeciphered scripts, comparative linguistics
- **Philosophy**: Consciousness, epistemology, philosophy of science
- **Indigenous Knowledge**: Traditional symbolic systems, oral histories

## 📋 Development Process

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/ShantiDraconis/indus-operational-mathematics.git
   cd indus-operational-mathematics
   ```

2. **Set Up Environment**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Examples**
   ```bash
   python examples/quantum_symbol_analysis.py
   python examples/consciousness_interface_demo.py
   ```

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write Code**
   - Follow existing code style
   - Add docstrings to functions and classes
   - Include type hints where appropriate
   - Comment complex algorithms

3. **Test Your Changes**
   - Run existing examples to ensure nothing breaks
   - Add new examples if introducing new features
   - Verify results are scientifically sound

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

### Code Style Guidelines

**Python Code:**
- Follow PEP 8 style guide
- Use descriptive variable names
- Maximum line length: 100 characters
- Use docstrings (Google or NumPy style)

**Documentation:**
- Use clear, accessible language
- Provide examples for complex concepts
- Link to academic sources where relevant
- Acknowledge uncertainty and limitations

## 🧪 Experimental Research Guidelines

### For Consciousness Studies

**Ethics First:**
- Obtain proper institutional approval (IRB/ethics board)
- Ensure informed consent
- Screen participants appropriately
- Provide integration support
- Protect participant privacy

**Scientific Rigor:**
- Pre-register studies when possible
- Use control groups
- Document methodology thoroughly
- Share raw data (with privacy protections)
- Report null results

### For Archaeological Analysis

**Cultural Sensitivity:**
- Consult with descendant communities
- Respect sacred knowledge
- Acknowledge source cultures
- Share benefits with origin regions
- Avoid extractive practices

**Academic Standards:**
- Cite sources properly
- Acknowledge uncertainties
- Distinguish hypothesis from evidence
- Use peer review
- Make data accessible

## 🤝 Collaboration Protocols

### Interdisciplinary Communication

- **Explain Jargon**: Define technical terms from your field
- **Bridge Concepts**: Help translate ideas across disciplines
- **Respect Expertise**: Value different forms of knowledge
- **Ask Questions**: No question is too basic
- **Be Patient**: Cross-disciplinary work takes time

### Conflict Resolution

- **Assume Good Faith**: Presume contributors have positive intentions
- **Discuss Ideas, Not People**: Focus on concepts, not personalities
- **Seek Understanding**: Try to see other perspectives
- **Find Common Ground**: Look for shared goals
- **Escalate if Needed**: Contact maintainers for serious issues

## 📚 Resources for Contributors

### Quantum Physics & Information Theory
- Nielsen & Chuang: "Quantum Computation and Quantum Information"
- Cover & Thomas: "Elements of Information Theory"

### Indus Valley Civilization
- Possehl: "The Indus Civilization: A Contemporary Perspective"
- Kenoyer: "Ancient Cities of the Indus Valley Civilization"
- HARP Database: harappa.com

### Consciousness Studies
- Thompson: "Waking, Dreaming, Being"
- Lutz et al.: "Attention regulation and monitoring in meditation"
- Velmans & Schneider: "The Blackwell Companion to Consciousness"

### Undeciphered Scripts
- Robinson: "Lost Languages: The Enigma of the World's Undeciphered Scripts"
- Chadwick: "The Decipherment of Linear B"

## 🎯 Priority Areas

Current priority areas for contribution:

1. **Symbol Database Expansion**: Add more verified Indus symbols
2. **Validation Framework**: Test methods on deciphered scripts
3. **Visualization Tools**: Interactive network visualizations
4. **Performance Optimization**: Handle larger corpora efficiently
5. **Experimental Protocols**: Design consciousness studies
6. **Documentation**: Tutorials for different audiences
7. **Community Outreach**: Connect with relevant communities

## ⚖️ Legal and Ethical Considerations

### Licensing
- All contributions must be compatible with project license
- Ensure you have rights to contributed data/code
- Acknowledge sources appropriately

### Data Privacy
- Do not include personal information without consent
- Anonymize experimental data
- Respect cultural intellectual property

### Academic Integrity
- No plagiarism
- Proper attribution
- Transparent about limitations
- Report conflicts of interest

## 📞 Contact

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Email**: [Maintainer contact info]

## 🙏 Acknowledgments

We thank all contributors who help bridge ancient wisdom and modern science. Every contribution, large or small, helps advance our understanding of these fascinating ancient symbols and the nature of consciousness and information itself.

---

*"In the beginner's mind there are many possibilities, but in the expert's there are few." - Shunryu Suzuki*

Together, we approach the Indus script with both scientific rigor and beginner's mind, open to unexpected insights and profound connections.
