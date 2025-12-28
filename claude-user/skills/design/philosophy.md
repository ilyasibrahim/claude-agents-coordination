# Design Philosophy

Load this file for design principles, influences, and strategic guidance.

---

## Core Principles

### 1. Data-First Clarity
UI supports data, never competes with it. Generous white space lets data breathe.

### 2. Dual-Palette Separation
Brand colors for UI. Data colors for visualizations. Never mix.

### 3. Tableau-Inspired Professionalism
Clean, uncluttered. Generous spacing. Subtle shadows. Corporate aesthetic.

### 4. Universal Accessibility
WCAG AA minimum. Colorblind-friendly data viz. Keyboard navigable.

### 5. Consistent Patterns
Reusable components. BEM naming. Standardized interactions.

---

## Design Influences

| Influence | Weight | What We Take |
|-----------|--------|--------------|
| Tableau | 60% | Data viz aesthetic, dual shadows, brand blues |
| Stripe | 20% | Modern UI, micro-interactions, form polish |
| Airbnb/Linear | 20% | Card layouts, smooth transitions, task focus |

---

## Visual Hierarchy

### Primary Emphasis
- Hero headings: 48px, Space Grotesk, Bold
- Primary CTAs: Tableau Blue background
- Key metrics: 30px, Space Grotesk

### Secondary
- Section headings: 24px, semibold
- Secondary buttons: Outline style

### Tertiary
- Body: 16px, Inter
- Captions: 12-14px
- Helper text: muted color

---

## Spacing Philosophy

**Tableau-inspired generous spacing:**
- Card padding: minimum 32px
- Card gap: minimum 24px
- Section spacing: 48-64px
- Hero padding: 80px+

**Rule:** When in doubt, double the spacing.

---

## Motion

```css
--transition-fast: 150ms;  /* Hovers */
--transition-base: 250ms;  /* Standard */
--transition-slow: 350ms;  /* Page changes */
--ease: cubic-bezier(0.4, 0, 0.2, 1);
```

### Interactive Feedback
- **Button hover:** lift 2px, deepen shadow
- **Card hover:** lift 2px, shadow sm→md
- **Link hover:** color shift, underline fade-in

---

## Color Usage Rules

### DO
- Brand colors for buttons, nav, forms, cards
- Data colors for charts, graphs, treemaps
- CSS variables (never hardcode)
- Test contrast ratios

### DON'T
- Brand blue in charts
- Data cyan for buttons
- Mix palettes in same context
- Skip accessibility checks
