# Original artwork inventory — Winter Wrapped Up

All artwork comes directly from `origin/main`, under `images/winter-wrapped-up/`.
No supplied PNG has been redrawn, cropped, recompressed, converted or overwritten.
`ARTWORK-MANIFEST.json` records the fetched source commit, byte sizes and SHA-256
hashes. Validation compares all ten files with that Git snapshot.

| Original file | Native pixels | Aspect ratio | Display at desktop email width | Campaign Monitor image label |
| --- | --- | --- | --- | --- |
| `hero.png` | 600 × 350 | 12:7 | 600 × 350px | Hero artwork including Pinkstones logo |
| `dealership.png` | 600 × 335 | 120:67 | 600 × 335px | Dealership photograph |
| `servicing.png` | 41 × 40 | 41:40 | Up to 41 × 40px | Servicing benefit heading icon |
| `warranty.png` | 38 × 38 | 1:1 | Up to 38 × 38px | Warranty benefit heading icon |
| `phone.png` | 22 × 22 | 1:1 | Up to 22 × 22px | Contact telephone icon |
| `web.png` | 22 × 22 | 1:1 | Up to 22 × 22px | Contact website icon |
| `facebook.png` | 38 × 38 | 1:1 | Up to 26 × 26px | Facebook destination icon |
| `linkedin.png` | 38 × 38 | 1:1 | Up to 26 × 26px | LinkedIn destination icon |
| `tiktok.png` | 38 × 38 | 1:1 | Up to 26 × 26px | TikTok destination icon |
| `background.png` | 600 × 382 | 300:191 | Background behind closing offer panel | Fixed CSS/table background; not a Campaign Monitor editable-image region |

The approved design PDF shows the original navy snowflake illustration behind the closing promotional panel. The supplied `background.png` is now used as that decorative background without modification. A solid navy `bgcolor` is retained as the classic Outlook/images-off fallback. Unlike `<img editable>`, a CSS/table background is **not independently replaceable in the Campaign Monitor editor**; replacing this decorative image requires editing the HTML and rebuilding the packages. The original hero and other nine foreground images remain separately editable.

## Header composition

The supplied hero already contains the Pinkstones logo, the campaign title and
the complete snow edge. It replaces both generated header graphics and their
separate headline band. The PNG is used intact as one editable image; there is
no separate logo overlay or generated snow divider. Campaign Monitor can replace
the entire graphic; it cannot edit words baked into its pixels.

The existing editable `Hero headline` text is retained in the white introduction,
before “Prices down. Extras included.”, keeping the approved campaign title
available as HTML and when images are blocked. Editing that HTML region does not
change the title in the hero artwork; replace the hero if both must change.

## Responsive sizing and future replacements

- Full-width hero and photograph use a 600px width attribute, fluid CSS width and
  automatic height. At 375px they display at approximately 375 × 218.75px and
  375 × 209.38px. At 320px: approximately 320 × 186.67px and 320 × 178.67px.
- No image uses `object-fit`, clipping, CSS crop or forced square dimensions.
  The non-square servicing icon retains its 41:40 ratio. Icons are not enlarged
  beyond their native dimensions. Original transparency is preserved.
- Keep the same aspect ratio and safe-area composition on replacement. The source
  hero logo/title and snow edge must remain visible at 320px; the entire image
  scales rather than crops. Do not stretch an existing export to make a 2× asset.
- If a designer supplies future high-density exports, use 1200 × 700 for the hero,
  1200 × 670 for photography, 82 × 80 for servicing, 76 × 76 for warranty,
  44 × 44 for phone/web and at least 52 × 52 for social icons. These are future
  export suggestions, not changes made to the supplied artwork.
- Use PNG with sRGB/RGB and retain transparency for the icons. Keep important
  photography centred and avoid essential small text within replacement photos.
  All campaign dates, benefit descriptions, CTAs and legal text remain HTML.
- Target no more than about 200KB for a future hero and 350KB for photography,
  and under 10KB per small icon where quality permits. The current files are
  retained exactly, irrespective of size. Their nine rendered originals total
  about 478KB; the closing background adds about 101KB to the delivery archives.

All HTML text uses `Arial, Helvetica, sans-serif`. Typography already baked into
supplied artwork is preserved; it has not been redrawn to match the HTML font.
