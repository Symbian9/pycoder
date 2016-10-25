import appuifw

def cn(x):return x.decode("utf-8")

appuifw.note(cn("你好欢迎查看七七资料"),"conf")
def dakai():
    turl=appuifw.query(cn("请输入要查询的网址:"),'text',u'http://8zntx.com')
    appuifw.app.body.color = 0
    m.set(cn("           运行信息："))
    m.add(cn("\n您输入的网址是：\n")+turl)
    conn = httplib.HTTPConnection('10.0.0.172', 80)
    conn.request('GET', turl)
    r = conn.getresponse()
    m.add(cn("\n正在读取…"))
    asp = r.read()    
    f = open('e://8zntxwml.asp', 'w')
    f.write(asp)
    f.close()
    dirname = en(powlite_fm.manager().AskUser(path='E:\\', find='dir'))
    name = appuifw.query(cn('请输入名称'), 'text', cn('八神源码'))
    filename = en(dirname + name+'.txt')
    os.rename('e://8zntxwml.asp',filename)
    m.add(cn("\n任务完成！\n请用JBAK DEdit查看"))
    appuifw.note(cn('任务完成'),'info')
    e32.ao_sleep(0.8)    
    main()

def about():
    appuifw.note(cn("网页源码 v0.01\n八神智能天下\n七七作品\n   zntx.org.cn"), "info")

def exit():
    if appuifw.query(cn("要退出吗"),"query"):
        appuifw.app.set_exit()
appuifw.app.menu = [(cn("打开网址"),dakai),(cn("关于"),about),(cn("退出"),exit)]
appuifw.app.exit_key_handler=exit
main()