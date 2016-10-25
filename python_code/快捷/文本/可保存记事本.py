
import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
  if appuifw.query(cn("要退出吗？"),"query"):
    appuifw.app.set_exit()

def read():
  try:
    file=open("e:\\new.txt","r")#"r"只读，"w"可写，"a"添加
    text=file.read().decode("utf8")
    t.set(text)
    file.close()
    appuifw.note(cn("读取成功！"),"conf")
  except:appuifw.note(cn("读取失败！"),"error")

'''
f.readline()#读一行
f.read().splitlines()#读全部行并且把行结束符、换行符去掉#获得每一行，而且把每一行作为一个列表的一个元素
f.readlines()和f.read().splitlines(1)相同
'''

def save():
  try:
    file=open("e:\\new.txt","w")
    text=t.get().encode("utf8")
    file.write(text)
    file.close()
    appuifw.note(cn("保存成功！"),"conf")
  except:appuifw.note(cn("保存失败！"),"error")

appuifw.app.body=t=appuifw.Text()
appuifw.app.title=cn("记事本")
appuifw.app.menu=[(cn("保存"),save),(cn("读取"),read),(cn("退出"),exit)]

e32.ao_sleep(5)