#巧⑥ㄨ№【天堂】(16982589)

import appuifw
import e32
appuifw.app.body=m=appuifw.Text()
def cn(x):return x.decode('utf-8')
m.color=(0,0,225)
m.style=appuifw.HIGHLIGHT_SHADOW
appuifw.app.title=(cn('倒数返回源码'))
def time():
  for i in range(9,0,-1):
    m.set(cn('谢谢使用哦~\n该功能在下一版本实现\n敬请期待(*^_^*)\n\n\n更多精彩\nheydust.80.hk\n\n\n'+'\t倒数'+str(i)+'秒返回'))
    e32.ao_sleep(1)
def main():
  m.set(cn('写软件的时候无意间想到的，很帅的倒数返回源码，发挥的余地很大哦！\n哈哈，越看越帅啊，也很好用。\n\t作者：嘿沙漠'))
time()
main()
e32.ao_sleep(3)