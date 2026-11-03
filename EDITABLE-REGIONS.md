# Editable regions — complete email

All regions belong to `winter-wrapped-up.html`, not the historical POC. The latest
brief authorises one hero image incorporating the logo; no separate logo region
or overlay exists. These are implemented custom-template regions. Recognition and
editing in the actual Campaign Monitor account remain to be confirmed by import.

| # | Exact editor label | Mechanism |
| --- | --- | --- |
| 1 | Inbox preview | Heading / single-line copy (`singleline`) |
| 2 | Hero artwork including Pinkstones logo | Editable image (`img editable="true"`) |
| 3 | Personalised greeting | Rich text and links (`multiline`) |
| 4 | Hero headline | Heading / single-line copy (`singleline`) |
| 5 | Supporting headline | Heading / single-line copy (`singleline`) |
| 6 | Campaign dates | Rich text and links (`multiline`) |
| 7 | Introduction | Rich text and links (`multiline`) |
| 8 | Primary CTA — label and link | Rich text and links (`multiline`) |
| 9 | Benefits section heading | Heading / single-line copy (`singleline`) |
| 10 | Servicing benefit heading | Heading / single-line copy (`singleline`) |
| 11 | Servicing benefit heading icon | Editable image (`img editable="true"`) |
| 12 | Servicing benefit description | Rich text and links (`multiline`) |
| 13 | Benefit choice separator | Heading / single-line copy (`singleline`) |
| 14 | Warranty benefit heading | Heading / single-line copy (`singleline`) |
| 15 | Warranty benefit heading icon | Editable image (`img editable="true"`) |
| 16 | Warranty benefit description | Rich text and links (`multiline`) |
| 17 | Benefit eligibility note | Rich text and links (`multiline`) |
| 18 | Closing headline | Heading / single-line copy (`singleline`) |
| 19 | Closing paragraph one | Rich text and links (`multiline`) |
| 20 | Closing paragraph two | Rich text and links (`multiline`) |
| 21 | Final CTA — label and link | Rich text and links (`multiline`) |
| 22 | Closing offer qualifier | Rich text and links (`multiline`) |
| 23 | Dealership photograph | Editable image (`img editable="true"`) |
| 24 | Visit heading | Heading / single-line copy (`singleline`) |
| 25 | Visit supporting copy | Rich text and links (`multiline`) |
| 26 | Contact telephone icon | Editable image (`img editable="true"`) |
| 27 | Contact telephone | Rich text and links (`multiline`) |
| 28 | Contact website icon | Editable image (`img editable="true"`) |
| 29 | Contact website | Rich text and links (`multiline`) |
| 30 | Facebook destination icon | Editable image (`img editable="true"`) |
| 31 | Facebook destination | Rich text and links (`multiline`) |
| 32 | LinkedIn destination icon | Editable image (`img editable="true"`) |
| 33 | LinkedIn destination | Rich text and links (`multiline`) |
| 34 | TikTok destination icon | Editable image (`img editable="true"`) |
| 35 | TikTok destination | Rich text and links (`multiline`) |
| 36 | Sender business name | Heading / single-line copy (`singleline`) |
| 37 | Sender postal address | Rich text and links (`multiline`) |
| 38 | Sender telephone | Rich text and links (`multiline`) |
| 39 | Terms and conditions heading | Heading / single-line copy (`singleline`) |
| 40 | Offer terms and conditions | Rich text and links (`multiline`) |
| 41 | Full promotional terms link | Rich text and links (`multiline`) |
| 42 | Sender identification | Rich text and links (`multiline`) |
| 43 | Safe sender message | Rich text and links (`multiline`) |
| 44 | Privacy link | Rich text and links (`multiline`) |
| 45 | Copyright | Heading / single-line copy (`singleline`) |

## Link editing and system tags

- Each CTA is a **separate `multiline` region containing one styled anchor**.
  Both its label and destination can be edited by selecting the existing link in
  the rich-text editor. There is no VML duplicate. See README for exact steps and
  the correction procedure if the editor changes formatting.
- Contact telephone, website, social destinations, sender telephone, full terms
  and privacy regions each contain editable HTML links. Select text and use the
  editor's link control. Icon assets are separately replaceable and do not carry
  fixed hidden social URLs. Confirm the currently generic social/privacy targets.
- `Personalised greeting` contains `Hi [firstname,fallback=there],`; preserve the
  token or use Campaign Monitor's personalisation control. Rendering requires a
  Campaign Monitor send; local screenshots only simulate the fallback.
- `Inbox preview` is hidden in the message and may not be selectable in the visual
  editor. Campaign settings provide the final subject/preview; see README for the
  hidden-default limitation. It is implemented with a labelled `singleline`.
- `<unsubscribe>Unsubscribe</unsubscribe>` and `<webversion>` are system-generated links, not ordinary
  marketer-editable destination URLs. They must remain intact, outside editable regions. Their labels are
  deliberately stable service text; Campaign Monitor resolves the destinations.
- The original hero contains the campaign headline as supplied image pixels;
  the entire image is replaceable. The preserved `Hero headline` HTML region is
  now in the introduction, so the campaign title remains editable and readable
  with images blocked. Editing this region does not change words inside the PNG.
  There is no separate snow-divider region. Dates, descriptions, CTA labels and
  legal copy remain editable HTML. Decorative rules, table
  colours and typography are template styling, not marketing-content regions.

Local source checks verify unique region labels, no nested editable regions,
all fifteen image controls, all ordinary links inside rich-text regions, and required
content coverage. They do not prove that an account's editor preserves these
controls after saving. Check every labelled region and both variants of the six image pairs after import and save/reopen.


The current template contains nine default/light foreground images, six additional dark-mode variants, and the original fixed closing background. Hero, phone, web and social icons are labelled separately for the light and dark variants. Facebook, LinkedIn and TikTok visible text labels have been removed: each network now has one clickable `<a>` wrapping the two separately editable images. There is **no enclosing `<multiline>`**, which Campaign Monitor prohibits for editable images. Each icon's image-edit controls may offer a destination URL, but the editor must be tested to ensure light/dark destinations stay synchronised. Validate the two image controls and the icon link in Campaign Monitor before live use. The dark counterpart may not be directly selectable in its visual editor when hidden; if that happens, amend the custom template source rather than assuming no-code edits are supported.

## New image variant controls

- Hero artwork including Pinkstones logo — light mode / dark mode
- Contact telephone icon — light mode / dark mode
- Contact website icon — light mode / dark mode
- Facebook destination icon — light mode / dark mode; one anchor around both images
- LinkedIn destination icon — light mode / dark mode; one anchor around both images
- TikTok destination icon — light mode / dark mode; one anchor around both images

The old **Facebook destination**, **LinkedIn destination**, and **TikTok destination** text regions were intentionally removed. The three links are embedded in HTML around image controls; Campaign Monitor's editable image interface offers URL options, but actual paired-image link edits must be validated after saving.

## Amendment: Campaign Monitor-safe footer (3 November 2026)

To prevent Campaign Monitor moving social text/metadata into the address region, the Facebook/LinkedIn/TikTok icons are now **static template assets within fixed linked HTML**, rather than six editable image controls. The visible labels stay removed. Updating social destinations or icons requires modifying this source template and reimporting; this is intentional until a stable editable-social-image implementation has been demonstrated in Campaign Monitor. Phone, website, both hero variants and other foreground artwork remain editable. The sender business, postal address, and telephone stay in independent, labelled text regions in their own address card.
