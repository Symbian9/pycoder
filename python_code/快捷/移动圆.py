#巧⑥ㄨ№【天堂】(16982589)

import appuifw,graphics,e32

pos_y=160
pos_x=120
running=1
def quit():
  global running
  running=0
def cn(x):return x.decode('utf8')

#img.rectangle((35,85,85,105),0x000000,fill=0x00ff00)
def move(x,y):
  global pos_y,pos_x
  tpos_y=pos_y
  tpos_x=pos_x
  pos_y+=y
  pos_x+=x
  if pos_y<0 or pos_y>320:
    pos_y=tpos_y
  if pos_x<0 or pos_x>240:
    pos_x=tpos_x
appuifw.app.body=canvas=appuifw.Canvas()
appuifw.app.screen='full'
img=graphics.Image.new(canvas.size)
appuifw.app.exit_key_handler=quit
canvas.bind(63495,lambda: move(-20,0))
canvas.bind(63496,lambda: move(20,0))
canvas.bind(63497,lambda: move(0,-20))
canvas.bind(63498,lambda: move(0,20))
while running:
  img.clear(0xb5d3ff)
  for i in range(1,17):
    img.line((0,20*i,240,20*i),0xaaaaaa,width=2)
  for i in range(1,13):
    img.line((20*i,0,20*i,320),0xaaaaaa,width=2)
  img.point((pos_x,pos_y),0x38ef,width=20)
  canvas.blit(img)
  e32.ao_sleep(.05)
  e32.ao_yield()