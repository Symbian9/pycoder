import appuifw,e32,key_codes
from graphics import *

def cn(x):return x.decode('utf-8')
def quit(): _quit=1
global running
running=1
def redraw(rect): canvas.blit(img)

def default():
 global con,color,font
 con={"l":15,"x":15,"y":33,"r":13,"n":15}
 color={"bg":0x7777bb,"fg":0x333333,"p1":0x000000,"p2":0xffffff,"w":0xff0000}
 font=u"Sans MT 936_S60"

def initial():
 global img,canvas,con,color,cur_x,cur_y,turn,pos1,pos2,pos
 appuifw.app.screen='full'
 appuifw.app.body=canvas=appuifw.Canvas()
 img=Image.new((240,320))
 img.clear(color["bg"])
 cur_x=7
 cur_y=7
 turn=1
 pos1=[]
 pos2=[]
 pos=[]
 for i in range(con["n"]*con["n"]):
  pos.append(0)

def paint_back():
 global img,color,font
 img.text((90,25),cn('欢乐五子棋'),color["fg"],font)
 for i in range(con["x"],con["x"]+con["l"]*con["n"]-1,con["l"]):
  img.line((i,con["y"],i,con["y"]+con["l"]*(con["n"]-1)),color["fg"])
 for i in range(con["y"],con["y"]+con["l"]*con["n"]-1,con["l"]):
  img.line((con["x"],i,con["x"]+con["l"]*(con["n"]-1),i),color["fg"])
 img.text((40,270),cn('玩家1'),color["p1"],font)
 img.text((160,270),cn('玩家2'),color["p2"],font)
 img.point((90,263),color["p1"],width=con["r"],fill=color["p1"])
 img.point((144,263),color["p2"],width=con["r"],fill=color["p2"])
 
def paint_cur(x,y,sh):
 global img,con,color,pos1,pos2,running
 if running<>1:return
 ax=con["x"]+con["l"]*x
 ay=con["y"]+con["l"]*y
 b=con["l"]/2
 if sh<>0:
  c=color["p"+str(sh)]
  if rp((x,y))<>0:
   c=color["w"]
 if sh==0:
  c=color["bg"]
 img.line((ax-b,ay-2,ax-b,ay-b,ax-2,ay-b),c)
 img.line((ax-b,ay+2,ax-b,ay+b,ax-2,ay+b),c)
 img.line((ax+b,ay-2,ax+b,ay-b,ax+2,ay-b),c)
 img.line((ax+b,ay+2,ax+b,ay+b,ax+2,ay+b),c)
 redraw(())

def paint_q(x,y,z):
 global img,con,color
 ax=con["x"]+con["l"]*x
 ay=con["y"]+con["l"]*y
 b=con["l"]/2
 if z==0:
  c=color["bg"]
 else:
  c=color["p"+str(z)]
 img.point((ax,ay),c,width=con["r"],fill=c)
 redraw(())
 if z==0:
  img.line((ax-b,ay,ax+b,ay),c)
  img.line((ax,ay-b,ax,ay+b),c)
  
def k_up():
 global cur_x,cur_y,con,turn
 paint_cur(cur_x,cur_y,0)
 cur_y=cur_y-1
 if cur_y==-1:
  cur_y=con["n"]-1
 paint_cur(cur_x,cur_y,turn)

def k_down():
 global cur_x,cur_y,con,turn
 paint_cur(cur_x,cur_y,0)
 cur_y=cur_y+1
 if cur_y==con["n"]:
  cur_y=0
 paint_cur(cur_x,cur_y,turn)

def k_left():
 global cur_x,cur_y,con,turn
 paint_cur(cur_x,cur_y,0)
 cur_x=cur_x-1
 if cur_x==-1:
  cur_x=con["n"]-1
 paint_cur(cur_x,cur_y,turn)

def k_right():
 global cur_x,cur_y,con,turn
 paint_cur(cur_x,cur_y,0)
 cur_x=cur_x+1
 if cur_x==con["n"]:
  cur_x=0
 paint_cur(cur_x,cur_y,turn)

def rp(x):
 global con,pos
 if (x[0]<0 or x[0]>=con["n"] or x[1]<0 or x[1]>=con["n"]):return 0
 #print x,pos[x[0]*con["n"]+x[1]]
 return pos[x[0]*con["n"]+x[1]]

def wp(x,y):
 global con,pos
 pos[x[0]*con["n"]+x[1]]=y
  
def win():
 for i in pos1:
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]))==1:
    k=k+1
   else:
    break
  if k>=5:
   return 1
  k=0
  for j in range(0,6):
   if rp((i[0],i[1]+j))==1:
    k=k+1
   else:
    break
  if k>=5:
   return 1
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]+j))==1:
    k=k+1
   else:
    break
  if k>=5:
   return 1
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]-j))==1:
    k=k+1
   else:
    break
  if k>=5:
   return 1

 for i in pos2:
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]))==2:
    k=k+1
   else:
    break
  if k>=5:
   return 2
  k=0
  for j in range(0,6):
   if rp((i[0],i[1]+j))==2:
    k=k+1
   else:
    break
  if k>=5:
   return 2
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]+j))==2:
    k=k+1
   else:
    break
  if k>=5:
   return 2
  k=0
  for j in range(0,6):
   if rp((i[0]+j,i[1]-j))==2:
    k=k+1
   else:
    break
  if k>=5:
   return 2
 return 0
 
def k_enter():
 global cur_x,cur_y,turn,pos1,pos2,con,color,font,running
 if running<>1:return
 if rp((cur_x,cur_y))==0:
  if turn==1:
   pos1.append((cur_x,cur_y))
   img.rectangle((35,255,100,272),color["bg"])
   img.rectangle((135,255,200,272),color["p2"])
  if turn==2:
   pos2.append((cur_x,cur_y))
   img.rectangle((35,255,100,272),color["p1"])
   img.rectangle((135,255,200,272),color["bg"])
  paint_q(cur_x,cur_y,turn)
  wp((cur_x,cur_y),turn)
  if win()<>0:
   img.text((80,300),cn('玩家')+str(turn)+cn("获胜！"),color["fg"],font)
   img.rectangle((35,255,100,272),color["bg"])
   img.rectangle((135,255,200,272),color["bg"])
   paint_cur(cur_x,cur_y,0)
   running=2
 turn=3-turn
 paint_cur(cur_x,cur_y,turn)

def bindkey():
 canvas.bind(key_codes.EKeyUpArrow, k_up)
 canvas.bind(key_codes.EKeyDownArrow,k_down)
 canvas.bind(key_codes.EKeyLeftArrow, k_left)
 canvas.bind(key_codes.EKeyRightArrow,k_right)
 canvas.bind(key_codes.EKeySelect,k_enter)

default()
initial()
paint_back()
paint_cur(cur_x,cur_y,1)
img.rectangle((35,255,100,272),color["p1"])
bindkey()

redraw(())
appuifw.app.exit_key_handler = quit()
_quit=0
while (1-_quit):
 e32.ao_sleep(0.2)
 redraw(())