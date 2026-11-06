# ☕ Bean-Roaster

> **Product Discovery, Cupping Form & Socratic Requirements Engine (Stages 0, 1, 3).**

---

## ☕ Why "The Roaster"?

Before raw green coffee beans can be brewed into an espresso, they must be roasted to bring out aroma, acidity, and complex flavor profiles. In software engineering, **`bean-roaster`** takes raw, ambiguous ideas or feature requests and roasts them into hardened, well-structured, testable Product Requirements Documents (`03_PRD.md`) using isolated subagents that keep the main orchestrator (`@expo`) within the `< 100K` Smart Zone.

---

## 🚀 Capabilities, Skills & Subagents

| Stage | Skill | Delegated Subagents | Description |
| :---: | :--- | :--- | :--- |
| **0** | **`ideator` (`skills/ideator`)** | `@product-ideator`, `@copy-editor` | Green Bean Selection: Dispatches `@product-ideator` via `invoke_subagent` to explore problem space, persona friction, CUJs, ADK topologies, and mock JSON schemas into `.scratch/<id>/00_IDEATION.md`. |
| **1** | **`cupping-form` & `grill`** | `@question-formulator` | Cupping Form & Dial-In: `cupping-form` dispatches `@question-formulator` via `invoke_subagent` to emit blind technical questions (`01_QUESTIONS.md`) with zero solution leakage before pausing via `ask_question`. `grill` conducts a relentless Socratic interview to produce `.scratch/<id>/02_EXTRACTION.md`, `docs/CONTEXT.md`, `docs/glossary.md`, and proposed ADRs (`docs/adr/`). |
| **3** | **`write-prd` (`skills/write-prd`)** | `@prd-author`, `@copy-editor`, `@threat-modeler` | First Crack / PRD Synthesis: Orchestrates `@prd-author` (drafting `.scratch/<id>/03_PRD.md` with numbered `AC1..ACN` and `evals/test_kpis.py`), `@copy-editor` (purification), and `@threat-modeler` (OWASP ASVS L2 audit from `bean-core`). |

---

## 🛠️ Testing

```bash
python3 -m unittest discover -s tests -v
```
