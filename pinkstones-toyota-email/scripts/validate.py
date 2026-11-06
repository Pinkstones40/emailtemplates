from pathlib import Path
from playwright.sync_api import sync_playwright
import json, threading, http.server, functools, os
R=Path(__file__).resolve().parents[1]
server=http.server.ThreadingHTTPServer(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(R)))
threading.Thread(target=server.serve_forever,daemon=True).start()
(R/'previews').mkdir(exist_ok=True)
from html.parser import HTMLParser
class Validate(HTMLParser):
 def __init__(self):
  super().__init__(); self.stack=[]; self.labels=[]; self.images=[]; self.links=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='tr': assert self.stack[-1] in ('table','tbody')
  if t=='td': assert self.stack[-1]=='tr'
  if t in ('singleline','multiline') or (t=='img' and 'editable' in a):
   assert a.get('label') and a['label'] not in self.labels;self.labels.append(a['label'])
   assert not any(x in ('singleline','multiline') for x in self.stack)
  if t=='img':
   assert 'editable' in a and a.get('width') and a.get('alt');assert (R/a['src']).is_file();self.images.append(a['src'])
  if t in ('unsubscribe','webversion'):assert not any(x in ('singleline','multiline') for x in self.stack)
  if t=='a':self.links.append(a['href'])
  assert t not in ('script','link')
  if t not in ('img','meta','br','hr','input'):self.stack.append(t)
 def handle_endtag(self,t):
  assert self.stack and self.stack[-1]==t,(t,self.stack[-5:]);self.stack.pop()
source=(R/'email.html').read_text();v=Validate();v.feed(source);assert not v.stack
assert len(v.images)==len(set(v.images))==13
assert source.count('<unsubscribe>Unsubscribe</unsubscribe>')==1 and source.count('<webversion ')==1
assert not any(x in source for x in ['winter-wrapped-up/','localhost','file://','<v:'])
(R/'STRUCTURE-CHECKS.json').write_text(json.dumps({'editable_regions':len(v.labels),'editable_images':len(v.images),'single_image_sources':True,'pending_urls':sorted(set(u for u in v.links if 'example.invalid' in u))},indent=2))
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),args=['--no-sandbox'])
 for theme in ['light','dark']:
  for width in [800,600,375,320]:
   page=b.new_page(viewport={'width':width,'height':900},color_scheme=theme,device_scale_factor=1)
   page.goto(f'http://127.0.0.1:{server.server_port}/preview.html');page.screenshot(path=str(R/f'previews/{width}-{theme}.png'),full_page=True)
   result=page.evaluate('''() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,broken:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),buttons:[...document.querySelectorAll('.cta a')].map(a=>({height:a.getBoundingClientRect().height,width:a.getBoundingClientRect().width}))})''')
   assert result['scroll']<=width,result
   assert not result['broken'],result
   unsubscribe=page.locator('.unsubscribe-link a')
   assert unsubscribe.count()==1 and unsubscribe.is_visible()
   assert unsubscribe.inner_text()=='Unsubscribe'
   assert float(unsubscribe.evaluate("a=>getComputedStyle(a).fontSize").replace('px',''))>=16
   assert all(a['height']>=44 for a in result['buttons']),result
   # Stress long editable content and image blocking at each width/theme.
   page.evaluate("""() => {document.querySelector('.cta a').textContent='A much longer call to action for business vehicle enquiries';document.querySelector('.legal p').textContent+=' Additional copy for layout stress.'.repeat(50);document.querySelectorAll('img').forEach(i=>i.src='/missing-test-image.png')}""")
   page.wait_for_timeout(100)
   stress=page.evaluate('document.documentElement.scrollWidth')
   assert stress<=width,('stress overflow',width,stress)
   results.append({'theme':theme,**result,'long_copy_and_blocked_images_no_overflow':True});page.close()
 b.close()
(R/'BROWSER-CHECKS.json').write_text(json.dumps(results,indent=2));print(json.dumps(results))
