import appuifw
import e32


def cn(x):
    return x.decode('utf-8')

appuifw.app.title = cn('八神编贴助手V0.3.2\nBy:捞坚')

def exit():
    appuifw.note(cn('感谢使用本作品！！'),'info')
    appuifw.app.set_exit()




def alist():
    appuifw.app.screen = 'normal'
    def press():
        index = listbox.current()
        if index == 0:
            txt()
        elif index == 1:
            about()
        else:
            appuifw.note(cn('请用手机登陆\nwap.8zntx.com\nN70/72版区'),'info')

    appuifw.app.menu = [(cn('进入'),txt),(cn('退出'),exit)]

    list = [cn('进入编贴助手'),cn('关于帮助[必读]'),cn('联系我们')]
    appuifw.app.body = listbox = appuifw.Listbox(list,press)
    appuifw.app.exit_key_handler = exit



def about():
    appuifw.app.screen = 'full'
    appuifw.app.body=tt=appuifw.Text()
    tt.set(cn('\n此版本号为V0.3.2，专为八神智能天下--6.10更新打造，您可按个人须要而对作品进行修改或发布。但必须征得本人同意的情况下进行，请您自觉尊守。\n为了使此作品更人性化，如有必要的修改或发现Bug，请上报。我会尽量满足您的要求或更改。\n最后祝您使用愉快！！\n更多资源请手机登陆:\nwap.8Zntx.Com    /by:捞坚。\n\n\n\n'))
    tt.add(u'******\u611f\u8c22\u4f7f\u7528\u635e\u575a\u4f5c\u54c1******\n\n                  \u590d\u5236\u8bf7\u6309    \n     \u201c\u7b14\u5f62\u952e\u201d\u002b\u201c\u5bfc\u822a\u952e\u201d')
    tt.color =0xff0000
    tt.add(u'\n\n  \u6362\u884c\u4ee3\u7801\u5feb\u6377\u952e\u4e3a\u5bfc\u822a\u4e2d\u5fc3\u952e\n\n\u5173\u4e8e\u4f5c\u54c1\u8bf7\u6309\u53f3\u952e\u7ee7\u7eed\u003e\u003e\u003e\n\n')
    appuifw.app.menu = [(cn('进入编贴助手'),txt),(cn('返回'),alist)]
    appuifw.app.exit_key_handler = alist


def txt():
    global m
    try:
        appuifw.app.body = m = appuifw.Text(m.get())
    except:
        appuifw.app.body = m = appuifw.Text()

    appuifw.app.screen = 'normal'

    m.bind(63557,lambda:m.add(u'[br]'))

    def exit2():
        if appuifw.query(cn('是否保存编贴内容？？'),'query'):
            text = m.get().encode('utf-8')
            f = open('E:\\system\\apps\\biaxi\\zntx.txt','w')
            f.write(text)
            f.close()
            appuifw.note(cn('保存成功！！\n感谢使用捞坚作品！！'),'conf')
            alist()
        else:
            alist()
#exit保存


    def load():
        try:
            z = open('E:\\system\\apps\\biaxi\\zntx.txt','r')
            content = z.read().decode('utf-8')
            z.close()
            m.add(content)
        except:
            appuifw.note(cn('找不到以存贴子！！\n请确定作品安装在E盘！！'),'error')
    def save():
        if appuifw.query(cn('是否储存当前内容？？'),'query'):
            text = m.get().encode('utf-8')
            s = open('E:\\system\\apps\\biaxi\\zntx.txt','w')
            s.write(text)
            s.close()
            appuifw.note(cn('保存成功！！\n感谢使用捞坚作品！！'),'conf')
#菜单存读

    def yy():
        appuifw.app.body = mm =appuifw.Text()
        mm.color = 0x0000ff
        appuifw.app.screen = 'full'
        mm.set(m.get().replace('[br]','\n').replace('[hello]',cn('<问候语>')).replace('[weekday]',cn('<系统星期>')).replace('[now]',cn('<系统时间>')).replace('[ttcc]',cn('<农历时间>')).replace('[nickname]',cn('<显示昵称>')))
        appuifw.app.menu = [(cn('返回'),txt)]
        appuifw.app.exit_key_handler = txt
#预览


    def coin():
        money = appuifw.query(cn('请输入金钱数：'),'number')
        m.add(u'[coin='+str(money)+cn(']内容[/coin]'))
    def grade():
        lv = appuifw.query(cn('请输入等级数：'),'number')
        m.add(u'[grade='+str(lv)+cn(']内容[/grade]'))
    def buy():
        gq = appuifw.query(cn('请输入金钱数：'),'number')
        m.add(u'[buy='+str(gq)+cn(']内容[/buy]'))


    appuifw.app.menu = [\
(cn('*ubb*代码'),\
(\
(cn('加粗字体'),lambda:m.add(cn('[b]内容[/b]'))),\
(cn('下划线'),lambda:m.add(cn('[u]内容[/u]'))),\
(cn('斜体'),lambda:m.add(cn('[i]内容[/i]'))),\
(cn('换行'),lambda:m.add(cn('[br]'))),\
(cn('分切页面'),lambda:m.add(cn('[next]'))),\
(cn('网页连接'),lambda:m.add(cn('[url=网页地址]显示内容[/url]'))),\
(cn('网络图片'),lambda:m.add(cn('[img]图片地址[/img]'))),\
(cn('问候语'),lambda:m.add(u'[hello]')),\
(cn('显示昵称'),lambda:m.add(u'[nickname]')),\
(cn('显示农历'),lambda:m.add(u'[ttcc]')),\
(cn('系统时间'),lambda:m.add(u'[now]')),\
(cn('系统星期'),lambda:m.add(u'[weekday]'))\
)),\
\
\
(cn('*可见贴*'),\
(\
(cn('登陆可见'),lambda:m.add(cn('[login]内容[/login]'))),\
(cn('手机可见'),lambda:m.add(cn('[mobi]内容[/mobi]'))),\
(cn('金钱可见'),coin),\
(cn('等级可见'),grade),\
(cn('付费可见'),buy)\
)),\
\
\
(cn('屏幕'),\
(\
(cn('清空屏幕'),lambda:m.set('')),\
(cn('隔离文字'),lambda:m.add(u'[br]\n[br]\n[br]')),\
(cn('预览贴子'),yy)\
)),\
\
\
(cn('模拟贴'),\
(\
(cn('软件发布'),mko),\
(cn('主题发布'),mkt)\
)),\
\
(cn('保存与读取'),\
(\
(cn('保存'),save),\
(cn('读取'),load)\
)),\
\
(cn('打开UcWeb60'),uc),\
]

    appuifw.app.exit_key_handler = exit2

def mko():
    m.add(cn('[br][英文名称]：[br][中文名称]： [br][版本信息]： [br][开发人员]：[br][软件类型]：[br][授权方式]： [br][测试机型]：[br][测试人员]：[br][软件平台]：[br][软件功能]：[br][软件说明]：[br][支持机型]：'))
def mkt():
    m.add(cn('[br][主题名称]： [br][制作人员]：[br][图片素材]：[br][主题类型]：[br][测试机型]：[br][测试人员]：[br][主题说明]：[br][支持机型]：'))

def uc():
    m.add(u'\n\n    *****\u611f\u8c22\u4f7f\u7528\u672c\u4f5c\u54c1*****\n\u5982\u4e0d\u80fd\u6b63\u5e38\u6253\u5f00\u8bf7\u68c0\u67e5\u662f\u5426\u5b89\u88c5\u4e86\u0055\u0063\u0077\u0065\u0062\u0036\u0030\u7248\u672c\u3001\u5b89\u88c5\u8def\u7ecf\u662f\u5426\u4e3a\u0045\u76d8!!\n')
    e32.start_exe('z:\\system\\programs\\apprun.exe','e:\\system\\apps\\ucweb60\\ucweb60.app')
#ucweb60

alist()
