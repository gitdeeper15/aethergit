# Figure 2 — Recursive Derived State

**File:** `fig2_derived_state.png`
**Source:** Definition 2
**Status:** ⏳ To be added

---

## Description

The recursive composition function `Φ_D` over the parent set `P(cᵢ)` and local delta `Δᵢ`:

```

D(cᵢ) = Φ_D({D_p | p ∈ P(cᵢ)}, Δᵢ)

```

---

## Visual Structure

```

D(c₁)  D(c₂)    ← computed server-side

```

- Derived data is computed recursively
- Computed server-side, not client-side
- Decoupled from write path
