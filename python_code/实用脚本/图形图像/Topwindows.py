#这节主要讲讲TopWindow(顶部窗口)也就是大家常说的随显，其实这只是它的一种用途而已#由于TopWindow可以和图形界面结合使用，所以特讲此节
#先来看看TopWindow模块的方法(函数)吧
#(1)TopWindow()实例化,返回一个TopWindow对象，这个不用具体理解#可以简单的认为:比如 w=TopWindow()，这样后我们可以用w.method()来操作了#方法不多，有下面几个
#(2)show()显示窗口，当这个函数被调用时，窗口会被显示出来
#(3)hide()隐藏窗口
#(4)add_image(image,position)#image可以是前面教程中的图片或者绘制的图形#position形式为(x1,y1[,x2,y2])这个参数的意义为image被添加到TopWindow的位置#如果只给出前两个参数(后两个参数可选)，那么image不会被缩放，如果给出四个那么image会被缩放至给定坐标大小(具体效果自测)
#(5)remove_image(image[,position])上个函数的反向操作 移除image
#(6)方法就这么多，再看看有哪些属性position,size,shadow,corner_type,background_color#position,指定窗口(左上角)在屏幕上的位置，例如w.position=(0,0)#size,指定窗口的大小，例如w.size=(176,208)#shadow,有无阴影，例如w.shadow=5#corner_type,顶角类型，如w.corner_type=’square’(方形)，此外还有corner1,corner2,corner3,corner5##background_color,TopWindow背景颜色,例如w.background_color=0xffffff(白色)#常用的也就这么多了，具体效果自己尝试吧#下面讲课程代码


#-*-coding:utf-8-*-
import appuifw,graphics,e32
import TopWindow

def chn(x):return x.decode('utf8')

canvas=appuifw.Canvas()
appuifw.app.body=canvas
appuifw.app.screen='full'
#新建图像
image=graphics.Image.new(canvas.size)
#实例化窗口对象(记住有这句就行了)
w=TopWindow.TopWindow()
#把image设置成黑色
image.clear(0)
#画文本
image.text((10,15),chn('iniwap教程系列'),fill=0x0000ff)
#画矩形
image.rectangle((10,15,20,30),outline=0x0000ff)
#你还可以画更多在这里#添加image到TopWindow,位置为(0,0)
w.add_image(image,(0,0))
#窗口大小宽160，高135
w.size=(160,135)
#设置窗口在屏幕的位置
w.position=(5,45)
#阴影值为5
w.shadow=5
#顶角类型corner5
w.corner_type='corner5'
#显示窗口
w.show()
#w.hide()