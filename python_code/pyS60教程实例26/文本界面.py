import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
    appuifw.app.set_exit()
appuifw.app.body= m =appuifw.Text()
#定义主界面是文本界面
m.set(cn("这是一个记事本程序！\n")+cn("制作者：tengge"))
#定义文本界面的内容，顺便学一下用"="建两段文本连在一起
appuifw.app.title=cn("记事本")
#定义标题栏
appuifw.app.screen="normal"
#定义窗口大小，有效值"normal"（标准）,"full"（全屏）,"large"（大屏）

appuifw.app.menu=[(cn("退出"),exit)]
#创建菜单，详见创建菜单一节
appuifw.app.exit_key_handler=exit
#定义右键动作，即：按下右软键，运行定义好的exit函数

e32.Ao_lock().wait()
