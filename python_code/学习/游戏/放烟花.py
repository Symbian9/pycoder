#
#烟花
import appuifw
import e32
from random import randint as rd
import math
from graphics import *
from sysinfo import display_pixels
############
scr = display_pixels()
cath_lock = e32.Ao_lock()
appuifw.app.screen = "full"
def cn(x): return x.decode("utf-8")
running = 1
image = Image.new(scr)
image.clear(0)
###########
def handle_redraw(rect):
    if image: canvas.blit(image)
canvas = appuifw.Canvas(event_callback=None,
    redraw_callback=handle_redraw)
appuifw.app.body = canvas
#################
def exit():
    global running
    running = 0
    cath_lock.signal()
#################
appuifw.app.exit_key_handler = exit
#烟花升空时的颜色控制，防止错色 


def p(xint):
    if (xint-15) < 0:
        return 0
    else: return (xint-15)
#########
#烟花炸开时往外扩散的效果(k值越大，花瓣越长) 

def shine(zb=None, co=None):
    for k in range(0, zb[2], 4):
        image.clear(0)
        for i in range(63):
            image.line((zb[0], zb[1], zb[0]+math.cos(0-0.1*i)*k, zb[1]+math.sin(0-0.1*i)*k), (co[0], co[1], co[2]), width=2)
        e32.ao_sleep(.001)
        handle_redraw(())
#################
#烟花熄灭(把烟花的花瓣for遍历涂黑) 

def exti(zb=None, co=None):

#eval("max"+str(tuple(co)))返回参数co中的最大值，并遍历这个最大值 

    for k in range(0, eval("max"+str(tuple(co))), 10):
        image.clear(0)
        #63为花瓣根数 

        for i in range(63):
            R = co[0]-k
            if R <= 0: R = 0
            G = co[1]-k
            if G <= 0: G = 0
            B = co[2]-k
            if B <= 0: B = 0
          #0.1*i为花瓣之间的间距

            image.line((zb[0], zb[1], zb[0]+math.cos(0-0.1*i)*zb[2], zb[1]+math.sin(0-0.1*i)*zb[2]), (R, G, B), width=2)
        e32.ao_sleep(.001)
        handle_redraw(())
#########
while running:
    e32.ao_yield()
    #l的成员为两个临时变量 

    l = [0, 0]
    #拆分tuple，调用成员 

    c0, c1, c2 = (rd(100, 220), rd(100, 220), rd(100, 220))
    #变量d的成员分别为：发射时纵坐标；升空后爆炸时的坐标；RGB颜色值 

    d = [rd(10, scr[0]-10), rd(10, scr[1]/2), rd(45, 80)]
    #发射升空时的拖尾 

    for i in range((scr[1]-d[1])/2):
        image.line((d[0], scr[1]+1-l[0], d[0]-1, scr[1]+1-l[1]), (p(0), p(c1), p(c2)))
        image.line((d[0], scr[1]-l[0], d[0], scr[1]+4-l[1]), (c0, c1, c2))
        image.line((d[0]+1, scr[1]+1-l[0], d[0]+1, scr[1]+1-l[1]), (p(c0), p(c1), p(c2)))
        #当l[0]的坐标大于6时，l[1]依次叠加2；形成拖尾；6是拖尾长度 

        l[0] += 2
        if l[0] > 6: l[1] += 2
        e32.ao_sleep(.001)
        image.clear(0)
        handle_redraw(())
    shine(d, [c0, c1, c2])
    exti(d, [c0, c1, c2])
    e32.ao_sleep(.001)
################
cath_lock.wait()