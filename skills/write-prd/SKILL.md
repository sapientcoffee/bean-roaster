---
name: write-prd
description: Stage 3 - Acts as a Product Manager to turn aligned discovery and extraction outputs into a rigorous Product Requirements Document (.scratch/<id>/03_PRD.md), saving the output and managing the user approval process.
---

# Skill: Write PRD (Product Requirements Document) (Stage 3)

## Objective
Orchestrate the synthesis, purification, and security auditing of a rigorous Product Requirements Document (`.scratch/<id>/03_PRD.md`) and executable KPI benchmark suite (`evals/test_kpis.py`) using isolated subagents (`@prd-author`, `@copy-editor`, `@threat-modeler`), then **pause for user approval** before any technical specification or implementation begins.

## Rules of Engagement
- **Artifact Handover**: Save final outputs to `.scratch/<id>/03_PRD.md` and `evals/test_kpis.py`.
- **Directory Reuse**: Reuse the existing `.scratch/<id>/` directory (containing `00_IDEATION.md`, `01_QUESTIONS.md`, or `02_EXTRACTION.md`) and inspect `docs/CONTEXT.md` and `docs/adr/`.
- **Pure Product Boundary**: Do NOT suggest technical frameworks, software libraries, databases, state management patterns, or physical file/folder structures unless already locked in `docs/adr/` (marked `Status: Proposed — Refs #<id>`).
- **Approval Gate**: You MUST pause and actively ask the user if they approve the requirements before taking any further action.
- **Iterative Rework**: If the user provides feedback, re-dispatch `@prd-author` and `@copy-editor` via `invoke_subagent` to update `.scratch/<id>/03_PRD.md` and ask for approval again.

## Instructions
1. **PRD Synthesis (`@prd-author` via `invoke_subagent`)**:
   - Dispatch `@prd-author` via `invoke_subagent` in an isolated context to ingest `.scratch/<id>/00_IDEATION.md`, `.scratch/<id>/01_QUESTIONS.md`, `.scratch/<id>/02_EXTRACTION.md`, `docs/CONTEXT.md`, and `docs/adr/`.
   - Require `@prd-author` to draft `.scratch/<id>/03_PRD.md` (including Problem Statement, Target Personas, User Stories & Epics, Scope Boundaries, numbered `AC1..ACN` Gherkin scenarios, Google Cloud Well-Architected NFR pillars, Deployment & DevOps Strategy, and SRE & Observability Integration) and generate executable KPI benchmarks in `evals/test_kpis.py`.
2. **Specification Purification Gate (`@copy-editor` via `invoke_subagent`)**:
   - Dispatch `@copy-editor` via `invoke_subagent` in an isolated context to ingest `.scratch/<id>/03_PRD.md`, eliminate AI boilerplate and corporate buzzwords, convert passive voice to active voice, and replace vague criteria with dense, measurable thresholds.
3. **OWASP ASVS Level 2 Threat Modeling Gate (`@threat-modeler` via `invoke_subagent`)**:
   - Dispatch `@threat-modeler` (from `bean-core`) via `invoke_subagent` in an isolated context to audit `.scratch/<id>/03_PRD.md` against baseline ASVS Level 2 domains: V2 (Authentication), V3 (Session Management), V4 (Access Control), and V5 (Validation & Sanitization).
   - Require `@threat-modeler` to write `docs/security/asvs_requirements.md` and return a binary `PASS` or `BLOCKED: <reasons>` decision.
   - If `BLOCKED`, refine `.scratch/<id>/03_PRD.md` via `@prd-author` until `@threat-modeler` returns `PASS`.
4. **Halt Execution for User Approval**:
   - Explicitly ask the user: "Do you approve of these product requirements and PRD? Please review `.scratch/<id>/03_PRD.md` and the executable KPIs in `evals/test_kpis.py`."
