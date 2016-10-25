#巧⑥ㄨ№【天堂】(16982589)

import appuifw,e32
from graphics import Image
from math import pi
runing=1
def quit():
  global runing
  runing=0
def cn(x):return x.decode('utf-8')
appuifw.app.screen='full'
appuifw.app.body=canvas=appuifw.Canvas()
img=Image.new(canvas.size)
def a():
 img.pieslice((20,40,120,120),3*pi/2,pi,0xee0f0f,width=1,fill=0x925909)#pi==π
 img.arc((110,120,170,190),0,3*pi/2,0x0943861,width=2)
appuifw.app.exit_key_handler=quit
while runing:
  img.clear(0x8cbeff)
  a()
  canvas.blit(img)
  e32.ao_sleep(0.1)
  e32.ao_yield()