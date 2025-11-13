# Gemini Research Infrastructure: Production Templates

**Phase:** 02 - Production-Ready Prompt Templates  
**Created:** 2025-10-07  
**Purpose:** Reference guide for crafting high-quality research prompts combining multiple advanced techniques  
**Source:** Same directory (Gemini Pro Prompting Capability Assessment + Self-Assessment research)
**Target:** Maximum quality output for complex research tasks

**Previous Step:** See `01_PRINCIPLES.md` - Core principles and meta-learnings that inform these templates

**Next Step:** See `03_APPLICATIONS/` - Practical applications of these templates (v4.8.1 API prompt + validators)

**Relationship in Chain:**
```
Source Research → 01_PRINCIPLES → 02_TEMPLATES (this doc) → 03_APPLICATIONS
```

This document provides practical operational framework with production-ready templates. The previous document extracts the empirical findings and technique classifications that inform these templates.

---

## Executive Summary

Gemini 2.5 Pro achieves optimal performance when prompts leverage its core architectural strengths and combine multiple advanced techniques. This framework provides a battle-tested structure for research prompts that consistently produce 9-10/10 quality outputs.

**Key Principle:** Structure prompts as complete, self-contained workflows that trigger Gemini's native "Thinking" mechanism and combine multiple high-reliability techniques.

---

## Part 1: Gemini 2.5 Pro Architecture - Core Strengths

### 1.1 The "Thinking" Mechanism (Critical Understanding)

**What It Is:**
- Internal reasoning process that occurs BEFORE final response generation
- Allocates computational "thinking budget" (128-32,768 tokens)
- Non-disablable for Pro model (always active)
- Performs meta-analysis of prompt complexity and auto-allocates resources

**How to Leverage:**
- Explicitly trigger with phrases: "Let's think step by step," "Show your reasoning," "Think deeply about"
- Set `thinkingBudget` parameter for depth control:
  - Default (-1): Dynamic allocation (Gemini decides)
  - 16384: High depth for complex analysis
  - 24576-32768: Maximum depth (slower, highest quality)
- Use `includeThoughts: true` to expose reasoning process

**Impact:**
- Higher thinking budget = demonstrably deeper analysis
- Benchmark validation: Thinking-enabled models significantly outperform non-thinking versions
- Best for: Complex reasoning, multi-step planning, strategic analysis

---

### 1.2 Native Capabilities (API-Level Support)

These capabilities are engineered features with high reliability:

| Capability | API Parameter | Reliability Score | Use Case |
|------------|---------------|-------------------|----------|
| **Structured Output** | `response_mime_type: "application/json"`<br>`responseSchema: {...}` | 9/10 | Data extraction, standardization, integration |
| **Grounding (Search)** | `tools: [GoogleSearch()]` | 9/10 | Current events, fact verification, citation-backed content |
| **Meta-Reasoning** | `includeThoughts: true` | 9/10 | Transparency, debugging, understanding model's approach |
| **Long Context** | 1M token window | 8/10 | Comprehensive document analysis, full codebase review |

**Critical Rule:** Always use API-level enforcement for mission-critical requirements. Don't rely on natural language instructions when a parameter exists.

---

### 1.3 Emergent Capabilities (High-Reliability Prompting Techniques)

These techniques leverage Gemini's architecture but require structured prompts:

| Technique | Effectiveness | Reliability | Primary Trigger |
|-----------|---------------|-------------|-----------------|
| **Chain-of-Thought (CoT)** | 10/10 | 10/10 | "Let's think step by step" |
| **Socratic Questioning** | 10/10 | 8/10 | Multi-stage critical thinking framework |
| **Multi-Agent Simulation** | 10/10 | 9/10 | Distinct persona definitions + role instructions |
| **Self-Scoring** | 10/10 | 9/10 | Objective rubric + evaluation instructions |
| **Quality Gates** | 10/10 | 9/10 | Conditional logic + few-shot examples |
| **Tree of Thoughts** | 9/10 | 7/10 | Explicit branching instructions + evaluation |
| **Iterative Self-Improvement** | 10/10 | 8/10 | Generate → Critique → Revise sequence |

**Key Insight:** These techniques achieve 9-10/10 effectiveness when properly structured. Quality depends heavily on prompt clarity.

---

## Part 2: Optimal Prompt Architecture Templates

### Template Selection Guide

| Template | Use Case | Output Length | Characteristics |
|----------|----------|---------------|-----------------|
| **A - Comprehensive** | Foundation topics, systematic coverage | 1,500-2,000 lines | Encyclopedic, multiple questions, high detail |
| **B - Strategic Decision** | Architectural decisions, recommendations | 500-800 lines | Synthesis-focused, clear recommendation, actionable |
| **C - Hybrid** | Complex topics needing knowledge + strategy | 800-1,200 lines | Foundation questions + strategic synthesis |

---

### Template A: Comprehensive Foundation Research

**Use When:** Building systematic knowledge, foundation topics, multiple aspects to cover

```markdown
# Topic [X]: [Name] - Comprehensive Research

## GEMINI CONFIGURATION
- Model: gemini-2.5-pro
- thinkingBudget: 24576
- includeThoughts: true

## ROLE DEFINITION
You are a senior research analyst specializing in [domain]. Your approach combines:
- Systematic investigation of all relevant aspects
- Evidence-based reasoning with source verification
- Pattern extraction for practical application
- Critical evaluation of findings

## PRIMARY RESEARCH TASK

### PHASE 1: SYSTEMATIC INVESTIGATION

**Instructions:** For each question below, think step by step:
1. Allocate thinking budget to map the question's scope
2. Provide detailed explanation (200+ words minimum)
3. Include minimum 2 concrete examples with context
4. Add code/configuration snippets where applicable
5. Provide source links for all claims
6. Question your own assumptions before finalizing

---

#### CLUSTER 1: [Core Concepts] (Questions 1-N)

**Q1: [Specific Question]**

Sub-components to address:
- [Aspect A]: [Guidance on what to explore]
- [Aspect B]: [Guidance on what to explore]
- [Aspect C]: [Guidance on what to explore]

**Required Output Structure:**
- **Overview:** High-level explanation
- **Deep Dive:** Detailed technical analysis
- **Examples:** Minimum 2 concrete cases with code/config
- **Best Practices:** Actionable guidance
- **Sources:** Links to documentation/research

**Thinking Trigger:** "Before answering Q1, think deeply about: What are the fundamental mechanisms? What are the edge cases? What do practitioners need to know?"

[Repeat structure for each question across 2-3 clusters]

---

### PHASE 2: CRITICAL SYNTHESIS

Using Socratic method, critically evaluate your Phase 1 findings:

#### Stage 1: Scrutinize Evidence
- What is the quality of sources used?
- Are there contradictions in the evidence?
- What assumptions underlie the findings?

#### Stage 2: Alternative Perspectives
Consider findings from viewpoint of:
- [Stakeholder A]: How do they evaluate this?
- [Stakeholder B]: What are their priorities?
- [Stakeholder C]: What concerns would they raise?

#### Stage 3: Identify Gaps
- What questions remain unanswered?
- Where is evidence weak or missing?
- What areas need deeper investigation?

---

### PHASE 3: PATTERN EXTRACTION

Extract 12+ template-ready, actionable patterns from your research.

**Pattern Quality Standard:**
Each pattern MUST include:
- **Name:** Clear, descriptive identifier
- **Context:** When to use vs alternatives
- **Structure:** Complete workflow with entry/exit conditions
- **Steps:** Numbered, actionable steps
- **Example:** Real code/config that works
- **Pitfalls:** Common mistakes to avoid

**Quality Gate:**
IF pattern lacks ANY required element → REFINE until complete
Patterns must be immediately usable by practitioners

---

## PART B: SELF-SCORING ASSESSMENT

Evaluate your research output against this objective rubric:

### Scoring Framework (0-10 scale for each criterion)

1. **Completeness:** Are all questions answered comprehensively?
   - 10: All questions fully answered with 200+ words, 2+ examples each
   - 7-9: Minor gaps in coverage or detail
   - 4-6: Several questions under-explored
   - 0-3: Major gaps or questions skipped

2. **Evidence Quality:** How strong and credible are sources?
   - 10: All claims backed by official docs, research papers, or proven patterns
   - 7-9: Most claims well-sourced, few rely on community/forums
   - 4-6: Mix of quality sources and weak evidence
   - 0-3: Many unsupported claims or low-quality sources

3. **Depth of Analysis:** How thoroughly are concepts explored?
   - 10: Covers mechanisms, edge cases, trade-offs, alternatives
   - 7-9: Good depth, minor aspects unexplored
   - 4-6: Surface-level in several areas
   - 0-3: Superficial treatment throughout

4. **Pattern Quality:** How usable are extracted patterns?
   - 10: All patterns complete (structure, steps, examples, context)
   - 7-9: Most patterns complete, minor refinement needed
   - 4-6: Patterns missing key elements
   - 0-3: Patterns too abstract or incomplete

5. **Critical Thinking:** How well are assumptions questioned?
   - 10: Evidence scrutinized, alternatives considered, gaps identified
   - 7-9: Good critical engagement, some areas accepted uncritically
   - 4-6: Limited critical analysis
   - 0-3: Accepts claims at face value

6. **Integration:** How well do findings connect across questions?
   - 10: Clear connections, cross-references, synthesized insights
   - 7-9: Good integration, some siloed sections
   - 4-6: Moderate integration
   - 0-3: Questions treated in isolation

7. **Actionability:** How immediately usable are recommendations?
   - 10: Clear next steps, template-ready patterns, implementation guidance
   - 7-9: Mostly actionable, minor gaps in guidance
   - 4-6: Some actionable elements, but requires significant adaptation
   - 0-3: Abstract recommendations without practical guidance

**Self-Scoring Instructions:**
1. Score each criterion objectively (0-10)
2. Calculate average across all criteria
3. Identify your 3 weakest criteria
4. Provide specific evidence for each score

---

## PART C: SELF-ENHANCEMENT PROTOCOL

Based on your self-scoring, execute the appropriate enhancement path:

### Enhancement Gate 1: Score < 8.0 → CRITICAL REFINEMENT REQUIRED

**Action:** Deep refinement of weakest areas

Process:
1. **Identify Root Causes:** For each of your 3 weakest criteria, diagnose WHY the score is low
2. **Targeted Re-Research:** For each weak criterion:
   - Re-activate thinking mode with higher budget
   - Use Socratic questioning to explore gaps
   - Add 3+ concrete examples per weak area
   - Strengthen source quality (prioritize official docs, research papers)
3. **Update Output:** Revise the relevant sections with enhanced content
4. **Re-Score:** Evaluate again with same rubric (must achieve ≥ 8.0 overall)
5. **Iterate:** If still < 8.0, repeat steps 1-4 until threshold met

---

### Enhancement Gate 2: Score 8.0-8.9 → TARGETED ENHANCEMENT

**Action:** Focused improvement on weakest criterion

Process:
1. **Deep Dive Weakest Area:** Identify your single lowest-scoring criterion
2. **Enhancement Strategy:** Add enhancement section specifically addressing this weakness
3. **Add Unexpected Insight:** Research one aspect NOT explicitly requested but highly relevant
4. **Re-Score:** Evaluate again (target: ≥ 9.0 overall)

---

### Enhancement Gate 3: Score ≥ 9.0 → OPTIONAL DEEP DIVE

**Action:** Advanced insights and future implications (optional)

If you choose to enhance:
1. **Novel Connections:** Draw unexpected links between findings
2. **Strategic Implications:** Project long-term consequences
3. **Research Frontiers:** Identify emerging patterns or uncharted territory
4. **Meta-Analysis:** Reflect on what this research reveals about the broader domain

---

## SUCCESS CRITERIA

Your research output is complete when:
- ✅ All N questions answered fully (200+ words, 2+ examples each)
- ✅ All claims backed by credible sources with links
- ✅ 12+ template-ready patterns extracted and validated
- ✅ Socratic critical evaluation completed
- ✅ Self-scored ≥ 8.5/10 overall (after enhancement if needed)
- ✅ All individual criteria ≥ 7.5/10
- ✅ Thinking process documented (via includeThoughts)
```

---

### Template B: Strategic Decision Research

**Use When:** Making architectural decisions, need recommendations, strategic guidance

```markdown
# Topic [X]: [Name] - Strategic Decision Analysis

## GEMINI CONFIGURATION
- Model: gemini-2.5-pro
- thinkingBudget: 24576
- includeThoughts: true
- response_mime_type: "application/json" (for final recommendation section)
- responseSchema: [decision framework schema]

## ROLE DEFINITION
You are a strategic technology advisor with deep expertise in [domain]. Your decisions:
- Are grounded in evidence from authoritative sources
- Consider multiple stakeholder perspectives
- Account for short-term and long-term consequences
- Provide clear, actionable recommendations
- Acknowledge uncertainty and trade-offs explicitly

## MISSION CONTEXT

**Decision Required:** [Clear statement of decision to be made]
**Current State:** [Baseline situation]
**Constraints:** [Technical, resource, timeline constraints]
**Success Criteria:** [What makes this decision "good"]

---

## THINKING PREPARATION

Before beginning analysis, allocate thinking budget to:
1. Map the complete decision space
2. Identify critical trade-offs and dependencies
3. Plan analysis strategy across multiple perspectives
4. Anticipate second-order consequences

---

## PART A: STRATEGIC ANALYSIS

### Section 1: Challenge Definition
**Think step-by-step:**
- What problem does this decision solve?
- Why is the current state insufficient?
- What would "success" look like concretely?

**Required Analysis:**
- **Problem Statement:** Clear, specific problem definition
- **Evidence of Pain:** Real-world examples showing current limitations
- **Requirements:** Must-have vs nice-to-have capabilities
- **Anti-Requirements:** What we explicitly DON'T need

---

### Section 2: Options Analysis

For EACH option:
- **Overview:** What is it and how does it work?
- **Strengths:** Where does it excel?
- **Weaknesses:** Where does it fall short?
- **Effort:** Implementation complexity (low/medium/high with justification)
- **Risk:** What could go wrong? How likely?
- **Sources:** Link to documentation, case studies, or research

**Quality Gate:**
IF analysis shows bias toward one option → REFINE
Must present options objectively

---

### Section 3: Stakeholder Perspectives

Analyze from distinct stakeholder viewpoints:
- **Perspective 1 [Role A]:** Primary concern, decision evaluation, key question
- **Perspective 2 [Role B]:** [Same structure]
- **Perspective 3 [Role C]:** [Same structure]
- **Synthesis:** Where do perspectives align? Where do they conflict?

---

### Section 4: Consequence Forecasting

For EACH option:
- **Short-Term (1-3 months):** Immediate effects
- **Medium-Term (6-12 months):** Operational characteristics
- **Long-Term (1-2 years):** Strategic positioning
- Include intended and unintended consequences

---

### Section 5: Recommendation (Structured Output)

**Output as JSON:**
```json
{
  "recommendation": {
    "primary_choice": "string",
    "confidence_level": "high|medium-high|medium",
    "one_sentence_rationale": "string"
  },
  "decision_criteria": [
    {
      "criterion": "string",
      "weight": "critical|high|medium",
      "how_recommendation_satisfies": "string"
    }
  ],
  "progressive_adoption_path": {
    "phase_1_baseline": "string",
    "phase_2_enhancement": "string",
    "phase_3_optimization": "string"
  },
  "triggers_for_reevaluation": ["string"],
  "trade_offs_accepted": ["string"]
}
```

**Quality Gate:** IF recommendation is vague → INSUFFICIENT. Must be specific and actionable.

---

### Section 6: Implementation Patterns

Extract 12+ template-ready patterns for implementing your recommendation.
[Use same pattern quality standard as Template A]

---

## PART B: SELF-SCORING (Weighted for Strategic Decisions)

**Weighted Scoring:**
- Completeness: 1.0x
- Evidence Quality: 1.5x (higher - decisions need strong evidence)
- Depth of Analysis: 1.0x
- Pattern Quality: 1.0x
- Critical Thinking: 1.5x (higher - challenge assumptions)
- Integration: 1.0x
- Actionability: 1.5x (higher - must provide clear next steps)

[Use same scoring framework as Template A with weights]

---

## PART C: SELF-ENHANCEMENT PROTOCOL
[Same 3-tier gates as Template A]

---

## SUCCESS CRITERIA
- ✅ Clear recommendation made (not "it depends")
- ✅ Decision criteria explicitly stated
- ✅ All options analyzed objectively
- ✅ Multiple stakeholder perspectives considered
- ✅ Consequences forecasted (short/medium/long-term)
- ✅ 12+ implementation patterns provided
- ✅ Self-scored ≥ 8.5/10 (weighted)
```

---

## Part 3: Advanced Techniques Reference

### Socratic Questioning Framework

```markdown
## SOCRATIC ANALYSIS

### Stage 1: Gather and Scrutinize Evidence
- What evidence supports this?
- How credible are sources?
- Are there contradictions?

### Stage 2: Expose and Question Assumptions
- What fundamental assumptions underlie this?
- Are these assumptions valid?
- What if assumptions are wrong?

### Stage 3: Analyze Alternative Viewpoints
- [Stakeholder A]: Their evaluation?
- [Stakeholder B]: Their concerns?
- [Stakeholder C]: Their opportunities?

### Stage 4: Generate Creative Alternatives
- If approach X doesn't work, what else?
- What unconventional solutions exist?

### Stage 5: Predict Consequences
- Short-term: What happens immediately?
- Long-term: What strategic position results?
```

---

### Quality Gates Pattern

```markdown
## QUALITY GATE: [NAME]

**Gate Criterion:** [Specific, measurable condition]

**Pass Condition:** IF [met] THEN [Action A]
**Fail Condition:** IF [NOT met] THEN [Action B]

**Few-Shot Examples:**
Example 1 - PASS: [Example + reason]
Example 2 - FAIL: [Example + reason]
```

---

### Multi-Agent Simulation Pattern

```markdown
## MULTI-PERSPECTIVE ANALYSIS

### Persona 1: [Name] - [Role]
**Background:** [Expertise]
**Primary Concern:** [Priority]
**Analysis:** [Perspective]
**Recommendation:** [Advice]

### Persona 2: [Name] - [Role]
[Same structure]

### Synthesis:
- Consensus: Where do all agree?
- Conflicts: Where do priorities clash?
- Balanced View: How to reconcile?
```

---

## Part 4: Common Pitfalls & Solutions

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Vague Thinking Triggers** | "Think about this" doesn't activate deep reasoning | Use explicit: "Let's think step by step," "Show your reasoning" |
| **Unstructured Comprehensiveness** | Long, unfocused outputs | Use numbered questions or explicit sections |
| **No API Schema Enforcement** | Inconsistent JSON format | ALWAYS use `response_mime_type` + `responseSchema` |
| **No Few-Shot Examples** | Abstract quality standards | Provide concrete examples of excellent vs poor |
| **Single-Pass** | First draft rarely achieves 9-10/10 | Build self-scoring + enhancement gates |
| **Default Thinking Budget** | Surface-level for complex analysis | Set `thinkingBudget: 24576+` explicitly |
| **Missing Grounding** | Current info without search → hallucination | Enable `GoogleSearch()` tool + validate metadata |

---

## Part 5: Quality Checklist

Before submitting research prompts, verify:

**Architecture Alignment:**
- [ ] Thinking triggers included
- [ ] Thinking budget set appropriately (16384+ for complex)
- [ ] includeThoughts enabled
- [ ] Structured output uses API parameters
- [ ] Grounding enabled if current info needed

**Prompt Structure:**
- [ ] Clear role definition with domain expertise
- [ ] Explicit step-by-step instructions
- [ ] Few-shot examples for quality standards
- [ ] Quality gates with pass/fail conditions
- [ ] Self-scoring rubric with objective criteria
- [ ] Enhancement protocol with thresholds

**Technique Combination:**
- [ ] Chain-of-Thought for reasoning
- [ ] Socratic questioning for critical analysis
- [ ] Quality gates for standards
- [ ] Self-improvement loop
- [ ] Multi-perspective when needed

**Output Requirements:**
- [ ] Success criteria defined
- [ ] Minimum standards specified
- [ ] Format requirements explicit
- [ ] Pattern quality standard provided

---

## Conclusion

**Quality Formula:**
```
Optimal Output = Native Architecture Leverage 
                + Multi-Technique Combination 
                + Structured Workflow 
                + Self-Enhancement Loops 
                + Objective Quality Gates
```

**Key Principles:**
1. Leverage Gemini's "Thinking" with explicit triggers
2. Combine multiple high-reliability techniques
3. Use API-level enforcement for critical requirements
4. Structure prompts as complete workflows
5. Build self-enhancement loops into every prompt
6. Prioritize quality over speed

When these elements align, Gemini 2.5 Pro consistently produces 9-10/10 research outputs.