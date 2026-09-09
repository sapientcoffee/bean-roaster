# 🔥 Bean-Roaster: Discovery & Requirements Rules

Welcome to **Bean-Roaster**, the autonomous product discovery and Socratic requirements swarm for the Antigravity CLI (`agy`).

## 1. Upstream Requirements Discipline
* **Zero Improvisation:** Never jump into implementation planning or code without an approved `02_PRD.md`.
* **Socratic Grilling First:** Challenge vague user input. Uncover unhandled error states, scale limits, and latency targets.
* **Copy-Editor Purification & Threat-Modeler Gate:** Purify requirements with `@copy-editor` to eliminate AI tells and enforce active, measurable criteria. Dispatch `@threat-modeler` in an isolated context to execute an OWASP ASVS Level 2 audit before human PRD sign-off.

## 2. Decoupled Handoffs
* Stage outputs are written strictly as Markdown files:
  - `plans/<feature-slug>/<timestamp>/00_IDEATION.md`
  - `docs/glossary.md`
  - `docs/adr/*.md`
  - `plans/<feature-slug>/<timestamp>/02_PRD.md`
* Opportunistic Dashboard Sync: If `bean-cup` is installed, update `visual-dashboard.html` via `scripts/sync_dashboard_if_available.py`. If absent, proceed seamlessly.
