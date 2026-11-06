# Previous campaign review

Reference repository: `/workspace/emailtemplates`.
Previous campaign: `winter-wrapped-up.html`, with `images/winter-wrapped-up/`, packaging/validation scripts and documentation. Reviewed the current HTML, README history, compatibility assessment, validation notes and scripts. Existing files are reference material only.

## Reusable patterns

- Presentation tables; fluid 100% shell capped at 600px; MSO-only 600px wrapper, table-spacing resets, Office 96dpi setting and Arial/Helvetica fallbacks.
- Critical inline presentation with embedded responsive/dark enhancements. Explicit image width attributes and fluid width/auto height for large images. No JavaScript, flex/grid or external CSS.
- At 599px, reduce side padding and heading size. At 420px, stack complete contact entries; nested two-cell icon/text tables preserve immediate horizontal adjacency. Legal content has no fixed height.
- Labelled `singleline` headings and `multiline` paragraphs/links; `img editable="true"` outside editable text. Native unsubscribe and webversion tags outside editable copy. No repeatable sections found.
- One anchor per CTA inside editable rich text, inline and stylesheet styling, no separate VML link. Classic Outlook uses square corners; decorative CSS background has a solid fallback rather than VML.
- Packaging utility gathers image paths and builds HTML/image ZIPs. Validator checks structure, editable nesting/labels, assets, archive consistency and Chromium layout, image failure and long-content behaviour. These are reusable concepts, not directly reusable scripts: existing scripts hardcode old content, asset paths and output locations.

## Client-specific findings

**Outlook desktop:** MSO wrapper, 96dpi Office setting, safe fonts and table resets. Dark-image wrappers are excluded with non-MSO conditionals to address previously doubled assets. CSS backgrounds can fall back to solid colour; no VML is present. New Outlook/Outlook.com require separate tests.

**Gmail:** inline defaults, simple tables and fluid images provide the base layout. Transparent outlined CTAs were adopted after Android forced-dark feedback; native inversion is allowed rather than assumed controllable. Media queries alone cannot establish Gmail dark-mode behaviour.

**Apple Mail/iOS:** viewport and format-detection metadata plus Apple data-detector link reset. Light/dark colour-scheme metadata and dark CSS pair dark surfaces with light text, address/legal cards, dividers, offer bars and CTA borders. The primary CTA additionally sets descendant text fill in supported dark mode. These are implemented mitigations, not evidence that all automatic iOS transformations are fixed.

## Editability concerns to avoid

Current HTML has paired editable hero and phone/web images for light/dark modes. Replacing one does not inherently update the other. Do not carry this pattern forward. Prefer one opaque/theme-safe artwork source with suitable contrast; inspect supplied art before deciding its treatment. Any requirement for separate theme artwork needs a documented Campaign Monitor-compatible proposal first.

Social icons currently have fixed light/dark assets and fixed destinations after reported editor corruption affecting the adjacent address. This protects that old layout but does not satisfy new campaign editability. The historical rejected nesting of editable images inside `multiline` must not recur. Keep social controls separate from editable postal address regions and test save/reopen.

CTA rich-text edits can strip inline styling or insert paragraphs; stylesheet fallback is defensive, not verified editor preservation. Fixed CSS background imagery is not editor-replaceable. Hidden preheader selection and image-link controls need account verification. Hero lettering baked into image pixels is editable only by replacing the image.

## Evidence limits

README and validation documents contain superseded iterations, including conflicting asset/control counts, earlier background decisions and older social-editing instructions. Current HTML and latest follow-up notes describe the final source more accurately. Local checks/browser screenshots are not actual Outlook, Gmail or iOS renders. Documentation records earlier import/client feedback but does not establish a passing acceptance test of the final revision. Official-document access had previously failed; this review does not assert fresh documentation verification or account access.

## New folder

`pinkstones-toyota-email/` contains this review, its own README and `assets/`. `email.html` and optional `preview.html` are deferred until creative specifications arrive. No old campaign imagery, copy, contacts or legal details are assumed appropriate. Production assets must resolve through Campaign Monitor hosting or verified public HTTPS hosting.

Confirmed franchise: Pinkstones Toyota, Stoke-on-Trent, part of Pinkstones Motor Group. Toyota artwork and approved brand guidance determine the new visual design. Contact and regulatory details remain unconfirmed.

## Implementation update

The supplied Fleet email introduction PDF has now been implemented in this folder. See README for design differences, confirmed PDF contact details, official editable-content documentation checked, evidence and unresolved production gates. Earlier awaiting-artwork notes above describe the preparation stage.
