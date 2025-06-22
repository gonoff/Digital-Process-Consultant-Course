# Obsidian Navigation Pattern Documentation

## Overview
This document defines the consistent navigation structure to be applied to ALL course files for optimal Obsidian vault integration and user experience.

## Navigation Pattern Structure

### Top Navigation Section
Place immediately after the main title (H1):

```markdown
## Navigation
**Course**: [[../../index|Course Home]] > [[../../Level1_index|Level 1]] > Chapter X  
**Previous**: [[LX_CY_reading|Chapter Y: Chapter Title]]  
**Next**: [[LX_CZ_reading|Chapter Z: Chapter Title]]

---
```

### Bottom Navigation Section
Place at the very end of each file:

```markdown
---

## Chapter Links
- 🧠 **Quiz**: [[LX_CY_quiz.html|Take the [Chapter Title] Quiz]]
- 🎯 **Project**: [[LX_CY_project|Project Assignment]]  
- ✅ **Solutions**: [[LX_CY_solutions|Solutions Guide]]

## Navigation
**Previous**: [[LX_CY_reading|Chapter Y: Chapter Title]]  
**Next**: [[LX_CZ_reading|Chapter Z: Chapter Title]]  
**Up**: [[../../Level1_index|Level 1 Index]]
```

## Implementation Rules

### File Types and Patterns

**Reading Files** (`LX_CY_reading.md`):
- Top navigation: Course breadcrumb + Previous/Next chapters
- Bottom navigation: Links to quiz, project, solutions + repeated navigation

**Project Files** (`LX_CY_project.md`):
- Top navigation: Same as reading files
- Bottom navigation: Links to reading, quiz, solutions + navigation

**Quiz Files** (`LX_CY_quiz.html`):
- HTML files get minimal navigation (can add meta tags if needed)

**Solutions Files** (`LX_CY_solutions.md`):
- Top navigation: Same pattern as other files
- Bottom navigation: Full chapter links + navigation

### Link Syntax Rules

1. **Internal Links**: Always use `[[file_path|Display Text]]` format
2. **Relative Paths**: Use appropriate `../` levels to navigate directory structure
3. **File Extensions**: 
   - Quiz links include `.html` extension: `[[LX_CY_quiz.html|Quiz Title]]`
   - Other files omit extensions: `[[LX_CY_reading|Chapter Title]]`
4. **Display Text**: Use descriptive titles, not just file names

### Path Structure Examples

```
Level 1 files: [[../../index|Course Home]] > [[../../Level1_index|Level 1]]
Level 2 files: [[../../index|Course Home]] > [[../../Level2_index|Level 2]]
Cross-chapter: [[L1_C1_reading|Chapter 1: Stakeholder Interviewing]]
Up navigation: [[../../Level1_index|Level 1 Index]]
```

### Chapter Progression Examples

**Chapter 1.1 (First Chapter)**:
- Previous: `[[../../Level1_index|Level 1 Index]]`
- Next: `[[L1_C2_reading|Chapter 2: AS-IS Mapping & Bottleneck Hunting]]`

**Chapter 1.4 (Last Chapter of Level)**:
- Previous: `[[L1_C3_reading|Chapter 3: Root-Cause & Data Capture]]`
- Next: `[[../../Level2_index|Level 2: Tech Integration]]`

**Mid-Level Chapters**:
- Previous: `[[L1_CX_reading|Chapter X: Title]]`
- Next: `[[L1_CY_reading|Chapter Y: Title]]`

## Visual Elements

### Emojis for Chapter Links
- 🧠 **Quiz**: Interactive assessment
- 🎯 **Project**: Hands-on assignment  
- ✅ **Solutions**: Instructor guide

### Formatting Standards
- **Bold** for navigation labels (`**Course**:`, `**Previous**:`, etc.)
- Horizontal rules (`---`) to separate navigation from content
- Consistent spacing and indentation

## Quality Checklist

Before finalizing any course file, verify:

- [ ] Top navigation present with correct paths
- [ ] Bottom navigation with all chapter links
- [ ] Relative paths navigate correctly 
- [ ] Display text is descriptive and consistent
- [ ] File extensions correct (HTML for quizzes, none for others)
- [ ] Emojis and formatting match pattern
- [ ] Horizontal rules separate navigation from content

## Implementation Notes

- Apply this pattern to ALL new files created
- Maintain consistency across languages (English/Portuguese)
- Test links in Obsidian to ensure proper navigation
- Update navigation when adding new chapters or levels
- Keep display text concise but descriptive

This pattern creates a fully interconnected course experience optimized for Obsidian's linking and navigation capabilities.