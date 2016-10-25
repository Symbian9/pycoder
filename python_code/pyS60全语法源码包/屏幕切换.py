#米饭教程

import appuifw,e32
def cn(x):
    return x.decode("utf-8")


appuifw.app.title=cn("米饭教程")

def Switch():
    if appuifw.app.screen=="normal":
        appuifw.app.screen="large"
    elif appuifw.app.screen=="large":
        appuifw.app.screen="full"
    else:
        appuifw.app.screen="normal"

def Manual():
    c=[cn("全屏"),cn("大屏"),cn("标准"),"full","large","normal"]#这里的意思请弄明白。
    d=appuifw.popup_menu(c[:3],u"=*=*=")
    if d!=None:
        appuifw.app.screen=c[d+3]


appuifw.app.body=m=appuifw.Text()
m.set(cn("按选项继续\n按拨号键切换屏幕"))
m.bind(63586,Switch)

appuifw.app.menu=[(cn("自动切换"),Switch), (cn("手动切换"),Manual)]

e32.Ao_lock().wait()