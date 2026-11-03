"""Structural/content/package checks plus Chromium stress tests; not a CM emulator."""
from pathlib import Path
from html.parser import HTMLParser
from zipfile import ZipFile
import json, re, shutil, os, functools, http.server, threading, hashlib, subprocess
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
SRC=(ROOT/'winter-wrapped-up.html').read_text()
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class Structure(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.stack=[]; self.images=[]; self.regions=[]; self.links=[]; self.text=[]; self.editable_images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); parent=self.stack[-1] if self.stack else None
  if tag=='tr': assert parent in ('table','tbody','thead','tfoot'), (tag,parent)
  if tag in ('td','th'): assert parent=='tr', (tag,parent)
  if tag in ('singleline','multiline') or (tag=='img' and 'editable' in a):
   assert a.get('label') and a['label'] not in self.regions
   self.regions.append(a['label'])
   if tag in ('singleline','multiline'):
    assert not any(t in ('singleline','multiline') for t in self.stack), 'Nested editable regions'
  if tag=='img':
   assert 'alt' in a and a.get('width')
   assert not any(t in ('singleline','multiline') for t in self.stack), 'Campaign Monitor forbids images within editable text regions'
   assert (ROOT/a['src']).is_file(); self.images.append(a['src'])
   if 'editable' in a:
    assert a['editable']=='true'; self.editable_images.append(a['src'])
   if 'editable' not in a: assert any(t=='a' for t in self.stack), 'Noneditable image must be linked'
  if tag=='unsubscribe':
   assert not any(t in ('singleline','multiline') for t in self.stack), 'Unsubscribe must be outside editable regions'
  if tag=='a':
   assert any(t in ('singleline','multiline') for t in self.stack) or a.get('class')=='social-icon-link', 'Uneditable ordinary link'
   self.links.append(a['href'])
  if tag not in VOID: self.stack.append(tag)
 def handle_endtag(self,tag):
  assert self.stack and self.stack[-1]==tag, (tag,self.stack[-4:])
  self.stack.pop()
  if tag in ('p','h1','h2','h3','td'): self.text.append(' ')
 def handle_data(self,data):
  self.text.append(data)
  if 'body' in self.stack and data.strip():
   assert any(t in ('singleline','multiline','unsubscribe','webversion') for t in self.stack), ('Uneditable body text',data[:60])
p=Structure(); p.feed(SRC); assert not p.stack
text=' '.join(''.join(p.text).split())
required=[
 'WINTER WRAPPED UP','Prices down. Extras included.','2nd – 30th November 2026',
 'Hi [firstname,fallback=there],',"The temperature isn't the only thing dropping this November!",
 "Our Winter Wrapped Up event has arrived at Pinkstones Used Car Centre, and we've reduced prices across a specially selected range of quality used cars.",
 "Whether you're looking for a practical runaround, a family SUV or simply fancy a change, there's never been a better time to take a look at what's waiting for you.",
 "And because we believe a great deal should come with a little something extra, we've wrapped up two fantastic benefits for you to choose from.",
 'YOUR CAR. YOUR CHOICE.',"2 YEARS' FREE SERVICING*",
 'Enjoy two manufacturer-recommended scheduled services with Pinkstones, helping you keep your next car in great shape without the cost of those services.',
 'OR','12-MONTH EXTENDED WARRANTY^',
 "Enjoy an additional 12 months' warranty cover on top of our standard six-month used car warranty, giving you a total of 18 months' cover for added peace of mind.",
 'A GREAT CAR. A GREAT PRICE. SOMETHING EXTRA.',
 'With reduced prices and your choice of added benefits, Winter Wrapped Up is the perfect opportunity to find your next car for less.',
 "But don't leave your favourite out in the cold! These offers are available on selected used cars until 30th November 2026, and once they're gone, they're gone.",
 'OFFER TERMS & CONDITIONS',
 "Selected used vehicles only. Customers can choose either two years' free servicing with Pinkstones or a 12-month extended warranty. Offers cannot be combined. Promotional period 2nd–30th November 2026. Full terms and conditions apply.",
 'Visit our Used Car Centre','499 Newcastle Road','ST6 6PJ','01782 711661']
for phrase in required: assert phrase in text, phrase
assert SRC.count('BROWSE WINTER WRAPPED UP CARS')==2
assert len(p.images)==15 and len(set(p.images))==15
assert len(p.editable_images)==9, 'Only hero, benefit, dealer and contact image controls should be editable'
assert not any('/facebook' in x or '/linkedin' in x or '/tiktok' in x for x in p.editable_images), 'Fixed social images must not be consumed by Campaign Monitor editor'
assert 'logo-a.png' not in SRC and 'position:absolute' not in SRC and '<v:' not in SRC
assert '<script' not in SRC and 'javascript:' not in SRC
assert SRC.count('<unsubscribe>Unsubscribe</unsubscribe>')==1
assert '<meta name="color-scheme" content="light dark">' in SRC
assert '<meta name="supported-color-schemes" content="light dark">' in SRC
assert '@media (prefers-color-scheme: dark)' in SRC
assert '[data-ogsc]' in SRC
assert 'class="pad dm-intro"' in SRC and 'class="pad dm-benefits"' in SRC
assert 'class="pad dm-visit"' in SRC and 'class="pad legal dm-legal"' in SRC
assert 'color:#df429c' not in SRC, 'Old pink divider/OR treatment unexpectedly present'
assert 'label="Benefit choice separator">OR</singleline>' in SRC
assert 'color:#555961;"><singleline label="Benefit choice separator">' in SRC
assert 'bgcolor="#df429c"' not in SRC, 'Pink divider still present'

assert 'background="images/winter-wrapped-up/background.png"' in SRC
assert "background-image:url('images/winter-wrapped-up/background.png')" in SRC
assert SRC.index('label="Warranty benefit heading"') < SRC.index('label="Servicing benefit description"')
assert SRC.index('label="Servicing benefit description"') < SRC.index('label="Warranty benefit description"')
assert '<webversion ' in SRC and '[First Name]' not in SRC
assert all(f.strip().removesuffix('!important').strip()=='Arial, Helvetica, sans-serif' for f in re.findall(r'font-family:\s*([^;}]+)',SRC))
for unwanted in ['Toyota','MY25','PCP','APR','£44,355']: assert unwanted not in text
assert all(int(h)<=2 for h in re.findall(r'(?:;|")height:\s*(\d+)px',SRC)), 'Fixed text height'
assert all(int(h)<=2 for h in re.findall(r'<td\b[^>]* height="(\d+)"',SRC)), 'Fixed cell height'
# Two CTA anchors and one separate full-terms link share the campaign URL.
assert p.links.count('https://www.pinkstones.uk/winter-wrapped-up')==3
assert len(p.links)==10, p.links
for platform in ('facebook.com','linkedin.com','tiktok.com'):
 assert sum(platform in link for link in p.links)==1, platform
for platform in ('Facebook','LinkedIn','TikTok'):
 assert f'aria-label="{platform}"' in SRC
 assert f'label="{platform} icon link"' not in SRC
 assert f'>{platform}</a>' not in SRC
assert 'outline:1px solid #8292ad' not in SRC
assert '.cta a { display:block; background-color:transparent; padding:14px 18px; border:2px solid #171d36;' in SRC
assert '@media (prefers-color-scheme: light)' in SRC
assert '.dm-intro .cta a { background-color:#171d36 !important; border-color:#171d36 !important; color:#ffffff !important; }' in SRC
assert SRC.count('class="dm-benefit-bar"')==2
assert '<font color="#ffffff"><span class="cta-white-label" style="color:#ffffff !important;text-decoration:none !important;">' in SRC
assert '<span class="cta-primary-label" style="color:#171d36;text-decoration:none;">' in SRC
assert '.dm-intro .cta a .cta-primary-label { color:#ffffff !important; }' in SRC
assert '.cta-light a, .cta-light a span, .cta-light a font { color:#ffffff !important; text-decoration:none !important; }' in SRC
assert SRC.count('<table role="presentation" align="center" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">')==2
assert '.dm-intro .cta a { background-color:transparent !important; border-color:#ffffff !important; color:#ffffff !important; }' in SRC
assert '.cta-light a { background-color:transparent; border-color:#ffffff; color:#ffffff !important; }' in SRC
assert 'background-color:#334b7b !important' not in SRC
assert '<!--[if !mso]><!-->' in SRC and SRC.count('<!--[if !mso]><!-->')==6
assert 'label="Sender postal address"' in SRC
assert '499 Newcastle Road' in SRC and 'Stoke on Trent | ST6 6PJ' in SRC
assert '.light-asset { display:block; }' in SRC
assert '.dark-asset { display:none;' in SRC

manifest=json.loads((ROOT/'ARTWORK-MANIFEST.json').read_text())
assets=[item['path'] for item in manifest['assets']]
dark_assets=['images/winter-wrapped-up/'+name for name in (
 'hero-dark.png','phone-white.png','web-white.png',
 'facebook-white.png','linkedin-white.png','tiktok-white.png')]
assert len(assets)==10 and len(dark_assets)==6
assert set(p.images)==set(assets+dark_assets)-{'images/winter-wrapped-up/background.png'}
for path in dark_assets:
 assert (ROOT/path).is_file() and (ROOT/path).read_bytes().startswith(bytes([137,80,78,71,13,10,26,10])), path

for item in manifest['assets']:
 data=(ROOT/item['path']).read_bytes()
 assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256']
 original=subprocess.check_output(['git','-C',str(ROOT),'show',manifest['source_commit']+':'+item['path']])
 assert data==original, 'Supplied artwork was modified'
assert not re.search(r'(?:src|background)=["\']images/(?!winter-wrapped-up/)',SRC)
assert SRC.count('background="images/winter-wrapped-up/background.png"') == 1, 'Original closing artwork must appear once'
assert 'background-color:#171d36' in SRC, 'Closing needs safe navy fallback'
# Compare every existing editable text region and its link destinations with the
# fetched main snapshot. This protects approved copy even outside the phrase list.
class Copy(HTMLParser):
 def __init__(self): super().__init__(); self.active=None; self.regions={}
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('singleline','multiline'):
   self.active=a['label']; self.regions[self.active]={'text':[],'links':[]}
  if tag=='a' and self.active: self.regions[self.active]['links'].append(a['href'])
 def handle_data(self,data):
  if self.active: self.regions[self.active]['text'].append(data)
 def handle_endtag(self,tag):
  if tag in ('singleline','multiline'): self.active=None
base=Copy(); current=Copy()
base.feed(subprocess.check_output(['git','-C',str(ROOT),'show',manifest['source_commit']+':winter-wrapped-up.html'],text=True))
current.feed(SRC)
removed_social_text={'Facebook destination','LinkedIn destination','TikTok destination'}
for label,content in base.regions.items():
 if label in removed_social_text:
  assert label not in current.regions
  continue
 assert label in current.regions
 assert ' '.join(''.join(content['text']).split())==' '.join(''.join(current.regions[label]['text']).split()), ('Approved copy changed',label)
 assert content['links']==current.regions[label]['links'], ('Approved link changed',label)
for name,expected in [('winter-wrapped-up-campaign-monitor.zip',['winter-wrapped-up.html']+assets+dark_assets),('winter-wrapped-up-images.zip',assets+dark_assets)]:
 with ZipFile(ROOT/name) as z:
  assert z.testzip() is None and sorted(z.namelist())==sorted(expected)
  for item in expected: assert z.read(item)==(ROOT/item).read_bytes()
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
results=[]; (ROOT/'previews').mkdir(exist_ok=True)
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or shutil.which('chromium'))
 for width in (800,600,375,320):
  page=browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
  page.goto(f'http://127.0.0.1:{server.server_port}/winter-wrapped-up.html')
  page.locator('img').evaluate_all('(is)=>Promise.all(is.map(i=>i.decode()))')
  assert page.locator('img').evaluate_all('(is)=>is.every(i=>i.naturalWidth>0)')
  assert page.locator('img').evaluate_all('(is)=>is.every(i=>{let b=i.getBoundingClientRect();return b.width===0 || (b.width<=i.naturalWidth+1 && b.height>0 && Math.abs(b.width/b.height-i.naturalWidth/i.naturalHeight)<0.02)})'), 'Image distortion or enlargement'
  assert page.locator('img.light-asset:visible').count()==6
  assert page.locator('.dark-asset:visible').count()==0
  assert page.locator('img.light-asset').first.get_attribute('src')=='images/winter-wrapped-up/hero.png'
  for social in ('Facebook','LinkedIn','TikTok'):
   assert page.locator(f'a.social-icon-link[aria-label="{social}"]').count()==1
   assert page.locator(f'a.social-icon-link[aria-label="{social}"] img').count()==2
   assert page.locator(f'a.social-icon-link[aria-label="{social}"] img[editable]').count()==0

  assert '499 Newcastle Road' in page.locator('.dm-address').inner_text()
  assert 'ST6 6PJ' in page.locator('.dm-address').inner_text()
  for unwanted_social_text in ('Facebook','LinkedIn','TikTok'):
   assert unwanted_social_text not in page.locator('.dm-address').inner_text()
  assert page.locator('.cta a').first.evaluate('(e)=>getComputedStyle(e).backgroundColor')=='rgb(23, 29, 54)'
  assert page.locator('.cta a').first.evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)'
  assert page.locator('.cta a').first.evaluate('(e)=>getComputedStyle(e).borderTopWidth')=='2px'
  assert page.locator('.cta-primary-label').evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)', ('primary label on navy not white',width)
  assert page.locator('.cta-white-label').evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)', ('closing label not white',width)
  for benefit in page.locator('.dm-benefit-bar').all():
   group=benefit.locator('table[align="center"]')
   assert group.count()==1
   g=group.bounding_box(); b=benefit.bounding_box()
   assert abs((g['x']+g['width']/2)-(b['x']+b['width']/2))<2, ('benefit group not centred',width)
  assert page.locator('unsubscribe').is_visible()
  assert page.locator('unsubscribe').inner_text()=='Unsubscribe'
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), width
  assert page.locator('.shell').bounding_box()['width']<=600
  # Preview fixture only: simulate a missing first name. This does not validate CM.
  page.locator('multiline[label="Personalised greeting"]').evaluate("e=>e.innerHTML=e.innerHTML.replace('[firstname,fallback=there]','there')")
  ctas=page.locator('.cta a'); assert ctas.count()==2
  for a in ctas.all():
   assert a.get_attribute('href')=='https://www.pinkstones.uk/winter-wrapped-up'
   box=a.bounding_box(); assert box['height']>=44
   a.scroll_into_view_if_needed(); box=a.bounding_box()
   for dx,dy in [(2,box['height']/2),(box['width']-2,box['height']/2),(box['width']/2,2),(box['width']/2,box['height']-2)]:
    assert page.evaluate('(p)=>!!document.elementFromPoint(p.x,p.y)?.closest("a")', {'x':box['x']+dx,'y':box['y']+dy})
  # Mimic an email client ignoring all @media rules: transparent primary CTA
  # is the fallback, so Android forced-dark need not invert an inline navy fill.
  page.add_style_tag(content='@media all { }')
  page.evaluate('scrollTo(0,0)')
  page.screenshot(path=str(ROOT/f'previews/email-{width}.png'),full_page=True)
  for a in ctas.all():
   a.evaluate("a=>{a.textContent='BROWSE ALL WINTER WRAPPED UP CARS AND DISCOVER YOUR CHOICE OF BENEFITS';a.href='https://example.com/edited-button';}")
  page.locator('multiline[label="Offer terms and conditions"]').evaluate("e=>{e.innerHTML=Array.from({length:16},(_,i)=>'<p>Legal paragraph '+(i+1)+': '+('Additional detailed eligibility, servicing and warranty conditions. '.repeat(8))+'</p>').join('')}")
  page.locator('singleline[label="Warranty benefit heading"]').evaluate("e=>e.textContent='12-MONTH EXTENDED WARRANTY FOR EXTRA PEACE OF MIND'")
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), ('long text',width)
  for a in ctas.all(): assert a.get_attribute('href')=='https://example.com/edited-button'
  # All generated legal paragraphs must contribute to height and precede the footer.
  legal=page.locator('multiline[label="Offer terms and conditions"]'); assert legal.locator('p').count()==16
  assert legal.bounding_box()['height']>1000
  assert page.locator('unsubscribe').bounding_box()['y']>legal.bounding_box()['y']+legal.bounding_box()['height']
  if width==375: page.screenshot(path=str(ROOT/'previews/email-375-long-text.png'),full_page=True)
  # Missing images and forced unstacked contact entries: ensure text still flows.
  page.locator('img').evaluate_all('(is)=>is.forEach(i=>i.src="data:image/png;base64,invalid")')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.add_style_tag(content='@media screen { .pad{padding-left:40px!important;padding-right:40px!important} .contact-cell{display:table-cell!important;width:auto!important} }')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), ('base-layout',width)
  results.append({'width':width,'initial':'pass','two_cta_border_hit_areas':'pass','long_copy_and_16_legal_paragraphs':'pass','missing_images':'pass','base_layout_contact_row':'pass'})
  page.close()
  # Browser-level OS preference simulation; does not prove email-client support.
  dark=browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1,color_scheme='dark')
  dark.goto(f'http://127.0.0.1:{server.server_port}/winter-wrapped-up.html')
  dark.locator('img').evaluate_all('(is)=>Promise.all(is.map(i=>i.decode()))')
  assert dark.locator('img.light-asset:visible').count()==0, ('light asset in dark view',width)
  assert dark.locator('.dark-asset:visible').count()==6, ('missing dark assets',width)
  assert dark.locator('.dark-asset img').first.get_attribute('src')=='images/winter-wrapped-up/hero-dark.png'
  for button in dark.locator('.cta a').all():
   assert button.evaluate('(e)=>getComputedStyle(e).backgroundColor')=='rgba(0, 0, 0, 0)', ('dark button fill',width)
   assert button.evaluate('(e)=>getComputedStyle(e).borderTopColor')=='rgb(255, 255, 255)', ('dark white border',width)
   assert button.evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)', ('dark white text',width)
  assert dark.locator('.cta-primary-label').evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)', ('dark primary CTA label',width)
  assert dark.locator('.cta-white-label').evaluate('(e)=>getComputedStyle(e).color')=='rgb(255, 255, 255)', ('dark closing CTA label',width)
  assert '499 Newcastle Road' in dark.locator('.dm-address').inner_text()
  dark_bg=dark.locator('.shell').evaluate('(e)=>getComputedStyle(e).backgroundColor')
  assert dark_bg == 'rgb(26, 32, 43)', ('dark shell',width,dark_bg)
  intro_bg=dark.locator('.dm-intro').evaluate('(e)=>getComputedStyle(e).backgroundColor')
  assert intro_bg == 'rgb(26, 32, 43)', ('dark intro',width,intro_bg)
  intro_txt=dark.locator('.dm-intro h1').evaluate('(e)=>getComputedStyle(e).color')
  assert intro_txt == 'rgb(228, 233, 241)', ('dark heading',width,intro_txt)
  legal_bg=dark.locator('.dm-legal').evaluate('(e)=>getComputedStyle(e).backgroundColor')
  assert legal_bg == 'rgb(32, 38, 51)', ('dark legal',width,legal_bg)
  assert dark.evaluate('document.documentElement.scrollWidth<=innerWidth'), ('dark overflow',width)
  assert dark.locator('.cta a').count()==2
  assert dark.locator('.dm-intro .cta a').first.evaluate('(e)=>getComputedStyle(e).color') == 'rgb(255, 255, 255)'
  dark.screenshot(path=str(ROOT/f'previews/email-{width}-dark.png'),full_page=True)
  dark.close()
 browser.close()
server.shutdown()
report={'scope':'Local source/package checks and Chromium; no Campaign Monitor or email-client test', 'editable_regions':len(p.regions),'images':len(p.images),'packaged_original_assets':len(assets),'new_dark_mode_assets':len(dark_assets),'original_asset_hashes':'all ten match fetched main','approved_text_and_links':'all existing text regions match fetched main','font_stack':'Arial, Helvetica, sans-serif','unsubscribe':'exact native tag outside editable regions','content_phrases_checked':len(required),'structural_checks':'passed (strict tag stack including custom tags; not W3C validation)','packages':'passed exact archive membership and bytes','responsive':results,'dark_mode':{'method':'OS media-query browser simulation, not real email-client rendering','widths':[800,600,375,320],'screenshots':'previews/email-{width}-dark.png','status':'passed'}}
(ROOT/'LOCAL-VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
