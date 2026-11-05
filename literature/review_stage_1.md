# Literature Review — Stage 1: Categorical Positioning

**Status:** Stage 1 completed 2026-11-05.
**Matrix:** `literature/review_matrix.csv`

---

## 1. Purpose

This document reports Stage 1 of the literature review: a categorical positioning of AetherGit's 10 categories (3 definitions + 4 pillars + 2 theorems + 1 framework) against five traditions. Stage 1 does not claim originality; it classifies each category as **Redundant** (already present), **Reorganized** (present but grouped differently), or **Distinct** (no clear counterpart).

---

## 2. The Five Traditions

### 2.1 Distributed Version Control (Git)

**Focus:** Baseline distributed VCS. Full local clones, packfiles, offline-first paradigm.

**Strengths:** Well-theorized DAG topology, content-addressed storage, distributed commits.

**Weaknesses:** No formal treatment of agentic workloads; no client-server asymmetry; no probabilistic cache bounds.

### 2.2 Centralized Monorepo Systems (Piper)

**Focus:** Google's centralized monorepo VCS.

**Strengths:** Client-server asymmetry; server-side derived data; scalable for millions of commits.

**Weaknesses:** Not designed for parallel autonomous agents; no formal cache bounds.

### 2.3 Scalable Monorepo Systems (Sapling/Mononoke)

**Focus:** Meta's scalable VCS.

**Strengths:** Sparse checkouts; server-side metadata; scalable.

**Weaknesses:** No formal probabilistic cache bounds; no lock-free changesets.

### 2.4 Distributed Systems

**Focus:** Spanner, CockroachDB, content-addressed storage.

**Strengths:** Tiered caching; strict immutability; distributed consistency.

**Weaknesses:** Not applied to VCS; no formal connection to changeset ingestion.

### 2.5 Agentic Software Engineering (Scion)

**Focus:** Anthropic's internal source control for agentic workloads.

**Strengths:** Case study of agentic VCS; operational figures.

**Weaknesses:** No formal framework; no probabilistic bounds; no lock-free changesets formalization.

---

## 3. Categorical Classification Summary

### 3.1 Definitions (3)

| Category | Classification | Primary Tradition |
|---|---|---|
| D1 — Repository State Space | **Reorganized** | Distributed VCS |
| D2 — Recursive Derived State | **Reorganized** | Piper / Sapling |
| D3 — Cache Hit Probability | **Distinct** | Distributed systems (partial) |

### 3.2 Pillars (4)

| Category | Classification | Primary Tradition |
|---|---|---|
| P1 — Client-Server Asymmetry | **Redundant** | Piper / Sapling |
| P2 — Sparse & Virtualized Checkouts | **Reorganized** | Git / Sapling |
| P3 — Lock-Free Changesets | **Distinct** | — |
| P4 — Tiered Cache Topology | **Reorganized** | Distributed systems |

### 3.3 Theorems (2)

| Category | Classification | Primary Tradition |
|---|---|---|
| T1 — Time Complexity O(\|Δ\|) | **Distinct** | — |
| T2 — Cache Bound P(Hit) ≥ 1−ε | **Distinct** | — |

---

## 4. Preliminary Findings

### 4.1 What Is Redundant

- **P1** (Client-Server Asymmetry): Well-established in Piper and Sapling/Mononoke.

**Implication:** AetherGit should not claim originality for this pillar. Its value is in the formal framework around it.

### 4.2 What Is Distinct

- **D3** (Cache Hit Probability): Probabilistic cache bound with content-addressing immutability is not formalized elsewhere.
- **P3** (Lock-Free Changesets): Lock-free changeset ingestion with CAS is not formalized in existing VCS.
- **T1** (Time Complexity O(\|Δ\|)): Not formally proven in existing VCS.
- **T2** (Cache Bound P(Hit) ≥ 1−ε): Not formalized elsewhere.

**Implication:** These are AetherGit's strongest conceptual contributions.

### 4.3 What Is Reorganized

- **D1, D2, P2, P4**: Exist in adjacent traditions but organized differently.

**Implication:** AetherGit's contribution to these categories is **integrative** — not the discovery of new categories, but their arrangement into a coherent architecture.

---

## 5. What This Stage Does Not Do

- It does **not** claim conceptual originality for any category.
- It does **not** provide reference-level citations (Stage 2).
- It does **not** synthesize across traditions (Stage 3).

---

## 6. Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Stage 1 completed |
| Matrix | `literature/review_matrix.csv` |
| Next Stage | Stage 2 (reference-level verification) |
