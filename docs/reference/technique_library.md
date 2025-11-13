# Technique Library: Complete Catalog for Gemini 2.5 Pro

**Created:** 2025-11-14 00:10 AEDT  
**Purpose:** Comprehensive reference of all prompting techniques for Gemini 2.5 Pro  
**Coverage:** 12 tested techniques + 5 gap techniques = 17 total  
**Audience:** LLMs (ChatGPT, Claude, etc.) selecting techniques for prompt generation

**Navigation:**
- [Tested Techniques (12)](#tested-techniques) - Empirically validated with scores
- [Gap Techniques (5)](#gap-techniques) - Identified but not yet tested
- [Compatibility Matrix](#compatibility-matrix) - Which techniques work well together
- [Selection Guide](#selection-guide) - Choose techniques by use case

---

## How to Use This Library

**For Each Technique, You'll Find:**
1. **Definition** - What the technique does
2. **Scores** - Effectiveness (0-10) and Reliability (0-10) where tested
3. **When to Use** - Ideal scenarios and use cases
4. **How to Implement** - Concrete prompt patterns and examples
5. **API Support** - Whether API parameters exist (Tier 1 only)
6. **Compatibility** - What techniques combine well
7. **Pitfalls** - Common mistakes to avoid

**Tier Classification:**
- **Tier 1:** API-enforced (hard constraints, highest reliability)
- **Tier 2:** Emergent high-reliability (prompt-dependent, very effective)
- **Tier 3:** Promising (effective but lower reliability)
- **Gap:** Identified but not empirically tested in source research

---

## Tested Techniques

### Tier 1: API-Enforced Techniques

#### 1. JSON Schema Validation

**Definition:** Enforces structured JSON output using API-level schema validation

**Scores:** Effectiveness 10/10 | Reliability 9/10

**When to Use:**
- Data extraction requiring specific format
- Integration with downstream systems
- Standardizing outputs across multiple queries
- When format consistency is critical

**API Support:**
```json
{
  "response_mime_type": "application/json",
  "responseSchema": {
    "type": "object",
    "properties": {
      "field_name": {"type": "string"},
      "field_number": {"type": "integer"}
    },
    "required": ["field_name"]
  }
}
```

**How to Implement (Web UI - Educational Context):**
While Web UI doesn't support direct schema enforcement, you can describe the structure:

```markdown
Output Format: Return ONLY valid JSON with this exact structure:
{
  "findings": [
    {
      "topic": "string",
      "summary": "string",
      "confidence": "HIGH|MEDIUM|LOW"
    }
  ],
  "metadata": {
    "total_sources": integer,
    "date_range": "string"
  }
}

Do not include any text outside the JSON structure.
```

**Example Use Case:**
Extract structured data from research for automated processing

**Compatibility:**
- ✅ Excellent with: Grounding (structured sources), Meta-Reasoning (validate logic)
- ✅ Good with: Chain-of-Thought (reasoning before extraction)
- ⚠️ Caution: May conflict with creative/narrative outputs

**Pitfalls:**
- Requesting complex nested structures (start simple)
- Not providing examples of valid JSON
- Mixing JSON with prose output requests

---

#### 2. Grounding (Google Search Integration)

**Definition:** Integrates real-time web search with structured metadata for verification

**Scores:** Effectiveness 10/10 | Reliability 9/10 (as Evidence-Based Structured Output)

**When to Use:**
- Current events or time-sensitive information
- Fact verification requirements
- Citation-backed content generation
- When source attribution is critical

**API Support:**
```json
{
  "tools": [{"googleSearch": {}}]
}
```

**Returns Metadata:**
- `groundingChunks`: Source snippets with content
- `groundingSupports`: Indices linking claims to sources
- `searchEntryPoint`: Search query used
- `webResults`: URLs, titles, snippets

**How to Implement (Web UI):**
```markdown
Use Google Search to find current information about [topic].

For each claim you make:
1. Search for authoritative sources
2. Cite the source with URL
3. Include publication date when available
4. Note any conflicting information found

Required: Include a "Sources" section at the end with all URLs referenced.
```

**Example Use Case:**
Research current trends in AI regulation with cited sources

**Compatibility:**
- ✅ Excellent with: JSON Schema (structured citations), Chain-of-Thought (reason about sources)
- ✅ Good with: Self-Scoring (evaluate source quality)
- ⚠️ Caution: Adds latency; use only when current info needed

**Pitfalls:**
- Requesting search without clear information need
- Not specifying recency requirements
- Failing to validate source credibility in prompt

---

#### 3. Meta-Reasoning (Exposed Thoughts)

**Definition:** Exposes internal reasoning process for transparency and debugging

**Scores:** Effectiveness 10/10 | Reliability 9/10

**When to Use:**
- Understanding how Gemini approached a problem
- Debugging unexpected outputs
- Building user trust through transparency
- Validating reasoning steps

**API Support:**
```json
{
  "includeThoughts": true
}
```

**Returns:** Thought summaries alongside final response

**How to Implement (Web UI - Simulate):**
```markdown
Before providing your final answer, explicitly show your reasoning process:

REASONING PROCESS:
1. How I interpreted the question: [explanation]
2. What information I considered: [sources, facts]
3. What approach I chose: [methodology]
4. What trade-offs I evaluated: [alternatives considered]
5. How I arrived at my conclusion: [logic chain]

FINAL ANSWER:
[Your actual response]
```

**Example Use Case:**
Complex strategic decision requiring transparent reasoning

**Compatibility:**
- ✅ Excellent with: Chain-of-Thought (natural pairing), Socratic (expose assumptions)
- ✅ Good with: Self-Scoring (evaluate reasoning quality)
- ⚠️ Neutral: Most techniques benefit from explicit reasoning

**Pitfalls:**
- Requesting reasoning without using it (adds tokens without value)
- Not providing structure for reasoning output
- Conflating reasoning with final answer

---

#### 4. Thinking Mode Control

**Definition:** Controls computational budget allocated to internal reasoning

**Scores:** Effectiveness 10/10 | Reliability 10/10

**When to Use:**
- Complex analysis requiring deep reasoning
- Quality-critical tasks where speed is secondary
- Research and strategic decisions
- Optimizing cost-quality trade-offs

**API Support:**
```json
{
  "thinkingBudget": 24576  // Range: 128-32768, or -1 for dynamic
}
```

**Budget Guidelines:**
- `128-8192`: Light thinking (simple tasks)
- `16384`: High depth (complex analysis)
- `24576-32768`: Maximum depth (research, strategy)
- `-1`: Dynamic (Gemini decides based on complexity)

**How to Implement (Web UI - Trigger Deep Thinking):**
```markdown
IMPORTANT: This is a complex task requiring deep analysis.

Before responding, allocate significant thinking budget to:
1. Map the complete problem space
2. Consider multiple solution approaches
3. Evaluate trade-offs comprehensively
4. Anticipate second-order consequences

Think step by step through each aspect. Take your time to reason thoroughly.
```

**Example Use Case:**
Strategic architecture decision with long-term implications

**Compatibility:**
- ✅ Excellent with: ALL techniques (thinking benefits everything)
- ⚠️ Trade-off: Higher quality but slower and more expensive

**Pitfalls:**
- Using maximum budget for simple tasks (wasteful)
- Not triggering thinking for complex tasks (poor quality)
- Requesting speed AND maximum thinking (contradictory)

---

### Tier 2: Emergent High-Reliability Techniques

#### 5. Chain-of-Thought (CoT)

**Definition:** Explicit step-by-step reasoning before drawing conclusions

**Scores:** Effectiveness 10/10 | Reliability 10/10

**When to Use:**
- Multi-step problems
- Complex reasoning tasks
- Mathematical or logical problems
- ANY task benefiting from explicit reasoning

**Trigger Phrases:**
- "Let's think step by step"
- "Show your reasoning"
- "Work through this systematically"
- "Before answering, consider..."

**How to Implement:**
```markdown
Let's approach this step by step:

Step 1: [First logical step - what do we know?]
Step 2: [Second step - what can we infer?]
Step 3: [Third step - what implications follow?]
...
Step N: [Final step - what conclusion do we draw?]

Based on this reasoning, the answer is: [conclusion]
```

**Example Use Case:**
Calculate optimal database sharding strategy

```markdown
Question: Should we shard our database by user_id or region?

Let's think step by step:

Step 1: Analyze current data distribution
- 80% of queries filter by user_id
- 20% of queries filter by region
- User data is evenly distributed

Step 2: Consider access patterns
- User-based sharding: Most queries hit single shard
- Region-based sharding: Most queries hit multiple shards

Step 3: Evaluate operational complexity
- User-based: Simple routing logic
- Region-based: Complex cross-shard joins

Step 4: Assess scalability
- User-based: Linear scaling with users
- Region-based: Limited by number of regions

Conclusion: Shard by user_id due to better query performance and simpler operations.
```

**Compatibility:**
- ✅ Excellent with: ALL techniques (fundamental reasoning pattern)
- ✅ Natural pairing: Socratic (question each step), Self-Scoring (evaluate reasoning)

**Pitfalls:**
- Skipping steps (defeats the purpose)
- Using for trivially simple tasks (unnecessary overhead)
- Not explicitly requesting step-by-step format

---

#### 6. Socratic Questioning

**Definition:** Multi-stage critical thinking through structured questioning

**Scores:** Effectiveness 10/10 | Reliability 8/10

**When to Use:**
- Critical analysis requirements
- Challenging assumptions
- Strategic decision-making
- Research requiring depth and skepticism

**Five-Stage Framework:**
```markdown
## SOCRATIC ANALYSIS

### Stage 1: Gather and Scrutinize Evidence
- What evidence supports this conclusion?
- How credible and authoritative are the sources?
- Are there contradictions in the evidence?
- What is the recency and relevance?

### Stage 2: Expose and Question Assumptions
- What fundamental assumptions underlie this?
- Are these assumptions valid in all contexts?
- What if these assumptions are wrong?
- What alternative assumptions could lead to different conclusions?

### Stage 3: Analyze Alternative Viewpoints
- [Perspective A]: How would they evaluate this?
- [Perspective B]: What concerns would they raise?
- [Perspective C]: What opportunities would they see?
- Where do perspectives conflict?

### Stage 4: Generate Creative Alternatives
- If this approach doesn't work, what alternatives exist?
- What unconventional solutions might be overlooked?
- How could we reframe the problem?

### Stage 5: Predict Consequences
- Short-term: What happens immediately?
- Long-term: What strategic position results?
- Unintended: What unexpected effects might emerge?
```

**Example Use Case:**
Evaluate whether to adopt microservices architecture

```markdown
Topic: Should we migrate from monolith to microservices?

Stage 1 - Scrutinize Evidence:
- Evidence for: Industry case studies show scalability improvements
- Quality check: Most case studies are from companies 10x our size
- Contradiction: Our team size (5 developers) vs case study teams (50+)
- Relevance: Our traffic patterns differ significantly

Stage 2 - Question Assumptions:
- Assumption: "Microservices always improve scalability"
- Challenge: Only true if scaling is the actual bottleneck
- Alternative: Maybe our bottleneck is database design, not architecture
- Risk: Distributed systems complexity might outweigh benefits

Stage 3 - Alternative Viewpoints:
- Developer: "More repos to manage, complex local dev environment"
- Operations: "Need to learn Kubernetes, monitoring becomes harder"
- Product: "Will this delay feature delivery during migration?"

Stage 4 - Creative Alternatives:
- Could we modularize the monolith without full microservices?
- What about a hybrid approach with 2-3 services instead of 20?
- Can we solve the actual problem (scaling) through database optimization?

Stage 5 - Predict Consequences:
- Short-term: 6-month migration, feature freeze
- Long-term: Either powerful flexibility or operational nightmare
- Unintended: Team knowledge silos, increased oncall burden

Critical Re-evaluation: Original problem was "slow API responses." Root cause analysis shows N+1 queries, not architecture. Solution: Fix queries, not architecture.
```

**Compatibility:**
- ✅ Excellent with: Chain-of-Thought (reason through each stage), Multi-Agent (different perspectives)
- ✅ Good with: Self-Scoring (evaluate critical thinking quality)
- ⚠️ Caution: Can be verbose; best for complex decisions

**Pitfalls:**
- Skipping stages (incomplete analysis)
- Not providing structure (becomes rambling)
- Using for simple yes/no questions (overkill)
- Failing to act on insights gained

---

#### 7. Multi-Agent Simulation

**Definition:** Simulates multiple distinct personas with role-specific analyses

**Scores:** Effectiveness 10/10 | Reliability 9/10

**When to Use:**
- Multiple stakeholder perspectives needed
- Challenging decisions from different angles
- Red team / blue team analysis
- Complex evaluations benefiting from diverse views

**How to Implement:**
```markdown
## MULTI-PERSPECTIVE ANALYSIS

### Persona 1: [Name] - [Role Title]
**Background:** [Relevant expertise and experience]
**Primary Concern:** [What matters most to this persona]
**Analytical Lens:** [How they evaluate problems]
**Assessment of [Topic]:**
[Their detailed perspective - 2-3 paragraphs]
**Recommendation:** [Their specific advice]

### Persona 2: [Name] - [Role Title]
[Same structure]

### Persona 3: [Name] - [Role Title]
[Same structure]

### Synthesis Across Perspectives:
- **Consensus Points:** Where do all personas agree?
- **Conflicting Priorities:** Where do perspectives clash and why?
- **Balanced View:** How to reconcile differences?
- **Blind Spots:** What might all perspectives miss?
```

**Example Use Case:**
Evaluate new feature proposal from multiple roles

```markdown
Feature Proposal: Add real-time collaboration to our document editor

### Persona 1: Sarah Chen - Senior Backend Engineer
**Background:** 8 years building distributed systems, focused on scalability
**Primary Concern:** System reliability and operational complexity
**Assessment:**
Real-time collaboration requires WebSocket infrastructure we don't have. We'll need to build:
- Connection management for 100K+ concurrent users
- Conflict resolution for simultaneous edits
- Reliable message delivery with reconnection handling
This is 6+ months of work with significant operational complexity. Our current infrastructure (REST API + polling) wasn't designed for this. We'd need Redis for pub/sub, load balancer upgrades, and new monitoring.
**Recommendation:** High technical risk. Consider third-party solutions (Yjs, Automerge) to reduce implementation complexity.

### Persona 2: Marcus Rodriguez - Product Manager
**Background:** 5 years PM experience, user research focused
**Primary Concern:** User value and competitive positioning
**Assessment:**
User research shows 78% of our power users want collaboration. Competitors (Google Docs, Notion) have this as table stakes. We're losing enterprise deals specifically because we lack this feature. However, our async commenting workflow is actually cited as a strength by 45% of users who prefer "quiet collaboration."
Real-time might disrupt our core value prop: focused, distraction-free writing.
**Recommendation:** Medium priority. Validate with beta program before full rollout. Consider making it opt-in to preserve focused writing mode.

### Persona 3: Elena Vasquez - Engineering Manager
**Background:** 10 years leading teams, focused on team health and velocity
**Primary Concern:** Team capacity and sustainable delivery
**Assessment:**
Our team of 5 backend engineers already committed to Q4 roadmap (auth overhaul, API v2 migration). Adding real-time collaboration means either:
1. Pushing Q4 work to Q1 2026 (breaks promises to enterprise customers)
2. Hiring 2-3 engineers (3-month ramp time minimum)
3. Burning out current team (already at 85% capacity)
Additionally, this requires new expertise (WebSockets, CRDT algorithms) we don't have. Training time: 4-6 weeks per engineer.
**Recommendation:** Not feasible in 2025 without major trade-offs. Propose Q2 2026 after current commitments complete.

### Synthesis:
**Consensus:** Feature has clear user value (Product) and technical feasibility concerns (Engineering)
**Conflicts:** Timeline expectations (Product wants Q4 2025, Engineering says Q2 2026 at earliest)
**Balanced View:** 
- Short-term: Partner with third-party solution (Yjs) to reduce technical complexity
- Medium-term: Beta launch Q1 2026 with opt-in flag
- Long-term: Full rollout Q2 2026 after validation
**Blind Spots:** None of the perspectives considered security implications of real-time sync (add Security review)
```

**Compatibility:**
- ✅ Excellent with: Socratic (each persona questions assumptions), Chain-of-Thought (explicit reasoning per persona)
- ✅ Good with: Self-Scoring (evaluate each perspective's logic)
- ⚠️ Caution: Requires large context for detailed personas

**Pitfalls:**
- Shallow personas (name only without real perspective differences)
- Too many personas (3-5 is optimal; >6 dilutes)
- No synthesis stage (perspectives presented but not reconciled)
- Personas that all agree (defeats the purpose)

---

#### 8. Objective Self-Scoring

**Definition:** Evaluates own outputs against explicit rubrics

**Scores:** Effectiveness 10/10 | Reliability 9/10

**When to Use:**
- Quality assurance requirements
- Iterative improvement loops
- Meeting specific standards
- Ensuring output meets criteria before delivery

**How to Implement:**
```markdown
## SELF-SCORING RUBRIC

After completing your response, evaluate it against these criteria (0-10 scale):

### Criterion 1: [Name]
**10:** [Description of perfect score]
**7-9:** [Description of good score]
**4-6:** [Description of adequate score]
**0-3:** [Description of poor score]

**Your Score:** [0-10]
**Evidence:** [Specific examples from your output justifying this score]

### Criterion 2: [Name]
[Same structure]

### Overall Assessment:
- Average Score: [Calculate across all criteria]
- Weakest Area: [Criterion with lowest score]
- Improvement Needed: [Specific actions to raise score]
```

**Example Use Case:**
Research output quality validation

```markdown
## SELF-SCORING ASSESSMENT

Evaluate your research output:

### Criterion 1: Completeness
**10:** All questions answered with 200+ words, 2+ examples each, all sub-components addressed
**7-9:** Minor gaps in coverage or slightly less detail
**4-6:** Several questions under-explored
**0-3:** Major gaps or questions skipped

**Your Score:** 8/10
**Evidence:** Answered all 8 questions with 200+ words each. Q3 and Q5 have 2 examples, but Q1, Q2, Q4, Q6-8 have 3+ examples. Sub-components addressed in all questions. Minor: Q3 could use one more example to match others.

### Criterion 2: Evidence Quality
**10:** All claims backed by official docs, research papers, or production patterns with links
**7-9:** Most claims well-sourced, few rely on community sources
**4-6:** Mix of quality and weak sources
**0-3:** Many unsupported claims

**Your Score:** 9/10
**Evidence:** 42 citations total. 38 from official documentation (AWS docs, React docs, academic papers). 4 from Stack Overflow (all for bug workarounds where official docs lack info). All sources linked and dated. Strong evidence quality.

### Criterion 3: Depth of Analysis
**10:** Covers mechanisms, edge cases, trade-offs, alternatives
**7-9:** Good depth, minor aspects unexplored
**4-6:** Surface-level in several areas
**0-3:** Superficial throughout

**Your Score:** 7/10
**Evidence:** Mechanisms explained for 6/8 questions. Q2 and Q7 lack edge case discussion. Trade-offs covered in 7/8 questions (Q4 missing). Alternatives provided for all architectural decisions. Good but not excellent depth.

**Overall Assessment:**
- Average Score: 8.0/10
- Weakest Area: Depth of Analysis (7/10)
- Improvement Needed: Add edge case discussion for Q2 and Q7, add trade-off analysis for Q4
```

**Compatibility:**
- ✅ Excellent with: Iterative Self-Improvement (score → improve → re-score), Quality Gates (pass/fail thresholds)
- ✅ Good with: Chain-of-Thought (explicit reasoning about scores)
- ⚠️ Note: Requires objective, measurable criteria to be effective

**Pitfalls:**
- Vague rubrics ("good" vs "bad" without specifics)
- No examples of score levels
- Scoring without evidence
- Not acting on low scores (score for appearance only)

---

#### 9. Quality Gates

**Definition:** Conditional logic enforcing standards with explicit pass/fail conditions

**Scores:** Effectiveness 10/10 | Reliability 9/10

**When to Use:**
- Standards enforcement requirements
- Quality thresholds must be met
- Conditional workflows (proceed only if X)
- Validation before delivery

**How to Implement:**
```markdown
## QUALITY GATE: [GATE NAME]

**Gate Criterion:** [Specific, measurable condition that must be met]

**Pass Condition:** IF [criterion is met] THEN [Action A - proceed/accept]
**Fail Condition:** IF [criterion is NOT met] THEN [Action B - refine/reject]

**Few-Shot Examples:**

Example 1 - PASS:
- Input: [Example that meets criterion]
- Evaluation: [Why it passes - be specific]
- Action: [What happens next - e.g., "Proceed to next section"]

Example 2 - FAIL:
- Input: [Example that fails criterion]
- Evaluation: [Why it fails - be specific]
- Action: [Required refinement - e.g., "Add 3 concrete examples"]

Example 3 - EDGE CASE:
- Input: [Borderline example]
- Analysis: [How to evaluate borderline cases]
- Decision: [Pass or fail with justification]

---

## YOUR OUTPUT EVALUATION

[After generating output, apply the gate]

Gate Check:
- Criterion Met? [YES/NO]
- Evidence: [Specific evidence from output]
- Decision: [PASS/FAIL]
- Action: [If PASS: proceed. If FAIL: refinement needed]
```

**Example Use Case:**
Ensure all code examples are runnable

```markdown
## QUALITY GATE: Runnable Code Examples

**Gate Criterion:** Every code example must be complete, syntactically valid, and runnable without modifications

**Pass Condition:** IF all code examples include imports, have no syntax errors, and execute successfully THEN approve output
**Fail Condition:** IF any code example is incomplete, has syntax errors, or won't run THEN revise examples

**Few-Shot Examples:**

Example 1 - PASS:
```python
import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# Calculate average salary
avg_salary = df['salary'].mean()
print(f"Average salary: ${avg_salary:,.2f}")
```
- Evaluation: Complete with imports, syntactically valid, executes successfully, produces output
- Action: PASS - Example meets standard

Example 2 - FAIL:
```python
# Filter DataFrame
filtered = df[df['age'] > 25]
print(filtered)
```
- Evaluation: Missing imports, undefined variable 'df', won't run without prior code
- Action: FAIL - Must add imports and df initialization

Example 3 - EDGE CASE:
```python
# ... previous DataFrame code ...
top_earner = df.loc[df['salary'].idxmax()]
```
- Analysis: Depends on previous example but uses "..." to indicate it. Is this acceptable?
- Decision: FAIL - Reader can't copy-paste and run. Must include full context or make standalone.

---

YOUR OUTPUT EVALUATION:

Code Examples in Output: 6 total

Gate Check Results:
- Example 1 (Lines 45-52): ✅ PASS - Complete with imports
- Example 2 (Lines 78-81): ❌ FAIL - Missing imports, undefined variables
- Example 3 (Lines 120-125): ✅ PASS - Complete and runnable
- Example 4 (Lines 156-159): ❌ FAIL - Syntax error (unclosed bracket)
- Example 5 (Lines 201-210): ✅ PASS - Complete with imports
- Example 6 (Lines 245-248): ❌ FAIL - References undefined function

**Gate Decision: FAIL (3 of 6 examples fail)**

**Required Action:** Revise Examples 2, 4, and 6 to meet standard before final output
```

**Compatibility:**
- ✅ Excellent with: Self-Scoring (gates enforce score thresholds), Iterative Self-Improvement (gate → refine → re-check)
- ✅ Good with: Chain-of-Thought (explain gate decisions)
- ⚠️ Requires: Clear, measurable criteria and concrete examples

**Pitfalls:**
- Vague gate criteria ("must be good quality")
- No examples of pass/fail cases
- Gates without enforcement (stating but not checking)
- Too many gates (cognitive overload)

---

#### 10. Iterative Self-Improvement

**Definition:** Generate → Critique → Revise cycle executed in single turn

**Scores:** Effectiveness 10/10 | Reliability 8/10

**When to Use:**
- Quality-critical outputs where first draft insufficient
- Learning from self-critique
- Refining complex responses
- Meeting high standards

**How to Implement:**
```markdown
## ITERATIVE IMPROVEMENT PROCESS

### Round 1: Initial Generation
[Generate first draft of response]

### Round 2: Self-Critique
Critically evaluate the draft:
- What works well? (Keep these elements)
- What's weak or missing? (Specific gaps)
- What could be clearer? (Confusing sections)
- What's the single biggest improvement needed?

### Round 3: Revision
Based on critique, create improved version addressing weaknesses.

### Round 4: Final Evaluation (Optional)
If significant improvements made, evaluate again and refine once more if needed.
Stop after 2-3 cycles to avoid diminishing returns.
```

**Example Use Case:**
Generate executive summary that meets high standards

```markdown
Task: Write executive summary of Q4 financial performance

## Round 1: Initial Generation

Q4 Results Summary:
Revenue increased 15% YoY to $2.3M. Costs rose 8% due to expanded sales team. Net profit margin improved from 12% to 14%. Customer acquisition cost decreased 22% through marketing efficiency gains. Churn remained stable at 3.2%. International expansion accounted for 40% of new revenue.

## Round 2: Self-Critique

What works well:
- Key metrics included (revenue, profit, CAC, churn)
- Quantitative data provided
- Concise (fits in paragraph)

What's weak or missing:
- No context (vs plan? vs expectations?)
- Missing year-end total
- No forward-looking implications
- Lacks executive framing (so what?)
- International expansion mentioned but not explained

Single biggest improvement: Add strategic context and implications, not just facts.

## Round 3: Revision

Q4 Financial Performance - Exceeded Targets:

Q4 revenue of $2.3M (+15% YoY) exceeded plan by 8%, bringing FY2024 total to $8.7M (19% above forecast). More importantly, the quality of growth improved: customer acquisition cost dropped 22% to $450 while churn held stable at 3.2%, indicating strong product-market fit. Profit margin expansion to 14% (vs 12% prior year) demonstrates operational leverage despite 8% cost increase from planned sales team expansion.

Strategic highlight: International revenue (40% of Q4 new business) validates our geographic expansion thesis and positions us for sustained growth in 2025. Management recommends accelerating EMEA investment based on these results.

## Round 4: Final Evaluation

Improvements made:
✅ Added strategic context (vs plan, vs expectations)
✅ Included year-end total and beat
✅ Explained international expansion
✅ Added forward-looking recommendation
✅ Executive framing ("so what" answered)

Quality: Significantly improved. Ready for executive distribution.
```

**Compatibility:**
- ✅ Excellent with: Self-Scoring (score → improve → re-score), Quality Gates (refine until passing)
- ✅ Good with: Socratic (critique challenges assumptions), Chain-of-Thought (explicit reasoning through improvements)
- ⚠️ Trade-off: More token usage for higher quality

**Pitfalls:**
- Too many improvement cycles (diminishing returns after 2-3)
- Vague critique ("make it better") - needs specifics
- Not actually revising (critique without action)
- Improving wrong aspects (optimize for the goal)

---

#### 11. Long-Context Reasoning

**Definition:** Comprehensive analysis leveraging 1M token context window

**Scores:** Effectiveness 10/10 | Reliability 8/10

**When to Use:**
- Large document sets requiring synthesis
- Full codebase analysis
- Extensive conversation history
- Multi-source comprehensive research

**Context Capacity:**
- Theoretical: 1,048,576 tokens (1M)
- Practical optimal: < 500K tokens
- Supports: Needle-in-haystack retrieval

**How to Implement:**
```markdown
[Provide large context - multiple documents, extensive conversation, full codebase]

Task: Analyze the complete [content] provided above.

Instructions for long-context analysis:
1. First pass: Identify main themes and structure
2. Deep dive: Analyze each major section thoroughly
3. Cross-reference: Find connections across the content
4. Synthesize: Draw integrated conclusions
5. Validate: Check findings against full context

Do not summarize superficially. Use the full context to provide deep insights.
```

**Example Use Case:**
Analyze entire codebase for architectural patterns

```markdown
[User provides 50K lines of code across 200 files]

Task: Analyze this codebase and identify architectural patterns, anti-patterns, and improvement opportunities.

Your analysis should:
1. Map the overall architecture (layers, modules, dependencies)
2. Identify recurring patterns (how is X typically done?)
3. Find anti-patterns (code smells, violations of principles)
4. Spot inconsistencies (same problem solved differently in different places)
5. Recommend top 5 improvements with specific file/line references

Use the complete codebase context. Reference specific files and line numbers in your analysis.
```

**Compatibility:**
- ✅ Excellent with: Chain-of-Thought (reason through large context), Socratic (question findings)
- ✅ Good with: Multi-Agent (different perspectives on large content)
- ⚠️ Note: Performance degrades slightly at extreme lengths

**Pitfalls:**
- Expecting perfect recall at 1M tokens (slight degradation at extremes)
- Not structuring the large context (hard to navigate)
- Superficial analysis despite large context
- Not cross-referencing across the context

---

### Tier 3: Promising Techniques

#### 12. Tree of Thoughts (ToT)

**Definition:** Explores multiple solution paths before selecting the best approach

**Scores:** Effectiveness 9/10 | Reliability 7/10

**When to Use:**
- Creative problem-solving where multiple approaches exist
- Optimization problems with various solutions
- Exploring solution space comprehensively
- When best approach isn't obvious upfront

**How to Implement:**
```markdown
## TREE OF THOUGHTS EXPLORATION

### Phase 1: Generate Multiple Approaches

Approach 1: [Solution Path A]
- Core idea: [Main concept]
- Steps: [1, 2, 3...]
- Pros: [Advantages]
- Cons: [Disadvantages]

Approach 2: [Solution Path B]
[Same structure]

Approach 3: [Solution Path C]
[Same structure]

### Phase 2: Evaluate Each Path

Evaluation Criteria:
- Feasibility (1-10): How practical to implement?
- Effectiveness (1-10): How well does it solve the problem?
- Risk (1-10): How likely to succeed?

Approach 1 Scores: Feasibility [X], Effectiveness [Y], Risk [Z]
Approach 2 Scores: [...]
Approach 3 Scores: [...]

### Phase 3: Select Best Path

Selected Approach: [Chosen path]
Rationale: [Why this path is optimal given scores and context]

### Phase 4: Elaborate Solution

[Detailed implementation of selected approach]
```

**Example Use Case:**
Design database schema for multi-tenant SaaS

```markdown
Problem: Design database schema for multi-tenant SaaS app (1000+ tenants, strict data isolation)

## TREE OF THOUGHTS EXPLORATION

### Phase 1: Generate Approaches

Approach 1: Separate Database Per Tenant
- Core idea: Each tenant gets dedicated database
- Steps: Create DB on signup, connection pooling per tenant, backup automation per DB
- Pros: Perfect isolation, easy compliance, simple queries
- Cons: High operational overhead, expensive, hard to scale beyond 1000 DBs

Approach 2: Shared Database, Separate Schemas
- Core idea: Single database, tenant_schema for each
- Steps: Schema creation on signup, SET search_path per request, shared connection pool
- Pros: Better resource utilization, easier operations than separate DBs
- Cons: PostgreSQL limit ~10K schemas, migration complexity

Approach 3: Shared Database, Shared Schema with tenant_id
- Core idea: All tables have tenant_id column, Row-Level Security
- Steps: Add tenant_id to all tables, RLS policies, tenant context in session
- Pros: Simplest operations, unlimited scalability, easy backups
- Cons: Risk of data leakage bugs, query complexity, all migrations affect all tenants

### Phase 2: Evaluate Paths

Evaluation Criteria (1-10 scale):
- Feasibility: How practical with our team/skills?
- Effectiveness: How well does it solve isolation requirement?
- Risk: How likely to succeed without issues?
- Scalability: How well does it scale to 10K+ tenants?

Approach 1 Scores:
- Feasibility: 6 (complex operations)
- Effectiveness: 10 (perfect isolation)
- Risk: 7 (operational complexity risk)
- Scalability: 3 (doesn't scale past few thousand DBs)
- Total: 26/40

Approach 2 Scores:
- Feasibility: 7 (moderate complexity)
- Effectiveness: 9 (very good isolation)
- Risk: 8 (proven pattern)
- Scalability: 6 (schema limit concern)
- Total: 30/40

Approach 3 Scores:
- Feasibility: 9 (simple to implement)
- Effectiveness: 7 (good if RLS perfect)
- Risk: 6 (data leakage risk)
- Scalability: 10 (unlimited)
- Total: 32/40

### Phase 3: Select Best Path

Selected Approach: Approach 3 (Shared Schema with RLS)
Rationale: Highest total score (32/40). While effectiveness is slightly lower than Approach 1 (7 vs 10), the massive scalability advantage (10 vs 3) and implementation feasibility (9 vs 6) make it optimal for our growth trajectory. The data leakage risk can be mitigated through:
- Comprehensive test suite for RLS policies
- Code review process requiring two approvals for tenant-related code
- Automated testing of tenant isolation on every deploy

Trade-off accepted: Slightly higher risk for much better scalability and operations.

### Phase 4: Elaborate Solution

[Detailed schema design with RLS policies, migration strategy, testing approach...]
```

**Compatibility:**
- ✅ Good with: Chain-of-Thought (reason through each path), Self-Scoring (evaluate approaches)
- ⚠️ Note: Requires clear evaluation criteria to choose effectively

**Pitfalls:**
- Generating paths without evaluation (exploration without selection)
- Too many paths (3-5 is optimal; >7 is overwhelming)
- Not elaborating the selected path (stopping at selection)
- Unclear evaluation criteria (can't compare fairly)
- Lower reliability: Must structure carefully for consistent results

---

## Gap Techniques

These 5 techniques were identified in source research but not empirically tested. They are known to be effective based on broader LLM research but lack Gemini-specific validation.

#### 13. Self-Consistency (Gap Technique)

**Definition:** Generate multiple reasoning paths, then use majority vote for final answer

**Scores:** Not tested for Gemini 2.5 Pro (proven effective in general LLM research)

**When to Use:**
- High-stakes decisions requiring validation
- Problems with multiple valid reasoning approaches
- Reducing reasoning errors through consensus
- Uncertain about single-path reasoning

**How to Implement:**
```markdown
## SELF-CONSISTENCY CHECK

Generate 3 independent reasoning paths to the same question:

### Path 1: [Approach A - e.g., First principles]
[Complete reasoning using this approach]
Conclusion: [Answer from Path 1]

### Path 2: [Approach B - e.g., Analogical reasoning]
[Complete reasoning using different approach]
Conclusion: [Answer from Path 2]

### Path 3: [Approach C - e.g., Empirical evidence]
[Complete reasoning using third approach]
Conclusion: [Answer from Path 3]

### Majority Vote:
- Path 1 says: [X]
- Path 2 says: [Y]
- Path 3 says: [Z]
- Consensus: [If 2+ agree, that's the answer. If all different, explain discrepancy]
```

**Example Use Case:**
Validate architectural decision through multiple reasoning methods

**Compatibility:**
- ✅ Good with: Tree of Thoughts (generates multiple paths), Chain-of-Thought (each path uses CoT)
- ⚠️ Trade-off: 3x token usage for validation

**Pitfalls:**
- Not truly independent paths (reusing same reasoning)
- Stopping at disagreement without reconciliation
- Using for simple problems (overkill)

**Status:** Gap - Needs Gemini-specific testing for effectiveness/reliability scores

---

#### 14. ReAct (Reason + Act) (Gap Technique)

**Definition:** Interleaves reasoning and action for autonomous agent behavior

**Scores:** Not tested for Gemini 2.5 Pro

**When to Use:**
- Autonomous agent scenarios
- Problems requiring environmental interaction
- Multi-step tasks with feedback loops
- When actions inform next reasoning steps

**How to Implement:**
```markdown
## REACT FRAMEWORK

Thought 1: [Reasoning about what to do first]
Action 1: [Action to take - e.g., search, analyze, compute]
Observation 1: [Result of action]

Thought 2: [Reasoning based on observation]
Action 2: [Next action based on reasoning]
Observation 2: [Result of second action]

[Continue cycle until task complete]

Final Answer: [Conclusion based on full thought-action-observation chain]
```

**Note:** Gemini's single-shot nature limits true ReAct. Can simulate within prompt but no persistent state between API calls.

**Example Use Case:**
Research with iterative refinement based on findings

**Compatibility:**
- ✅ Natural pairing: Chain-of-Thought (reasoning steps), Grounding (actions = searches)
- ⚠️ Limited by: Single-shot execution boundary

**Pitfalls:**
- Expecting true multi-turn agent behavior (Gemini is single-shot)
- Not providing action results (breaks the cycle)
- Confusing simulation with real environmental interaction

**Status:** Gap - Needs testing; may be limited by Gemini's single-shot architecture

---

#### 15. Few-Shot Prompting (Gap Technique)

**Definition:** Provide examples of desired input-output pairs to guide behavior

**Scores:** Not tested standalone (used within other techniques)

**When to Use:**
- Clarifying desired output format
- Demonstrating quality standards
- Showing edge case handling
- Teaching specific patterns

**How to Implement:**
```markdown
Task: [Description of task]

Here are examples of excellent outputs:

Example 1:
Input: [Example input]
Output: [High-quality output showing desired format/style/depth]

Example 2:
Input: [Different example input]
Output: [High-quality output demonstrating consistency]

Example 3 (Edge Case):
Input: [Challenging/unusual input]
Output: [How to handle edge cases]

Now apply the same approach to:
Input: [Actual user input]
Output: [Your response following the examples]
```

**Example Use Case:**
Generate consistent API documentation format

```markdown
Task: Generate API documentation for endpoints

Examples:

Example 1:
Endpoint: POST /api/users
Request:
```json
{
  "name": "string",
  "email": "string"
}
```
Response: 201 Created
```json
{
  "id": "uuid",
  "name": "string",
  "email": "string",
  "created_at": "ISO 8601 datetime"
}
```
Errors:
- 400: Invalid email format
- 409: Email already exists

[Now document the actual endpoints following this format]
```

**Compatibility:**
- ✅ Excellent with: Quality Gates (examples show pass/fail), Self-Scoring (examples define score levels)
- ✅ Universal: Most techniques benefit from examples

**Pitfalls:**
- Low-quality examples (defeats purpose)
- Too few examples (1-2 insufficient for pattern)
- No edge case examples (model doesn't know how to handle)
- Examples that contradict instructions

**Status:** Gap - Not tested standalone but implicit in many techniques

---

#### 16. Generated Knowledge Prompting (Gap Technique)

**Definition:** Two-step process: first generate relevant facts, then use those facts

**Scores:** Not tested for Gemini 2.5 Pro

**When to Use:**
- Complex questions requiring background knowledge
- When answer depends on recalled facts
- Improving factual accuracy
- Organizing knowledge before reasoning

**How to Implement:**
```markdown
## STEP 1: Generate Relevant Knowledge

Before answering the question, first generate relevant background knowledge:

Question: [User's question]

Relevant Knowledge to Recall:
1. [Fact 1 related to question]
2. [Fact 2 related to question]
3. [Fact 3 related to question]
...

## STEP 2: Answer Using Generated Knowledge

Now using the knowledge above, answer the question:

[Answer that references and builds on the generated knowledge]
```

**Example Use Case:**
Answer complex question requiring multiple facts

**Compatibility:**
- ✅ Good with: Chain-of-Thought (organize knowledge, then reason), Grounding (generate knowledge via search)
- ⚠️ Note: Grounding may be more reliable for factual knowledge than generation

**Pitfalls:**
- Generating wrong knowledge (leads to wrong answer)
- Not using generated knowledge in answer
- Skipping verification of generated facts

**Status:** Gap - Needs testing vs direct answering and vs grounding

---

#### 17. Directional Stimulus Prompting (Gap Technique)

**Definition:** Prime output with desired direction or keyword hints

**Scores:** Not tested for Gemini 2.5 Pro

**When to Use:**
- Guiding output toward specific conclusion
- Constraining creative generation
- Priming for specific perspective
- Steering analysis direction

**How to Implement:**
```markdown
Question: [User question]

Hints/Keywords to guide your response:
- [Keyword 1 - concept to emphasize]
- [Keyword 2 - perspective to take]
- [Keyword 3 - conclusion direction]

Using these directional hints, provide your response:
[Response incorporating the priming keywords]
```

**Example Use Case:**
Guide analysis toward specific considerations

**Compatibility:**
- ✅ Good with: Chain-of-Thought (priming doesn't replace reasoning), Multi-Agent (prime each persona)
- ⚠️ Caution: Can bias output; use carefully

**Pitfalls:**
- Over-constraining (forces predetermined conclusion)
- Conflicting with objective analysis requirements
- Using instead of proper instructions

**Status:** Gap - Needs testing; effectiveness unclear for Gemini

---

## Compatibility Matrix

Which techniques work well together? This matrix shows compatibility:

| Technique | Excellent With | Good With | Caution |
|-----------|---------------|-----------|---------|
| **JSON Schema** | Grounding, Meta-Reasoning, CoT | Self-Scoring | Creative/narrative outputs |
| **Grounding** | JSON Schema, CoT, Self-Scoring | Most techniques | Adds latency |
| **Meta-Reasoning** | CoT, Socratic, Self-Scoring | Most techniques | Adds token usage |
| **Thinking Mode** | ALL techniques | ALL techniques | Cost/speed trade-off |
| **Chain-of-Thought** | ALL techniques (foundational) | ALL techniques | Unnecessary for trivial tasks |
| **Socratic** | CoT, Multi-Agent, Self-Scoring | Meta-Reasoning | Verbose for simple questions |
| **Multi-Agent** | Socratic, CoT, Self-Scoring | Tree of Thoughts | Large context needed |
| **Self-Scoring** | Iterative Improve, Quality Gates, CoT | Most techniques | Needs objective criteria |
| **Quality Gates** | Self-Scoring, Iterative Improve, Few-Shot | CoT, Self-Consistency | Needs concrete examples |
| **Iterative Improve** | Self-Scoring, Quality Gates, Socratic | CoT | More token usage |
| **Long-Context** | CoT, Socratic, Multi-Agent | Most techniques | Performance at extremes |
| **Tree of Thoughts** | CoT, Self-Scoring | Self-Consistency | Lower reliability |
| **Self-Consistency** | Tree of Thoughts, CoT | Quality Gates | 3x token usage |
| **ReAct** | CoT, Grounding | Meta-Reasoning | Limited by single-shot |
| **Few-Shot** | Quality Gates, Self-Scoring | ALL techniques | Universal benefit |
| **Generated Knowledge** | CoT, Grounding | Self-Scoring | Verify generated facts |
| **Directional Stimulus** | CoT, Multi-Agent | Most techniques | Can bias output |

**General Rules:**
- ✅ **Always safe:** CoT + any technique
- ✅ **Powerful combos:** Self-Scoring + Iterative Improve + Quality Gates
- ✅ **Multi-perspective:** Socratic + Multi-Agent + CoT
- ⚠️ **Trade-offs:** Thinking Mode (quality vs speed), Grounding (accuracy vs latency)
- ❌ **Avoid:** >6 techniques in one prompt (cognitive overload)

---

## Selection Guide

### By Use Case

**Comprehensive Research:**
- Required: Chain-of-Thought, Long-Context
- Recommended: Socratic, Self-Scoring, Quality Gates, Iterative Improve
- Optional: Multi-Agent (multiple perspectives), Grounding (current info)

**Strategic Decisions:**
- Required: Chain-of-Thought, Multi-Agent
- Recommended: Socratic, Tree of Thoughts, Self-Scoring, Quality Gates
- Optional: Iterative Improve (refine recommendation)

**Data Extraction:**
- Required: JSON Schema, Chain-of-Thought
- Recommended: Quality Gates, Few-Shot (examples)
- Optional: Grounding (verify facts), Self-Scoring

**Current Information:**
- Required: Grounding, Chain-of-Thought
- Recommended: JSON Schema (structured citations), Quality Gates
- Optional: Self-Scoring (source quality evaluation)

**Creative Problem-Solving:**
- Required: Chain-of-Thought, Tree of Thoughts
- Recommended: Socratic, Multi-Agent, Iterative Improve
- Optional: Self-Consistency (validate creative solutions)

**Code Generation:**
- Required: Chain-of-Thought, Few-Shot (examples)
- Recommended: Quality Gates (runnable code check), Iterative Improve
- Optional: Self-Scoring (code quality evaluation)

**Analysis/Evaluation:**
- Required: Chain-of-Thought, Long-Context (large documents)
- Recommended: Socratic, Multi-Agent, Self-Scoring
- Optional: Meta-Reasoning (show analysis process)

### By Priority Level

**Critical (Always Use):**
1. Chain-of-Thought - Universal reasoning foundation
2. Thinking Mode - Quality control (when API available)

**High Priority (Use Often):**
3. Self-Scoring - Quality assurance
4. Quality Gates - Standards enforcement
5. Socratic Questioning - Critical analysis
6. Few-Shot - Clarify expectations with examples

**Medium Priority (Context-Dependent):**
7. Multi-Agent - When perspectives matter
8. Iterative Improve - When quality critical
9. JSON Schema - When structure required
10. Grounding - When current info needed

**Lower Priority (Specific Use Cases):**
11. Tree of Thoughts - Creative exploration
12. Long-Context - Large document analysis
13. Meta-Reasoning - Transparency needs
14. Self-Consistency - Validation for high stakes
15. ReAct - Agent scenarios (limited by single-shot)
16. Generated Knowledge - Background needed first
17. Directional Stimulus - Specific steering needed

---

## Version & Updates

**Document Version:** 1.0  
**Last Updated:** 2025-11-14 00:10 AEDT  
**Coverage:** 12 tested + 5 gap = 17 techniques total

**Evidence Base:**
- Tested techniques: 1,582 lines of academic research papers
- Gap techniques: Identified in systematic gap analysis
- See: `docs/analysis/source_papers_complete_analysis.md`
- See: `docs/reference/gemini_capabilities.md`

**Status:** Production-ready reference for technique selection

---

## Related Documentation

- **Capabilities:** `docs/reference/gemini_capabilities.md` - What Gemini can do
- **Principles:** `docs/methodology/principles/core_discoveries.md` - Why techniques work
- **Templates:** `docs/methodology/templates/web_ui_templates.md` - How to apply techniques
- **Analysis:** `docs/analysis/source_papers_complete_analysis.md` - Research foundation
