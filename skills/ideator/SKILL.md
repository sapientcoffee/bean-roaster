---
name: ideator
description: Generates a product discovery and technical architecture draft from any raw product idea, feature request, or prompt. It dynamically analyzes friction points, personas, CUJs, ADK routing topologies, and a data schema, writing the results to .scratch/<id>/00_IDEATION.md.
---
# Skill: Ideator (Stage 0 Discovery)

## Objective
Expand a raw product idea, feature request, or prompt into a comprehensive product discovery and technical architecture draft (`.scratch/<id>/00_IDEATION.md`) while keeping the main orchestrator (`@expo`) within the Smart Zone (`< 100K` tokens) by delegating heavy authoring to `@product-ideator`.

## Instructions

### Step 1: Resolve Scratch Bundle
1. Check if `.scratch/<id>/` already exists for the active feature or issue `<id>`. If it exists, **reuse that exact directory**; otherwise create `.scratch/<id>/`.

### Step 2: Dispatch `@product-ideator` Subagent
1. Dispatch `@product-ideator` via `invoke_subagent` with the raw product idea/prompt, the target `.scratch/<id>/00_IDEATION.md` path, and any relevant `docs/CONTEXT.md` pointer.
2. `@product-ideator` operates in an isolated context window to:
   - Deconstruct the domain and identify 3–4 real-world friction points and 2–3 target personas.
   - Formulate 2–3 end-to-end Customer User Journeys (Trigger, Core Transaction, AI Agent Intervention, Outcome).
   - Map each CUJ to an optimal ADK orchestration topology (`Coordinator-Specialist`, `SequentialAgent / Pipeline`, or `LoopAgent / Evaluator-Refiner`).
   - Generate a dynamic JSON schema with 3–5 mock records and agent telemetry fields (`agent_status`, `refinement_count`, `evaluation_result`).
   - Write `.scratch/<id>/00_IDEATION.md`, stamp OKF metadata if `scripts/okf.py` is available, and return a concise ($\le 300$ words) summary.
3. Optional Purification: If prose tightening is needed, dispatch `@copy-editor` via `invoke_subagent` on `.scratch/<id>/00_IDEATION.md`.

### Step 3: Completion Handover
Once `@product-ideator` returns `PASS` and `.scratch/<id>/00_IDEATION.md` is written, output:
"🟢 Discovery complete! `@product-ideator` generated the discovery draft at `.scratch/<id>/00_IDEATION.md` with product direction, ADK agent topologies, and a mock JSON schema. Review the file, customize your preferences if needed, and run `/cupping-form` or `/grill` to align on the next phase."
