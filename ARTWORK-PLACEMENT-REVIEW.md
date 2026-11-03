# Winter Wrapped Up — artwork placement review

Reference: original one-page Adobe XD PDF, “Winter Wrapped Up Campaign Email – 1(1).pdf”, and the ten original PNG exports in `images/winter-wrapped-up/`.

## Confirmed layout

| Source artwork | Correct use in current HTML |
| --- | --- |
| `hero.png` | Editable full-width 600px header image, including Pinkstones branding, campaign lettering and snow edge |
| `servicing.png` | Editable pink icon alongside navy servicing benefit bar |
| `warranty.png` | Editable pink icon alongside navy extended-warranty benefit bar |
| `background.png` | **Restored** to the closing dark-navy winter promotional section, behind editable heading, supporting copy and white CTA |
| `dealership.png` | Editable full-width dealership photograph beneath closing section |
| `phone.png` and `web.png` | Editable contact icons in the visit section |
| `facebook.png`, `linkedin.png`, `tiktok.png` | Editable footer/social icons |

The PDF places the two navy benefit bars before their explanatory paragraphs. This revision restores that order while retaining the expressly requested visible OR separator. All ten original PNG files are unchanged.

## Email client trade-offs

The closing `background.png` is used with the HTML table `background` attribute and inline CSS `background-image`, with `bgcolor="#171d36"` and the equivalent CSS background colour as fallback. Classic Outlook for Windows may show the safe **solid navy** colour instead of the winter texture. This is intentional because no real Campaign Monitor/Outlook send has yet validated a Word/VML image background, and editable text must not be clipped by fixed-height VML containers.

This decorative background is not an `<img editable>` region. Campaign Monitor should not be assumed to provide no-code replacement for it. All nine foreground images remain independently labelled/replaceable in the template editor.

The header uses one complete designer image with embedded lettering as approved; the separate HTML title beneath it remains for readability with images blocked. Campaign Monitor can replace the whole header but cannot edit words baked into the PNG.

## Open pre-send checks

- Import template in Campaign Monitor; verify all editable images, text and both single-anchor CTAs survive save/reopen
- Send tests to classic Outlook, new Outlook, Gmail and Apple Mail and check background fallback, CTA click areas, dark mode and images-off
- Replace generic social URLs and privacy-page placeholder; confirm address, telephone and full terms landing page
- Validate the native Campaign Monitor unsubscribe tag in an actual test send
- Download regenerated packages and browser previews from the GitHub Actions build of this branch, **not** the pre-existing ZIPs on the branch (which precede these source changes)
