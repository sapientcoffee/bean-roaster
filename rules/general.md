# 🔥 Bean-Roaster: Discovery & Requirements Rules

Welcome to **Bean-Roaster**, the autonomous product discovery and Socratic requirements swarm for the Antigravity CLI (`agy`).

## 1. Upstream Requirements Discipline
* **Zero Improvisation:** Never jump into implementation planning or code without an approved `02_PRD.md`.
* **Socratic Grilling First:** Challenge vague user input. Uncover unhandled error states, scale limits, and latency targets.
* **Maintain Ubiquitous Language:** Record all domain concepts in `docs/glossary.md` and high-leverage architectural choices in `docs/adr/`.
* **Red-Team Gate:** Prior to asking for human PRD approval, dispatch `@red-team-reviewer` to audit requirements against Murphy's Law.

## 2. Decoupled Handoffs
* Stage outputs are written strictly as Markdown files:
  - `plans/<feature-slug>/<timestamp>/00_IDEATION.md`
  - `docs/glossary.md`
  - `docs/adr/*.md`
  - `plans/<feature-slug>/<timestamp>/02_PRD.md`
* Opportunistic Dashboard Sync: If `bean-cup` is installed, update `visual-dashboard.html` via `scripts/sync_dashboard_if_available.py`. If absent, proceed seamlessly.
