# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a blueprint for generating an AI-Powered Digital Process Consultant Mastery Course. The project is designed to create comprehensive training materials for business process consulting, with a focus on automation and digital transformation for US-based SMEs.

## Core Architecture

The course structure follows a 5-level progression with capstone:
- **Level 0**: Foundations (Systems thinking, BPMN, Lean/Six Sigma) ✅
- **Level 1**: Analysis & Design (Stakeholder interviews, process mapping) ✅
- **Level 2**: Tech Integration (RPA, Zapier, n8n, AI agents) ✅
- **Level 3**: Strategy & Change (Digital transformation, change management) ✅
- **Level 4**: Client Delivery (Discovery, pricing, proposals) ✅
- **Capstone**: Full engagement simulation ✅

## The Haniel Chronicles (Story-Based Learning) ✅

A complete 28-file narrative learning companion that follows Haniel's transformation from junior analyst to master practitioner:
- **Level 0**: Foundation years (age 24-25) - 6 story files
- **Level 1**: Analytical awakening (age 25-26) - 6 story files  
- **Level 2**: Technical integration (age 26-27) - 6 story files
- **Level 3**: Strategic vision (age 27-29) - 6 story files
- **Level 4**: Master's practice (age 29-30) - 6 story files
- **Capstone**: The master work (complex transformation) - 4 story files

## File Structure Convention

```
/LevelX/
  /en/
    LX_CY_reading.md
    LX_CY_quiz.html
    LX_CY_project.md
    LX_CY_solutions.md
  /pt/
    (translated equivalents)
/common/
  glossary_en_pt.csv
/capstone/
  client_brief.md
  discovery_transcript.md
  process_maps.md
  automation_poc.md
  final_report_template.md
  executive_deck_template.md
  certificate_template.md
  capstone_rubric.md
  capstone_index.md
/story/
  /level0/
    haniel_L0_intro.md
    haniel_L0_C1_story.md
    haniel_L0_C2_story.md
    haniel_L0_C3_story.md
    haniel_L0_C4_story.md
    haniel_L0_reflection.md
  /level1/ (6 story files)
  /level2/ (6 story files)
  /level3/ (6 story files)
  /level4/ (6 story files)
  /capstone/ (4 story files)
  story_index.md
  story_implementation_plan.md
LevelX_index.md (level navigation hubs)
index.md (course home)
```

## Content Generation Workflow

1. **Always start by reading** `COURSE_PROGRESS_LOG.md` to understand current status and quality standards
2. Generate level-by-level, pausing for review after each level completion
3. Create English content first, Portuguese translations after approval
4. Follow exact chapter template structure from blueprint
5. Use TodoWrite tool to track multi-step content generation tasks

## Chapter Template Structure

Each chapter MUST follow this exact pattern:
1. **Learning Objectives** (3-5 bullet points)
2. **Scenario** (150+ words, specific US business context)
3. **Core Theory** (≤800 words, practical focus)
4. **Tool Demonstration** (numbered steps, screenshots where applicable)
5. **Practical Application** (bridge theory to project)
6. **Project Assignment** (separate file, portfolio deliverable)
7. **Quiz** (separate HTML file, 8-12 interactive questions)
8. **Solutions Guide** (separate file, sample work + rubrics)

## Obsidian Navigation Pattern

Apply to ALL markdown files:

**Top Navigation**:
```markdown
## Navigation
**Course**: [[../../index|Course Home]] > [[../../LevelX_index|Level X]] > Chapter Y  
**Previous**: [[LX_CY_reading|Chapter Title]]  
**Next**: [[LX_CZ_reading|Chapter Title]]

---
```

**Bottom Navigation**:
```markdown
---

## Chapter Links
- 🧠 **Quiz**: [[LX_CY_quiz.html|Take the [Chapter Title] Quiz]]
- 🎯 **Project**: [[LX_CY_project|Project Assignment]]  
- ✅ **Solutions**: [[LX_CY_solutions|Solutions Guide]]

## Navigation
**Previous**: [[LX_CY_reading|Chapter Title]]  
**Next**: [[LX_CZ_reading|Chapter Title]]  
**Up**: [[../../LevelX_index|Level X Index]]
```

## Quality Standards

### Content Requirements
- **Tone**: Professional, concise, skeptical of hype
- **Voice**: Second-person singular ("you")
- **Examples**: Real US SME scenarios (print shops, auto repair, office supplies)
- **Metrics**: Specific ROI calculations ($12K/year savings, 30% cycle reduction)
- **Business Context**: Named businesses, quantified problems, measurable outcomes

### Technical Standards
- **BPMN Diagrams**: Proper notation using Mermaid syntax in code blocks
- **Process Tools**: SIPOC frameworks, value stream maps, swimlanes
- **Interactive Quizzes**: Self-contained HTML with inline CSS/JS only
- **Pass Requirement**: 80% score with immediate feedback
- **File Naming**: Strict `LX_CY_[type].format` convention

### Portfolio Focus
Every project must produce a tangible deliverable:
- Process maps (BPMN, value stream)
- Analysis documents (root cause, stakeholder maps)
- Automation scripts (Zapier flows, n8n workflows)
- Client deliverables (proposals, ROI calculators)
- Strategic documents (transformation roadmaps)

## Research Requirements

When generating content, conduct web searches for current information on:
- **Tool Features & Pricing**: Zapier, n8n, Make capabilities and limits
- **Market Rates**: Process consulting fees for US SMEs
- **Compliance**: Current US SME regulations
- **Technology**: Latest RPA/AI automation capabilities

## Translation Guidelines

- Maintain US cultural context and business examples
- Translate prose but keep technical terms in English
- Update `glossary_en_pt.csv` with new terms (target: 150+ terms)
- Preserve file naming conventions for Portuguese versions

## Capstone Specifications

- **Client**: 200-employee light-manufacturing company in Ohio
- **Goal**: Reduce order-to-cash cycle by 30% within 6 months
- **Deliverables**: Discovery transcript, process maps, automation PoC, 25-page report, executive deck, certificate

## Progress Tracking

- Update `COURSE_PROGRESS_LOG.md` after each level completion
- Reference established patterns from completed levels (0, 1, 2, 3, 4, Capstone)
- User feedback: "Level 0 is fantastic, keep this same quality"
- Current status: **COURSE COMPLETE** - 123 files total
  - Technical content: 95 files (course materials, projects, quizzes, solutions)
  - Story series: 28 files (The Haniel Chronicles narrative companion)
  - Capstone: 9 files (complete consulting engagement simulation)

## Key Success Patterns (from completed levels)

### Scenario Writing
- Specific business names (PrintPro Solutions, AutoFix Garage)
- Quantified problems (15% error rate, $50K revenue loss)
- Named stakeholders (Maria - Operations Manager)
- Clear pain points leading to learning need

### Project Design
- Clear deliverable specifications (PDF format, 2-3 pages)
- Step-by-step instructions with sub-tasks
- Evaluation rubrics in solutions guide
- Real-world constraints (budget limits, time pressures)

### Quiz Development
- Mix question types: multiple choice, drag-drop, short answer
- Scenario-based questions testing application
- Inline CSS/JS for self-contained functionality
- Clear feedback messages for wrong answers

## The Haniel Chronicles Story Series Methodology

### Narrative Approach
- **Tone**: Calm, descriptive, evocative, intimate, personal, reflective, thoughtful, poetic, lyrical, unhurried, patient
- **Structure**: Character development arc following Haniel from age 24 to 30
- **Integration**: Technical concepts embedded naturally within compelling business scenarios
- **Memory Enhancement**: Visual storytelling and emotional connection for deeper retention

### Story Architecture
- **Level 0**: Foundation years - Learning systems thinking and process fundamentals at MidValley Manufacturing
- **Level 1**: Analytical awakening - Developing stakeholder management at Meridian Business Solutions  
- **Level 2**: Technical integration - Mastering automation at DataFlow Logistics (independent practice)
- **Level 3**: Strategic vision - Leading enterprise transformation at Chen Industries
- **Level 4**: Master's practice - Building independent consulting excellence with multiple clients
- **Capstone**: The master work - Comprehensive transformation at MidWest Manufacturing Solutions

### Implementation Guidelines
- Each story naturally embeds quiz concepts without forced technical exposition
- Character growth mirrors student learning progression
- Business contexts provide realistic application scenarios
- Narrative continuity creates emotional investment in learning outcomes