# Pinkstones Winter Wrapped Up — Campaign Monitor template

Complete coded email for **2–30 November 2026**, prepared for import and testing.
Includes the approved campaign copy, two independent CTA links, two benefits with
an explicit OR, a dealership/contact section, original snowy closing artwork, flexible terms and Campaign Monitor
footer tags. No vehicle listings or unrelated Toyota finance copy are included.

**Status:** local validation passed. No Campaign Monitor import/edit round trip or
real email-client send has been performed. Original artwork is integrated; complete the
checks below before a live send. This is the full template, not the earlier POC.

## What to upload

- `winter-wrapped-up.html`: custom editable template source.
- `winter-wrapped-up-campaign-monitor.zip`: portable delivery bundle containing
  that HTML at its root and all ten original PNGs plus six dark-mode variants under `images/winter-wrapped-up/`
  (nine editable foreground images plus the fixed decorative closing background).
- `winter-wrapped-up-images.zip`: image-only archive for an import screen that
  asks for the HTML file and image ZIP separately.

Extract the delivery bundle first if Campaign Monitor asks for separate uploads.
In Campaign Monitor, use **custom-coded template import**, not an HTML-only static
campaign import or the drag-and-drop email builder. Account menu wording varies:
open the template library / My templates, choose import/upload your own template,
upload `winter-wrapped-up.html` and, when prompted, the image archive. Preserve
relative `images/` paths. Name the saved template and create a draft campaign from
it. Review import warnings and verify the labelled regions are recognised.
Do not import `poc/overlay-and-cta.html`; it is an obsolete experiment.

## Original artwork and copy editing

1. The supplied `hero.png` is already integrated intact: branding, campaign title
   and snow edge are baked into the graphic. Replace the entire image using
   **Hero artwork including Pinkstones logo**. There is no separate logo overlay.
   Its embedded words are image content, not editable HTML. The existing editable
   campaign title is retained in the introduction for images-off readability.
2. The original benefit icons, dealership photo, phone/web icons and all three
   supplied social icons (Facebook, LinkedIn, TikTok) are individually replaceable.
   Follow `IMAGE-SPECS.md`; retain proportions and native sizing. No original
   graphic has been modified. The closing section now uses the original `background.png` snowflake artwork,
   with a solid navy fallback for clients such as classic Outlook. This decorative
   background is a fixed HTML/CSS asset rather than an editable image region.
3. Use each labelled heading or rich-text region to edit its content.
   `EDITABLE-REGIONS.md` lists the current named regions. Keep the explicit OR and one-benefit
   eligibility message. Avoid pasting document formatting; paste plain text first.
4. Update the visit copy, telephone, website, sender name/address and footer details.
   Phone number, website, social URLs, privacy URL and full-terms link use editable
   rich-text anchors; select the link and use the editor's link control.

**Pre-send links to confirm:** Facebook, LinkedIn and TikTok currently point to their generic
platform homepages because verified Pinkstones profile URLs were not supplied.
Replace these with the actual profiles (or remove the social content during template
maintenance). The privacy link currently points to `https://www.pinkstones.uk/`;
replace it with the exact approved privacy page. The full-terms link initially uses
the campaign landing URL; confirm it contains the approved full terms or change
it. Telephone and postal address were transcribed from the design reference;
confirm they and the sender identity are current. Configure the authorised From
name/address and reply-to address in Campaign Monitor; these are not HTML settings.

## Edit either CTA without HTML

Both CTA regions are independent: **Primary CTA — label and link** (navy button)
and **Final CTA — label and link** (white button on navy).

1. Click that labelled rich-text region in the custom-template content editor.
2. Place the cursor inside the existing linked text, select just its label, and
   replace it with your new wording. Keep it as one link; do not delete the whole
   paragraph and paste an unlinked label.
3. Select the linked text and open the editor's link/edit-link control. Change the
   destination, initially `https://www.pinkstones.uk/winter-wrapped-up`, and apply.
4. Save, close and reopen the draft. Check label, URL, button treatment and mobile
   wrapping. Repeat separately for the other CTA if both should change.
5. Send to test inboxes, click the centre and near the four button edges, and
   confirm the tracked link reaches the edited destination.

Each CTA has exactly one HTML anchor, inside a `multiline` region. Its own coloured
borders supply the clickable padding; no separate VML link exists. Square corners
in classic Outlook are acceptable. The table cell outside the anchor is not a link.

**Known unverified behaviour:** Campaign Monitor's rich-text editor may change
inline anchor styles, insert paragraphs, or strip formatting after edits. Inline
styles plus `.cta a`/`.cta-light a` stylesheet rules provide two styling paths if
the anchor remains in the region. These rules are a defensive measure, not proof
that editing preserves the design. If formatting is lost, first undo the edit and
edit the existing label/link instead of replacing the whole block. Recreate the
draft from the unmodified imported template if necessary. If that still fails,
a template maintainer must restore the region's markup/styles once and reimport;
marketing should not be asked to synchronise hidden destinations. A plain editable
text link remains functional if styling cannot be retained, but is a visual
fallback to assess, not a claim of a validated button. Record the actual editor
behaviour and correct it before approving a live send.

## Terms, personalisation and required footer

The **Offer terms and conditions** rich-text region supports multiple paragraphs
without a fixed height. Paste the approved full servicing/warranty eligibility,
exclusions and symbol definitions (`*`, `^`) here. The supplied short campaign
terms are included initially; do not assume they cover every final legal detail.
The legal heading and full-terms link are separate regions. No unrelated Toyota
finance boilerplate is used. Confirm both benefits mean a choice of one benefit.

Greeting source: `Hi [firstname,fallback=there],` — intended to render as **Hi Alex,**
when first name is Alex and **Hi there,** when missing. Use Campaign Monitor's
personalisation control if editing this field; do not replace it with literal
`[First Name]`. Check the subscriber first-name field is populated/mapped and test
one record with a name and one without using an actual campaign send. Local
screenshots substitute the fallback only as an illustration; they do not execute
Campaign Monitor personalisation. Blank and whitespace-only values also need testing.

`<unsubscribe>Unsubscribe</unsubscribe>` (visible, outside editable regions) and
`<webversion>` are Campaign Monitor system tags. Leave them
intact; Campaign Monitor generates recipient-specific URLs. They are not normal
static links in a browser. Do not replace unsubscribe with a hard-coded URL.
Sender identification and postal address are editable above these links.

## Subject and inbox preview options

| Option | Subject | Preview |
| --- | --- | --- |
| A (default preview in HTML) | Winter Wrapped Up: Prices down. Extras included. ❄️ | Discover reduced used car prices, plus your choice of two fantastic extras. |
| B | The prices have dropped. The extras haven't. 👀 | Your next car could cost less, with something extra included. |
| C | We've wrapped up something special for you 🎁 | Reduced prices, free servicing or an extended warranty. Discover more. |

Set the actual subject in campaign settings. Set preview text there too where
available, matching the hidden HTML **Inbox preview** region to avoid conflicting
copies. That region may not be selectable in a visual editor because it is hidden;
use campaign preview settings and verify the received inbox snippet. If a different
hidden snippet must be permanently stored in the template and the editor does not
expose it, the template maintainer must update that one default. Test truncation
and emoji rendering in real inboxes.

## Design choices and client expectations

PDF layout retained: navy winter header, pink underline, white introduction,
stacked navy benefit bars with pink icons, navy closing message/white CTA,
full-width dealership photograph, contact/social information, address card and
legal footer. The revised brief permits a combined logo/hero asset. Campaign
headline remains editable HTML in the introduction. The supplied 600 × 350 hero
already contains the snow edge and the graphic campaign title, so the generated
snow divider and separate navy headline band have been removed. This uses the
original artwork without cropping it or repeating the large header title band.
Descriptions sit directly below their respective benefits to clarify the choice.

The closing panel uses solid navy rather than a fixed snowflake background to
avoid noneditable CSS/VML sources. Legal text is larger and darker than the PDF's
small light text for readability. Phone/social icons are separated from editable
text links; mobile stacks contact entries for legibility. There are no absolute
positioning tricks, text-over-image overlays, flex/grid layouts or VML buttons.
Fonts fall back to Arial/Helvetica/sans-serif. Desktop max width is 600px with an
MSO conditional fixed-width wrapper and 96dpi Office setting. Corners may be square
in Word-based Outlook. No claim of identical client rendering is made.

## Validation and required import/send acceptance

Local evidence is in `LOCAL-VALIDATION.json` and `VALIDATION.md`. Screenshots in
`previews/` show Chromium at desktop and mobile widths, including long-copy stress.
They are not Campaign Monitor or Outlook screenshots.

Before live sending:

1. Import and create a draft. Verify every editable region and image control.
   Change each image, save/reopen, and confirm replacements survive. Check alt
   text and sizing. Confirm no imported asset is missing.
2. Change both CTA labels and URLs through the editor as described above. Inspect
   after save/reopen; no lost styling, duplicate links or stale destinations.
3. Paste multi-paragraph final terms, change longer headings and check mobile.
4. Send to authorised test inboxes. Test classic Outlook Windows (Microsoft 365
   and supported perpetual versions) at 100%/125% Windows scaling, new Outlook,
   Outlook.com, Gmail desktop/mobile, Apple Mail and iOS Mail. Test images on/off,
   narrow widths, both CTA edge clicks, link tracking and any dark-mode changes.
5. Check first-name populated/missing/blank cases, actual unsubscribe and browser
   view URLs, sender/address and landing/terms/privacy/social links. Verify the
   received text alternative and edit Campaign Monitor's generated plain-text
   version if necessary. Confirm final campaign dates and one-benefit terms.
6. Have marketing/legal approve imagery, links and terms; then schedule using
   the account's normal sending workflow. No email has been sent by this task.

Official reference URLs are recorded in `CAMPAIGN-MONITOR-COMPATIBILITY.md`.
Earlier source requests were blocked, so these are references rather than claims
that the current account editor was exercised. The overlay POC and historical
review gates are superseded by the latest combined-hero development instruction.

## Maintaining the files

Use the existing checkout; no worktree is needed. The placeholder generator has
been removed. Original PNGs are maintained under `images/winter-wrapped-up/`;
do not regenerate or overwrite them. Their exact source provenance and hashes
are recorded in `ARTWORK-MANIFEST.json`. Validation requires the recorded source
commit to be available locally so it can check original bytes and preserve every
previous editable text region and link destination.
Repackage after any HTML/image changes: `python3 scripts/package-template.py`.
Run `python3 scripts/validate-template.py` with Python, Playwright and Chromium
installed (`CHROMIUM_PATH` can choose the executable). This regenerates local
screenshots/results; it does not send mail or contact Campaign Monitor.

## Artwork fidelity adjustment (3 November 2026)

The original Adobe XD PDF has been reviewed. The winter illustration behind the closing CTA is restored from `images/winter-wrapped-up/background.png`, and both benefit bars now precede their supporting descriptions, matching the reference design's section order. The previously approved full campaign copy, OR separator, two editable CTA links, Arial fallback and exact `<unsubscribe>Unsubscribe</unsubscribe>` tag remain intact. For reliable accessibility and edits, all closing text remains actual HTML, not baked into the background. The background is fixed for the campaign; classic Outlook may display the intentionally solid navy fallback rather than the snowflake texture. This requires a real Outlook test before release.

## Dark-mode adaptation (3 November 2026)

The OS-responsive variant is embedded in the **same** Campaign Monitor HTML template; no separate dark-mode campaign is needed. The header declares `light dark` supported colour schemes, and a `@media (prefers-color-scheme: dark)` block changes light content sections to charcoal, updates body/headline copy to readable near-white, and changes the address/legal cards to darker tones. Additional `[data-ogsc]` selectors provide best-effort support for some Outlook app/web implementations.

Light mode no longer has the pink lines beneath “Prices down. Extras included.” or “Visit our Used Car Centre”; “OR” is now the normal body-text grey. In dark mode “OR” follows the near-white body text to retain contrast.

The hero and designer-supplied winter imagery are **not recoloured or swapped**. The two navy benefit panels retain their white lettering, and the closing winter section keeps its original background and high-contrast white CTA. Arial remains the email-safe font stack.

**Important compatibility limitation:** Different email clients implement dark mode differently. Apple Mail and other media-query-capable clients should follow the custom dark scheme; Gmail and some classic Outlook/Windows variants perform their own inversion or ignore the query, so an exact OS-matched dark version cannot be guaranteed everywhere. Inspect actual received messages in light/dark Outlook (classic and new), Apple Mail/iOS Mail, Gmail (iOS and Android) and Outlook.com. Browser screenshots are simulations, not email-client acceptance.

The GitHub Actions build artifact contains `previews/email-600-dark.png`, `previews/email-375-dark.png`, `previews/email-320-dark.png` (and 800px), alongside the light-mode previews and rebuilt Campaign Monitor ZIPs. The native unsubscribe tag and independently editable CTA anchors are unchanged.


## Paired artwork and social icon-only links (3 November 2026)

The light image is the **default** on clients without dark-mode media-query support, including Gmail Android forced dark mode. Supporting Apple Mail and other clients switch to the corresponding white/dark artwork through `prefers-color-scheme: dark`. The template includes both `<img editable>` sources, with distinct labels such as **Hero artwork including Pinkstones logo — light mode** and **Hero artwork including Pinkstones logo — dark mode**. This is intended to let a marketer replace both variants independently, but **we must verify both controls actually appear in Campaign Monitor**: hidden dark images can be hard or impossible to select in some custom-template editors. If the hidden images are not exposed, a controlled HTML/template update is required.

The supplied six new image variants are `hero-dark.png`, `phone-white.png`, `web-white.png`, `facebook-white.png`, `linkedin-white.png`, `tiktok-white.png`. All ten original assets remain unchanged. Dark variants are packaged in the image ZIP along with the originals.

Facebook, LinkedIn and TikTok are **icon-only clickable links**, each with an accessible link name and two theme variants in a single anchor **outside `<multiline>`**. Campaign Monitor rejects editable images nested inside editable text regions. The underlying destinations are still generic platform URLs until the correct Pinkstones accounts are supplied; do not send with these placeholders. Phone and website keep their visible contact details.

### Android forced dark and buttons

There is **no Android-specific media query** or colour-lock trick. Gmail Android's automatic darkening is accepted; the default light hero/icons remain in place where theme image swap CSS is ignored. Both existing CTAs keep their single, independently editable anchor destinations and have a subtle outline to maintain a visible edge where supported when the client darkens the canvas to near-black. Android may also recolour border, background or text, so verify real Gmail Android test sends at both dark and light device themes. The outline is a best-effort aid, **not** a guarantee that Gmail will preserve the colour.

### Critical import and client test

Import the current GitHub Actions regenerated HTML + image ZIP. In Campaign Monitor edit/save/reopen both hero variants, both phone/web variant pairs, and all six social icon images plus their **one link per social network**. The image-edit controls can offer URL fields, rather than a rich-text link editor, so check both theme variants share the intended destination. Verify the hidden dark variants remain linked after replacing the light variant and that the social icons are still clickable. Test Android Gmail forced dark, Apple Mail dark mode, Gmail light mode, and Outlook clients. Don't send the campaign until this test passes.

## Campaign Monitor nested editable region import correction

The first import rejected three social icons because `<img editable>` tags were inside `<multiline>` regions. This revision removes those three `<multiline>` wrappers. Each social icon is a clickable `<a>` directly wrapping both separately labelled editable image variants. According to Campaign Monitor's image template documentation, the editable image control can expose an image destination URL. **Check and synchronise both light and dark social icon destinations when changing social links**; Campaign Monitor may alter anchor markup when an image's link is edited. Test the outcome after save/reopen. No text caption is displayed. If the editor prevents consistent editing of both variants, maintain the shared social link in the HTML template rather than introducing nested editable regions again.

## Campaign Monitor / Outlook / Android fixes (3 November 2026)

**Footer and address:** The contact details now occupy a dedicated two-column row; the social icons have a separate table before the address. The business name, postal address and telephone remain a dedicated editable address card. Because the previous Campaign Monitor editor was moving social icon text into this address card and clearing the address, Facebook/LinkedIn/TikTok image elements are now fixed template HTML (not editable Campaign Monitor images). Their three links remain clickable, but changing destinations or artwork requires a template HTML update. This deliberate trade-off protects the editable address. The original and white social assets are still packaged, no words are displayed beside the icons, and screen-reader links retain labels.

**Outlook doubled images:** Each dark hero, phone, website and social image is within a hidden wrapper excluded from classic Microsoft Outlook by conditional comments. Light/default images remain visible to Outlook where dark-mode CSS is unsupported. Responsive dark-mode CSS reveals the six alternate assets in compatible clients. Outlook.com and new Outlook may transform markup, so retest the actual Campaign Monitor send; never assume browser previews prove Outlook compatibility.

**Android forced dark buttons (revised):** The primary CTA has no fill in any mode: light/default uses a navy outline with navy text, CSS-supported dark uses a white outline with white text. Gmail Android that ignores media queries gets the transparent navy default and is allowed to apply its own automatic forced-dark recolouring. The closing CTA remains transparent with a white outline over the winter artwork. Real light/dark client testing is still required. Gmail Android is not targeted with colour locking or competing overrides: the native forced-dark transformation is allowed. Test Gmail Android forced-dark mode to check inversion and hit areas; its rendering cannot be guaranteed by browser simulation.

**Campaign Monitor import checklist:** Download a fresh ZIP from the GitHub Actions build for this branch. In a **new** draft or new template import (rather than an old saved draft that may contain broken editor state), verify the contact address is intact, no social text is present, and neither the hero nor any contact/social icons are doubled in Outlook. Edit/save/reopen the remaining hero and phone/web image fields. Review both buttons in actual Gmail Android dark mode and classic Outlook. The three generic social links and the privacy link still require their approved final destinations.


## Gmail Android forced-dark CTA and centred offers (3 November 2026)

**Final requested first CTA treatment:** always transparent. Light/default: 2px navy outline and navy text. Supported dark: 2px white outline and white text. Gmail Android forced dark that ignores colour-scheme CSS gets the default transparent button and may transform its navy text and border itself. No CSS colour-lock techniques or navy background fill are used. Client-rendered Android colours still require visual verification.

The two navy benefit bars now each contain a centred inner two-column table, aligning the title and icon together as one group, including at mobile breakpoints. Confirm visual balance in Campaign Monitor and Outlook after a fresh import.

A Gmail-only spam-test failure is distinct from HTML validation. Review the actual spam-test details (authentication SPF/DKIM/DMARC, Gmail-specific policy feedback, From domain alignment, reputation, unwanted content or failed URLs). Do not claim the CTA markup solves spam placement. Provide the specific Gmail spam-test error and sending domain for further diagnosis; don't modify authentication blindly.
