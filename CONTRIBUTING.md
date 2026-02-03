# Contributing to Indus Operational Mathematics

Thank you for your interest in contributing to this research project!

## Types of Contributions

### Academic Discussion
- Open issues for questions about the methodology
- Suggest alternative interpretations
- Point out potential errors or inconsistencies
- Propose new analyses or comparisons

### Data Contributions
- Additional sign frequency data
- New inscription transcriptions
- Site-specific distributional data
- Corrections to existing datasets

### Code Contributions
- Improvements to Python models
- New analysis scripts
- Visualization tools
- Statistical tests

### Documentation
- Clarifications to existing text
- Additional examples
- Improved explanations
- Bibliography additions

## How to Contribute

### For Academic Discussion

1. **Open an Issue**: Use GitHub issues for questions and discussions
2. **Be Specific**: Reference specific sections, equations, or claims
3. **Provide Evidence**: Support critiques with data or citations
4. **Stay Focused**: Keep discussions on-topic and academic

### For Code/Data Contributions

1. **Fork the Repository**: Create your own fork
2. **Create a Branch**: `git checkout -b feature/your-contribution`
3. **Make Changes**: Follow existing code style and documentation standards
4. **Test Your Changes**: Ensure code runs and data is properly formatted
5. **Submit Pull Request**: Describe your changes clearly

### For Documentation Improvements

1. **Minor Fixes**: Submit pull requests directly
2. **Major Changes**: Open an issue first to discuss the approach
3. **LaTeX Style**: Follow existing formatting conventions
4. **Citations**: Use proper academic citation format

## Code Standards

### Python Code
- Follow PEP 8 style guidelines
- Include docstrings for all functions and classes
- Add type hints where appropriate
- Include example usage in docstrings
- Write unit tests for new functionality

### LaTeX
- Use consistent formatting
- Keep line length reasonable for version control
- Comment complex equations
- Use semantic macros for repeated elements

### Data Files
- CSV format preferred
- Include header row with clear column names
- Comment lines start with #
- Document data sources and methodology

## Review Process

1. **Submission**: Pull request or issue opened
2. **Initial Review**: Maintainer reviews within 1 week
3. **Discussion**: Collaborative refinement if needed
4. **Acceptance**: Merge or incorporate into project
5. **Attribution**: Contributors acknowledged in commits and/or documentation

## Academic Ethics

### Attribution
- All contributions will be attributed to contributors
- Major contributions may warrant co-authorship in publications
- Data sources must be properly cited

### Originality
- Only contribute original work or properly attributed material
- Respect copyright and licensing
- Do not plagiarize or misrepresent sources

### Peer Review
- Be respectful in critiques
- Focus on ideas, not individuals
- Acknowledge valid counterarguments
- Update positions based on evidence

## Licensing

By contributing to this repository, you agree that your contributions will be licensed under:
- **Text/Documentation**: CC BY 4.0
- **Code**: MIT License
- **Data**: CC0 1.0 (Public Domain)

## Questions?

Open an issue with the label "question" or contact the maintainer through GitHub.

## Code of Conduct

### Expected Behavior
- Professional and respectful communication
- Constructive criticism and feedback
- Focus on academic merit
- Collaborative problem-solving

### Unacceptable Behavior
- Personal attacks or ad hominem arguments
- Harassment or discrimination
- Plagiarism or academic dishonesty
- Off-topic or disruptive discussions

Violations may result in removal of contributions and blocking from the repository.

## Recognition

Contributors will be recognized in:
- Git commit history
- CONTRIBUTORS.md file (for significant contributions)
- Acknowledgments section of publications (when appropriate)
- Co-authorship on papers (for substantial intellectual contributions)

Thank you for helping advance our understanding of the Indus script!
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
