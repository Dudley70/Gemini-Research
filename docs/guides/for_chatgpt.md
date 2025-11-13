# Guide for ChatGPT: Using the Gemini Research Framework

**Created:** 2025-11-14 00:40 AEDT  
**Purpose:** How ChatGPT should use this framework to generate Gemini prompts  
**Audience:** ChatGPT instances (including Custom GPTs) helping users generate research prompts

---

## Quick Start for ChatGPT

**Your Mission:** Generate effective Gemini research prompts for users

**Simple Process:**
1. Read `FRAMEWORK_GUIDE.md` (comprehensive overview)
2. Read `gemini_capabilities.md` → Understand Gemini's strengths
3. Read `technique_library.md` → Select 4-6 compatible techniques
4. Read `web_ui_templates.md` → Apply Template A or B
5. Customize for user's topic
6. Deliver complete, ready-to-paste prompt

**Expected Result:** User copies prompt → pastes into Gemini → receives high-quality research

---

## Reading Order for ChatGPT

### Essential Docs (Read Every Time)

**1. `FRAMEWORK_GUIDE.md` (536 lines)**
- Purpose: Complete framework overview
- When: First time, or whenever context resets
- Contains: Structure, reading paths, workflow examples, key concepts

**2. `docs/reference/gemini_capabilities.md` (696 lines)**
- Purpose: Know what Gemini 2.5 Pro can do
- When: Every prompt generation
- Contains: Architecture specs, 12 tested techniques with scores, API parameters, limitations

**3. `docs/reference/technique_library.md` (1,438 lines)**
- Purpose: Select appropriate techniques
- When: Every prompt generation
- Contains: All 17 techniques with implementation details, compatibility matrix, selection guide

**4. `docs/methodology/templates/web_ui_templates.md` (899 lines)**
- Purpose: Get template structure
- When: Every prompt generation
- Contains: Template A (Comprehensive), Template B (Strategic), quality frameworks, examples

### Integration Docs (For Advanced Use)

**5. `docs/enhancements/unified_methodology.md` (684 lines)**
- Purpose: Understand ChatGPT + Claude integration
- When: Building Custom GPTs, combining approaches
- Contains: Branch comparison, hybrid examples, validation strategies, Custom GPT guide

**6. `docs/analysis/chatgpt_v1.3.0_pack/`** (11 files)
- Purpose: Reference original ChatGPT automation approach
- When: Building on existing ChatGPT Pack patterns
- Contains: Preset system, compliance validation, project configs

---

## Workflow Example: Generate Research Prompt

**User Request:** "Generate a Gemini prompt to research Kubernetes deployment patterns"

### Step 1: Understand Gemini's Capabilities

```
Read: gemini_capabilities.md

Key capabilities for this task:
✓ 1M token context (can analyze extensive patterns)
✓ Thinking mechanism (allocate budget for deep reasoning)
✓ Long-context reasoning: 10/10 effectiveness
✓ Chain-of-Thought: 10/10 effectiveness, 10/10 reliability
✓ Multi-Agent Simulation: 10/10 effectiveness, 9/10 reliability
✓ Self-Scoring: 10/10 effectiveness, 9/10 reliability

Architecture: MoE transformer, thinking budget 128-32,768 tokens
```

### Step 2: Select Techniques

```
Read: technique_library.md (selection guide)

For comprehensive research on patterns:
1. Chain-of-Thought (reasoning foundation - always include)
2. Long-Context Reasoning (synthesize many patterns)
3. Multi-Agent Simulation (DevOps, Developer, SRE perspectives)
4. Self-Scoring (quality assurance via rubric)
5. Quality Gates (pattern completeness enforcement)
6. Socratic Questioning (critical evaluation of trade-offs)

Total: 6 techniques ✓ (optimal: 4-6)

Compatibility check via matrix:
- All selected techniques compatible ✓
- CoT pairs excellently with all others ✓
- Multi-Agent + Socratic = powerful combination ✓
```

### Step 3: Choose Template

```
Read: web_ui_templates.md

Decision: Template A (Comprehensive Foundation Research)
Reason: Need systematic coverage of multiple deployment patterns

Template provides:
- Structured question clusters
- Socratic critical thinking framework
- Pattern extraction section (12+ patterns required)
- Self-scoring rubric (7 criteria, 0-10 scale)
- Enhancement protocol (refine if score < 8.5/10)
```

### Step 4: Customize for Topic

```
Adapt Template A for Kubernetes:

Topic: "Kubernetes Deployment Patterns"

Question Clusters:
Cluster 1: Core Deployment Patterns (6 questions)
- Blue-Green deployments
- Canary deployments
- Rolling updates
- Recreate strategy
- A/B testing
- Shadow deployments

Cluster 2: Advanced Patterns (6 questions)
- Multi-cluster deployments
- GitOps workflows
- Service mesh integration
- StatefulSet patterns
- DaemonSet use cases
- Job/CronJob patterns

Cluster 3: Production Considerations (6 questions)
- Health checks and probes
- Resource management
- Security patterns
- Monitoring and observability
- Disaster recovery
- Cost optimization

Multi-Agent Perspectives:
- Persona 1: DevOps Engineer (operational reliability)
- Persona 2: Application Developer (deployment simplicity)
- Persona 3: SRE (observability and troubleshooting)

Pattern Requirements:
Each of 12+ patterns must include:
- Name, Context, Structure, Steps, Example (YAML), Pitfalls
```

### Step 5: Generate Complete Prompt

```markdown
# Kubernetes Deployment Patterns: Comprehensive Research

## ROLE DEFINITION
You are a senior DevOps architect specializing in Kubernetes with 10+ 
years of container orchestration experience. Your approach combines 
production battle-tested patterns with deep understanding of 
Kubernetes internals...

[Complete customized prompt with all 6 techniques integrated]

## SUCCESS CRITERIA
- ✅ All 18 questions answered (200+ words each, 2+ examples with YAML)
- ✅ 12+ deployment patterns extracted (complete with code examples)
- ✅ Multi-perspective analysis (DevOps, Developer, SRE)
- ✅ Socratic critical evaluation complete
- ✅ Self-scored ≥8.5/10 across all 7 criteria
...
```

### Step 6: Deliver to User

```
I've created a comprehensive Gemini research prompt for Kubernetes deployment patterns.

**What you'll get from Gemini:**
- 1,500-2,000 lines of detailed analysis
- 18 key aspects of K8s deployments covered
- 12+ production-ready patterns with YAML examples
- Analysis from DevOps, Developer, and SRE perspectives
- Critical evaluation of trade-offs and best practices

**How to use:**
1. Copy the entire prompt below
2. Go to https://google.com/gemini (Gemini Deep Research)
3. Paste the prompt
4. Submit and wait 2-3 minutes for comprehensive output

---

[COMPLETE PROMPT]

---

The prompt includes self-assessment and will refine itself if quality 
is below 8.5/10. Let me know if you'd like any adjustments!
```

---

## ChatGPT v1.3.0 Pack Integration

### Leveraging the Preset System

**The v1.3.0 Pack Presets:**
- `tier1_deep_dive`: thinkingBudget 32768 (maximum depth)
- `tier2_standard_report`: thinkingBudget 16384 (balanced)
- `tier3_fast_summary`: thinkingBudget 8192 (quick insights)
- `multimodal_analysis`: Image/PDF/video processing

**How to Integrate:**

```
User request → Determine depth needed → Select preset → Apply framework template

Example:
"Deep research on X" → tier1_deep_dive → Template A + 6 techniques
"Quick analysis of Y" → tier3_fast_summary → Template B + 4 techniques
"Analyze this diagram" → multimodal_analysis → Custom multimodal prompt
```

**Preset Configuration:**
```json
{
  "tier1_deep_dive": {
    "framework_template": "A (Comprehensive)",
    "technique_count": 6,
    "techniques": ["CoT", "Socratic", "Multi-Agent", "Self-Scoring", "Quality Gates", "Long-Context"],
    "output_expectation": "1500-2000 lines",
    "thinking_trigger": "Think deeply about each aspect. Allocate maximum thinking budget."
  },
  "tier2_standard": {
    "framework_template": "B (Strategic Decision)",
    "technique_count": 5,
    "techniques": ["CoT", "Multi-Agent", "Tree of Thoughts", "Self-Scoring", "Quality Gates"],
    "output_expectation": "500-800 lines",
    "thinking_trigger": "Let's think step by step through this decision."
  }
}
```

### Combining Pack Validation with Framework Templates

**Unified Approach:**

1. **Use Framework Templates** (this repo) for prompt structure
2. **Use Pack Presets** for configuration and depth control
3. **Use Pack Validation** (Gate 0) for compliance checking

**Example Workflow:**
```
1. User request: "Research topic X"
2. Select preset: tier1_deep_dive
3. Load framework: Template A from web_ui_templates.md
4. Select techniques: 6 from technique_library.md
5. Generate prompt: Customize Template A
6. Validate: Run Gate 0 compliance check (from Pack)
7. Deliver: Complete, validated prompt
```

**Gate 0 Compliance Check (from ChatGPT Pack):**
```
✓ Role definition present
✓ Thinking triggers included
✓ Output structure specified
✓ Quality rubric defined
✓ Success criteria listed
✓ Pattern extraction section included
```

---

## Building a Custom GPT with This Framework

### Knowledge Base Setup

**Add These Docs to Custom GPT Knowledge:**
1. `FRAMEWORK_GUIDE.md` (entry point)
2. `docs/reference/gemini_capabilities.md` (Gemini specs)
3. `docs/reference/technique_library.md` (all techniques)
4. `docs/methodology/templates/web_ui_templates.md` (templates)
5. `docs/enhancements/unified_methodology.md` (integration guide)

**Total:** ~4,600 lines of reference material

### Custom GPT Instructions

```markdown
You are a Gemini Research Prompt Generator. Your purpose is to create 
high-quality research prompts optimized for Gemini 2.5 Pro.

**Process:**
1. Understand user's research need (ask clarifying questions if needed)
2. Consult gemini_capabilities.md to know what Gemini can do
3. Select 4-6 compatible techniques from technique_library.md
4. Apply Template A (comprehensive) or Template B (strategic decision)
5. Customize template for user's specific topic
6. Generate complete, ready-to-paste prompt

**Quality Standards:**
- Include thinking triggers ("Let's think step by step")
- Use 4-6 compatible techniques (check compatibility matrix)
- Include self-scoring rubric (7 criteria, 0-10 scale)
- Set quality threshold (≥8.5/10)
- Provide clear success criteria

**Presets:**
- Deep Research: Template A + 6 techniques + max thinking
- Standard Analysis: Template B + 5 techniques + balanced
- Quick Insights: Template B + 4 techniques + lighter

**Output:**
Provide complete prompt with:
1. Brief explanation of approach
2. Expected output description
3. Usage instructions (copy → paste to google.com/gemini)
4. Complete prompt text

Always reference the framework documentation in your knowledge base.
```

### Custom GPT Conversation Starters

```
1. "Generate a deep research prompt for [topic]"
2. "Create a strategic decision prompt for [choice]"
3. "Help me research [complex topic] comprehensively"
4. "I need to decide between [A] and [B]"
```

---

## ChatGPT-Specific Best Practices

### 1. Structured Output

**Advantage:** ChatGPT handles structured formats well

**Use It:**
```
I've generated your Gemini research prompt.

**Approach:**
- Template: A (Comprehensive Foundation Research)
- Techniques: 6 selected (CoT, Socratic, Multi-Agent, Self-Scoring, Quality Gates, Long-Context)
- Expected Output: 1,500-2,000 lines of detailed analysis

**How It Works:**
[Bulleted explanation]

**Usage:**
1. Copy prompt below
2. Paste into google.com/gemini
3. Wait 2-3 minutes

**Prompt:**
[Complete prompt in code block]
```

### 2. Preset-Based Efficiency

**Leverage:** ChatGPT's ability to work with configurations

**Pattern:**
```
User: "Research X"
ChatGPT: [Internally: tier1_deep_dive preset]
         [Load: Template A configuration]
         [Select: 6 techniques]
         [Generate: Customized prompt]
         [Output: Complete prompt with explanation]
```

### 3. Validation Automation

**From ChatGPT Pack:** Gate 0 Preflight

**Apply to Framework Prompts:**
```
Before delivering prompt, validate:
✓ All mandatory sections present
✓ Thinking triggers included
✓ Quality rubric defined
✓ Success criteria clear
✓ Technique count: 4-6
✓ Techniques compatible (check matrix)

If validation fails → Fix before delivery
```

### 4. Iterative Refinement

**ChatGPT Strength:** Quick iterations

**Use It:**
```
User: "Make it more detailed"
ChatGPT: [Adjust: Increase question count 12→18]
         [Add: More sub-components per question]
         [Enhance: Require 3+ examples instead of 2+]
         [Regenerate: Updated prompt]

User: "Focus more on X aspect"
ChatGPT: [Rebalance: Add 6 questions specifically on X]
         [Maintain: Other aspects at appropriate depth]
         [Regenerate: Refocused prompt]
```

---

## Common Scenarios for ChatGPT

### Scenario 1: User Asks for Quick Summary

**User:** "Just give me a quick summary of [topic]"

**ChatGPT Response:**
```
Gemini 2.5 Pro is optimized for deep, comprehensive research (1,500-2,000 lines), 
not quick summaries. For quick summaries, I can provide that directly here.

However, if you want Gemini's comprehensive analysis that you can reference 
later, I can generate a lighter research prompt (500-800 lines using 
Template B with 4 techniques).

Which would you prefer:
A) Quick summary from me now (2-3 paragraphs)
B) Lighter Gemini research prompt (500-800 lines, still detailed)
C) Full Gemini comprehensive research (1,500-2,000 lines, exhaustive)
```

### Scenario 2: User Provides Project Context

**User:** "I'm building [project]. Research [technology]."

**ChatGPT Response:**
```
Perfect! I'll customize the research prompt for your specific project context.

Let me clarify a few things to make this highly relevant:
1. What's your current tech stack?
2. What specific problem are you trying to solve?
3. Any constraints (timeline, team size, budget)?
4. What decision will this research inform?

[After getting answers]

I've generated a project-specific research prompt that:
- Focuses on aspects relevant to [project]
- Considers your constraints ([specifics])
- Analyzes from perspectives of [relevant roles]
- Provides patterns you can immediately apply

[Complete customized prompt]
```

### Scenario 3: User Wants Multiple Topics

**User:** "Research topics A, B, and C"

**ChatGPT Response:**
```
I can create research prompts for all three topics. 

For efficiency, I recommend:
Option 1: Three separate prompts (best depth for each)
Option 2: One unified prompt covering all three (finds connections)

For Option 1:
- Each gets Template A treatment (full depth)
- Run sequentially in Gemini
- ~1,500-2,000 lines per topic

For Option 2:
- Single comprehensive prompt
- Analyzes connections between topics
- ~2,500-3,000 lines total
- Better for seeing relationships

Which approach works better for your needs?
```

### Scenario 4: User Gives Vague Request

**User:** "Research AI"

**ChatGPT Response:**
```
"AI" is a broad topic! To generate an effective research prompt, I need 
to narrow the focus. What aspect of AI are you interested in?

Examples:
- AI architectures (transformers, CNNs, RNNs)
- AI applications (computer vision, NLP, reinforcement learning)
- AI deployment (serving, scaling, monitoring)
- AI ethics (bias, fairness, transparency)
- AI tools (frameworks, platforms, services)
- Specific technique (few-shot learning, transfer learning, etc.)

Or describe your goal:
- "Learn how AI works"
- "Choose AI tool for [project]"
- "Understand AI impact on [industry]"

This helps me create targeted, useful research.
```

---

## Advanced: Hybrid Workflows

### Workflow 1: ChatGPT Generates → User Executes → ChatGPT Processes

**Step 1:** ChatGPT generates research prompt
```
"Here's your Gemini research prompt for [topic]..."
```

**Step 2:** User pastes into Gemini, gets results
```
[Gemini produces 1,500-2,000 lines of research]
```

**Step 3:** User shares results with ChatGPT
```
User: "Here's what Gemini found: [research output]"
ChatGPT: "Let me extract the key insights for your specific situation..."
[Summarizes, highlights, recommends based on Gemini's research]
```

**Result:** Gemini's depth + ChatGPT's synthesis

### Workflow 2: Preset-Based Batch Generation

**Scenario:** User needs prompts for 10 related topics

**ChatGPT Process:**
```
1. Identify common structure across topics
2. Select appropriate preset (tier2_standard)
3. Load Template B base
4. Generate 10 variations:
   For each topic:
   - Customize Template B
   - Maintain consistent structure
   - Apply same 5 techniques
   - Validate via Gate 0
5. Deliver all 10 prompts
```

**User Benefit:** Consistent quality across batch, efficient generation

### Workflow 3: Progressive Refinement

**Round 1:** Initial prompt
```
User: "Research X"
ChatGPT: [Generates comprehensive Template A prompt]
```

**Round 2:** Refine based on feedback
```
User: "Need more depth on aspect Y"
ChatGPT: [Regenerates with 6 questions on Y, maintains overall structure]
```

**Round 3:** Optimize
```
User: "Can you make it shorter but keep depth on Y?"
ChatGPT: [Reduces total questions to 12, keeps 6 on Y, condenses others]
```

**Result:** Iterative improvement until perfect fit

---

## Troubleshooting

### Issue: Prompt Too Long

**Solution:**
```
I'll create a more concise version by:
- Reducing question count (18 → 12)
- Simplifying instruction phrasing
- Removing optional sections
- Maintaining quality techniques

The effectiveness remains high - what matters is technique selection, 
not prompt length.
```

### Issue: Output Not Meeting Expectations

**Diagnosis Questions:**
```
1. Was the output too short? → Add stronger minimum standards
2. Was it too generic? → Need more project-specific context
3. Missing key aspects? → Add explicit questions for those aspects
4. Quality too low? → Increase self-scoring threshold (8.5 → 9.0)
```

### Issue: User Confused About Process

**Clarification:**
```
Here's the simple process:

1. I generate a research prompt (what you're reading now)
2. You copy the prompt text
3. You paste it into Gemini at google.com/gemini
4. Gemini does the research and gives you comprehensive output
5. You read Gemini's research output

I don't do the research myself - I create the prompt that tells Gemini 
how to do the research optimally.
```

---

## Quality Assurance Checklist

**Before Delivering Any Prompt, Verify:**

- [ ] Read gemini_capabilities.md for this session ✓
- [ ] Selected 4-6 techniques from technique_library.md ✓
- [ ] Checked technique compatibility matrix ✓
- [ ] Applied Template A or B from web_ui_templates.md ✓
- [ ] Included thinking triggers ✓
- [ ] Added self-scoring rubric (7 criteria) ✓
- [ ] Set quality threshold (≥8.5/10) ✓
- [ ] Defined success criteria clearly ✓
- [ ] Customized for user's specific context ✓
- [ ] Provided usage instructions ✓

**Optional (if using ChatGPT Pack):**
- [ ] Selected appropriate preset ✓
- [ ] Ran Gate 0 compliance validation ✓

---

## Summary: ChatGPT's Role

**Your Strengths:**
- ✅ Structured output and formatting
- ✅ Preset-based efficiency
- ✅ Validation automation
- ✅ Iterative refinement
- ✅ Batch generation

**Your Process:**
1. Understand user need (clarify if vague)
2. Select preset + techniques (from framework)
3. Apply template (A or B)
4. Customize for context
5. Validate (Gate 0 if available)
6. Deliver with explanation

**Your Value:**
- Converting user requests into optimized Gemini prompts
- Ensuring quality through validation
- Efficient batch operations
- Clear, structured delivery

---

## Quick Reference

**Essential Docs:**
1. `FRAMEWORK_GUIDE.md` - Complete overview
2. `gemini_capabilities.md` - What Gemini can do
3. `technique_library.md` - Technique selection + compatibility
4. `web_ui_templates.md` - Template A & B

**For Every Prompt:**
- ✅ 4-6 compatible techniques
- ✅ Thinking triggers included
- ✅ Template A (research) or B (decisions)
- ✅ Self-scoring rubric (7 criteria, ≥8.5/10)
- ✅ Clear success criteria

**ChatGPT Advantages:**
- Preset efficiency (tier1/2/3 from Pack)
- Validation automation (Gate 0)
- Structured delivery format
- Batch generation capability

**Avoid:**
- >6 techniques (overload)
- Incompatible combinations
- Creating from scratch (use templates)
- Vague quality standards
- Missing thinking triggers

**Version:** 1.0  
**Last Updated:** 2025-11-14 00:40 AEDT  
**Status:** Production-ready guide for ChatGPT
