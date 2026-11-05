# Contributing to AetherGit

**AetherGit: Scalable Source Control for Autonomous AI Agents**

---

## Status

This project is a **formal research paper** (`v1.0.0`). The framework is specified through three formal definitions and four architectural pillars. No empirical work has been performed.

Contributions at this stage are welcome in:

- **Formalization**: Critical review of Definitions 1–3, proofs, and probabilistic bounds.
- **Architecture**: Proposals for the four pillars (client-server asymmetry, sparse checkouts, lock-free changesets, tiered cache).
- **Empirical evaluation**: Proposals for benchmarking against Git, Piper, Sapling/Mononoke.
- **Documentation**: Clarifying the manuscript, adding examples, or improving figure quality.

**Not accepted at this stage:**

- Empirical claims presented as findings (no empirical work has been performed).
- New architectural commitments that bypass the sequential formalization discipline.
- Changes to the formal definitions without a documented rationale.

For extensions, open an issue first to discuss scope.

---

## Reporting Issues

Open an issue with:

- A one-sentence description.
- The affected file (e.g., `README.md`, `PUBLICATION/research_paper_styled.docx`).
- A minimal reproduction or screenshot.
- Expected vs. actual behavior.

---

## Submitting Changes

```bash
git checkout -b feature/short-description
# make changes
git commit -m "feat: short description"
git push origin feature/short-description
```

Then open a pull request. Each PR should address one concern.

---

Code Standards

Language Standard
Python PEP 8, black (88 chars), isort, flake8
Markdown markdownlint (MD013 disabled)
YAML yamllint

Reproducibility: every documentation change must preserve the sequential formalization discipline and the negative commitments.

---

Data Provenance

All figures and diagrams are original to this project. No third-party imagery was used. The architectural diagrams (three-tier AetherGit topology, four pillars) were constructed from the formal description in the manuscript.

---

Review Process

· All changes are reviewed by the maintainer (Samir Baladi).
· Changes to the manuscript, figures, or formal definitions require explicit documentation in CHANGELOG.md with rationale.
· Adoption of any new formal construct requires an explicit version increment.

---

Contact

· Email: gitdeeper@gmail.com
· ORCID: https://orcid.org/0009-0003-8903-0029
· Zenodo DOI: https://doi.org/10.5281/zenodo.23966896
· PyPI: https://pypi.org/project/AetherGit
· Website: https://aethergit.netlify.app

---

Thank you for helping improve the formal analysis of high-throughput source control for autonomous AI agents.
