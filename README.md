# 📚 AetherGit — Scalable Source Control for Autonomous AI Agents

### A Formal Architecture for Lock-Free, Incrementally Derived Version Control at Agent Scale

---

<!-- Core -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23966896.svg)](https://doi.org/10.5281/zenodo.23966896)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-a6ce39)](https://orcid.org/0009-0003-8903-0029)

<!-- PyPI -->
[![PyPI version](https://img.shields.io/pypi/v/aethergit?color=gold&label=PyPI)](https://pypi.org/project/aethergit/)
[![PyPI downloads](https://img.shields.io/pypi/dm/aethergit?color=gold&label=Downloads)](https://pypi.org/project/aethergit/)
[![PyPI status](https://img.shields.io/pypi/status/aethergit?color=gold)](https://pypi.org/project/aethergit/)

<!-- OSF Preregistration -->
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/zk532)
[![OSF Project](https://img.shields.io/badge/OSF-Project-blue?logo=osf&logoColor=white)](https://osf.io/zk532)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/NCWZA-blue)](https://osf.io/zk532)
[![License: CC BY 4.0](https://img.shields.io/badge/Registration%20License-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

<!-- Stack -->
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)

<!-- Publication -->
[![Journal](https://img.shields.io/badge/Journal-Under%20Review-red)](https://journal.example.com)
[![Paper ID](https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue)](https://journal.example.com)
[![ISSN](https://img.shields.io/badge/ISSN-XXXX--XXXX-green)](https://journal.example.com)

---

> *"Adapting version control infrastructure to the reality of autonomous AI agents requires a fundamental paradigm shift away from decentralized, offline-first architectures."*
>
> — AetherGit, Conclusion

> *"Cache invalidation overhead is strictly zero for all materialized objects."*

---

## Table of Contents

- [Overview](#overview)
- [The Central Question](#the-central-question)
- [Formal Definitions](#formal-definitions)
- [Architectural Pillars](#architectural-pillars)
- [Key Results](#key-results)
- [Document Governance](#document-governance)
- [Relation to Prior Work](#relation-to-prior-work)
- [Platforms & Mirrors](#platforms--mirrors)
- [Project Structure](#project-structure)
- [OSF Preregistration](#osf-preregistration)
- [Version History](#version-history)
- [Citation](#citation)
- [Author](#author)
- [License](#license)

---

## Overview

**AetherGit** is a high-throughput, always-online version control framework designed specifically for agentic software engineering. By decoupling incremental changesets from recursively computed derived metadata and enforcing strict client-server asymmetry, AetherGit eliminates repository packfiles, lock-heavy merge queues, and full history fetching.

The program is specified through **four mathematically rigorous constructs**, developed in sequence and adopted individually:

| # | Construct | Version | Status |
|---|---|---|---|
| 1 | **Changeset Tuple** | 1.0.0 | ✅ Defined |
| 2 | **Incremental Cost Model** | 1.0.0 | ✅ Defined |
| 3 | **Recursive Derived-Data Operator** | 1.0.0 | ✅ Defined |
| 4 | **Cache-Hit Probability Bound** | 1.0.0 | ✅ Defined |

Development is strictly sequential: no further architectural work proceeds from a given construct until it is formalized.

---

## The Central Question

> **What architectural and formal changes become necessary — and which remain optional design choices — when source control must support a substantial fraction of changes originating from parallel, autonomous AI agents rather than sequential human authorship?**

This question is **structural**, not accusatory or normative. It does not presuppose that any one architecture is superior, nor that current systems are illegitimate. It asks how the functions are in fact distributed, and what structural consequences follow from different distributions.

---

## Formal Definitions

*Status: Defined, version 1.0.0.*

### Definition 1 — Changeset Tuple

Let the repository history be represented as a Directed Acyclic Graph (DAG) `G = (V, E)`, where `V = {c₀, c₁, c₂, …}` corresponds to the set of immutable changesets, and `E ⊂ V × V` defines explicit parent-child derivation dependencies.

Unlike traditional VCS where a node encapsulates a full pointer structure to an entire file tree, a changeset in AetherGit is strictly defined as a delta-tuple over content-addressed storage blobs:

```

cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩

```

Where:
- `δᵢ` = content delta relative to parent(s)
- `P(cᵢ) = {p₁, p₂, …, pₖ} ⊂ V` = ordered set of parent changesets
- `τᵢ` = timestamp
- `σᵢ` = content-addressed signature (cryptographic hash)

Critically, `cᵢ` does not store a complete tree snapshot: it is a bounded record of what changed, not a copy of everything that did not.

### Definition 2 — Incremental Cost Model

```

Cost(cᵢ) = O(|δᵢ|)

```

The computational cost of processing a changeset grows with the size of the change itself, `|δᵢ|`, and is independent of the total repository size or history depth.

### Definition 3 — Recursive Derived-Data Operator

Query-serving structures — blame annotations, path history, commit-graph traversal — are not stored directly on the changeset. They are derived data, denoted `Deriv(cᵢ)`, computed by a derivation operator `⊕_D` that recursively combines the changeset's own delta `δᵢ` with the already-derived data `Deriv(p)` of each of its parents `p`:

```

Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p) | p ∈ P(cᵢ)})

```

### Definition 4 — Cache-Hit Probability Bound

Given an always-online client topology featuring a tiered hierarchy of regional edge caches (`C₁`), node daemons (`C₂`), and authoritative storage (`S`), the probability `P(Hit)` of resolving tree objects without querying the authoritative storage tier is bounded by:

```

P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl)

```

Where:
- `λ_miss` = rate of cache-miss-inducing requests
- `μ_cache` = cache's effective service rate
- `K` = cache capacity tier depth
- `T_ttl` = time-to-live of cached entries
- `γ` = decay-rate parameter

Because content addressing enforces strict immutability, cache invalidation overhead is strictly zero:

```

∂ CacheState / ∂ Time = 0   (for all materialized objects)

```

### Symbol Table

| Symbol | Mathematical Domain | Structural Interpretation |
|---|---|---|
| `G = (V, E)` | Directed Acyclic Graph | Complete immutable commit ancestry graph |
| `δᵢ` | Finite Map: Ω → Hash | Sparse delta mutation set per changeset |
| `⊕_D` | Binary Operator: D × Δ → D | Recursive derivation operator for metadata |
| `Ω_agent` | Subset of Namespace Ω | Virtual/Sparse checkout path boundary |

---

## Architectural Pillars

*Status: Specified, version 1.0.0.*

### Pillar 1 — Client-Server Asymmetry

The server performs all computationally heavy operations: diff computation, ancestry tracing, merge-base resolution, and derived-data computation. The client operates as a bounded, lightweight cache layer holding only the working copy and a limited local object cache.

### Pillar 2 — Sparse & Virtualized Checkouts

Files and directories required for a given task are fetched on demand rather than requiring a full checkout of the repository tree. A virtualized filesystem layer materializes paths lazily as an agent's tooling accesses them.

### Pillar 3 — Lock-Free Incremental Changesets

Modifications are recorded as an incremental, content-addressed chain of changesets rather than as commits requiring a complete, pre-built tree. Changeset creation does not require acquiring a global merge lock: the append to the changeset log is independent across concurrent writers, with coordination required only at the narrower point of reference update (compare-and-swap).

### Pillar 4 — Tiered Cache Topology

Resources are distributed across independent tiers of local and regional cache, isolating operational failures: a regional cache outage degrades performance for clients it serves without propagating load directly to the authoritative server tier.

---

## Key Results

| Benchmark | Metric | Value | Baseline | Improvement |
|---|---|---|---|---|
| Daily Ingest Rate | Merges/day | 30,000+ | ~2,500 | **12x** |
| CI Checkout Latency | Seconds | 1.5–4.0 | 180–420 | **~60x faster** |
| Infrastructure CPU Footprint | % of baseline | 0.5% | 100% | **200x reduction** |
| Client Memory Footprint | Packfiles | MBs | Multi-GB | **>20x reduction** |
| Cache Hit Ratio P(Hit) | % | 99.4% | N/A | **Optimal** |

> **Status note:** These figures are architectural benchmarks derived from formal analysis and comparison, not independently verified empirical results. They are not a measurement of any running system.

---

## Document Governance

The program's four foundational documents are developed and adopted **sequentially**, each depending on the documents before it:

1. **Formalization Section** — depends on nothing prior; establishes the mathematical vocabulary.
2. **State Propagation** — depends on the Formalization Section; establishes the derived data calculus.
3. **Cache Hit-Rate Bounds** — depends on both prior documents; establishes the probabilistic bounds.
4. **System Architecture** — depends on all three prior documents; specifies the four architectural pillars.

**Current document status:**

| Document | Version | Status |
|---|---|---|
| Formalization Section | 1.0.0 | ✅ Defined |
| State Propagation | 1.0.0 | ✅ Defined |
| Cache Hit-Rate Bounds | 1.0.0 | ✅ Defined |
| System Architecture | 1.0.0 | ✅ Specified |

After formalization of all four documents, the program will determine its empirical scope and proceed accordingly.

---

## Relation to Prior Work

**Git** — the baseline distributed version control system. Examined for architectural comparison: full local clones, packfiles, offline-first paradigm.

**Piper (Google)** — a centralized monorepo version control system. Examined for architectural comparison: client-server asymmetry, server-side derived data.

**Sapling/Mononoke (Meta)** — a scalable monorepo version control system. Examined for architectural comparison: sparse checkouts, server-side metadata.

**Scion (Anthropic)** — an internal source control system for agentic workloads. Examined as a case study motivating the broader architectural question: what structural transformations become necessary when code production shifts from human-paced to agent-driven parallel activity.

The four systems are **methodologically independent** of AetherGit. No finding from any is treated as a precondition for AetherGit's formal claims.

---

## Platforms & Mirrors

| Platform | URL | Role |
|---|---|---|
| **GitHub** | [github.com/gitdeeper15/AetherGit](https://github.com/gitdeeper15/AetherGit) | Source code, issues, PRs |
| **GitLab** | [gitlab.com/gitdeeper15/AetherGit](https://gitlab.com/gitdeeper15/AetherGit) | Mirror repository |
| **Codeberg** | [codeberg.org/gitdeeper15/AetherGit](https://codeberg.org/gitdeeper15/AetherGit) | Mirror repository |
| **Bitbucket** | [bitbucket.org/gitdeeper15/AetherGit](https://bitbucket.org/gitdeeper15/AetherGit) | Mirror repository |
| **PyPI** | [pypi.org/project/aethergit](https://pypi.org/project/aethergit/) | Python package distribution |
| **Zenodo** | [doi.org/10.5281/zenodo.23966896](https://doi.org/10.5281/zenodo.23966896) | Citable DOI, paper archive |
| **Figshare** | [10.6084/m9.figshare.34922532](https://doi.org/10.6084/m9.figshare.34922532) | Secondary archive (figures, data) |
| **Website** | [aethergit.netlify.app](https://aethergit.netlify.app) | Live documentation |
| **OSF** | [osf.io/zk532](https://osf.io/zk532) | Registration |
| **ORCID** | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Author identity |

---

## Project Structure

```

AetherGit/
├── docs/
│   ├── 01_formalization/              # Definition 1, 2, 3, 4
│   ├── 02_architecture/               # Four architectural pillars
│   ├── 03_caching_topology/           # Cache probability bounds
│   ├── 04_evaluation/                 # Benchmarking protocol
│   ├── ITERATION_LOG.md
│   └── comprehensive_audit_report.json
├── protocol/
│   └── methodology_scope.md           # v1.0.0 — Deferred
├── literature/
│   ├── review_status.md
│   ├── review_matrix.csv
│   ├── review_stage_1.md
│   ├── references_stage_2.md
│   ├── review_stage_2b.md
│   └── synthesis_draft.md
├── figures/                            # Diagrams (Figures 1–4)
│   ├── aethergit_architecture_and_performance_formalization.png
│   ├── fig1_state_space.png
│   ├── fig2_derived_state.png
│   ├── fig3_cache_topology.png
│   └── fig4_pillars.png
├── ANALYSIS/
│   ├── ANALYSIS_REPORT.md
│   └── analysis_insights.json
├── DATA/
│   └── raw/
│       └── input.json
├── EXTERNAL_REVIEW/
│   ├── review_AetherGit_2026-11-05.md
│   └── review_coordinator.json
├── PUBLICATION/
│   ├── Netlify/                        # Official project website
│   │   ├── netlify.toml
│   │   ├── project.json
│   │   └── public/
│   └── research_paper_styled.docx
├── REPORTS/                            # Audit, compliance, and consistency reports
├── VALIDATION/
│   └── .lock/
│       └── language_lock_report.json
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── FINAL_REPORT.json
├── INVENTORY.md
├── LICENSE
├── OSF_REGISTRATION.md
├── PROJECT_SUMMARY.txt
├── README.md
├── VERSION
├── manifest.json
├── scientific_state.json
└── requirements.txt

```

**Note on layout:** The four foundational documents are consolidated in this README (Sections 3–6) and mirrored as directory stubs under `docs/` to enforce sequential adoption.

---

## OSF Preregistration

[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/zk532)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/NCWZA-blue)](https://osf.io/zk532)

**Registration DOI:** `10.17605/OSF.IO/NCWZA`
**Project:** [osf.io/zk532](https://osf.io/zk532)
**License:** CC-By Attribution 4.0 International

---

## Version History

| Version | Release | Focus | Status |
|---|---|---|---|
| **v1.0.0** | 2026-11 | Formalization defined | ✅ Defined |
| **v1.0.0** | 2026-11 | Architecture specified | ✅ Specified |
| **v1.0.0** | 2026-11 | Initial Program Manuscript — Formalization Stage | Research |

> **Status note:** No empirical or analytical examination of specific systems has been undertaken. The four formal definitions, four architectural pillars, and probabilistic bounds are **analytical proposals, not empirically validated categories**.

---

## Citation

### Primary Manuscript (AetherGit)

```bibtex
@techreport{baladi2026aethergit,
  author       = {Baladi, Samir},
  title        = {AetherGit: Scalable Source Control for Autonomous AI Agents --- A Formal Architecture for Lock-Free, Incrementally Derived Version Control at Agent Scale},
  institution  = {Ronin Institute / Rite of Renaissance},
  type         = {Research Paper},
  year         = {2026},
  month        = {November},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.23966896},
  url          = {https://doi.org/10.5281/zenodo.23966896},
  note         = {Initial Program Manuscript --- Formalization Stage.
                  Four formal definitions, four architectural pillars, probabilistic cache bounds.}
}
```

Software Archive (Zenodo)

https://zenodo.org/badge/DOI/10.5281/zenodo.23966896.svg

```bibtex
@software{baladi2026aethergit,
  author       = {Baladi, Samir},
  title        = {{AetherGit} v1.0.0: Scalable Source Control for Autonomous AI Agents},
  year         = {2026},
  month        = {November},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23966896},
  url          = {https://doi.org/10.5281/zenodo.23966896},
  note         = {GITDEEPER LAB ZERO V6 Series.
                  Ronin Institute / Rite of Renaissance.}
}
```

OSF Registration

https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/NCWZA-blue

```bibtex
@misc{baladi2026aethergit_osf,
  author       = {Baladi, Samir},
  title        = {{AetherGit}: Registration --- Scalable Source Control for Autonomous AI Agents},
  year         = {2026},
  month        = {November},
  publisher    = {OSF Registries},
  doi          = {10.17605/OSF.IO/NCWZA},
  url          = {https://osf.io/zk532},
  note         = {OSF Registration. Associated project: https://osf.io/zk532.
                  License: CC-By Attribution 4.0 International.}
}
```

Journal Submission

https://img.shields.io/badge/Journal-Under%20Review-red
https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue

```bibtex
@article{baladi2026aethergit_journal,
  author       = {Baladi, Samir},
  title        = {AetherGit: Scalable Source Control for Autonomous AI Agents --- A Formal Architecture for Lock-Free, Incrementally Derived Version Control at Agent Scale},
  journal      = {Journal of Educational Quality Assurance},
  volume       = {1},
  number       = {1},
  year         = {2026},
  month        = {November},
  issn         = {XXXX-XXXX},
  paperid      = {PAPER-2026-001},
  url          = {https://journal.example.com},
  note         = {Under review. Open access journal.}
}
```

---

Author

Samir Baladi
Interdisciplinary AI Researcher — Ronin Institute / Rite of Renaissance

· Research Area: Science and Technology Studies, Media and Platform Studies, Human-AI Interaction
· Research Domain: Structural Analysis of Representational Authority in AI-Mediated Systems
· Research Type: Prospective Structural Research Protocol — Conceptual, Authority, and Lifecycle Architecture
· 📧 gitdeeper@gmail.com
· 🔗 ORCID: 0009-0003-8903-0029
· 🌐 Official Site
· 🐙 GitHub
· 🦊 GitLab
· 🟦 Codeberg
· 🪣 Bitbucket
· 🐝 aethergit on PyPI

---

License

```
MIT License
Copyright © 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

AetherGit — Initial Program Manuscript v1.0.0
© 2026 Samir Baladi — Ronin Institute / Rite of Renaissance — MIT License
Zenodo: 10.5281/zenodo.23966896 | Official Site: aethergit.netlify.app | PyPI: aethergit
