# Guide for Claude: Using the Gemini Research Framework

**Created:** 2025-11-14 00:35 AEDT  
**Purpose:** How Claude (and Claude Desktop users) should use this framework  
**Audience:** Claude instances helping users generate Gemini research prompts

---

## Quick Start for Claude

**Your Mission:** Help users generate effective Gemini research prompts

**Simple Process:**
1. Read `FRAMEWORK_GUIDE.md` first (if not already familiar)
2. Read `gemini_capabilities.md` → Know what Gemini can do
3. Read `technique_library.md` → Select 4-6 compatible techniques
4. Read `web_ui_templates.md` → Adapt Template A or B
5. Customize for user's specific topic
6. Deliver complete prompt with explanation

**Expected Output:** User receives ready-to-paste prompt for Gemini Deep Research

---

## Reading Order for Claude

### Essential Docs (Read Every Time)

**1. `FRAMEWORK_GUIDE.md` (536 lines)**
- Purpose: Understand entire framework structure
- When: First time using framework, or context reset
- Contains: Repository overview, reading paths, workflow examples

**2. `docs/reference/gemini_capabilities.md` (696 lines)**
- Purpose: Know what Gemini 2.5 Pro can do
- When: Every prompt generation task
- Contains: Architecture, 12 tested techniques with scores, API parameters, limitations

**3. `docs/reference/technique_library.md` (1,438 lines)**
- Purpose: Select appropriate techniques
- When: Every prompt generation task
- Contains: All 17 techniques, implementation examples, compatibility matrix, selection guide

**4. `docs/methodology/templates/web_ui_templates.md` (899 lines)**
- Purpose: Get production-ready template structure
- When: Every prompt generation task
- Contains: Template A (Comprehensive), Template B (Strategic Decision), quality frameworks

### Reference Docs (Consult as Needed)

**5. `docs/methodology/principles/core_discoveries.md` (413 lines)**
- Purpose: Understand why techniques work
- When: Need deeper understanding, troubleshooting, optimization
- Contains: Instruction adherence trade-off, tier classifications, anti-patterns

**6. `docs/enhancements/unified_methodology.md` (684 lines)**
- Purpose: Learn integration strategies
- When: Combining approaches, building custom workflows, advanced use
- Contains: Claude + ChatGPT branch comparison, hybrid examples, validation strategies

---

## Workflow Example: Comprehensive Research

**User Request:** "Generate a Gemini research prompt for database sharding strategies"

### Step 1: Understand Gemini's Capabilities

```
Action: Read gemini_capabilities.md

Key findings for this task:
- Architecture: 1M token context (can handle extensive analysis)
- Thinking mechanism: Activate with "Let's think step by step"
- Relevant techniques:
  * Chain-of-Thought: 10/10 effectiveness, 10/10 reliability
  * Socratic Questioning: 10/10 effectiveness, 8/10 reliability
  * Multi-Agent Simulation: 10/10 effectiveness, 9/10 reliability
  * Self-Scoring: 10/10 effectiveness, 9/10 reliability
  * Long-Context Reasoning: 10/10 effectiveness, 8/10 reliability
```

### Step 2: Select Techniques

```
Action: Read technique_library.md (selection guide section)

For comprehensive research:
✓ Chain-of-Thought (foundation - always use)
✓ Socratic Questioning (critical analysis of trade-offs)
✓ Multi-Agent Simulation (Developer, DBA, Architect perspectives)
✓ Self-Scoring (quality assurance with rubric)
✓ Quality Gates (pattern completeness check)
✓ Long-Context (synthesize multiple sharding approaches)

Total: 6 techniques (optimal range: 4-6 ✓)

Compatibility check:
- CoT + Socratic: ✅ Excellent pairing
- Multi-Agent + CoT: ✅ Natural fit
- Self-Scoring + Quality Gates: ✅ Powerful combo
- All compatible with Long-Context: ✅
```

### Step 3: Apply Template

```
Action: Read web_ui_templates.md

Choose: Template A (Comprehensive Foundation Research)
Reason: Systematic coverage needed, multiple aspects to explore

Template Structure:
- Role Definition (senior database architect)
- Phase 1: Systematic Investigation (18 questions about sharding)
- Phase 2: Critical Synthesis (Socratic analysis)
- Phase 3: Pattern Extraction (12+ actionable patterns)
- Self-Scoring Assessment (7 criteria, 0-10 scale)
- Self-Enhancement Protocol (refine if < 8.5/10)
```

### Step 4: Customize for Topic

```
Replace template placeholders:

[TOPIC] → "Database Sharding Strategies"

Questions (examples):
Q1: What are the fundamental approaches to database sharding?
    - Sub: Key-based vs range-based vs directory-based
    - Sub: Horizontal vs vertical partitioning
    - Sub: When to use each approach

Q2: How do different sharding strategies affect query performance?
    - Sub: Single-shard queries vs cross-shard queries
    - Sub: Aggregation complexity
    - Sub: Index strategies per shard

[... continue for 18 questions covering all aspects]

Multi-Agent Perspectives:
- Persona 1: Senior DBA (operational concerns)
- Persona 2: Application Developer (code complexity)
- Persona 3: System Architect (scalability/maintainability)

Pattern Requirements:
- Must include: Name, Context, Structure, Steps, Example, Pitfalls
- Each pattern = complete implementation guide
```

### Step 5: Generate Complete Prompt

```markdown
# Database Sharding Strategies: Comprehensive Research

## ROLE DEFINITION
You are a senior database architect with 15+ years experience designing 
large-scale distributed data systems. Your approach combines practical 
implementation experience with theoretical foundations...

[Complete customized prompt following Template A structure]

## SUCCESS CRITERIA
- ✅ All 18 questions answered (200+ words each, 2+ examples)
- ✅ 12+ template-ready patterns extracted
- ✅ Multi-perspective analysis complete (DBA, Developer, Architect)
- ✅ Socratic critical evaluation performed
- ✅ Self-scored ≥8.5/10 across all criteria
...
```

### Step 6: Deliver to User

```
I've generated a comprehensive Gemini research prompt for database sharding strategies.

**What this prompt does:**
- Systematically explores 18 key aspects of database sharding
- Analyzes from 3 expert perspectives (DBA, Developer, Architect)
- Includes critical Socratic questioning of trade-offs
- Extracts 12+ actionable implementation patterns
- Self-assesses quality and refines if needed

**Expected output from Gemini:**
- 1,500-2,000 lines of detailed analysis
- Complete coverage of sharding approaches
- Production-ready patterns with examples
- Critical evaluation of trade-offs

**How to use:**
1. Copy the entire prompt below
2. Go to google.com/gemini (Gemini Deep Research)
3. Paste the prompt
4. Wait for comprehensive research output (~2-3 minutes)

---

[COMPLETE PROMPT TEXT]

---

Let me know if you'd like me to adjust the depth, add specific aspects, 
or modify the approach.
```

---

## Workflow Example: Strategic Decision

**User Request:** "Should we migrate from PostgreSQL to MongoDB?"

### Claude's Process

**Step 1: Recognize Decision Context**
```
This is a strategic decision → Use Template B
User needs clear recommendation, not just information
```

**Step 2: Select Decision-Focused Techniques**
```
From technique_library.md (selection guide for strategic decisions):
✓ Chain-of-Thought (structured analysis)
✓ Multi-Agent Simulation (stakeholders: Developer, DBA, DevOps)
✓ Tree of Thoughts (explore PostgreSQL optimization vs MongoDB migration)
✓ Socratic Questioning (challenge "MongoDB is better" assumption)
✓ Self-Scoring (evaluate recommendation quality)

Total: 5 techniques ✓
```

**Step 3: Customize Template B**
```
Decision: PostgreSQL to MongoDB migration?
Current State: PostgreSQL with [user's specifics]
Constraints: [team size, timeline, data model]
Success Criteria: [scalability, performance, maintainability]

Options to analyze:
1. Stay with PostgreSQL + optimization
2. Migrate to MongoDB completely
3. Hybrid approach (polyglot persistence)
```

**Step 4: Generate & Deliver**
```
Provide complete Template B prompt customized for this decision,
with explanation that output will include:
- Clear recommendation (not "it depends")
- Thorough options analysis
- Stakeholder perspectives considered
- Consequence forecasting (short/medium/long-term)
- Implementation path if recommendation is "migrate"
```

---

## Integration with ClaudeWorkflow

### Using Desktop Commander

**Access Framework Docs:**
```
# Read capabilities reference
desktop-commander:read_file /Users/dudley/Projects/Gemini-Research/docs/reference/gemini_capabilities.md

# Check technique compatibility
desktop-commander:read_file /Users/dudley/Projects/Gemini-Research/docs/reference/technique_library.md

# Get template structure
desktop-commander:read_file /Users/dudley/Projects/Gemini-Research/docs/methodology/templates/web_ui_templates.md
```

**Workflow:**
1. User asks for Gemini research prompt
2. Use Desktop Commander to read relevant framework docs
3. Generate customized prompt
4. Provide to user with usage instructions

### Project Knowledge Integration

**If Framework Added to Claude Project:**
- All docs available in context automatically
- No need to explicitly read files
- Can reference across entire framework
- Faster prompt generation

**Setup:**
1. Add `/Users/dudley/Projects/Gemini-Research/docs/` to Project Knowledge
2. Framework automatically available in all conversations
3. Claude can reference any doc as needed

---

## Claude-Specific Best Practices

### 1. Always Provide Context

**Don't:**
```
Here's your prompt: [dump large text]
```

**Do:**
```
I've created a comprehensive research prompt using:
- Template A (Comprehensive Foundation Research)
- 6 techniques: CoT, Socratic, Multi-Agent, Self-Scoring, Quality Gates, Long-Context
- Expected output: 1,500-2,000 lines

What this prompt does:
[Explain the approach]

How to use:
[Clear instructions]

[PROMPT]
```

### 2. Explain Technique Selection

**Don't:**
```
[Just provide prompt without explanation]
```

**Do:**
```
I selected these techniques because:
- Chain-of-Thought: Systematic reasoning through complex topic
- Socratic: Your question involves trade-offs that need critical analysis
- Multi-Agent: Multiple stakeholder perspectives relevant
- Self-Scoring: Ensures quality meets your standards (≥8.5/10)
```

### 3. Offer Customization

**Don't:**
```
Here's the prompt. [End]
```

**Do:**
```
Here's the prompt. Let me know if you'd like me to:
- Adjust depth (more/less detail)
- Change focus (emphasize certain aspects)
- Modify perspectives (different stakeholders)
- Add specific examples or constraints
```

### 4. Validate Compatibility

**Before generating, mentally check:**
- Are selected techniques compatible? (Check compatibility matrix)
- Is technique count 4-6? (Optimal range)
- Does template match use case? (Template A for research, B for decisions)
- Are thinking triggers included? ("Let's think step by step")

### 5. Handle Edge Cases

**User asks for quick summary:**
```
That's not ideal for Gemini's strengths. Gemini excels at deep, 
comprehensive analysis (1,500-2,000 lines). For quick summaries, 
consider using me (Claude) directly, or ChatGPT with GPT-4.

If you still want a Gemini prompt for faster output, I can create 
one with fewer techniques and lighter thinking budget, but quality 
will be reduced.
```

**User asks for API execution:**
```
The templates I have are optimized for Web UI (PATH 1). For API 
execution (PATH 2), you'd need:
- JSON schema-based prompt structure
- API parameter configuration (thinkingBudget, responseSchema, etc.)
- Different output format (structured JSON vs prose)

See docs/api/applications/v4.8.1_api_prompt.md for API approach.
```

---

## Common Scenarios

### Scenario 1: User New to Gemini

**User:** "I've never used Gemini before. Can you help?"

**Claude's Response:**
```
Absolutely! Gemini 2.5 Pro excels at comprehensive research and analysis. 
Here's how we'll work together:

1. You tell me what you want to research (e.g., "microservices patterns")
2. I generate a detailed research prompt optimized for Gemini
3. You copy that prompt → paste into google.com/gemini
4. Gemini produces 1,500-2,000 lines of detailed analysis
5. You review the research Gemini provides

Gemini is particularly good at:
- Systematic, comprehensive research
- Multi-perspective analysis
- Extracting actionable patterns
- Critical evaluation of trade-offs

What would you like to research?
```

### Scenario 2: User Wants Faster Output

**User:** "Can I get a shorter research output?"

**Claude's Response:**
```
Yes, I can adapt the prompt for shorter output. However, there's a trade-off:

Gemini's strength is comprehensive, deep research (1,500-2,000 lines). 
Shorter outputs (500-800 lines) are possible using Template B (Strategic 
Decision format), which focuses on synthesis rather than exhaustive coverage.

Would you prefer:
A) Comprehensive research (1,500-2,000 lines, Template A)
B) Focused strategic analysis (500-800 lines, Template B)
C) Quick summary (not Gemini's strength - I can provide this directly)

For most research needs, the comprehensive approach provides better value.
```

### Scenario 3: User Wants to Iterate

**User:** "The first research was good, but I need more depth on [aspect]"

**Claude's Response:**
```
Great! For iterative deepening, I recommend:

Option 1: Generate a focused follow-up prompt
- Use Template A but with 6-8 questions specifically on [aspect]
- Reference findings from first research
- Request deeper analysis and more examples

Option 2: Refine original prompt
- Add specific sub-questions about [aspect]
- Increase minimum word count for that section
- Request 5+ examples instead of 2+

Which approach would you prefer?
```

### Scenario 4: User Asks About Validation

**User:** "How do I know if the research quality is good?"

**Claude's Response:**
```
The prompts I generate include built-in quality assurance:

1. Self-Scoring Rubric (7 criteria, 0-10 scale):
   - Completeness, Evidence Quality, Depth, etc.
   - Gemini evaluates its own output
   - Target: ≥8.5/10 average

2. Enhancement Protocol:
   - If score < 8.5, Gemini refines automatically
   - Identifies weakest areas
   - Improves before delivering final output

3. Quality Gates:
   - Pattern completeness checks
   - Example requirements enforced
   - Source citation requirements

You'll see Gemini's self-assessment at the end of the research output.
If you're not satisfied, I can regenerate with stricter quality standards.
```

---

## Troubleshooting

### Issue: Generated Prompt Too Long

**Symptom:** Prompt exceeds Gemini's input limit

**Solution:**
```
I'll create a more concise version:
- Reduce question count (18 → 12 questions)
- Simplify instruction phrasing
- Remove optional sections
- Maintain core quality techniques

The output quality won't decrease significantly - the techniques 
are what matter, not prompt length.
```

### Issue: Output Not Comprehensive Enough

**Symptom:** Gemini output shorter or less detailed than expected

**Solution:**
```
Let me enhance the prompt with:
- Explicit minimum standards (200+ words per question)
- More thinking triggers ("Think deeply about...")
- Stronger quality gates (must include 3+ examples)
- Higher self-scoring threshold (≥9.0 instead of ≥8.5)

I'll regenerate with these adjustments.
```

### Issue: Output Too Generic

**Symptom:** Gemini provides generic information, not specific to user's context

**Solution:**
```
I need more context to customize the prompt:
- What specific problem are you trying to solve?
- What's your current situation/constraints?
- What decisions will this research inform?
- Are there specific examples or use cases relevant to you?

With these details, I can make the prompt much more targeted.
```

### Issue: User Confused About Next Steps

**Symptom:** User doesn't know what to do with Gemini's output

**Solution:**
```
After Gemini completes the research, you can:

1. Read it directly (comprehensive reference)
2. Ask me to summarize key findings
3. Ask me to extract specific information
4. Use it to inform your decision/project
5. Request follow-up research on specific aspects

Would you like me to help you process the Gemini output?
```

---

## Advanced: Combining with Claude's Capabilities

### Workflow: Claude + Gemini Partnership

**Step 1: Claude helps define research scope**
```
User: "I need to choose a database"
Claude: "Let me help you clarify what to research..."
[Discussion to define requirements, constraints, priorities]
```

**Step 2: Claude generates Gemini prompt**
```
Claude: "Based on our discussion, here's a targeted research prompt 
for Gemini focusing on [specific aspects]..."
```

**Step 3: User gets research from Gemini**
```
User: [Pastes prompt into Gemini]
Gemini: [Produces 1,500-2,000 lines of research]
```

**Step 4: Claude helps process results**
```
User: [Shares Gemini output with Claude]
Claude: "Looking at this research, the key findings for your specific 
situation are... My recommendation based on this analysis is..."
```

**Result:** Claude's conversational intelligence + Gemini's research depth

---

## Summary: Claude's Role

**You Are:**
- ✅ The translator (user needs → Gemini prompt)
- ✅ The expert (select right techniques)
- ✅ The guide (explain process and results)
- ✅ The customizer (adapt to user's specific needs)

**You Are Not:**
- ❌ Doing the research yourself (that's Gemini's job)
- ❌ Creating prompts from scratch (use templates)
- ❌ Inventing techniques (use documented ones)

**Your Value:**
- Understanding user's true needs
- Selecting optimal framework components
- Generating production-ready prompts
- Explaining process clearly
- Helping process results

---

## Quick Reference

**Essential Reading:**
1. `FRAMEWORK_GUIDE.md` (overview)
2. `gemini_capabilities.md` (what Gemini can do)
3. `technique_library.md` (technique selection)
4. `web_ui_templates.md` (template structure)

**For Every Prompt:**
- ✅ Select 4-6 compatible techniques
- ✅ Include thinking triggers
- ✅ Use Template A (research) or B (decisions)
- ✅ Add self-scoring rubric
- ✅ Set quality threshold (≥8.5/10)
- ✅ Provide clear success criteria

**Common Pitfalls to Avoid:**
- ❌ >6 techniques (overload)
- ❌ Incompatible technique combinations
- ❌ Vague quality standards
- ❌ No thinking triggers
- ❌ Creating from scratch vs adapting templates

**Version:** 1.0  
**Last Updated:** 2025-11-14 00:35 AEDT  
**Status:** Production-ready guide for Claude
