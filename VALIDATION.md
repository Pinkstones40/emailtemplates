# Full-template validation

Scope: `winter-wrapped-up.html` and its two upload packages. The results below are from the prior artwork integration, **before this new closing-background and benefit-order change**. A GitHub Actions workflow on this branch regenerates packages and previews and reruns checks. Until that workflow completes successfully, treat the prior passing results and committed ZIPs/previews as historical only. No Campaign Monitor account import, editor test, sending operation,
Litmus/Email on Acid run or Microsoft Outlook rendering was performed.

Machine-readable results: `LOCAL-VALIDATION.json`. Reproduce using
`python3 scripts/package-template.py` then `python3 scripts/validate-template.py`.
The latter requires Python Playwright and installed Chromium. It uses a temporary
loopback server and never opens CTA URLs or sends mail.

## Passed local checks

| Check | Evidence / scope |
| --- | --- |
| Full campaign content | 23 explicit phrase checks cover approved introduction, headings, descriptions, both closing paragraphs, initial terms, dates and sender address; CTA labels counted separately |
| Editable regions | 45 uniquely labelled regions, no nested editable regions; visible body text must be within a text region or Campaign Monitor system-link tag |
| CTA destinations | Exactly two `.cta a` anchors with campaign URL; one additional, independently editable full-terms link starts at the same URL; no VML destinations |
| Markup structure | Strict start/end-tag stack, table/tr/td hierarchy, unique region labels, no scripts, no fixed-height text containers; this is structural checking, not W3C validation of Campaign Monitor's custom tags |
| Image assets | Nine distinct original PNG paths; each displayed image has an editable control, alt text and a width attribute; one intact hero including logo/title/snow edge, no separate overlay |
| Original artwork integrity | SHA-256/byte counts for all ten sources match `ARTWORK-MANIFEST.json` and the fetched Git commit; no original file modified |
| Approved content regression | Every existing editable text region and its link URLs matches the fetched main snapshot; only the native unsubscribe label changes as requested; Facebook adds a new editable social link |
| Font stack | Every HTML font-family declaration uses `Arial, Helvetica, sans-serif`; image pixels are unchanged |
| Image geometry | Each image retains its natural aspect ratio in Chromium at every tested width and is never enlarged beyond its native width |
| ZIPs | Delivery archive contains exact HTML and all ten original PNGs; image-only archive contains all ten PNGs, including the closing decorative background; CRC, membership and byte equality checked |
| Responsive layout | Chromium at viewport widths 800, 600, 375 and 320px; shell no wider than 600px; no horizontal overflow |
| Button geometry | Both CTAs at least 44px tall; browser hit testing at the midpoint of each of four borders resolves to the anchor |
| Longer content | Both CTA labels lengthened and URLs changed in the local DOM; warranty heading lengthened; terms replaced by 16 long paragraphs; no horizontal overflow or legal/footer overlap |
| Missing images | Local image sources deliberately broken after the stress test; remaining text still has no horizontal overflow |
| Contact fallback stress | Contact entries forced back into an unstacked row with larger side padding at each width; no horizontal overflow; this is not a complete no-CSS email-client simulation |
| Excluded content | No unrelated Toyota/MY25/PCP/APR copy, vehicle-price copy or stock listing sections in the source |
| Personalisation/footer source | Expected `[firstname,fallback=there]`, exact `<unsubscribe>Unsubscribe</unsubscribe>` outside editable regions, and `webversion` tags present; literal `[First Name]` absent; actual expansion remains untested |

The local DOM substitutions are fixtures. They do not exercise Campaign Monitor's
editor sanitisation, region recognition, tracking or personalisation engine.

## Previews and reference review

- `previews/email-800.png`: desktop viewport, centred 600px email.
- `previews/email-600.png`: email-width desktop layout.
- `previews/email-375.png`: mobile.
- `previews/email-320.png`: narrow mobile.
- `previews/email-375-long-text.png`: long-terms/long-label stress, not campaign copy.

Normal screenshots substitute “Hi there,” in the DOM for illustration; the source
retains the Campaign Monitor personalisation token. Browser view/unsubscribe tags
are not recipient-specific links until Campaign Monitor processes them.

The desktop/mobile screenshots were visually reviewed against the supplied PDF.
Retained: navy winter header/logo placement and white snow edge, white intro with
pink underline, stacked navy benefit bars with pink icons, closing navy/white CTA,
full-width dealership image, contact/social row, address card and grey legal footer.
Changed for editable content/readability: the existing editable campaign title in
the introduction below the intact original hero, explicit OR and benefit-associated descriptions, original snowy closing-panel background with navy fallback,
legible dark legal text, and stacked contact entries on small mobile viewports.
All generated placeholder artwork is replaced by untouched original PNG exports
fetched from GitHub. The original hero incorporates its logo, title and snow edge.
The supplied photograph is used without cropping; no attempt was made to alter
it to match a different photograph in the PDF. Facebook joins the contact/social
row. `background.png` has now been restored to the closing section by the user's updated instruction; source-only packaging is no longer its purpose.

## Outstanding import and real-client validation

Use the detailed checklist in README. Required outcomes before live use:

1. Import both uploads; all 45 regions and nine image controls recognised; no lost
   styles or unresolved assets. Save/reopen after each image and text edit.
2. Edit CTA labels and destinations through the rich-text link UI; both buttons
   retain formatting and one destination each after save/reopen and tracked send.
   Follow README's recovery procedure if the editor alters anchor formatting.
3. Send to classic Outlook Windows, new Outlook/Outlook.com, Gmail web/mobile,
   Apple Mail/iOS Mail. Check Windows 100%/125% scaling, images blocked, mobile
   wrapping, dark mode and actual button edge clicks. Square Outlook corners are
   acceptable. A browser screenshot does not establish Outlook compatibility.
4. Test populated, missing, blank and whitespace first names; inspect unsubscribe,
   browser-view links, generated plain-text version, sender identity and landing
   links in received messages. Do not infer successful personalisation from a
   browser's static token rendering.
5. Approve legal text and validate sender/contact data.
   Replace generic Facebook/LinkedIn/TikTok/privacy destinations and confirm full terms URL.

No unsupported overlay work remains necessary under the new combined-hero brief.

## New branch verification gate

On branch `fix/winter-wrapped-up-artwork-final`, GitHub Actions workflow `.github/workflows/validate-email-artwork.yml` rebuilds both ZIPs and regenerates previews before running structural and responsive validation. Its uploaded `winter-wrapped-up-campaign-monitor-tested` artifact is the authoritative package for the new HTML once the workflow has passed. The ZIPs and preview PNGs already stored in this branch were generated before these changes and must not be treated as current until rebuilt. Actual Campaign Monitor and Outlook acceptance remains outstanding.

## Dark-mode / decorative changes (3 November 2026)

- Removed the two pink accent dividers below the supporting headline and dealership visit heading
- Changed the editable “OR” separator to body-copy grey in light mode
- Added `color-scheme` and `supported-color-schemes` meta tags, `prefers-color-scheme: dark` email CSS and best-effort `data-ogsc` Outlook hooks
- Added explicit dark surface, dark legal/address cards, light text and high-contrast CTA selectors while retaining untouched PNG exports
- `scripts/validate-template.py` now asserts these requirements and creates browser-simulated `email-{width}-dark.png` previews at widths 800, 600, 375 and 320

The earlier validation table relates to the historical integration commit. The new GitHub Actions workflow builds and validates the current branch; use its downloadable artifact. **No claim is made that Gmail iOS, Windows Outlook or Campaign Monitor will preserve all custom dark-mode CSS until a real send/client test has passed.**
