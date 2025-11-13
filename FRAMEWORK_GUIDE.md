# Framework Guide: Cross-LLM Prompt Engineering for Gemini

**Created:** 2025-11-14 00:25 AEDT  
**Purpose:** Entry point for LLMs (ChatGPT, Claude, etc.) to understand and use this framework  
**Read This First:** Before accessing any other documentation

---

## What This Framework Is

**A comprehensive reference library** enabling any LLM to generate effective research prompts for Gemini 2.5 Pro.

**Based on:** 1,582 lines of academic research papers testing 12 prompting techniques empirically

**Provides:**
- ✅ What Gemini can do (capabilities, API parameters, limitations)
- ✅ Which techniques work best (effectiveness + reliability scores)
- ✅ How to combine techniques (compatibility matrix)
- ✅ Production-ready templates (comprehensive research, strategic decisions)
- ✅ Implementation examples (concrete code and patterns)

**NOT a tool or API** - this is documentation that LLMs read to learn how to generate Gemini prompts.

---

## Quick Start: 3-Minute Overview

### For LLMs Reading This

**Your Task:** Help users generate effective Gemini research prompts

**Simple Process:**
1. **Understand Gemini** → Read `gemini_capabilities.md` (what can it do?)
2. **Select Techniques** → Read `technique_library.md` (which techniques for this task?)
3. **Apply Template** → Read `web_ui_templates.md` (Template A or B?)
4. **Generate Prompt** → Customize for user's specific need
5. **Deliver** → Provide complete prompt user can copy/paste into Gemini

**Expected Result:** User pastes prompt into Gemini Deep Research → Gets high-quality research output (1,500-2,000 lines for comprehensive, 500-800 for strategic)

---

### For Users Reading This

**What You Get:** Research prompts optimized for Gemini 2.5 Pro

**How It Works:**
1. Ask your LLM (ChatGPT, Claude, etc.): "Generate a Gemini research prompt for [topic]"
2. LLM reads this framework → generates customized prompt
3. You copy prompt → paste into Gemini at google.com/gemini
4. Gemini executes research → returns comprehensive analysis

**Quality Standard:** Framework techniques consistently produce 9-10/10 outputs when applied correctly

---

## Repository Structure

### Core Methodology (Read These First)

**1. `docs/reference/gemini_capabilities.md` (696 lines)**
- **What:** Complete reference on Gemini 2.5 Pro capabilities
- **When to Read:** Every time - understand what Gemini can do
- **Contains:**
  - Architecture (MoE transformer, 1M context, thinking mechanism)
  - 12 tested techniques with effectiveness/reliability scores
  - API parameters (thinkingBudget, includeThoughts, responseSchema, tools)
  - Native capabilities and limitations
  - Best practices for prompt generation

**2. `docs/reference/technique_library.md` (1,438 lines)**
- **What:** Complete catalog of all 17 prompting techniques
- **When to Read:** For technique selection and implementation details
- **Contains:**
  - 12 tested techniques (Tier 1: API-enforced, Tier 2: Emergent, Tier 3: Promising)
  - 5 gap techniques (identified but not tested for Gemini)
  - For each: Definition, scores, when to use, implementation examples, compatibility, pitfalls
  - Compatibility matrix (which techniques work together)
  - Selection guide by use case and priority

**3. `docs/methodology/templates/web_ui_templates.md` (899 lines)**
- **What:** Production-ready prompt templates
- **When to Read:** When generating actual prompts
- **Contains:**
  - Template A: Comprehensive Foundation Research (1,500-2,000 line outputs)
  - Template B: Strategic Decision Analysis (500-800 line outputs)
  - Thinking mechanism explanation
  - Technique patterns (Socratic, Quality Gates, Multi-Agent)
  - Self-scoring rubric and enhancement protocols

**4. `docs/methodology/principles/core_discoveries.md` (413 lines)**
- **What:** Why techniques work and how to combine them
- **When to Read:** For deeper understanding of principles
- **Contains:**
  - Instruction adherence vs output quality trade-off
  - Tier 1/2/3 technique classifications with evidence
  - Optimal technique stacks for different research types
  - Anti-patterns and compatibility matrix
  - Phrasing patterns for instruction adherence

---

### Integration Guides (Read for Specific Workflows)

**5. `docs/enhancements/unified_methodology.md` (684 lines)**
- **What:** How Claude and ChatGPT branches complement each other
- **When to Read:** Understanding different approaches and combining them
- **Contains:**
  - Branch comparison (Claude's docs vs ChatGPT's automation)
  - Hybrid approach examples
  - PATH 1 (Web UI) vs PATH 2 (API) integration
  - Combined validation strategies
  - Decision matrix for choosing approaches

**6. `docs/guides/for_claude.md`** (pending - Phase 2)
- **What:** How Claude should use this framework
- **Contains:** Reading order, workflow examples, ClaudeWorkflow integration

**7. `docs/guides/for_chatgpt.md`** (pending - Phase 2)
- **What:** How ChatGPT should use this framework
- **Contains:** Reading order, Custom GPT integration, ChatGPT v1.3.0 Pack usage

---

### Reference Materials (Consult as Needed)

**8. `docs/analysis/source_papers_complete_analysis.md` (255 lines)**
- **What:** Complete analysis of the two foundation papers
- **When to Read:** For evidence base and research foundation
- **Contains:**
  - Summary of both papers (1,582 lines of research)
  - 12 techniques tested with scores
  - What each branch extracted
  - Critical gaps identified

**9. `docs/reference/source_materials/`** (2,431 lines)
- **What:** Original source materials archived for reference
- **When to Read:** Verification, historical context, comparison
- **Contains:**
  - Original 01_PRINCIPLES.md and 02_TEMPLATES.md
  - Source papers (Gemini Pro Prompting Capability Assessment + Self-Assessment)
  - Explanation of relationship to adapted content

**10. `docs/api/applications/`** (1,020 lines)
- **What:** API-focused implementations (PATH 2)
- **When to Read:** For programmatic/automated use cases
- **Contains:**
  - v4.8.1 API prompt with 4 presets
  - quality_validator.py (automated quality scoring)
  - traceability_validator.py (confidence validation)

---

## Reading Order by Role

### If You're an LLM Generating Prompts

**Essential (Read Every Time):**
1. ✅ `gemini_capabilities.md` - Understand what Gemini can do
2. ✅ `technique_library.md` - Select 4-6 compatible techniques
3. ✅ `web_ui_templates.md` - Apply Template A or B

**Reference (Consult as Needed):**
4. `core_discoveries.md` - Understand why techniques work
5. `unified_methodology.md` - Learn different approaches
6. `for_claude.md` or `for_chatgpt.md` - LLM-specific guidance

**Total Reading:** ~3,000 lines (capabilities + techniques + templates)

---

### If You're a User Learning the Framework

**Start Here:**
1. ✅ This document (FRAMEWORK_GUIDE.md) - Overview
2. ✅ `gemini_capabilities.md` - What Gemini can do
3. ✅ `web_ui_templates.md` - See example templates

**Go Deeper:**
4. `technique_library.md` - Learn individual techniques
5. `core_discoveries.md` - Understand principles
6. `unified_methodology.md` - Compare approaches

**Reference:**
7. `source_papers_complete_analysis.md` - Evidence base
8. LLM-specific guides when available

---

### If You're Building on This Framework

**Foundation:**
1. ✅ `source_papers_complete_analysis.md` - Understand research base
2. ✅ `core_discoveries.md` - Principles and evidence
3. ✅ `gemini_capabilities.md` - Technical specifications

**Implementation:**
4. `technique_library.md` - All techniques documented
5. `web_ui_templates.md` - Template patterns
6. `unified_methodology.md` - Integration strategies

**Extensions:**
7. `api/applications/` - API automation examples
8. `source_materials/` - Original materials for verification

---

## Workflow Examples

### Example 1: LLM Generates Research Prompt

**User Request:** "Generate a Gemini research prompt for analyzing microservices architecture patterns"

**LLM Process:**

**Step 1: Understand Gemini's Capabilities**
```
Read: gemini_capabilities.md
Key findings:
- 1M token context (can handle extensive analysis)
- Thinking mechanism (activate with "Let's think step by step")
- Chain-of-Thought: 10/10 effectiveness, 10/10 reliability
- Multi-Agent Simulation: 10/10 effectiveness, 9/10 reliability
- Long-Context Reasoning: 10/10 effectiveness, 8/10 reliability
```

**Step 2: Select Techniques**
```
Read: technique_library.md (selection guide)
For comprehensive research, select:
1. Chain-of-Thought (foundation - always use)
2. Socratic Questioning (critical analysis)
3. Multi-Agent Simulation (multiple perspectives)
4. Self-Scoring (quality assurance)
5. Quality Gates (standards enforcement)
6. Long-Context (comprehensive synthesis)
Total: 6 techniques (optimal range: 4-6)
```

**Step 3: Apply Template**
```
Read: web_ui_templates.md
Choose: Template A (Comprehensive Foundation Research)
Reason: Systematic coverage needed for architecture patterns

Customize:
- Replace [TOPIC] with "Microservices Architecture Patterns"
- Define 18 questions covering patterns, trade-offs, implementations
- Add Socratic analysis for critical thinking
- Include Multi-Agent (Developer, Architect, Operations perspectives)
- Set self-scoring rubric (7 criteria, 0-10 scale)
- Define quality gates for pattern completeness
```

**Step 4: Generate Complete Prompt**
```markdown
# Microservices Architecture Patterns: Comprehensive Research

## ROLE DEFINITION
You are a senior software architect specializing in distributed systems...

[Complete customized prompt based on Template A with all 6 techniques integrated]

## SUCCESS CRITERIA
- ✅ 18 questions answered (200+ words each)
- ✅ 12+ implementation patterns extracted
- ✅ Multi-perspective analysis complete
- ✅ Self-scored ≥8.5/10
...
```

**Step 5: Deliver to User**
```
Here's your Gemini research prompt. Copy the entire text below and paste it into 
Gemini Deep Research at google.com/gemini

Expected output: 1,500-2,000 lines of comprehensive analysis covering:
- Core microservices patterns with examples
- Trade-offs and decision criteria  
- Multiple expert perspectives
- Implementation guidance
- Quality self-assessment

[PROMPT TEXT]
```

---

### Example 2: Strategic Decision Research

**User Request:** "Should we migrate from monolith to microservices?"

**LLM Process:**

**Step 1: Recognize Decision Context**
```
This is a strategic decision → Use Template B
Read: web_ui_templates.md (Strategic Decision Analysis)
```

**Step 2: Select Decision-Focused Techniques**
```
Read: technique_library.md (selection guide for strategic decisions)
Select:
1. Chain-of-Thought (structured analysis)
2. Multi-Agent (stakeholder perspectives)
3. Tree of Thoughts (explore multiple approaches)
4. Socratic Questioning (challenge assumptions)
5. Self-Scoring (evaluate recommendation quality)
Total: 5 techniques
```

**Step 3: Customize Template B**
```
- Define decision clearly: "Migrate to microservices: Yes/No/Hybrid?"
- Current state: Monolith serving 10K users
- Constraints: Team of 5 developers, 6-month timeline
- Success criteria: Scalability + manageable complexity
- Options: Stay monolith, full microservices, hybrid (2-3 services)
- Perspectives: Developer, Operations, Product stakeholders
```

**Step 4: Generate & Deliver**
```
Customized Template B prompt with:
- Clear recommendation requirement (not "it depends")
- Options analysis with pros/cons
- Stakeholder perspectives (3 distinct views)
- Consequence forecasting (short/medium/long-term)
- Implementation patterns
- Quality self-scoring
```

**Expected Output:** 500-800 lines with clear recommendation backed by analysis

---

## Key Concepts

### PATH 1 vs PATH 2

**PATH 1: Web UI (Copy/Paste) - PRIMARY**
- Interface: Gemini Deep Research at google.com/gemini
- Method: User copies generated prompt → pastes into web interface
- Output: Human-readable prose (1,500-2,000 lines for comprehensive research)
- Templates: Template A & B from `web_ui_templates.md`
- Use Cases: Interactive research, learning, strategic analysis

**PATH 2: API (Programmatic) - SECONDARY**
- Interface: Gemini API via code
- Method: Direct API execution from application
- Output: Structured JSON for automation
- Templates: v4.8.1 API prompt from `api/applications/`
- Use Cases: Automated validation, batch processing, integration pipelines

**This framework primarily targets PATH 1** (Web UI) unless explicitly stated.

---

### Technique Tiers

**Tier 1: API-Enforced (Highest Reliability)**
- JSON Schema Validation, Grounding, Meta-Reasoning, Thinking Mode Control
- Hard constraints enforced by API parameters
- 9-10/10 reliability scores
- Use when: Format or feature is critical requirement

**Tier 2: Emergent High-Reliability (Prompt-Dependent)**
- CoT, Socratic, Multi-Agent, Self-Scoring, Quality Gates, Iterative Improve, Long-Context
- Effectiveness depends on prompt structure quality
- 8-10/10 reliability when well-structured
- Use when: Quality and depth are priorities

**Tier 3: Promising (Lower Reliability)**
- Tree of Thoughts
- Must be simulated through prompting (not native feature)
- 7/10 reliability
- Use when: Creative exploration needed, reliability less critical

**Gap Techniques (Not Yet Tested for Gemini)**
- Self-Consistency, ReAct, Few-Shot, Generated Knowledge, Directional Stimulus
- Known to work in general LLM research
- Need Gemini-specific validation
- Use with caution until tested

---

### Quality Standards

**Target Score:** ≥8.5/10 average across 7 criteria

**7 Criteria:**
1. Completeness (all questions answered fully)
2. Evidence Quality (authoritative sources)
3. Depth of Analysis (mechanisms, edge cases, trade-offs)
4. Pattern Quality (immediately usable)
5. Critical Thinking (assumptions questioned)
6. Integration (connections across findings)
7. Actionability (clear next steps)

**Enhancement Protocol:**
- < 8.0: Critical refinement required
- 8.0-8.9: Targeted enhancement recommended
- ≥ 9.0: Optional advanced insights

---

## Common Pitfalls

### For LLMs Generating Prompts

❌ **Don't:**
- Generate prompts without reading capabilities first
- Combine >6 techniques (cognitive overload)
- Use techniques incompatibly (check compatibility matrix)
- Create prompts from scratch (adapt templates instead)
- Mix PATH 1 and PATH 2 approaches (choose one)

✅ **Do:**
- Always start with `gemini_capabilities.md`
- Select 4-6 compatible techniques from `technique_library.md`
- Adapt Template A or B from `web_ui_templates.md`
- Include thinking triggers ("Let's think step by step")
- Provide clear success criteria

---

### For Users

❌ **Don't:**
- Expect LLM to remember framework across sessions (reload docs each time)
- Mix Web UI prompts with API execution (different formats)
- Skip quality self-scoring in prompts (reduces output quality)
- Request too many techniques (>6 = diminishing returns)

✅ **Do:**
- Ensure LLM has access to framework docs
- Specify whether you want PATH 1 (Web UI) or PATH 2 (API)
- Copy complete generated prompt (don't modify unless you understand techniques)
- Paste into Gemini Deep Research at google.com/gemini
- Expect 1,500-2,000 lines for comprehensive, 500-800 for strategic

---

## Framework Statistics

**Documentation Size:**
- Core Methodology: 3,446 lines
- Total Framework: 6,260 lines
- Evidence Base: 1,582 lines (source papers)

**Coverage:**
- 12 techniques tested empirically
- 5 gap techniques documented
- 2 production templates (A & B)
- 3 tier classifications
- 17 techniques total

**Quality:**
- Techniques consistently achieve 9-10/10 when properly applied
- Based on systematic academic research
- Validated through empirical testing
- Cross-platform (works with any LLM)

---

## Support & Resources

**Documentation Index:**
- See `docs/INDEX.md` for complete file listing

**Project Context:**
- See `PROJECT.md` for strategic context and decisions

**Session State:**
- See `SESSION.md` for current development status

**Recovery Guide:**
- See `CONTEXT_RESET_RECOVERY.md` for quick context recovery

**GitHub Repository:**
- https://github.com/Dudley70/Gemini-Research

---

## Version & Status

**Framework Version:** 1.0  
**Last Updated:** 2025-11-14 00:25 AEDT  
**Status:** Phase 1 Complete - Phase 2 In Progress

**Phase 1 (Complete):**
- ✅ Core discoveries documented
- ✅ Web UI templates created
- ✅ Gemini capabilities reference complete
- ✅ Technique library comprehensive
- ✅ Source materials archived

**Phase 2 (In Progress):**
- ✅ Unified methodology complete
- 🔄 LLM-specific guides (for_claude.md, for_chatgpt.md)
- 📋 Technique gap documentation (self_consistency.md, react_framework.md)
- 📋 Real-world examples

**Phase 3 (Planned):**
- Fill technique gaps with detailed documentation
- Create comprehensive examples
- Add before/after comparisons

**Phase 4 (Planned):**
- Update README.md with complete overview
- Create CONTRIBUTING.md for collaboration
- Final review and polish

---

## Quick Reference Card

**For LLMs: 5-Step Process**
1. Read `gemini_capabilities.md` → Know what Gemini can do
2. Read `technique_library.md` → Select 4-6 techniques
3. Read `web_ui_templates.md` → Choose Template A or B
4. Customize for user's specific need
5. Deliver complete prompt

**For Users: 3-Step Process**
1. Ask LLM: "Generate Gemini research prompt for [topic]"
2. Copy generated prompt → Paste into google.com/gemini
3. Receive comprehensive research (1,500-2,000 lines)

**Expected Quality:** 9-10/10 with proper technique application

---

**This document is your entry point. Start here, then navigate to specific docs as needed.**
