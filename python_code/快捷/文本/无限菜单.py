import appuifw,e32
def cn(x):return x.decode("utf8")
def popup_menu():
    list=[cn("菜单一"),cn("菜单二")]#这是列表，详见元组、列表和字典一节
    index=appuifw.popup_menu(list,cn("无限菜单"))
    if index==0:
        appuifw.note(cn("这是菜单一"),"info")
    else:
        appuifw.note(cn("这是菜单二"),"info")
appuifw.app.exit_key_handler=popup_menu#定义在右键上

e32.Ao_lock().wait()