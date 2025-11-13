# Questions for User - Context Optimization Solution

**Purpose:** Get details needed to design the right solution  
**Status:** Must answer before creating any new framework documents

---

## Question 1: Your Compression Method

**You mentioned having a compression method. Please explain:**

### What does it compress?
- [ ] The framework (3,000 lines → X lines)?
- [ ] Research outputs (1,500 lines → X lines)?
- [ ] Both?
- [ ] Something else?

### How much compression?
**Example needed:**
```
Input: [what] at [N] lines
Process: [how it compresses]
Output: [what] at [M] lines
```

### Mechanism?
- [ ] It's a tool/script (what tool?)
- [ ] It's a prompt pattern (can you share?)
- [ ] It's a manual process (what steps?)
- [ ] Something else?

### What gets preserved?
- [ ] All key findings
- [ ] Technical details
- [ ] Trade-offs and decisions
- [ ] Cross-domain considerations
- [ ] What else?

### What gets discarded?
- [ ] Examples
- [ ] Detailed explanations
- [ ] Redundant information
- [ ] What else?

### Does it handle unknown dependencies?
**Scenario:** Domain 1 research completed and compressed. Later, Domain 5 needs something from Domain 1 that wasn't obviously important.

- [ ] Yes, compression preserves enough for unknown future needs
- [ ] No, need to know dependencies upfront
- [ ] Partially - explain:

---

## Question 2: Sub-Agent Pattern

**You mentioned Claude Code + sub-agents. Please explain the architecture:**

### Pattern A: Sub-Agent Per Domain?
```
Main Claude (Project Context):
├─ Spawns Agent for Domain 1
│   └─ Fresh context, generates prompt, returns, dies
├─ Spawns Agent for Domain 2  
│   └─ Fresh context, generates prompt, returns, dies
├─ Spawns Agent for Domain 3
│   └─ Gets Domain 1+2 findings, generates prompt, dies
```
**Is this the pattern?** [ ] Yes [ ] No [ ] Close but different (explain):

### Pattern B: Single Reusable Prompt Generator?
```
Main Claude (Project Context):
├─ Manages overall research workflow
├─ When needs prompt:
│   └─ Calls PromptGenerator Agent
│       └─ Gets context, returns prompt, dies
├─ Analyzes results in main context
```
**Is this the pattern?** [ ] Yes [ ] No [ ] Close but different (explain):

### Pattern C: Something Else?
**Draw your architecture (ASCII art is fine):**
```
[Your pattern here]
```

### Where does the framework live?
- [ ] In Project Knowledge (shared across all agents)
- [ ] Passed to each agent
- [ ] Each agent reads from files
- [ ] Agent has it pre-loaded somehow
- [ ] Other:

### How do findings pass between agents?
**Example: Domain 3 needs findings from Domain 1 and 2**

- [ ] Main agent holds findings, passes to Domain 3 agent
- [ ] Findings stored in project files, Domain 3 agent reads them
- [ ] Findings in shared Project Knowledge
- [ ] Other:

### Is Claude Code specifically required?
- [ ] Yes, must be Claude Code (why?)
- [ ] No, just need disposable agent concept
- [ ] Don't know yet

---

## Question 3: Integration

**How do compression + sub-agents work together?**

### When does compression happen?
- [ ] In main agent after research returns
- [ ] In sub-agent before it dies
- [ ] Separate compression agent
- [ ] Other:

### What stays in main context?
- [ ] Just compressed findings from all domains
- [ ] Framework (full or condensed?)
- [ ] Project requirements
- [ ] Conversation about analysis
- [ ] Other:

### What's passed to sub-agents?
- [ ] Full framework (3,000 lines)
- [ ] Condensed framework (X lines)
- [ ] Just current domain requirements
- [ ] Compressed findings from prior domains
- [ ] Other:

---

## Question 4: Validation

### Do you have a real project example?
- [ ] Yes - can share details (domain list, dependencies)
- [ ] No - this is theoretical
- [ ] Have one but can't share details

**If yes, what scale?**
- Number of domains: ___
- Typical dependency depth: ___ (e.g., Domain 8 depends on 5 prior domains)
- Research output size: ___ lines typical

### Have you tried this pattern?
- [ ] Yes, it works
- [ ] Yes, partially works (what issues?)
- [ ] No, this is the design
- [ ] Other:

---

## Question 5: Current Pain Points

**When you've tried multi-domain research, what specifically breaks?**

### Context issues:
- [ ] Can't generate quality prompts after N iterations (N = ___)
- [ ] Claude forgets framework details
- [ ] Claude can't access prior research findings
- [ ] Conversation becomes confused/unfocused
- [ ] Other:

### Quality issues:
- [ ] Later prompts are lower quality
- [ ] Dependencies not properly incorporated
- [ ] Research doesn't build on prior findings
- [ ] Other:

### Workflow issues:
- [ ] Too manual/tedious
- [ ] Hard to track dependencies
- [ ] Don't know when research is "done"
- [ ] Other:

---

## What I Need to Design Solution

**Minimum required (can't proceed without):**
1. Compression method details (Q1)
2. Sub-agent architecture (Q2)
3. How they integrate (Q3)

**Helpful but not blocking:**
4. Real project example (Q4)
5. Specific pain points (Q5)

**With this info, I can:**
- Design solution that works with your existing methods
- Create minimal necessary documentation
- Avoid over-engineering
- Ensure solution solves actual problem

---

## Next Steps

**After you provide answers:**

1. I'll design solution architecture
2. Show you the design for validation
3. Create necessary docs (likely 1,000-1,500 lines total)
4. Test with example scenario
5. Refine based on feedback

**Without answers:**
- Risk building wrong thing
- May over-engineer
- Can't integrate with your methods
- Waste time on unnecessary work

---

**Please answer Questions 1-3 minimum before next session.**

**Preferred format:** Just answer inline in this doc, or explain conversationally in next chat.
