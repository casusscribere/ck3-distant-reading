# 03 · Components

Reusable UI pieces translated from CK3's interface: gilded buttons, framed
parchment panels, character/realm cards, heraldic shields, tooltips, dividers and
tables. All depend on the variables in
[`01-color-and-texture.md`](01-color-and-texture.md). Everything here is in
[`theme.css`](theme.css) too.

---

## 1. Buttons

CK3 buttons read like cast-metal plates: a beveled gold/bronze face, dark engraved
label, and a satisfying press.

```css
.ck3-btn {
  font-family: var(--ck3-font-head);
  font-size: .95rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--ck3-ink);
  padding: .6em 1.4em;
  border: 1px solid var(--ck3-gold-shadow);
  border-radius: 3px;
  background: var(--ck3-grad-gold);
  box-shadow:
    inset 0 1px 0 var(--ck3-gold-hi),
    inset 0 -2px 3px rgba(0,0,0,.35),
    0 2px 3px rgba(0,0,0,.5);
  cursor: pointer;
  transition: filter .12s, transform .05s;
}
.ck3-btn:hover { filter: brightness(1.08); }
.ck3-btn:active { transform: translateY(1px); filter: brightness(.95); }
.ck3-btn:disabled {
  background: var(--ck3-parchment-aged);
  color: var(--ck3-ink-faint);
  border-color: var(--ck3-parchment-shadow);
  box-shadow: none; cursor: not-allowed;
}

/* Secondary: tooled-leather button on dark chrome */
.ck3-btn--ghost {
  background: var(--ck3-grad-wood);
  color: var(--ck3-gold);
  border: 1px solid var(--ck3-gold);
  box-shadow: inset 0 1px 0 rgba(255,220,160,.12);
}
.ck3-btn--ghost:hover { color: var(--ck3-gold-hi); }

/* Destructive: wax-seal red */
.ck3-btn--danger {
  background: linear-gradient(180deg, #a13030, var(--ck3-wax) 70%, #5a1414);
  color: var(--ck3-parchment-hi);
  border-color: #4a1010;
  text-shadow: 0 1px 1px rgba(0,0,0,.6);
}
```

---

## 2. Panels (the parchment frame)

The workhorse container: parchment interior, gilded border, dark header bar. This
is the single most recognizable CK3 shape.

```css
.ck3-panel {
  position: relative;
  background: var(--ck3-grad-parchment);
  color: var(--ck3-ink);
  border: 1px solid var(--ck3-gold-shadow);
  border-radius: 4px;
  box-shadow:
    0 0 0 3px var(--ck3-wood-light),       /* inner wood mat */
    0 0 0 4px var(--ck3-gold),             /* gilt rule */
    0 10px 28px rgba(0,0,0,.55);           /* drop shadow */
  overflow: hidden;
}
.ck3-panel__header {
  font-family: var(--ck3-font-head);
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--ck3-gold-hi);
  padding: .7em 1.1em;
  background: var(--ck3-grad-wood);
  border-bottom: 2px solid var(--ck3-gold);
  text-shadow: 0 1px 0 #000;
}
.ck3-panel__body { padding: 1.2em 1.4em; }

/* Corner flourishes (optional): small gold squares at the header corners */
.ck3-panel__header::before,
.ck3-panel__header::after {
  content: ""; position: absolute; top: .55em; width: 8px; height: 8px;
  background: var(--ck3-grad-gold); transform: rotate(45deg);
  box-shadow: 0 0 2px #000;
}
.ck3-panel__header::before { left: .6em; }
.ck3-panel__header::after  { right: .6em; }
```

---

## 3. Character / realm card

CK3's portrait cards: a framed image area, a name plate, and trait/attribute
chips. Pair with a heraldic shield (below) for the realm color.

```css
.ck3-card {
  width: 220px;
  background: var(--ck3-grad-parchment);
  border: 3px solid var(--ck3-bronze);
  border-radius: 4px;
  box-shadow: inset 0 0 0 1px var(--ck3-gold-hi), 0 6px 16px rgba(0,0,0,.5);
  overflow: hidden;
}
.ck3-card__portrait {
  aspect-ratio: 1 / 1;
  background: var(--ck3-grad-wood) center/cover;
  border-bottom: 2px solid var(--ck3-gold);
}
.ck3-card__name {
  font-family: var(--ck3-font-head);
  font-weight: 700;
  text-align: center;
  padding: .5em;
  color: var(--ck3-ink);
}
.ck3-chip {
  display: inline-block;
  font-size: .8rem;
  padding: .15em .6em;
  margin: .15em;
  border-radius: 10px;
  background: var(--ck3-parchment-mid);
  border: 1px solid var(--ck3-parchment-shadow);
  color: var(--ck3-ink-soft);
}
.ck3-chip--gold { background: var(--ck3-grad-gold); color: var(--ck3-ink); border-color: var(--ck3-gold-shadow); }
```

---

## 4. Heraldic shield / crest

Stands in for avatars, logos and category badges. A CSS-only escutcheon you can
fill with any tincture and charge.

```css
.ck3-shield {
  width: 64px; aspect-ratio: 5 / 6;
  background: var(--ck3-gules);            /* field tincture */
  border: 3px solid var(--ck3-gold);
  /* escutcheon silhouette: flat top, pointed base */
  clip-path: polygon(0 0, 100% 0, 100% 60%, 50% 100%, 0 60%);
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.25);
  display: grid; place-items: center;
  color: var(--ck3-argent);
}
/* Per-tincture modifiers */
.ck3-shield--azure  { background: var(--ck3-azure); }
.ck3-shield--vert   { background: var(--ck3-vert); }
.ck3-shield--sable  { background: var(--ck3-sable); }
.ck3-shield--purpure{ background: var(--ck3-purpure); }
.ck3-shield--or     { background: var(--ck3-gold); color: var(--ck3-sable); }

/* "Per pale" division example (two colors split vertically) */
.ck3-shield--per-pale {
  background: linear-gradient(90deg, var(--ck3-gules) 50%, var(--ck3-argent) 50%);
}
```

For real arms, drop an SVG charge (lion, cross, eagle) inside the shield `div`.

---

## 5. Tooltip / scroll

CK3 tooltips are little parchment scrolls with a gold edge. Good for hovercards.

```css
.ck3-tooltip {
  max-width: 280px;
  background: var(--ck3-grad-parchment);
  color: var(--ck3-ink);
  border: 1px solid var(--ck3-gold);
  border-radius: 3px;
  padding: .7em .9em;
  font-size: .95rem;
  box-shadow: 0 6px 18px rgba(0,0,0,.6);
}
.ck3-tooltip__title {
  font-family: var(--ck3-font-head);
  color: var(--ck3-wax);
  border-bottom: 1px solid var(--ck3-parchment-shadow);
  padding-bottom: .25em; margin-bottom: .4em;
}
.ck3-tooltip__stat { color: var(--ck3-state-good); font-weight: 600; }
.ck3-tooltip__stat--bad { color: var(--ck3-state-bad); }
```

---

## 6. Dividers & ornaments

```css
/* Gilded rule with a center lozenge */
.ck3-divider {
  display: flex; align-items: center; gap: .8em;
  color: var(--ck3-gold); margin: 1.6em 0;
}
.ck3-divider::before, .ck3-divider::after {
  content: ""; flex: 1; height: 2px;
  background: linear-gradient(90deg, transparent, var(--ck3-gold), transparent);
}
.ck3-divider__lozenge { width: 10px; height: 10px; background: var(--ck3-grad-gold); transform: rotate(45deg); }
```

---

## 7. Tables (ledger style)

```css
.ck3-table {
  width: 100%; border-collapse: collapse;
  background: var(--ck3-parchment);
  color: var(--ck3-ink);
  border: 1px solid var(--ck3-gold-shadow);
}
.ck3-table thead th {
  font-family: var(--ck3-font-head);
  text-align: left;
  background: var(--ck3-grad-wood);
  color: var(--ck3-gold-hi);
  padding: .6em .9em;
  border-bottom: 2px solid var(--ck3-gold);
}
.ck3-table td { padding: .55em .9em; border-bottom: 1px solid var(--ck3-parchment-shadow); }
.ck3-table tbody tr:nth-child(even) { background: var(--ck3-parchment-mid); }
.ck3-table tbody tr:hover { background: var(--ck3-parchment-hi); }
```

---

## 8. Form fields

```css
.ck3-input, .ck3-select, .ck3-textarea {
  font-family: var(--ck3-font-body);
  font-size: 1rem;
  color: var(--ck3-ink);
  background: var(--ck3-parchment-hi);
  border: 1px solid var(--ck3-parchment-shadow);
  border-radius: 3px;
  padding: .5em .7em;
  box-shadow: inset 0 1px 3px rgba(80,60,30,.25);
}
.ck3-input:focus {
  outline: none;
  border-color: var(--ck3-gold);
  box-shadow: inset 0 1px 3px rgba(80,60,30,.25), 0 0 0 2px rgba(201,162,39,.4);
}
```

Each component uses only the shared tokens, so re-theming is a matter of editing
the variables — not the components.
