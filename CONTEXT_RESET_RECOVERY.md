# Context Reset Recovery Guide

**Purpose:** This document helps any LLM (or human) quickly recover full context when starting a new conversation about this project.

**Last Updated:** 2025-11-13 23:35 AEDT

---

## Quick Start: Essential Reading Order

**For immediate understanding, read in this order:**

1. **This file first** (you're reading it) - 5 minutes
2. **PROJECT.md** - Strategic context and decisions - 10 minutes
3. **docs/analysis/source_papers_complete_analysis.md** - The foundation - 15 minutes
4. **SESSION.md** - Current state and next steps - 5 minutes

**Total time to full context: ~35 minutes**

---

## Project Purpose (30 seconds)

**Enable any LLM to generate effective Gemini research prompts**

- Primary use: Web UI copy/paste (PATH 1)
- Secondary use: API automation (PATH 2)
- Cross-LLM collaboration framework
- Evidence-based methodology from academic research

---

## The Foundation Story

### Three Sources, One Goal

**Source Papers** (The Authority):
- Paper 1: "Empirical Evaluation" (250 lines) - Third-party analysis
- Paper 2: "Self-Assessment" (1,332 lines) - Gemini analyzing itself
- **Total:** 1,582 lines of academic research
- **Location:** `/Users/dudley/Projects/Gemini Research Method/`

**Claude's Branch** (Web UI Focus):
- 01_PRINCIPLES.md (370 lines) - Meta-learnings
- 02_TEMPLATES.md (613 lines) - Production templates
- 03_APPLICATIONS/ (~1,020 lines) - API implementations
- **Innovation:** PATH 1/2 distinction, practical templates, anti-patterns

**ChatGPT's Branch** (Automation Focus):
- v1.3.0 Pack (11 files) - Custom GPT generator
- **Innovation:** Schema-driven, compliance validation, preset system

**Critical Insight:** Claude and ChatGPT branches are **sibling implementations** - both extracted from same source papers, neither complete.

---

## What We Know (The Evidence)

### 12 Techniques Tested in Source Papers

Each scored on Effectiveness (0-10) and Reliability (0-10):

| Technique | E/R | Key Insight |
|-----------|-----|-------------|
| Chain-of-Thought | 10/10 | Native "Thinking" architecture |
| Evidence-Based Structured Output | 10/9 | Grounding + JSON schema |
| Multi-Agent Simulation | 10/9 | Large context enables personas |
| Socratic Questioning | 10/8 | Emergent, prompt-dependent |
| Meta-Reasoning | 10/9 | includeThoughts API feature |
| Objective Self-Scoring | 10/9 | Critical self-assessment |
| Quality Gates | 10/9 | Conditional logic via few-shot |
| Tree of Thoughts | 9/7 | Can simulate, not native |
| JSON Schema Validation | 10/9 | API-enforced responseSchema |
| Long-Context Reasoning | 10/8 | 1M tokens, needle-in-haystack |
| Iterative Self-Improvement | 10/8 | Generate→Critique→Revise |
| Thinking Mode | 10/10 | thinkingBudget parameter |

### 5 Gap Techniques (Missing from Both Branches)

- Self-Consistency (multiple paths + majority vote)
- ReAct (Reason + Act for agents)
- Few-Shot Prompting (fundamental)
- Generated Knowledge Prompting
- Directional Stimulus Prompting

---

## Repository Status

**Git:** https://github.com/Dudley70/Gemini-Research  
**Branch:** main  
**Commits:** 3 (foundation complete)

**Structure:**
```
Gemini-Research/
├── PROJECT.md           ✅ Strategic context
├── SESSION.md           ✅ Current state
├── README.md            ✅ Overview
└── docs/
    ├── INDEX.md         ✅ Documentation map
    ├── analysis/        ✅ Complete (3 docs)
    ├── methodology/     📁 Awaiting content
    ├── api/             📁 Awaiting content
    ├── reference/       📁 Awaiting content
    ├── guides/          📁 Awaiting content
    └── enhancements/    📁 Awaiting content
```

---

## What's Next (Immediate Priorities)

**Phase 1: Port Methodology**
1. 01_PRINCIPLES.md → docs/methodology/principles/core_discoveries.md
2. 02_TEMPLATES.md → docs/methodology/templates/web_ui_templates.md
3. Create docs/reference/gemini_capabilities.md (from source papers)
4. Create docs/reference/technique_library.md (all 17 techniques)

**Phase 2: Integration**
5. Unified methodology (combine both branches)
6. LLM-specific guides (for Claude, for ChatGPT)

**Phase 3: Fill Gaps**
7. Document the 5 missing techniques

---

## Key Decisions Made

**Decision #003 (Most Recent):** Treat Claude and ChatGPT branches as sibling implementations, neither subordinate

**Decision #002:** PATH 1 (Web UI copy/paste) primary, PATH 2 (API automation) secondary

**Decision #001:** Use ClaudeWorkflow project structure for cross-LLM collaboration

---

## Critical Files to Know

**Strategic:**
- `PROJECT.md` - Why this exists, what we're building, decisions made
- `SESSION.md` - Where we are, what's done, what's next

**Analysis:**
- `docs/analysis/source_papers_complete_analysis.md` - THE FOUNDATION (must read)
- `docs/analysis/chatgpt_approach_analysis.md` - ChatGPT branch evaluation

**Source Material:**
- `/Users/dudley/Projects/Gemini Research Method/` - Original research location
  - Read source papers if needed, but analysis doc covers it
  - 01_PRINCIPLES.md, 02_TEMPLATES.md, 03_APPLICATIONS/ ready to port

---

## How to Continue This Project

**For Claude:**
1. Read this file + PROJECT.md + source_papers_complete_analysis.md + SESSION.md
2. Check SESSION.md "NEXT STEPS" for current phase
3. Use desktop-commander MCP tools for all file operations
4. Follow commit conventions from SESSION.md
5. Update SESSION.md after significant progress

**For ChatGPT:**
1. Same reading order as above
2. Understand you're working with a sibling implementation
3. Your v1.3.0 Pack is preserved in docs/analysis/
4. Contribute through GitHub pull requests or direct file creation

**For Any LLM:**
1. Read foundational docs first (35 minutes)
2. Understand the three sources (Papers, Claude, ChatGPT)
3. Respect the sibling implementation status
4. Follow PATH 1 (Web UI) primary focus
5. Build on evidence-based foundation

---

## Common Questions

**Q: Why two paths (Web UI and API)?**  
A: Different use cases. Web UI for interactive research (primary), API for automation (secondary).

**Q: Why are Claude and ChatGPT "siblings"?**  
A: Both extracted from same source papers independently. Neither is complete. Both valid.

**Q: Where's the source research?**  
A: `/Users/dudley/Projects/Gemini Research Method/` - Two papers (1,582 lines) analyzed in docs/analysis/source_papers_complete_analysis.md

**Q: What makes this unique?**  
A: Only repository that:
- Documents the complete evidence base (source papers)
- Preserves both implementation branches
- Provides cross-LLM collaboration framework
- Identifies and plans to fill technique gaps

**Q: What's the immediate priority?**  
A: Port methodology content from source to new structure (Phase 1 in SESSION.md)

---

**Context Recovery Time: 35 minutes**  
**Full Understanding: Read PROJECT.md → source_papers_complete_analysis.md → SESSION.md**
