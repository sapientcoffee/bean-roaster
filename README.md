<p align="center">
  <img src="assets/banner.png" alt="Bean-Roaster Banner" width="100%" />
</p>

# 🔥 Bean-Roaster

> **Product Discovery, Socratic Alignment, Domain Modeling, and PRD Synthesis Engine for Antigravity SDLC pipelines (Stages 0–2).**

---

## ☕ Why "The Roaster"? (The Metaphor Explained)

<p align="center">
  <img src="assets/sketch.png" alt="Bean-Roaster Fun Sketch" width="480px" />
</p>

In coffee production, raw green coffee beans are dense, hard, and flavorless. You cannot grind or brew them in their raw state. They must first undergo controlled thermal profiling in the roaster—developing body, caramelizing sugars, and unlocking aromatic complexity.

In software engineering, raw feature requests and initial user prompts are the green beans: vague, full of hidden assumptions, and unready for implementation. 

**`bean-roaster`** is the roasting chamber of our swarm:
- It takes raw, ambiguous ideas and subjects them to rigorous Socratic grilling.
- It identifies user personas, core friction points, and domain boundaries.
- It bakes unassailable product requirements (`02_PRD.md`), establishes a ubiquitous domain language (`docs/glossary.md`), and subjects the design to adversarial red-team stress testing before a single line of application code is written.

---

## 🏛️ Origin & Architectural Rationale

### Spawned from `bean-to-cup`
**`bean-roaster`** was extracted from the monolithic [`bean-to-cup`](https://github.com/sapientcoffee/bean-to-cup) repository as part of a modular decomposition of the Antigravity barista swarm.

### Why Decompose?
1. **Dedicated Product Focus:** Product managers, solutions architects, and designers can use `bean-roaster` for rapid discovery and specification without pulling in bulky code generators, test runners, git worktree managers, or SRE tooling.
2. **Reduced Context Footprint:** Isolates requirements-gathering prompts, Socratic interview templates, and red-team auditing rules from unrelated implementation baggage.
3. **Strict Stage Boundary ("No Spec, No Code"):** Clear physical separation between the discovery phase (`bean-roaster`) and implementation phase (`bean-brewer`) reinforces architectural discipline: code is never written without an approved, hardened PRD.
4. **Markdown Contract Handoff:** Produces version-controlled, human-readable markdown artifacts (`00_IDEATION.md`, `docs/glossary.md`, `02_PRD.md`) that hand off seamlessly to `bean-brewer` and `bean-cup`.

---

## 🚀 Capabilities & Skills Reference

| Stage | Skill / Agent | Description |
| :---: | :--- | :--- |
| **0** | **`ideator` (`skills/ideator`)** | Explores problem friction, identifies user personas, maps Critical User Journeys (CUJs), and synthesizes initial data schemas into `00_IDEATION.md`. |
| **1** | **`grill` (`skills/grill`)** | Conducts a relentless Socratic interview to challenge architectural assumptions, clarify edge cases, and auto-generate `docs/glossary.md` and Architecture Decision Records (`docs/adr/`). |
| **1.5** | **`domain-modeling` (`skills/domain-modeling`)** | Defines ubiquitous terminology, entity boundaries, and bounded contexts to prevent domain leakage. |
| **2** | **`write-prd` (`skills/write-prd`)** | Synthesizes an executive-grade Product Requirements Document (`02_PRD.md`) with explicit Non-Goals, measurable KPIs, and acceptance criteria. |
| **2.5** | **`@red-team-reviewer` (`agents/red-team-reviewer.md`)** | Dispatches an adversarial subagent to audit the PRD for security flaws, race conditions, unhandled failure modes, and KPI ambiguities before human sign-off. |
| **—** | **`feature` (`skills/feature`)** | Orchestrator skill initializing versioned plan directories (`plans/<feature>/<timestamp>/`) and coordinating Stages 0 through 2. |

---

## 🔄 Detailed Discovery & Alignment Workflow

```mermaid
flowchart TD
    subgraph Inputs["💡 Raw Inputs"]
        UserGoal["Raw User Goal / Feature Prompt"]
        ExistingRepo["Existing Repository Context"]
    end

    subgraph Stage0["Stage 0: Discovery & Ideation (/ideator)"]
        FrictionAnalysis["Persona Friction Analysis"]
        CUJMapping["Critical User Journey (CUJ) Mapping"]
        DraftDataModel["Initial Entity & Schema Drafting"]
        EmitIdeation["Emit: 00_IDEATION.md"]
    end

    subgraph Stage1["Stage 1: Socratic Alignment (/grill)"]
        InterviewLoop{"Socratic Interview Engine<br/>Relentless Grilling Loop"}
        Clarify["Clarify Edge Cases & Failure Modes"]
        Glossary["Ubiquitous Language Builder<br/>Emit: docs/glossary.md"]
        ADR["Architecture Decisions<br/>Emit: docs/adr/"]
        Domain["Domain Modeling Boundary Checks<br/>(skills/domain-modeling)"]
    end

    subgraph Stage2["Stage 2: PRD Synthesis (write-prd)"]
        SynthesizePRD["Assemble PRD Structure"]
        NonGoals["Explicit Non-Goals & Out-of-Scope"]
        ExecutableKPIs["KPI Definitions<br/>Emit: evals/test_kpis.py"]
        EmitPRD["Emit: 02_PRD.md"]
    end

    subgraph RedTeam["Stage 2.5: Adversarial Audit (@red-team-reviewer)"]
        AdversarialScan["Red-Team Reviewer Subagent"]
        ChecklistReview["Audit for KPI Ambiguity,<br/>Race Conditions & Security Holes"]
        RedTeamVerdict{"Red-Team Audit Verdict"}
        RefineLoop["Refine PRD Requirements"]
    end

    subgraph Gate["🛑 Stage 2.9: Human Review Gate"]
        HumanSignoff{"User Explicit Sign-Off"}
        Rejected["Revise Requirements"]
        Approved["PRD Approved & Frozen"]
    end

    subgraph Handoff["🚀 Downstream Handoff"]
        HandoffBrewer["Hand off 02_PRD.md to bean-brewer<br/>(Specification & Implementation)"]
        SyncDashboard["Opportunistic Telemetry Sync<br/>(sync_dashboard_if_available.py ➔ bean-cup)"]
    end

    UserGoal & ExistingRepo --> FrictionAnalysis
    FrictionAnalysis --> CUJMapping --> DraftDataModel --> EmitIdeation
    EmitIdeation --> InterviewLoop
    InterviewLoop --> Clarify
    Clarify --> Glossary & ADR & Domain
    Glossary & ADR --> SynthesizePRD
    SynthesizePRD --> NonGoals --> ExecutableKPIs --> EmitPRD
    EmitPRD --> AdversarialScan
    AdversarialScan --> ChecklistReview --> RedTeamVerdict
    RedTeamVerdict -->|Deficiencies Found| RefineLoop --> SynthesizePRD
    RedTeamVerdict -->|Passed Clean| HumanSignoff
    HumanSignoff -->|Changes Requested| Rejected --> InterviewLoop
    HumanSignoff -->|Approved| Approved
    Approved --> HandoffBrewer
    EmitIdeation & EmitPRD -.-> SyncDashboard
```

---

## 🔌 Decoupled Telemetry

`bean-roaster` includes an opportunistic telemetry script (`scripts/sync_dashboard_if_available.py`):
- If `bean-cup` is installed in the workspace or plugin path, it automatically syncs updates to `visual-dashboard.html`.
- If `bean-cup` is absent, the script exits silently with code 0 without interrupting execution.

---

## 📦 Installation

```bash
# Install to local Antigravity plugin registry
./install.sh

# Or install via agy CLI
agy plugin install .
```

---

## 📜 License
Apache-2.0 - Copyright 2026 Google LLC.
