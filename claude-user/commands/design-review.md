---
description: Launch ux-ui-designer for UI/design review with Playwright
argument-hint: [PR number or URL]
---

# Design Review

Launch ux-ui-designer to conduct comprehensive design review of UI changes using Playwright for live environment testing.

## Process

1. **Identify Review Target**
   - PR number: Fetch PR details from GitHub
   - URL: Direct preview URL
   - If omitted: Review current branch changes

2. **Set Up Environment**
   - Start preview server if needed
   - Initialize Playwright browser
   - Configure viewport (1440x900 desktop)

3. **Execute Review Phases**
   - **Phase 1:** Interaction & user flow
   - **Phase 2:** Responsiveness (desktop/tablet/mobile)
   - **Phase 3:** Visual polish (spacing, typography, colors)
   - **Phase 4:** Accessibility (WCAG AA)
   - **Phase 5:** Robustness (error states, edge cases)
   - **Phase 6:** Code health (design system compliance)
   - **Phase 7:** Console errors check

4. **Generate Report**
   - Summary with overall assessment
   - Findings categorized:
     - Blockers
     - High-priority
     - Medium-priority
     - Nitpicks
   - Screenshots for visual issues
   - Recommendations

## Arguments

- **$1**: Optional PR number or preview URL
  - `123` - Review PR #123
  - `https://preview.app` - Review preview URL
  - If omitted: Review current branch

## Examples

```bash
# Review specific PR
/design-review 234

# Review preview URL
/design-review https://preview-abc123.app

# Review current branch
/design-review
```

## Requirements

- Live preview environment accessible
- Playwright installed (`npx playwright install`)
- Design system skills loaded automatically

## Notes

- Uses Playwright for automated interaction testing
- Captures screenshots for visual evidence
- Verifies design-system compliance
- Creates design review report in `.claude/reports/design/`
