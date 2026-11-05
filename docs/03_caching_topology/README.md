# Caching Topology — v1.0.0

**Status:** Defined, version 1.0.0.
**Source:** Section 3.3 of the manuscript.
**Depends on:** Formalization Section (v1.0.0).

---

## Cache Hit Probability Bound

Given an always-online client topology featuring a tiered hierarchy of regional edge caches (`C₁`), node daemons (`C₂`), and authoritative storage (`S`), we model the request service latency `L` for sparse checkout operations.

Let `R` be a sparse tree query requested by an autonomous agent execution sandbox targeting a path subset `Ω_agent ⊂ Ω`. The probability `P(Hit)` of resolving tree objects without querying the authoritative Spanner storage tier `S` is bounded by:

```

P(Hit) = 1 − ∏_{k=1}^{N}(1 − h_k) ≥ 1 − ε

```

Where:
- `h_k` = local cache hit ratio at tier `k`
- `ε` = upper bound on cache miss probability under stationary access distributions

---

## Strict Immutability

Because content addressing enforces strict immutability (`hash(Object) = Constant`), cache invalidation overhead is strictly zero:

```

∂ CacheState / ∂ Time = 0   (for all materialized objects)

```

---

## Three-Tier Topology

| Tier | Component | Role |
|---|---|---|
| C₁ | Node-Local Daemon | Local cache & disk layout |
| C₂ | Regional Cache | Tiered in-memory cache |
| S | Authoritative Server | Spanner DB / Distributed Blob Store |

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Defined |
| Source | Section 3.3 of the manuscript |
| Depends on | Formalization Section (v1.0.0) |
