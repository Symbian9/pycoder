import graphics, appuifw as a, e32,key_codes

import sys
sys.setdefaultencoding('utf-8')
del sys

rotate=0
stretch=0
path0='c:\\system\\apps\\pysokoban\\'
x=y=0
dx=dy=0
cx=cy=0
n=isinstalled=0
level=1
scores=0
size=graphics.Image.inspect(path0+'wall.png')['size']
wall=graphics.Image.new(size)
wall.load(path0+'wall.png')

size=graphics.Image.inspect(path0+'free.png')['size']
free=graphics.Image.new(size)
free.load(path0+'free.png')

size=graphics.Image.inspect(path0+'target.png')['size']
targets=graphics.Image.new(size)
targets.load(path0+'target.png')

size=graphics.Image.inspect(path0+'bar.png')['size']
bar=graphics.Image.new(size)
bar.load(path0+'bar.png')
import sysinfo as s
bar=bar.resize((s.display_pixels()[0],int((20.0/320.0)*s.display_pixels()[1])))

size=graphics.Image.inspect(path0+'box.png')['size']
box=graphics.Image.new(size)
box.load(path0+'box.png')

size=graphics.Image.inspect(path0+'player.png')['size']
player=graphics.Image.new(size)
player.load(path0+'player.png')

size=graphics.Image.inspect(path0+'boxtarget.png')['size']
tb=graphics.Image.new(size)
tb.load(path0+'boxtarget.png')

size=graphics.Image.inspect(path0+'playertarget.png')['size']
tp=graphics.Image.new(size)
tp.load(path0+'playertarget.png')


def ru(x): return x.decode('utf-8')
freepositions=[]
field=[]
class LevelLoader:
    def open(self,level):
        global isinstalled,canvas,buffer, cx,cy
        cx=cy=0
        isinstalled=0        
        f=open(path0+'levels\\'+str(level)+'.txt','r')
        listlines=[str([j for j in i.split(',')]) for i in f.read().splitlines()]
        f.close()
        i=0
        while i<len(listlines):
            listlines[i]=eval(listlines[i])
            i=i+1
        return listlines
        
def setresize():
    global field,free,box,player,targets,wall,tb,canvas,stretch,tp
    free=box=player=targets=wall=tb=tp=None
    size=graphics.Image.inspect(path0+'wall.png')['size']
    wall=graphics.Image.new(size)
    wall.load(path0+'wall.png')

    size=graphics.Image.inspect(path0+'free.png')['size']
    free=graphics.Image.new(size)
    free.load(path0+'free.png')

    size=graphics.Image.inspect(path0+'target.png')['size']
    targets=graphics.Image.new(size)
    targets.load(path0+'target.png')

    size=graphics.Image.inspect(path0+'box.png')['size']
    box=graphics.Image.new(size)
    box.load(path0+'box.png')

    size=graphics.Image.inspect(path0+'player.png')['size']
    player=graphics.Image.new(size)
    player.load(path0+'player.png')

    size=graphics.Image.inspect(path0+'boxtarget.png')['size']
    tb=graphics.Image.new(size)
    tb.load(path0+'boxtarget.png')
    size=graphics.Image.inspect(path0+'playertarget.png')['size']
    tp=graphics.Image.new(size)
    tp.load(path0+'playertarget.png')

    xm=len(field[1])
    ym=len(field)
    import sysinfo
    min=65535
    r=(int(sysinfo.display_pixels()[0]/xm),int(sysinfo.display_pixels()[1]/ym-(bar.size[1]/ym)))
    for m in r:
        if m<min: min=m
    s=(min,min)        
    if not stretch:
        r=s
    free= free.resize(r)
    box= box.resize(r)
    player= player.resize(r)
    targets= targets.resize(r)
    wall= wall.resize(r)
    tb= tb.resize(r)
    tp= tp.resize(r)
    del sysinfo


    
def redraw():
    global canvas, buffer,field,cx,cy,free, box,player,targets,wall,tb,n,bar,scores,level,tp
    buffer.clear(0x0)
    listlines=field
    n=0
    xe=canvas.size[0]//wall.size[0]+1
    ye=canvas.size[1]//wall.size[1]+1
    k=0
    while k<(ye):
        l=0
        while l<(xe):
            buffer.blit(wall,target=(0+wall.size[0]*l,0+wall.size[1]*k))
            l=l+1
        k=k+1
    isinstalled=0
    i=0
    while i<len(listlines):
        j=0
        while j<len(listlines[i]):
            if listlines[i][j]=='1':
                buffer.blit(wall,target=(0+wall.size[0]*j,0+wall.size[1]*i))
            if listlines[i][j]=='0':
                buffer.blit(free,target=(0+free.size[0]*j,0+free.size[1]*i))
            if listlines[i][j]=='T':
                buffer.blit(targets,target=(0+targets.size[0]*j,0+targets.size[1]*i))
            if listlines[i][j]=='TB':
                buffer.blit(tb,target=(0+tb.size[0]*j,0+tb.size[1]*i))
                n=n+1
                isinstalled=isinstalled+1
            if listlines[i][j]=='B':
                buffer.blit(box,target=(0+box.size[0]*j,0+box.size[1]*i))
                n=n+1
            if listlines[i][j]=='S':
                buffer.blit(player,target=(0+player.size[0]*j,0+player.size[1]*i))
                cx=j
                cy=i
            if listlines[i][j]=='ST':
                buffer.blit(tp,target=(0+tp.size[0]*j,0+tp.size[1]*i))
                cx=j
                cy=i
            j=j+1
        i=i+1            
        
    buffer.blit(bar,target=(0,canvas.size[1]-bar.size[1]))
    import sysinfo
    buffer.text((int((155.0/240.0)*sysinfo.display_pixels()[0]),canvas.size[1]-5),unicode(str(level)))
    buffer.text((int((210.0/240.0)*sysinfo.display_pixels()[0]),canvas.size[1]-5),unicode(str(scores)))
    buffer.text((int((20.0/240.0)*sysinfo.display_pixels()[0]),canvas.size[1]-5),ru('菜单'))
    buffer.text((int((90.0/240.0)*sysinfo.display_pixels()[0]),canvas.size[1]-5),ru('级别：'))
    buffer.text((int((170.0/240.0)*sysinfo.display_pixels()[0]),canvas.size[1]-5),ru('得分：'))
    blit(())
    del sysinfo

def blit(a):
    global canvas, buffer
    canvas.blit(buffer)

def event(event):
  global field,dx,dy,cx,cy,n,isinstalled,level,scores,canvas,buffer
  dx=dy=0
  if event["type"] == 1:
    ev = event["keycode"]
    if (ev == key_codes.EKeyUpArrow) or (ev == key_codes.EKey2):
      dx=0
      dy=-1
      #вверх
    elif ev == key_codes.EKeyRightArrow or (ev == key_codes.EKey6) :
      dx=1
      dy=0
      #вправо
    elif ev == key_codes.EKeyDownArrow or (ev == key_codes.EKey8) :
      dy=1
      dx=0
      #вниз
    elif ev == key_codes.EKeyLeftArrow or (ev == key_codes.EKey4):
      dy=0
      dx=-1
      #влево
  if field[(cy)][(cx)]=='ST' and field[(cy+dy)][(cx+dx)]=='0':
      field[(cy+dy)][(cx+dx)]='S'
      field[cy][cx]='T'
  elif field[(cy+dy)][(cx+dx)]=='0' and field[(cy)][(cx)]=='S':
      field[(cy+dy)][(cx+dx)]='S'
      field[cy][cx]='0'
      scores=scores-1
  elif field[(cy+dy)][(cx+dx)]=='T' and field[cy][cx]=='S':
      field[(cy+dy)][(cx+dx)]='ST'
      field[cy][cx]='0'
  elif field[(cy+dy)][(cx+dx)]=='T' and field[cy][cx]=='ST':
      field[(cy+dy)][(cx+dx)]='ST'
      field[cy][cx]='T'
      
  elif field[(cy+dy)][(cx+dx)]=='TB' and field[cy][cx]=='S' and field[(cy+2*dy)][(cx+2*dx)]=='0':
      isinstalled=isinstalled-1
      field[(cy+dy)][(cx+dx)]='ST'
      field[cy][cx]='0'
      field[(cy+2*dy)][(cx+2*dx)]='B'

  elif field[(cy+dy)][(cx+dx)]=='TB' and field[cy][cx]=='ST' and field[(cy+2*dy)][(cx+2*dx)]=='T':
      field[(cy+dy)][(cx+dx)]='ST'
      field[cy][cx]='T'
      field[(cy+2*dy)][(cx+2*dx)]='TB'
  elif field[(cy+dy)][(cx+dx)]=='TB' and field[cy][cx]=='S' and field[(cy+2*dy)][(cx+2*dx)]=='T':
#      isinstalled=isinstalled-1
      field[(cy+dy)][(cx+dx)]='ST'
      field[cy][cx]='0'
      field[(cy+2*dy)][(cx+2*dx)]='TB'

  elif (field[(cy+dy)][(cx+dx)]=='B') and (field[(cy+2*dy)][(cx+2*dx)]=='0') and field[(cy)][(cx)]=='ST':
      field[(cy+2*dy)][(cx+2*dx)]='B'
      field[(cy+dy)][(cx+dx)]='S'
      field[cy][cx]='T'
  elif (field[(cy+dy)][(cx+dx)]=='B') and (field[(cy+2*dy)][(cx+2*dx)]=='0') and field[(cy)][(cx)]=='S':
      field[(cy+2*dy)][(cx+2*dx)]='B'
      field[(cy+dy)][(cx+dx)]='S'
      field[cy][cx]='0'

      scores=scores+1
  elif (field[(cy+dy)][(cx+dx)]=='B') and (field[(cy+2*dy)][(cx+2*dx)]=='T'):
      scores=scores+100
      field[(cy+2*dy)][(cx+2*dx)]='TB'
      field[(cy+dy)][(cx+dx)]='S'
      field[cy][cx]='0'
      isinstalled=isinstalled+1
      
  if (isinstalled==n):
      import os
      global path0
      if level<len(os.listdir(path0+'levels\\')):
          del os
          buffer.clear(0x0)
          level=level+1
          field=levelloader.open(level)
          setresize()
      else:
          isinstalled=0
          n=0
          a.note(u'game over')
          main()
  if event['type']==1:
      redraw()
  

def trans():
    global field
    a=[]
    l=len(field[1])
    i=0
    while i<l:
        a.append([x[i] for x in field])
        i=i+1
    field=a
    setresize()
    redraw()

def exit():
    import os
    os.abort()

def newgame():
    global level,field,scores
    scores=0
    level=1
    field=LevelLoader().open(level)
    setresize()

def loadgame():
        global field,level,scores,path0,isinstalled
        try:
            f=open(path0+'save.txt','r')
        except:
            a.note(ru('未找到已存游戏'))
            main()
        listlines=[str([j for j in i.split(',')]) for i in f.read().splitlines()]
        f.close()
        i=0
        while i<len(listlines):
            listlines[i]=eval(listlines[i])
            i=i+1
        field=listlines
        f2=open('c:\\system\\apps\\pysokoban\\save2.txt','r')
        a=f2.read()
        level=int(a.split(chr(10))[0])
        scores=int(a.split(chr(10))[1])
        isinstalled=int(a.split(chr(10))[2])
        f2.close()
        setresize()
        redraw()



def restartlevel():
    global field,level,scores
    scores=scores-250
    del field
    field=LevelLoader().open(level)
    redraw()
    
def save():
    global path0,field,level,scores,isinstalled
    import os
    if os.path.isfile(path0+'save.txt'):
        os.remove(path0+'save.txt')
    if os.path.isfile(path0+'save2.txt'):
        os.remove(path0+'save2.txt')
    f=open(path0+'save.txt','a')
    f2=open(path0+'save2.txt','a')
    i=0
    while i<len(field):
        j=0
        s=''
        while j<len(field[i]):
            s=s+field[i][j]+','
            j=j+1
        f.write(s[0:len(s)-1]+chr(10))
        i=i+1
    f.close()
    f2.write(str(level)+chr(10)+str(scores)+chr(10)+str(isinstalled))
    f2.close()
    
canvas=buffer=None
levelloader=LevelLoader()
def main():
    global canvas,buffer
    index=a.selection_list([ru('新游戏'),ru('加载游戏'),ru('退出')])
    if index==0:
        newgame()
    elif index==1:
        loadgame()
    elif index==2:
        exit()
    setresize()
    canvas = a.Canvas(redraw_callback = blit, event_callback = event)
    a.app.body = canvas
    a.app.screen = "full"
    w, h = canvas.size
    canvas.clear(0x0)
    buffer = graphics.Image.new((w, h))

a.app.menu = [(ru('保存游戏'),save),(ru('加载游戏'),loadgame),(ru('重置游戏'),restartlevel),(ru('屏幕变动'),trans),(ru('主菜单'),main),(ru('退出'),exit)]
main()
redraw()
canvas.clear(0x0)
buffer.clear(0x0)
redraw()
while 1:
    e32.ao_yield()
