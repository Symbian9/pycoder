import appuifw,e32
def cn(x):return x.decode("utf8")
def exit():
    appuifw.app.set_exit()
def list():
    icon1=appuifw.Icon(u"Z:\\resource\\apps\\About.mbm",0,1)#用appuifw中的Icon函数将mbm或mif位图图片变为图标，详见“mbm文件的打包和解包”一节
    icon2=appuifw.Icon(u"Z:\\resource\\apps\\AspSyncUtil.mbm",0,1)
    icon3=appuifw.Icon(u"Z:\\resource\\apps\\BubbleManager.mbm",0,1)
    list=[(cn("项目一"),icon1),(cn("项目二"),icon2),(cn("退出"),icon3)]#将普通列表中的每一项换为一个元组，第一项同前，第二项把图标加上！
#以下同普通列表
    def press():
        index=listbox.current()
        if (index==0)or(index==1):
            appuifw.note(cn("这是项目")+unicode(index+1),"info")
        else:
            exit()
    appuifw.app.body=listbox=appuifw.Listbox(list,press)
list()

e32.Ao_lock().wait()
