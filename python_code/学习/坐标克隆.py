'''
坐标克隆
by爱不只是说说
冰冰python论坛
'''

class fix:

  def __init__(s):
    import appuifw
    import graphics
    import powlite_fm
    s.A, s.E, s.P, s.G = appuifw, appuifw.e32, powlite_fm.manager(), graphics
    s.img = None
    s.A.app.screen='full'
    s.A.app.body = s.ca = s.A.Canvas(s.redraw, s.event)
    s.lock = s.E.Ao_lock()
    s.x, s.y = s.ca.size
    s.index = s.x/2#光标坐标
    s.indey = s.y/2
    s.inde_x = 0#图片坐标
    s.inde_y = 0
    s.n = 0
    s.h = 0
    s.clo2 = 0xff0000
    s.list = None
    s.wh = None
    s.image = None
    s.img = s.G.Image.new((s.x, s.y))
    s.main()
    s.A.app.exit_key_handler = s.lock.signal
    s.A.app.menu=[(u'open',s.openimg)]
    s.lock.wait()
    print s.list
  
  def redraw(s, x):
    if s.img:s.ca.blit(s.img)
  
  def openimg(s):
    path=s.P.AskUser(ext=['.jpg','.png','.gif','.bmp','.mbm'])
    if path:
      s.image = s.G.Image.open(path)
      s.list = None
      s.n = 0
      s.h = 0
      x, y = s.image.size
      s.index, s.indey = s.x/2, s.y/2
      s.inde_x, s.inde_y = s.x/2-x/2, s.y/2-y/2
      s.main()

  def main(s):
    s.img.clear(0)
    if s.image:s.img.blit(s.image,target=(s.inde_x, s.inde_y))
    if s.list:
      [s.img.line(i,s.clo2) for i in s.list if len(i)<>0]
      if s.h:
        if len(s.list[-1])!=0:
          __c=s.list[-1][-2:]
          __c+=(s.index,s.indey)
          s.img.line(__c,s.clo2)

    __clo = s.img.getpixel((s.index, s.indey))
    __clo = tuple([255-i for i in __clo[0]])
    s.img.line((s.index-4, s.indey, s.index+5, s.indey),__clo)
    s.img.line((s.index, s.indey-4, s.index, s.indey+5),__clo)
    s.ca.blit(s.img)

  def event(s, v):
    ty=v['type']#按键状态
    sc=v['scancode']#键值
    if ty==2:#停止
      if s.wh: s.wh=None
    elif ty==3:#短按
      if sc==14:#左导航键
        if s.h!=0:s.h=1
        if s.index>0:
          s.index-=1
          s.main()
        s.wh=True
        s.E.ao_sleep(0.25)
        while s.wh:
          if s.index>0:
            s.index-=1
            s.main()
          else:break
          s.E.ao_yield()
          s.E.ao_sleep(0.001)
      elif sc==15:#右导航键
        if s.h!=0:s.h=1
        if s.index<s.x:
          s.index+=1
          s.main()
        s.wh=True
        s.E.ao_sleep(0.25)
        while s.wh:
          if s.index<s.x:
            s.index+=1
            s.main()
          else:break
          s.E.ao_yield()
          s.E.ao_sleep(0.001)
      if sc==16:#上导航键
        if s.h!=0:s.h=1
        if s.indey>0:
          s.indey-=1
          s.main()
        s.wh=True
        s.E.ao_sleep(0.25)
        while s.wh:
          if s.indey>0:
            s.indey-=1
            s.main()
          else:break
          s.E.ao_yield()
          s.E.ao_sleep(0.001)
      elif sc==17:#下导航键
        if s.h!=0:s.h=1
        if s.indey<s.y:
          s.indey+=1
          s.main()
        s.wh=True
        s.E.ao_sleep(0.25)
        while s.wh:
          if s.indey<s.y:
            s.indey+=1
            s.main()
          else:break
          s.E.ao_yield()
          s.E.ao_sleep(0.001)
      elif sc==127:##键
        if s.clo2 != 0:
          s.clo2 = 0
        else:s.clo2 = 0xff0000
        s.main()
      elif sc==167:#ok键
        s.h+=1
        if s.h==3:
          s.h=0
          s.n+=1
          s.list.extend([()])
        if s.list == None:
          s.list = [()]
        s.list[s.n]+=(s.index,s.indey)
        s.main()

fix()