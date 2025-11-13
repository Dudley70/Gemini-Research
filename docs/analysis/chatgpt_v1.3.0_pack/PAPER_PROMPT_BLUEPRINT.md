# Gemini Deep Research Prompt: {{PAPER_TITLE}}

**Research Type:** {{RESEARCH_TYPE}}
**Thinking Budget:** {{THINKING_BUDGET|Maximum}}
**Expected Output:** {{EXPECTED_OUTPUT|2000–3000 lines of detailed specifications}}

---

## Research Context
{{RESEARCH_CONTEXT}}

{{#INTEGRATION_CONTEXT}}
## Integration Context
{{INTEGRATION_CONTEXT}}
{{/INTEGRATION_CONTEXT}}

---

## PHASE 1 — Technical Components
{{#PHASE1_TOPICS}}
### {{index}}  {{title}}
{{description}}
{{/PHASE1_TOPICS}}

---

## PHASE 2 — Critical Synthesis (Socratic)
### Stage 1 — Scrutinize Evidence
{{#SOCRATIC.stage1}}- {{.}}
{{/SOCRATIC.stage1}}
### Stage 2 — Alternative Perspectives
{{#SOCRATIC.stage2}}- {{.}}
{{/SOCRATIC.stage2}}
### Stage 3 — Identify Gaps
{{#SOCRATIC.stage3}}- {{.}}
{{/SOCRATIC.stage3}}

---

## PART B — Self-Scoring Assessment
| # | Criterion | Scoring Guide (0–10) |
|:--|:---------|:----------------------|
{{#SCORING_CRITERIA}}| {{index}} | **{{name}}** | {{descriptor|Use 10/7–9/4–6/0–3 pattern with type-specific focus}} |
{{/SCORING_CRITERIA}}

**Protocol:** Self-score → compute average → proceed to Part C based on gates.

---

## PART C — Self-Enhancement (Quality Gates)
{{#QUALITY_GATES}}- **{{name}} ({{condition}})** — {{actions}}
{{/QUALITY_GATES}}

---

## SUCCESS CRITERIA
{{#SUCCESS_CRITERIA}}- {{.}}
{{/SUCCESS_CRITERIA}}

---

## Verification Checklist
{{#VERIFICATION_CHECKLIST}}- [ ] {{.}}
{{/VERIFICATION_CHECKLIST}}

---

## Outcome
{{OUTCOME_SUMMARY}}

---

### Instructions to the LLM (Hidden if supported)
- Resolve placeholders using `RESEARCH_TYPE_SCHEMA.yaml` for `{{RESEARCH_TYPE}}`.
- Use `PROJECT_CONTEXT.yaml` thresholds/defaults where relevant.
- Emit a final **Compliance Report JSON** per `COMPLIANCE_REPORT_SCHEMA.json`.
