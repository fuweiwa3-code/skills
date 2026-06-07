# Tool Handoffs

## Product Discussion To DESIGN.md

Transfer decisions, not conversation history:

- Primary user and job.
- Product identity and emotional tone.
- Chosen layout direction.
- Density, variance, and motion targets.
- Accessibility and device constraints.
- Rejected directions and why.

## DESIGN.md To Stitch

Provide:

- The same product requirements for every alternative.
- Exact visual rules and anti-patterns.
- Required content and component states.
- Target desktop and mobile sizes.
- The dimension that should vary between alternatives.

Ask for materially different compositions. Do not ask Stitch to invent product scope.

## Stitch To Figma

Treat Stitch output as reference material:

1. Select or merge a composition.
2. Remove decorative UI that lacks product purpose.
3. Rebuild repeated elements as Figma components.
4. Replace local colors and type with variables or styles.
5. Add missing responsive frames and component states.
6. Check contrast, touch targets, and reading order.

## Figma To Code

Extract:

- Token names and values.
- Component inventory and variants.
- Layout rules, not only pixel positions.
- Assets and icon source.
- Required states and interactions.
- Desktop/mobile behavior.

Do not rely on screenshots alone when design context is available.

## Code To Browser QA

Compare at consistent viewports. Capture:

- Expected reference.
- Actual runtime screenshot.
- Difference description.
- Severity: blocker, major, minor, accepted.
- Resolution and recheck result.

Prefer fixing shared token or component causes before page-level exceptions.
