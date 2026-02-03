# Release Checklist for Indus Operational Mathematics

Use this checklist when preparing a new release.

## Pre-Release Tasks

### Version Update
- [ ] Update version in `README.md`
- [ ] Update version in `CITATION.cff`
- [ ] Update version in `code/pyproject.toml`
- [ ] Update version in `book/frontmatter/title.tex`
- [ ] Update "Last Updated" dates in all major docs

### Code Quality
- [ ] All CI/CD pipelines passing (green)
- [ ] Python: `black`, `mypy`, `pylint` pass
- [ ] No critical security vulnerabilities

### Formal Verification
- [ ] Lean 4: `lake build` succeeds
- [ ] Coq: `make all` succeeds
- [ ] Isabelle: `isabelle build -D .` succeeds
- [ ] Agda: `agda --safe` succeeds

### Documentation
- [ ] README.md up to date
- [ ] All public/* files reviewed
- [ ] Book chapters complete (or marked as draft)
- [ ] CHANGELOG.md updated

### Data & Reproducibility
- [ ] All data sources documented in `data/provenance/sources.yml`
- [ ] Reproducibility pipeline runs successfully
- [ ] Figures and tables regenerate correctly
- [ ] No proprietary or restricted data in repository

### LaTeX Book
- [ ] `pdflatex main.tex` compiles without errors
- [ ] Bibliography renders correctly
- [ ] All cross-references resolve
- [ ] Table of contents accurate
- [ ] PDF looks good (no formatting issues)

## Release Process

### 1. Create Release Branch
```bash
git checkout -b release/v1.0.0
git push origin release/v1.0.0
```

### 2. Final Testing
- [ ] Run full test suite
- [ ] Build book PDF
- [ ] Test all installation instructions
- [ ] Review all public-facing content

### 3. Tag Release
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 4. GitHub Release
- [ ] Create GitHub release for tag `v1.0.0`
- [ ] Upload compiled book PDF
- [ ] Write release notes (see template below)
- [ ] Mark as "Latest Release"

### 5. Zenodo DOI
- [ ] Trigger Zenodo archival via GitHub integration
- [ ] Wait for DOI assignment
- [ ] Update DOI in:
  - [ ] `CITATION.cff`
  - [ ] `README.md`
  - [ ] `book/frontmatter/abstract.tex`
- [ ] Commit DOI updates

### 6. Announcement
- [ ] Update GitHub Pages site
- [ ] Post announcement in GitHub Discussions
- [ ] Update any external listings (if applicable)

## Post-Release Tasks

### Documentation Updates
- [ ] Add version to docs/releases page
- [ ] Update "Current Version" badges
- [ ] Archive previous version docs (if needed)

### Community
- [ ] Respond to any release-related issues
- [ ] Thank contributors (if any)
- [ ] Update roadmap with next version goals

---

## Release Notes Template

```markdown
# Release v1.0.0 - Initial Release

## Overview

First public release of Indus Operational Mathematics framework.

## What's Included

### Core Framework
- ✅ Axioms A1-A5 formally defined
- ✅ TCOP theorem proven
- ✅ Formal verification in 4 proof assistants

### Implementations
- ✅ Python computational framework
- ✅ C++ performance implementation (partial)
- ✅ Reproducible analysis scripts

### Documentation
- ✅ Complete public-facing docs (one-pager, FAQ, glossary)
- ✅ LaTeX book (chapters 1-11)
- ✅ Formal model specifications
- ✅ GitHub Pages site

### Data
- ✅ Provenance tracking
- ✅ Derived data schemas
- ✅ Example datasets

## Known Limitations

- Book chapters 5-7 are partial drafts
- C++ implementation is prototype-level
- Full corpus analysis not yet complete

## Citation

```bibtex
@software{draconis2026indus,
  author = {Draconis, Shanti},
  title = {Indus Operational Mathematics},
  year = {2026},
  version = {1.0.0},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://github.com/ShantiDraconis/indus-operational-mathematics}
}
```

## Downloads

- **Book PDF**: [main.pdf](https://github.com/.../releases/download/v1.0.0/main.pdf)
- **Source Code**: [Source zip](https://github.com/.../archive/refs/tags/v1.0.0.zip)

## What's Next (v1.1 planned)

- Extended symbol catalog (45-200)
- Additional comparative systems (Sumerian, Egyptian)
- Machine learning integration
- Interactive web demonstrations

## Feedback Welcome

Please open issues or discussions with any questions, suggestions, or findings.

---

**Full Changelog**: https://github.com/.../compare/v0.1.0...v1.0.0
```

---

## Hotfix Checklist (for urgent fixes)

If a critical bug is found after release:

- [ ] Create hotfix branch from release tag
- [ ] Fix bug with minimal changes
- [ ] Test thoroughly
- [ ] Tag as v1.0.1 (patch version)
- [ ] Release with clear notes about what was fixed
- [ ] Merge back into main branch

---

**Last Updated**: 2026-02-03  
**Template Version**: 1.0
