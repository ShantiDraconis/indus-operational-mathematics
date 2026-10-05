# Product Release Manifest

## Product
**Indus Operational Mathematics**

Operational mathematics research framework and supporting artifacts.

## Commercial positioning
This repository is intended to be packaged as a digital research/developer product. Commercial packaging must describe what the software or formalization actually does and must not promote unverified mathematical claims as established results.

## Editions
- Personal / Research license target price: **US$49**
- Commercial / Professional license target price: **US$99**
- Launch discounts may be applied separately on Gumroad.

## Release gate
A Gumroad release is READY only when all gates below are GREEN:

- [ ] G0 OWNERSHIP — distributable code/assets identified; third-party material reviewed.
- [ ] G1 LICENSE — customer-facing license selected and included.
- [ ] G2 CLEAN — no secrets, credentials, personal evidence, or private operational data.
- [ ] G3 BUILD — clean installation/build succeeds from documented prerequisites.
- [ ] G4 TEST — smoke test or equivalent verification succeeds.
- [ ] G5 CLAIM_AUDIT — product page claims match reproducible behavior.
- [ ] G6 DOCS — README, INSTALL/QUICKSTART, and usage documentation are adequate.
- [ ] G7 EXAMPLE — buyer can reproduce at least one useful result quickly.
- [ ] G8 PACKAGE — release archive contains only distributable files.
- [ ] G9 VERSION — version/tag and CHANGELOG exist.
- [ ] G10 STOREFRONT — title, description, screenshots/demo, pricing, support statement prepared.
- [ ] G11 OPEN_MATH_DISCLOSURE — any genuinely open mathematical frontier is explicitly labeled OPEN_MATH / CONDITIONAL / EXPERIMENTAL.

## Required package layout
```
dist/
  README.md
  QUICKSTART.md
  CHANGELOG.md
  LICENSE-or-EULA.txt
  examples/
  docs/
  src-or-package/
  RELEASE_MANIFEST.json
```

## Status vocabulary
- SOURCE — source exists but is not release-verified.
- BUILD_PENDING — build not reproduced yet.
- GREEN — relevant build/test gate passed.
- FROZEN — exact verified version pinned.
- CERTIFIED — release evidence and claims audited.
- OPEN_MATH — a mathematical producer is still genuinely unresolved.
- EXPERIMENTAL — research artifact, not a production guarantee.

## Claim policy
Machine-checkable formalization, engineering infrastructure, numerical experiments, conjectural research, and genuinely solved theorems must be presented as different categories. A release must never imply that an OPEN_MATH frontier has been solved merely because surrounding infrastructure compiles.

## Gumroad package checklist
Before upload:
1. Freeze a release commit/tag.
2. Build from a clean environment.
3. Generate the distribution archive.
4. Record checksums.
5. Verify the archive contains no credentials or private data.
6. Write the storefront copy from the verified release manifest.
7. Upload only the release artifact, not the working repository history.
