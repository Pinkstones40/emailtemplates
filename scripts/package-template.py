"""Build template + assets ZIP, and a separate image archive for CM's two uploads."""
from pathlib import Path
from html.parser import HTMLParser
from zipfile import ZipFile, ZIP_DEFLATED
ROOT=Path(__file__).resolve().parents[1]
class Images(HTMLParser):
 def __init__(self): super().__init__(); self.paths=[]
 def handle_starttag(self,tag,attrs):
  if tag=='img': self.paths.append(dict(attrs)['src'])
p=Images(); p.feed((ROOT/'winter-wrapped-up.html').read_text())
assert len(p.paths)==len(set(p.paths))
for package,paths in [('winter-wrapped-up-campaign-monitor.zip',['winter-wrapped-up.html']+p.paths),('winter-wrapped-up-images.zip',p.paths)]:
 with ZipFile(ROOT/package,'w',ZIP_DEFLATED) as z:
  for path in paths:
   assert not Path(path).is_absolute() and '..' not in Path(path).parts
   z.write(ROOT/path,path)
 print(package)
