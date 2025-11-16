---
name: design-system
description: Dual-palette design system for data/ML dashboards. Tableau-inspired brand colors for UI elements (buttons, navigation, cards, forms), colorblind-friendly data colors for visualizations (charts, treemaps, graphs). Auto-invokes when working on styling, design, CSS, visual components, frontend implementation, or any UI/visualization work. Includes component patterns, spacing, shadows, typography, accessibility guidelines.
allowed-tools: Read, Grep, Glob
---

# Design System Skill

## Quick Decision Rule

**Is this a UI element or a data visualization?**
- **UI Element** → Use Brand Colors (#0176D3, #032D60)
- **Data Visualization** → Use Data Colors (#33BBEE, #0077BB, sequence)

---

## Brand Colors (UI Elements)

Use for buttons, navigation, hero, cards, forms, badges, general UI.

```css
/* Primary Brand Colors */
--tableau-blue: #0176D3           /* Primary CTA buttons, links */
--tableau-navy: #032D60           /* Headings, navigation */
--tableau-navy-link: #0B5CAB      /* Link hover state */
--tableau-bg-light-blue: #EAF5FE  /* Light backgrounds */
--tableau-green: #00A651          /* Success states */

/* Text Hierarchy */
--tableau-text-primary: #080707   /* Headings */
--tableau-text-secondary: #333333 /* Body text */
--tableau-text-light: #555555     /* Muted text */

/* Borders */
--tableau-gray-border: #EBEBEB    /* Subtle borders */
--tableau-gray-divider: #D1D1D1   /* Strong dividers */
```

---

## Data Visualization Colors (Charts Only)

Use ONLY for charts, graphs, treemaps, data cards, analyst mode visualizations.

```css
/* Primary Data Colors (Colorblind-Friendly) */
--data-cyan-primary: #33BBEE      /* Series 1 (most important) */
--data-blue-primary: #0077BB      /* Series 2 */
--data-cyan-lighter: #66CCEE      /* Series 3 */
--data-blue-lighter: #4477AA      /* Series 4 */
--data-teal: #44AA99              /* Series 5 */
--data-cyan-light: #88CCEE        /* Series 6 */
--data-teal-dark: #009988         /* Series 7 */

/* Semantic Data Colors */
--data-grey: #BBBBBB              /* Baseline/reference */
--data-red: #EE6677               /* Errors/outliers */
--data-sand: #DDCC77              /* Alternative neutral */
```

**Data Color Sequence (Priority Order):**
```javascript
const dataColorSequence = [
  '#33BBEE', // 1. Primary Cyan
  '#0077BB', // 2. Primary Blue
  '#66CCEE', // 3. Lighter Cyan
  '#4477AA', // 4. Lighter Blue
  '#44AA99', // 5. Teal
  '#88CCEE', // 6. Light Cyan
  '#009988', // 7. Darker Teal
  '#BBBBBB', // 8. Grey (baseline)
  '#EE6677', // 9. Red (errors)
  '#DDCC77'  // 10. Sand (rarely)
];
```

---

## Typography

```css
/* Font Families */
--font-sans: 'Inter', sans-serif;              /* Body text */
--font-display: 'Space Grotesk', sans-serif;   /* Headings */
--font-mono: 'Fira Code', monospace;           /* Code, data */

/* Font Sizes */
--text-xs: 0.75rem;      /* 12px - captions */
--text-sm: 0.875rem;     /* 14px - small text */
--text-base: 1rem;       /* 16px - body */
--text-lg: 1.125rem;     /* 18px - emphasis */
--text-xl: 1.25rem;      /* 20px - subheadings */
--text-2xl: 1.5rem;      /* 24px - headings */
--text-3xl: 1.875rem;    /* 30px - page headings */
--text-4xl: 2.25rem;     /* 36px - hero */
```

---

## Spacing

```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

---

## Shadows (Tableau-Inspired Dual-Layer)

```css
/* Subtle elevation for cards */
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);

/* Medium elevation for modals */
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);

/* Large elevation for popovers */
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
```

---

## Component Patterns

### Button (Brand Color)

```html
<button class="btn btn--primary">Get Started</button>
```

```css
.btn--primary {
  background-color: var(--tableau-blue);
  color: white;
  padding: 14px 32px;
  border-radius: 6px;
  font-weight: 600;
  transition: all 250ms;
}

.btn--primary:hover {
  background-color: #0158A5;
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn--primary:focus-visible {
  outline: 3px solid rgba(1, 118, 211, 0.5);
  outline-offset: 3px;
}
```

### Card (Brand Color)

```html
<div class="card">
  <div class="card__header">Title</div>
  <div class="card__body">Content</div>
</div>
```

```css
.card {
  background: white;
  border: 1px solid var(--tableau-gray-border);
  border-radius: 16px;
  padding: var(--space-8);
  box-shadow: var(--shadow-sm);
}

.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  transition: all 250ms;
}
```

### Data Card (Data Color - Analyst Mode)

```html
<div class="data-card data-card--positive">
  <div class="data-card__label">Total Records</div>
  <div class="data-card__value">1,234,567</div>
  <div class="data-card__trend">+12.5%</div>
</div>
```

```css
.data-card {
  background: white;
  border-radius: 16px;
  padding: var(--space-8);
  box-shadow: var(--shadow-md);
  border-top: 4px solid var(--data-cyan-primary); /* Data color */
}

.data-card__value {
  color: var(--data-blue-primary); /* Data color */
  font-size: var(--text-3xl);
  font-weight: 700;
  font-family: var(--font-display);
}

.data-card--positive {
  border-top-color: var(--data-cyan-primary);
}

.data-card--positive .data-card__value {
  color: var(--data-cyan-primary);
}
```

### Data Toggle (Data Color - Analyst Mode)

```html
<div class="data-toggle">
  <button class="data-toggle__option data-toggle__option--active">Daily</button>
  <button class="data-toggle__option">Weekly</button>
  <button class="data-toggle__option">Monthly</button>
</div>
```

```css
.data-toggle__option--active {
  background: var(--data-cyan-primary); /* Data color */
  color: white;
  border-radius: 9999px;
  padding: 0.5rem 1.25rem;
}
```

---

## Chart.js Configuration

### Multi-Series Chart (Data Colors)

```javascript
const barChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Northern', 'Southern', 'Central'],
    datasets: [
      {
        label: 'Training',
        data: [1200, 980, 850],
        backgroundColor: '#33BBEE' // Data cyan primary
      },
      {
        label: 'Validation',
        data: [300, 245, 210],
        backgroundColor: '#0077BB' // Data blue primary
      },
      {
        label: 'Test',
        data: [150, 120, 105],
        backgroundColor: '#66CCEE' // Data cyan lighter
      }
    ]
  },
  options: {
    plugins: {
      legend: {
        labels: {
          font: { family: 'Inter', size: 12 },
          color: '#333333' // Brand text color for UI
        }
      }
    }
  }
});
```

### Data Color Utilities

```javascript
// Get color by series index
function getDataColor(index) {
  const colors = ['#33BBEE', '#0077BB', '#66CCEE', '#4477AA', '#44AA99'];
  return colors[index % colors.length];
}

// Convert to rgba for transparency
function hexToRgba(hex, alpha) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

// Example: semi-transparent area chart
backgroundColor: hexToRgba('#33BBEE', 0.3)
```

---

## Accessibility

### Focus States

**UI Components (Brand Colors):**
```css
.btn:focus-visible {
  outline: 3px solid var(--tableau-blue);
  outline-offset: 3px;
}
```

**Data Components (Data Colors):**
```css
.data-toggle__option:focus-visible {
  outline: 2px solid var(--data-blue-primary);
  outline-offset: 2px;
}
```

### Color Contrast (WCAG AA Minimum)

| Foreground | Background | Ratio | Status |
|------------|------------|-------|--------|
| White | Tableau Blue (#0176D3) | 4.83:1 | ✅ AA |
| White | Tableau Navy (#032D60) | 13.55:1 | ✅ AAA |
| Text (#333) | White | 12.63:1 | ✅ AAA |

---

## BEM Naming Convention

```css
.block__element--modifier

/* Examples */
.btn { }                      /* Block */
.btn__icon { }                /* Element */
.btn--primary { }             /* Modifier */

.data-card { }                /* Block */
.data-card__label { }         /* Element */
.data-card--positive { }      /* Modifier */
```

---

## Responsive Breakpoints

```css
--breakpoint-sm: 640px;   /* Phones */
--breakpoint-md: 768px;   /* Tablets */
--breakpoint-lg: 1024px;  /* Desktops */
--breakpoint-xl: 1280px;  /* Large desktops */
```

---

## Usage Guidelines

### ✅ DO

- Use brand colors for all UI elements (buttons, nav, forms)
- Use data colors for all charts and visualizations
- Use CSS custom properties (variables) for colors
- Follow BEM naming convention
- Maintain WCAG AA minimum contrast ratios
- Apply dual-layer shadows for depth
- Use generous spacing (Tableau-inspired)

### ❌ DON'T

- Mix brand colors and data colors in same context
- Use hardcoded color values (always use variables)
- Deviate from established color sequences
- Skip the style guide review
- Use colors not in the documented palette

---

## Code Comment Examples

```css
/* Brand color per design-system skill: Brand Colors section */
.btn-primary {
  background-color: var(--tableau-blue);
}
```

```javascript
// Data color sequence per design-system skill: Data Viz section
const colors = ['#33BBEE', '#0077BB', '#66CCEE'];
```

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Styling, CSS, SCSS, styles
- Design system, component design
- Colors, brand colors, data colors
- UI elements, buttons, cards, forms
- Charts, graphs, visualizations, treemaps
- Typography, fonts, spacing
- Shadows, borders, radius
- Accessibility, WCAG, contrast
- Frontend implementation

---

## Complete Reference

For complete design system documentation with all component examples, see:
`.claude/DESIGN_SYSTEM.md`

---

**Version:** 2.0.0
**Last Updated:** 2025-11-06
