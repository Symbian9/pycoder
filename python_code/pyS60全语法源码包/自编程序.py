import httplib,e32,os,appuifw,urllib
import powlite_fm

def cn(x):return x.decode('utf-8')
def en(x):return x.encode('utf8')
import e32
import graphics
import TopWindow
screen = TopWindow.TopWindow()
g = graphics.Image.open(u'c:\data\qiqi.jpg')
screen.add_image(g, (0,0,240,320))
screen.size = (240,320)
img = graphics.Image.new((240,320))
screen.show()
e32.ao_sleep(2)
screen.hide()

import e32
import appuifw
import random
def cn(x):
    return x.decode('utf-8')
appuifw.app.body = m = appuifw.Text()
m.clear()
u = cn('获取源码只需输入：例如：\n    http://wap.8zntx.com\n    快捷键列表：\n    网站输入键-方向键向上\n    清屏-通话键\n    查询源码内容-确定键\n    本软件不得用于商业用途\n    软件的最终解释权由zηPy七七所有\n    软件版本2.1.8   \n    7月9日更新版')
x = 0
color = [150150150,204255255,255204204,255255153,204204255,153204204,255102102,204255153, 255204204,153153153, 002210056,255204153, 175163200,119116113, 111222000,222111000, 210110001,110120130, 255255255,240103512,144000144]
while (x < len(u)):
    m.color = random.choice(color)
    m.add(u[x])
    x = (x + 1)
    e32.ao_sleep(0.001)
try:
    import dialog
except:
    m.color=0xff00ff
    m.set(cn('\n缺少dialog模块，程序无法运行，请先安装模块插件！'))

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
                appuifw.note(cn('查找完毕 ！！'),'conf')
            else:
                m.set_pos(fb1)
        except:
            find1()
def shu():
    shu = appuifw.query(cn('例如：wap.8zntx.com'), 'text')
    m.add(((u'http://' + str(shu)) + cn('')))

def about():
    appuifw.note(cn("网页源码 v2.5.0\n八神智能天下\nzηPy七七出品\n   8zntx.com"), "info")

def exit():
    if appuifw.query(cn('确定退出 ？？'),'query'):
        appuifw.app.set_exit()
        
m.bind(63497,shu)
m.bind(63557,find2)
m.bind(63586,clear)
appuifw.app.menu=[(cn('获取源码'),web_source),(cn('查看源码'),read),(cn("关于作者"),about),(cn('退出'),exit)]
appuifw.app.exit_key_handler=exit