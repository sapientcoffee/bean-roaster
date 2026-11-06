# Bean-Roaster Agent & Skill Routing Rules

## Subagents
- `copy-editor` (`agents/copy-editor.md`): Local subagent (`kind: local`, `subagent: true`, `mainAgent: false`, `model: inherit`) with tools `[read_file, write_file, edit_file]`. Used to scrub AI boilerplate and enforce measurable criteria in `.scratch/<id>/00_IDEATION.md` and `.scratch/<id>/03_PRD.md`.
- `threat-modeler`: Shared security auditor provided by `bean-core`.

## Skills & Stage Artifacts
- `ideator`: Produces `.scratch/<id>/00_IDEATION.md`.
- `cupping-form`: Produces `.scratch/<id>/01_QUESTIONS.md` with zero feature solution leakage.
- `grill`: Conducts Socratic interview and extracts domain context into `.scratch/<id>/02_EXTRACTION.md`, `docs/CONTEXT.md`, `docs/glossary.md`, and `docs/adr/` (marking pre-merge ADRs as `Status: Proposed — Refs #<id>`).
- `domain-modeling`: Maintains `docs/CONTEXT.md`, `docs/glossary.md`, and `docs/adr/` (with `Status: Proposed — Refs #<id>` for pre-merge ADRs).
- `write-prd`: Synthesizes `.scratch/<id>/03_PRD.md` and `evals/test_kpis.py`.
