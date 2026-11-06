# ☕ Bean-Roaster

> **Product Discovery, Cupping Form & Socratic Requirements Engine (Stages 0, 1, 3).**

---

## ☕ Why "The Roaster"?

Before raw green coffee beans can be brewed into an espresso, they must be roasted to bring out aroma, acidity, and complex flavor profiles. In software engineering, **`bean-roaster`** takes raw, ambiguous ideas or feature requests and roasts them into hardened, well-structured, testable Product Requirements Documents (`03_PRD.md`).

---

## 🚀 Capabilities & Stages

| Stage | Skill / Agent | Description |
| :---: | :--- | :--- |
| **0** | **`ideator` (`skills/ideator`)** | Green Bean Selection: Explores problem space, persona friction, and user journeys. Emits `.scratch/<id>/00_IDEATION.md`. |
| **1** | **`cupping-form` & `grill`** | Cupping Form & Dial-In: Emits blind technical questions (`01_QUESTIONS.md`) with zero solution leakage, and conducts a relentless Socratic interview to produce context notes, glossary terms, and proposed ADRs (`docs/adr/`). |
| **3** | **`write-prd` & `@copy-editor`** | First Crack / PRD Synthesis: Compiles numbered acceptance criteria (`AC1..ACN`), user stories, and measurable metrics into `03_PRD.md`. Purified by `@copy-editor` and audited by `@threat-modeler` (from `bean-core`). |

---

## 🛠️ Testing

```bash
python3 -m unittest discover -s tests -v
```
