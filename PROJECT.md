# Gemini Research: Cross-LLM Prompt Engineering Framework

**Created:** 2025-11-13 23:00 AEDT  
**Purpose:** Multi-LLM collaboration repository for building, enhancing, and using complex Gemini research prompts  
**Target Users:** ChatGPT, Claude Desktop, and other LLMs  
**Foundation:** Enhanced version of Gemini Research Method

---

## Strategic Context

### Vision
Create a universal framework enabling any LLM to:
1. Understand Gemini's research capabilities (1M context, fast, free, detailed)
2. Generate effective research prompts using proven methodologies
3. Enhance existing prompts based on empirical findings
4. Collaborate across platforms to improve the method

### Core Value Proposition
- **For LLMs:** Clear specifications → effective Gemini research prompts
- **For Users:** Leverage Gemini's strengths without deep prompt engineering
- **For Research:** Systematic, reproducible, high-quality outputs (9-10/10)

### Current Status
**Phase:** Foundation - Initial setup and source material review
**Next:** Complete review of Gemini Research Method → enhance → document

### Solution Architecture

**Repository Structure:**
```
docs/
├── methodology/     - Core principles, templates, patterns (WEB UI FOCUS)
│   ├── principles/  - Proven techniques, anti-patterns
│   ├── templates/   - Web UI prompt templates (prose-optimized)
│   └── patterns/    - Reusable prompt patterns
├── api/             - API-specific content (SECONDARY)
│   ├── templates/   - JSON-based API prompts
│   └── validators/  - Quality validation tools
├── reference/       - Gemini capabilities, API specs, benchmarks
├── guides/          - How-to guides for different LLMs
├── analysis/        - Research findings, evaluations, comparisons
└── enhancements/    - Proposed improvements, experimental features
```

**Key Principles:**
1. **Cross-Platform Clarity:** Documentation readable by any LLM
2. **Evidence-Based:** All claims backed by testing/sources
3. **Template-Ready:** Practical, copy-paste solutions
4. **Progressive Enhancement:** Start simple, scale complexity
5. **Collaborative Evolution:** Open to contributions from any LLM

### Critical Distinction: Two Execution Paths

**PATH 1: WEB UI (Primary Use Case)**
- **Interface:** Gemini Deep Research Web UI (google.com/gemini)
- **Method:** Copy/paste generated prompt
- **Output:** Human-readable prose (1,500-2,000 lines)
- **Use Case:** Interactive research, reading, analysis
- **Template:** Comprehensive or Strategic Decision formats
- **Example:** v1.5 generator style from source material

**PATH 2: API (Programmatic Use Case)**
- **Interface:** Gemini API programmatic calls
- **Method:** Direct API execution via application
- **Output:** Structured JSON for automation
- **Use Case:** Automated validation, integration, pipelines
- **Template:** JSON schema-enforced formats
- **Example:** v4.8.1 style from source material

**THESE ARE FUNDAMENTALLY DIFFERENT:**
- Web UI = prose for humans to read and understand
- API = structured data for machines to process
- Web UI = interactive, exploratory, comprehensive
- API = automated, repeatable, validation-focused

**Default:** This framework primarily targets **PATH 1 (Web UI)** unless explicitly stated otherwise. API path is secondary for automation scenarios.

### Core Workflow (Web UI Primary)
1. **LLM reads** methodology docs → understands Gemini capabilities
2. **LLM receives** user research requirements  
3. **LLM generates** Web UI prompt using templates (prose-optimized)
4. **User copies/pastes** into Gemini Deep Research
5. **Gemini executes** → returns comprehensive prose output
6. **LLM learns** from results → enhances method

---

## Decision Log

### Decision #002 - 2025-11-13 23:05 AEDT
**Context:** Two distinct execution paths need clear separation  
**Decision:** Framework primarily targets Web UI copy/paste (PATH 1), with API automation as secondary (PATH 2)  
**Rationale:**  
- Web UI is primary user workflow (interactive research)
- API is for automation/validation scenarios
- Different output formats (prose vs JSON)
- Different optimization strategies
- Mixing them creates confusion

**Impact:**  
- Methodology docs focus on Web UI templates
- API content isolated in docs/api/
- Clear PATH 1 vs PATH 2 labels throughout
- Default examples use Web UI approach

### Decision #001 - 2025-11-13 23:00 AEDT
**Context:** Project initialization  
**Decision:** Adopt standard ClaudeWorkflow project structure with cross-LLM focus  
**Rationale:**  
- Proven structure for complex projects
- Enables systematic documentation
- Git-based collaboration model
- Clear handover between sessions

**Impact:**  
- Use docs/ hierarchy for content organization
- Maintain PROJECT.md and SESSION.md
- Follow commit conventions
- Enable smooth ChatGPT/Claude collaboration

---

## Core Principles

### From Source Research
1. **Instruction Adherence Trade-off:** Explicit structure vs intelligent optimization
2. **Technique Combinations:** 4-6 complementary techniques optimal
3. **Evidence Quality:** Tier system (Official > Production > Community > Anecdotal)
4. **Self-Enhancement:** Build quality gates and refinement loops
5. **Thinking Budget:** Explicit allocation for complex reasoning

### Cross-LLM Collaboration
1. **Universal Documentation:** Clear for ChatGPT, Claude, others
2. **No Assumptions:** Explicit context, no implied knowledge
3. **Examples Over Theory:** Show working implementations
4. **Version Everything:** Track evolution of methodology
5. **Test, Document, Share:** Empirical validation required

---

## Technology Stack

**Foundation Materials:**
- Gemini Research Method (source: `/Users/dudley/Projects/Gemini Research Method/`)
  - 01_PRINCIPLES.md (370 lines)
  - 02_TEMPLATES.md (613 lines)  
  - 03_APPLICATIONS/ (v4.8.1 + validators)
  - Source research documents

**Target Platform:**
- Gemini 2.5 Pro (1M context, Thinking mechanism, grounding)
- API and Deep Research UI interfaces

**Documentation Tools:**
- Markdown for universal readability
- JSON schemas for structured data
- Git for version control
- GitHub for collaboration

---

## References

**Source Repository:**  
- `/Users/dudley/Projects/Gemini Research Method/`
- Complete methodology development history
- Proven templates achieving 9-10/10 quality
- Empirical findings from capability assessments

**Key Documents to Review:**

**PATH 1 (Web UI) Focus:**
- README.md - Infrastructure overview and knowledge chain
- 01_PRINCIPLES.md - Meta-learnings and proven techniques (370 lines)
- 02_TEMPLATES.md - Production-ready Web UI templates (613 lines)
  - Template A: Comprehensive Foundation Research (1,500-2,000 lines)
  - Template B: Strategic Decision Research (500-800 lines)

**PATH 2 (API) Reference:**
- 03_APPLICATIONS/v4.8.1_api_prompt.md - JSON API implementation (331 lines)
- 03_APPLICATIONS/quality_validator.py - Automated quality scoring (359 lines)
- 03_APPLICATIONS/traceability_validator.py - Confidence validation (330 lines)

**Background (Context Only):**
- Source assessments (capability testing - for reference, not direct read)

---

**Last Strategic Update:** 2025-11-13 23:00 AEDT  
**Current Phase:** Foundation
