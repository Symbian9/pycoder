import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
    if appuifw.query(cn("要退出吗？"),"query"):#按“是”时执行下个语句
        appuifw.app.set_exit()

def read():#定义读取函数
    try:#尝试，若无此语句，不存在“e:\\tengge.txt”时会出错！
        file=open("e:\\tengge.txt","r")#"r"只读，"w"可写，"a"添加
        text=file.read().decode("utf8")#读取，并将储存的数据按"utf8"格式译码为unicode
        t.set(text)
        file.close()#最后一定要关闭该文件供系统使用
        appuifw.note(cn("读取成功！"),"conf")
    except:#如果上面语句无法执行，就执行下面的
        appuifw.note(cn("读取失败！"),"error")

def save():#定义保存函数
    try:
        file=open("e:\\tengge.txt","w")
        text=t.get().encode("utf8")#获取屏幕内容以“utf8”的方式编码并储存
        file.write(text)#向文件中写数据，对应read
        file.close()
        appuifw.note(cn("保存成功！"),"conf")
    except:
        appuifw.note(cn("保存失败！"),"error")

appuifw.app.body=t=appuifw.Text()
appuifw.app.title=cn("记事本")
appuifw.app.menu=[(cn("保存"),save),(cn("读取"),read),(cn("退出"),exit)]
e32.Ao_lock().wait()