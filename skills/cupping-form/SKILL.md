---
name: cupping-form
description: Stage 1 - Generates a structured technical questionnaire (.scratch/<id>/01_QUESTIONS.md) to uncover ambiguities, boundaries, NFRs, and failure modes with zero feature solution leakage.
---

# Skill: Cupping Form (Stage 1)

## Objective
Generate a rigorous, Socratic technical questionnaire (`.scratch/<id>/01_QUESTIONS.md`) to surface hidden assumptions, ambiguous domain boundaries, edge cases, and non-functional requirements before any architecture or implementation solution is proposed.

## Rules of Engagement
1. **Zero Feature Solution Leakage:** Do NOT prescribe, suggest, or embed specific implementation solutions, frameworks, database choices, or code architectures inside the questions. Ask solely about problem boundaries, contracts, invariants, scale targets, and failure semantics.
2. **Scratch Workspace Mandate:** Resolve or reuse the active feature identifier `<id>` under `.scratch/<id>/`. Read `.scratch/<id>/00_IDEATION.md` and `docs/CONTEXT.md` (if present) for context.
3. **Output Path:** Write the structured questionnaire directly to `.scratch/<id>/01_QUESTIONS.md`.

## Instructions
1. **Context Inspection:**
   - Check `.scratch/<id>/00_IDEATION.md` and `docs/CONTEXT.md` (plus `docs/glossary.md` if present) to understand the problem statement, personas, and domain vocabulary.
2. **Formulate Technical Questions:**
   - Group questions under clear sections:
     - **Domain Invariants & Terminology**
     - **Boundary Conditions & Edge Cases**
     - **Reliability, Scale & Latency Targets (NFRs)**
     - **Security, Authorization & Trust Boundaries**
3. **Verify Zero Solution Leakage:**
   - Audit every question to ensure it probes *what* must hold true rather than *how* to code it.
4. **Save & Pause:**
   - Write `.scratch/<id>/01_QUESTIONS.md` and present the questions to the user via `ask_question` (or interactive prompt).
   - **Execution Barrier:** Halt and wait for user responses before proceeding to Stage 2 (`/grill` or `.scratch/<id>/02_EXTRACTION.md`).
