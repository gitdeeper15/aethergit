# Figure 3 — Cache Hit Probability

**File:** `fig3_cache_topology.png`
**Source:** Definition 3
**Status:** ⏳ To be added

---

## Description

Three-tier cache topology: node-local daemons (C₁), regional caches (C₂), and authoritative storage (S).

The probability `P(Hit)` of resolving tree objects without querying `S` is bounded by:

```

P(Hit) = 1 − ∏_{k=1}^{N}(1 − h_k) ≥ 1 − ε

```

Because content addressing enforces strict immutability:

```

∂ CacheState / ∂ Time = 0

```

---

## Visual Structure

```

[ Agent / CI Workspace ]
│
▼
┌────────────────┐
│ Aether Daemon  │  C₁ (Node-Local Cache)
└───────┬────────┘
│
▼
┌────────────────┐
│ Aether Cache   │  C₂ (Regional Cache)
└───────┬────────┘
│
▼
┌────────────────┐
│ Aether Server  │  S (Authoritative Storage)
└────────────────┘

```

- Three independent tiers
- Failure isolation
- Horizontal scalability
