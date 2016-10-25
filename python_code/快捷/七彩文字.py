#道夫

import random,appuifw,e32
appuifw.app.body=m=appuifw.Text()

def a():
  hel="玉\n树\n宁\n峰\n哇\n麦".decode('utf8')
  for i in (hel):
    m.color=random.randrange(0xffffff)
    m.add(i)
    e32.ao_sleep(0.1)
a()