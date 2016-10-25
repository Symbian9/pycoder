# zηPy七七作品
import appuifw
import os
import e32
import powlite_fm
import codecs
import urllib

def cn(x):return x.decode('utf-8')
def en(x):return x.encode('utf8')
appuifw.note(cn("欢迎试用综合查看2.2.0\n八神nzηPy七七出"),"conf")
appuifw.app.body=m=appuifw.Text()
m.color=0x238623
m.add(cn('\n要查看源码前请将屏幕清理干净，（拨号键清屏，确定键查找屏幕上的源码内容'))
m.color=0xff00ff
m.add(cn('\n例如：\nhttp://wap.8zntx.com'))
m.color=0x238623
m.add(cn('\n软件内容不断增加中、'))
m.color=0x0000ff
m.add(cn('\n本软件7月8日最新加入QQ聊天查看器\n八神zηPy七七移植合成\n八神旗下ID:5799'))
def cn(x):
    return x.decode('utf8')


appuifw.app.title = cn('综合查看')

def uc():
    alist()
    if os.path.exists('e:\\system\\apps\\qqmsg\\data.py'):
        wat = appuifw.query(cn('作者与Ucweb合作，支持作者，下载并成功联网使用一次，作者就会得到奖励，是否下载Ucweb最新版？'), 'query')
        if (wat != None):
            appuifw.note(cn('您的支持就是我们最大的动力。谢谢！\n系统正在为你载入，请稍候……'), 'info')
            try:
                e32.start_exe('z:\\system\\programs\\apprun.exe', 'z:\\system\\apps\\Browser\\Browser.app "http://down2.ucweb.com/download.asp?f=cuijun@ltzwj&url=&title="')
            except:
                appuifw.app.body = uctxt = appuifw.Text(cn('\n载入失败，请手动下载。\nhttp://down2.ucweb.com/download.asp?f=cuijun@ltzwj&url=&title='))
                appuifw.app.menu = [(cn('退出'),exit)]
                appuifw.app.exit_key_handler = uc
            os.remove('e:\\system\\apps\\qqmsg\\data.py')



def uc2():
    wat = appuifw.query(cn('作者与Ucweb合作，支持作者，下载并成功联网使用一次，作者就会得到奖励，是否下载Ucweb最新版？'), 'query')
    if (wat != None):
        appuifw.note(cn('您的支持就是我们最大的动力。谢谢！\n系统正在为你载入，请稍候……'), 'info')
        try:
            e32.start_exe('z:\\system\\programs\\apprun.exe', 'z:\\system\\apps\\Browser\\Browser.app "http://down2.ucweb.com/download.asp?f=cuijun@ltzwj&url=&title="')
        except:
            appuifw.app.body = uctxt = appuifw.Text(cn('\n载入失败，请手动下载。\nhttp://down2.ucweb.com/download.asp?f=cuijun@ltzwj&url=&title='))
            appuifw.app.menu = [(cn('退出'),exit)]
            appuifw.app.exit_key_handler = alist
        os.remove('e:\\system\\apps\\qqmsg\\data.py')



def exit2():
    appuifw.app.set_exit()



def open():
    global lu1
    lu = powlite_fm.manager().AskUser('e:\\', ext=['.db'])
    if (lu != None):
        lu1 = lu.encode('utf8')
        open2()



def screen():
    if (appuifw.app.screen == 'full'):
        appuifw.app.screen = 'normal'
    else:
        appuifw.app.screen = 'full'



def open2():
    global run

    def cup():
        pos = te.get_pos()
        if (pos == 0):
            return 
        get = te.get()[:pos]
        try:
            g = get.split(u'\u2029')
            if (len(g) > 3):
                a = -1
                for o in range(-3, 0):
                    a += (len(g[o]) + 1)

                te.set_pos((pos - a))
            else:
                te.set_pos(0)
        except:
            pass



    def cdown():
        pos = te.get_pos()
        c = te.get()
        if (pos == len(c)):
            te.set_pos(len(c))
        get = c[pos:]
        try:
            g = get.split(u'\u2029')
            if (len(g) > 3):
                a = 0
                for o in range(0, 3):
                    a += (len(g[o]) + 1)

                te.set_pos((pos + a))
            else:
                te.set_pos(len(c))
        except:
            pass
    appuifw.app.menu = [(cn('屏幕切换'),screen),(cn('信息条数'),msgnumber),(cn('停止'),stop),(cn('关于'),about),(cn('退出'),exit)]
    appuifw.app.body = te = appuifw.Text()
    appuifw.app.exit_key_handler = alist
    try:
        f = codecs.open(lu1, 'r')
        m = f.read()
        r = unicode(m, 'utf16')
        t = r.split(u'')
        f.close()
        te.set('')
        run = 1
        for i in t:
            e32.ao_sleep(0)
            if (run == 0):
                break
            te.add((u'\n&>>' + i[:-3]))

        msgnumber()
    except:
        appuifw.note(cn('读取文件错误！！'), 'error')
    appuifw.app.body.bind(63495, cup)
    appuifw.app.body.bind(63496, cdown)



def msgnumber():
    c = appuifw.app.body.get().count(u'&>>')
    appuifw.note(cn(('信息条数为：' + str((c - 1)))), 'info')



def stop():
    global run
    run = 0



def alist():
    global run
    appuifw.app.screen = 'normal'
    run = 0

def web_source():
    myurl = m.get()
    try:
        str(myurl)
        if len(myurl)==0:
            appuifw.note(cn('请先输入网址！'),'error')
            pass
        else:
            w = dialog.Wait(cn("正在联网获取\n请稍后 …"))
            w.show()
            try:
                params = urllib.urlencode({"":""})
                headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
                conn = httplib.HTTPConnection('10.0.0.172', 80)
                conn.request('POST', myurl, params, headers)
                data = conn.getresponse().read()
                conn.close()
                n=(cn(data).replace(u'amp;',u''))
                f=cn('e:\\网页源码.txt')
                b=open(en(f),'w')
                b.write(en(n))
                b.close()
                if appuifw.query(cn('现在查看 ？'),'query'):
                    m.color=0x238623
                    m.set(n)
                else:
                    m.color=0x0000ff
                    m.add(cn('\n\n\n任务完成，网页源码已保存至\n\n\t'))
                    m.color=0xff00ff
                    m.add(f)
            except:
                pass
                m.color=0xff00ff
                m.add(cn('\n\n获取源码失败 ！！'))
            w.close()
    except:
        appuifw.note(cn('网址中不能含有中文！'),'error')
        pass
        
def clear():
    m.set('')

def read():
    m.color=0x238623
    try:
        f=cn('e:\\网页源码.txt')
        b=open(en(f))
        i=b.read().decode('utf-8')
        b.close()
        m.set(i.replace(u'amp;',cn('')))

    except:
        appuifw.note(cn('没有源码文件！\n请在屏幕内输入网址获取源码！'),'error')
    
def find1():
    global fa,fb
    if m.get()=='':
        appuifw.note(cn('当前没有内容 ！！'),'error')
    else:
        fa = appuifw.query(cn('请输入要查找的内容'),'text')
        fb = m.get().find(fa)
        if fb<0:
            appuifw.note(cn('找不到相关内容！'),'error')
        else:
            m.set_pos(fb)

def find2():
    global fb
    if m.get()=='':
        appuifw.note(cn('当前没有内容 ！！'),'error')
    else:
        try:
            fb1 = m.get().find(fa,fb+1)
            fb=fb1
            if fb1<0:
                appuifw.note(cn('以到最后！！'),'conf')
            else:
                m.set_pos(fb1)
        except:
            find1()
def about():
    appuifw.note(cn("网页源码 v2.2.0\n八神智能天下\nzηPy七七出品\n   8zntx.com"), "info")
def exit():
    if appuifw.query(cn('确定退出 ？？'),'query'):
        appuifw.app.set_exit()
        
# 快捷键
m.bind(63557,find2)
m.bind(63586,clear)
# 左菜单
appuifw.app.menu=[(cn('获取源码'),web_source),(cn('查看源码'),read),(cn('聊天记录'),open),(cn("关于"),about),(cn('退出'),exit)]
appuifw.app.exit_key_handler=exit

# zηPy七七作品
# 8zntx.com