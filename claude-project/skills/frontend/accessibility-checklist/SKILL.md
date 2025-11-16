---
name: accessibility-checklist
description: WCAG AA accessibility checklist and verification protocols for Somali dialect classifier dashboard. Covers keyboard navigation, screen readers, color contrast, ARIA labels, and accessibility testing procedures.
allowed-tools: Read
---

# Accessibility Checklist (WCAG AA)

## Keyboard Navigation

### ✅ Requirements

**Tab Order:**
- [ ] All interactive elements reachable via Tab
- [ ] Logical tab order (left-to-right, top-to-bottom)
- [ ] Skip links provided for repetitive navigation
- [ ] No keyboard traps

**Interactive Elements:**
- [ ] Buttons activate with Enter/Space
- [ ] Links activate with Enter
- [ ] Form inputs accessible via Tab
- [ ] Dropdowns navigable with Arrow keys
- [ ] Modals closable with Escape

**Testing:**
```
1. Unplug mouse
2. Navigate entire dashboard using only keyboard
3. Verify all features accessible
4. Check tab order is logical
```

---

## Focus Indicators

### ✅ Requirements

**Visibility:**
- [ ] Focus indicators visible on ALL interactive elements
- [ ] Minimum 2px outline or 3px box-shadow
- [ ] Sufficient color contrast (3:1 minimum)
- [ ] Not removed with `outline: none` unless replaced

**Implementation:**
```css
/* Good focus states */
.btn:focus-visible {
  outline: 3px solid var(--tableau-blue);
  outline-offset: 3px;
}

.data-toggle__option:focus-visible {
  outline: 2px solid var(--data-blue-primary);
  outline-offset: 2px;
  z-index: 1;
}

/* Chart canvas focus */
canvas:focus-visible {
  outline: 2px solid var(--data-cyan-primary);
  outline-offset: 2px;
  border-radius: 4px;
}
```

---

## Color Contrast

### ✅ Requirements (WCAG AA)

**Normal Text (< 18px):**
- [ ] Minimum 4.5:1 contrast ratio

**Large Text (≥ 18px or 14px bold):**
- [ ] Minimum 3:1 contrast ratio

**UI Components:**
- [ ] Buttons: 3:1 minimum
- [ ] Form inputs: 3:1 border contrast
- [ ] Icons: 3:1 against background

**Verified Combinations:**
| Foreground | Background | Ratio | Status |
|------------|------------|-------|--------|
| White | Tableau Blue (#0176D3) | 4.83:1 | ✅ AA |
| White | Tableau Navy (#032D60) | 13.55:1 | ✅ AAA |
| Text (#333) | White | 12.63:1 | ✅ AAA |
| Data Cyan (#33BBEE) | White | 2.4:1 | ❌ (use dark text) |

**Testing Tool:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

---

## Semantic HTML

### ✅ Requirements

**Landmarks:**
- [ ] `<header>` for site/page header
- [ ] `<nav>` for navigation
- [ ] `<main>` for main content
- [ ] `<aside>` for sidebars
- [ ] `<footer>` for footer

**Headings:**
- [ ] Logical heading hierarchy (H1 → H2 → H3, no skipping)
- [ ] One H1 per page
- [ ] Headings describe content

**Lists:**
- [ ] `<ul>`/`<ol>` for lists
- [ ] `<dl>` for definition lists

**Buttons vs Links:**
- [ ] `<button>` for actions (submit, toggle, delete)
- [ ] `<a>` for navigation (go to another page)

**Example:**
```html
<!-- Good semantic structure -->
<header>
  <h1>Somali Dialect Classifier Dashboard</h1>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/overview">Overview</a></li>
      <li><a href="/data">Data Sources</a></li>
    </ul>
  </nav>
</header>

<main>
  <section aria-labelledby="metrics-heading">
    <h2 id="metrics-heading">Pipeline Metrics</h2>
    <!-- Content -->
  </section>
</main>
```

---

## ARIA Labels

### ✅ Requirements

**Icon Buttons:**
```html
<button aria-label="Delete dataset">
  <svg><!-- trash icon --></svg>
</button>
```

**Status Indicators:**
```html
<span
  className="status-icon"
  aria-label="Pipeline status: healthy"
  role="img"
>
  ✓
</span>
```

**Charts (Canvas):**
```html
<canvas
  aria-label="Bar chart showing dialect distribution: Northern 60%, Southern 25%, Central 15%"
  role="img"
></canvas>
```

**Form Inputs:**
```html
<label for="dataset-name">Dataset Name</label>
<input
  id="dataset-name"
  type="text"
  aria-describedby="name-help"
/>
<p id="name-help" className="help-text">
  Choose a descriptive name for your dataset
</p>
```

---

## Alt Text for Images

### ✅ Requirements

**Informative Images:**
- [ ] Descriptive alt text explaining content
- [ ] Context-specific descriptions

**Decorative Images:**
- [ ] `alt=""` (empty alt attribute)

**Examples:**
```html
<!-- Informative -->
<img
  src="confusion-matrix.png"
  alt="Confusion matrix showing Northern dialect correctly classified 94% of the time, Southern 82%, Central 79%"
/>

<!-- Decorative -->
<img src="decorative-pattern.svg" alt="" />
```

**Charts as Images:**
- Provide detailed description in alt text OR
- Provide data table alternative

---

## Form Accessibility

### ✅ Requirements

**Labels:**
- [ ] All inputs have associated `<label>`
- [ ] Labels visible (not placeholder-only)
- [ ] Labels describe purpose clearly

**Error Messages:**
- [ ] Error messages associated via `aria-describedby`
- [ ] Errors announced to screen readers
- [ ] Error styling includes text/icons (not color-only)

**Example:**
```html
<div className="form-field">
  <label for="source-url">Source URL</label>
  <input
    id="source-url"
    type="url"
    aria-describedby="url-error"
    aria-invalid="true"
  />
  <p id="url-error" className="error-message" role="alert">
    Invalid URL format. Use: https://example.com
  </p>
</div>
```

---

## Screen Reader Testing

### ✅ Requirements

**Announcement Priorities:**
- [ ] Page title describes current page
- [ ] Headings announce hierarchy
- [ ] Landmark regions labeled
- [ ] Dynamic content changes announced

**Live Regions:**
```html
<!-- Status updates -->
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>

<!-- Urgent alerts -->
<div role="alert" aria-live="assertive">
  {errorMessage}
</div>
```

**Testing Tools:**
- macOS: VoiceOver (Cmd+F5)
- Windows: NVDA (free) or JAWS
- Chrome extension: ChromeVox

---

## Modal Accessibility

### ✅ Requirements

**Focus Management:**
- [ ] Focus moves to modal when opened
- [ ] Focus trapped within modal
- [ ] Focus returns to trigger element when closed
- [ ] Closable with Escape key

**ARIA Attributes:**
```html
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <h2 id="dialog-title">Delete Dataset?</h2>
  <p id="dialog-desc">
    This action cannot be undone.
  </p>
  <button onClick={confirmDelete}>Delete</button>
  <button onClick={closeModal}>Cancel</button>
</div>
```

---

## Testing Checklist

### Manual Tests

**Keyboard:**
- [ ] Tab through entire dashboard
- [ ] Activate all interactive elements
- [ ] Verify no keyboard traps
- [ ] Check tab order is logical

**Screen Reader:**
- [ ] Navigate with headings
- [ ] Read all content
- [ ] Interact with forms
- [ ] Verify dynamic updates announced

**Visual:**
- [ ] Zoom to 200% (text remains readable)
- [ ] Check focus indicators visible
- [ ] Verify color contrast
- [ ] Test without color (grayscale mode)

### Automated Tools

**Browser Extensions:**
- axe DevTools (Chrome/Firefox)
- WAVE (Web Accessibility Evaluation Tool)
- Lighthouse (Chrome DevTools)

**Command:**
```bash
# Run Lighthouse accessibility audit
npx lighthouse https://dashboard-url --only-categories=accessibility --view
```

**Target Score:** Lighthouse Accessibility Score ≥ 95/100

---

## Common Issues & Fixes

### Issue: Missing Alt Text
**Fix:** Add descriptive alt attributes to all images

### Issue: Poor Color Contrast
**Fix:** Use design-system colors (verified contrast ratios)

### Issue: No Focus Indicators
**Fix:** Add `:focus-visible` styles to all interactive elements

### Issue: Inaccessible Charts
**Fix:** Add `aria-label` to canvas, provide data table alternative

### Issue: Form Errors Not Announced
**Fix:** Use `role="alert"` and `aria-describedby`

---

## When This Skill Activates

This skill auto-invokes when you mention:
- Accessibility, a11y, WCAG, ARIA
- Screen readers, VoiceOver, NVDA
- Keyboard navigation, tab order
- Focus indicators, focus states
- Color contrast, contrast ratios
- Alt text, image descriptions
- Semantic HTML, landmarks
- Form accessibility, labels
- Modal accessibility, dialogs

---

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Project:** Somali Dialect Classifier Dashboard
