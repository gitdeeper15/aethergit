# Figure 1 — Repository State Space

**File:** `fig1_state_space.png`
**Source:** Definition 1
**Status:** ⏳ To be added

---

## Description

A Directed Acyclic Graph (DAG) `G = (V, E)`, where `V` is the set of immutable changesets and `E` defines parent-child dependencies.

Each changeset is a delta-tuple over content-addressed blobs:

```

cᵢ = ⟨P(cᵢ), Δᵢ, tᵢ, sigᵢ⟩

```

---

## Visual Structure

```

```

- Nodes: changesets
- Edges: parent-child derivation
- Each node is a delta-tuple
