# Overlay and single-link CTA experiment

**Not production-ready. Do not send as a campaign.** This isolates technical
questions; it is not the full email or an approved redesign. Headline/date copy
is below the artwork to keep this experiment small; final composition is pending.

## Files and proposed mechanism

- `overlay-and-cta.html`: two separately labelled editable foreground images;
  the logo is in a zero-height, visible-overflow wrapper above the hero.
  `position:relative` and stacking order assist layering; no absolute positioning,
  image background, VML fill or duplicated image source is used.
- `images/hero-a.png`, `hero-b.png`: visibly distinct 1200 × 600 PNG placeholders.
- `images/logo-a.png`, `logo-b.png`: separate transparent 400 × 120 PNG placeholders.
- `previews/`: Chromium screenshots at 600, 375 and 320px, before and after local
  DOM replacements. These are browser illustrations, not editor/client evidence.
- `check-local.py`: executable structural and browser assertions. Requires Python,
  Playwright and Chromium; run `python3 poc/check-local.py` from the repository.
  Optional `CHROMIUM_PATH` chooses an installed browser. It starts a temporary
  loopback HTTP server. No external page or CTA navigation occurs.

The hero is 600 × 300 on desktop and scales proportionally. Logo display is
180 × 54, 28px from the right and 24px from the top; the mobile rule uses 130 × 39,
20px right and 18px top. These provisional placements only test the overlay.
Keep supplied asset ratios to avoid overlap geometry changing unexpectedly.
The logo placeholder is lettering for identification, not final brand artwork.

**Critical risk:** classic Outlook can ignore zero-height/overflow styling or
alter stacking. The logo may occupy a separate row, disappear or move. That is
failure of this candidate, not permission to change the design. No claim of
Outlook support is made. The experiment deliberately avoids the unverified
background-to-VML synchronisation problem; it does not prove a replacement method.

## Single-link CTA

One styled `<a>` lives inside a labelled `<multiline>` rich-text region. Its
coloured borders form the padded button area, avoiding a second VML `href` or
label. The surrounding table cell is not claimed to be clickable. Rounded corners
may become square in classic Outlook. Whether the Campaign Monitor rich-text
editor retains the styled anchor and allows convenient label/URL editing remains
an explicit test. This is a candidate editable CTA, not certified editor support.

## Import and edit test — required, not run

1. Import `overlay-and-cta.html` as a **custom editable template**, using
   `overlay-and-cta-images.zip` for the relative `images/` assets (or the upload
   format requested by the account UI). This ZIP is an image archive, not a
   production campaign package. Record any parser warnings verbatim.
2. Create a draft campaign from the template. Record account/editor version if
   exposed, date, template/campaign identifier, and tester. Keep it unsent to
   subscribers. Verify both image edit controls are independently accessible;
   a visually overlapping logo must not prevent selecting the underlying hero.
3. Replace only hero A with hero B using the editor. Save, close and reopen.
   Confirm logo A is unchanged, hero B is used, and layering/geometry persist.
4. Replace only logo A with logo B. Repeat save/reopen. Confirm hero B remains.
   Check transparency, width attributes, responsive styles, rewritten image URLs,
   and alt text controls. Download/export generated HTML where available.
5. Change heading, supporting text and date independently. Check no formatting
   leaks into neighbouring regions.
6. Edit the CTA link through the rich-text link control: change its label and
   destination to a controlled test URL. Save, close/reopen, then verify both.
   Repeat with a long label. Check that no extra links/paragraph margins are
   introduced and that formatting remains a usable button. If restoring styling
   requires source editing, mark marketing editability as failed.
7. Check the generated email has one CTA destination (tracking rewrites are
   expected), two distinct image sources, no stale A assets after replacement,
   and no unintended logo link. Verify the unsubscribe tag resolves in a send.

## Actual send/client test — required, not run

Send through Campaign Monitor to authorised test inboxes after the edits above;
editor/browser previews and forwarding the email are insufficient. Use a small
real test campaign if the platform's preview send does not exercise the same
rewrites. Do not send to a subscriber list merely to run this test.

Record screenshots, received MIME/HTML where available, client/version, Windows
scaling, image loading setting and observed destination for each test:

| Client / condition | Required observation |
| --- | --- |
| Classic Outlook Windows Microsoft 365 and a supported perpetual version | Logo B over hero B at upper right; no extra logo row, clipping or displacement; check 100% and 125% Windows scaling |
| Classic Outlook, images blocked | Alt text/HTML still understandable, CTA visible and clickable, no excessive layout damage |
| Classic Outlook CTA | Click centre and near all four inner button edges; edited destination reached; label not clipped; repeat with long label |
| New Outlook Windows / Outlook.com | Same edited assets and destination; test separately from classic Outlook |
| Gmail web and mobile; Apple Mail / iOS Mail | No overflow at narrow widths; both assets remain independent and positioned; CTA at least 44px tall |
| All clients | Reopen received message, load images, follow tracked CTA and verify final landing URL; no stale destinations |

The entire visual button area must behave as a link. A browser geometry check or
an anchor count alone does not prove Outlook click behaviour. Fail the candidate
if Campaign Monitor changes wrapper styles, editor image selection is obstructed,
CTA styling is lost, assets change together, or classic Outlook loses the overlay.

## Acceptance gate and alternatives

Proceed to full development only after an actual editor round trip and received
classic Outlook send pass, with evidence recorded. Until then the approach is
**unestablished**. If it fails, options requiring approval are:

- Separate logo row: straightforward independent foreground image editing, but
  changes the approved overlay composition.
- Fixed decorative background with separately editable logo/text: closer visual
  match via HTML/VML, but background replacement requires developer maintenance.
- Continue researching a different layered foreground technique: preserves the
  goal, adds time and still needs the same import/send evidence.

No flattened logo/hero alternative has been implemented. No final template build
is authorised by passing the local tests alone.
