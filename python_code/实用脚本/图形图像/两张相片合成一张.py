"""草根作品"""
"""草虽渺小，根系天下"""
"""qq476116973"""
"""转注草根"""
import appuifw,graphics,e32
run=1
def exit():
  appuifw.note("草根\n草虽渺小，根系天下".decode("u8"))
  global run
  run=0
appuifw.app.body=m=appuifw.Canvas()
appuifw.app.screen='full'
m.clear(0)
if appuifw.query("一定要打开两张图片才能显示效果\n图片较大请耐心等待\n草根".decode("u8"),"query"):
  import powlite_fm
  path=powlite_fm.manager().AskUser("e:\\",ext=[".png",".jpg"])
  path1=powlite_fm.manager().AskUser("e:\\",ext=[".png",".jpg"])
img=graphics.Image.open(path).resize((240,320))
img1=graphics.Image.open(path1).resize((240,320))
appuifw.app.exit_key_handler=exit
wy,wy1=0,1
while run:
  a=img.getpixel([(x,wy)for x in xrange(240)])
  b=img1.getpixel([(x,wy)for x in xrange(240)])
  for i in xrange(240):
        m.point((i,wy),a[i])
        m.point((i,wy1),b[i])
  wy+=2
  wy1+=2
  if wy==320:pass
  if wy==320:pass
  e32.ao_yield()
graphics.screenshot().save("e:\\10.jpg")
