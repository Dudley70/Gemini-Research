# Research Prompt Framework Guide
Version: 1.3.0 · Date: 2025-11-12

## Purpose
Deterministic composition of research prompts that share a common skeleton (Phases/Parts/Gates) while adapting Socratic questions, scoring, and quality gates per **research_type**.

## Non-Negotiables (all research types)
- Emit **one** continuous Markdown document.
- Use **tables first** for formulas, thresholds, IO contracts, dependencies, and actions.
- Name fields as `paper.element.field` and include **units** and **timing** (event/compute/cash).
- Provide **self-score** and apply **quality gates** before finalizing.
- Append a **Compliance Report JSON** (see `COMPLIANCE_REPORT_SCHEMA.json`).

## Standard Sections
1. **Phase 1 — Technical Components** (8 topics minimum)
2. **Phase 2 — Critical Synthesis (Socratic)** — Stage 1 Scrutiny · Stage 2 Perspectives · Stage 3 Gaps
3. **Part B — Self-Scoring Assessment** (7 criteria, 0–10 scale)
4. **Part C — Self-Enhancement (Quality Gates)** — Gate 0 (Preflight), Gate 1, Gate 2, Gate 3
5. **Success Criteria & Verification Checklist**
6. **Outcome**

## Gate 0 — Preflight (run before publish)
Proceed only if:
- Global compute order declared (e.g., **P2 → P1 → P7**) and any loops broken (e.g., **t−1** rule).
- **Source-of-Truth (SoT)** identified for every dependency.
- **IO Contracts**, **Validation Matrix**, **Error Handling Matrix** present where applicable.
- Worked **examples/stress tests** requested and summarized.
- **Compliance Report JSON** appended and indicates pass.

## Determinism Rules
- Explicit variable names, units, and order of operations.
- For time-based outputs: **Y1 monthly** + **Y1–Y5 roll-ups** (where applicable).
- Thresholds always include **alert levels** and **actions**.
