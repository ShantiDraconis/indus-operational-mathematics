# Security Policy

## Supported Versions

We are currently in initial release phase. Security updates will be provided for:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security seriously, even for research projects. If you discover a security vulnerability, please follow these steps:

### What Constitutes a Security Issue?

Given the nature of this research project, security concerns include:

1. **Code vulnerabilities**:
   - Buffer overflows or memory safety issues in C++ code
   - Code injection vulnerabilities in Python scripts
   - Path traversal or file system access issues
   - Dependency vulnerabilities with known CVEs

2. **Data integrity issues**:
   - Issues that could corrupt or falsify research data
   - Problems with provenance tracking
   - Reproducibility failures that could affect research validity

3. **Formal verification issues**:
   - Soundness bugs in proof assistant code
   - Axiom inconsistencies that could prove false theorems
   - Issues that compromise mathematical rigor

4. **Infrastructure security**:
   - CI/CD pipeline vulnerabilities
   - Secrets exposure in workflows
   - Unauthorized access to build artifacts

### How to Report

**Please DO NOT open a public issue for security vulnerabilities.**

Instead:

1. **Email**: Send details to [security email - to be added]
2. **Subject**: "[SECURITY] Brief description"
3. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 1 week
- **Fix timeline**: Depends on severity
  - Critical: 1-7 days
  - High: 1-2 weeks
  - Medium: 2-4 weeks
  - Low: Next release cycle

### Disclosure Policy

- We follow **responsible disclosure**
- We will credit researchers who report issues (unless they prefer anonymity)
- We will coordinate disclosure timing with reporters
- We will publish a security advisory once fixed

## Research Integrity as Security

For this academic project, we also consider **research integrity** as a security concern:

### Threats to Research Integrity

1. **Data provenance**:
   - Unattributed sources
   - Unclear data lineage
   - Missing copyright information

2. **Reproducibility**:
   - Non-deterministic builds
   - Missing dependencies
   - Undocumented manual steps

3. **Overclaiming**:
   - Claims beyond what the mathematics supports
   - Misleading presentation of results
   - Phonetic decipherment claims (which we explicitly avoid)

### Reporting Integrity Issues

If you notice issues that could compromise research integrity:

1. Open a regular GitHub issue (not security-sensitive)
2. Tag with `research-integrity` label
3. Provide specific examples and references

## Dependency Management

We actively monitor dependencies for security issues:

### Python Dependencies

```bash
# Check for vulnerabilities
pip install safety
safety check

# Update dependencies
pip-audit
```

### C++ Dependencies

- Use CMake's `FetchContent` for dependency management
- Pin specific versions
- Monitor GitHub Security Advisories

### Proof Assistant Libraries

- Use stable releases
- Document exact versions in `lean-toolchain`, `_CoqProject`, etc.
- Test against multiple versions when possible

## Build Security

### CI/CD Security

- All workflows use pinned action versions
- Secrets are stored securely
- Pull requests from forks have limited permissions
- Build artifacts are signed

### Verification Pipeline

- Formal proofs are checked in isolated environments
- LaTeX compilation runs in sandboxed containers
- No arbitrary code execution in build process

## Acknowledgments

We thank the security research community for helping keep this project secure and maintaining the integrity of our research.

---

*Last updated: 2026-02-03*
