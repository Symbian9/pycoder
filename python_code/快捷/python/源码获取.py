import httplib,e32,appuifw,urllib,dialog

def cn(x):return x.decode('utf-8')
def en(x):return x.encode('utf8')
def exit():
    if appuifw.query(cn('要退出 吗？'),'query'):
        appuifw.app.set_exit()

appuifw.app.body=m=appuifw.Text()
m.color=0x2386ff
m.add(cn('请先清空屏幕，然后将需要获取源码的网页地址写在此界面上。按拨号键清屏。'))

def web_source():
    try:
        myurl = m.get()
        str(myurl)
        w = dialog.Wait(cn("正在联网获取\n请稍后 …"))
        w.show()
        params = urllib.urlencode({"":""})
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        conn = httplib.HTTPConnection('10.0.0.172', 80)
        conn.request('POST', myurl, params, headers)
        data = conn.getresponse().read()
        conn.close()
        m.set(cn(data))
    except:
        appuifw.note(cn("无法获取！"),"error")
        m.set(cn("网页源码无法获取，可能发生了以下错误：\n1.网址中含中文\n2.网址不存在\n3.网址没以“http://”开头\n4.用户处于离线状态"))

def clear():
    m.set('')

m.bind(63586,clear)
appuifw.app.menu=[(cn('获取源码'),web_source),(cn('清除屏幕'),clear),(cn('退出'),exit)]
appuifw.app.exit_key_handler=exit
e32.Ao_lock().wait()