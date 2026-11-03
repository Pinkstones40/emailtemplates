# Campaign Monitor compatibility assessment

Status: experimental foreground-overlay and single-link CTA proof of concept added;
Campaign Monitor editor and received Outlook tests pending. Full build not approved.

## Evidence from the resumed verification

The configuration draft (revision 2) contains both `www.campaignmonitor.com`
and `help.campaignmonitor.com`. The running environment reports a restricted,
enforced policy with an empty custom `allowed_hosts` list; neither host appears
in its effective allowed hosts. Thus the saved configuration and runtime differ.

Requests through the inherited proxy, outside the command sandbox, to both URLs
below failed with `HTTP/1.1 403 Forbidden` and `CONNECT tunnel failed`:

- https://www.campaignmonitor.com/create/email-builder/custom-html/
- https://help.campaignmonitor.com/

These are attempted official documentation entry points, **not retrieved sources
supporting a compatibility claim**. No official article contents were retrieved.
No Campaign Monitor account import/editor test or real Outlook send test was run.
This evidence does not establish that Campaign Monitor lacks a requested feature.

## 1. Independent editable hero/logo overlay

Not verified. Standard editable foreground images do not by themselves solve a
layered header. A background implementation must allow the marketing editor to
replace the hero and propagate the replacement to every rendering path, including
an Outlook VML fill, while leaving the foreground logo separately editable.

Do not assume an `editable` attribute on an image also controls CSS, a table's
`background` attribute or `<v:fill src="…">`. Do not assume identically named
regions synchronise their values. These behaviours need explicit documentation
and an import/edit/send check before claiming support.

If current support does not provide this synchronisation, proposed alternatives
for user approval are:

1. A separate navy logo row immediately above an independently editable hero.
   Both remain foreground images; the visual overlay is sacrificed.
2. A fixed decorative winter background with an editable foreground logo and
   editable HTML headlines. Replacing the background would require a developer
   to update HTML/CSS/VML, sacrificing no-code hero replacement.

Neither alternative has been selected. Flattening the logo into the hero is not
an approved alternative. CSS absolute positioning alone is not an Outlook solution.

## 2. Editable CTA text and destination

Automatic synchronisation between an editable HTML anchor and a separate VML
button's `href` and text is **not verified**. Duplicated values must not be
advertised as one reliably editable button without evidence.

Preferred implementation to verify: one HTML link within a presentation table,
using email-compatible borders/padding and a solid background, with no separate
VML destination. That removes duplicated editor state. Classic Outlook may show
square corners. Validate the clickable area and wrapping after importing, editing
both the label and destination, and sending to classic Outlook. A table background
alone does not make the entire cell clickable.

If identical rounded geometry across clients requires a separate VML button and
Campaign Monitor cannot synchronise it, the choices are to accept square Outlook
corners with one link, or require developer maintenance of both paths. The latter
does not meet the brief's no-HTML maintenance requirement.

## 3. Template syntax requiring current official confirmation

The following are candidate legacy Campaign Monitor patterns, supplied to define
what must be checked; they are **not currently verified production instructions**:

| Purpose | Candidate syntax | Remaining verification |
| --- | --- | --- |
| Replaceable foreground image | `<img editable="true" label="Header image" src="images/header.png" width="600" alt="Winter campaign artwork">` | Required attributes, unique-region rules, image/link controls, resizing behaviour |
| Single-line copy | `<singleline label="Hero heading">WINTER WRAPPED UP</singleline>` | Allowed nesting, formatting and link editing |
| Rich text / long legal copy | `<multiline label="Offer terms"><p>…</p></multiline>` | Allowed HTML, editor sanitisation and link controls |
| Editable CTA link | An anchor in a supported editable text region | Whether editor preserves button styles and exposes both label and URL; no assumption of a separate generic editable-link tag |
| First name with fallback | `Hi [firstname,fallback=there],` | Exact supported syntax, behaviour with missing/blank values and editor preservation |
| Unsubscribe | `<unsubscribe>Unsubscribe</unsubscribe>` | Custom-template requirements and generated link behaviour |
| Browser version | `<webversion>View online</webversion>` | Supported attributes and generated link behaviour |

Ordinary `contenteditable` is not a substitute for Campaign Monitor template
regions. Account-generated links and personalisation must be tested in an actual
send; an offline HTML renderer cannot establish their behaviour.

## 4. Responsive layout and Outlook constraints

These are engineering constraints to design and test against, not findings from
the inaccessible Campaign Monitor documentation:

- Classic Outlook for Windows uses Word-based rendering. Do not rely on CSS
  absolute positioning, flex/grid, media queries, CSS background images or rounded
  corners as the only implementation. New Outlook and Outlook.com are distinct
  clients and do not replace classic Outlook testing.
- Use presentation tables, explicit image widths, fluid sizing, inline defaults,
  fallback fonts and conditional markup where needed. Media queries can enhance
  mobile rendering; the base layout must remain understandable without them.
- Avoid fixed-height text containers, especially for editable headlines and long
  multi-paragraph terms. Test long CTA labels and narrow screens for wrapping.
- Image replacement can change proportions. Document required aspect ratios and
  test the editor's resize/crop behaviour rather than promising automatic safe
  cropping. Keep essential copy as HTML and meaningful content when images fail.
- VML is a classic Outlook fallback, not proof of editor compatibility. Background
  sizing and any nested VML combinations require real-client testing.

## Next action and build gate

Apply the saved host permissions to the running task through the supported
environment settings/publication flow, or provide the official documentation
as files. Retry both entry points after the runtime policy changes. Read the
editable-image, editable-text/link, personalisation and Outlook/background-image
documentation and record exact article URLs and relevant statements.

Proceed with the build only when the required editor behaviour is supported.
If verification establishes an overlay or CTA editing limitation, obtain a
decision on the concrete alternatives above before implementing a compromise.
No template, placeholder asset package or client-validated preview is complete.


## Proof-of-concept follow-up

Read both review documents from fetched `origin/main` before development. The
existing review above is retained as historical context; the local experiment is
now in [poc/README.md](poc/README.md), with exact import/edit/send acceptance steps.

### Evidence and sources

All five URLs supplied by the user were retried through the configured proxy.
Every request failed with `Tunnel connection failed: 403 Forbidden` before any
article was retrieved:

- https://www.campaignmonitor.com/create/editable-content/
- https://www.campaignmonitor.com/create/
- https://help.campaignmonitor.com/articles/Knowledge/import-custom-coded-email-templates
- https://help.campaignmonitor.com/articles/Knowledge/custom-template-content-editor
- https://help.campaignmonitor.com/articles/Knowledge/email-builder-background-images

The user's supplied documentation summary confirms editable foreground images and
text; that is attributed evidence, not an independently retrieved quotation.
No current source confirms a shared image/VML binding or CTA/VML synchronisation.
Email-builder background-image documentation must not be assumed to describe the
custom-template editor. These URLs are research references, not proof of an
untested behaviour. Personalisation syntax remains pending verification; this
small experiment does not add personalisation or terms sections.

### Independently verified local findings

`poc/check-local.py` executed in installed Chromium at 600, 375 and 320px:

- Two different foreground image assets exist, each with its own editable label.
- The zero-height wrapper visually overlays the logo within the hero bounds at
  each width. Each source can change independently in the local DOM.
- There is exactly one CTA anchor, with the requested initial destination. There
  is no VML button, duplicated CTA destination or background image reference.
- A locally edited long CTA label and destination preserve one anchor and do not
  cause horizontal overflow. The initial button is at least 44px tall.
- Browser screenshots were generated before/after replacements. DOM modification
  is a fixture simulation, not Campaign Monitor editing. Python HTMLParser checks
  selected structural invariants; it is not a full HTML standards validator.

### Unresolved limitations and decision

The foreground overlap avoids background-source synchronisation entirely, but
uses max-height/visible-overflow/stacking behaviour that may fail in classic
Outlook or be changed by Campaign Monitor. It is deliberately experimental.
A layout where the logo becomes a separate row is a failed test, not an approved
fallback. No inference of Outlook support follows from Chromium results.

The CTA uses one styled link inside `multiline`; whether the editor preserves its
styles and exposes convenient link editing is unverified. Its square-corner
Outlook rendering and clickable borders must be inspected in a real received
message. No VML editing capability is claimed. The original candidate syntax table
is not promoted to fully verified status by the local browser checks.

No Campaign Monitor import, editor save/reopen cycle, tracked send, received MIME
inspection or real email-client test has been performed. The test matrix and
alternatives with trade-offs are in `poc/README.md`. Full campaign development
remains gated on these tests or approval of a documented alternative.
