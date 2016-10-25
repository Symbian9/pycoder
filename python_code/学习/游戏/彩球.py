import appuifw,graphics,e32
ziti=appuifw.app.body.font
run=1
def exit():
  global run
  run=0
def cn(x):
  return x.decode('utf8')
appuifw.app.body=m=appuifw.Canvas()
appuifw.app.screen='full'
p,q=m.size
x,y=30,30
while run:
  img=graphics.Image.new(m.size)
  if x<=30:b=1
  if x>=p-30:b=-1
  if y<=30:a=1
  if y>=q-30:a=-1
  y+=a
  x+=b
  img.clear(0)#((x-30,p-30-x,0))
  for i in range(30):
      img.point((x-i/2,y-i/2),(i*8,i*8,x-x/8),width=60-2*i)
  for i in range(4):
    img.text((p-60-i,y+15-i),cn("草根"),(255-i*60,p-i*60,0),(ziti[0],28,50))
  img.text((p-59,y+16),cn("草根"),(255,255,0),(ziti[0],28,50))
  m.blit(img)
  e32.ao_sleep(0)
  appuifw.app.exit_key_handler=exit
