# AI‑Powered Digital Process Consultant Mastery Course — Claude Code Generation Blueprint

> **Purpose of this document** Guide Claude Code CLI to auto‑generate an end‑to‑end, self‑paced course that surpasses flagship executive programs in depth and practicality, while staying certificate‑ready (you’ll issue the certificate yourself). Everything below is an explicit instruction set; Claude should follow it *exactly*, pausing only where review is required.

---

## 1 High‑Level Goals

1. **Outcome‑focused:** enable the learner (Haniel) to analyse, redesign and automate business processes for US‑based SMEs, then sell & deliver consulting engagements.
2. **Portfolio‑driven:** every level produces a *real* artefact (maps, automation scripts, client reports) that doubles as portfolio proof.
3. **Bilingual mastery:** all learning material is first produced in **English (US context)**, then **translated into Portuguese** while preserving US business terminology.
4. **Interactive & applied:** quizzes are HTML/JS‑based, scenario‑driven and provide immediate feedback; projects use real‑world print‑shop examples where possible.

---

## 2 Overall Course Architecture

| Level        | Title                      | Primary Competency                                                        | Core Deliverables                                                            |
| ------------ | -------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **0**        | Foundations                | Systems thinking, BPMN, Lean/Six Sigma basics                             | Reading pack, worksheet: map a pizza shop order flow, 10‑question quiz       |
| **1**        | Analysis & Design          | Stakeholder interviews, AS‑IS → TO‑BE mapping, KPI design                 | Interview script template, root‑cause fishbone, improved TO‑BE map, quiz     |
| **2**        | Tech Integration           | Automation stack (RPA, Zapier, n8n, APIs), database modelling, AI agents  | Hands‑on lab: build Zapier flow; ER diagram; quiz                            |
| **3**        | Strategy & Change          | Digital transformation frameworks, change mgmt., agile delivery, ROI calc | Transformation roadmap slide‑deck, ROI calculator sheet, quiz                |
| **4**        | Client Delivery            | Discovery, pricing, proposals, objection handling, post‑launch support    | Fixed‑fee “Process X‑Ray” playbook, proposal template, final exam            |
| **Capstone** | Full Engagement Simulation | End‑to‑end practice with a fictional \$5 M manufacturing SME              | 25‑page client report, automation demo video script, self‑issued certificate |

> *Prompt Claude to generate each level sequentially; pause after producing all artefacts in a level for user review before continuing.*

---

## 3 Detailed Chapter Breakdown

### Level 0 Foundations

1. **0.1 Systems Thinking 101** – mental models, feedback loops, causal‑loop diagrams.
2. **0.2 Business Process Basics** – value chains, SIPOC, process vs. procedure.
3. **0.3 Process Mapping with BPMN** – notation essentials, swim‑lanes, gateways.
4. **0.4 Lean & Six Sigma Intro** – waste types, DMAIC overview, basic metrics.

### Level 1 Analysis & Design

1. **1.1 Stakeholder Interviewing** – questioning techniques, empathy mapping.
2. **1.2 AS‑IS Mapping & Bottleneck Hunting** – cycle time, takt time, Mura/Muri/Muda.
3. **1.3 Root‑Cause & Data Capture** – 5 Whys, Ishikawa, collection plan.
4. **1.4 TO‑BE Design & KPI Definition** – future‑state map, SMART metrics.

### Level 2 Tech Integration

1. **2.1 Automation Landscape** – RPA vs. iPaaS vs. custom scripts.
2. **2.2 Low‑Code Workflow Tools** – Zapier, Make, n8n hands‑on.
3. **2.3 Databases & Entities** – relational basics, ERD, CRUD thinking.
4. **2.4 AI in Processes** – LLM prompt engineering, retrieval‑augmented workflows.

### Level 3 Strategy & Change

1. **3.1 Digital Transformation Frameworks** – MIT, McKinsey 7‑S, Gartner.
2. **3.2 Change Management** – ADKAR, Kotter, stakeholder resistance.
3. **3.3 Agile Governance** – scrum‑ban for ops improvement; OKRs.
4. **3.4 ROI & Benefits Realisation** – NPV, payback, scorecards.

### Level 4 Client Delivery

1. **4.1 Discovery & Process X‑Ray** – 1‑day assessment productised offer.
2. **4.2 Pricing & Proposals** – value‑based pricing, tiered offers.
3. **4.3 Communication & Objection Handling** – scripts, framing, storytelling.
4. **4.4 Post‑Implementation Support** – hyper‑care, KPI dashboards, upsell paths.
5. **4.5 Personal Brand & GTM** – LinkedIn authority loops, content calendar.

---

## 4 File & Folder Convention

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

*X = level number, Y = chapter number.*

---

## 5 Chapter Template Claude Must Use

```markdown
# LX.CY <Chapter Title>

## Learning Objectives
- … (3–5 bullet goals)

## Real‑World Scenario
Narrative opening (≈150 words) presenting a US‑based SME challenge.

## Core Theory (≲800 words)
Explain concepts needed to solve scenario; use plain English, minimal jargon.

## Tool Demonstration
```

- If automation tool: step‑by‑step numbered list (max 10 steps)
- If diagram: include Mermaid **inside code block**

```

## Mini Project
Describe a hands‑on task using learner’s own environment; specify deliverable file(s).

## Quiz Placeholder
`<QUIZ_LINK will be replaced by generated HTML file>`

---
### Portuguese Version
*(exact same structure, translated; retain English technical terms in parentheses)*
```

Claude must output both English and Portuguese sections back‑to‑back.

```

---
## 6 Quiz Generation Rules
1. 8–12 questions: mix of multiple‑choice, drag‑and‑drop (HTML5), short answer.
2. Every wrong answer yields a custom explanation.
3. Single self‑contained HTML file; inline CSS/JS only (no external libs).
4. Auto‑score at submission; pass mark ≥ 80 %.

---
## 7 Diagrams & Visuals
- Prefer Mermaid where possible; else export PNG (base64) into /assets/.
- Each BPMN diagram includes swimlanes for at least two roles.

---
## 8 Translation Guidelines
- Keep US cultural context intact; do **not** localise examples to Brazil.
- Translate prose, but leave acronyms & tool names in English.
- Provide side‑by‑side glossary file (English, Portuguese, definition).

---
## 9 Generation Workflow for Claude Code
1. **Read this blueprint.**
2. Prompt user: “Ready to generate Level 0. Proceed?”
3. On confirmation:
    1. Create `/Level0/en` & `/Level0/pt` folders.
    2. For each chapter, generate: reading MD (EN & PT), quiz HTML, project brief, solution guide.
    3. Zip Level 0 folder, output download link.
4. Pause, await user feedback before Level 1.
5. Repeat until capstone complete.

---
## 10 Capstone Specifications
- **Client:** fictitious 200‑employee light‑manufacturing company in Ohio.
- **Brief:** reduce order‑to‑cash cycle by 30 % within 6 months.
- **Artifacts:** discovery transcript, AS‑IS/TO‑BE maps, automation PoC (Zapier scenario), 25‑page report, 5‑slide exec deck, self‑signed PDF certificate (fill learner name, date).

---
## 11 Style & Tone Rules
- Professional, concise, skeptical; avoid hype.
- Include real numbers & analogies, e.g., “cutting 2 hrs per 10‑order batch equals +$12 K/year.”
- Use second‑person singular (“you”).
- Break up long paragraphs with sub‑headings.

---
## 12 Review Checkpoints
After each level, Claude must prompt for:
- Accuracy of translations
- Practical relevance of examples
- Usability of quizzes
- Any required tweaks

Incorporate feedback before starting next level.

---
## 13 Completion Criteria
Course is ‘done’ when:
- All 5 levels plus capstone folders generated & reviewed
- Glossary CSV populated (>150 terms)
- Certificate template exported as editable PDF
- Index.md README summarises structure and study tips

---
### End of Blueprint
*Claude, acknowledge receipt and await “Proceed Level 0” command.*

```
