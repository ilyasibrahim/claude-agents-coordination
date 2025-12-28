# Design Implementation Details

Load this file for full CSS variables, component code, and Chart.js configuration.

---

## Complete Color Tokens

### Brand Colors (UI)

```css
:root {
  /* Primary */
  --tableau-blue: #0176D3;
  --tableau-navy: #032D60;
  --tableau-navy-link: #0B5CAB;
  --tableau-bg-light-blue: #EAF5FE;
  --tableau-green: #00A651;

  /* Text */
  --tableau-text-primary: #080707;
  --tableau-text-secondary: #333333;
  --tableau-text-light: #555555;

  /* Borders */
  --tableau-gray-border: #EBEBEB;
  --tableau-gray-divider: #D1D1D1;
}
```

### Data Colors (Visualizations)

```css
:root {
  /* Primary sequence */
  --data-cyan-primary: #33BBEE;
  --data-blue-primary: #0077BB;
  --data-cyan-lighter: #66CCEE;
  --data-blue-lighter: #4477AA;
  --data-teal: #44AA99;
  --data-cyan-light: #88CCEE;
  --data-teal-dark: #009988;

  /* Semantic */
  --data-grey: #BBBBBB;
  --data-red: #EE6677;
  --data-sand: #DDCC77;
}
```

---

## Full Component Patterns

### Primary Button

```html
<button class="btn btn--primary">Action</button>
```

```css
.btn--primary {
  background-color: var(--tableau-blue);
  color: white;
  padding: 14px 32px;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  font-family: var(--font-body);
  cursor: pointer;
  transition: all 250ms var(--ease);
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

.btn--primary:active {
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}
```

### Card

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
  transition: all 250ms var(--ease);
}

.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.card__header {
  font-family: var(--font-heading);
  font-size: var(--text-h3);
  color: var(--tableau-navy);
  margin-bottom: var(--space-4);
}
```

### Data Card

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
  border-top: 4px solid var(--data-cyan-primary);
}

.data-card__label {
  font-size: var(--text-small);
  color: var(--tableau-text-light);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.data-card__value {
  font-size: var(--text-hero);
  font-weight: 700;
  font-family: var(--font-heading);
  color: var(--data-blue-primary);
  margin: var(--space-2) 0;
}

.data-card--positive .data-card__trend {
  color: var(--tableau-green);
}
```

### Data Toggle

```css
.data-toggle {
  display: inline-flex;
  background: var(--tableau-bg-light-blue);
  border-radius: 9999px;
  padding: 4px;
}

.data-toggle__option {
  padding: 0.5rem 1.25rem;
  border: none;
  background: transparent;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 150ms;
}

.data-toggle__option--active {
  background: var(--data-cyan-primary);
  color: white;
}
```

---

## Chart.js Configuration

### Multi-Series Bar Chart

```javascript
const dataColors = [
  '#33BBEE', '#0077BB', '#66CCEE',
  '#4477AA', '#44AA99', '#88CCEE'
];

const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Category A', 'Category B', 'Category C'],
    datasets: [
      {
        label: 'Series 1',
        data: [1200, 980, 850],
        backgroundColor: dataColors[0]
      },
      {
        label: 'Series 2',
        data: [300, 245, 210],
        backgroundColor: dataColors[1]
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          font: { family: 'Inter', size: 12 },
          color: '#333333'
        }
      }
    },
    scales: {
      y: {
        grid: { color: '#EBEBEB' },
        ticks: { color: '#555555' }
      },
      x: {
        grid: { display: false },
        ticks: { color: '#555555' }
      }
    }
  }
});
```

### Color Utilities

```javascript
function getDataColor(index) {
  const colors = ['#33BBEE', '#0077BB', '#66CCEE', '#4477AA', '#44AA99'];
  return colors[index % colors.length];
}

function hexToRgba(hex, alpha) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

// Semi-transparent for area charts
const areaFill = hexToRgba('#33BBEE', 0.3);
```

---

## Accessibility Details

### Contrast Ratios

| Foreground | Background | Ratio | Status |
|------------|------------|-------|--------|
| White | #0176D3 | 4.83:1 | AA |
| White | #032D60 | 13.55:1 | AAA |
| #333333 | White | 12.63:1 | AAA |
| #555555 | White | 7.46:1 | AAA |

### Focus States

```css
/* UI elements */
.btn:focus-visible,
.card:focus-visible,
input:focus-visible {
  outline: 3px solid var(--tableau-blue);
  outline-offset: 3px;
}

/* Data elements */
.data-toggle__option:focus-visible,
.chart-legend-item:focus-visible {
  outline: 2px solid var(--data-blue-primary);
  outline-offset: 2px;
}
```

---

## Responsive Breakpoints

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}

/* Mobile-first example */
.card-grid {
  display: grid;
  gap: var(--space-6);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .card-grid { grid-template-columns: repeat(3, 1fr); }
}
```

---

## BEM Naming

```css
.block { }
.block__element { }
.block--modifier { }

/* Examples */
.btn { }
.btn__icon { }
.btn--primary { }
.btn--secondary { }

.data-card { }
.data-card__label { }
.data-card__value { }
.data-card--positive { }
.data-card--negative { }
```
