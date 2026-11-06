# Bean-Roaster: Discovery & Requirements Rules

Welcome to **Bean-Roaster**, the autonomous product discovery and Socratic requirements swarm for Antigravity (`agy`).

## 1. Upstream Requirements Discipline
* **Zero Improvisation:** Never jump into implementation planning or code without an approved `.scratch/<id>/03_PRD.md`.
* **Cupping Form & Socratic Grilling First:** Generate `.scratch/<id>/01_QUESTIONS.md` with zero feature solution leakage, challenge vague user input, and uncover unhandled error states, scale limits, and latency targets.
* **Copy-Editor Purification & Threat-Modeler Gate:** Purify requirements with `@copy-editor` to eliminate AI tells and enforce active, measurable criteria. Dispatch `@threat-modeler` (provided by `bean-core`) in an isolated context to execute an OWASP ASVS Level 2 audit before human PRD sign-off.

## 2. Decoupled Handoffs
* Stage outputs are written strictly as Markdown files:
  - `.scratch/<id>/00_IDEATION.md`
  - `.scratch/<id>/01_QUESTIONS.md`
  - `.scratch/<id>/02_EXTRACTION.md`
  - `.scratch/<id>/03_PRD.md`
  - `docs/CONTEXT.md`
  - `docs/glossary.md`
  - `docs/adr/*.md` (pre-merge ADRs marked `Status: Proposed — Refs #<id>`)
