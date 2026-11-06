---
name: grill
description: Stage 1/2 - A relentless Socratic interview to sharpen a plan or design, extract domain context into .scratch/<id>/02_EXTRACTION.md and docs/CONTEXT.md, and record ADRs and glossary terms as we go.
---

# Skill: Grill

## Objective
Your goal is to conduct an interactive Socratic alignment and requirements gathering session. You must analyze the requirements of the feature or change, identify ambiguities, challenge terms, and stress-test the design before any technical specification or PRD (`.scratch/<id>/03_PRD.md`) is drafted.

## Context Check & Scratch Directory Reuse
1. **Search for Ideation & Questions Output**: Check if `.scratch/<id>/` contains `.scratch/<id>/00_IDEATION.md` or `.scratch/<id>/01_QUESTIONS.md`, and inspect `docs/CONTEXT.md` if present.
   - **REUSE `.scratch/<id>/`** for all subsequent stage outputs.
2. **Use Context if Exists**: If `.scratch/<id>/00_IDEATION.md` or `.scratch/<id>/01_QUESTIONS.md` exists, read them immediately to prime and guide the grilling session.
3. **Fallback**: If no existing `.scratch/<id>/` directory is found, create `.scratch/<id>/` using the issue number or feature slug.

## Instructions
1. Engage in Socratic requirements gathering by running an interactive alignment session with the user.
2. Formulate **3 to 5 targeted Socratic questions** using the `ask_question` tool (or direct interactive text prompt) to challenge assumptions and clarify ambiguities.
3. Align with the `/domain-modeling` skill guidelines:
   - Challenge terms against the ubiquitous language in `docs/glossary.md` and `docs/CONTEXT.md`.
   - Challenge design assumptions and align requirements with Google Cloud Well-Architected Framework pillars (Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency), deployment strategies, and SRE/observability best practices.
   - Sharpen fuzzy or overloaded terms.
   - Discuss concrete scenarios and probe edge cases one-by-one.
   - Write or update `docs/glossary.md`, `docs/CONTEXT.md`, and `.scratch/<id>/02_EXTRACTION.md` as terms and domain boundaries are resolved.
   - Record architectural decisions as ADRs inside `docs/adr/` if they meet the ADR criteria, marking pre-merge ADRs with `Status: Proposed — Refs #<id>`.
4. **EXECUTION BARRIER**: Present your Socratic questions and **STOP execution immediately**. Do NOT draft `.scratch/<id>/03_PRD.md` or move to subsequent stages until the user answers your questions.
