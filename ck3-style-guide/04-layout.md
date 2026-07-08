# 04 · Layout, Spacing & Motion

How to assemble the pieces into a page that feels like CK3's interface: a dark
framed stage, parchment content floating inside gilded borders, deliberate
spacing, and restrained, weighty motion.

---

## 1. Page structure

CK3 frames the whole screen in dark chrome and floats panels over a map/scene.
Translate that to: a dark textured `body`, a constrained content column, and
panels that sit on top with clear borders.

```css
.ck3-page {
  min-height: 100vh;
  background: var(--ck3-wood-deep);
  background-image:
    radial-gradient(ellipse at 50% -10%, rgba(120,90,50,.35), transparent 60%),
    var(--ck3-grad-wood);
  background-attachment: fixed;
  color: var(--ck3-parchment-text-hi);
  font-family: var(--ck3-font-body);
}
.ck3-shell {
  max-width: 1200px;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 3rem);
}
```

### Recommended regions
- **Top bar (`.ck3-topbar`)** — dark wood strip with gold bottom rule; holds the
  logo (script) and primary nav (Cinzel small-caps). Mirrors CK3's persistent top
  resource bar.
- **Hero** — script logo over a darkened scene image, gilded divider beneath.
- **Content** — one or two columns of `.ck3-panel`s on the dark stage.
- **Sidebar** — a leather column of crests/links, like the character/realm trees.
- **Footer** — dark wood, low-contrast small-caps, a single gold rule on top.

```css
.ck3-topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: .6em clamp(1rem, 3vw, 2rem);
  background: var(--ck3-grad-wood);
  border-bottom: 3px solid var(--ck3-gold);
  box-shadow: 0 2px 10px rgba(0,0,0,.6);
}
.ck3-nav a {
  font-family: var(--ck3-font-head);
  text-transform: uppercase; letter-spacing: .12em; font-size: .85rem;
  color: var(--ck3-parchment-aged); margin-left: 1.6em; text-decoration: none;
}
.ck3-nav a:hover, .ck3-nav a[aria-current] { color: var(--ck3-gold-hi); }
```

---

## 2. Spacing scale

An 8px base keeps rhythm consistent. Panels are generously padded — CK3 interfaces
are dense but never edge-crammed.

```css
:root {
  --ck3-space-1: 4px;
  --ck3-space-2: 8px;
  --ck3-space-3: 16px;
  --ck3-space-4: 24px;
  --ck3-space-5: 40px;
  --ck3-space-6: 64px;
  --ck3-radius: 4px;
  --ck3-radius-sm: 3px;
}
```

Guidelines: panel padding `--ck3-space-4`; gap between panels `--ck3-space-4` to
`-5`; section rhythm `--ck3-space-6`; never below `--ck3-space-2` between framed
elements (borders need breathing room or the gold lines visually merge).

---

## 3. Framing rule

The defining habit of the look: **layered borders**. A panel is dark mat → gold
rule → parchment, reading as paper mounted in a gilt frame. Reuse this stacking
with `box-shadow` rings (see `.ck3-panel`) rather than nested elements.

```css
.ck3-frame {
  border: 1px solid var(--ck3-gold-shadow);
  box-shadow:
    0 0 0 3px var(--ck3-wood-light),
    0 0 0 4px var(--ck3-gold),
    0 8px 24px rgba(0,0,0,.5);
  border-radius: var(--ck3-radius);
}
```

Apply `.ck3-frame` to images, video embeds, map figures and portraits so media
matches the panel language.

---

## 4. Grid patterns

```css
/* Card gallery (characters, realms, articles) */
.ck3-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: var(--ck3-space-4);
}
/* Two-column reading layout: content + crest sidebar */
.ck3-split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 280px;
  gap: var(--ck3-space-5);
}
@media (max-width: 860px) {
  .ck3-split { grid-template-columns: 1fr; }
}
```

---

## 5. Responsive rules

- **Fluid frame, fixed feel.** Use `clamp()` for shell padding and hero type so
  the gilded framing scales without breaking.
- **Collapse sidebars below ~860px**; move crest/nav into a top row of chips.
- **Keep borders proportional.** On small screens reduce the multi-ring shadow to
  a single gold rule so frames don't dominate.
- **Parchment stays readable.** Max line length ~70ch regardless of viewport.

```css
@media (max-width: 600px) {
  .ck3-panel { box-shadow: 0 0 0 2px var(--ck3-gold), 0 6px 16px rgba(0,0,0,.5); }
  :root { --ck3-fs-h1: 2rem; --ck3-fs-display: 3rem; }
}
```

---

## 6. Motion

CK3's UI motion is weighty and deliberate — things slide and settle, gold
glints, nothing bounces. Keep durations modest and easing soft.

```css
:root { --ck3-ease: cubic-bezier(.22,.61,.36,1); }

/* Panel entrance: settle down into its frame */
@keyframes ck3-settle {
  from { opacity: 0; transform: translateY(-8px) scale(.99); }
  to   { opacity: 1; transform: none; }
}
.ck3-panel { animation: ck3-settle .35s var(--ck3-ease) both; }

/* Gold shimmer for emphasis (e.g. on a new achievement/title) */
@keyframes ck3-glint {
  0%, 100% { filter: brightness(1); }
  50%      { filter: brightness(1.25); }
}
.ck3-glint { animation: ck3-glint 2.4s var(--ck3-ease) infinite; }

@media (prefers-reduced-motion: reduce) {
  .ck3-panel, .ck3-glint { animation: none; }
}
```

Principles: hover = brighten/lift, never recolor wholesale; transitions
120–350ms; reserve the gold glint for genuinely important, infrequent moments;
always honor `prefers-reduced-motion`.

---

## 7. Accessibility notes

- Ink-brown on parchment (`#2b2017` on `#e3d5b0`) and parchment-hi text on dark
  wood both clear WCAG AA for body text — but **gold (`#c9a227`) on parchment does
  not**; use gold only on dark chrome or for large/decorative text.
- Don't rely on tincture alone to convey state; pair color with an icon or label.
- Keep focus rings visible — the `.ck3-input:focus` gold halo is intentional;
  don't remove outlines without a replacement.
