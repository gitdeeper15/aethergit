# Figure 4 — Architectural Pillars

**File:** `fig4_pillars.png`
**Source:** Section 3
**Status:** ⏳ To be added

---

## Description

Four architectural pillars:

1. **Client-Server Asymmetry** — Server performs all history calculations; client is bounded cache.
2. **Sparse & Virtualized Checkouts** — On-demand file materialization; zero I/O for unread directories.
3. **Lock-Free Changesets** — Distributed WAL + CAS primitives; no global reference locks.
4. **Tiered Cache Topology** — Node daemons + regional caches + authoritative storage.

---

## Visual Structure

```

┌─────────────────────────────────────────────────┐
│                   AetherGit                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. Client-Server Asymmetry                     │
│     Server does all history; client is cache    │
│                                                 │
│  2. Sparse & Virtualized Checkouts              │
│     On-demand; zero I/O for unread              │
│                                                 │
│  3. Lock-Free Changesets                        │
│     WAL + CAS; no global locks                  │
│                                                 │
│  4. Tiered Cache Topology                       │
│     C₁ → C₂ → S; failure isolation              │
│                                                 │
└─────────────────────────────────────────────────┘

```

- Four pillars, one framework
- Each pillar is independent
- All four are specified in v1.0.0
