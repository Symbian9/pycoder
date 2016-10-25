import appuifw,e32
def cn(x):return x.decode("utf8")
def menu1():
    appuifw.note(cn("这是菜单一"),"info")
def menu2():
    appuifw.note(cn("这是菜单二"),"info")
def exit():
    appuifw.note(cn("这是退出"),"info")
    appuifw.app.set_exit()
appuifw.app.menu=[(cn("一级菜单"),((cn("菜单一"),menu1),(cn("菜单二"),menu2))),(cn("退出"),exit)]

e32.Ao_lock().wait()
