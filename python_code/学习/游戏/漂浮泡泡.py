#软件名：飘浮泡泡
#作者：Better(木狼)
#QQ:269246882
#日期:2009.02.13

import appuifw,e32,os,globalui
from graphics import *
from topwindow import *
x=[]
y=[]
mysets=[]
#图片大小
running=1
label1=1
label2=0
#表现方式
def cn(x):return x.decode("utf-8")

#配置为空,启动时载入

#初始化
pathlogo="c:\\data\\paopao\\pic\\logo.jpg"
imglogo=Image.open(pathlogo)
imglogo.text((60,50),cn("飘浮泡泡"),0xff2222,font="title")
windowlogo=TopWindow()
windowlogo.size=(220,300)
windowlogo.position=(10,10)
windowlogo.add_image(imglogo,(0,0,220,300))
windowlogo.shadow=1
windowlogo.show()
e32.ao_sleep(3)
windowlogo.hide()

#载入配置文件
try:
  run=1
  n=0
  f=open("c:\\data\\paopao\\data\\sets.ini","r")
  while run:
    n+=1
    txt=f.readline()
    #print txt
    try:
      txtxy=int(txt)
    except:pass
    if n<11:
      x.append(txtxy)
      print x[n-1]
    if 10<n<21:
      y.append(txtxy)
      print y[n-11]
    if 20<n<23:
      mysets.append(float(txt))
      print mysets[0]
      print type(mysets[0])
    if 22<n<30:
      mysets.append(txtxy)
    
    if n==30:
      print u"break"
      break
  print u"ready close"
  f.close()
  print u"Closed"
except:
  appuifw.note(cn("配置错误!"),"error")

try:
  if not os.path.exists("c:\\data\\paopao"):
    os.makedirs("c:\\data\\paopao\\pic")
    appuifw.note(cn("图片丢失!"),"error")
  else:pass
  print u"if ok\n"
  path="c:\\data\\paopao\\pic\\"
  path1=path+"1.jpg"
  path2=path+"2.jpg"
  path3=path+"3.jpg"
  path4=path+"4.jpg"
  path5=path+"5.jpg"
  path6=path+"6.jpg"
  path7=path+"7.jpg"
  path8=path+"8.jpg"
  path9=path+"9.jpg"
  path10=path+"10.jpg"
  #获取路径
  print u"pathok\n"
  img1=Image.open(path1)
  img2=Image.open(path2)
  img3=Image.open(path3)
  img4=Image.open(path4)
  img5=Image.open(path5)
  img6=Image.open(path6)
  img7=Image.open(path7)
  img8=Image.open(path8)
  img9=Image.open(path9)
  img10=Image.open(path10)
  print u"load img ok\n"
  #载入图片
  window1=TopWindow()
  window2=TopWindow()
  window3=TopWindow()
  window4=TopWindow()
  window5=TopWindow()
  window6=TopWindow()
  window7=TopWindow()
  window8=TopWindow()
  window9=TopWindow()
  window10=TopWindow()
  print u"load windows ok\n"
  print type(x[0])
  window1.size=(x[0],y[0])
  window2.size=(x[1],y[1])
  window3.size=(x[2],y[2])
  window4.size=(x[3],y[3])
  window5.size=(x[4],y[4])
  window6.size=(x[5],y[5])
  window7.size=(x[6],y[6])
  window8.size=(x[7],y[7])
  window9.size=(x[8],y[8])
  window10.size=(x[9],y[9])
  print u"windows size ok\n"
  #窗口大小
  #img2.text((5,15),u"2",0)
  #img3.text((5,15),u"3",0)
  window1.add_image(img1,(0,0,x[0],y[0]))
  window2.add_image(img2,(0,0,x[1],y[1]))
  window3.add_image(img3,(0,0,x[2],y[2]))
  window4.add_image(img4,(0,0,x[3],y[3]))
  window5.add_image(img5,(0,0,x[4],y[4]))
  window6.add_image(img6,(0,0,x[5],y[5]))
  window7.add_image(img7,(0,0,x[6],y[6]))
  window8.add_image(img8,(0,0,x[7],y[7]))
  window9.add_image(img9,(0,0,x[8],y[8]))
  window10.add_image(img10,(0,0,x[9],y[9]))
  print u"add img ok\n"
  print u"Finish loading..."
  
  #添加图片
except:
  appuifw.note(cn("程序文件丢失,请重新安装软件!"),"error")
#启动
def start():
  global running
  t1=mysets[0]
  t2=mysets[1]
  if label1:
    n=0
    sx=[0,30,60,90,120,150,180,210,240,70]
    sy=[280,360,100,350,280,150,220,340,300,270]
    for i in range(97):
      n+=1
      if n<33:
        g=1
      elif 32<n<65:
        g=2
      elif 64<n<97:
        g=1
      elif 96<n<129:
        g=2
      elif 128<n<161:
        g=1
      if g==1:
        sx[0]+=1
        sy[0]-=5
        sx[1]-=1
        sy[1]-=3
        sx[2]+=1
        sy[2]-=2
        sx[3]-=1
        sy[3]-=1
        sx[4]+=1
        sy[4]-=3.8
        sx[5]-=1
        sy[5]-=2.5
        sx[6]+=1
        sy[6]-=3.5
        sx[7]-=1
        sy[7]-=1.5
        sx[8]+=1
        sy[8]-=5
        sx[9]-=1
        sy[9]-=2.2
      else:
        sx[0]-=1
        sy[0]-=5
        sx[1]+=1
        sy[1]-=3
        sx[2]-=1
        sy[2]-=2
        sx[3]+=1
        sy[3]-=1
        sx[4]-=1
        sy[4]-=3.8
        sx[5]+=1
        sy[5]-=2.5
        sx[6]-=1
        sy[6]-=3.5
        sx[7]+=1
        sy[7]-=1.5
        sx[8]-=1
        sy[8]-=5
        sx[9]+=1
        sy[9]-=2.2

      window1.position=(sx[0],sy[0])
      window2.position=(sx[1],sy[1])
      window3.position=(sx[2],sy[2])
      window4.position=(sx[3],sy[3])
      window5.position=(sx[4],sy[4])
      window6.position=(sx[5],sy[5])
      window7.position=(sx[6],sy[6])
      window8.position=(sx[7],sy[7])
      window9.position=(sx[8],sy[8])
      window10.position=(sx[9],sy[9])
      window1.show()
      window2.show()
      window3.show()
      window4.show()
      window5.show()
      window6.show()
      window7.show()
      window8.show()
      window9.show()
      window10.show()
      e32.Ao_timer().after(t1)
  if label2:
    n=0
    sx=[-160,-80,0,60,120,-120,-60,0,60,120]
    sy=[0,0,0,0,0,-60,-60,-60,-60,-60]
    for i in range(140):
      n+=1
      sx[0]+=2
      sy[0]+=2
      sx[1]+=1
      sy[1]+=1
      sx[2]+=2
      sy[2]+=2
      sx[3]+=1
      sy[3]+=1
      sx[4]+=3.5
      sy[4]+=3.5
      sx[5]+=2
      sy[5]+=2
      sx[6]+=3
      sy[6]+=3
      sx[7]+=3.5
      sy[7]+=3
      sx[8]+=4
      sy[8]+=4
      sx[9]+=2
      sy[9]+=2
      window1.position=(sx[0],sy[0])
      window2.position=(sx[1],sy[1])
      window3.position=(sx[2],sy[2])
      window4.position=(sx[3],sy[3])
      window5.position=(sx[4],sy[4])
      window6.position=(sx[5],sy[5])
      window7.position=(sx[6],sy[6])
      window8.position=(sx[7],sy[7])
      window9.position=(sx[8],sy[8])
      window10.position=(sx[9],sy[9])
      window1.show()
      window2.show()
      window3.show()
      window4.show()
      window5.show()
      window6.show()
      window7.show()
      window8.show()
      window9.show()
      window10.show()
      e32.Ao_timer().after(t2)
  if running:
    start()
  else:
    window1.hide()
    window2.hide()
    window3.hide()
    window4.hide()
    window5.hide()
    window6.hide()
    window7.hide()
    window8.hide()
    window9.hide()
    window10.hide()

#设置
def set1():
  global label1,label2
  if label1==0:
    label2=0
    label1=1
  else:pass

#设置
def set2():
  global label1,label2
  if label2==0:
    label1=0
    label2=1
  else:pass
#保存配置
def savesets():
  global mysets
  mysets[0]=appuifw.query(cn("效果一移动速度,初始为0.08"),"float")
  mysets[1]=appuifw.query(cn("效果二移动速度,初始为0.08"),"float")
  appuifw.note(cn("本版无此功能,请参考说明手动修改配置文件."))
  pass

#停止
def stop():
  global running
  if running:
    running=0
  else:running=1

def help():
  index=appuifw.popup_menu([cn("使用说明"),cn("配置说明"),cn("图片更换")])
  if index==0:
    globalui.global_msg_query(cn("  点击开始启动程序\n  选择效果可以更换效果\n  点击停止\重置可停止运行或重新开始运行\n  请先停止运行后再退出."),cn("使用说明"))
  elif index==1:
    globalui.global_msg_query(cn("配置文件在c:\\data\\paopao\\data\\sets.ini内\n建议使用dedit以java-utf8编码打开编辑并保存\n编码格式不要修改,否则无法读配置!\n内含初始图片大小\n前十个分别为各飘浮物宽度\n第十一至第二十为高度\n两个小数分别是效果一和二的初始速度,后边的数据暂时无效,但不要改动."),cn("配置说明"))
  elif index==2:
    globalui.global_msg_query(cn("图片保存位置c:\\data\\paopao\\pic,里边有十个jpg格式图片,可以自己更换,建议图片不要太大."),cn("更换图片"))
#退出
def quit():
  app_lock.signal()
  if running:
    appuifw.note(cn("请先选择停止!"),"error")
  else:
    appuifw.app.exit_key_handler=None
    appuifw.app.set_exit()

appuifw.app.title=cn("飘浮泡泡")
appuifw.app.body=m=appuifw.Text(cn("飘浮泡泡\n作者：冰冰智能编程组Better(木狼)\nQQ:269246882\n版本:1.0(测试版)\n"))
appuifw.app.body.style=eval('appuifw.STYLE_UNDERLINE')
m.add(cn("软件只是测试版，拿出来先给大家看看玩玩，功能还不够完善，因为我只花了一个晚上和一个上午制作\n缺陷一:\n  由于py平台本身不支持gif动态图片，所以本软件也不支持动态飘浮物\n缺陷二:\n  飘浮物只能是方块形状,不支持透明图片.\n后期开发说明,我想在后期版本内加入用户Diy模式,自己可以配置飘浮物的路线,我想这样会更好,但愿不要太难,我尽量做.\n做这个版本是为了起一个抛砖引玉的效果,各位比我厉害的大哥大姐们希望你们能开发出比我这个更好玩的东西来哦！\n为了使程序运行速度更好,我把源代码编译为了pyc\n源代码在冰冰智能(wap.aapig.com pys60专区与软件一起发布.需要的朋友可以去下载.)"))
m.set_pos(0)
appuifw.app.exit_key_handler=quit
mainmenu=[(cn("开始"),start),(cn("效果"),((cn("效果一"),set1),(cn("效果二"),set2),(cn("配置设置"),savesets),)),(cn("停止\重置"),stop),(cn("说明"),help),(cn("退出"),quit)]
appuifw.app.menu=mainmenu
app_lock=e32.Ao_lock()
app_lock.wait()