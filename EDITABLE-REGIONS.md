# Editable regions — complete email

All regions belong to `winter-wrapped-up.html`, not the historical POC. The latest
brief authorises one hero image incorporating the logo; no separate logo region
or overlay exists. These are implemented custom-template regions. Recognition and
editing in the actual Campaign Monitor account remain to be confirmed by import.

| # | Exact editor label | Mechanism |
| --- | --- | --- |
| 1 | Inbox preview | Heading / single-line copy (`singleline`) |
| 2 | Hero artwork including Pinkstones logo | Editable image (`img editable="true"`) |
| 3 | Hero headline | Heading / single-line copy (`singleline`) |
| 4 | Header snow divider | Editable image (`img editable="true"`) |
| 5 | Personalised greeting | Rich text and links (`multiline`) |
| 6 | Supporting headline | Heading / single-line copy (`singleline`) |
| 7 | Campaign dates | Rich text and links (`multiline`) |
| 8 | Introduction | Rich text and links (`multiline`) |
| 9 | Primary CTA — label and link | Rich text and links (`multiline`) |
| 10 | Benefits section heading | Heading / single-line copy (`singleline`) |
| 11 | Servicing benefit heading | Heading / single-line copy (`singleline`) |
| 12 | Servicing benefit heading icon | Editable image (`img editable="true"`) |
| 13 | Servicing benefit description | Rich text and links (`multiline`) |
| 14 | Benefit choice separator | Heading / single-line copy (`singleline`) |
| 15 | Warranty benefit heading | Heading / single-line copy (`singleline`) |
| 16 | Warranty benefit heading icon | Editable image (`img editable="true"`) |
| 17 | Warranty benefit description | Rich text and links (`multiline`) |
| 18 | Benefit eligibility note | Rich text and links (`multiline`) |
| 19 | Closing headline | Heading / single-line copy (`singleline`) |
| 20 | Closing paragraph one | Rich text and links (`multiline`) |
| 21 | Closing paragraph two | Rich text and links (`multiline`) |
| 22 | Final CTA — label and link | Rich text and links (`multiline`) |
| 23 | Closing offer qualifier | Rich text and links (`multiline`) |
| 24 | Dealership photograph | Editable image (`img editable="true"`) |
| 25 | Visit heading | Heading / single-line copy (`singleline`) |
| 26 | Visit supporting copy | Rich text and links (`multiline`) |
| 27 | Contact telephone icon | Editable image (`img editable="true"`) |
| 28 | Contact telephone | Rich text and links (`multiline`) |
| 29 | Contact website icon | Editable image (`img editable="true"`) |
| 30 | Contact website | Rich text and links (`multiline`) |
| 31 | LinkedIn destination icon | Editable image (`img editable="true"`) |
| 32 | LinkedIn destination | Rich text and links (`multiline`) |
| 33 | TikTok destination icon | Editable image (`img editable="true"`) |
| 34 | TikTok destination | Rich text and links (`multiline`) |
| 35 | Sender business name | Heading / single-line copy (`singleline`) |
| 36 | Sender postal address | Rich text and links (`multiline`) |
| 37 | Sender telephone | Rich text and links (`multiline`) |
| 38 | Terms and conditions heading | Heading / single-line copy (`singleline`) |
| 39 | Offer terms and conditions | Rich text and links (`multiline`) |
| 40 | Full promotional terms link | Rich text and links (`multiline`) |
| 41 | Sender identification | Rich text and links (`multiline`) |
| 42 | Safe sender message | Rich text and links (`multiline`) |
| 43 | Privacy link | Rich text and links (`multiline`) |
| 44 | Copyright | Heading / single-line copy (`singleline`) |

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
- `<unsubscribe>` and `<webversion>` are system-generated links, not ordinary
  marketer-editable destination URLs. They must remain intact. Their labels are
  deliberately stable service text; Campaign Monitor resolves the destinations.
- The hero and snow divider contain no campaign headlines, dates or terms. All
  essential copy appears in the regions listed above. Decorative rules, table
  colours and typography are template styling, not marketing-content regions.

Local source checks verify unique region labels, no nested editable regions,
all nine image controls, all ordinary links inside rich-text regions, and required
content coverage. They do not prove that an account's editor preserves these
controls after saving. Check all 44 regions after import and save/reopen.
