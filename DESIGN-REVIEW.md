# Winter Wrapped Up — design and compatibility review

## Authoritative references

Visual reference: supplied `Winter Wrapped Up Campaign Email – 1.pdf`, one page,
600 × 3544 pt. Campaign copy and requirements: the development brief in this
conversation. Text in the PDF is reference content, not additional instructions.

## Design observations

- Full-width navy winter artwork, white snow drift at its lower edge, white
  Pinkstones logo at the upper right, and large white campaign title.
- White introduction with dark navy headings, restrained pink underline accents,
  grey body copy and a compact rounded navy CTA.
- Benefits arranged vertically as two rounded navy bars with white headings and
  pink icons at the right. A pink separator sits between them. Supporting copy
  follows on white. The brief requires an explicit editable “OR”.
- Closing message on navy winter artwork with a white rounded CTA.
- Full-width dealership photograph, then a white visit/contact section, social
  links, a thin navy rule and a pale grey postal-address card.
- Grey legal footer. Replace unrelated Toyota vehicle/finance/legal copy with
  this campaign's supplied terms and appropriate sender/unsubscribe information.
- Use approximately 600px desktop width and fluid mobile sizing. Long legal
  copy must flow naturally rather than sit in fixed-height containers.

## Brief takes precedence over reference copy

Use the supplied November 2026 dates, benefit wording and campaign destination.
Keep headlines as editable HTML rather than artwork. Do not introduce vehicle
stock listings. Keep hero and logo as separate replaceable assets. Additional
photography and any footer image assets also need editable image regions.

## Blocking compatibility verification

The selected Option A requires a replaceable hero and a separately replaceable
logo overlaid on it, including classic Outlook for Windows. Before implementing,
verify Campaign Monitor's current editable-image support for background images
and whether one editor operation can update both the standard background and
Outlook VML source. A foreground editable image alone does not establish this.
Absolute positioning alone is insufficient. Flattening assets is prohibited.

Also verify supported editable text/link markup for an Outlook-compatible CTA
so marketing does not have to update duplicate HTML and VML destinations.

Official documentation requests to `www.campaignmonitor.com` and
`help.campaignmonitor.com` were denied by the environment proxy (HTTP 403 CONNECT).
These domains have been saved as additive custom network destinations in the
environment configuration draft; runtime access remains blocked. No conclusion
that the requested overlay is impossible has been established.

Next step: apply documentation access through environment settings, retry the
official documentation, then implement if supported. If verification establishes
that the overlay cannot be maintained through Campaign Monitor's editor, explain
the limitation and obtain approval for the closest supported alternative before
building that alternative. A possible alternative to assess is a separate logo
row above the editable hero; this has not been selected or approved.

## Validation still required

Resumed verification: see [CAMPAIGN-MONITOR-COMPATIBILITY.md](CAMPAIGN-MONITOR-COMPATIBILITY.md)
for the draft/runtime policy mismatch, attempted documentation URLs, proposed
alternatives and the outstanding implementation gates. Access is still denied
by the running proxy; the requested features have not been ruled out.

All template implementation, assets, packaging, desktop/mobile previews and
functional validation remain pending. Local browser previews will not establish
Outlook compatibility or Campaign Monitor editor behaviour. Import/edit tests in
Campaign Monitor and real email-client tests must be reported separately from
local structural and responsive checks.
