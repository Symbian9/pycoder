#巧⑥ㄨ№【天堂】(16982589)
#请随意按数字键！^o^

import appuifw2 as appuifw
appuifw.app.body= m =appuifw.Text()
def cn(x):return x.decode('utf-8')
m.focus=False
m.read_only=1
m.set(cn("禁止输入\nForbidden"))

txt=[cn("星海＆专业潜水员"),cn("木易东"),cn("Η♂ГОΛБ♀У"),cn("ENO==9527"),cn("八脚麒麟"),cn("笕℡十╱兵★卫╲"),cn("悠悠鱼o0"),cn("?流星?"),cn("№榀榀※"),cn("◇ζ蝴蝶ぢ"),cn("古枫"),cn("陈小睿")]

def a(x):
  appuifw.note(txt[x]+cn("大白痴"))

m.bind(48,lambda:a(0))
m.bind(49,lambda:a(1))
m.bind(50,lambda:a(2))
m.bind(51,lambda:a(3))
m.bind(52,lambda:a(4))
m.bind(53,lambda:a(5))
m.bind(54,lambda:a(6))
m.bind(55,lambda:a(7))
m.bind(56,lambda:a(8))
m.bind(57,lambda:a(9))
m.bind(35,lambda:a(10))# 
m.bind(42,lambda:a(11))#

appuifw.e32.Ao_lock().wait()