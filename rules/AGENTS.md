# Bean-Roaster Agent & Skill Routing Rules

## Subagents
All local subagents in `agents/*.md` use `kind: local`, `subagent: true`, `mainAgent: false`, `model: inherit`, and normalized tool names (`read_file`, `write_file`, `edit_file`, `run_command`):
- `product-ideator` (`agents/product-ideator.md`): Local subagent with tools `[read_file, write_file, edit_file, run_command]`. Executes heavy Stage 0 product discovery, friction analysis, personas, CUJs, ADK topologies, and dynamic JSON schema generation into `.scratch/<id>/00_IDEATION.md`, returning a $\le 300$-word summary to `@expo`.
- `question-formulator` (`agents/question-formulator.md`): Local subagent with tools `[read_file, write_file, edit_file]`. Enforces the strict **Zero Feature Solution Leakage** boundary in an isolated context, reading `.scratch/<id>/00_IDEATION.md` and `docs/CONTEXT.md` and writing `.scratch/<id>/01_QUESTIONS.md`.
- `prd-author` (`agents/prd-author.md`): Local subagent with tools `[read_file, write_file, edit_file, run_command]`. Synthesizes discovery and extraction artifacts into `.scratch/<id>/03_PRD.md` (with numbered `AC1..ACN`, Gherkin scenarios, Google Cloud Well-Architected NFR pillars, and SRE observability) and generates `evals/test_kpis.py`.
- `copy-editor` (`agents/copy-editor.md`): Local subagent with tools `[read_file, write_file, edit_file]`. Scrubs AI boilerplate and enforces active, measurable criteria in `.scratch/<id>/00_IDEATION.md` and `.scratch/<id>/03_PRD.md`.
- `threat-modeler`: Shared security auditor provided by `bean-core` to audit `.scratch/<id>/03_PRD.md` against OWASP ASVS Level 2 controls.

## Skills & Stage Artifacts (Subagent Delegation)
- `ideator`: Dispatches `@product-ideator` via `invoke_subagent` to produce `.scratch/<id>/00_IDEATION.md` in an isolated context window.
- `cupping-form`: Dispatches `@question-formulator` via `invoke_subagent` to produce `.scratch/<id>/01_QUESTIONS.md` with zero feature solution leakage, then presents questions to the user via `ask_question`.
- `grill`: Conducts Socratic interview and extracts domain context into `.scratch/<id>/02_EXTRACTION.md`, `docs/CONTEXT.md`, `docs/glossary.md`, and `docs/adr/` (marking pre-merge ADRs as `Status: Proposed — Refs #<id>`).
- `domain-modeling`: Maintains `docs/CONTEXT.md`, `docs/glossary.md`, and `docs/adr/` (with `Status: Proposed — Refs #<id>` for pre-merge ADRs).
- `write-prd`: Orchestrates `@prd-author`, `@copy-editor`, and `@threat-modeler` via `invoke_subagent` to synthesize, purify, and security-audit `.scratch/<id>/03_PRD.md` and `evals/test_kpis.py`, then pauses for user approval.
