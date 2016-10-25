import appuifw
def cn(x):return x.decode("utf-8")
def add():
    m.add(cn("ID:5799"))
def qiq():
    m.add(cn("nzηPy七七"))
def clear():
    m.set("")
def about():
    appuifw.note(cn("小其信息 v0.01\n八神智能天下\n七七作品\n   8zntx.com"), "info")
def exit():
    if appuifw.query(cn("要退出吗"),"query"):
        appuifw.app.set_exit()

appuifw.app.body = m = appuifw.Text()
m.set(u"8zntx.com")
m.add(cn("\七七个人资料"))
appuifw.app.menu = [(cn("八神ID"),add),(cn("八神名称"),qiq),(cn("清除屏幕"),clear),(cn("关于作者"),about),(cn("退出程序"),exit)]
