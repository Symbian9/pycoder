#来完成一个三维曲线的绘制，并旋转它。
import appuifw, key_codes,graphics,e32,math
import glcanvas
from gles import *
angle,running,turning_axis =0.0,1,0
#点坐标列表
vertice=[]
#顶点列表
points = array(GL_UNSIGNED_BYTE,1,[i for i in range(300)])
#下面的函数几乎可以固定
def reshape():#回调定义投影变换
    glViewport(0, 0, 240, 320)#设置视口
    aspect = 4/3.0#长宽比
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glFrustumf( -1.0, 1.0, -1.0*aspect, 1.0*aspect, 10.0,300.0)#透视投影
##初始化函数，用于创建运行参数环境
def myinit():
    glClearColor( 0, 0, 0, 1.0 )#背景色
    #通过方程获得坐标点，放入坐标点列表
    #可以看到三维下的坐标是三个参数x,y,z
    for i in range(300):
        vertice.append(i*2.0/100*math.sin(i*2.0*math.pi/100))
        vertice.append(i*2.0/100*math.cos(i*2.0*math.pi/100))
        vertice.append(-1.0+i*2.0/100)
    line()
#线模型
def line():
    #生成顶点数组
    vertices = array(GL_FLOAT, 3,vertice)
    glMatrixMode( GL_MODELVIEW )#视图变换
    glEnableClientState( GL_VERTEX_ARRAY )#激活顶点数组
    glVertexPointerf(vertices)#送往图形管线绘制
    glPointSize(3.0)#设置点大小3
#显示函数，包括一系列变换操作
def display(i):
    global turning_axis,angle
    cameraD,SCALE=100,10.0
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    glTranslatef( 0 , 0 , -cameraD)#平移  
    if turning_axis==0:
        glRotatef(angle,1.0,0.0,0.0)#旋转,绕x轴
    if turning_axis==1:
        glRotatef(angle,0.0,1.0,0.0)
    if turning_axis==2:
        glRotatef(angle,1.0,0.0,1.0)
    if turning_axis==3:
        glRotatef(angle,1.0,1.0,0.0)
    glColor4f(1.0,0.0,1.0,1.0)#设置点颜色
    glDrawElementsub( GL_POINTS, points )#使用绘制函数绘制
#退出
def set_exit():
    global running, canvas
  #  graphics.screenshot().save("c:\\line2.png")
    canvas=None
    running = 0
#定义按键时间
def keys(event):
    global turning_axis,angle
    angle+=5.0#旋转角度加5
    if event['keycode'] == key_codes.EKeyDownArrow:
        turning_axis = 1
    elif event['keycode'] == key_codes.EKeyRightArrow:
        turning_axis = 2
    elif event['keycode'] == key_codes.EKeyLeftArrow:
        turning_axis = 3
    elif event['keycode'] == key_codes.EKeyUpArrow:
        turning_axis = 0
def main():
    appuifw.app.exit_key_handler=set_exit
    appuifw.app.screen = 'full'
    #定义界面
    canvas=glcanvas.GLCanvas(redraw_callback=display,event_callback=keys, resize_callback=reshape)
    appuifw.app.body=canvas
    #调用初始化
    myinit()
    #开始绘制
    while running:
        canvas.drawNow()
        e32.ao_yield()
main()