# Source Materials Archive

**Created:** 2025-11-13 23:55 AEDT  
**Purpose:** Preserve original source materials from Gemini Research Method repository  
**Status:** Reference only - adapted versions exist in docs/methodology/

---

## What These Files Are

This directory contains the **original source materials** from the Gemini Research Method repository that both the ChatGPT v1.3.0 Pack and Claude's methodology branches were derived from.

**Source Location:** `/Users/dudley/Projects/Gemini Research Method/`

**Files Archived:**
- `01_PRINCIPLES.md` (370 lines) - Original meta-learnings and technique classifications
- `02_TEMPLATES.md` (613 lines) - Original production templates for Web UI and API
- `README.md` (286 lines) - Original infrastructure documentation
- `papers/` - The two academic papers (1,582 lines total)
  - `Gemini Pro Prompting Capability Assessment.md` (250 lines)
  - `Gemini Prompting Capability Self-Assessment.md` (1,332 lines)

---

## Relationship to Adapted Content

**These are the SOURCE materials.** Our repository has adapted them for cross-LLM use:

### Original → Adapted Mappings

| Original Source | Adapted Version | What Changed |
|-----------------|-----------------|--------------|
| `01_PRINCIPLES.md` | `docs/methodology/principles/core_discoveries.md` | Reorganized for cross-LLM clarity, added evidence citations, expanded technique stacks |
| `02_TEMPLATES.md` | `docs/methodology/templates/web_ui_templates.md` | Removed API-specific parameters, emphasized PATH 1 (Web UI), added LLM usage workflow |
| Source papers | `docs/analysis/source_papers_complete_analysis.md` | Extracted key findings, documented all 12 tested techniques, identified gaps |

### Why Both Exist

**Original Files (this directory):**
- Preserve exact source material for reference
- Enable verification of adaptations
- Provide historical context
- Allow future reconciliation if needed

**Adapted Files (docs/methodology/):**
- Optimized for cross-LLM use (ChatGPT, Claude, etc.)
- Clear PATH 1 (Web UI) vs PATH 2 (API) separation
- Enhanced documentation and examples
- Integrated with new framework structure

---

## When to Reference These Files

**Use Original Source Materials When:**
- Verifying that adaptations preserve original intent
- Understanding historical context of techniques
- Comparing original vs adapted versions
- Researching specific implementation details from source

**Use Adapted Versions (docs/methodology/) When:**
- Building new research prompts
- Learning how to use the framework
- Generating prompts with ChatGPT or Claude
- Following current best practices

**Use Source Papers (papers/) When:**
- Need authoritative evidence for technique claims
- Understanding the research foundation
- Verifying effectiveness/reliability scores
- Deep-diving into specific technique testing

---

## Why We Preserve These

**1. Verification**
- Ensures adaptations remain faithful to source research
- Allows validation of claims and scores
- Provides audit trail for framework decisions

**2. Context**
- Shows evolution from research → principles → templates
- Documents what existed before this framework
- Enables understanding of adaptation choices

**3. Reference**
- Source of truth for original findings
- Baseline for future enhancements
- Historical record of methodology development

**4. Reconciliation**
- If discrepancies arise between branches, source materials are authoritative
- Both ChatGPT and Claude branches can be verified against these originals
- Future updates can check against source research

---

## Knowledge Chain

```
Source Papers (1,582 lines)
    ↓
    [Extracted by original researcher]
    ↓
01_PRINCIPLES.md (370 lines)
    ↓
    [Applied to create templates]
    ↓
02_TEMPLATES.md (613 lines)
    ↓
    [Branched into two implementations]
    ↓
┌────────────────────────┴────────────────────────┐
│                                                  │
▼                                                  ▼
Claude's Branch                           ChatGPT's Branch
(Cross-LLM docs)                         (Custom GPT automation)
    │                                                  │
    └─────────────────┬────────────────────────────────┘
                      │
                      ▼
            This Framework
    (Unified, cross-platform)
```

---

## Do Not Modify These Files

**CRITICAL:** Files in this directory are **read-only archives**.

- ✅ **DO:** Reference, read, compare, verify
- ❌ **DON'T:** Edit, update, or modify
- ✅ **DO:** Create new adapted versions in docs/methodology/
- ❌ **DON'T:** Change original source materials

If improvements are needed, create new documents in the appropriate docs/ subdirectories.

---

## File Descriptions

### 01_PRINCIPLES.md (370 lines)
**Original meta-learnings document** covering:
- Instruction Adherence vs Output Quality trade-off
- Tier 1/2/3 technique classifications
- Anti-patterns discovered through testing
- Technique compatibility insights
- Optimal stacks for different research types

**Adapted version:** `docs/methodology/principles/core_discoveries.md` (413 lines)

---

### 02_TEMPLATES.md (613 lines)
**Original production templates** including:
- Gemini 2.5 Pro architecture overview
- Template A: Comprehensive Foundation Research
- Template B: Strategic Decision Research
- Advanced technique patterns
- Quality checklists and pitfall tables

**Adapted version:** `docs/methodology/templates/web_ui_templates.md` (899 lines)

---

### README.md (286 lines)
**Original infrastructure documentation** explaining:
- Directory structure of source repository
- Knowledge chain from papers → principles → templates
- Document purposes and reading order
- Relationship to ClaudeWorkflow tools
- Learning paths for new users

**Note:** Historical context only - not applicable to this framework

---

### papers/ (1,582 lines total)

#### Gemini Pro Prompting Capability Assessment.md (250 lines)
- Third-party empirical evaluation
- Tests 4 core techniques
- Establishes single-shot execution boundary
- Validates effectiveness of prompting strategies

#### Gemini Prompting Capability Self-Assessment.md (1,332 lines)
- Gemini 2.5 Pro analyzing itself
- Tests 12 techniques with dual scoring (Effectiveness + Reliability)
- Multi-perspective critique methodology
- Identifies technique gaps and limitations

**Analysis:** `docs/analysis/source_papers_complete_analysis.md` (255 lines)

---

## Status

- ✅ Original materials archived for reference
- ✅ Adapted versions created in docs/methodology/
- ✅ Source papers analyzed and documented
- ✅ Verification pathway established
- ✅ Read-only preservation enforced

**Last Updated:** 2025-11-13 23:55 AEDT  
**Source:** `/Users/dudley/Projects/Gemini Research Method/`  
**Purpose:** Reference and verification only - use adapted versions for active work
