"""Generate clearly labelled designer placeholders; no final campaign artwork."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'images'; OUT.mkdir(exist_ok=True)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def f(n): return ImageFont.truetype(FONT,n)
NAVY='#171d36'; PINK='#df429c'
def snow(d,x,y,r,color):
    for a in (0,math.pi/3,2*math.pi/3):
        dx,dy=math.cos(a)*r,math.sin(a)*r
        d.line((x-dx,y-dy,x+dx,y+dy),fill=color,width=2)
im=Image.new('RGB',(1200,260),NAVY); d=ImageDraw.Draw(im)
for x in range(30,1200,90):
 for y in range(25,260,85): snow(d,x,y,11+(x%3)*4,'#303a57')
d.text((810,48),'PINKSTONES',font=f(40),fill='white')
d.text((812,100),'USED CAR CENTRE',font=f(17),fill='white')
d.text((40,194),'HERO ARTWORK PLACEHOLDER',font=f(17),fill='#b8c2d8')
im.save(OUT/'hero-with-logo.png',optimize=True)
im=Image.new('RGB',(1200,120),NAVY); d=ImageDraw.Draw(im)
points=[(0,120),(0,48)]+[(x,int(46+20*math.sin(x/150))) for x in range(0,1201,5)]+[(1200,120)]
d.polygon(points,fill='#eff3f6'); d.rectangle((0,90,1200,120),fill='white')
im.save(OUT/'snow-divider.png',optimize=True)
for name in ['servicing','warranty']:
 im=Image.new('RGBA',(200,200),(0,0,0,0)); d=ImageDraw.Draw(im)
 if name=='servicing':
  d.line((48,150,143,55),fill=PINK,width=19); d.ellipse((110,20,175,85),outline=PINK,width=12)
  d.ellipse((28,135,68,175),outline=PINK,width=10)
 else:
  d.polygon([(100,20),(162,45),(155,115),(135,146),(100,174),(65,146),(45,115),(38,45)],outline=PINK,width=9)
  d.line((65,97,90,122,137,69),fill=PINK,width=11)
 im.save(OUT/f'{name}-icon.png',optimize=True)
im=Image.new('RGB',(1200,720),'#d6dce1'); d=ImageDraw.Draw(im)
d.rectangle((0,420,1200,720),fill='#bbc4cc')
d.rectangle((40,155,650,420),fill='#8796a3'); d.rectangle((65,180,625,345),fill='#e8edf0')
for x in range(55,1150,190):
 d.rounded_rectangle((x,440,x+160,530),radius=15,fill=NAVY)
 d.rectangle((x+25,410,x+135,460),fill='#f7fafc')
 d.ellipse((x+15,505,x+50,540),fill='#59646d'); d.ellipse((x+110,505,x+145,540),fill='#59646d')
d.rectangle((160,50,1040,123),fill='white')
d.text((195,68),'DEALERSHIP PHOTO PLACEHOLDER',font=f(32),fill=NAVY)
d.text((255,622),'Replace with approved site photography',font=f(28),fill=NAVY)
im.save(OUT/'dealership.jpg',quality=88,optimize=True)
for name in ['phone','website','linkedin','tiktok']:
 im=Image.new('RGBA',(80,80),(0,0,0,0)); d=ImageDraw.Draw(im)
 if name in ('linkedin','tiktok'):
  d.ellipse((2,2,78,78),fill=NAVY)
  d.text((18 if name=='linkedin' else 26,14),'in' if name=='linkedin' else '♪',font=f(38),fill='white')
 elif name=='website':
  d.ellipse((10,10,70,70),outline=NAVY,width=4); d.ellipse((27,10,53,70),outline=NAVY,width=3)
  d.line((10,40,70,40),fill=NAVY,width=3); d.line((15,25,65,25),fill=NAVY,width=2); d.line((15,55,65,55),fill=NAVY,width=2)
 else:
  d.arc((16,8,70,66),80,195,fill=NAVY,width=15)
  d.rounded_rectangle((10,12,26,32),radius=4,fill=NAVY); d.rounded_rectangle((48,52,67,69),radius=4,fill=NAVY)
 im.save(OUT/f'{name}-icon.png',optimize=True)
print('Generated',len(list(OUT.iterdir())),'separate image assets')
