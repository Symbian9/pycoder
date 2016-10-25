import appuifw,graphics,e32
img=graphics.Image.open('e:\\pd.png')
img.rectangle((0,10,18,18),0x0000ff,fill=0x0000ff)
def redraw(rect):
  for x in range(0,176,18):
    for y in range(0,208,18):
      ca.blit(img,target=(x,y))
    e32.ao_sleep(.5)
  e32.ao_sleep(.5)
appuifw.app.body=ca=appuifw.Canvas()
redraw(())

e32.ao_sleep(5)