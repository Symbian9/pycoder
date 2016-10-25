# emacs-mode: -*- python-*-
import e32
import appuifw
import graphics
import TopWindow
screen = TopWindow.TopWindow()
g = graphics.Image.open(u'c:\\data\\s60.jpg')
screen.add_image(g, (0,
 0,
 240,
 320))
screen.size = (240,
 320)
img = graphics.Image.new((240,
 320))
screen.show()
e32.ao_sleep(2)
screen.hide()
import os
import envy
import uitricks
from key_tricks import *

def cn(x):
    return x.decode('utf-8')



def exit():
    import random
    appuifw.app.body = m = appuifw.Text()
    appuifw.app.screen = 'full'
    m.clear()
    u = cn('软件名称：智能编程Bata\n软件版本：1.0.0\n软件编辑：宇狼共舞\n测试机型：N73、6120C、N95\n软件介绍：智能编程是一款S60v3手机编程工具，需要py平台及其插件的支持，具有定义模板、傻瓜式操作，短短几天就能使你成为编程高手…使用简单，操作方便，功能实用。\nQQ:1003205747\n八神智能天下：8zntx.com')
    x = 0
    color = [150150150,
     204255255,
     255204204,
     255255153,
     204204255,
     153204204,
     255102102,
     204255153,
     255204204,
     153153153,
     593966,
     255204153,
     175163200,
     119116113,
     111222000,
     222111000,
     210110001,
     110120130,
     255255255,
     240103512,
     144000144]
    while (x < len(u)):
        m.color = random.choice(color)
        m.add(u[x])
        x = (x + 1)
        e32.ao_sleep(3.7682853E-04)

    e32.ao_sleep(1)
    appuifw.app.set_exit()



def ma(x):
    m.add(cn('x'))


aq = appuifw.query
apm = appuifw.popup_menu

def zhong():
    caidan = [cn('换行'),
     cn('缩进4+'),
     cn('缩进8+'),
     cn('文字输入')]
    c = apm(caidan, cn('★常用代码★'))
    if (c == 0):
        m.add(u'\n')
    if (c == 1):
        m.add(u'    ')
    if (c == 2):
        m.add(u'        ')
    if (c == 3):
        a = aq(cn('请输入文字'), 'text', cn(' 输入文字'))
        m.add(((u"cn('" + a) + "')"))



def fwjt():
    caidan = [cn('保存源码'),
     cn('读取文档'),
     cn('复制全文'),
     cn('清空内容'),
     cn('锁定键盘'),
     cn('切换屏幕')]
    c = apm(caidan, cn('★快捷菜单★'))
    if (c == 0):
        save()
    if (c == 1):
        load()
    if (c == 2):
        copy()
    if (c == 3):
        p_2()
    if (c == 4):
        sjp()
    if (c == 5):
        p_1()



def copy():
    import clipboard_CHN
    if clipboard_CHN.Set(m.get()):
        appuifw.note(cn('复制成功'), 'conf')



def sjp():
    import PyKeyLock
    appuifw.note(cn('键盘已锁'), 'conf')
    PyKeyLock.Lock()
    del PyKeyLock



def load():
    global pyfile
    import powlite_fm
    pyfile = powlite_fm.manager().AskUser('c:\\', ext=['.txt',
     '.py'])
    try:
        p = open(pyfile, 'r')
        content = p.read().decode('utf-8')
        p.close()
        m.set(content)
    except:
        appuifw.note(cn('未找到文件'), 'error')



def save():
    if appuifw.query(cn('是否保存当前内容'), 'query'):
        a = appuifw.query(cn('文件名'), 'text', cn('zntx'))
        text = m.get().encode('utf-8')
        o = open((('c:\\data\\' + a.encode('utf8')) + '.py'), 'w')
        o.write(text)
        o.close()
        appuifw.note(cn('保存成功'), 'conf')



def g_1():
    caidan = [cn('文字类型'),
     cn('大小颜色'),
     cn('彩色打字')]
    c = apm(caidan, cn('★高级代码—文字类★'))
    if (c == 0):
        g_1_1()
    if (c == 1):
        g_1_2()
    if (c == 2):
        g_1_3()



def g_1_1():
    w = [cn('阴影'),
     cn('下划线'),
     cn('粗体'),
     cn('删除线'),
     cn('方型抹黑'),
     cn('椭圆抹黑'),
     cn('斜体')]
    c = apm(w, cn('文字类型'))
    if (c == 0):
        x = 'HIGHLIGHT_SHADOW'
    elif (c == 1):
        x = 'STYLE_UNDERLINE'
    elif (c == 2):
        x = 'STYLE_BOLD'
    elif (c == 3):
        x = 'STYLE_STRIKETHROUGH'
    elif (c == 4):
        x = 'HIGHLIGHT_STANDARD'
    elif (c == 5):
        x = 'HIGHLIGHT_ROUNDED'
    elif (c == 6):
        x = 'STYLE_ITALIC'
    m.add((cn('\nm.style=appuifw.') + x))



def g_1_2():
    w = [cn('大'),
     cn('中'),
     cn('小')]
    c = apm(w, cn('大小颜色'))
    if (c == 0):
        m.add(cn("\nfont = u'CombinedChinesePlain16'"))
    elif (c == 1):
        m.add(cn("\nfont = u'CombinedChinesePlain12'"))
    elif (c == 2):
        m.add(cn("\nfont = u'Sans MT 936_S60'"))



def g_1_3():
    m.add(cn("\n#\xe6\x8f\x90\xe5\x8f\x96\xe8\x87\xaa\xe4\xb8\x8a\xe5\xb8\x9d\xe7\x9a\x84\xe5\xb7\xa6\xe6\x89\x8b\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xb2\xbe\xe7\x81\xb5\nimport e32\nimport appuifw\nimport random\ndef cn(x):\n    return x.decode('utf-8')\nappuifw.app.body = m = appuifw.Text()\nm.clear()\nu = cn('\xe8\xbe\x93\xe5\x85\xa5\xe6\x96\x87\xe5\xad\x97')\nx = 0\ncolor = [150150150,204255255,255204204,255255153,204204255,153204204,255102102,204255153, 255204204,153153153, 002210056,255204153, 175163200,119116113, 111222000,222111000, 210110001,110120130, 255255255,240103512,144000144]\nwhile (x < len(u)):\n    m.color = random.choice(color)\n    m.add(u[x])\n    x = (x + 1)\n    e32.ao_sleep(0.001)"))



def g_2():
    caidan = [cn('左右键文字'),
     cn('定义快捷键')]
    c = apm(caidan, cn('★高级代码—按键类★'))
    if (c == 0):
        m.add(cn("\nimport uitricks\nfrom key_tricks import*\n    uitricks.set_text(cn('\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe5\xb7\xa6\xe9\x94\xae\xe6\x96\x87\xe5\xad\x97'),EAknSoftkeyOptions)\n    uitricks.set_text(cn('\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe5\x8f\xb3\xe9\x94\xae\xe6\x96\x87\xe5\xad\x97'),EAknSoftkeyExit)"))
    elif (c == 1):
        import globalui
        k1 = cn(' 代码：42 (*键) 代码：35 (#键)\n 代码：48 (0键) 代码：49 (1键)\n 代码：50 (2键) 代码：51 (3键)\n 代码：52 (4键) 代码：53 (5键)\n 代码：54 (6键) 代码：55 (7键)\n 代码：56 (8键) 代码：57 (9键)\n 代码：8 (删除键)\n 代码：63495 (导航向左)\n 代码：63496 (导航向右)\n 代码：63497 (导航向上)\n 代码：63498 (导航向下)\n 代码：63554 (左软键)\n 代码：63555 (右软键)\n 代码：63556 (关机键)\n 代码：63557 (确认键)\n 代码：63499 (笔型键)\n 代码：63561 (照相键)\n 代码：63570 (菜单键)\n 代码：63586 (通话键)\n 代码：63587 (挂机键)')
        k2 = cn('\n凤舞九天 开发\n保留所有权利\n\n')
        globalui.global_msg_query((k1 + k2), cn('-=*按键代码大全*=-'))
        m.add(cn('\nappuifw.app.body.bind(按键代码,定义函数)'))



def tupian():
    m.add(cn("import e32\nimport graphics\nimport TopWindow\nscreen = TopWindow.TopWindow()\ng = graphics.Image.open(u'c:\\data\\s60.jpg')\nscreen.add_image(g, (0,0,240,320))\nscreen.size = (240,320)\nimg = graphics.Image.new((240,320))\nscreen.show()\ne32.ao_sleep(2)\nscreen.hide()\n#\xe5\x8f\xaf\xe5\xb0\x86240,320\xe6\x94\xb9\xe4\xb8\xba\xe5\x90\x88\xe9\x80\x82\xe7\x9a\x84\xe5\x88\x86\xe8\xbe\xa8\xe7\x8e\x87"))



def k_1():
    a = aq(cn('请输入模块名'), 'text', u'appuifw')
    m.add((cn('\nimport ') + a))
    while 1:
        if aq(cn('继续引入模块？'), 'query'):
            a = aq(cn('请输入模块名'), 'text')
            m.add((cn('\nimport ') + a))
        else:
            m.add(cn('\n'))
            break




def k_2():
    m.add(cn("\ndef cn(x):return x.decode('utf-8')"))



def k_3():
    m.add(cn('\nappuifw.app.body = '))



def k_4():
    m.add(cn('\nappuifw.app.title = '))



def j_1():
    m.add(cn('\nappuifw.app.body = m = appuifw.Text()\nm.set()'))



def j_2():
    m.add(cn("\ndef press():\n    index = listbox.current()\n    if index == 0:\n    elif index == 1:\n    else:\nlist = [cn('\xe7\xbc\x96\xe5\xb8\x96\xe5\x8a\xa9\xe6\x89\x8b'),cn('\xe5\x87\xa4\xe8\x88\x9e\xe4\xb9\x9d\xe5\xa4\xa9'),cn('\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')]\nappuifw.app.body = listbox = appuifw.Listbox(list,press)"))



def j_3():
    m.add(cn('\npage1 = \npage2 = \npage3 = \npage4 = '))
    m.add(cn('\n\ndef action(index):\n    if index == 0:\n        appuifw.app.body = page1\n    if index == 1:\n        appuifw.app.body = page2\n    if index == 2:\n        appuifw.app.body = page3\n    if index == 3:\n        appuifw.app.body = page4'))
    m.add(cn("\nappuifw.app.set_tabs([cn('\xe7\x95\x8c\xe9\x9d\xa2\xe4\xb8\x80')cn('\xe7\x95\x8c\xe9\x9d\xa2\xe4\xba\x8c')cn('\xe7\x95\x8c\xe9\x9d\xa2\xe4\xb8\x89')cn('\xe7\x95\x8c\xe9\x9d\xa2\xe5\x9b\x9b')],action)\nappuifw.app.body = page1"))



def j_4():
    import appuifw



def c_1():
    m.add(cn('\nappuifw.app.menu = '))



def c_2():
    m.add(cn('\nappuifw.app.exit_key_handler = '))



def c_3():
    wang = [cn('一级菜单'),
     cn('二级菜单'),
     cn('弹出菜单')]
    c = apm(wang, cn('请选择菜单类型'))
    if (c == 0):
        yiji()
    elif (c == 1):
        erji()
    elif (c == 2):
        tanchu()



def yiji():
    (a, b,) = appuifw.multi_query(cn('菜单名'), cn('定义动作'))
    m.add(((((cn("\nmenu = [(cn('") + a) + cn("'),")) + b) + cn(')')))
    while 1:
        if aq(cn('继续添加菜单？'), 'query'):
            (a, b,) = appuifw.multi_query(cn('新增菜单'), cn('定义动作'))
            m.add(((((cn(",(cn('") + a) + cn("'),")) + b) + cn(')')))
        else:
            break

    m.add(cn(']'))



def erji():
    a = aq(cn('主菜单名'), 'text', cn('主菜单'))
    m.add(((cn("\nmenu = [(cn('") + a) + cn("'),")))
    (a, b,) = appuifw.multi_query(cn('二级菜单'), cn('定义动作'))
    m.add(((((cn("((cn('") + a) + cn("'),")) + b) + cn(')')))
    while 1:
        if aq(cn('继续添加二级菜单？'), 'query'):
            (a, b,) = appuifw.multi_query(cn('新增菜单'), cn('定义动作'))
            m.add(((((cn(",(cn('") + a) + cn("'),")) + b) + cn(')')))
        else:
            m.add(cn('))'))
            zhu()
            break




def zhu():
    if aq(cn('继续添加主菜单？'), 'query'):
        a = aq(cn('主菜单名'), 'text', cn('主菜单'))
        m.add(((cn(",(cn('") + a) + cn("'),")))
        (a, b,) = appuifw.multi_query(cn('二级菜单'), cn('定义动作'))
        m.add(((((cn("((cn('") + a) + cn("'),")) + b) + cn(')')))
    else:
        if aq(cn('继续添加主菜单？'), 'query'):
            zhu()
        m.add(cn(']'))
    while 1:
        if aq(cn('继续添加二级菜单？'), 'query'):
            (a, b,) = appuifw.multi_query(cn('新增菜单'), cn('定义动作'))
            m.add(((((cn(",(cn('") + a) + cn("'),")) + b) + cn(')')))
        else:
            m.add(cn('))'))
            m.add(cn(']'))
            break




def tanchu():
    (a, b,) = appuifw.multi_query(cn('菜单名一'), cn('菜单名二'))
    m.add((((("\ndef pop():\n    w = [cn('" + a) + "'),cn('") + b) + "')"))
    while 1:
        if aq(cn('继续添加菜单？'), 'query'):
            a = aq(cn('新增菜单'), 'text')
            m.add(((",cn('" + a) + "')"))
        else:
            break

    m.add(cn("]\n    c = appuifw.popup_menu(w,cn('\xe8\xaf\xb7\xe9\x80\x89\xe6\x8b\xa9'))\n    if c == 0:\n    elif c == 1:\n    elif c == 2:"))



def c_4():
    z = aq(cn('提示内容：'), 'text', cn('请输入'))
    wang = [cn('文本输入'),
     cn('数字输入'),
     cn('时间输入'),
     cn('日期输入'),
     cn('密码输入'),
     cn('双项输入')]
    c = apm(wang, cn('请选择提示类型'))
    if (c == 0):
        y = 'text'
    elif (c == 1):
        y = 'number'
    elif (c == 2):
        y = 'time'
    elif (c == 3):
        y = 'date'
    elif (c == 4):
        y = 'code'
    elif (c == 5):
        m.add(cn("\nappuifw.multi_query(cn('\xe4\xb8\x80'),cn('\xe4\xba\x8c'))"))
    m.add((((('\nappuifw.query(' + z) + ',') + y) + ')'))



def c_5():
    z = aq(cn('提示内容：'), 'text', cn('请输入'))
    wang = [cn('提示'),
     cn('错误'),
     cn('正确'),
     cn('询问')]
    c = apm(wang, cn('请选择提示类型'))
    if (c == 0):
        y = 'info'
    elif (c == 1):
        y = 'error'
    elif (c == 2):
        y = 'conf'
    elif (c == 3):
        y = 'query'
    m.add((((('\nappuifw.note(' + z) + ',') + y) + ')'))



def c_6():
    (a, b,) = appuifw.multi_query(cn('函数名：'), cn('定义动作：'))
    m.add((((cn('\ndef ') + a) + cn('():\n    ')) + b))



def c_7():
    m.add(cn("\ndef exit():\n    if aq(cn('\xe6\x98\xaf\xe5\x90\xa6\xe9\x80\x80\xe5\x87\xba\xef\xbc\x9f'),'query'):\n        appuifw.app.set_exit()"))



def p_1():
    if (appuifw.app.screen == 'normal'):
        appuifw.app.screen = 'large'
    elif (appuifw.app.screen == 'large'):
        appuifw.app.screen = 'full'
    else:
        appuifw.app.screen = 'normal'



def p_2():
    m.set('')



def p_3():
    global text
    text = aq(cn('输入查找内容'), 'text')
    pos = m.get().find(text)
    if (pos < 0):
        appuifw.note(cn('未搜索到！'), 'info')
    else:
        m.set_pos(pos)



def p_4():
    global pos
    try:
        poss = m.get().find(text, (pos + 1))
        pos = poss
        if (poss < 0):
            if appuifw.query(cn('已搜索到结尾，\n是否从头开始？'), 'query'):
                p_4()
        else:
            m.set_pos(poss)
    except:
        p_3()



def p_5():
    m.set_pos(0)



def p_6():
    m.set_pos(m.len())



def p_7():
    pos = appuifw.app.body.get_pos()
    text = appuifw.app.body.len()
    percentage = aq(cn((('转至几%？(当前' + str(((pos * 100) / text))) + '%)')), 'number')
    if 0 < percentage < 101:
        chr = int(round((float(text) * (float(percentage) / 100.0))))
        appuifw.app.body.set_pos(chr)
    elif (percentage > 100):
        appuifw.note('！', 'error')



def p_8():
    pos = appuifw.app.body.get_pos()
    text = appuifw.app.body.get()
    x = []
    for i in text:
        if (i[-1] == u'\u2029'):
            x.append(i)

    p = aq(cn((('跳转行数到？(共有' + str((len(x) + 1))) + '行)')), 'number', cn('1'))
    if (p > (len(x) + 1)):
        er('已超过行数')
    elif 0 <= p <= (len(x) + 1):
        try:
            m.set_pos(0)
            ns((p - 1))
        except:
            appuifw.note(cn('错误'), 'error')
            m.set_pos(a)



def ns(oo):
    pos = m.get_pos()
    c = m.get()
    if (pos == len(c)):
        m.set_pos(len(c))
    get = c[pos:]
    try:
        g = get.split(u'\u2029')
        if (oo == -1):
            appuifw.note(cn('没有第0行！'), 'info')
        elif (len(g) > oo):
            a = 0
            for o in range(0, oo):
                a += (len(g[o]) + 1)

            m.set_pos((pos + a))
        else:
            m.set_pos(len(c))
    except:
        appuifw.note(cn('错误'), 'error')
        return 


appuifw.app.title = cn('智能编程')
appuifw.app.screen = 'normal'
appuifw.app.body = m = appuifw.Text()
m.color = 16711680
m.set(cn('智能编程'))
m.color = 50
m.add(cn('操作指南：'))
m.color = 255
m.add(cn('\n    按绿键可快速切换屏幕\n    按确认键直接添加常用代码\n    左菜单键可保存载入文件\n    红键锁按红键自动隐藏\n    使用模板编程时可将内容按需要修改\n    保存的源码不能直接使用需修改\n    全文复制可复制到剪贴板'))
m.color = 255
appuifw.app.body.bind(63586, p_1)
appuifw.app.body.bind(63557, zhong)
envy.set_app_system(1)
uitricks.set_text(cn('捷径'), EAknSoftkeyExit)
appuifw.app.menu = [(cn('开始编写'),
  ((cn('加载模块'),
    k_1),
   (cn('定义文字'),
    k_2),
   (cn('屏幕大小'),
    k_3),
   (cn('定义标题'),
    k_4),
   (cn('文字界面'),
    j_1),
   (cn('列表界面'),
    j_2),
   (cn('折叠界面'),
    j_3))),
 (cn('常用代码'),
  ((cn('定义函数'),
    c_6),
   (cn('定义左键'),
    c_1),
   (cn('定义右键'),
    c_2),
   (cn('定义菜单'),
    c_3),
   (cn('退出语句'),
    c_7),
   (cn('输  入  框'),
    c_4),
   (cn('提  示  框'),
    c_5))),
 (cn('高级代码'),
  ((cn('文字类'),
    g_1),
   (cn('按键类'),
    g_2),
   (cn('随显图片'),
    tupian))),
 (cn('编辑操作'),
  ((cn('查找文字'),
    p_3),
   (cn('查找下个'),
    p_4),
   (cn('转到开头'),
    p_5),
   (cn('转到结尾'),
    p_6),
   (cn('转百分比'),
    p_7),
   (cn('跳转行数'),
    p_8))),
 (cn('退出程序'),
  exit)]
appuifw.app.exit_key_handler = fwjt

# local variables:
# tab-width: 4