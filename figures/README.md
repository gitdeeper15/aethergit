# AetherGit — Figures

**Version:** 1.0.0
**Date:** 2026-11-05
**Status:** Pending

---

## Planned Figures

| # | Figure | Description |
|---|---|---|
| 1 | Repository State Space | DAG topology with changeset tuple |
| 2 | Recursive Derived State | Φ_D recursion over parent set |
| 3 | Cache Hit Probability | Three-tier cache topology |
| 4 | Architectural Pillars | Four pillars overview |

---

## Figure 1 — Repository State Space

**File:** `fig1_state_space.png`
**Source:** Definition 1
**Description:** A Directed Acyclic Graph (DAG) `G = (V, E)`, where `V` is the set of immutable changesets and `E` defines parent-child dependencies. Each changeset is a delta-tuple over content-addressed blobs.

---

## Figure 2 — Recursive Derived State

**File:** `fig2_derived_state.png`
**Source:** Definition 2
**Description:** The recursive composition function `Φ_D` over the parent set `P(cᵢ)` and local delta `Δᵢ`.

---

## Figure 3 — Cache Hit Probability

**File:** `fig3_cache_topology.png`
**Source:** Definition 3
**Description:** Three-tier cache topology: node-local daemons (C₁), regional caches (C₂), and authoritative storage (S).

---

## Figure 4 — Architectural Pillars

**File:** `fig4_pillars.png`
**Source:** Section 3
**Description:** Four architectural pillars: client-server asymmetry, sparse & virtualized checkouts, lock-free changesets, tiered cache topology.

---

## Status

| Figure | File | Status |
|---|---|---|
| **Combined** | aethergit_architecture_and_performance_formalization.png | ✅ Added |
| 1 | fig1_state_space.png | ✅ Added |
| 2 | fig2_derived_state.png | ✅ Added |
| 3 | fig3_cache_topology.png | ✅ Added |
| 4 | fig4_pillars.png | ✅ Added |

The four figures have been generated and added to this directory.
