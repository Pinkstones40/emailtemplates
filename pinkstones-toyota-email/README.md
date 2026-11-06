# Pinkstones Toyota — Fleet introduction

Implemented from the supplied one-page `Fleet email introduction.pdf` (600 × 4339pt). **For design, editor and compliance approval; not cleared for distribution.** No campaign has been imported or sent. The earlier Winter Wrapped Up campaign is untouched.

## Files and preview

- `email.html`: Campaign Monitor custom-template import source.
- `preview.html`: local browser version with editable wrappers removed and inert illustrations of system links.
- `assets/`: 13 independent, campaign-specific PNGs.
- `previews/`: Chromium desktop/mobile light/dark screenshots.
- `PDF-COPY.txt`: complete extracted design text, with typographic ligatures normalised.
- `ASSET-MANIFEST.json`: original artwork extraction/export methods, PDF bounds, dimensions and hashes.
- `STRUCTURE-CHECKS.json`, `BROWSER-CHECKS.json`: local validation evidence.
- `REPOSITORY-REVIEW.md`: technical findings from the preceding campaign.
- `scripts/validate.py`: independent structural/browser checks; Python Playwright and Chromium required. Set `CHROMIUM_PATH` if necessary. Does not exercise Campaign Monitor or send mail.
- `campaign-monitor-import.zip`: HTML at archive root with `assets/` directory.
- `images.zip`: image-only archive for an importer requesting separate files.

Run `python3 -m http.server 8000 --bind 127.0.0.1` inside this folder and open `http://localhost:8000/preview.html`. The preview retains unapproved PDF copy and placeholder destinations intentionally. It is not an approved campaign.

## Editable content

There are **54 uniquely labelled editable controls: 41 text regions and 13 image regions**. Headings use `singleline`; body/benefit copy, legal text, dealership details and all four CTA labels/destinations use `multiline`. Edit the existing CTA anchor using the rich-text link control rather than replacing the whole block. Save/reopen to verify label, destination, clickable padding and styling survive editor sanitisation.

Every image has one foreground `img editable="true"` source, used in both themes. Use its image control to replace artwork, alt text and associated destination. Four social icons are separate editable image/link controls outside editable text and away from the address. Their URLs require confirmation. Test link replacement through the account editor, including save/reopen. No dark-image duplicates, CSS image sources or VML image sources exist. Keep replacement images at the stated proportions and at least the HTML width; the manifest records their native dimensions. No image dimensions use a fixed HTML height.

Toyota Professional identity is extracted from the supplied artwork as part of the hero: replacing it means replacing that hero image. Its white lettering remains over the photograph, rather than over a client-recoloured background. The logo is not invented or redrawn. Icons have opaque source-colour tiles to keep them legible when card backgrounds change. Embedded words in supplied artwork are replaced through image editing, not text controls.

The four benefit blocks remain independently editable rather than repeatable: they are a fixed set of distinct claims, and unrestricted duplication/deletion could obscure associated caveats. No repeaters or unverified template tags have been added.

Native `unsubscribe` and `webversion` tags sit outside editable text and become recipient-specific links only after Campaign Monitor processing. Do not replace them with hardcoded URLs or remove them. Subject, From, reply-to and inbox preview are campaign settings; no unapproved subject/preheader copy is supplied. The literal `Hello [name],` is preserved from the PDF and **must be replaced with approved copy or properly configured/tested personalisation before sending**.

## Import and image hosting — outstanding production step

Use Campaign Monitor's **custom-coded template import**, not a static HTML campaign import or drag-and-drop builder. Import `email.html` with `images.zip`, or use the combined `campaign-monitor-import.zip` if supported by the account upload flow. Preserve `assets/` paths during upload.

The import source intentionally references bundled assets relatively. **Hosting has not been configured or verified. This file is not a sendable standalone production export.** The importer must ingest every PNG and rewrite every image reference to Campaign Monitor-hosted URLs. If the account does not ingest the bundled paths, host the supplied PNGs on an approved public HTTPS host and update all 13 references before reimporting. Do not use localhost, filesystem URLs or development-only hosting. Inspect a Campaign Monitor-processed export/received message and verify all image URLs resolve publicly before distribution. No fabricated image host is used.

Create a new template and draft. Replace every `example.invalid` link: four CTAs, four social destinations, privacy and footer contact page (10 unique destinations). They are deliberately nonfunctional placeholders, not dealership URLs. The PDF supplies no dealership website URL; do not infer one from its email address. Add approved website information through the contact rich-text region if required. Telephone and email links are transcribed from the PDF.

Confirm every text/image control appears; edit each image, alt/link, CTA and longer copy, save, reopen and inspect a test send. Confirm addresses remain intact and image replacements appear in both themes. Review final tracked destinations, unsubscribe, online view and generated plain-text copy. Have marketing and compliance approve the complete message before distribution.

Official syntax references checked during implementation:

- https://www.campaignmonitor.com/create/editable-content/ — singleline, multiline, editable images, image width and link/alt editing; repeater behaviour.
- https://www.campaignmonitor.com/api/v3-3/templates/ — template validation errors, required widths and nested unsubscribe restrictions.
- The previous repository's native unsubscribe/webversion usage is retained. The important-links page was inaccessible through the documentation tool; actual account processing still requires verification.

## PDF fidelity and technical choices

Retained: 600px shell; charcoal canvas; white Toyota Professional branding on the fleet hero; red accents; Dan Newton panel; alternating vehicle photo/text panels; four benefits and original icons; Hilux image; white rectangular CTAs; social row; dealership card; full legal copy and figures.

Differences: fleet/Hilux headings are live HTML below the images, rather than overlays. This avoids duplicate editable background/VML sources and preserves one-source editing and images-off copy. Arial/Helvetica replaces the PDF's embedded Type3 typography, whose licensed web/email font files were not supplied. The team underline is omitted. Natural table heights differ from the fixed artwork, and panels stack in source order on mobile. Mobile images retain their proportions and do not upscale beyond their desktop display widths. Legal copy grows to 13px/19px on mobile. Supported dark mode changes white cards to charcoal with light text; opaque icon tiles remain white. System links occupy clearly separated lines for visibility.

Images are original embedded PNG extractions or 3× exports of original PDF artwork regions without campaign text, not low-resolution screenshots of whole PDF sections. The only campaign branding in the hero comes from the approved PDF. No additional imagery is required for this implementation; optional licensed font files and updated approved artwork can improve fidelity. Original export files are preferable for future art changes. No shared/old campaign assets are referenced.

## Approval issues in supplied copy

1. Introductory, team, feature, benefit and Hilux descriptions are supplied pseudo-Latin placeholder copy; preserved rather than rewritten. Editable labels identify these placeholders. Obtain final approved copy.
2. `[name]` is design placeholder text, not functioning Campaign Monitor personalisation. Confirm subscriber field and fallback or use approved generic greeting.
3. Fleet/Hilux body is followed by C-HR MY25 finance and insurance disclosures. Preserve pending compliance direction; do not assume they are applicable. These include £44,355, £310, 0% APR, 0%–35% deposit and other supplied figures.
4. Supplied finance/insurance windows end in January–June 2026, before the current 6 November 2026 date. Compliance must supply applicable current wording/dates. No dates have been silently updated.
5. Warranty claim `*` appears without a warranty-specific explanation; the footer's `*` refers to a C-HR finance offer. `^` and `^^` also appear without matching main-body claims. Clarify references and preserve approved relationships.
6. The PDF's electric-consumption figure `95.2 miles/kWh`, model description and related performance figures need compliance confirmation. They are preserved as supplied, not verified specifications.
7. The footer's customer-status/consent, no-reply, data-sharing and regulatory statements require sender/compliance approval for this actual campaign. The sentence `help you on you next steps` is preserved as supplied. No company registration details or additional legal statements have been invented.
8. Confirm all ten pending URLs, dealership details, any required website and corporate/regulatory information, and final sender/reply-to settings.

## Validation and remaining client tests

Structural checks pass: balanced HTML stack/table hierarchy, unique editable labels, no nested editable text/images, one system unsubscribe/webversion, all 13 sources independent and present, no scripts/external CSS or old campaign asset dependencies. Chromium tests pass at 800/600/375/320px in both colour schemes: no horizontal overflow, all assets load, all four CTAs are 46px tall, longer CTA/legal copy and deliberately blocked images remain within the viewport. Screenshots were visually reviewed against the PDF; an initial image-mask export issue was corrected by exporting the original icons on their supplied white background.

These are browser checks, **not** Campaign Monitor editor or email-client tests. Dark CSS coordinates text, card surfaces and borders, with Apple data-detector resets, colour-scheme metadata, explicit text fill on dark card/CTA treatments and best-effort Outlook data-ogsc rules. Automatic iOS/Gmail/Outlook inversion can still override colours; media queries cannot guarantee its result.

Before release test received messages in classic Outlook Windows (100%/125% scaling), new Outlook/Outlook.com, Gmail desktop and iOS/Android, Apple Mail and iOS Mail, light/dark, blocked images and narrow screens. Test CTA centre/edges, long edits, image/link edit round trips, tracking, unsubscribe and online view. The source uses tables, inline defaults, explicit widths, MSO width wrapper and Office 96dpi settings; no VML is needed because there are no image backgrounds or rounded buttons. Classic Outlook CTA padding/edge hit areas remain an acceptance test. No client certification or successful editor round trip is claimed.

## Unsubscribe visibility update

The footer now includes a dedicated 16px, bold, underlined **Unsubscribe** link using exactly `<unsubscribe>Unsubscribe</unsubscribe>`, outside all editable regions. Campaign Monitor replaces this system tag with the subscriber-specific anchor when processing the campaign. Import `email.html`, not `preview.html`; the latter uses an inert local demonstration anchor. Reimport the updated template and create a fresh draft if an existing draft retains the older footer. Verify the processed link in a received test campaign before sending.

Official requirements checked: https://www.campaignmonitor.com/create/important/ and https://help.campaignmonitor.com/articles/Knowledge/unsubscribe-links-in-emails . The first confirms the tag must be outside editable regions; the second documents subscriber-specific URL generation. The account’s actual send/unsubscribe flow remains untested here.
