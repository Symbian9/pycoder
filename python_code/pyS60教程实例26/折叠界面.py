import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
    appuifw.app.set_exit()

def lab1():#文本界面
    appuifw.app.body=t=appuifw.Text()
    t.clear()
    t.set(cn("我是tengge!\nQQ:930372551"))
    
def lab2():#列表界面
    list=[cn("土豆"),cn("地瓜")]
    def press():
        index=listbox.current()
        appuifw.note(cn("这是")+list[index])
    appuifw.app.body=listbox=appuifw.Listbox(list,press)
    
def lab3():#画布界面
    from graphics import Image
    appuifw.app.body=canvas=appuifw.Canvas()
    img=Image.new((240,320))
    img.clear(0x0000ff)
    def redraw():
        canvas.blit(img)
    while True:
        redraw()#借循环语句使redraw函数不断执行，比米饭的简单吧
        e32.Ao_yield()#监控退出命令，使程序能退出

def action(x):
    if x==0:
        lab1()
    elif x==1:
        lab2()
    else:
        lab3()
tabs=[cn("文本界面"),cn("列表界面"),cn("画布界面")]
appuifw.app.set_tabs(tabs,action)#仅本段是建标签的关键段！

appuifw.exit_key_handler=exit
e32.Ao_lock().wait()