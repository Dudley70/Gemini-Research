# Gemini Research: Cross-LLM Prompt Engineering Framework

**Multi-LLM collaboration framework for generating effective Gemini research prompts**

[![Status](https://img.shields.io/badge/status-foundation-yellow)]()
[![Primary Use](https://img.shields.io/badge/primary%20use-Web%20UI-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## Overview

This repository enables **any LLM** (ChatGPT, Claude, etc.) to generate high-quality research prompts for **Gemini 2.5 Pro**, leveraging its 1M context window, speed, and research capabilities.

**Quality Target:** 9-10/10 research outputs consistently

---

## Two Execution Paths

### 🌐 PATH 1: Web UI (Primary - 95% Use Cases)

**Copy/paste prompts into Gemini Deep Research**

- **Interface:** google.com/gemini (Deep Research)
- **Output:** Human-readable prose (1,500-2,000 lines)
- **Use Case:** Interactive research, exploration, analysis
- **Templates:** Comprehensive Foundation or Strategic Decision
- **Docs:** `docs/methodology/`

**Workflow:**
1. LLM reads methodology → understands Gemini capabilities
2. LLM receives your research requirements
3. LLM generates Web UI prompt using templates
4. You copy/paste into Gemini Deep Research
5. Gemini returns comprehensive prose research

### 🔌 PATH 2: API (Secondary - Automation)

**Programmatic API calls for automation**

- **Interface:** Gemini API (programmatic)
- **Output:** Structured JSON for validation/integration
- **Use Case:** Automated pipelines, quality validation
- **Templates:** JSON schema-enforced formats
- **Docs:** `docs/api/`

---

## Quick Start

### For LLMs (ChatGPT, Claude, etc.)

1. Read `PROJECT.md` for strategic context
2. Review `docs/methodology/principles/` for proven techniques
3. Use `docs/methodology/templates/` to generate prompts
4. Follow PATH 1 (Web UI) workflow by default

### For Users

1. Describe your research need to your LLM
2. LLM generates Gemini prompt using this framework
3. Copy/paste generated prompt into Gemini Deep Research
4. Get high-quality research output

---

## Repository Structure

```
Gemini-Research/
├── PROJECT.md                    # Strategic context and principles
├── SESSION.md                    # Current session state
├── README.md                     # This file
│
└── docs/
    ├── INDEX.md                  # Documentation map
    │
    ├── methodology/              # PATH 1: Web UI (PRIMARY)
    │   ├── principles/           # Proven techniques, anti-patterns
    │   ├── templates/            # Web UI prompt templates
    │   └── patterns/             # Reusable prompt patterns
    │
    ├── api/                      # PATH 2: API (SECONDARY)
    │   ├── templates/            # JSON-based API prompts
    │   └── validators/           # Quality validation tools
    │
    ├── reference/                # Gemini capabilities, specs
    ├── guides/                   # LLM-specific how-tos
    ├── analysis/                 # Research findings
    └── enhancements/             # Proposed improvements
```

---

## Foundation

Based on proven **Gemini Research Method** with:
- 370 lines of extracted principles
- 613 lines of production templates
- Empirical testing achieving 9-10/10 quality
- Multi-technique combinations (Chain-of-Thought, Socratic, Quality Gates)

---

## Key Principles

1. **Web UI First:** Default to PATH 1 unless automation needed
2. **Evidence-Based:** All techniques validated through testing
3. **Template-Ready:** Practical, copy-paste solutions
4. **Cross-Platform:** Clear for any LLM to understand
5. **Quality-Focused:** 9-10/10 outputs consistently

---

## Contributing

This is a **cross-LLM collaboration framework**:
- ChatGPT can propose enhancements
- Claude can refine documentation
- Other LLMs can add techniques
- All contributions welcome

**Process:**
1. Test technique/enhancement
2. Document findings in `docs/analysis/`
3. Propose changes via pull request
4. Update `docs/INDEX.md`

---

## Status

**Current Phase:** Foundation
- ✅ Repository structure created
- ✅ PATH 1/PATH 2 distinction established
- ⏳ Port source materials from Gemini Research Method
- ⏳ Create LLM-specific guides
- ⏳ Add examples and use cases

---

## Source Attribution

Enhanced version of **Gemini Research Method**:
- Original research on Gemini 2.5 Pro capabilities
- Proven templates and techniques
- Empirical quality validation
- Foundation for this cross-LLM framework

---

## License

MIT License - See LICENSE file for details

---

**Created:** 2025-11-13  
**Maintained By:** Cross-LLM collaboration (ChatGPT, Claude Desktop, others)  
**Primary Use Case:** Web UI copy/paste (PATH 1)
