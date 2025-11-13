# Documentation Index

**Last Updated:** 2025-11-13 23:55 AEDT

This index tracks all documentation in the repository organized by category.

---

## Root Documents

- [PROJECT.md](../PROJECT.md) - Active - Strategic context, 3 decisions, complete principles
- [SESSION.md](../SESSION.md) - Active - Current state, next steps, technical notes
- [README.md](../README.md) - Active - Repository overview for GitHub
- [CONTEXT_RESET_RECOVERY.md](../CONTEXT_RESET_RECOVERY.md) - Active - **START HERE** for quick context recovery (205 lines)

---

## PATH 1: Web UI (Primary)

### Methodology (docs/methodology/)

**Principles** (docs/methodology/principles/)
- [core_discoveries.md](methodology/principles/core_discoveries.md) - Active - **ESSENTIAL** Proven techniques with evidence (413 lines)

**Templates** (docs/methodology/templates/)
- [web_ui_templates.md](methodology/templates/web_ui_templates.md) - Active - **PRODUCTION** Template A (Comprehensive) + Template B (Strategic Decision) (899 lines)

**Patterns** (docs/methodology/patterns/)
- Status: To be extracted from templates

---

## PATH 2: API (Secondary)

### API (docs/api/)

**Applications** (docs/api/applications/)
- [v4.8.1_api_prompt.md](api/applications/v4.8.1_api_prompt.md) - Reference - Self-contained API prompt with 4 presets (331 lines)
- [quality_validator.py](api/applications/quality_validator.py) - Reference - Automated quality assessment tool (359 lines)
- [traceability_validator.py](api/applications/traceability_validator.py) - Reference - Confidence validation tool (330 lines)

**Templates** (docs/api/templates/)
- Status: To be created - API-focused templates for programmatic use

**Validators** (docs/api/validators/)
- Status: See applications/ - validators already present

---

## Reference Materials (docs/reference/)

**Source Materials Archive** (docs/reference/source_materials/)
- [README.md](reference/source_materials/README.md) - Reference - Explains archived materials and their relationship to adapted content (209 lines)
- [01_PRINCIPLES.md](reference/source_materials/01_PRINCIPLES.md) - Reference - Original meta-learnings (370 lines)
- [02_TEMPLATES.md](reference/source_materials/02_TEMPLATES.md) - Reference - Original production templates (613 lines)
- **Source Papers** (reference/source_materials/papers/)
  - Gemini Pro Prompting Capability Assessment.md - Reference - Third-party evaluation (250 lines)
  - Gemini Prompting Capability Self-Assessment.md - Reference - Self-assessment research (1,332 lines)

**Note:** Source materials are read-only archives. Use adapted versions in docs/methodology/ for active work.

**Pending:**
- gemini_capabilities.md - Architecture, tested techniques, API features
- technique_library.md - All 17 techniques with examples

---

## Guides (docs/guides/)

- Status: To be created
- Purpose: LLM-specific how-to guides

---

## Analysis (docs/analysis/)

- [chatgpt_approach_analysis.md](analysis/chatgpt_approach_analysis.md) - Active - ChatGPT v1.3.0 pack review and integration recommendations (128 lines)
- [source_papers_complete_analysis.md](analysis/source_papers_complete_analysis.md) - Active - **CRITICAL** Complete analysis of both foundation papers (255 lines)
- **ChatGPT v1.3.0 Pack** (analysis/chatgpt_v1.3.0_pack/) - Reference - ChatGPT's prompt generation system (11 files)

---

## Enhancements (docs/enhancements/)

- Status: To be created
- Purpose: Proposed improvements, experimental features

---

## Notes

**Document Status:**
- **Active** - Current, maintained document
- **Reference** - Historical, archived, or comparative material (read-only)
- **Pending** - Planned, not yet created

**Workflow:**
1. Create new document in appropriate category
2. Add entry to this index with status
3. Update status as document evolves
4. Commit index updates with document changes
