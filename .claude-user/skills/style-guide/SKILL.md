---
name: style-guide
description: Visual design philosophy, brand principles, and aesthetic guidelines for data/ML dashboards. Covers Tableau-inspired professionalism, data-first clarity, generous spacing, dual-layer shadows, and design influences. Auto-invokes when discussing visual design, brand identity, design principles, aesthetic decisions, or design philosophy. Complements design-system skill with strategic guidance.
allowed-tools: Read, Grep
---

# Style Guide Skill

## Design Philosophy

Data/ML dashboards embody **analytical clarity** and **data transparency** through a sophisticated dual-palette system.

### Core Principles

1. **Data-First Clarity**
   - UI elements support, never compete with, data visualizations
   - Generous white space allows data to breathe
   - Clear hierarchy guides user attention to insights

2. **Dual-Palette Separation**
   - Brand colors (Tableau blues) for all UI elements
   - Data colors (colorblind-friendly) for visualizations only
   - Never mix the two systems in the same context

3. **Tableau-Inspired Professionalism**
   - Clean, uncluttered interfaces
   - Generous spacing (minimum 16px between major elements)
   - Dual-layer shadows for subtle depth
   - Professional corporate aesthetic

4. **Universal Accessibility**
   - WCAG AA minimum for all color combinations
   - Colorblind-friendly data visualizations
   - Keyboard navigable
   - Screen reader friendly

5. **Consistent Patterns**
   - Reusable components with predictable behavior
   - BEM naming convention for CSS
   - Standardized interactions across the platform

---

## Design Influences

### Primary: Tableau (60%)
- Professional data visualization aesthetic
- Generous white space and structured hierarchy
- Dual-layer shadows for subtle depth
- Brand blues for UI, data-optimized colors for charts
- Clean, corporate presentation

### Secondary: Stripe (20%)
- Modern, refined UI components
- Subtle micro-interactions
- Developer-focused clarity
- Polished form design

### Tertiary: Airbnb + Linear (20%)
- Card-based layouts with hover states
- Smooth transitions (250ms default)
- Task-oriented interfaces
- Friendly, approachable interactions

---

## Visual Hierarchy

### Emphasis Levels

**Primary Emphasis (Most Important)**
- Hero headings (48px, Space Grotesk, Bold)
- Primary CTA buttons (Tableau Blue background)
- Key data metrics (30px, Space Grotesk, Bold)

**Secondary Emphasis**
- Section headings (24px, Space Grotesk, Semibold)
- Secondary buttons (Outline style)
- Supporting data metrics

**Tertiary Emphasis**
- Body text (16px, Inter, Regular)
- Captions (12-14px, Inter, Regular)
- Helper text

---

## Spacing Philosophy

### Tableau-Inspired Generous Spacing

- **Minimum padding inside cards:** 32px (2rem)
- **Minimum gap between cards:** 24px (1.5rem)
- **Section spacing:** 48-64px (3-4rem)
- **Hero section padding:** 80px+ (5rem+)

### Breathing Room

- Never cram elements together
- Allow white space to create calm, professional feel
- Use padding generously (double what feels "enough")
- Increase spacing proportionally on larger screens

---

## Shadow System

### Tableau-Inspired Dual-Layer Shadows

**Philosophy:** Subtle elevation, never dramatic

```css
/* Subtle (Cards at rest) */
box-shadow:
  0 1px 2px rgba(0, 0, 0, 0.06),
  0 1px 3px rgba(0, 0, 0, 0.1);

/* Medium (Cards on hover, modals) */
box-shadow:
  0 4px 6px rgba(0, 0, 0, 0.07),
  0 2px 4px rgba(0, 0, 0, 0.06);

/* Large (Popovers, dropdowns) */
box-shadow:
  0 10px 15px rgba(0, 0, 0, 0.1),
  0 4px 6px rgba(0, 0, 0, 0.05);
```

**Rules:**
- Always use dual-layer (two box-shadow values)
- Keep opacity low (0.05-0.1 range)
- Avoid harsh, heavy shadows
- Increase shadow on hover for interactive elements

---

## Motion & Transitions

### Timing

```css
--transition-fast: 150ms;   /* Hover states, minor UI changes */
--transition-base: 250ms;   /* Standard transitions */
--transition-slow: 350ms;   /* Page transitions, major changes */
```

### Easing

```css
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);  /* Default */
```

### Interactive Feedback

**Button Hover:**
- Lift slightly (translateY(-2px))
- Deepen shadow
- Transition: 250ms

**Card Hover:**
- Lift (translateY(-2px))
- Increase shadow from subtle to medium
- Transition: 250ms

**Link Hover:**
- Color shift (Navy → Navy Link color)
- Underline fade-in
- Transition: 150ms (fast)

---

## Typography Philosophy

### Font Choices

**Space Grotesk (Headings)**
- Modern, geometric, slightly quirky
- Professional but approachable
- Bold weights for emphasis

**Inter (Body)**
- Highly legible at all sizes
- Clean, neutral, professional
- Default for all body text

**Fira Code (Code/Data)**
- Monospace for technical content
- Good readability for numbers/data
- Use sparingly

### Type Scale

- **Hero:** 48px (3rem)
- **H1:** 36px (2.25rem)
- **H2:** 30px (1.875rem)
- **H3:** 24px (1.5rem)
- **Body:** 16px (1rem)
- **Small:** 14px (0.875rem)
- **Captions:** 12px (0.75rem)

### Line Height

- **Headings:** 1.25 (tight)
- **Body text:** 1.5 (normal)
- **Long-form content:** 1.625 (relaxed)

---

## Interaction Patterns

### Hover States (UI Elements)

**Buttons:**
- Background color deepens
- Lift 2px upward
- Shadow increases
- Cursor: pointer

**Links:**
- Color shifts to link color
- Underline appears
- Cursor: pointer

**Cards:**
- Lift 2px upward
- Shadow increases
- Border remains subtle
- Cursor: default (unless clickable)

### Focus States

**Keyboard Focus (All Interactive Elements):**
- 3px outline in brand blue
- 3px outline offset
- High visibility for accessibility

**Data Visualization Focus:**
- 2px outline in data blue primary
- 2px outline offset

### Active States

**Buttons:**
- Pressed down (translateY(-1px))
- Shadow decreases
- Background darkens further

---

## Color Usage Guidelines

### ✅ DO

**For UI Elements:**
- Primary buttons → Tableau Blue (#0176D3)
- Headings → Tableau Navy (#032D60)
- Links → Tableau Navy Link (#0B5CAB)
- Success states → Tableau Green (#00A651)
- Backgrounds → Tableau BG Light Blue or Off-White

**For Data Visualizations:**
- Chart series → Data color sequence (#33BBEE, #0077BB, #66CCEE...)
- Data cards → Data cyan/blue for accents
- Toggle/capsule active states → Data cyan primary
- Treemaps, heatmaps → Data color palette

### ❌ DON'T

- Use brand blue in charts/graphs
- Use data cyan/blue for buttons or UI elements
- Mix brand and data colors in same context
- Use hardcoded colors (always use CSS variables)
- Deviate from approved color sequences

---

## Accessibility Principles

### Color Contrast

- **Minimum:** WCAG AA (4.5:1 for normal text, 3:1 for large text)
- **Target:** WCAG AAA when possible
- **All text on backgrounds must meet minimum contrast**
- **Test with colorblind simulators**

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Visible focus indicators required
- Logical tab order (left-to-right, top-to-bottom)
- Skip links for complex navigation

### Screen Readers

- Semantic HTML (headings, landmarks, lists)
- ARIA labels for icon buttons
- Alt text for informative images
- Form labels explicitly associated

---

## Responsive Design Principles

### Mobile-First

- Design for smallest screen first
- Progressively enhance for larger screens
- Touch targets minimum 44x44px
- Generous spacing on mobile (prevent mis-taps)

### Breakpoints

- **Small:** 640px (phones)
- **Medium:** 768px (tablets)
- **Large:** 1024px (desktops)
- **XL:** 1280px (large desktops)

### Layout Adaptation

- Stack cards vertically on mobile
- Show 2 columns on tablet
- Show 3-4 columns on desktop
- Hide/reveal navigation appropriately

---

## When to Use This Skill

This skill activates when you mention:
- Design philosophy, design principles
- Visual design, aesthetic decisions
- Brand identity, brand guidelines
- Spacing, shadows, elevation
- Motion, transitions, animations
- Typography philosophy, font choices
- Interaction patterns, hover states
- Design influences (Tableau, Stripe, Airbnb)

---

## Related Skills

- **design-system:** Technical implementation (colors, components, code)
- **ux-writing:** Content, messaging, tone, voice
- **accessibility-checklist:** WCAG compliance verification (project-specific)

---

## Complete Reference

For detailed color tokens, component code, and implementation specifics, see:
- `.claude/STYLE_GUIDE.md` (complete reference)
- `design-system` skill (technical implementation)

---

**Version:** 2.0.0
**Last Updated:** 2025-11-06
