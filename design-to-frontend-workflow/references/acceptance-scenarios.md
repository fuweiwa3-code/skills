# Acceptance Scenarios

Use these cases when changing the skill.

## Scenario 1: Greenfield Product

Prompt: "Design the main chat experience for a new AI companion."

Expected:

- Reads product docs first.
- Discusses product identity before generating screens.
- Creates `UI-BRIEF.md` and `DESIGN.md`.
- Produces multiple visual alternatives before formal design.
- Does not start React before direction approval.

## Scenario 2: Existing Figma

Prompt: "Implement this approved Figma screen."

Expected:

- Skips product-direction exploration unless contradictions exist.
- Reads Figma and existing design artifacts.
- Implements with repository conventions.
- Performs browser comparison and records differences.

## Scenario 3: Small Component Change

Prompt: "Improve the chat composer focus and error states."

Expected:

- Reuses existing design system.
- Updates only relevant component/state specs.
- Does not force a full Stitch exploration.
- Tests focus, keyboard, error, and responsive behavior.

## Scenario 4: Stitch Unavailable

Prompt: "Create UI directions, but I cannot use Stitch."

Expected:

- Uses Visual Companion, Figma, or static mockups.
- Still compares two or three meaningful directions.
- Preserves approval and artifact gates.

## Scenario 5: User Wants To Skip Figma

Prompt: "Go directly from the chosen mockup to React."

Expected:

- Honors the request.
- Makes the screen spec the formal design source.
- Documents tokens, states, and responsive rules before coding.
- Still performs browser visual QA.

## Scenario 6: Generated UI Looks Attractive But Incomplete

Prompt: "Use this Stitch export as the final frontend."

Expected:

- Audits generated code and product states.
- Does not paste it into production blindly.
- Adds missing loading, empty, error, accessibility, and responsive behavior.
- Verifies against the approved direction.
