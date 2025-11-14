# Technique Library: Gemini 2.5 Pro (V7)

**Src**: 1,438L/40KB technique catalog | **V7**: 72% reduction to ~11KB | **LLM only**

**Coverage**: 12 tested + 5 gap = 17 techniques | **Tiers**: 1=API-enforced, 2=Emergent, 3=Promising, Gap=Untested

**Nav**: Tested (12) | Gap (5) | Compatibility Matrix | Selection Guide

---

## Usage

**Per Technique:**
1. Def - What it does
2. Scores - E/R (0-10, tested only)
3. When - Ideal scenarios
4. How - Patterns + examples
5. API - Tier 1 only
6. Compat - Combines well w/
7. Pitfalls - Avoid

---

## Tested Techniques

### Tier 1: API-Enforced

#### 1. JSON Schema

**Def**: API-level schema validation → structured JSON

**Scores**: E=10/10, R=9/10

**When**: Data extraction, integration, format consistency, standardization

**API**:
```json
{
  "response_mime_type": "application/json",
  "responseSchema": {
    "type": "object",
    "properties": {
      "field": {"type": "string"}
    },
    "required": ["field"]
  }
}
```

**Web UI** (educational):
```
Output: ONLY valid JSON w/ structure:
{
  "findings": [{"topic": "str", "summary": "str", "confidence": "HIGH|MED|LOW"}],
  "metadata": {"total_sources": int, "date_range": "str"}
}
No text outside JSON.
```

**Compat**: ✅ Grounding, Meta-Reasoning | ✅ CoT | ⚠️ Creative/narrative

**Pitfalls**: Complex nesting (start simple), no examples, mixing JSON + prose

---

#### 2. Grounding (Search)

**Def**: API grounding → live search → current info → citations

**Scores**: E=10/10, R=9/10

**When**: Current info, verifiable facts, citations needed, broad topics

**API**:
```json
{
  "tools": [{"google_search": {}}]
}
```

**Web UI**:
```
Research [topic]. Include:
- Sources from last 6 months
- Citations [1], [2] format
- Multiple perspectives
- Current statistics/data
```

**Compat**: ✅ JSON Schema, Few-Shot | ⚠️ Deep analysis (may prioritize breadth)

**Pitfalls**: Narrow topics (insufficient results), no date guidance, assuming comprehensiveness

---

#### 3. Thinking Mode

**Def**: Extended reasoning budget (API parameter)

**Scores**: E=9/10, R=9/10

**When**: Complex logic, multi-step, optimization, edge cases

**API**:
```json
{
  "thinking": {
    "type": "THINKING_MODE_ENABLED",
    "thinkingBudget": 8192
  }
}
```

**Budget**: 128-32,768 tokens (default 8K reasonable)

**Web UI**: Not available (always-on internal Thinking)

**Compat**: ✅ CoT, Meta-Reasoning, ToT | Universal compatibility

**Pitfalls**: Excessive budget (cost vs benefit), assuming always optimal

---

### Tier 2: Emergent High-Reliability

#### 4. Chain-of-Thought (CoT)

**Def**: Break complex → intermediate steps. "Think step by step."

**Scores**: E=10/10, R=9/10

**When**: Logic, math, multi-step, planning, debugging

**Pattern**:
```
[Problem]
Think step by step:
1. [What's first?]
2. [What follows?]
3. [How to verify?]
Show work for each step.
```

**Example**:
```
Warehouse A=40, B=30, C=20.
Step 1: Move half A→B
Step 2: Move 10 C→A
Step 3: Distribute B evenly to A+C
Step 4: Move 5 A→C

Think step by step. Show calculations. Final state?
```

**Compat**: ✅ Universal | Best w/ Self-Scoring, Quality Gates

**Pitfalls**: Implicit steps, unclear sequence, no verification request

---

#### 5. Socratic Questioning

**Def**: Self-interrogation → surface assumptions → critical analysis

**Scores**: E=9/10, R=8/10

**When**: Assumptions unchecked, biases, complex decisions, critical analysis

**Pattern**:
```
Before answering [question], ask yourself:
- What assumptions underlie this?
- What evidence supports/contradicts?
- What perspectives am I missing?
- What would change my conclusion?

Then answer with reasoning shown.
```

**Example**:
```
Should Company X expand to Market Y?

Self-interrogate:
- What assumptions about market size?
- What data on competition?
- What risks not considered?
- What would make expansion fail?

Provide recommendation w/ reasoning.
```

**Compat**: ✅ CoT, Multi-Agent, Quality Gates | May slow for simple tasks

**Pitfalls**: Overuse (simple queries), vague questions, no answer synthesis

---

#### 6. Multi-Agent Simulation

**Def**: Simulate multiple perspectives → one response

**Scores**: E=9/10, R=8/10

**When**: Trade-offs, stakeholders, balanced view, blind spots

**Pattern**:
```
Analyze [topic] from 3 perspectives:
1. [Perspective A]: Focus on [aspect]
2. [Perspective B]: Focus on [aspect]
3. [Perspective C]: Focus on [aspect]

Synthesize: agreements, disagreements, gaps.
```

**Example**:
```
Database architecture decision:
1. Developer: Code simplicity, debugging
2. DBA: Performance, maintenance, scaling
3. Business: Cost, reliability, time-to-market

Each perspective's view, then synthesis.
```

**Compat**: ✅ Socratic, CoT | ⚠️ Simple queries (overkill)

**Pitfalls**: Too many agents (3-5 max), vague roles, no synthesis

---

#### 7. Few-Shot Examples

**Def**: Show examples → clarify expectations → consistent format

**Scores**: E=9/10, R=9/10

**When**: Format unclear, style needed, consistency, complex structure

**Pattern**:
```
Examples:
Input: [example 1]
Output: [format 1]

Input: [example 2]
Output: [format 2]

Now:
Input: [actual query]
Output:
```

**Example**:
```
Examples:
Q: "Python list comprehension for squares"
A: [x**2 for x in range(10)]

Q: "Filter even numbers from list"
A: [x for x in numbers if x % 2 == 0]

Q: "Extract names from dict list"
A:
```

**Compat**: ✅ JSON Schema, Grounding | Universal utility

**Pitfalls**: Contradictory examples, insufficient variety, too many (3-5 ideal)

---

#### 8. Self-Scoring Quality

**Def**: Explicit rubric → self-evaluation → quality awareness

**Scores**: E=9/10, R=8/10

**When**: Quality critical, standards clear, improvement loops, validation

**Pattern**:
```
[Task instructions]

Evaluate your response (0-10):
- Criterion 1: [specific measure]
- Criterion 2: [specific measure]
- Criterion 3: [specific measure]

Provide score + justification for each.
```

**Example**:
```
Research database sharding strategies.

Self-score (0-10):
- Comprehensiveness: All major strategies?
- Trade-off clarity: Pros/cons explicit?
- Practical guidance: Implementation clear?
- Source quality: Authoritative references?

Report scores + reasoning.
```

**Compat**: ✅ CoT, Quality Gates, Socratic | ✅ Post-generation validation

**Pitfalls**: Vague criteria, too many (>7), no justification requirement

---

#### 9. Meta-Reasoning (Transparency)

**Def**: Explain reasoning process → show decisions → transparency

**Scores**: E=8/10, R=8/10

**When**: Decisions need justification, audit trails, trust, learning

**Pattern**:
```
[Task]

In your response:
1. Show reasoning: Why this approach?
2. Explain choices: Why X not Y?
3. Note limitations: What's uncertain?
4. Document assumptions: What's assumed?
```

**Example**:
```
Recommend caching strategy.

Include:
- Why this strategy vs alternatives?
- What assumptions about traffic?
- What trade-offs made?
- What uncertainties remain?
```

**Compat**: ✅ CoT, Socratic, Thinking Mode | Verbose (use selectively)

**Pitfalls**: Excessive (every decision), shallow ("because better"), no structure

---

#### 10. Self-Consistency Sampling

**Def**: Multiple reasoning paths → majority voting → robust answers

**Scores**: E=8/10, R=7/10

**When**: High-stakes, verification, disagreement likely, multiple valid paths

**Pattern**:
```
Solve [problem] using 3 different approaches:
1. Approach A: [method]
2. Approach B: [method]
3. Approach C: [method]

Compare results. If agree → high confidence. If differ → explain why.
```

**Example**:
```
Calculate project timeline:
1. Bottom-up: Task estimates
2. Historical: Past projects
3. Statistical: PERT

Compare. Agreement → use. Disagreement → investigate.
```

**Compat**: ✅ CoT, Socratic | Resource-intensive

**Pitfalls**: Simple problems (overkill), rushed approaches, ignoring disagreements

---

### Tier 3: Promising (Lower Reliability)

#### 11. Tree of Thoughts (ToT)

**Def**: Explore multiple reasoning branches → backtrack → find optimal

**Scores**: E=8/10, R=6/10

**When**: Creative, open-ended, complex optimization, multiple solutions

**Pattern**:
```
Problem: [statement]

Explore 3 branches:
Branch 1: [approach] → evaluate
Branch 2: [approach] → evaluate
Branch 3: [approach] → evaluate

Prune weak. Expand promising. Synthesize best.
```

**Example**:
```
Product naming:
Branch 1: Descriptive (ClearDB) → evaluate memorability
Branch 2: Abstract (Zenith) → evaluate meaning
Branch 3: Hybrid (DataZen) → evaluate both

Prune, expand, recommend.
```

**Compat**: ✅ CoT, Thinking Mode | ⚠️ Single-shot limits backtracking depth

**Pitfalls**: Too many branches (3-5 max), no pruning criteria, shallow exploration

---

#### 12. Long-Context Utilization

**Def**: Leverage 1M context → multi-doc analysis → comprehensive synthesis

**Scores**: E=9/10, R=7/10

**When**: Multiple docs, large codebases, comprehensive analysis, cross-referencing

**Pattern**:
```
Documents: [list all]

Task: [analysis across all]

For each document:
- Key points
- Relationships to others
- Contradictions
- Synthesis across all
```

**Example**:
```
Analyze 5 architecture proposals (50 pages each).

Extract:
- Common patterns across all
- Unique approaches per proposal
- Trade-offs identified
- Gaps in any proposal

Synthesize comprehensive view.
```

**Compat**: ✅ Grounding, JSON Schema | Reliability varies w/ length

**Pitfalls**: Assuming equal depth across all content, no clear focus, overwhelming synthesis

---

## Gap Techniques (Identified, Not Tested)

### 13. Quality Gates

**Def**: Checkpoints + explicit standards → don't proceed if fail

**When**: Iterative work, quality critical, clear standards, failure costly

**Pattern**:
```
[Task]

Gate 1: [criterion] → Must pass before Gate 2
Gate 2: [criterion] → Must pass before Gate 3
Gate 3: [criterion] → Final validation

Report: Which gates passed/failed, why, action.
```

**Example**:
```
API design:

Gate 1: RESTful conventions (Y/N)
Gate 2: Error handling complete (Y/N)
Gate 3: Security considered (Y/N)

Pass all → proceed. Fail any → fix first.
```

**Compat**: ✅ Self-Scoring, CoT, Socratic

**Status**: Not empirically tested, principle-derived

---

### 14. Iterative Improvement

**Def**: Generate → critique → refine → repeat

**When**: Quality matters more than speed, subjective judgments, creative work

**Pattern**:
```
Draft 1: [generate]
Critique: [what's weak?]
Draft 2: [improve]
Critique: [still weak?]
Final: [polish]
```

**Example**:
```
Write product description:
Draft 1: Basic version
Critique: Too technical, no emotion
Draft 2: Add benefits, soften tone
Critique: Better, but vague claims
Final: Specific + emotional
```

**Compat**: ✅ Self-Scoring, Quality Gates, Socratic

**Status**: Not empirically tested, single-shot limits iterations

---

### 15. ReAct (Reason+Act)

**Def**: Thought → action → observation → repeat

**When**: Agent tasks, tool use, environment interaction, sequential decisions

**Pattern**:
```
Thought: [what to do?]
Action: [do it]
Observation: [what happened?]
Thought: [next?]
...
```

**Example**:
```
Thought: Need current gas prices
Action: Search "US gas prices 2024"
Observation: $3.45 avg
Thought: Compare to historical
Action: Search "gas prices 2020"
Observation: $2.17 avg
Conclusion: 59% increase
```

**Compat**: ✅ Grounding, CoT | Limited by single-shot (no true environment)

**Status**: Not tested, theoretical application only

---

### 16. Generated Knowledge

**Def**: Generate relevant background → use for main task

**When**: Context needed, domain-specific, background missing, primer helpful

**Pattern**:
```
Step 1: Generate knowledge about [topic]
Step 2: Use that knowledge for [main task]
```

**Example**:
```
Step 1: Explain CAP theorem (consistency, availability, partition tolerance)
Step 2: Using that explanation, evaluate database choice for [use case]
```

**Compat**: ✅ CoT, Few-Shot

**Status**: Not tested, overlap w/ CoT unclear

---

### 17. Directional Stimulus

**Def**: Seed initial direction → steer toward desired outcome

**When**: Open-ended, specific framing needed, avoid common paths, bias correction

**Pattern**:
```
[Task]

Starting perspective: [frame]
Explore from this angle first, then broaden.
```

**Example**:
```
Analyze merger impact.

Starting perspective: Employee retention risk
Explore this first, then financial/strategic.
```

**Compat**: ✅ Multi-Agent, Socratic | Risk: Over-biasing

**Status**: Not tested, use cautiously

---

## Compatibility Matrix

| Technique | Best With | Good With | Caution |
|-----------|-----------|-----------|---------|
| JSON Schema | Grounding, Meta-Reason | CoT | Creative |
| Grounding | JSON, Few-Shot | CoT, Long-Context | Deep analysis |
| Thinking Mode | CoT, Meta, ToT | Universal | - |
| CoT | Self-Score, Quality Gates | Universal | - |
| Socratic | CoT, Multi-Agent, Quality | Meta | Simple queries |
| Multi-Agent | Socratic, CoT | Meta | Simple/3-5 agents |
| Few-Shot | JSON, Grounding | Universal | Contradictions |
| Self-Score | CoT, Quality Gates, Socratic | Most | Vague criteria |
| Meta-Reason | CoT, Socratic, Thinking | Most | Verbose |
| Self-Consist | CoT, Socratic | - | Resource-heavy |
| ToT | CoT, Thinking | Socratic | Single-shot limits |
| Long-Context | Grounding, JSON | CoT | Variable reliability |
| Quality Gates | Self-Score, CoT, Socratic | Iterative | - |
| Iterative | Self-Score, Gates, Socratic | - | Single-shot limits |
| ReAct | Grounding, CoT | - | No true environment |
| Gen Knowledge | CoT, Few-Shot | - | CoT overlap |
| Directional | Multi-Agent, Socratic | - | Over-biasing risk |

---

## Selection Guide

### By Use Case

**Data Extraction:**
1. JSON Schema (structure)
2. Few-Shot (format examples)
3. Self-Score (quality check)

**Current Information:**
1. Grounding (search)
2. Few-Shot (format)
3. JSON Schema (structure)

**Complex Reasoning:**
1. CoT (foundation)
2. Thinking Mode (budget)
3. Socratic (critical analysis)
4. Self-Consistency (verification)

**Creative/Open-Ended:**
1. ToT (exploration)
2. CoT (structure)
3. Socratic (challenge)

**Multi-Document:**
1. Long-Context (leverage 1M)
2. JSON Schema (structure findings)
3. Few-Shot (consistent format)

**Quality-Critical:**
1. Self-Score (rubric)
2. Quality Gates (checkpoints)
3. Socratic (assumptions)
4. Self-Consistency (verification)

**Balanced Analysis:**
1. Multi-Agent (perspectives)
2. Socratic (interrogate)
3. CoT (reasoning)

**Transparent Decisions:**
1. Meta-Reasoning (explain)
2. CoT (show work)
3. Socratic (surface assumptions)

---

### By Technique Count

**Universal (Always Use):**
- CoT - Reasoning foundation
- Thinking Mode - Quality (API only)

**High Priority (Use Often):**
- Self-Score - QA
- Quality Gates - Standards
- Socratic - Critical analysis
- Few-Shot - Clarity

**Medium Priority (Context-Dependent):**
- Multi-Agent - Perspectives
- Iterative - Quality loops
- JSON Schema - Structure
- Grounding - Current info

**Lower Priority (Specific Cases):**
- ToT - Creative exploration
- Long-Context - Multi-doc
- Meta-Reason - Transparency
- Self-Consist - High-stakes validation
- ReAct - Agent (limited)
- Gen Knowledge - Background
- Directional - Steering

---

## Optimal Stacks (4-6 Techniques)

**Standard Research:**
CoT + Grounding + JSON Schema + Self-Score

**Critical Analysis:**
CoT + Socratic + Multi-Agent + Quality Gates + Self-Score

**Structured Extraction:**
JSON Schema + Few-Shot + Grounding + Self-Score

**Creative Exploration:**
ToT + CoT + Socratic + Iterative

**Multi-Document:**
Long-Context + CoT + JSON Schema + Self-Score

**High-Stakes Decision:**
CoT + Socratic + Multi-Agent + Self-Consistency + Meta-Reason

---

## Version

**Doc**: 1.0 | **Updated**: 2025-11-14 00:10 AEDT | **Coverage**: 17 techniques (12 tested, 5 gap)

**Evidence**: 1,582L academic research (tested), systematic gap analysis (gap)

**Related**:
- Capabilities: `docs/reference/gemini_capabilities.md`
- Principles: `docs/methodology/principles/core_discoveries.md`
- Templates: `docs/methodology/templates/web_ui_templates.md`
- Analysis: `docs/analysis/source_papers_complete_analysis.md`
