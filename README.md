# Pinkstones Winter Wrapped Up — Campaign Monitor template

Complete coded email for **2–30 November 2026**, prepared for import and testing.
Includes the approved campaign copy, two independent CTA links, two benefits with
an explicit OR, a dealership/contact section, flexible terms and Campaign Monitor
footer tags. No vehicle listings or unrelated Toyota finance copy are included.

**Status:** local validation passed. No Campaign Monitor import/edit round trip or
real email-client send has been performed. Original artwork is integrated; complete the
checks below before a live send. This is the full template, not the earlier POC.

## What to upload

- `winter-wrapped-up.html`: custom editable template source.
- `winter-wrapped-up-campaign-monitor.zip`: portable delivery bundle containing
  that HTML at its root and all ten original PNGs under `images/winter-wrapped-up/`
  (nine rendered images plus the unused background).
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
   graphic has been modified. Per your choice, the closing section stays solid
   navy and `background.png` is retained only as an unused packaged source asset.
3. Use each labelled heading or rich-text region to edit its content.
   `EDITABLE-REGIONS.md` lists all 45 regions. Keep the explicit OR and one-benefit
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
