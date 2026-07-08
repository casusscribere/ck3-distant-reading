# Crusader Kings III — Web Style Guide

A practical design system for building websites that evoke the look and feel of
**Crusader Kings III** (Paradox Interactive). It distills the game's visual
identity — aged parchment, dark carved wood and leather, gilded bronze framing,
illuminated-manuscript typography and medieval heraldry — into reusable tokens,
CSS, and component patterns.

> **Scope & honesty note.** This guide is an *homage* built from publicly
> observable design cues on Paradox's official site and the CK3 Wiki. The exact
> in-game fonts (**Paradox King Script** for the logo/map, **GitanLatin** for UI
> text) and art assets are Paradox's proprietary property and are **not** bundled
> here. Everything below uses free, openly licensed substitutes (Google Fonts,
> CSS gradients, SVG) chosen to match the spirit of the originals. Do not pass off
> the result as official Paradox material.

---

## The files

| File | What's in it |
|------|--------------|
| [`01-color-and-texture.md`](01-color-and-texture.md) | Full palette, heraldic tinctures, parchment/wood/gold textures, CSS variables |
| [`02-typography.md`](02-typography.md) | Typeface choices, the type scale, headings, body, drop caps, CSS |
| [`03-components.md`](03-components.md) | Buttons, panels, cards, shields/crests, tooltips, dividers, tables |
| [`04-layout.md`](04-layout.md) | Page structure, framing, spacing, responsive rules, motion |
| [`theme.css`](theme.css) | Consolidated, copy-paste stylesheet of every token and component |

## Fastest path to using it

1. Drop [`theme.css`](theme.css) into your project and link it in `<head>`.
2. Add the Google Fonts line from [`02-typography.md`](02-typography.md).
3. Wrap content in the structural classes documented in
   [`04-layout.md`](04-layout.md) (`.ck3-page`, `.ck3-panel`, etc.).
4. Compose UI from the component classes in [`03-components.md`](03-components.md).

## The five design principles

1. **Parchment over glass.** Content sits on warm, aged paper — never flat white.
   Backgrounds are dark, tactile, and material (wood, leather, stone).
2. **Everything is framed.** Panels, portraits and crests get a gilded or carved
   border. Nothing floats edge-to-edge; borders are a feature, not a footnote.
3. **Gold is the accent, not the field.** Bronze/gold signals importance — titles,
   actions, dividers. Used sparingly it reads regal; overused it reads gaudy.
4. **Heraldry carries identity.** Shields, tinctures and ordinaries stand in for
   logos, avatars and category colors.
5. **Legible, literary text.** A humanist serif for reading, a Roman titling face
   for headers, blackletter and script used *only* as ornament.

See each file for the specifics, the rationale, and ready-to-paste CSS.
