---
name: write-prd
description: Stage 3 - Acts as a Product Manager to turn aligned discovery and extraction outputs into a rigorous Product Requirements Document (.scratch/<id>/03_PRD.md), saving the output and managing the user approval process.
---

# Skill: Write PRD (Product Requirements Document) (Stage 3)

## Objective
Your goal as the Product Manager is to turn aligned user ideas and extracted context into a rigorous Product Requirements Document (`.scratch/<id>/03_PRD.md`) and **pause for user approval** before any technical specification or implementation begins.

## Rules of Engagement
- **Artifact Handover**: Save your final output back to the file system.
- **Save Location & Directory Reuse**: Output the markdown document to `.scratch/<id>/03_PRD.md`. **CRITICAL**: Check if `.scratch/<id>/` already exists (containing `00_IDEATION.md`, `01_QUESTIONS.md`, or `02_EXTRACTION.md`) and inspect `docs/CONTEXT.md` and `docs/adr/`. Reuse `.scratch/<id>/`.
- **Pure Product Boundary**: Do NOT suggest technical frameworks, software libraries, databases, state management patterns, or physical file/folder structures unless already locked in `docs/adr/` (marked `Status: Proposed — Refs #<id>`). Keep the requirements focused on the business problem, personas, customer journeys, scope, and functional/non-functional acceptance criteria.
- **Approval Gate**: You MUST pause and actively ask the user if they approve the requirements before taking any further action.
- **Iterative Rework**: If the user leaves comments or provides feedback in chat, apply the requested changes to `.scratch/<id>/03_PRD.md` and ask for approval again!

## Instructions
1. **Deconstruct User Intent & Context**: Deeply analyze `.scratch/<id>/00_IDEATION.md`, `.scratch/<id>/01_QUESTIONS.md`, `.scratch/<id>/02_EXTRACTION.md`, `docs/CONTEXT.md`, and `docs/adr/`.
2. **Draft the Markdown PRD (`.scratch/<id>/03_PRD.md`)**: Your PRD MUST include:
   - **Problem Statement**: Definition of the pain point.
   - **Target Personas**: Who will use this feature.
   - **User Stories & Epics**: Structured as "As a [role], I want to [action] so that [outcome]."
   - **Scope Boundaries**: In-Scope and Out-of-Scope lists.
   - **Acceptance Criteria**: Gherkin (Given-When-Then) scenarios.
   - **Non-Functional Requirements (NFRs) / Google Cloud Well-Architected Framework Pillars**: Reliability (self-healing, backups), Security (least-privilege IAM, VPC Service Controls, Cloud Secret Manager), Cost Optimization (right-sizing, cleanups), Performance Efficiency (indexes, cache, autoscaling thresholds).
   - **Deployment & DevOps Strategy**: Target runtimes, Infrastructure-as-Code resources, CI/CD setup, and progressive release strategies (canary, rolling, blue-green).
   - **SRE & Observability Integration**: Structured logging, monitoring metrics, tracing integration, SLIs/SLOs targets, error budget rules, and operational runbooks.
3. **Specification Purification Gate (`@copy-editor`)**:
   - Post-drafting, dispatch the subagent `@copy-editor` in an isolated context to ingest `.scratch/<id>/03_PRD.md`, eliminate AI boilerplate and corporate buzzwords, convert passive voice to active voice, and replace vague criteria with dense, measurable thresholds.
4. **OWASP ASVS Level 2 Threat Modeling Gate (`@threat-modeler`)**:
   - Dispatch `@threat-modeler` (from `bean-core`) in an isolated context to audit `.scratch/<id>/03_PRD.md` against baseline ASVS Level 2 domains: V2 (Authentication), V3 (Session Management), V4 (Access Control), and V5 (Validation & Sanitization).
   - Require `@threat-modeler` to write `docs/security/asvs_requirements.md` and return a binary `PASS` or `BLOCKED: <reasons>` decision.
   - Refine `.scratch/<id>/03_PRD.md` until `@threat-modeler` returns `PASS`.
5. **Generate Executable Evals (`evals/test_kpis.py`)**:
   - Parse all measurable KPIs and non-functional requirements in `.scratch/<id>/03_PRD.md` and generate programmatic benchmark test scripts in `evals/test_kpis.py` (e.g., testing latency thresholds, error rate bounds, and payload limits).
6. Save all documents (`.scratch/<id>/03_PRD.md`, `evals/test_kpis.py`).
7. **Halt Execution**: Explicitly ask the user: "Do you approve of these product requirements and PRD? Please review `.scratch/<id>/03_PRD.md` and the executable KPIs in `evals/test_kpis.py`."
