---
name: design-to-frontend-workflow
description: Use when designing or redesigning a web or app interface that should move from product direction through Stitch or visual exploration, Figma, frontend implementation, and browser-based visual validation.
---

# Design To Frontend Workflow

## Overview

Turn UI work into a traceable sequence with explicit artifacts and approval gates. Keep product intent, formal design, implementation, and runtime validation aligned without treating generated UI as production-ready by default.

## Required Skills

- **REQUIRED:** Use `brainstorming` before choosing or changing product direction.
- Use `stitch-design-taste` when preparing Stitch inputs or `DESIGN.md`.
- Use `design-taste-frontend` for implementation.
- Use `high-end-visual-design` only when the approved direction calls for premium visual polish.
- Use the Figma MCP whenever a Figma file or Figma delivery is part of the task.
- Use the Browser plugin for runtime and responsive verification.

Do not load every visual skill automatically. The approved design direction decides which visual skill applies.

## Start By Detecting State

Inspect the repository and existing design tools before acting. Find:

- Product requirements and project instructions.
- Existing `UI-BRIEF.md`, `DESIGN.md`, screen specs, decision records, or visual QA reports.
- Existing frontend stack and dependencies.
- Figma links or connected Figma files.
- Current Stitch exports, screenshots, or reference images.

Classify the request into the earliest incomplete stage:

1. Product direction
2. Design system
3. Visual exploration
4. Formal design
5. Frontend implementation
6. Runtime validation

Resume there. Do not restart completed stages unless the user asks to reconsider them or evidence shows they are stale.

## Project Artifacts

Prefer this project-local structure:

```text
design/
├── UI-BRIEF.md
├── DESIGN.md
├── screens/
│   └── <screen-name>.md
├── decisions/
│   └── YYYY-MM-DD-<decision>.md
└── visual-qa/
    └── <screen-name>.md
```

Use the templates in `assets/`. Adapt their content to the project; do not copy placeholder text unchanged.

Source-of-truth hierarchy:

| Concern | Source of truth |
|---|---|
| Product intent and scope | `design/UI-BRIEF.md` |
| Visual language and tokens | `design/DESIGN.md` |
| Approved screen composition | Figma, or screen spec when Figma is intentionally skipped |
| Runtime behavior | Frontend code |
| Fidelity and responsive evidence | `design/visual-qa/` |

Stitch is an exploration tool, not the final source of truth.

## Workflow

### 1. Product Direction

Clarify the primary user, core task, product identity, information density, emotional tone, and target devices. Offer two or three materially different directions, not palette swaps.

**Gate:** The user approves one direction. Record it in `UI-BRIEF.md` and a decision file.

### 2. Design System

Create or update `DESIGN.md` using approved direction and real product constraints. Define:

- Atmosphere and design dials.
- Color roles and tokens.
- Typography and spacing.
- Surfaces, borders, radii, elevation, and icons.
- Motion and reduced-motion behavior.
- Responsive rules.
- Loading, empty, error, disabled, focus, and destructive states.
- Explicit anti-patterns.

**Gate:** Tokens and rules are concrete enough that two screens would look related without copying layouts.

### 3. Visual Exploration

Use Stitch to generate two or three high-fidelity alternatives when broad visual exploration is valuable. Give every alternative the same functional requirements and `DESIGN.md`, while varying composition or emphasis.

Evaluate alternatives against product fit, hierarchy, accessibility, responsive plausibility, and implementation cost. Record what is selected, rejected, and merged.

If Stitch is unavailable or intentionally skipped, use Visual Companion, Figma, or static mockups. Preserve the same evaluation gate.

**Gate:** One composition is approved, including any elements merged from other alternatives.

### 4. Formal Design

Use Figma to turn the approved composition into maintainable design:

- Variables or styles for tokens.
- Reusable components and variants.
- Desktop and mobile frames.
- Component states.
- Prototype only the flows needed to resolve interaction questions.

Do not clean every generated layer blindly. Rebuild repeated UI as components.

If Figma is skipped, make the screen spec authoritative and include exact layout, tokens, states, and responsive behavior.

**Gate:** The implementation target is unambiguous and covers required states.

### 5. Frontend Implementation

Inspect the codebase and follow its stack and component conventions. Verify dependencies before importing them. Implement reusable primitives from tokens, then screen composition, interaction states, and responsive behavior.

Do not copy generated Stitch HTML into production without architectural review.

**Gate:** Build, type checks, and relevant tests pass.

### 6. Runtime Validation

Open the implementation with Browser. Compare it with the approved Figma frame or screen spec at representative desktop and mobile viewports.

Verify:

- Visual hierarchy, alignment, spacing, typography, color, and icon consistency.
- Loading, empty, error, disabled, focus, hover, active, and reduced-motion states.
- No horizontal overflow or clipped controls.
- Keyboard usability and reasonable contrast.
- Motion uses transform and opacity where possible.

Record differences in `design/visual-qa/<screen>.md`, fix material issues, and recheck.

**Gate:** No unresolved high-impact visual, interaction, responsive, or accessibility differences remain.

## Scope Rules

- For a small component change, reuse existing project artifacts and run only affected stages.
- For a new product or major redesign, use the complete workflow.
- Do not require Stitch or Figma when the user explicitly excludes them.
- Do not mark a stage complete from intent alone; require its artifact or runtime evidence.
- Ask for approval at product-direction and formal-design decisions. Do not ask for approval between mechanical implementation steps.

## Handoffs

Read `references/tool-handoffs.md` before moving content between Stitch, Figma, and code.
Read `references/acceptance-scenarios.md` when validating this skill or handling an unusual entry point.

## Completion Report

Report:

- Current source-of-truth files.
- Approved direction and screens implemented.
- Verification performed.
- Remaining design decisions or fidelity gaps.

Do not claim end-to-end completion if Figma or browser validation was required but not performed.
