# AetherGit: Scalable Source Control for Autonomous AI Agents

---

**Registration DOI:** [10.17605/OSF.IO/NCWZA](https://doi.org/10.17605/OSF.IO/NCWZA)
**Registration Type:** OSF Preregistration
**Registry:** OSF Registries
**Date Created:** Nov 5, 2026, 7:57 AM
**Date Registered:** Nov 5, 2026, 7:57 AM
**Associated Project:** [https://osf.io/zk532](https://osf.io/zk532)
**License:** CC-By Attribution 4.0 International
**Contributor:** Samir Baladi

---

## Data / Analytic Code / Materials / Papers / Supplements

The following files were attached to this registration:

- `README.md`
- `AetherGit_Research_Paper.pdf`
- `Formalization Section.pdf`

---

## Overview

### Research questions or hypotheses

This is a formal architecture paper. No empirical hypotheses are tested. The paper formalizes four definitions and derives two structural claims.

The central research question is:

What architectural and formal changes become necessary — and which remain optional design choices — when source control must support a substantial fraction of changes originating from parallel, autonomous AI agents rather than sequential human authorship?

The paper decomposes this question into four formal claims, each stated as a definition or theorem:

1. Changeset Tuple (Definition 1): A changeset cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩ is a bounded delta over content-addressed blobs, not a full tree snapshot.

2. Incremental Cost Model (Definition 2): Cost(cᵢ) = O(|δᵢ|). Per-change cost grows with the size of the change, not the size of the repository.

3. Recursive Derived-Data Operator (Definition 3): Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p)}). Query-serving structures (blame, path history) are computed server-side recursively, not stored on the client.

4. Cache-Hit Probability Bound (Definition 4): P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl). A probabilistic lower bound on cache-hit rate under steady-state load.

These are formal structural claims, not empirical hypotheses. No hypothesis is tested in this paper. The paper does not report an implementation, a benchmark, or empirically measured performance.

### Foreknowledge of data or evidence

Data does not yet exist. No part of the data that will be used for this analysis plan exists, and no part will be generated until after this plan is registered.

### Explanation of foreknowledge and managing unintended influences

Not applicable. No data has been collected, observed, or generated. This is a formal architecture paper, not an empirical study.

The paper does not report:
- An implementation of AetherGit.
- A benchmark of AetherGit.
- Empirically measured performance figures.

The illustrative worked example in Section 6 applies the cache-hit bound under stated hypothetical parameters (ρ = 0.6, γ = 0.15). It is explicitly labeled as an illustration, not a measurement. It is not a simulation of any real deployment.

All operational figures cited for Git and Scion throughout the paper are drawn from the cited published sources, not independently measured by this author.

No pilot analysis has been conducted. No data will be generated until after registration.

---

## Research Design

### Study type

Other: Formal architecture paper. The paper specifies a source-control architecture (AetherGit) built on four pillars and formalizes four definitions with two structural theorems. No empirical data is collected, no experiment is run, and no simulation is performed.

### Intention for causal interpretation

No causal relationship inferred: This study is not intended to inform a causal relationship.

### Blinding of experimental treatments

No blinding is involved.

### Additional blinding during research or analysis

Not applicable. No experimental treatments, no human subjects, no blinding procedures.

### Study design

This is a formal architecture paper. The study design is conceptual and mathematical, not empirical.

Structure:

1. Architecture specification (Section 4): Four pillars are specified —
   (a) Client-Server Asymmetry,
   (b) Sparse and Virtualized Checkouts,
   (c) Lock-Free Incremental Changesets,
   (d) Tiered Cache Topology.

2. Formal specification (Section 5): Four definitions are stated —
   (a) Changeset Tuple: cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩
   (b) Incremental Cost Model: Cost(cᵢ) = O(|δᵢ|)
   (c) Recursive Derived-Data Operator: Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p)})
   (d) Cache-Hit Probability Bound: P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl)

3. Illustrative worked example (Section 6): The cache-hit bound is applied under stated hypothetical parameters (ρ = 0.6, γ = 0.15). This is an illustration of the formula, not a benchmark or simulation of a real system.

4. Comparative positioning (Section 7): AetherGit's specified properties are positioned against Git's documented design and Scion's publicly disclosed architecture.

No randomization. No experimental manipulation. No human subjects. No data collection. No implementation. No benchmark.

Units of analysis:
- Formal definition (primary unit).
- Architectural pillar (secondary unit).
- Structural theorem (tertiary unit).

No between-subject or within-subject design. No counterbalancing.

### Randomization

No data

---

## Sampling

### Data collection procedures

This is a formal architecture paper. No new data is collected. No human subjects are involved. No recruiting occurs.

Data sources are published documents only:

1. Anthropic. (2026). Redesigning Source Control at Anthropic. Anthropic Research. https://www.anthropic.com/research/redesigning-source-control — the sole source for all Scion-specific architectural claims.

2. Baladi, S. (2026a). Rethinking Source Control for Agentic Software Engineering. Zenodo. https://doi.org/10.5281/zenodo.23934465 — the author's own directly preceding paper.

3. Corbett, J. C., Dean, J., Epstein, M., et al. (2013). Spanner: Google's Globally-Distributed Database. ACM TOCS, 31(3). https://doi.org/10.1145/2491245 — background on the authoritative server tier.

4. Potvin, R., & Levenberg, J. (2016). Why Google Stores Billions of Lines of Code in a Single Repository. CACM, 59(7), 78-87. https://doi.org/10.1145/2854146 — comparator system (Piper).

5. Sapling SCM. (n.d.). Sapling: A Scalable, User-Friendly Source Control System. Meta Platforms. https://sapling-scm.com/ — comparator system.

6. Chacon, S., & Straub, B. (2014). Pro Git (2nd ed.). Apress. https://git-scm.com/book — baseline system (Git).

Inclusion criteria:
- Publicly accessible architectural descriptions and documentation.
- Peer-reviewed or officially published sources.
- Sources directly relevant to the four pillars or four formal definitions.

Exclusion criteria:
- Internal design documents or source code not publicly available.
- Independent benchmark data (none is available for Scion).
- Any claim that cannot be traced to a published source.

No data will be generated before registration. The documents themselves exist publicly, but they have not been collected, coded, or analyzed for this protocol.

Expected duration: not applicable (document analysis only).

### Sample size

Sample size is not defined in the conventional sense because this is a formal architecture paper, not an empirical study.

Units of analysis and planned sample sizes:

1. Comparator systems: 4 (Git, Piper, Sapling/Mononoke, Scion).

2. Published sources: 6 primary references (see Data collection procedures).

3. Formal definitions: 4 (Changeset Tuple, Incremental Cost Model, Recursive Derived-Data Operator, Cache-Hit Probability Bound).

4. Architectural pillars: 4 (Client-Server Asymmetry, Sparse & Virtualized Checkouts, Lock-Free Changesets, Tiered Cache Topology).

5. Structural theorems: 2 (Cost(cᵢ) = O(|δᵢ|); P(Hit) ≥ 1 − ε).

6. Illustrative worked example: 1 (Section 6, hypothetical parameters).

7. Comparative table: 1 (Section 7, AetherGit vs. Git vs. Scion).

Expected total sample:
- Comparator systems: 4
- Published sources: 6
- Formal definitions: 4
- Architectural pillars: 4
- Structural theorems: 2
- Illustrative example: 1
- Comparative table: 1

No conditions, treatments, or clusters. No multi-level or mixed design.

### Sample size rationale

The sample size is determined by the scope of the published material, not by power analysis.

- Scion is documented in a single public disclosure (Anthropic, 2026).
- Piper, Sapling/Mononoke, and Git are selected as comparator systems because each represents a distinct architectural approach to large-scale source control.
- The four formal definitions and four architectural pillars are derived from the published material and the author's own prior structural analysis (Baladi, 2026a).

No statistical power analysis is applicable because this is a formal architecture paper, not a hypothesis test.

A larger empirical benchmark (implementation of the four pillars, instrumentation of λ_miss and μ_cache) is proposed as future work in Section 10.

### Starting and stopping rules

Starting rule:

Document analysis begins with the publication of Anthropic's October 2026 disclosure (Reference 1). There is no pilot phase.

Stopping rule:

The analysis terminates when:
1. All four pillars have been specified (Section 4).
2. All four definitions have been stated (Section 5).
3. The illustrative worked example has been presented (Section 6).
4. The comparative positioning has been completed (Section 7).
5. The limitations have been stated (Section 9).

No sequential testing or early stopping is involved. The paper is not an empirical study.

The proposed implementation and benchmark (Section 10) have not been executed. If executed in the future, their starting and stopping rules would be specified in a separate registration.

---

## Variables

### Manipulated variables

None. This is a formal architecture paper. No variables are manipulated. No treatments or conditions are administered. No randomization is involved.

The paper specifies an architecture and formalizes four definitions. It does not assign conditions, treatments, or arms.

The illustrative worked example in Section 6 applies the cache-hit bound under stated hypothetical parameters (ρ = 0.6, γ = 0.15). These are not manipulated variables — they are illustrative values chosen for clarity of exposition, not measured or assigned.

### Measured variables

This paper does not report empirical measurements. The variables below are analytical constructs drawn from the formal specification.

A. Formal definitions (4 variables):
- D1: Changeset Tuple — cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩. Measured as: formal statement; components present/absent.
- D2: Incremental Cost Model — Cost(cᵢ) = O(|δᵢ|). Measured as: formal statement; asymptotic complexity class.
- D3: Recursive Derived-Data Operator — Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p)}). Measured as: formal statement; recursion structure.
- D4: Cache-Hit Probability Bound — P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl). Measured as: formal statement; parameters (λ_miss, μ_cache, K, T_ttl, γ).

B. Architectural pillars (4 variables):
- P1: Client-Server Asymmetry — measured as: specified/not specified.
- P2: Sparse & Virtualized Checkouts — measured as: specified/not specified.
- P3: Lock-Free Incremental Changesets — measured as: specified/not specified.
- P4: Tiered Cache Topology — measured as: specified/not specified.

C. Structural theorems (2 variables):
- T1: Time Complexity — Cost(cᵢ) = O(|δᵢ|). Measured as: proven/not proven.
- T2: Cache Bound — P(Hit) ≥ 1 − ε. Measured as: proven/not proven.

D. Comparative properties (7 variables, Section 7):
- Topology (Git: distributed; Scion: client-server; AetherGit: client-server).
- Connectivity (Git: offline-first; Scion: always-online; AetherGit: always-online).
- Checkout model (Git: full clone; Scion: sparse/virtualized; AetherGit: sparse/virtualized).
- Object addressing (Git: packfiles; Scion: content-addressed; AetherGit: content-addressed).
- Change unit cost (Git: not formally bounded; Scion: reported, not formalized; AetherGit: O(|δᵢ|), formalized).
- Derived query data (Git: client-side; Scion: server-side, recursive; AetherGit: server-side, recursive, formalized).
- Coordination (Git: local; Scion: none at changeset creation, CAS at ref update; AetherGit: none at changeset creation, CAS at ref update).
- Cache-hit guarantee (Git: not applicable; Scion: >99% reported; AetherGit: ≥ bound of Eq. 4, illustrated not measured).

No covariates. No subsetting variables. No exclusion variables.

### Indices

No composite indices or derived variables are constructed.

The paper reports formal definitions, architectural specifications, and structural theorems — not numerical scores or composite indices.

The only numerical quantities reported are:
- The cache-hit bound parameters in the illustrative worked example (ρ = 0.6, γ = 0.15, T_ttl = 2, 8, 20, K = 1 to 12). These are hypothetical illustrative values, not measured or combined into an index.
- Operational figures cited for Git and Scion are drawn from the cited published sources, not independently measured by this author. They are not combined into any index.

No composite index, score, or derived variable is constructed from the formal definitions or architectural pillars.

---

## Analysis Plan

### Statistical models

No statistical models are used. This is a formal architecture paper, not a hypothesis test. No inferential statistics are planned.

Analysis proceeds through four formal procedures:

Procedure 1 — Formal specification (Section 5):
Four definitions are stated and interpreted in prose:
- Definition 1: Changeset Tuple.
- Definition 2: Incremental Cost Model.
- Definition 3: Recursive Derived-Data Operator.
- Definition 4: Cache-Hit Probability Bound.

Each definition is stated as an explicit mathematical claim. No statistical estimation is involved.

Procedure 2 — Architectural specification (Section 4):
Four architectural pillars are specified. Each pillar is described as an architectural commitment, not a measured property.

Procedure 3 — Illustrative worked example (Section 6):
The cache-hit bound (Equation 4) is applied under stated hypothetical parameters (ρ = 0.6, γ = 0.15). The bound is plotted as a function of K for three T_ttl values (2, 8, 20). This is an illustration of the formula, not a benchmark or simulation.

Procedure 4 — Comparative positioning (Section 7):
A table positions AetherGit's specified properties against Git's documented design and Scion's publicly disclosed architecture. The rightmost column is phrased in terms of specification, not measurement.

No controls, no manipulation checks, no convergence criteria, no assumption tests.

### Transformations

No transformations are applied. No coding scheme, centering, recoding, logging, winsorizing, or other data transformation is performed.

The analysis works with:
- Formal mathematical statements (Equations 1–4).
- Architectural specifications (Section 4).
- Qualitative comparative properties (Section 7).

No numerical data is collected, coded, or transformed. The illustrative worked example (Section 6) uses stated hypothetical parameters (ρ = 0.6, γ = 0.15, T_ttl ∈ {2, 8, 20}, K ∈ {1, …, 12}). These are not transformed — they are stated.

### Inference criteria

No p-values, Bayes factors, or model fit indices are used. The analysis is formal and architectural, not inferential.

Inferences are supported by:
1. Direct citation of the published architectural descriptions (Anthropic, 2026; Potvin & Levenberg, 2016; Corbett et al., 2013; Sapling SCM; Chacon & Straub, 2014).
2. Explicit distinction between (a) architectural claims reported in the source material, (b) structural inferences drawn from distributed-systems principles, and (c) self-reported operational figures that have not been independently verified.
3. Formal statements of the four definitions (Equations 1–4) and the two structural theorems (T1, T2).

No one-tailed or two-tailed tests are used. No multiple-comparison correction is applied, because no hypothesis tests are performed.

The illustrative worked example in Section 6 is not an inferential test. It plots Equation 4 under stated hypothetical parameters. It does not establish that any real system satisfies those parameters.

### Data inclusion and exclusion

Inclusion criteria:
- Publicly accessible architectural descriptions of source-control systems (Scion, Piper, Sapling/Mononoke, Git).
- Published documentation of each system's own design.
- Peer-reviewed or officially published sources.
- Anthropic's October 2026 disclosure as the sole source for all Scion-specific claims.

Exclusion criteria:
- Internal design documents or source code not publicly available (Scion is not public at the time of writing).
- Independent benchmark data (none is available for Scion).
- Any claim that cannot be traced to a published source.

Outliers:
No outliers are defined, because no numerical data are collected. All qualifying sources are included.

All observations (documents) meeting inclusion criteria are used. No subsetting is planned.

### Missing data

Not applicable. No empirical dataset is used, so no missing data arises.

Scion's source code and internal design documents are not publicly available. This absence is stated explicitly as a limitation of the manuscript (Section 9), not treated as missing data to be imputed.

No imputation is performed. No missing-data models are used.

### Other planned analysis

The paper proposes a future implementation and benchmark (Section 10). If executed, it would include:

1. Implementation of the four pillars: client-server asymmetry, sparse/virtualized checkouts, lock-free incremental changesets, tiered cache topology.

2. Instrumentation of λ_miss and μ_cache under a real or realistically synthesized agentic request stream.

3. Measurement of observed P(Hit) against the Equation 4 bound.

4. Instantiation and cost analysis of the derivation operator ⊕_D for specific derived-data categories (blame, path history).

5. Execution of the empirical evaluation protocol proposed in prior work (Baladi, 2026a, Section 9).

This protocol has not been executed. It is presented as proposed future work, not as analysis performed for this manuscript.

---

## Other

### Context and additional information

Context of the research program:

AetherGit is a formal architecture paper. It is a direct sequel to, and dependent on, the structural analysis in Baladi (2026a), which examined Anthropic's 2026 operational disclosure of its internal Scion source-control system.

The present paper formalizes a generalized architecture — named AetherGit — built from the structural properties that the prior analysis identified as plausibly load-bearing for agentic workloads: the decoupling of changeset creation from reference coordination, the separation of the write path from recursively derived query structures, and tiered caching with fault isolation.

What this registration does not include:

1. No implementation. AetherGit has not been built. No benchmark has been executed. No empirical performance has been measured.

2. No independent verification of operational figures. All operational figures attributed to Git and Scion throughout the paper are drawn from the cited published sources, not independently measured by this author.

3. No causal claims. The paper's claims are structural and formal, not causal.

4. No integration with the author's other research programs. This paper is independent of the author's prior work on Research I (epistemic discipline) and Research II (production and control of representations). It is a direct formal sequel to Baladi (2026a) on source control.

Related materials:

- Zenodo DOI: 10.5281/zenodo.23966896
- Figshare DOI: 10.6084/m9.figshare.34922532
- Official website: https://aethergit.netlify.app
- GitHub: https://github.com/gitdeeper15/AetherGit
- ORCID: https://orcid.org/0009-0003-8903-0029

Primary external source:

Anthropic. (2026). Redesigning Source Control at Anthropic. Published October 13, 2026 (updated October 15, 2026). https://www.anthropic.com/research/redesigning-source-control

This is the sole source for all Scion-specific architectural and operational claims.

Comparator systems:

- Git — Chacon & Straub (2014).
- Piper (Google) — Potvin & Levenberg (2016).
- Spanner (Google) — Corbett et al. (2013).
- Sapling/Mononoke (Meta) — Sapling SCM.

Ethics:

This study does not involve human subjects. No personal data is collected. All cited sources are public.

Protocol integrity:

The protocol is frozen at registration. Any change after registration will be documented as a protocol amendment with explicit rationale.

Next research stage:

Implementation of the four pillars; instrumentation and measurement of Equation 4 under synthetic or real agentic workload traces; per-category instantiation of the derivation operator.

Version 1.0.0 — November 2026.

---

## Metadata

### Contributors

Samir Baladi

### Resource type

No resource type

### Description

AetherGit is a proposed formal architecture for source control at agent scale, designed to meet the requirements of high-velocity, algorithmically driven development carried out by autonomous AI agents.

The architecture is built on four pillars: client-server asymmetry, sparse and virtualized checkouts, lock-free incremental changesets, and a tiered cache topology.

The paper gives four formal definitions:
(1) the changeset tuple cᵢ = ⟨δᵢ, P(cᵢ), τᵢ, σᵢ⟩;
(2) the incremental cost model Cost(cᵢ) = O(|δᵢ|);
(3) the recursive derived-data operator Deriv(cᵢ) = ⊕_D(δᵢ, {Deriv(p)});
(4) the cache-hit probability bound P(Hit) ≥ 1 − (λ_miss/μ_cache)^K · e^(−γ·T_ttl).

An illustrative worked example applies the cache-hit bound under stated hypothetical parameters (ρ = 0.6, γ = 0.15). A comparative table positions AetherGit's specified properties against Git's documented design and Scion's publicly disclosed architecture.

AetherGit is presented as a theoretical architecture and formalization exercise, developed in direct response to Anthropic's 2026 operational disclosure of its internal Scion system. It does not report an implementation, a benchmark, or empirically measured performance.

No implementation has been built and no benchmark has been executed for this manuscript.

The paper's contribution is a formal vocabulary and a set of provable structural claims, offered as a reference point against which a future implementation, or other systems serving agentic software-engineering workloads, can be evaluated.

Version 1.0.0 — November 2026.

DOI (Zenodo): 10.5281/zenodo.23966896
DOI (Figshare): 10.6084/m9.figshare.34922532
Website: https://aethergit.netlify.app

### Registration Type

OSF Preregistration

### Registry

OSF Registries

### Associated project

https://osf.io/zk532

### Date Created

Nov 5, 2026, 7:57 AM

### Date registered

Nov 5, 2026, 7:57 AM

### Subjects

- Software Engineering
- Computer Sciences
- Physical Sciences and Mathematics

### Tags

- AetherGit
- agentic software engineering
- cache theory
- content-addressed storage
- distributed systems
- formal methods
- incremental computation
- source control
- version control systems

### Affiliated Institutions

No affiliated institutions

### Funder Names

No information

### Language

No language

### Associated project

https://osf.io/zk532

### License

CC-By Attribution 4.0 International

### Registration DOI

10.17605/OSF.IO/NCWZA

---

## Citations

### APA

Baladi, S. (2026, November 5). AetherGit: Scalable Source Control for Autonomous AI Agents. OSF. https://doi.org/10.17605/OSF.IO/NCWZA

### MLA

Baladi, Samir. "AetherGit: Scalable Source Control for Autonomous AI Agents." OSF, 5 Nov. 2026. Web.

### Chicago

Baladi, Samir. 2026. "AetherGit: Scalable Source Control for Autonomous AI Agents." OSF. November 5. doi:10.17605/OSF.IO/NCWZA.

### BibTeX

```bibtex
@misc{baladi2026aethergit_osf,
  author       = {Baladi, Samir},
  title        = {{AetherGit: Scalable Source Control for Autonomous AI Agents}},
  year         = {2026},
  month        = nov,
  day          = {5},
  publisher    = {OSF},
  doi          = {10.17605/OSF.IO/NCWZA},
  url          = {https://doi.org/10.17605/OSF.IO/NCWZA},
  note         = {OSF Preregistration. Associated project: https://osf.io/zk532}
}
```

---

Source: Center for Open Science · OSF Registries
Retrieved: 2026-11-05
