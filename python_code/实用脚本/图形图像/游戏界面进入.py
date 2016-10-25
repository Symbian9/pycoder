#-*-coding:utf-8-*-
import appuifw
import graphics
import e32
ziti=u'Sans MT 936_s60'
#设置主界面为画布(canvas)
appuifw.app.body=canvas=appuifw.Canvas()
appuifw.app.screen="full"
#新建图形
img=graphics.Image.new(canvas.size)
def cn(x):return x.decode("utf8")
    #这里是闪屏的主要函数了#闪屏的目的是增加游戏的观赏性，也就是游戏开始前的那部分画面。
def start():
  #闪屏中的一些文字提示，比方说出来两个人物的对话啦上面的。#这里只是象征性的提示而已，具体使用你尽情发挥想象力吧。
    start_info=[cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading"),cn("loading")]
    #一个循环，什么作用呢？实现的时候两个矩形框向中间靠拢的闪屏效果#记住y从0取到8
    for y in range(15):
      #清屏为黑
        img.clear(0)
        #(0,y*10,176,10+(y*10)这样的用法多次讲到了吧？#画一个宽0--176，高y*10--10+y*10的吧矩形。#仔细想下，每次循环Y在增加，那矩形的位置呢？
        img.rectangle((0,y*10,240,10+(y*10)), 0x99ccff, fill=0x99ccff)
        img.rectangle((0,198-10*y,240,208-(y*10)), 0x99ccff, fill=0x99ccff)
        #把img画到canvas上
        canvas.blit(img)
        #记得讲过了，这里并不是用while死循环，因为闪屏要的就是闪动的效果，所以是要用很短的延时实现的。#这里延时0.08秒
        e32.ao_sleep(0.08)
    #判断两个矩形相遇了，现在该显示文字信息??，当然这只是形式而已，你可以在任何时间显示
    if y==14:
      #又见循环，实现的还是坐标的增减
      for j in range(10):
        #这次矩形是从中间往两边消失了，看坐标。这变化要多琢磨。很有用#结合测试和坐标位置变化弄懂下面这4句
          img.rectangle((88-10*j,78,88,88),0,fill=0)
          img.rectangle((88,78,88+10*j,88),0,fill=0)
          img.rectangle((88-10*j,120,88,130),0,fill=0)
          img.rectangle((88,120,88+10*j,130),0,fill=0)
          canvas.blit(img)
          e32.ao_sleep(0.2)
          #下面这些没用什么具体含义的。只是把文字信息以一种风格显示而已#你可以随便设计的，这里的设计是文字从中间一个向左一个向右交替出现#j%2是什么意思呢？就是判断j能不能被2整除也就是判断j是不是偶数了#刚说了一左一右当然是偶数向左奇数向右了(奇数j%2!=0)
          if j%2==0:
            #画字函数记得吧？start_info[j]这个的话就是开始那个列表的一个元素了也就是其中一个汉字。#列表的用法大家一定要掌握的。
              img.text((80-8*j,105),start_info[j],0xff0000,font=ziti)
              canvas.blit(img)
          else:
            #这句也一样了，文字向右而已，坐标是加。
              img.text((80+8*j,105),start_info[j],0xff0000,font=ziti)
              canvas.blit(img)
    e32.ao_sleep(1)
    #感觉下面这个还是有点新意的#循环20次，坐标改变20次
    for i in range(20):
      #清屏黑色，因为刚才拿效果结束了，这次要清屏了，不然都显示到一块了
        img.clear(0)
        #(0,0,240,18+(i*10)先说坐标，这是个向下扩大的矩形，最后一个坐标增加了不是？i*10每次增加10#0x99ccff，这个位置对应参数outline也就是边框颜色# fill=(153-(i/4)*50,204-(i/4)*50,255-(i/4)*50)填充色，是一种渐变色，产生一种明暗变化是效果#具体颜色变化怎么控制，这个需要你多尝试才能体会。具体说不清楚
        img.rectangle((0,0,240,130+(i*10)), 0x99ccff, fill=(153-(i/4)*50,204-(i/4)*50,255-(i/4)*50))
        canvas.blit(img)
          #延时0.02秒
        e32.ao_sleep(0.02)
      #调用函数，这个函数调用明显是在游戏开始时，然后闪屏结束后就进入游戏主菜单了
start()
