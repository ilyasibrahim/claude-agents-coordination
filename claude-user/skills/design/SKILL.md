---
name: design
description: Unified design system for data/ML dashboards. Quick reference for brand vs data color decisions, component patterns, typography, spacing. Auto-invokes on styling, CSS, design, colors, UI, visualization keywords. Tiered loading - core always, philosophy/implementation on-demand.
allowed-tools: Read, Grep, Glob
---

# Design System (Core)

## Quick Decision

**UI element or data visualization?**
- **UI Element** → Brand Colors (#0176D3, #032D60)
- **Data Visualization** → Data Colors (#33BBEE, #0077BB, sequence)

**Never mix brand and data colors in same context.**

---

## Brand Colors (UI Only)

```css
--tableau-blue: #0176D3;       /* Primary CTA */
--tableau-navy: #032D60;       /* Headings, nav */
--tableau-green: #00A651;      /* Success */
--tableau-bg-light: #EAF5FE;   /* Backgrounds */
--tableau-text: #333333;       /* Body text */
--tableau-border: #EBEBEB;     /* Borders */
```

## Data Colors (Charts Only)

```css
--data-1: #33BBEE;  /* Primary cyan */
--data-2: #0077BB;  /* Primary blue */
--data-3: #66CCEE;  /* Light cyan */
--data-4: #4477AA;  /* Light blue */
--data-5: #44AA99;  /* Teal */
--data-error: #EE6677;  /* Red (errors) */
--data-neutral: #BBBBBB; /* Grey (baseline) */
```

**Sequence:** `['#33BBEE', '#0077BB', '#66CCEE', '#4477AA', '#44AA99']`

---

## Typography

```css
--font-heading: 'Space Grotesk', sans-serif;
--font-body: 'Inter', sans-serif;
--font-code: 'Fira Code', monospace;

--text-hero: 2.25rem;   /* 36px */
--text-h1: 1.875rem;    /* 30px */
--text-h2: 1.5rem;      /* 24px */
--text-body: 1rem;      /* 16px */
--text-small: 0.875rem; /* 14px */
```

## Spacing

```css
--space-2: 0.5rem;   /* 8px */
--space-4: 1rem;     /* 16px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px - card padding */
--space-12: 3rem;    /* 48px - section gap */
```

## Shadows (Dual-Layer)

```css
--shadow-sm: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.1);
--shadow-md: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.1);
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05);
```

---

## Component Patterns

### Button (Brand)
```css
.btn-primary {
  background: var(--tableau-blue);
  color: white;
  padding: 14px 32px;
  border-radius: 6px;
}
.btn-primary:hover { transform: translateY(-2px); }
```

### Card (Brand)
```css
.card {
  background: white;
  border: 1px solid var(--tableau-border);
  border-radius: 16px;
  padding: var(--space-8);
  box-shadow: var(--shadow-sm);
}
```

### Data Card (Data Colors)
```css
.data-card {
  border-top: 4px solid var(--data-1);
}
.data-card__value {
  color: var(--data-2);
  font-size: var(--text-h1);
  font-family: var(--font-heading);
}
```

---

## Chart.js Setup

```javascript
const chartColors = ['#33BBEE', '#0077BB', '#66CCEE', '#4477AA', '#44AA99'];

new Chart(ctx, {
  data: {
    datasets: [
      { backgroundColor: chartColors[0] },
      { backgroundColor: chartColors[1] }
    ]
  },
  options: {
    plugins: {
      legend: { labels: { color: '#333333' } } // Brand for UI
    }
  }
});
```

---

## Accessibility

- **Contrast:** 4.5:1 minimum (WCAG AA)
- **Focus:** 3px outline, brand blue
- **Touch:** 44x44px minimum targets

---

## Extended Reference

For philosophy and full implementation details:
- **Philosophy:** `skills/design/philosophy.md`
- **Full implementation:** `skills/design/implementation.md`

---

**Version:** 3.0.0
