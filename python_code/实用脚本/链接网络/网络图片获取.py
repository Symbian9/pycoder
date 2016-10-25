import appuifw,e32,httplib

Conn=httplib.HTTPConnection("10.0.0.172", 80)
Conn.putrequest("GET",图片地址)
Conn.putheader('Accept', '*/*')
Conn.endheaders()
gif = Conn.getresponse().read()
gi=open("e:\\henryczq\\yzm.gif","w")
gi.write(gif)
gi.close()
img=Image.open("e:\\henryczq\\yzm.gif")
def handle_redraw(rect):
  canvas.blit(img)
canvas=appuifw.Canvas(redraw_callback=handle_redraw)
appuifw.app.body=canvas
appuifw.app.screen="normal"

e32.ao_sleep(5)