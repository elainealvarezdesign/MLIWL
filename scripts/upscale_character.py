"""Upscale a small character PNG 4x with Real-ESRGAN (anime 6B model), keeping transparency.

Usage: python3 scripts/upscale_character.py <RealESRGAN_x4plus_anime_6B.pth> <in.png> <out.png>
Needs torch, numpy, Pillow. Model (BSD-3): github.com/xinntao/Real-ESRGAN releases v0.2.2.4.
Used for Kyle, Dante and Danny, whose only art was ~200px tall. Prefer original art when the client has it.
"""
import sys, torch, torch.nn as nn, torch.nn.functional as F, numpy as np
from PIL import Image
class RDB(nn.Module):
    def __init__(s, nf=64, gc=32):
        super().__init__()
        s.conv1=nn.Conv2d(nf,gc,3,1,1); s.conv2=nn.Conv2d(nf+gc,gc,3,1,1); s.conv3=nn.Conv2d(nf+2*gc,gc,3,1,1)
        s.conv4=nn.Conv2d(nf+3*gc,gc,3,1,1); s.conv5=nn.Conv2d(nf+4*gc,nf,3,1,1); s.l=nn.LeakyReLU(0.2,True)
    def forward(s,x):
        x1=s.l(s.conv1(x)); x2=s.l(s.conv2(torch.cat((x,x1),1))); x3=s.l(s.conv3(torch.cat((x,x1,x2),1)))
        x4=s.l(s.conv4(torch.cat((x,x1,x2,x3),1))); x5=s.conv5(torch.cat((x,x1,x2,x3,x4),1)); return x5*0.2+x
class RRDB(nn.Module):
    def __init__(s,nf,gc):
        super().__init__(); s.rdb1=RDB(nf,gc); s.rdb2=RDB(nf,gc); s.rdb3=RDB(nf,gc)
    def forward(s,x): return s.rdb3(s.rdb2(s.rdb1(x)))*0.2+x
class Net(nn.Module):
    def __init__(s,nb=6,nf=64,gc=32):
        super().__init__()
        s.conv_first=nn.Conv2d(3,nf,3,1,1); s.body=nn.Sequential(*[RRDB(nf,gc) for _ in range(nb)]); s.conv_body=nn.Conv2d(nf,nf,3,1,1)
        s.conv_up1=nn.Conv2d(nf,nf,3,1,1); s.conv_up2=nn.Conv2d(nf,nf,3,1,1); s.conv_hr=nn.Conv2d(nf,nf,3,1,1); s.conv_last=nn.Conv2d(nf,3,3,1,1); s.l=nn.LeakyReLU(0.2,True)
    def forward(s,x):
        f=s.conv_first(x); f=f+s.conv_body(s.body(f))
        f=s.l(s.conv_up1(F.interpolate(f,scale_factor=2,mode='nearest'))); f=s.l(s.conv_up2(F.interpolate(f,scale_factor=2,mode='nearest')))
        return s.conv_last(s.l(s.conv_hr(f)))
net=Net(); sd=torch.load(sys.argv[1],map_location='cpu'); net.load_state_dict(sd.get('params_ema',sd.get('params',sd))); net.eval()
def up(rgb):
    t=torch.from_numpy(np.asarray(rgb,dtype=np.float32)/255).permute(2,0,1)[None]
    with torch.no_grad(): o=net(t).clamp(0,1)[0].permute(1,2,0).numpy()
    return Image.fromarray((o*255).round().astype(np.uint8))
src,dst=sys.argv[2],sys.argv[3]
im=Image.open(src).convert('RGBA'); im=im.crop(im.getbbox())
pad=8; big=Image.new('RGBA',(im.width+2*pad,im.height+2*pad),(0,0,0,0)); big.paste(im,(pad,pad))
a=big.getchannel('A')
# colour edge pixels into transparent area so edges don't fade to black

from PIL import ImageFilter
bleed=big.convert('RGB')
for _ in range(6):
    m=Image.fromarray((np.asarray(a)>0).astype(np.uint8)*255)
    grown=bleed.filter(ImageFilter.MaxFilter(3))
    bleed=Image.composite(bleed,grown,m); a2=a.filter(ImageFilter.MaxFilter(3)); a=a2
rgb_up=up(bleed)
al=up(Image.merge('RGB',[big.getchannel('A')]*3)).getchannel('G')
out=rgb_up.convert('RGBA'); out.putalpha(al)
out=out.crop(out.getchannel('A').point(lambda v:255 if v>8 else 0).getbbox())
out.save(dst); print(dst, out.size)
