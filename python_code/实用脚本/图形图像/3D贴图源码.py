
#3d贴图

#石头 编写

#感谢┈┾夨憶D*.亼ぺ3D教程及末叶苍穹的指导

#ok键     改变缩放

#上下键 左右键、数字键2、8   移动盒子

#在c盘根目录下放a、b、c、d、e、f六张图片(jpg格式的)

import appuifw,e32
from glcanvas import *
from key_codes import *
from graphics import *
from gles import *
from sysinfo import display_pixels

varray=array(GL_BYTE,3,(
    -1,  1,  1,
    1,  1,  1,
    1, -1,  1,
    -1, -1,  1,

    1,  1,  1,
    1,  1, -1,
    1, -1, -1,
    1, -1,  1,

    -1,  1,  1,
    -1,  1, -1,
    1,  1, -1,
    1,  1,  1,

    1, -1,  1,
    1, -1, -1,
    -1, -1, -1,
    -1, -1,  1,

    -1, -1,  1,
    -1, -1, -1,
    -1,  1, -1,
    -1,  1,  1,

    -1,  1, -1,
    1,  1, -1,
    1, -1, -1,
    -1, -1, -1
))

tarrays=(
 (17,16,19,17,19,18),
 (5,4,7,5,7,6),
 (21,22,23,21,23,20),
 (1,0,3,1,3,2),
 (13,12,15,13,15,14),
 (9,8,11,9,11,10)
 )
tarray=array(GL_UNSIGNED_BYTE,3,tarrays)

def texcoord():
 return (127,127),(127,-128),(-128,-128),(-128,127)

tcarray=array(GL_BYTE, 2,((-128,-128),(127,-128),(127,127),(-128,127),texcoord(),texcoord(),texcoord(),texcoord(),texcoord()))

def resize():
 glViewport(0,0,canvas.size[0],canvas.size[1])
 aspect=canvas.size[1]/canvas.size[0]
 glMatrixMode(GL_PROJECTION)
 glFrustumf(-1.0,1.0,-1.0*aspect,1.0*aspect,3.0,1000.0)

def init():
 glClearColor(0.0,0.0,0.0,1.0)
 glBindTexture(GL_TEXTURE_2D,1)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img1.size[0], img1.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img1)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
 glBindTexture(GL_TEXTURE_2D,2)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img2.size[0], img2.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img2)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
 glBindTexture(GL_TEXTURE_2D,3)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img3.size[0], img3.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img3)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )

 glBindTexture(GL_TEXTURE_2D,4)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img4.size[0], img4.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img4)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )

 glBindTexture(GL_TEXTURE_2D,5)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img5.size[0], img5.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img5)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )

 glBindTexture(GL_TEXTURE_2D,6)
 glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,img5.size[0], img5.size[1],0, GL_RGB, GL_UNSIGNED_BYTE,img6)
 glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )

 glVertexPointerb(varray)
 glTexCoordPointerb(tcarray)
 glEnableClientState(GL_VERTEX_ARRAY)
 glEnableClientState( GL_TEXTURE_COORD_ARRAY )
 glEnable(GL_CULL_FACE)
 glEnable(GL_TEXTURE_2D)

mode=0
def scalemode():
 global mode
 if mode==0:mode+=1
 elif mode==1:mode-=1

x=0
def left():
 global x;x-=1
def right():
 global x;x+=1

y=0
def up():
 global y;y+=1
def down():
 global y;y-=1

z=-20
def key_2():
 global z;z+=2
def key_8():
 global z;z-=2

def press():
 canvas.bind(EKey2,lambda:key_2())
 canvas.bind(EKey8,lambda:key_8())

 canvas.bind(EKeyLeftArrow,lambda:left())
 canvas.bind(EKeyRightArrow,lambda:right())

 canvas.bind(EKeyUpArrow,lambda:up())
 canvas.bind(EKeyDownArrow,lambda:down())

 canvas.bind(EKeySelect,lambda:scalemode())

def redraw(a):
 global i
 i+=2
 glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
 if mode==0:
  glMatrixMode(GL_TEXTURE)
  glLoadIdentity()
  glScalef(1.0/255,1.0/255, 1.0)
  glTranslatef(128.0,128.0,1.0 )
 if mode==1:
  glMatrixMode(GL_TEXTURE)
  glLoadIdentity()
  glScalef(2.0/255,2.0/255, 1.0)
  glTranslatef(128.0,128.0,1.0 )
 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()
 glTranslatef(x<<2,y<<2,z<<2)#平移
 glRotatef(i,1.2,1.6,0.4)#旋转
 glScalef(1<<4,1<<4,1<<4)#缩放

 glBindTexture(  GL_TEXTURE_2D,1)
 glDrawElementsub( GL_TRIANGLES,tarrays[0])

 glBindTexture(  GL_TEXTURE_2D,2)
 glDrawElementsub( GL_TRIANGLES,tarrays[1])

 glBindTexture(  GL_TEXTURE_2D,3)
 glDrawElementsub( GL_TRIANGLES,tarrays[2])

 glBindTexture(  GL_TEXTURE_2D,4)
 glDrawElementsub( GL_TRIANGLES,tarrays[3])

 glBindTexture(  GL_TEXTURE_2D,5)
 glDrawElementsub( GL_TRIANGLES,tarrays[4])

 glBindTexture(  GL_TEXTURE_2D,6)
 glDrawElementsub( GL_TRIANGLES,tarrays[5])

def exit():
 global run
 screenshot().save('d:\\3Dimg.jpg')
 run=False

appuifw.app.screen='full'

i=0
run=True
img=Image.new(display_pixels())
canvas=appuifw.Canvas()
appuifw.app.body=canvas
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d.',0xffff00,('normal',20))
canvas.blit(img)
size=(256,256)
imga=Image.open('c:\\a.jpg')
img1=imga.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d..',0xffff00,('normal',20))
canvas.blit(img)
imgb=Image.open('c:\\b.jpg')
img2=imgb.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d...',0xffff00,('normal',20))
canvas.blit(img)
imgc=Image.open('c:\\c.jpg')
img3=imgc.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d.',0xffff00,('normal',20))
canvas.blit(img)
img3.text((40,140),u'3 D \u8d34 \u56fe',0xffff00,('normal',40))
imgd=Image.open('c:\\d.jpg')
img4=imgd.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d..',0xffff00,('normal',20))
canvas.blit(img)
img4.text((40,140),u'\u77f3\u5934\u7f16\u5199',0xffff00,('normal',40))
imge=Image.open('c:\\e.jpg')
img5=imge.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d...',0xffff00,('normal',20))
canvas.blit(img)
imgf=Image.open('c:\\f.jpg')
img6=imgf.resize(size)
img.clear(0)
img.text((40,80),u'\u8f7d\u5165\u4e2d...',0xffff00,('normal',20))
canvas.blit(img)
canvas=GLCanvas(redraw_callback=redraw,event_callback=lambda x:press(),resize_callback=resize)

init()

appuifw.app.body=canvas

appuifw.app.exit_key_handler=exit

while run:
 canvas.drawNow()
 e32.ao_yield()