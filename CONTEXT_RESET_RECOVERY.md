# Context Reset Recovery Guide

**Last Updated:** 2025-11-14 00:50 AEDT  
**Purpose:** Rapid context recovery for returning to this project  
**Read Time:** 3-5 minutes

---

## FASTEST RECOVERY (60 seconds)

**Project:** Gemini Research Framework  
**Purpose:** Enable LLMs to generate effective Gemini research prompts  
**Status:** Phase 1 + 2 Complete - Production-ready  
**Location:** /Users/dudley/Projects/Gemini-Research  
**GitHub:** https://github.com/Dudley70/Gemini-Research

**Quick Facts:**
- 8,823 lines of documentation
- 17 techniques documented (12 tested + 5 gaps)
- 2 production templates (A: comprehensive, B: strategic)
- Evidence-based (1,582 lines of research)
- Works with any LLM (ChatGPT, Claude, etc.)

**Read These 3 Files:**
1. `FRAMEWORK_GUIDE.md` (536 lines) - Complete overview
2. `SESSION.md` (499 lines) - What was done, what's next
3. `docs/INDEX.md` (110 lines) - Documentation map

---

## WHAT IS THIS PROJECT?

**Framework Goal:**
Enable any LLM (ChatGPT, Claude, etc.) to generate high-quality research prompts optimized for Gemini 2.5 Pro.

**How It Works:**
```
User → LLM → Generated Prompt → User copies → Gemini executes → 1,500-2,000 lines of research
```

**Example:**
```
User to Claude: "Generate a Gemini research prompt for database sharding"
Claude: [reads framework docs] → [generates optimized prompt]
User: [copies prompt] → [pastes into google.com/gemini]
Gemini: [produces comprehensive 1,500-line research output]
```

**Quality:** Framework techniques consistently achieve 9-10/10 outputs

---

## REPOSITORY STRUCTURE

```
Gemini-Research/
├── FRAMEWORK_GUIDE.md          ← START HERE (universal entry point)
├── PROJECT.md                  ← Strategic context
├── SESSION.md                  ← Current state (detailed)
├── README.md                   ← GitHub overview
│
└── docs/
    ├── INDEX.md                ← Documentation map
    │
    ├── methodology/            ← PHASE 1 (how to use)
    │   ├── principles/
    │   │   └── core_discoveries.md (why techniques work)
    │   └── templates/
    │       └── web_ui_templates.md (Template A & B)
    │
    ├── reference/              ← PHASE 1 (what's available)
    │   ├── gemini_capabilities.md (what Gemini can do)
    │   └── technique_library.md (all 17 techniques)
    │
    ├── enhancements/           ← PHASE 2 (integration)
    │   └── unified_methodology.md (Claude + ChatGPT)
    │
    └── guides/                 ← PHASE 2 (LLM-specific)
        ├── for_claude.md (how Claude uses framework)
        └── for_chatgpt.md (how ChatGPT uses framework)
```

---

## KEY CONCEPTS (2-minute read)

### PATH 1 vs PATH 2

**PATH 1: Web UI (PRIMARY)**
- User copies generated prompt → pastes into google.com/gemini
- Output: Human-readable prose (1,500-2,000 lines)
- Templates: A (comprehensive) & B (strategic decision)

**PATH 2: API (SECONDARY)**
- Programmatic execution via Gemini API
- Output: Structured JSON
- Use case: Automation, validation

### Technique Tiers

**Tier 1:** API-enforced (9-10/10 reliability)  
**Tier 2:** Emergent high (8-10/10 reliability)  
**Tier 3:** Promising (7/10 reliability)  
**Gaps:** Not yet tested for Gemini

### Quality Standard

**Target:** ≥8.5/10 average across 7 criteria
1. Completeness
2. Evidence Quality
3. Depth of Analysis
4. Pattern Quality
5. Critical Thinking
6. Integration
7. Actionability

---

## WHAT WAS ACCOMPLISHED

### Phase 1: Methodology Foundation (COMPLETE)
- ✅ Core discoveries (413 lines) - Why techniques work
- ✅ Web UI templates (899 lines) - Template A & B
- ✅ Gemini capabilities (696 lines) - Technical specs
- ✅ Technique library (1,438 lines) - All 17 techniques

### Phase 2: Integration & Guidance (COMPLETE)
- ✅ Unified methodology (684 lines) - Branch integration
- ✅ Framework guide (536 lines) - Entry point
- ✅ For Claude guide (632 lines) - Claude workflow
- ✅ For ChatGPT guide (711 lines) - ChatGPT workflow

**Total:** 6,009 lines of core content  
**Status:** Production-ready

---

## WHAT'S NEXT (Optional)

### Phase 3: Technique Gaps (~1,000-1,500 lines)
- Document Self-Consistency technique
- Document ReAct framework
- Document Few-Shot prompting
- Add comprehensive examples

### Phase 4: Polish (~500-800 lines)
- Update README.md with quick start
- Create CONTRIBUTING.md
- Final review and optimization

**Both phases are optional enhancements. Framework works now.**

---

## HOW TO USE (If User Asks)

### For LLMs (You Are Claude)

**When user requests Gemini prompt:**
1. Read `gemini_capabilities.md` → Know what Gemini can do
2. Read `technique_library.md` → Select 4-6 techniques
3. Read `web_ui_templates.md` → Apply Template A or B
4. Customize for user's topic
5. Deliver complete prompt with instructions

**Detailed workflow:** See `docs/guides/for_claude.md`

### For Users

**Simple 3-step process:**
1. Ask LLM: "Generate Gemini research prompt for [topic]"
2. Copy generated prompt
3. Paste into google.com/gemini

**Expected:** 1,500-2,000 lines of comprehensive research

---

## EVIDENCE BASE

**Foundation:** Two academic papers (1,582 lines)
- Paper 1: Empirical Evaluation (250 lines)
- Paper 2: Systematic Self-Assessment (1,332 lines)

**Testing:** 12 techniques tested empirically
- Dual scoring: Effectiveness (0-10) + Reliability (0-10)
- Example: Chain-of-Thought (10/10, 10/10)

**Documentation:** All findings in `docs/analysis/source_papers_complete_analysis.md`

---

## GIT STATUS

**Repository:** https://github.com/Dudley70/Gemini-Research  
**Branch:** main  
**Latest Commit:** 8508f27 phase2: COMPLETE  
**Status:** Clean, all changes committed and pushed

**To check status:**
```bash
cd /Users/dudley/Projects/Gemini-Research
git status
git log -5 --oneline
```

---

## DECISION LOG (Key Decisions Made)

**Decision #001:** Adopt ClaudeWorkflow structure  
**Decision #002:** PATH 1 (Web UI) primary, PATH 2 (API) secondary  
**Decision #003:** ChatGPT & Claude are sibling implementations  

**See PROJECT.md for full decision log with rationale**

---

## IF CONTINUING DEVELOPMENT

### Starting Phase 3 (Technique Gaps)

**Read first:**
- `docs/reference/technique_library.md` (gap techniques section)
- `docs/analysis/source_papers_complete_analysis.md` (technique gaps identified)

**Create:**
- `docs/methodology/techniques/self_consistency.md`
- `docs/methodology/techniques/react_framework.md`
- `docs/methodology/techniques/few_shot_prompting.md`

### Starting Phase 4 (Polish)

**Update:**
- `README.md` with complete quick start guide
- Create `CONTRIBUTING.md` for community contributions
- Final review of all cross-references

---

## IF HELPING USER

### User Wants Framework Overview

**Direct them to:** `FRAMEWORK_GUIDE.md`

**Explain:** "This framework helps me generate high-quality research prompts for Gemini. I read the docs, select techniques, customize a template, and give you a complete prompt to paste into Gemini."

### User Wants Research Prompt

**Follow workflow in:** `docs/guides/for_claude.md`

**Process:**
1. Read capabilities (what Gemini can do)
2. Select techniques (4-6 compatible)
3. Apply template (A for comprehensive, B for decisions)
4. Customize for their topic
5. Deliver with usage instructions

### User Confused About Process

**Clarify:**
```
Simple 3 steps:
1. I generate a prompt (based on framework)
2. You copy it
3. You paste it into Gemini at google.com/gemini

Then Gemini does the research and gives you 1,500-2,000 lines
of comprehensive analysis.
```

---

## CRITICAL FILES

**Must Read (For Context):**
1. `FRAMEWORK_GUIDE.md` - Complete overview
2. `SESSION.md` - Current state
3. `docs/INDEX.md` - Documentation map

**Must Read (For Usage):**
4. `docs/reference/gemini_capabilities.md` - What Gemini can do
5. `docs/reference/technique_library.md` - Technique selection
6. `docs/methodology/templates/web_ui_templates.md` - Templates

**Optional (For Deep Understanding):**
7. `docs/methodology/principles/core_discoveries.md` - Why it works
8. `docs/enhancements/unified_methodology.md` - Integration
9. `docs/guides/for_claude.md` - Your specific workflow

---

## QUICK STATS

**Documentation:** 8,823 lines  
**Techniques:** 17 (12 tested + 5 gaps)  
**Templates:** 2 (comprehensive + strategic)  
**Quality Target:** ≥8.5/10  
**Expected Output:** 1,500-2,000 lines from Gemini  
**Time to Context:** 3-5 minutes (read this + FRAMEWORK_GUIDE.md)

---

## SUCCESS CRITERIA (All Met)

✅ Cross-platform (works with any LLM)  
✅ Evidence-based (1,582 lines of research)  
✅ Production-ready (9-10/10 outputs)  
✅ Complete entry point (FRAMEWORK_GUIDE.md)  
✅ Integration guide (unified methodology)  
✅ LLM-specific workflows (Claude + ChatGPT)  
✅ Documented and committed to GitHub

---

## FINAL CONTEXT

**What:** Cross-LLM framework for Gemini prompt generation  
**Why:** Enable any LLM to produce high-quality research prompts  
**How:** Templates + Techniques + Quality assurance  
**Status:** Production-ready (Phase 1 + 2 complete)  
**Next:** Optional enhancements (Phase 3 + 4)  
**Location:** /Users/dudley/Projects/Gemini-Research  
**GitHub:** https://github.com/Dudley70/Gemini-Research

**Read FRAMEWORK_GUIDE.md for complete details.**

---

**Last Session:** 2025-11-13 23:00 - 2025-11-14 00:50 AEDT (1hr 50min)  
**Status:** COMPLETE - Ready for handover  
**Context Recovery:** 3-5 minutes (this file + FRAMEWORK_GUIDE.md)
