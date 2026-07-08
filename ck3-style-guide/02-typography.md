# 02 · Typography

CK3 uses three typographic registers, and the substitution strategy below mirrors
them with freely licensed Google Fonts.

| CK3 register | In-game face (proprietary) | Free substitute (Google Fonts) | Role |
|--------------|----------------------------|--------------------------------|------|
| Logo / map script | **Paradox King Script** | **Pinyon Script** (or **Tangerine**) | Logo, hero flourish |
| Titling / headers | Roman-capital titling | **Cinzel** | H1–H3, buttons, labels |
| UI & body text | **GitanLatin** (humanist serif) | **EB Garamond** | All reading text |
| DLC / ceremonial blackletter | **Missale Solis** (Royal Court) | **UnifrakturCook** / **MedievalSharp** | Rare ornament only |

Why these substitutes: GitanLatin is a warm humanist serif → **EB Garamond** is the
closest open analogue with true italics and small caps. CK3 headers and the store
branding lean on engraved Roman capitals → **Cinzel** is the standard open match.
The logo is a flowing chancery script → **Pinyon Script**. Blackletter appears
only on ceremonial DLC art (e.g. *The Royal Court*), so treat it as a spice, never
for body copy.

---

## 1. Loading the fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Pinyon+Script&family=UnifrakturCook:wght@700&display=swap" rel="stylesheet">
```

```css
:root {
  --ck3-font-display: "Pinyon Script", "Tangerine", cursive;
  --ck3-font-head: "Cinzel", "Trajan Pro", Georgia, serif;
  --ck3-font-body: "EB Garamond", Georgia, "Times New Roman", serif;
  --ck3-font-black: "UnifrakturCook", "MedievalSharp", serif;
}
```

---

## 2. Type scale

A restrained modular scale (~1.25). Headers use Cinzel; everything readable uses
EB Garamond at a comfortable 18px base with generous line-height — the game's text
panels are dense but never cramped.

| Token | Size | Line height | Face | Use |
|-------|------|-------------|------|-----|
| `--ck3-fs-display` | 4.5rem | 1.05 | Pinyon Script | Hero logo |
| `--ck3-fs-h1` | 2.75rem | 1.15 | Cinzel 700 | Page title |
| `--ck3-fs-h2` | 2rem | 1.2 | Cinzel 600 | Section |
| `--ck3-fs-h3` | 1.5rem | 1.25 | Cinzel 600 | Subsection |
| `--ck3-fs-h4` | 1.2rem | 1.3 | Cinzel 600 | Card / label |
| `--ck3-fs-body` | 1.125rem | 1.6 | EB Garamond | Paragraphs |
| `--ck3-fs-small` | 0.95rem | 1.5 | EB Garamond | Captions, meta |
| `--ck3-fs-tiny` | 0.8rem | 1.4 | EB Garamond SC | Tags, overlines |

```css
:root {
  --ck3-fs-display: 4.5rem;
  --ck3-fs-h1: 2.75rem;
  --ck3-fs-h2: 2rem;
  --ck3-fs-h3: 1.5rem;
  --ck3-fs-h4: 1.2rem;
  --ck3-fs-body: 1.125rem;
  --ck3-fs-small: 0.95rem;
  --ck3-fs-tiny: 0.8rem;
}
```

---

## 3. Base styles

```css
body {
  font-family: var(--ck3-font-body);
  font-size: var(--ck3-fs-body);
  line-height: 1.6;
  color: var(--ck3-ink);
}

h1, h2, h3, h4 {
  font-family: var(--ck3-font-head);
  font-weight: 700;
  color: var(--ck3-ink);
  letter-spacing: .02em;
  text-wrap: balance;
}

/* Headers on dark chrome get a gilded treatment */
.ck3-on-dark h1, .ck3-on-dark h2, .ck3-on-dark h3 {
  color: var(--ck3-gold);
  text-shadow: 0 1px 0 var(--ck3-gold-shadow), 0 0 14px rgba(201,162,39,.25);
}

h1 { font-size: var(--ck3-fs-h1); }
h2 { font-size: var(--ck3-fs-h2); }
h3 { font-size: var(--ck3-fs-h3); }
h4 { font-size: var(--ck3-fs-h4); text-transform: uppercase; letter-spacing: .08em; }

p { margin: 0 0 1em; max-width: 70ch; }

a {
  color: var(--ck3-azure);
  text-decoration-color: var(--ck3-gold);
  text-underline-offset: .15em;
}
a:hover { color: var(--ck3-wax); }
```

---

## 4. Signature ornaments

### The hero logo
Layered script over a gilded gradient — the marquee CK3 treatment.

```css
.ck3-logo {
  font-family: var(--ck3-font-display);
  font-size: var(--ck3-fs-display);
  line-height: 1;
  background: var(--ck3-grad-gold);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 2px 1px rgba(0,0,0,.6));
}
```

### Illuminated drop cap
Open chapters/articles like a manuscript: an oversized Cinzel initial in gold on a
dark block.

```css
.ck3-prose > p:first-of-type::first-letter {
  font-family: var(--ck3-font-head);
  font-weight: 800;
  float: left;
  font-size: 3.6em;
  line-height: .8;
  padding: .08em .12em 0 0;
  margin: .04em .08em 0 0;
  color: var(--ck3-gold-hi);
  background: var(--ck3-grad-wood);
  border: 1px solid var(--ck3-gold);
  box-shadow: inset 0 0 6px rgba(0,0,0,.6);
}
```

### Overline / kicker
Small-caps Cinzel with letter-spacing for section eyebrows and tags.

```css
.ck3-overline {
  font-family: var(--ck3-font-head);
  font-size: var(--ck3-fs-tiny);
  text-transform: uppercase;
  letter-spacing: .22em;
  color: var(--ck3-bronze);
}
```

### Blackletter accent (use rarely)
For a single ceremonial title or seal caption — never a paragraph.

```css
.ck3-blackletter {
  font-family: var(--ck3-font-black);
  letter-spacing: .01em;
}
```

---

## 5. Rules

- **One serif does the reading.** Keep all body copy in EB Garamond; switching
  faces mid-paragraph breaks the manuscript illusion.
- **Cinzel is for short strings.** Titles, buttons, labels — its all-caps Roman
  forms get fatiguing in long runs.
- **Script and blackletter are jewelry.** A logo, a drop cap, a seal — used once
  per view, they feel regal; repeated, they feel like a Renaissance-fair flyer.
- **Generous leading on parchment.** 1.6 line-height keeps dense text breathable.
- **Color text by surface.** Ink-brown on parchment, gold on dark chrome.
