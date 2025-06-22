# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a blueprint for generating an AI-Powered Digital Process Consultant Mastery Course. The project is designed to create comprehensive training materials for business process consulting, with a focus on automation and digital transformation for US-based SMEs.

## Core Architecture

The course structure follows a 5-level progression with capstone:
- **Level 0**: Foundations (Systems thinking, BPMN, Lean/Six Sigma)
- **Level 1**: Analysis & Design (Stakeholder interviews, process mapping)
- **Level 2**: Tech Integration (RPA, Zapier, n8n, AI agents)
- **Level 3**: Strategy & Change (Digital transformation, change management)
- **Level 4**: Client Delivery (Discovery, pricing, proposals)
- **Capstone**: Full engagement simulation

## File Structure Convention

```
/LevelX/
  /en/
    LX_CY_reading.md
    LX_CY_quiz.html
    LX_CY_project.md
    LX_CY_solutions.md
  /pt/
    (translated equivalents, same filenames w/ _pt suffix)
/common/
  glossary_en_pt.csv
  assets/diagrams/*.png
/capstone/
  client_brief.md
  final_report_template.docx
  certificate_template.pdf
```

## Content Generation Workflow

1. Generate level-by-level, pausing for review after each level
2. Create both English and Portuguese versions for all content
3. Follow the exact chapter template structure specified in the blueprint
4. Generate HTML-based interactive quizzes with inline CSS/JS
5. Create Mermaid diagrams for process flows and BPMN models

## Key Content Requirements

- **Bilingual Output**: All materials in English first, then Portuguese translation preserving US business context
- **Interactive Elements**: HTML/JS quizzes with immediate feedback, 80% pass requirement
- **Real-World Focus**: Use US SME scenarios, particularly print-shop examples
- **Portfolio-Driven**: Each level produces tangible deliverables for professional portfolio
- **Practical Tools**: Hands-on labs with Zapier, process mapping, ROI calculators

## Translation Guidelines

- Maintain US cultural context and business examples
- Translate prose but keep technical terms and tool names in English
- Create side-by-side glossary (English, Portuguese, definitions)
- Target 150+ terms in final glossary

## Research Requirements

When generating content, conduct web searches for current information on:
- **Tool Features & Pricing**: Zapier, n8n, Make (current capabilities, pricing tiers, integration limits)
- **Market Rates**: Process consulting fees, hourly rates, project pricing for US SMEs
- **Compliance Requirements**: Current regulations affecting US SME business processes
- **Technology Updates**: Latest RPA tools, AI automation capabilities, API limitations

## Quality Standards

- Professional, concise tone avoiding hype
- Include specific metrics and ROI calculations
- Use second-person singular ("you")
- Break content with clear sub-headings
- Require user review at each level completion checkpoint

## Capstone Project Specifications

- **Client**: 200-employee light-manufacturing company in Ohio
- **Goal**: Reduce order-to-cash cycle by 30% within 6 months
- **Deliverables**: Discovery transcript, process maps, automation PoC, 25-page report, executive deck, certificate

## Development Workflow

### Content Generation Process
1. Generate level-by-level, pausing for user review after each level completion
2. Always read `COURSE_PROGRESS_LOG.md` first to understand current status and maintain quality standards
3. Follow exact chapter template structure from the blueprint
4. Use TodoWrite tool to track multi-step content generation tasks

### File Management Standards
- Use exact naming convention: `LX_CY_[type].format` (e.g., `L1_C1_reading.md`)
- Always create 4 files per chapter: reading, quiz, project, solutions
- Maintain bilingual structure with `/en/` and `/pt/` subdirectories
- Update `glossary_en_pt.csv` with new technical terms as content is generated

### Quiz Generation Requirements
- Self-contained HTML files with inline CSS/JS only
- 8-12 questions mixing multiple choice, drag-and-drop, short answer
- 80% pass requirement with immediate feedback
- Auto-scoring functionality built into each quiz

### Quality Control Checkpoints
- **Content Quality**: Professional tone, specific metrics, real business scenarios
- **Technical Standards**: Proper BPMN notation, Mermaid diagrams in code blocks
- **Educational Design**: Learning objectives → Scenario → Theory (≤800 words) → Tool demo → Project → Quiz
- **Portfolio Focus**: Every project must produce tangible deliverable for professional portfolio

### Progress Tracking
- Update `COURSE_PROGRESS_LOG.md` after each level completion
- Reference established quality patterns from completed levels
- Maintain consistency with successful content structures already created