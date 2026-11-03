"""Local Chromium experiment only. Does not emulate Campaign Monitor or Outlook."""
from pathlib import Path
from html.parser import HTMLParser
import json
import os
import shutil
import functools
import http.server
import threading
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent
class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.images=[]; self.links=[]; self.edit=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='img': self.images.append(a)
        if tag=='a': self.links.append(a)
        if tag in ('singleline','multiline'): self.edit.append(a['label'])
src=(ROOT/'overlay-and-cta.html').read_text()
p=Inspect(); p.feed(src)
assert len(p.images)==2 and all(i.get('editable')=='true' for i in p.images)
assert len({i['src'] for i in p.images})==2
assert len(p.links)==1 and p.links[0]['href']=='https://www.pinkstones.uk/winter-wrapped-up'
assert '<v:' not in src and 'background-image' not in src
assert len(p.edit)==4 and '<unsubscribe>' in src
assert '2nd – 30th November 2026' in src
for i in p.images: assert (ROOT/i['src']).is_file()
results=[]
handler=functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
server=http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or shutil.which("chromium"))
    for width in (600,375,320):
        page=browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
        page.goto(f'http://127.0.0.1:{server.server_port}/overlay-and-cta.html')
        page.locator('img').evaluate_all('(imgs)=>Promise.all(imgs.map(i=>i.decode()))')
        hero=page.locator('img').nth(1).bounding_box(); logo=page.locator('img').nth(0).bounding_box()
        assert logo['x']>=hero['x'] and logo['y']>=hero['y']
        assert logo['x']+logo['width']<=hero['x']+hero['width']
        assert logo['y']+logo['height']<=hero['y']+hero['height']
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        link=page.locator('a'); assert link.bounding_box()['height']>=44
        box=link.bounding_box()
        for dx,dy in [(2,box['height']/2),(box['width']-2,box['height']/2),(box['width']/2,2),(box['width']/2,box['height']-2)]:
            assert page.evaluate('(p)=>document.elementFromPoint(p.x,p.y).closest("a") !== null', {'x':box['x']+dx,'y':box['y']+dy})
        page.screenshot(path=str(ROOT/f'previews/chromium-{width}.png'),full_page=True)
        # Simulate replacement locally; this is not an editor round trip.
        original_logo=page.locator('img').nth(0).get_attribute('src')
        page.locator('img').nth(1).evaluate("i=>i.src='images/hero-b.png'")
        assert page.locator('img').nth(0).get_attribute('src')==original_logo
        page.locator('img').nth(0).evaluate("i=>i.src='images/logo-b.png'")
        assert page.locator('img').nth(1).get_attribute('src')=='images/hero-b.png'
        link.evaluate("a=>{a.textContent='EXPLORE ALL WINTER WRAPPED UP OFFERS AND CHOOSE YOUR NEXT CAR';a.href='https://example.com/edited-cta';}")
        assert page.locator('a').count()==1 and link.get_attribute('href')=='https://example.com/edited-cta'
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        page.locator('img').evaluate_all('(imgs)=>Promise.all(imgs.map(i=>i.decode()))')
        page.screenshot(path=str(ROOT/f'previews/chromium-{width}-replaced.png'),full_page=True)
        results.append({'width':width,'overlay_geometry':'pass','horizontal_overflow':'none','single_link_and_long_label':'pass','local_independent_src_changes':'pass'})
        page.close()
    browser.close()
server.shutdown()
report=json.dumps({'renderer':'Chromium (not Outlook or Campaign Monitor)','checks':results},indent=2)
(ROOT/'LOCAL-RESULTS.json').write_text(report+'\n')
print(report)
