from akntextutils import wrap_text_to_array
import appuifw,e32
def cn(x):return x.decode("utf-8")
appuifw.app.body=canvas=appuifw.Canvas( )
lines = wrap_text_to_array(cn("这是使用了帖子中介绍的方法后的效果。文字自动分句显示了。"), "dense", 220)
#其中220表示每句话的长度，达到该值后即换行
x, y = 10, 10
#设定文字开始的坐标为(10,10)
for line in lines:
  y += 15
#这里是换行时改变的距离，数值过小会导致文字重叠，你也可以改变x或者同时改变x,y以实现不同效果
  canvas.text((x, y), line, font="dense")
  canvas.text((10, 100),cn("这是未使用帖子中介绍的方法的效果。"), font="dense")
e32.Ao_lock().wait()