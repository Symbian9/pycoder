# emacs-mode: -*- python-*-
import appuifw
import os
import e32
import powlite_fm
import codecs

def cn(x):
    return x.decode('utf8')


appuifw.app.title = cn('QQmsg.v0.1')

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
                appuifw.app.menu = [(cn('返回'),
                  uc)]
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
            appuifw.app.menu = [(cn('返回'),
              alist)]
            appuifw.app.exit_key_handler = alist
        os.remove('e:\\system\\apps\\qqmsg\\data.py')



def exit2():
    appuifw.app.set_exit()



def open():
    global lu1
    lu = powlite_fm.manager().AskUser('e:\\qq\\', ext=['.db'])
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


    appuifw.app.menu = [(cn('屏幕切换'),
      screen),
     (cn('停止'),
      stop),
     (cn('信息条数'),
      msgnumber),
     (cn('返回'),
      alist),
     (cn('支持作者'),
      uc2)]
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

    def press():
        index = listbox.current()
        if (index == 0):
            open()
        elif (index == 1):
            (allabout(),
             about1())
        elif (index == 2):
            (allabout(),
             about2())
        elif (index == 3):
            uc2()
    appuifw.app.body = listbox = appuifw.Listbox(list, press)
    appuifw.app.exit_key_handler = exit2
    appuifw.app.menu = [(cn('查看聊天记录'),open),(cn('帮助'),about1),(cn('关于'),about2),(cn('支持作者'),uc2)]



def allabout():
    appuifw.app.exit_key_handler = alist
    appuifw.app.screen = 'full'



def about1():
    appuifw.app.body = appuifw.Text(cn('\t感谢使用捞坚作品\n本作品还有待完善的地方。\n这版本存在快捷键Bug，和读取信息时不能达到屏幕常亮的效果。由于没找到解决方案，所以暂时用着。以后慢慢优化起来。\n>>翻页快捷键为:导航向左和右\n最后感谢您的支持，如果更好的方案请联系：\nQQ:297012226\n\t\t    QQmsg@by:捞坚'))



def about2():
    appuifw.app.body = appuifw.Text(cn('\t感谢使用捞坚作品\n多谢你们一路的支持.如果你满意本作品的你可以通过支持作者去下载最新的Ucweb浏览器，因作者与Ucweb作了推广协议。你每次下载并成功联网使用一次，我就会从Ucweb那里得到那一点的劳动成果(也算是报酬拉,哈)，最后感谢您的支持，如果更好的方案请联系：\nQQ:297012226\n\t\tQQmsg@by:捞坚'))


uc()

# local variables:
# tab-width: 4