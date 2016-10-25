# by 悲观者
# E乐网wapele.cn

import appuifw2
import graphics
import random

def cn(x):
  return x.decode('utf-8')
def en(x):
  return x.encode('utf-8')
  
class main:
  def __init__(s):
    s.run=1
    s.score=0
    s.player=82
    s.foods=[]
    s.shots=[]
    (s.A,s.E,s.G,s.R)=(appuifw2,appuifw2.e32,graphics,random.randrange)
    s.A.app.screen='full'
    s.font=u'CombinedChinesePlain'
    s.A.app.exit_key_handler=s.Exit
    s.Img1=s.G.Image.new((176,208))
    s.Img2=s.G.Image.new((176,208))
    s.Img1.clear((200,200,200))
    for x in range(20):
      s.Img1.line((0,x,176,x),(x*4,x*4,x*4))
    s.Img1.text((5,15),cn('Py轰炸机'),(200,200,200),s.font+u'12')
    s.body=s.A.Canvas(event_callback=s.Key,redraw_callback=s.Draw)
    s.A.app.body=s.body
    for n in range(5):
      s.Getfood()
    s.Play()
    
  def Draw(s,draw=1):
    s.Img2.blit(s.Img1)
    s.Img2.text((110,15),cn('分数: '+str(s.score)),(100,230,100),s.font+u'12')
    s.Img2.text((s.player,200),cn('▲'),(100,100,100),s.font+u'12')
    for x,y in s.foods:
      if y>30:
        s.Img2.text((x,y),cn('★'),(230,100,100),s.font+u'12')
    for x,y in s.shots:
      s.Img2.text((x,y),cn('↑'),(100,100,100),s.font+u'12')
      
    s.body.blit(s.Img2)
  
  def Getfood(s):
    x=s.R(2,163,10)
    y=s.R(-30,30)
    while (x,y) in s.foods:
      x=s.R(2,163,10)
      y=30
    s.foods.insert(0,(x,y))
 
  def Getshot(s):
    x=s.player
    y=190
    s.shots.insert(0,(x,y))
    
  def Play(s):
    while s.run:
      try:
        for n in range(len(s.shots)):
          x,y=s.shots[n]
          if y>30:
            y-=1
            s.shots[n]=(x,y)
          else:
            s.shots.pop(n)
          if (x,y) in s.foods:
            s.shots.remove((x,y))
            s.foods.remove((x,y))
            s.Getfood()
            s.score+=10
      except:
        pass
      try:
        for n in range(len(s.foods)):
          x,y=s.foods[n]
          if x==s.player and 190<=y<=200:
            s.Again()
          if y<208:
            y+=1
            s.foods[n]=(x,y)
          else:
            if s.score>0:
              s.foods.pop(n)
              s.Getfood()
              s.score-=10
            else:
              s.Again()
          if (x,y) in s.shots:
            s.foods.remove((x,y))
            s.shots.remove((x,y))
            s.Getfood()
            s.score+=10
      except:
        pass
      
      s.Draw()
      s.E.ao_sleep(0.02)
      s.E.ao_yield()    
    
  def Again(s):
    if s.A.query(cn('重新开始？'),'query',1):
      s.__init__()
    else:
      s.Exit()
  
  def Key(s,event):
    if event['type']==s.A.EEventKey:
      if event['scancode']==14:
        if s.player>2:
          s.player-=10
        else:
          s.player=162
      elif event['scancode']==15:
        if s.player<162:
          s.player+=10
        else:
          s.player=2
      elif event['scancode']==16:
        pass
      elif event['scancode']==17:
        pass
    elif event['type']==s.A.EEventKeyDown:
      if event['scancode']==167:
        if len(s.shots)<5:
          s.Getshot()
        
      s.Draw()
      
  def Exit(s):
    s.run=0
      
m=main()