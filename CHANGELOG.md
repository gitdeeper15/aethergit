# AetherGit — Changelog

All notable changes to this research project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-11-05

### Initial Program Manuscript

First public release of **AetherGit: Scalable Source Control for Autonomous AI Agents**.

This is a research paper with a formal framework. No empirical findings are reported.

### Added — Research Manuscript

- `PUBLICATION/research_paper_styled.docx` — full manuscript.
- Four formal definitions:
  - Definition 1: Changeset Tuple (cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩).
  - Definition 2: Incremental Cost Model (Cost(cᵢ) = O(|δᵢ|)).
  - Definition 3: Recursive Derived-Data Operator (Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p)})).
  - Definition 4: Cache-Hit Probability Bound (P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl)).
- Four architectural pillars:
  - Client-Server Asymmetry.
  - Sparse & Virtualized Checkouts.
  - Lock-Free Changesets.
  - Tiered Cache Topology.

### Added — Central Question

- What architectural and formal changes become necessary — and which remain optional design choices — when source control must support a substantial fraction of changes originating from parallel, autonomous AI agents rather than sequential human authorship?

### Added — Formal Constructs

- **Changeset Tuple** (v1.0.0) — `cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩`.
- **Incremental Cost Model** (v1.0.0) — `Cost(cᵢ) = O(|δᵢ|)`.
- **Recursive Derived-Data Operator** (v1.0.0) — `Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p) | p ∈ P(cᵢ)})`.
- **Cache-Hit Probability Bound** (v1.0.0) — `P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl)`.

### Added — Methodological Commitments

1. Function ≠ Owner — functions are analytical, owners are empirical.
2. Incremental changesets ≠ full file trees.
3. Derived data is computed server-side, not client-side.
4. Content addressing enforces strict immutability (no cache invalidation).
5. The canonical path is a reference point, not a norm.

### Added — Open Research Questions

- OQ1: What is the latency cost of on-demand derived-data computation under high concurrent load?
- OQ2: What is the scope of "functional decentralization" in practice?

### Added — Documentation

- `README.md` — full project overview (with badges, formal definitions, architecture).
- `AUTHORS.md` — author and contributor record.
- `CITATION.cff` — citation metadata with Zenodo DOI.
- `CHANGELOG.md` — this file.
- `CONTRIBUTING.md` — contribution guidelines.
- `LICENSE` — MIT.
- `INVENTORY.md` — complete inventory.

### Added — Project Infrastructure

- `VERSION` — `1.0.0`.
- `requirements.txt` — Python dependencies.
- `setup.cfg` — project metadata.
- `setup.py` — installation script.
- `manifest.json` — project manifest.
- `scientific_state.json` — scientific state record.
- `docs/` — formalization, architecture, caching topology, evaluation.
- `protocol/` — methodological scope placeholder.
- `literature/` — literature review placeholder.
- `figures/` — diagrams.

### Status

| Dimension | Status |
|-----------|--------|
| Manuscript | Complete (DOCX) |
| Formal Definitions | 4 |
| Architectural Pillars | 4 |
| Performance Theorems | 2 (O(\|Δ\|), P(Hit) ≥ 1−ε) |
| Research Questions | 2 (OQ1, OQ2) |
| Empirical Evaluation | Not executed |
| Causal claims | None (formal analysis) |

---

**Last Updated:** 2026-11-05
**Current Version:** 1.0.0
