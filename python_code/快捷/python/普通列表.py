import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
    appuifw.app.set_exit()
def list():
    list=[cn("项目一"),cn("项目二"),cn("退出")]
    def press():#定义动作
        index=listbox.current()#取得用户选的是哪一项
        if (index==0)or(index==1):#or指只要符合两种中某一情况就运行，py从0开始计数
            appuifw.note(cn("这是项目")+unicode(index+1),"info")
        else:
            exit()
    appuifw.app.body=listbox=appuifw.Listbox(list,press)#在某一项上按确定，就执行press定义的动作
list()
e32.Ao_lock().wait()
