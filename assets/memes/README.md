# Generic meme templates (SVG only, original geometric reconstructions)

This folder holds **original SVG redraws** of well-known meme
template *layouts* — never traced photographs and never the actual
image files of the real memes. The point is the visual rhythm of
the layout (two-panel comparison, three-panel hierarchy, etc.), not
the source image.

Permitted layouts (each a thin SVG of rectangles + simple shapes +
two/three text slots; figures are stylised, not derived):

- `drake.svg` — two-panel "no / yes" comparison.
- `distracted-boyfriend.svg` — three-figure "tempted by the new" layout.
- `expanding-brain.svg` — four-row escalating-complexity stack.
- `success-kid.svg` — single triumphant figure with caption.
- `is-this-a-pigeon.svg` — figure pointing at object, two captions.
- `two-buttons.svg` — sweating figure with two button choices.
- `change-my-mind.svg` — figure at table with sign + caption.

Use them on slides via the `.meme-frame` CSS helper:

```html
<figure class="meme-frame">
  <svg>...inline SVG redraw...</svg>
  <figcaption>Caption that turns the meme into a teaching joke.</figcaption>
</figure>
```

Hard rules:

1. No photographs, no AI-image, no traced lines from the real
   meme. Geometric reconstruction only.
2. No copyrighted pop-culture references in captions.
3. No institution logos.
