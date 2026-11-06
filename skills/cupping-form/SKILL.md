---
name: cupping-form
description: Stage 1 - Generates a structured technical questionnaire (.scratch/<id>/01_QUESTIONS.md) to uncover ambiguities, boundaries, NFRs, and failure modes with zero feature solution leakage.
---

# Skill: Cupping Form (Stage 1)

## Objective
Generate a rigorous, Socratic technical questionnaire (`.scratch/<id>/01_QUESTIONS.md`) to surface hidden assumptions, ambiguous domain boundaries, edge cases, and non-functional requirements with strict **Zero Feature Solution Leakage** before any architecture or implementation solution is proposed.

## Rules of Engagement
1. **Zero Feature Solution Leakage:** Do NOT prescribe, suggest, or embed specific implementation solutions, frameworks, database choices, or code architectures inside the questions. Ask solely about problem boundaries, contracts, invariants, scale targets, and failure semantics.
2. **Subagent Context Isolation:** Delegate questionnaire drafting to `@question-formulator` via `invoke_subagent` so the Zero Feature Solution Leakage boundary is enforced in an isolated context window.
3. **Output Path:** Write the structured questionnaire directly to `.scratch/<id>/01_QUESTIONS.md`.

## Instructions
1. **Resolve Scratch Bundle:**
   - Resolve or reuse the active feature identifier `<id>` under `.scratch/<id>/`.
2. **Dispatch `@question-formulator` via `invoke_subagent`:**
   - Invoke `@question-formulator` via `invoke_subagent`, instructing it to read `.scratch/<id>/00_IDEATION.md` and `docs/CONTEXT.md` (if present) and generate `.scratch/<id>/01_QUESTIONS.md` covering:
     - **Domain Invariants & Terminology**
     - **Boundary Conditions & Edge Cases**
     - **Reliability, Scale & Latency Targets (NFRs)**
     - **Security, Authorization & Trust Boundaries**
   - Verify `@question-formulator` returns `PASS` and confirms zero feature solution leakage.
3. **Present Questions & Pause at Execution Barrier:**
   - Present the questions from `.scratch/<id>/01_QUESTIONS.md` to the user via `ask_question` (or interactive prompt).
   - **Execution Barrier:** Halt and wait for user responses before proceeding to Stage 2 (`/grill` or Blind Cupping `.scratch/<id>/02_EXTRACTION.md`).
