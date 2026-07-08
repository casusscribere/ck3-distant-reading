# 01 · Color & Texture

CK3's palette is built on three material families — **dark wood/leather chrome**,
**aged parchment content**, and **gilded bronze metal** — punctuated by the
saturated **heraldic tinctures** of medieval coats of arms. The mood is warm,
low-key and tactile: almost nothing is pure black, pure white, or fully
saturated.

---

## 1. Core palette

### Chrome — the dark frame
The window furniture: carved wood, tooled leather, stone. Deep, warm, desaturated
browns that let parchment and gold pop.

| Token | Hex | Use |
|-------|-----|-----|
| `--ck3-wood-deep` | `#1d1710` | Outermost background / darkest shadow |
| `--ck3-wood` | `#2a2017` | Main app/chrome background |
| `--ck3-wood-light` | `#3a2c1e` | Raised chrome, headers, navbars |
| `--ck3-leather` | `#473324` | Leather panels, hover chrome |
| `--ck3-stone` | `#4d463a` | Neutral dividers on dark areas |

### Parchment — the content surface
Where text lives. Warm, slightly uneven cream that ages toward tan at the edges.

| Token | Hex | Use |
|-------|-----|-----|
| `--ck3-parchment-hi` | `#efe6cf` | Lightest paper / highlight |
| `--ck3-parchment` | `#e3d5b0` | Default content surface |
| `--ck3-parchment-mid` | `#d4c193` | Secondary panels, inset paper |
| `--ck3-parchment-aged` | `#c2a972` | Edges, aged/disabled paper |
| `--ck3-parchment-shadow` | `#a68a55` | Paper shadow / inner border |

### Gold & bronze — the metal
Frames, ornaments, important actions and dividers. A real metal needs a
highlight, a midtone and a shadow to read as gilded rather than flat yellow.

| Token | Hex | Use |
|-------|-----|-----|
| `--ck3-gold-hi` | `#f2dd8c` | Metal highlight / top bevel |
| `--ck3-gold` | `#c9a227` | Primary gold (borders, accents) |
| `--ck3-bronze` | `#9c7a2e` | Bronze midtone |
| `--ck3-gold-shadow` | `#6b4f1c` | Metal shadow / bottom bevel |

### Ink — text colors
Never pure black on parchment — use warm dark brown to read like iron-gall ink.

| Token | Hex | Use |
|-------|-----|-----|
| `--ck3-ink` | `#2b2017` | Body text on parchment |
| `--ck3-ink-soft` | `#5a4733` | Secondary text, captions |
| `--ck3-ink-faint` | `#8a7355` | Disabled / hint text |
| `--ck3-parchment-text-hi` | `#f4ecd6` | Text on dark chrome |

---

## 2. Heraldic tinctures

CK3's coat-of-arms designer is built on real heraldry. Use these as **category /
accent colors**: faction tags, status states, chart series, link colors. The
classic rule of tincture (don't put color on color) is a good contrast guide —
pair a saturated tincture with a metal (gold/argent), not with another color.

| Heraldic name | Token | Hex | Typical meaning |
|---------------|-------|-----|-----------------|
| Gules (red) | `--ck3-gules` | `#8f2222` | War, danger, claims |
| Azure (blue) | `--ck3-azure` | `#244f7a` | Loyalty, diplomacy |
| Vert (green) | `--ck3-vert` | `#3a5e2e` | Growth, stewardship |
| Sable (black) | `--ck3-sable` | `#181410` | Death, secrets |
| Purpure (purple) | `--ck3-purpure` | `#5b2a58` | Royalty, intrigue |
| Or (gold metal) | `--ck3-gold` | `#c9a227` | Wealth, prestige |
| Argent (silver metal) | `--ck3-argent` | `#e8e2d0` | Peace, faith |
| Wax seal red | `--ck3-wax` | `#7a1f1f` | Seals, alerts, stamps |

> Heraldic reds in CK3 sit between brick and blood — avoid pure `#ff0000`.

### Semantic states
Map the tinctures to UI status so red/green/etc. stay on-theme:

| State | Token | Hex |
|-------|-------|-----|
| Positive / success | `--ck3-state-good` | `#3a5e2e` (vert) |
| Negative / danger | `--ck3-state-bad` | `#8f2222` (gules) |
| Warning / caution | `--ck3-state-warn` | `#b8860b` (dark gold) |
| Info / neutral | `--ck3-state-info` | `#244f7a` (azure) |

---

## 3. CSS variables

```css
:root {
  /* Chrome */
  --ck3-wood-deep: #1d1710;
  --ck3-wood: #2a2017;
  --ck3-wood-light: #3a2c1e;
  --ck3-leather: #473324;
  --ck3-stone: #4d463a;

  /* Parchment */
  --ck3-parchment-hi: #efe6cf;
  --ck3-parchment: #e3d5b0;
  --ck3-parchment-mid: #d4c193;
  --ck3-parchment-aged: #c2a972;
  --ck3-parchment-shadow: #a68a55;

  /* Metal */
  --ck3-gold-hi: #f2dd8c;
  --ck3-gold: #c9a227;
  --ck3-bronze: #9c7a2e;
  --ck3-gold-shadow: #6b4f1c;

  /* Ink */
  --ck3-ink: #2b2017;
  --ck3-ink-soft: #5a4733;
  --ck3-ink-faint: #8a7355;
  --ck3-parchment-text-hi: #f4ecd6;

  /* Heraldic tinctures */
  --ck3-gules: #8f2222;
  --ck3-azure: #244f7a;
  --ck3-vert: #3a5e2e;
  --ck3-sable: #181410;
  --ck3-purpure: #5b2a58;
  --ck3-argent: #e8e2d0;
  --ck3-wax: #7a1f1f;

  /* Semantic */
  --ck3-state-good: #3a5e2e;
  --ck3-state-bad: #8f2222;
  --ck3-state-warn: #b8860b;
  --ck3-state-info: #244f7a;

  /* Gradients (see below) */
  --ck3-grad-gold: linear-gradient(180deg, var(--ck3-gold-hi) 0%, var(--ck3-gold) 45%, var(--ck3-bronze) 75%, var(--ck3-gold-shadow) 100%);
  --ck3-grad-parchment: linear-gradient(180deg, var(--ck3-parchment-hi) 0%, var(--ck3-parchment) 55%, var(--ck3-parchment-aged) 100%);
  --ck3-grad-wood: linear-gradient(180deg, var(--ck3-wood-light) 0%, var(--ck3-wood) 60%, var(--ck3-wood-deep) 100%);
}
```

---

## 4. Textures (pure CSS, no image files)

You can get most of the tactile feel without shipping image assets by layering
gradients and SVG noise. Real projects can swap in tiled paper/wood photos, but
these keep the kit self-contained.

### Parchment surface
A soft vignette plus faint fibre mottling.

```css
.ck3-parchment-surface {
  background-color: var(--ck3-parchment);
  background-image:
    radial-gradient(ellipse at 50% 0%, rgba(255,255,255,.35), transparent 60%),
    radial-gradient(ellipse at 100% 100%, rgba(120,90,50,.25), transparent 55%),
    radial-gradient(circle at 20% 30%, rgba(150,120,70,.10) 0 2px, transparent 2px),
    radial-gradient(circle at 70% 60%, rgba(150,120,70,.08) 0 2px, transparent 2px);
  background-blend-mode: normal, multiply, normal, normal;
  color: var(--ck3-ink);
}
```

### Aged paper grain (SVG noise overlay)
Add as a `::before` over any surface for a film of grain.

```css
.ck3-grain::before {
  content: "";
  position: absolute; inset: 0;
  pointer-events: none;
  opacity: .06;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

### Carved wood / leather chrome
```css
.ck3-wood-surface {
  background-color: var(--ck3-wood);
  background-image:
    linear-gradient(180deg, rgba(255,220,160,.05), rgba(0,0,0,.35)),
    repeating-linear-gradient(90deg, rgba(0,0,0,.18) 0 2px, transparent 2px 7px);
}
```

### Gilded edge / metallic strip
A thin gold rule with a highlight line — use for dividers and frame edges.

```css
.ck3-gold-rule {
  height: 4px;
  background: var(--ck3-grad-gold);
  border-top: 1px solid var(--ck3-gold-hi);
  border-bottom: 1px solid var(--ck3-gold-shadow);
}
```

---

## 5. Do / Don't

- **Do** keep large dark areas warm-brown, not neutral gray or pure black.
- **Do** reserve saturated tinctures for small, meaningful accents.
- **Do** give gold a bevel (highlight + shadow) so it reads as metal.
- **Don't** put body text on saturated color — keep reading on parchment.
- **Don't** use flat `#ffffff` panels or `#000000` text; it breaks the period feel.
- **Don't** let more than ~10% of a screen be gold.
