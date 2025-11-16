---
name: design-review
description: Format for UI/UX design reviews and accessibility assessments
---

# Design Review Output Style

Use this format for UI/UX design reviews, accessibility audits, and visual design assessments.

## Template

```markdown
# Design Review: [Feature or Component Name]

**Reviewer:** [Agent Name]
**Date:** YYYY-MM-DD
**Review Target:** [PR, URL, or file path]
**Overall Design Quality:** X.X/10.0 ⭐⭐⭐

---

## Summary

[2-3 sentences summarizing the design changes and overall assessment]

**Recommendation:** ✅ Approve | ⚠️ Approve with Minor Fixes | ❌ Major Revision Needed

---

## Design Overview

**What Changed:**
- UI Component 1
- Feature 2
- Visual Update 3

**Affected Screens/Views:**
- Screen 1
- Screen 2

**Design System Compliance:** ✅ / ⚠️ / ❌

---

## Review Phases

### Phase 1: Visual Hierarchy & Layout

**Score:** X/10

**✅ Strengths:**
- [What works well]
- [Another positive aspect]

**⚠️ Issues:**

**Issue 1: [Title]**
- **Severity:** High | Medium | Low
- **Location:** [Component/screen]
- **Problem:** [Description]
- **Screenshot:** [If applicable]
- **Fix:** [Specific recommendation]
  ```css
  /* Current */
  .element { margin: 8px; }

  /* Recommended (design-system spacing) */
  .element { margin: var(--space-2); /* 8px */ }
  ```

### Phase 2: Color System Compliance

**Score:** X/10

**Brand Colors (UI Elements):** ✅ / ⚠️ / ❌
- Buttons: [Assessment]
- Navigation: [Assessment]
- Cards: [Assessment]
- Forms: [Assessment]

**Data Colors (Visualizations):** ✅ / ⚠️ / ❌
- Charts: [Assessment]
- Graphs: [Assessment]
- Treemaps: [Assessment]

**Critical Rules:**
- [ ] Brand colors used ONLY for UI elements
- [ ] Data colors used ONLY for charts/visualizations
- [ ] No mixing of brand and data colors
- [ ] All colors use CSS variables

**Issues:**
- [Color violation 1]
- [Color violation 2]

### Phase 3: Typography

**Score:** X/10

**Hierarchy:** ✅ / ⚠️ / ❌
- [ ] Proper heading levels (h1 → h2 → h3)
- [ ] Consistent font sizes (--text-xs through --text-4xl)
- [ ] Appropriate font weights
- [ ] Line height for readability

**Font Families:**
- Display: [Usage assessment]
- Body: [Usage assessment]
- Monospace: [Usage assessment]

**Issues:**
- [Typography issue 1]

### Phase 4: Spacing & Layout

**Score:** X/10

**Spacing System:** ✅ / ⚠️ / ❌
- [ ] Uses design system spacing (--space-1 through --space-16)
- [ ] Consistent padding/margins
- [ ] Generous white space (Tableau-inspired)
- [ ] No hardcoded spacing values

**Layout:**
- [ ] Proper use of flexbox/grid
- [ ] Logical visual grouping
- [ ] Clear content hierarchy

**Issues:**
- [Spacing issue 1]

### Phase 5: Responsiveness

**Score:** X/10

**Breakpoint Testing:**
- [ ] Mobile (375px): Layout adapts correctly
- [ ] Tablet (768px): Comfortable spacing
- [ ] Desktop (1440px): Optimal space usage

**Issues by Breakpoint:**

**Mobile (375px):**
- Issue 1: [Description]
- Issue 2: [Description]

**Tablet (768px):**
- Issue 1: [Description]

**Desktop (1440px+):**
- Issue 1: [Description]

### Phase 6: Accessibility (WCAG AA)

**Score:** X/10

**Color Contrast:**
- [ ] Text contrast ≥ 4.5:1 (or ≥ 3:1 for large text)
- [ ] UI component contrast ≥ 3:1
- [ ] No color-only information conveyance

**Keyboard Navigation:**
- [ ] All interactive elements reachable via Tab
- [ ] Logical tab order
- [ ] Visible focus indicators (3px minimum)
- [ ] Escape key closes modals/dropdowns

**Screen Reader:**
- [ ] Semantic HTML (nav, main, article, aside)
- [ ] ARIA labels for interactive elements
- [ ] Alt text for images
- [ ] Proper heading hierarchy

**Touch Targets:**
- [ ] Minimum 44x44px for interactive elements
- [ ] Adequate spacing between targets

**Issues:**
| Issue | WCAG Level | Impact | Fix |
|-------|------------|--------|-----|
| Low contrast | AA | High | Increase to 4.5:1 |
| Missing ARIA label | A | Medium | Add aria-label |

### Phase 7: Interaction & UX

**Score:** X/10

**User Flow:**
- [ ] Clear call-to-action
- [ ] Intuitive navigation
- [ ] Expected behavior
- [ ] Helpful feedback (loading states, success/error messages)

**Micro-interactions:**
- [ ] Smooth transitions (250ms default)
- [ ] Appropriate hover states
- [ ] Clear active states
- [ ] Meaningful animations

**UX Writing:**
- [ ] Tone matches context (calm for errors, encouraging for success)
- [ ] Clear, action-oriented microcopy
- [ ] No jargon for end users
- [ ] Error messages provide solutions

**Issues:**
- [UX issue 1]

---

## Findings Summary

### By Severity

**🔴 CRITICAL (Block Deployment):**
1. [Issue summary]
2. [Issue summary]

**🟡 HIGH (Fix Before Release):**
1. [Issue summary]
2. [Issue summary]

**🟢 MEDIUM (Nice to Have):**
1. [Issue summary]
2. [Issue summary]

**🔵 LOW (Polish/Nitpick):**
1. [Issue summary]

### By Category

| Category | Issues | Critical | High | Medium | Low |
|----------|--------|----------|------|--------|-----|
| Visual Design | 3 | 0 | 1 | 2 | 0 |
| Color System | 2 | 1 | 1 | 0 | 0 |
| Accessibility | 4 | 0 | 2 | 1 | 1 |
| Responsiveness | 2 | 0 | 0 | 2 | 0 |
| **TOTAL** | **11** | **1** | **4** | **5** | **1** |

---

## Test Evidence

**Browsers Tested:**
- ✅ Chrome 130
- ✅ Safari 17
- ✅ Firefox 120

**Devices Tested:**
- ✅ Desktop (1440px)
- ✅ iPad (768px)
- ✅ iPhone (375px)

**Accessibility Testing:**
- ✅ Keyboard navigation
- ✅ Screen reader (NVDA/VoiceOver)
- ✅ Color contrast validator

**Screenshots:**
- [Attach or reference screenshots of issues]

---

## Recommendations

### Must Fix (Before Deployment)
1. [Critical issue 1 - specific fix]
2. [Critical issue 2 - specific fix]

### Should Fix (Before Release)
1. [High-priority issue 1]
2. [High-priority issue 2]

### Nice to Have
1. [Medium-priority improvement]
2. [Polish suggestion]

---

## Design System Checklist

- [ ] Brand colors (#0176D3, #032D60) used for UI ONLY
- [ ] Data colors (#33BBEE, #0077BB) used for charts ONLY
- [ ] Spacing uses design tokens (--space-*)
- [ ] Typography follows hierarchy (--text-*)
- [ ] Shadows use dual-layer pattern (--shadow-sm/md/lg)
- [ ] Components follow BEM naming
- [ ] WCAG AA minimum (4.5:1 text, 3:1 UI)
- [ ] Keyboard navigation functional
- [ ] Responsive at 3 breakpoints minimum

---

## References

- Design System: `.claude/DESIGN_SYSTEM.md`
- Style Guide: `.claude/STYLE_GUIDE.md`
- UX Writing Guide: `.claude/UX_WRITING_GUIDE.md`
- WCAG Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
```

## Usage Guidelines

**Use this style for:**
- UI/UX design reviews
- Pull request design assessments
- Accessibility audits
- Design system compliance checks

**Key Principles:**
- Review in phases (visual → color → typography → spacing → responsive → a11y → UX)
- Provide specific CSS code examples
- Include screenshots for visual issues
- Test across browsers and devices
- Focus on WCAG AA compliance minimum
- Balance aesthetics with functionality
- Reference design system standards

**Phase Structure:**
1. Visual Hierarchy & Layout
2. Color System Compliance (critical for dual-palette design system)
3. Typography
4. Spacing & Layout
5. Responsiveness
6. Accessibility (WCAG AA)
7. Interaction & UX

**Scoring:**
- 9.0-10.0: Excellent (⭐⭐⭐)
- 7.0-8.9: Good (⭐⭐)
- 5.0-6.9: Needs Improvement (⭐)
- <5.0: Major Revision Needed (❌)

## Examples

**Good Design Review:**
- Structured phase-by-phase assessment
- Specific CSS code examples with fixes
- WCAG compliance verification
- Browser/device test evidence
- Clear severity categorization
- Design system compliance checked

**Avoid:**
- Vague feedback ("looks off")
- Missing specific fixes
- Skipping accessibility review
- No cross-browser testing
- Ignoring design system standards
- Subjective opinions without rationale
