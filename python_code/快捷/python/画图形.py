import appuifw,e32
from graphics import Image

def cn(x):return x.decode('utf-8')
appuifw.app.screen='full'
appuifw.app.body=canvas=appuifw.Canvas()
#设定程序界面主体为画布

img=Image.new((210,280))
#创建一张大小为210×280的图像
img.clear(0)
#用黑色覆盖图像，最后那个数为颜色代码

img.text((45,250),cn('石工七班很强！'),0xffff00,u'')
#写字，最后缺省的一项是字体
img.point((20,25),0xff0000,width=35,fill=0xff0000)
#画圆
img.polygon((10,240,10,160,60,200),0x0000ff,width=1.5,fill=0xff00ee)
#画三角形
img.rectangle((5,70,50,120),0x004000,width=0.6,fill=0x00ff00)
#画矩形
img.line((70,220,70,80,160,10),0xaa00ee,width=5)
#画线段
img.ellipse((90,140,200,180),0xffff00,width=1,fill=0x3ff3e9)
#画椭圆
img.pieslice((110,70,180,120),0,1.8,0xee0f0f,width=1,fill=0x925909)
#画扇形
img.arc((130,200,180,260),-0.5,2.5,0x0943861,width=2)
#画弧线
def redraw(rect):
    canvas.blit(img)
    #将上面画好的图复制到画布上面
redraw(())#连续重复执行redraw函数，使系统重复将img画在画布上

e32.Ao_lock().wait()

#字体可通过
#import appuifw
#fonts=appuifw.avail_fonts()
#获得手机可用字体。

#img.rectangle((5,70,50,120),0x004000,width=0.6,fill=0x00ff00)
#(5,70,50,120)是矩形左上角和右下角坐标，0x004000是边框颜色，width是边框粗细，fill是填充颜色
