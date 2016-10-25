import appuifw,e32
import powlite_fm

appuifw.app.body = m = appuifw.Text()

def cn(x):return x.decode("utf8")

def txt():
    t = appuifw.query(cn('提示'),'text',cn('请输入文字'))
    m.add(t)

def exit():
    if appuifw.query(cn('确定退出吗？'),'query'):
        appuifw.app.set_exit()
        appuifw.note(cn('谢谢使用！'),'info')

def menu1():
    appuifw.note(cn('二级菜单2'))
appuifw.app.title=(cn('记事本'))

m.set(cn('\n\t小小菜鸟\n'))
m.add(cn("\t学Py编程"))
    
def read():    
    file=powlite_fm.manager().AskUser(ext=[".txt"])
    if file==None:
        appuifw.note(cn('打开失败！'),'error')
    else:
        txt=open(file)
        text=txt.read().decode('utf-8')
        m.set(text)
        txt.close()
        appuifw.note(cn("读取成功！"),"conf")

appuifw.app.menu=[(cn('功能'),((cn('打开'),read),(cn('写入'),txt),)),(cn('菜单2'),((cn('二级菜单'),menu1),(cn('哈哈'),menu1),)),(cn('退出'),exit)]

appuifw.app.exit_key_handler=e32.Ao_lock().signal()

e32.Ao_lock().wait()