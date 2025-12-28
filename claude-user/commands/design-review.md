---
description: UI/UX review with ux-designer agent (mode: design)
argument-hint: [PR number or URL]
---

# Design Review

## Process

1. **Target:** PR number → fetch PR | URL → preview | None → current branch
2. **Setup:** Start preview server, initialize Playwright
3. **Review:** Interaction, responsiveness, visual, accessibility, code health
4. **Report:** Findings in `.claude/reports/design/`

## Arguments

- `[number]` - PR number (e.g., `234`)
- `[url]` - Preview URL
- None - Current branch changes

## Review Phases

1. Interaction & user flow
2. Responsiveness (desktop/tablet/mobile)
3. Visual polish (spacing, typography, colors)
4. Accessibility (WCAG AA)
5. Error states & edge cases
6. Design system compliance
7. Console errors

## Output

- Summary with overall assessment
- Categorized findings (blockers/high/medium/nitpicks)
- Screenshots for visual issues
