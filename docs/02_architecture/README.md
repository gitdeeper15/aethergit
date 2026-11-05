# Architectural Pillars — v1.0.0

**Status:** Specified, version 1.0.0.
**Source:** Section 3 of the manuscript.
**Depends on:** Formalization Section (v1.0.0).

---

## Pillar 1 — Client-Server Asymmetry

The AetherGit client performs no history calculations or delta compression locally. When an agent requests a sparse workspace view, the client transmits a recursive descriptor query specifying only the target paths. The server streams exact tree nodes and file content blobs directly to the client's bounded cache.

---

## Pillar 2 — Sparse & Virtualized Checkouts

For automated testing and AI evaluation jobs, physical on-disk file materialization is frequently unnecessary. AetherGit provides virtualized file systems that load file contents on-demand upon filesystem read hooks. Jobs reading only a fraction of a repository pay zero disk I/O cost for unread directories.

---

## Pillar 3 — Lock-Free Changesets

Rather than relying on global reference locks during commit ingestion, AetherGit appends changesets to a distributed write-ahead log stored in a global database (e.g., Google Spanner). Branch updates are executed via atomic Compare-And-Swap (CAS) primitives, isolating commit creation from reference movement.

---

## Pillar 4 — Tiered Cache Topology

AetherGit employs a three-tier hierarchy: node-local daemons (`C₁`), regional object caches (`C₂`), and authoritative storage (`S`). Each tier is independent, enabling failure isolation and horizontal scalability.

```

[ Agent / CI Workspace ]
│ (Sparse / Virtualized RPC)
▼
┌────────────────┐
│ Aether Daemon  │  (Node-Local Cache & Disk Layout)
└───────┬────────┘
│
▼
┌────────────────┐
│ Aether Cache   │  (Regional Tiered In-Memory Cache)
└───────┬────────┘
│
▼
┌────────────────┐
│ Aether Server  │  (Spanner DB / Distributed Blob Store)
└────────────────┘

```

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Specified |
| Source | Section 3 of the manuscript |
| Depends on | Formalization Section (v1.0.0) |
