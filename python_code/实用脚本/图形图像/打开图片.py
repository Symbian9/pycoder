import appuifw, e32, graphics
def cn(x):return x.decode('utf-8')
img=graphics.Image.open("E:\\image.jpg")
def handle_redraw(rect):
    canvas.blit(img)
canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
Appuifw.app.body=canvas

e32.Ao_lock().wait()