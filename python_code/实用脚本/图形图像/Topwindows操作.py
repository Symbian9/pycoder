import appuifw,graphics,e32,TopWindow
from key_codes import *
#光标位置变量pos_y=0#记录菜单级变量M=0
#生成(实例化)四个Topwindow
w1=TopWindow.TopWindow()
w2=TopWindow.TopWindow()
w3=TopWindow.TopWindow()
w4=TopWindow.TopWindow()
#生成四个图像，前三个为突破最后一个为图形
img1=graphics.Image.open('c:\\11.jpg')
img2=graphics.Image.open('c:\\12.jpg')
img3=graphics.Image.open('c:\\13.jpg')
img4=graphics.Image.new((60,80))
def chn(x):return x.decode('utf8')
def quit():
  lock.signal()
  #菜单级控制函数以及光标移动函数
def move(y,x):
  #声明各全局变量
  global pos_y,M,w1,w2,w3,w4
  tpos_y=pos_y
  pos_y+=x
  #函数的两个参数x控制光标移动用,y控制菜单级用#如果传入参数为y=1这里对应按导航键向右
  if y==1:
    #如果菜单为显示，即0级菜单，但是此时按了向右键#说明将要显示第一级菜单，后面三个判断类同
    if M==0:
      #则显示第一级菜单
      Menu()#第二级
    elif M==1:
      SubMenu()
      #第三极
    elif M==2:
      SSubMenu()
      #第四级
    elif M==3:
      SSSubMenu()
      #传入y=-1则菜单后退，也即撤销当前显示的菜单
  if y==-1:
    #如果当前是第四级
    if M==4:
      #则隐藏第四级
      w4.hide()
      #设置菜单级变量为3
      M=3#同上
    elif M==3:
      w3.hide()
      M=2
    elif M==2:
      w2.hide()
      M=1
    elif M==1:
      w1.hide()
      M=0
      #判断光标为移出菜单范围，否则不做变化
  if pos_y<0 or (M==4 and pos_y==4):
    pos_y=tpos_y
    #如果在第四级，即可以移动光标，这里必须对第四级菜单更新，更新条件还有y==0,即传入的参数是光标移动变量x
  if M==4 and y==0:
    SSSubMenu()
    #如果按下导航键确认键，则给出提示，这里可以是其他任意函数的调用，调用后，注意要隐藏所有随显
  if y==0 and x==0:
    appuifw.note(u'OK','info')
canvas=appuifw.Canvas()
appuifw.app.body=canvas
appuifw.app.screen='full'
canvas.bind(63496,lambda:move(1,0))
canvas.bind(63557,lambda:move(0,0))
canvas.bind(63495,lambda:move(-1,0))
canvas.bind(63498,lambda:move(0,1))
canvas.bind(63497,lambda:move(0,-1))
#第一级菜单，由于前三级一样，所以只解释其中之一
def Menu():
  global img1,M
  #第一级标志变量赋为1
  M=1
  #TopWindow基本函数，前面有讲解，请熟练掌握
  w1.add_image(img1,(0,0))
  w1.size=(img1.size)
  #随显的位置一定要设置正确，自己修改看效果
  w1.position=(0,canvas.size[1]-img1.size[1])
  #显示出来
  w1.show()#第二季
def SubMenu():
  global img2,M
  M=2
  w2.add_image(img2,(0,0))
  w2.size=(img2.size)
  w2.position=(img1.size[0],canvas.size[1]-img2.size[1])
  w2.show()
  #第三极
def SSubMenu():
  global img3,M
  M=3
  w3.add_image(img3,(0,0))
  w3.size=(img3.size)
  w3.position=(canvas.size[0]-img3.size[0],canvas.size[1]-img3.size[1])
  w3.show()
  #第四级，这级菜单是纯绘图，所以讲解详细点
def SSSubMenu():
  global img4,M
  M=4
  #清屏img4，记住，绘制图形，不清楚上一次的话，会乱掉
  img4.clear(0xaaaaaa)
  #画矩形，起始位置为img4的左上角加权某个值
  img4.rectangle((0,5+pos_y*20,60,5+(pos_y+1)*20),fill=(0,153,255))
  #画出菜单项
  img4.text((5,15),chn('1.***1'),(204,255,255))
  img4.text((5,35),chn('2.***2'),(204,255,255))
  img4.text((5,55),chn('3.***3'),(204,255,255))
  img4.text((5,75),chn('3.***3'),(204,255,255))
  #下同
  w4.size=(img4.size)
  w4.add_image(img4,(0,0))#位置一定要弄清楚
  w4.position=(canvas.size[0]-60,canvas.size[1]-80)
  w4.show()
  #退出按键
appuifw.app.exit_key_handler=quit
#线程锁
lock=e32.Ao_lock()
#调用第一级显示
Menu()
#等待，不wait的话，直接就结束了，你什么也看不到了lock.wait()