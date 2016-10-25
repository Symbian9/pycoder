import appuifw,graphics,e32
running=1
def cn(x):return x.decode('utf8')
def quit():
  global running
  running=0
canvas=appuifw.Canvas()
appuifw.app.body=canvas
appuifw.app.screen='full'
appuifw.app.exit_key_handler=quit
img=graphics.Image.new(canvas.size)
#进度条常见形式为100%#所以这里循环100次
for i in range(100):
  #清屏(黑色)
  img.clear(0)
  #进度条边框
  img.rectangle((20,80,220,100),0x777777)
  #下面这个循环产生所谓的立体感，效果看截图#原理方法在前面的教程有讲了，颜色渐变#这里利用的是矩形的，原理是一样的
  for j in range(10):
    img.rectangle((20,80+j,20+2*i,100-j),fill=(50+j*10,50+j*10,255-j*10))
    #显示进度百分比，这里str()内建函数，转化数字为字符串
    img.text((100,95),cn(str(i+1)+'%'),0xff0000)
  canvas.blit(img)
    #延时0.05秒，不然就看不到进度了。一下就跑到头了。
  e32.ao_sleep(0.05)
  #下面这段实现进度条来回游动的效果#和上面的有所不同，这是两种不同的进度效果而已#定义进度条运动变量，记录的是进度条坐标增加或者减少了多少
move=0
#进度条向左或者向右运动标志(x坐标)，主要是控制move是加还是减，不然进度条就跑到外面去了
flag=1
#既然是来回运动，这种效果肯定要保持住了，这样的话要while死循环。#这和上面的不同，上面的进度满后，就要转入游戏界面，所以不能死循环。当然这个也是不能的#不然就到不了游戏界面了，实际中也要控制时间的。
while running:
  #首先向右，这时flag是正的，move是增加的，于是向右运动
  move+=flag
  #外框
  img.clear(0)
  #清屏
  img.rectangle((20,80,220,100),0x777777)
  #如果运动到了边界，flag取负，这样下次move就是减少了
  if move>140:
    flag=-flag
    #如果运动到最左边，flag再取负，这时move是增加了。
  if move<0:
    flag=-flag
    #立体效果
  for j in range(10):
    img.rectangle((20+move,80+j,80+move,100-j),fill=(50+j*10,50+j*10,255-j*10))
  canvas.blit(img)
    #延时0.05秒，不然又是跑的太快了
  e32.ao_sleep(0.05)
  