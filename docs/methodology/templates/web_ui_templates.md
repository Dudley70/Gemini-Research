# Web UI Prompt Templates: Production-Ready Research Frameworks

**Created:** 2025-11-13 23:45 AEDT  
**Purpose:** Production-ready prompt templates for Gemini Deep Research Web UI (PATH 1)  
**Execution:** Copy/paste generated prompts into google.com/gemini  
**Target Output:** Human-readable prose research (1,500-2,000 lines for comprehensive, 500-800 for strategic)  
**Quality Standard:** Consistently achieves 9-10/10 outputs when properly applied

**Critical Context:**
- **PATH 1 (Web UI):** These templates generate prose-optimized prompts for interactive copy/paste use
- **NOT for API:** API automation uses different formats (see docs/api/templates/)
- **Cross-LLM Ready:** Any LLM (ChatGPT, Claude, etc.) can read this doc and generate effective prompts
- **Evidence-Based:** Derived from 1,582 lines of academic research on Gemini 2.5 Pro capabilities

**Prerequisites:** Read `docs/methodology/principles/core_discoveries.md` first for technique foundations

---

## Executive Summary

Gemini 2.5 Pro achieves optimal performance when prompts leverage its core architectural strengths and combine multiple advanced techniques. This framework provides battle-tested templates for research prompts that consistently produce 9-10/10 quality outputs.

**Key Principle:** Structure prompts as complete, self-contained workflows that trigger Gemini's native "Thinking" mechanism and combine multiple high-reliability techniques.

**Template Selection:**
- **Template A (Comprehensive):** Foundation topics requiring systematic coverage → 1,500-2,000 line outputs
- **Template B (Strategic Decision):** Architectural decisions needing clear recommendations → 500-800 line outputs
- **Hybrid Approach:** Complex topics needing both knowledge foundation + strategic synthesis → 800-1,200 lines

---

## Part 1: Understanding Gemini 2.5 Pro Architecture

### 1.1 The "Thinking" Mechanism (Critical for Prompt Design)

**What It Is:**
Gemini 2.5 Pro includes an internal reasoning process that occurs BEFORE generating the final response. This "Thinking" mechanism:
- Allocates computational budget (128-32,768 tokens worth of reasoning)
- Performs meta-analysis of prompt complexity
- Auto-calibrates depth based on task requirements
- Is **always active** and cannot be disabled in the Pro model

**How to Trigger in Web UI Prompts:**
Use explicit phrases that activate deeper reasoning:
- "Let's think step by step"
- "Show your reasoning process"
- "Think deeply about..."
- "Before answering, consider..."
- "Allocate thinking budget to..."

**Impact on Quality:**
- Prompts with thinking triggers consistently produce deeper analysis
- Benchmark validation shows thinking-enabled outputs significantly outperform surface-level responses
- Best for: Complex reasoning, multi-step planning, strategic analysis, pattern extraction

**Web UI Limitation:**
You cannot directly control thinking budget or expose thoughts via copy/paste prompts. However, explicit thinking triggers still activate the mechanism and improve quality.

---

### 1.2 High-Reliability Prompting Techniques

These techniques leverage Gemini's architecture through structured prompt design:

| Technique | Effectiveness | Reliability | Primary Use Case |
|-----------|---------------|-------------|------------------|
| **Chain-of-Thought (CoT)** | 10/10 | 10/10 | Step-by-step reasoning for complex problems |
| **Socratic Questioning** | 10/10 | 8/10 | Critical thinking, assumption challenging |
| **Multi-Agent Simulation** | 10/10 | 9/10 | Multiple perspective analysis |
| **Self-Scoring** | 10/10 | 9/10 | Quality self-assessment with rubrics |
| **Quality Gates** | 10/10 | 9/10 | Conditional standards enforcement |
| **Iterative Self-Improvement** | 10/10 | 8/10 | Generate → Critique → Revise loops |
| **Tree of Thoughts** | 9/10 | 7/10 | Exploring multiple solution paths |

**Key Insight:** These techniques achieve 9-10/10 effectiveness when properly structured in prompts. The quality depends heavily on clear instructions and examples.

**Evidence Source:** Systematic testing documented in source research papers (see `docs/analysis/source_papers_complete_analysis.md`)

---

### 1.3 Optimal Technique Combinations

Based on empirical testing, combine 4-6 complementary techniques for best results:

**For Comprehensive Research:**
1. Chain-of-Thought (reasoning framework)
2. Socratic Questioning (critical analysis)
3. Self-Scoring (quality assessment)
4. Quality Gates (standards enforcement)
5. Pattern Extraction (actionable outputs)
6. Self-Improvement Loop (refinement)

**For Strategic Decisions:**
1. Chain-of-Thought (structured analysis)
2. Multi-Agent Simulation (stakeholder perspectives)
3. Consequence Forecasting (impact analysis)
4. Self-Scoring (decision quality)
5. Quality Gates (recommendation standards)
6. Pattern Extraction (implementation guidance)

**Warning:** Don't combine >6 techniques - creates cognitive overload and dilutes effectiveness.

---

## Part 2: Template A - Comprehensive Foundation Research

### When to Use Template A

**Ideal Scenarios:**
- Building systematic knowledge on a foundation topic
- Need encyclopedic coverage of multiple aspects
- Extracting actionable patterns and best practices
- Research that will inform multiple downstream decisions

**Expected Output:**
- Length: 1,500-2,000 lines of detailed prose
- Structure: Multiple questions, each fully explored
- Format: Overview + Deep Dive + Examples + Best Practices + Sources
- Patterns: 12+ template-ready, immediately usable patterns

**Not Suitable For:**
- Simple yes/no questions (overkill)
- Time-sensitive queries needing quick answers
- Topics where you need specific recommendations (use Template B)

---

### Template A Structure

```markdown
# [TOPIC NAME]: Comprehensive Research

## ROLE DEFINITION
You are a senior research analyst specializing in [domain]. Your approach combines:
- Systematic investigation of all relevant aspects
- Evidence-based reasoning with source verification
- Pattern extraction for practical application
- Critical evaluation of findings with Socratic questioning

## PRIMARY RESEARCH TASK

### INSTRUCTIONS FOR ANSWERING
For each question below, think step by step and provide:
1. Detailed explanation (minimum 200 words)
2. At least 2 concrete examples with full context
3. Code snippets, configuration samples, or implementation details where applicable
4. Source links for all factual claims
5. Critical evaluation: Question your own assumptions before finalizing each answer

---

### CLUSTER 1: [CORE CONCEPTS] (Questions 1-N)

#### Q1: [Specific Question]

**Sub-components to address:**
- [Aspect A]: [Clear guidance on what to explore]
- [Aspect B]: [Clear guidance on what to explore]
- [Aspect C]: [Clear guidance on what to explore]

**Required Output Structure for Q1:**
- **Overview:** High-level explanation of the concept
- **Deep Dive:** Detailed technical analysis with mechanisms explained
- **Examples:** Minimum 2 concrete cases with code/configuration samples
- **Best Practices:** Actionable guidance practitioners can immediately use
- **Sources:** Links to official documentation, research papers, or authoritative sources

**Thinking Trigger:** Before answering Q1, think deeply about: What are the fundamental mechanisms at work? What edge cases exist? What do practitioners actually need to know to use this effectively?

---

#### Q2: [Specific Question]

[Repeat same structure as Q1]

---

#### Q3: [Specific Question]

[Continue for all questions in cluster]

---

### CLUSTER 2: [RELATED ASPECTS] (Questions N+1 to M)

[Repeat cluster structure with 3-5 related questions]

---

### CLUSTER 3: [ADVANCED TOPICS] (Questions M+1 to Z)

[Repeat cluster structure]

---

### PHASE 2: CRITICAL SYNTHESIS

Now that you've completed systematic investigation, use the Socratic method to critically evaluate your findings:

#### Stage 1: Scrutinize the Evidence
- What is the quality level of sources you used? (Official docs > research papers > production use > community forums > anecdotal)
- Are there contradictions or inconsistencies in the evidence?
- What fundamental assumptions underlie your findings?
- Where is evidence strongest? Where is it weakest?

#### Stage 2: Challenge from Alternative Perspectives

Consider your findings from the viewpoint of different stakeholders:
- **[Stakeholder A - e.g., Developer]:** How would they evaluate these findings? What are their priorities?
- **[Stakeholder B - e.g., Architect]:** What concerns would they raise? What opportunities would they see?
- **[Stakeholder C - e.g., Operations]:** What practical limitations would they identify?

#### Stage 3: Identify Gaps and Limitations
- What important questions remain unanswered?
- Where is evidence weak, missing, or contradictory?
- What areas need deeper investigation beyond this research?
- What did you assume that might not be universally true?

---

### PHASE 3: PATTERN EXTRACTION

Based on your comprehensive research, extract 12 or more template-ready, actionable patterns that practitioners can immediately apply.

**Pattern Quality Standard (CRITICAL - READ CAREFULLY):**

Each pattern MUST include ALL of the following elements:
1. **Name:** Clear, descriptive identifier (e.g., "Circuit Breaker for API Resilience")
2. **Context:** When to use this pattern vs alternatives, what problem it solves
3. **Structure:** Complete workflow including entry conditions, process, and exit conditions
4. **Steps:** Numbered, actionable steps that someone can follow
5. **Example:** Real code, configuration, or implementation sample that actually works
6. **Pitfalls:** Common mistakes people make when applying this pattern

**Quality Gate for Patterns:**
IF any pattern is missing ANY of the 6 required elements → STOP and REFINE that pattern until complete.

Patterns must be immediately usable by practitioners without additional research.

---

## SELF-SCORING ASSESSMENT

Evaluate your research output using this objective rubric. Score each criterion on a 0-10 scale:

### Scoring Criteria

**1. Completeness (0-10):**
- **10:** All questions fully answered with 200+ words each, minimum 2 examples per question, all sub-components addressed
- **7-9:** Minor gaps in coverage or slightly less detail than standard
- **4-6:** Several questions under-explored or missing examples
- **0-3:** Major gaps, questions skipped, or superficial treatment

**2. Evidence Quality (0-10):**
- **10:** All claims backed by official documentation, research papers, or proven production patterns with links provided
- **7-9:** Most claims well-sourced, a few rely on community sources or forums
- **4-6:** Mix of quality sources and weak evidence
- **0-3:** Many unsupported claims or reliance on low-quality sources

**3. Depth of Analysis (0-10):**
- **10:** Covers underlying mechanisms, edge cases, trade-offs, and alternatives for all topics
- **7-9:** Good depth overall, minor aspects left unexplored
- **4-6:** Surface-level treatment in several areas
- **0-3:** Superficial throughout, lacks technical depth

**4. Pattern Quality (0-10):**
- **10:** All 12+ patterns complete with all 6 required elements (name, context, structure, steps, example, pitfalls)
- **7-9:** Most patterns complete, minor refinement needed on a few
- **4-6:** Patterns missing key elements or too abstract
- **0-3:** Patterns incomplete or not immediately usable

**5. Critical Thinking (0-10):**
- **10:** Evidence scrutinized, alternative perspectives considered, assumptions questioned, gaps identified
- **7-9:** Good critical engagement, some areas accepted without deep questioning
- **4-6:** Limited critical analysis, mostly descriptive
- **0-3:** Accepts claims at face value without evaluation

**6. Integration (0-10):**
- **10:** Clear connections between findings, cross-references between questions, synthesized insights
- **7-9:** Good integration, some sections could be better connected
- **4-6:** Moderate integration, several siloed sections
- **0-3:** Questions treated in complete isolation

**7. Actionability (0-10):**
- **10:** Clear next steps, template-ready patterns, immediately implementable guidance
- **7-9:** Mostly actionable, minor gaps in practical guidance
- **4-6:** Some actionable elements, but requires significant adaptation
- **0-3:** Abstract recommendations without clear implementation path

### Self-Scoring Instructions

1. Score each of the 7 criteria objectively (0-10)
2. Calculate the average score across all criteria
3. Identify your 3 weakest-scoring criteria
4. For each score, provide specific evidence from your output that justifies the score

**Example Scoring:**
- Completeness: 9/10 - "All 8 questions answered with 200+ words and 2+ examples each, minor: Q3 could use one more example"
- Evidence Quality: 8/10 - "90% of claims have official doc links, 2 claims in Q6 rely on Stack Overflow discussions"
- [Continue for all 7 criteria]
- **Average: [X.X]/10**

---

## SELF-ENHANCEMENT PROTOCOL

Based on your calculated average score, follow the appropriate enhancement path:

### Enhancement Gate 1: Score < 8.0 → CRITICAL REFINEMENT REQUIRED

Your output needs significant improvement before it meets quality standards.

**Process:**
1. **Root Cause Analysis:** For each of your 3 weakest-scoring criteria, diagnose WHY the score is low. Be specific.

2. **Targeted Re-Research:** For each weak criterion:
   - Think step by step about what's missing
   - Use Socratic questioning to explore gaps in your analysis
   - Add minimum 3 concrete examples for each weak area
   - Strengthen source quality (prioritize official documentation and research papers over community sources)

3. **Update Output:** Revise the relevant sections of your research with enhanced content. Show which sections you improved.

4. **Re-Score:** Evaluate again using the same rubric. You must achieve ≥ 8.0 overall average.

5. **Iterate if Needed:** If still < 8.0 after revision, repeat steps 1-4 until threshold is met.

---

### Enhancement Gate 2: Score 8.0-8.9 → TARGETED ENHANCEMENT

Your output is good but can be elevated to excellent with focused improvements.

**Process:**
1. **Focus on Weakest Area:** Identify your single lowest-scoring criterion from the rubric.

2. **Deep Dive Enhancement:** Create an enhancement section that specifically addresses this weakness:
   - If weak on evidence: Add 5+ authoritative source links with context
   - If weak on depth: Expand 3 sections with mechanism explanations and edge cases
   - If weak on patterns: Ensure all patterns have complete 6-element structure
   - If weak on critical thinking: Add Socratic challenge section for 3 key findings

3. **Add Unexpected Insight:** Research one aspect that was NOT explicitly requested but is highly relevant to the topic. This demonstrates going beyond the prompt.

4. **Re-Score:** Evaluate again (target: ≥ 9.0 overall)

---

### Enhancement Gate 3: Score ≥ 9.0 → OPTIONAL ADVANCED INSIGHTS

Your output meets high quality standards. Further enhancement is optional.

If you choose to enhance for exceptional quality:
1. **Novel Connections:** Draw unexpected links between findings across different questions
2. **Strategic Implications:** Project long-term consequences and future evolution of the topic
3. **Research Frontiers:** Identify emerging patterns, uncharted territory, or open questions in the field
4. **Meta-Analysis:** Reflect on what this research reveals about the broader domain beyond the specific topic

---

## SUCCESS CRITERIA CHECKLIST

Your comprehensive research is complete when ALL of the following are true:

- ✅ All questions answered fully (minimum 200 words each)
- ✅ Minimum 2 concrete examples provided for each question
- ✅ All factual claims backed by credible sources with links
- ✅ 12+ template-ready patterns extracted with all 6 required elements
- ✅ Socratic critical evaluation completed (evidence scrutiny, alternative perspectives, gap identification)
- ✅ Self-scored with average ≥ 8.5/10 across all 7 criteria
- ✅ All individual criteria scored ≥ 7.5/10 (no weak areas)
- ✅ Enhancement protocol completed if score was initially < 8.5

END OF TEMPLATE A
```

---

## Part 3: Template B - Strategic Decision Research

### When to Use Template B

**Ideal Scenarios:**
- Making architectural or technology decisions
- Need clear recommendation with justification
- Evaluating multiple options against criteria
- Strategic guidance for implementation path

**Expected Output:**
- Length: 500-800 lines of synthesis-focused prose
- Structure: Problem definition → Options analysis → Stakeholder perspectives → Recommendation → Implementation patterns
- Format: Narrative analysis with clear decision conclusion
- Patterns: 12+ implementation-focused patterns

**Not Suitable For:**
- Exploratory research without decision point
- Topics needing comprehensive encyclopedic coverage (use Template A)
- Questions where "it depends" is the right answer

---

### Template B Structure

```markdown
# [TOPIC NAME]: Strategic Decision Analysis

## ROLE DEFINITION
You are a strategic technology advisor with deep expertise in [domain]. Your decision-making approach:
- Grounds recommendations in evidence from authoritative sources
- Considers multiple stakeholder perspectives explicitly
- Accounts for short-term and long-term consequences
- Provides clear, actionable recommendations (never "it depends" without choosing)
- Acknowledges uncertainty and trade-offs transparently

## MISSION CONTEXT

**Decision Required:** [Clear, specific statement of the decision to be made]

**Current State:** [Describe the baseline situation - what exists today]

**Constraints:** [Technical limitations, resource constraints, timeline requirements, regulatory requirements]

**Success Criteria:** [What specific outcomes would make this decision "successful" - be measurable]

---

## THINKING PREPARATION

Before beginning your analysis, allocate thinking budget to:
1. Map the complete decision space - what are ALL the options?
2. Identify critical trade-offs and dependencies between options
3. Plan your analysis strategy across multiple perspectives
4. Anticipate second-order consequences that aren't immediately obvious

---

## PART A: STRATEGIC ANALYSIS

### Section 1: Challenge Definition

Think step-by-step about the core problem:

**Analysis Required:**
1. What specific problem does this decision solve? Be concrete, not abstract.
2. Why is the current state insufficient? What evidence shows the pain?
3. What would "success" look like in measurable terms?
4. What do we explicitly NOT need? (Anti-requirements prevent scope creep)

**Output Format:**
- **Problem Statement:** Clear, specific problem definition (2-3 sentences)
- **Evidence of Pain:** Real-world examples showing current limitations
- **Requirements:** Must-have capabilities (prioritized)
- **Anti-Requirements:** What we explicitly DON'T need and why

---

### Section 2: Options Analysis

**Instructions:** For EACH viable option, provide complete analysis:

#### Option 1: [Name]

**Overview:** What is this option and how does it work? (2-3 paragraphs)

**Strengths:** Where does this option excel? What problems does it solve well?
- Strength A: [Specific advantage with evidence]
- Strength B: [Specific advantage with evidence]
- Strength C: [Specific advantage with evidence]

**Weaknesses:** Where does this option fall short? What problems does it NOT solve?
- Weakness A: [Specific limitation with evidence]
- Weakness B: [Specific limitation with evidence]
- Weakness C: [Specific limitation with evidence]

**Effort Assessment:** How complex is implementation?
- Complexity Level: [Low / Medium / High]
- Justification: [Specific factors contributing to complexity]
- Time Estimate: [Rough timeline based on complexity]

**Risk Analysis:** What could go wrong?
- Risk A: [Specific risk] - Likelihood: [Low/Medium/High] - Impact: [Low/Medium/High]
- Risk B: [Specific risk] - Likelihood/Impact
- Risk C: [Specific risk] - Likelihood/Impact

**Sources:** [Links to official documentation, case studies, research papers, or production implementations]

---

#### Option 2: [Name]

[Repeat same structure as Option 1]

---

#### Option 3: [Name]

[Repeat same structure]

---

**Quality Gate for Options Analysis:**
IF your analysis shows obvious bias toward one option → STOP and REFINE
All options must be presented objectively with both strengths and weaknesses clearly documented

---

### Section 3: Stakeholder Perspectives

Analyze this decision from distinct stakeholder viewpoints. Each perspective challenges different aspects:

#### Perspective 1: [Role A - e.g., Development Team Lead]
- **Primary Concern:** [What matters most to this role]
- **Decision Evaluation:** [How would they assess each option]
- **Key Question They Would Ask:** [Critical question from their viewpoint]
- **Influence on Decision:** [How should their perspective weight the decision]

#### Perspective 2: [Role B - e.g., Operations/SRE]
[Same structure]

#### Perspective 3: [Role C - e.g., Product/Business]
[Same structure]

#### Synthesis:
- **Where Perspectives Align:** [Common ground across stakeholders]
- **Where Perspectives Conflict:** [Competing priorities that create trade-offs]
- **Balanced View:** [How to reconcile conflicts]

---

### Section 4: Consequence Forecasting

For EACH option, project consequences across time horizons:

#### Option 1: [Name] - Consequence Timeline

**Short-Term (1-3 months):**
- Intended Consequences: [Expected immediate effects]
- Unintended Consequences: [Possible unexpected effects]

**Medium-Term (6-12 months):**
- Intended Consequences: [Expected operational characteristics]
- Unintended Consequences: [Possible emergent issues]

**Long-Term (1-2 years):**
- Intended Consequences: [Strategic positioning results]
- Unintended Consequences: [Possible long-term limitations]

[Repeat for all options]

---

### Section 5: Final Recommendation

**CRITICAL INSTRUCTION:** You must make a clear recommendation. Do NOT conclude with "it depends" unless you then specify what it depends on and make conditional recommendations.

#### Primary Recommendation

**Chosen Option:** [Clearly state which option you recommend]

**Confidence Level:** [High / Medium-High / Medium] - with justification

**One-Sentence Rationale:** [Concise explanation of why this option is best given the context]

**Detailed Justification:** [2-3 paragraphs explaining your reasoning]

#### Decision Criteria Met

For each success criterion from Mission Context, explain how your recommendation satisfies it:

1. **[Success Criterion 1]:** How recommendation meets this - [Specific explanation]
2. **[Success Criterion 2]:** How recommendation meets this
3. **[Success Criterion 3]:** How recommendation meets this

#### Progressive Adoption Path

Your recommendation should be implemented in phases:

**Phase 1 - Baseline (Months 1-2):**
[Minimum viable implementation to validate approach]

**Phase 2 - Enhancement (Months 3-6):**
[Expand capabilities, address initial learnings]

**Phase 3 - Optimization (Months 6-12):**
[Refine, scale, optimize based on production experience]

#### Triggers for Re-Evaluation

Circumstances that should prompt reconsidering this decision:
1. [Trigger A - specific measurable condition]
2. [Trigger B - specific measurable condition]
3. [Trigger C - specific measurable condition]

#### Trade-Offs Accepted

Be explicit about what you're giving up with this recommendation:
1. [Trade-off A accepted]
2. [Trade-off B accepted]
3. [Trade-off C accepted]

---

### Section 6: Implementation Patterns

Extract 12 or more template-ready patterns for implementing your recommendation.

**Pattern Quality Standard:** [Use same 6-element structure as Template A]
- Name, Context, Structure, Steps, Example, Pitfalls

Focus patterns on implementation specifics, not abstract principles.

---

## PART B: SELF-SCORING (Weighted for Strategic Decisions)

Use the same 7-criteria framework as Template A, but with adjusted weights for strategic context:

### Weighted Scoring Formula

- Completeness: 1.0x (normal weight)
- Evidence Quality: 1.5x (higher - strategic decisions require strong evidence)
- Depth of Analysis: 1.0x (normal weight)
- Pattern Quality: 1.0x (normal weight)
- Critical Thinking: 1.5x (higher - must challenge assumptions rigorously)
- Integration: 1.0x (normal weight)
- Actionability: 1.5x (higher - must provide clear next steps)

**Weighted Score Calculation:**
1. Score each criterion 0-10 using Template A rubric
2. Apply weights: [(Criterion Score × Weight) for all criteria]
3. Sum weighted scores
4. Divide by sum of weights (8.5 total)
5. Result is weighted average

**Example:**
- Completeness: 9 × 1.0 = 9.0
- Evidence Quality: 8 × 1.5 = 12.0
- Critical Thinking: 9 × 1.5 = 13.5
- [Continue for all 7]
- Sum: 75.5 / 8.5 weights = **8.88 weighted average**

---

## PART C: SELF-ENHANCEMENT PROTOCOL

Use the same 3-tier enhancement gates as Template A:
- Score < 8.0 → Critical Refinement
- Score 8.0-8.9 → Targeted Enhancement
- Score ≥ 9.0 → Optional Advanced Insights

[Follow exact same process detailed in Template A]

---

## SUCCESS CRITERIA CHECKLIST

Your strategic decision analysis is complete when:

- ✅ Clear recommendation made (not vague "it depends")
- ✅ Decision criteria from Mission Context explicitly addressed
- ✅ All viable options analyzed objectively with strengths/weaknesses
- ✅ Minimum 3 stakeholder perspectives considered
- ✅ Consequences forecasted across short/medium/long-term for all options
- ✅ Progressive adoption path provided (3 phases)
- ✅ 12+ implementation patterns extracted
- ✅ Self-scored ≥ 8.5/10 (weighted average)
- ✅ Enhancement protocol completed if needed

END OF TEMPLATE B
```

---

## Part 4: Advanced Technique Patterns

### 4.1 Socratic Questioning Framework

Use when critical analysis and assumption-challenging are needed:

```markdown
## SOCRATIC ANALYSIS

### Stage 1: Gather and Scrutinize Evidence
- What specific evidence supports this claim or finding?
- How credible and authoritative are the sources?
- Are there contradictions or inconsistencies in the evidence?
- What is the recency and relevance of the evidence?

### Stage 2: Expose and Question Assumptions
- What fundamental assumptions underlie this conclusion?
- Are these assumptions valid in all contexts?
- What would happen if these assumptions were wrong?
- What alternative assumptions could lead to different conclusions?

### Stage 3: Analyze Alternative Viewpoints
- **[Stakeholder A]:** How would they evaluate this?
- **[Stakeholder B]:** What concerns would they raise?
- **[Stakeholder C]:** What opportunities would they see?
- Where do these perspectives conflict?

### Stage 4: Generate Creative Alternatives
- If the primary approach doesn't work, what alternatives exist?
- What unconventional solutions might be overlooked?
- How could we reframe the problem to reveal new options?

### Stage 5: Predict Consequences
- Short-term: What happens immediately?
- Long-term: What strategic position results?
- Unintended: What unexpected effects might emerge?
```

---

### 4.2 Quality Gates Pattern

Use when enforcing standards or conditional logic:

```markdown
## QUALITY GATE: [GATE NAME]

**Gate Criterion:** [Specific, measurable condition that must be met]

**Pass Condition:** IF [criterion is met] THEN [Action A - proceed/accept]
**Fail Condition:** IF [criterion is NOT met] THEN [Action B - refine/reject]

**Few-Shot Examples:**

Example 1 - PASS:
- Input: [Example that meets criterion]
- Reason: [Why it passes]
- Action: [What happens next]

Example 2 - FAIL:
- Input: [Example that fails criterion]
- Reason: [Why it fails]
- Action: [Required refinement]

Example 3 - EDGE CASE:
- Input: [Borderline example]
- Analysis: [How to evaluate]
- Decision: [Pass/Fail with justification]
```

---

### 4.3 Multi-Agent Simulation Pattern

Use when multiple perspectives enhance decision quality:

```markdown
## MULTI-PERSPECTIVE ANALYSIS

### Persona 1: [Name] - [Role Title]
**Background:** [Relevant expertise and experience]
**Primary Concern:** [What matters most to this persona]
**Analytical Lens:** [How they evaluate problems]
**Assessment of [Topic]:** [Their detailed perspective]
**Recommendation:** [Their advice]

### Persona 2: [Name] - [Role Title]
[Same structure]

### Persona 3: [Name] - [Role Title]
[Same structure]

### Synthesis Across Perspectives:
- **Consensus Points:** Where do all personas agree?
- **Conflicting Priorities:** Where do perspectives clash?
- **Balanced View:** How to reconcile differences?
- **Blind Spots:** What might all perspectives miss?
```

---

## Part 5: Common Pitfalls & Solutions

| Pitfall | Problem It Creates | Solution |
|---------|-------------------|----------|
| **Vague Thinking Triggers** | Generic "think about this" doesn't activate deep reasoning | Use explicit triggers: "Let's think step by step," "Show your reasoning," "Before answering, consider..." |
| **Unstructured Questions** | Long, unfocused outputs that don't address core needs | Use numbered questions, explicit sections, clear sub-components |
| **No Quality Standards** | Abstract outputs without actionable guidance | Provide concrete few-shot examples of excellent vs poor quality |
| **Single-Pass Generation** | First draft rarely achieves 9-10/10 quality | Build self-scoring + enhancement gates into every prompt |
| **Missing Examples** | Theoretical patterns users can't apply | Require minimum 2 concrete examples with code/config per pattern |
| **Weak Sources** | Claims based on anecdotal evidence or forums | Explicitly prioritize: Official docs > Research papers > Production use > Community |
| **No Critical Analysis** | Accepts all information at face value | Include Socratic questioning stage to challenge assumptions |

---

## Part 6: Quality Checklist for Prompt Generation

Before using these templates to generate a research prompt, verify your prompt includes:

**Thinking Activation:**
- [ ] Explicit thinking triggers ("Let's think step by step")
- [ ] Phrases that encourage deep reasoning ("Before answering, consider...")
- [ ] Budget allocation guidance ("Think deeply about...")

**Structural Clarity:**
- [ ] Clear role definition with domain expertise specified
- [ ] Explicit step-by-step instructions for each section
- [ ] Numbered questions or sections for organization
- [ ] Required output structure defined (Overview, Deep Dive, Examples, etc.)

**Quality Standards:**
- [ ] Few-shot examples showing excellent quality
- [ ] Quality gates with specific pass/fail conditions
- [ ] Self-scoring rubric with objective 0-10 criteria
- [ ] Enhancement protocol with clear thresholds (< 8.0, 8.0-8.9, ≥ 9.0)
- [ ] Minimum standards specified (200+ words, 2+ examples, 12+ patterns)

**Technique Integration:**
- [ ] Chain-of-Thought for reasoning (step-by-step triggers)
- [ ] Socratic questioning for critical analysis (evidence scrutiny, assumption challenge)
- [ ] Quality gates for standards enforcement (if/then conditions)
- [ ] Self-improvement loop (score → enhance → re-score)
- [ ] Multi-perspective when appropriate (stakeholder analysis)

**Output Requirements:**
- [ ] Success criteria checklist provided
- [ ] Pattern quality standard defined (6 elements: name, context, structure, steps, example, pitfalls)
- [ ] Format requirements explicit (word counts, example counts)
- [ ] Source quality hierarchy specified (official > research > production > community)

---

## Part 7: Usage Workflow

### For LLMs Generating Prompts from These Templates

**Step 1: Understand User Need**
- Is this comprehensive research (Template A) or strategic decision (Template B)?
- What is the specific topic or decision?
- What context and constraints exist?

**Step 2: Select and Adapt Template**
- Copy appropriate template (A or B)
- Replace all [bracketed placeholders] with specific content
- Customize question clusters for the topic
- Adjust stakeholder perspectives to match domain

**Step 3: Customize Quality Standards**
- Ensure rubric criteria match user's quality expectations
- Adjust enhancement thresholds if needed (default: 8.5/10 target)
- Verify pattern requirements fit the domain

**Step 4: Add Domain-Specific Elements**
- Include relevant examples from the domain
- Reference authoritative sources specific to the topic
- Adjust terminology to match user's context

**Step 5: Validate Completeness**
- Run through quality checklist (Part 6)
- Confirm all techniques are properly integrated
- Verify thinking triggers are present throughout

**Step 6: Deliver to User**
- Provide the complete, customized prompt
- Explain: "Copy this entire prompt and paste into Gemini Deep Research at google.com/gemini"
- Set expectations: "You'll receive 500-2,000 lines of detailed research prose"

---

## Conclusion

**Quality Formula for Web UI Prompts:**
```
Optimal Output = Thinking Mechanism Activation
                + Multi-Technique Combination (4-6 techniques)
                + Structured Workflow Design
                + Self-Enhancement Loops
                + Objective Quality Gates
```

**Core Principles for Effective Prompts:**
1. **Trigger Gemini's Thinking** with explicit reasoning phrases
2. **Combine 4-6 complementary techniques** (not more - avoid overload)
3. **Structure as complete workflows** with clear phases
4. **Build quality loops** (generate → score → enhance → validate)
5. **Specify objective standards** with measurable criteria
6. **Prioritize actionability** over abstract theory

**Expected Results:**
When these elements align properly, Gemini 2.5 Pro consistently produces:
- 9-10/10 quality research outputs
- 1,500-2,000 lines for comprehensive research (Template A)
- 500-800 lines for strategic decisions (Template B)
- Immediately actionable patterns and recommendations
- Evidence-backed findings with authoritative sources

**Critical Reminder:**
These templates are for **PATH 1 (Web UI)** use only. They generate human-readable prose for interactive research. For API automation (PATH 2), see separate templates in `docs/api/templates/`.

---

**Last Updated:** 2025-11-13 23:45 AEDT  
**Status:** Production-Ready  
**Evidence Base:** Derived from 1,582 lines of academic research on Gemini 2.5 Pro  
**Validation:** Templates consistently produce 9-10/10 quality outputs when properly applied
