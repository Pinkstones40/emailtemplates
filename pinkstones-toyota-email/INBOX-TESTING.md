# Campaign Monitor inbox-testing import

This package is ready for template import and rendering tests, not a customer distribution. Extract `campaign-monitor-inbox-testing.zip` first. It contains exactly:

- `email.html` — custom editable template; select this in the HTML upload field.
- `images.zip` — all 13 active PNGs inside `assets/`; select this in the accompanying image/CSS ZIP upload field.
- `INBOX-TESTING.md` — these instructions.

## Import

1. In Campaign Monitor open your profile menu → My templates → Create a template. Use a name such as `Pinkstones Toyota — Fleet — inbox test`.
2. Choose Upload your own HTML. Under HTML page select the extracted `email.html`. Under All other image and CSS files in ZIP format select the extracted `images.zip`.
3. Click Add template. Confirm there are no import errors and all images display. Campaign Monitor imports the relative image assets; verify the received message uses publicly accessible hosted image URLs. There is no separate GitHub image-host setup required for this two-file import.
4. Create a draft campaign, choose Design email → Use a template and select the newly imported template. Do not import `preview.html` or paste browser-preview markup.
5. Configure your authorised From/reply-to address and a clearly identified internal test subject. Use Campaign Monitor's preview/test or inbox-testing feature available in your account and send only to your approved test inboxes.

Official import instructions: https://help.campaignmonitor.com/articles/Knowledge/import-custom-coded-email-templates . Account wording/feature availability may differ.

## What is ready

The template has 41 editable text controls and 13 editable image controls, with one source per image across themes. Native `<unsubscribe>Unsubscribe</unsubscribe>` and `webversion` system tags are outside editable regions. These resolve through Campaign Monitor, not by opening the HTML locally. The current image ZIP includes the seven supplied standalone PNG replacements and the remaining six active artwork assets. Combined supplied graphics stay in the project as reference files, keeping HTML copy and independent links editable.

## Known test-only content

Ten CTA/social/privacy/contact-page destinations intentionally use `https://example.invalid/…` because no approved destinations were provided. Rendering can be tested now, but destination/link checks will report these as broken until edited. Telephone and email links use PDF-supplied details. The greeting still reads `Hello [name],`; it is not configured personalisation. Supplied placeholder prose and the expired/mismatched C-HR finance/insurance footer are preserved for review. Do not interpret this package as approved copy or a deliverability baseline; placeholder content/invalid links can affect content/spam reports.

## Inbox checks

- Check Outlook classic Windows at 100%/125% scaling, new Outlook/Outlook.com, Gmail web/iOS/Android and Apple Mail/iOS Mail, in light/dark modes and with images blocked.
- Check all images, mobile stacking, text contrast, card/icon backgrounds, CTA outlines/padding and footer alignment. Automatic colour inversion requires actual inbox inspection.
- Edit each image and its link/alt, save/reopen, and confirm there is no stale dark-mode image. Check both CTA wording and destination edits retain styling. Social icons are separate image/link controls.
- Check the visible Unsubscribe link and browser-view link in the processed message. Preview/test messages may behave differently from a real campaign; verify subscriber-specific actions using a controlled campaign to a designated internal test subscriber before release. Use only that designated test subscriber when testing unsubscribe.
- Actual Campaign Monitor editor, hosted-image processing, recipient-specific links and email-client rendering have not been exercised by the developer. Browser screenshots are not inbox certification.

Once testing is complete, replace all placeholder copy/URLs, confirm the required disclosures/caveats and obtain marketing/compliance approval before customer distribution. See README for the full issue list.
