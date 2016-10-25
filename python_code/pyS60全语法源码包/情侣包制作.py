#connwap135@vip.qq.com
#QQ223081080,635516282,1107853339
#回忆不受伤
import appuifw
import e32
import os,os.path
import re
import httplib
import graphics
import urllib
import socket
from dialog import Wait
DB_FILE = u"c:\\system\\qzone_set.cfg"
class _FancyURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN78-1/21.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
def cn(x):
    return x.decode('utf-8')
def set_body(text=''):
    body.clear()
    body.focus=False
    body.color=0x0000fe
    body.style = ((appuifw.STYLE_BOLD | appuifw.STYLE_ITALIC) | appuifw.HIGHLIGHT_SHADOW)
    body.font='symbol'
    body.set(cn('手机腾讯网QQ空间助手1.2beta\n\t'))
    body.style = ((appuifw.STYLE_BOLD | appuifw.STYLE_ITALIC) | appuifw.STYLE_UNDERLINE|appuifw.HIGHLIGHT_SHADOW)
    body.font='symbol'
    body.add(cn('(http://z.qq.com)\n'))
    body.color=0xffffff
    body.style = appuifw.HIGHLIGHT_ROUNDED
    body.add(cn('谢谢你的使用,如有任何意见及建议请到QQ空间留言或邮件至connwap135@vip.qq.com'))
    body.color=0x333333
    body.style=appuifw.STYLE_BOLD
    body.font='symbol'
    body.add(text)
    body.set_pos(0)
def get(url,u=False):
        content=''
        try:
            try:
                conn=_FancyURLopener()
                conn.addheader('Accept', 'text/plain')
                chou=conn.open(url)
                if u:content=chou.read()
                chou.close()
            except:
                conn = httplib.HTTPConnection('10.0.0.172', 80)
#                conn.debuglevel=1
                conn.putrequest('GET', url)
                conn.putheader('Accept', 'text/plain')
                conn.putheader('User-Agent','Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN78-1/21.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')            
                conn.endheaders()
                if u:content = conn.getresponse().read()
                conn.close()
        except:
            appuifw.note(unicode('网络连接异常或服务器繁忙，请稍后重试','utf-8'),'error')
        return content

def post(url, data):
        content=''
        try:
            try:
                conn=_FancyURLopener()
                conn.addheader('Accept', 'text/plain')
                chou=conn.open(url, data)
                content=chou.read()
                chou.close()                
            except:
                conn = httplib.HTTPConnection('10.0.0.172', 80)
                conn.putrequest('POST',url)
                conn.putheader('Accept', 'text/plain')
                conn.putheader('User-Agent','Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN78-1/21.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
                conn.putheader('Content-type','application/x-www-form-urlencoded')
                conn.putheader('Content-length', '%d' % len(data))
                conn.endheaders()
                conn.send(data)
                content = conn.getresponse().read()
                conn.close()
        except:
            appuifw.note(unicode('网络连接异常或服务器繁忙，请稍后重试','utf-8'),'error')
        return content
def bugout(text):
    rf=open('c:\\a.txt','w')
    print>>rf,text
    rf.close()    
def step1(url='http://z.qq.com'):
    x=get(url,True)
    r='<card(?:(?:\\s*.*?\\s)|(?:\\s+))ontimer=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'
    x1=re.compile(r).findall(x)
    return x1[0].strip('"/').replace('amp;','')

def lookurl(url,check):
    z=get(url,True)
    z=z.replace('<a','\r\n<a')
    r='<a(?:(?:\\s*.*?\\s)|(?:\\s+))href=(?P<url>\S*?)(?:(?:\\s.*>)|(?:>))(?P<name>.*?)</a>'
    x1=re.compile(r).findall(z)
    for n in x1:
        if n[1]==check:
            return n[0].strip('"').replace('amp;','')
            break
def open_browser():
    try:
        e32.start_exe('BrowserNG.exe',' "4 %s"' %myzone_url,0)
    except:
        appuifw.note(cn('没有提取到你的sid信息，请点击开始得到sid信息后再试！'),'info')
def update_browser():
    appuifw.note(cn('无可用更新版本！'),'info')
    appuifw.note(cn('您所使用的已经是最新版本了！'),'info')
def get_sid(loginurl,qq,mm):
    global myzone_url
    p=get(loginurl,True)
    r1='<go(?:(?:\\s*.*?\\s)|(?:\\s+))href=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'
    r2='<postfield(?:(?:\\s*.*?\\s)|(?:\\s+))value=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'
    r2_1='<postfield(?:(?:\\s*.*?\\s)|(?:\\s+))name=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'
    r3='<card(?:(?:\\s*.*?\\s)|(?:\\s+))ontimer=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'
    r4='<img(?:(?:\\s*.*?\\s)|(?:\\s+))src=(?P<val>\S*?)(?:(?:\\s.*>)|(?:>))'    
    x1=re.compile(r1).findall(p)
    x2=re.compile(r2).findall(p)
    x3=re.compile(r2_1).findall(p)
    purl=x1[0].strip('"').replace('amp;','')
    data=''
    for index in range(len(x2)):
        fname=x3[index].strip('"')
        fvalue=x2[index].strip('" /')
#        body.add(cn('\n'+fname+','+fvalue+'\n'))
        if fname=='qq':fvalue=str(qq)
        if fname=='pwd':fvalue=str(mm)
        data+=urllib.urlencode({fname:fvalue})+'&'
    params = data[:len(data)-1]
    ym=post(purl,params)
    try:
        iconurls=re.compile(r4).findall(ym)
        imgurl=iconurls[0].strip('"')
        urllib.urlretrieve(imgurl,'d:\\system\\data\\temp.gif')
        img = graphics.Image.open('d:\\system\\data\\temp.gif')
        old_body = appuifw.app.body
        def handle_redraw(rect):
            img.rectangle((0,0,100,2), fill = (255,0,0))
            img.rectangle((0,0,2,40), fill = (255,0,0))
            img.rectangle((98,0,100,40), fill = (255,0,0))
            img.rectangle((0,38,100,40), fill = (255,0,0))
            canvas.blit(img, target=(70,70,0,0), scale=0)
            canvas.text((10, 50), cn('你必需输入下面的验证码'),fill=(255, 0, 0),font='symbol')
        canvas = appuifw.Canvas(redraw_callback=handle_redraw)
        appuifw.app.body = canvas
        appuifw.e32.ao_yield()
        verify=0
        while len(str(verify))!=4:
            verify = appuifw.query(cn('请输入图片上4位数字验证码:\n'), 'number')
            if verify<10:
                verify='000'+str(verify)
            elif verify<100:
                verify='00'+str(verify)
            elif verify<1000:
                verify='0'+str(verify)
        appuifw.app.body=old_body
        gourls=re.compile(r1).findall(ym)
        gourl=gourls[1]
        login2url=gourl.strip('"')
        pos1=ym.find(gourl)
        pos2=len(ym)
        postdata=re.compile(r2).findall(ym[pos1:pos2])
        postname=re.compile(r2_1).findall(ym[pos1:pos2])
        data=''
        for index in range(len(postdata)):
            fname=postname[index].strip('"')
            fvalue=postdata[index].strip('"/')
            if fname=='verify':fvalue=verify
            data+=urllib.urlencode({fname:fvalue})+'&'
        params1 = data[:len(data)-1]
        ym=post(login2url,params1)
    except:
        pass
    myzone_url_find=re.compile(r3).findall(ym)
    myzone_url=myzone_url_find[0].strip('"/').replace('amp;','')
    x1=ym.find('amp;sid=')
    x2=ym[x1+8:]
    x3=x2.find('==')
    x4=x2[:x3+2]
    return x4
def readnext(url):
    z=get(url,True)
    z=z.replace('<a','\r\n<a')
    r='<a(?:(?:\\s*.*?\\s)|(?:\\s+))href=(?P<url>\S*?)(?:(?:\\s.*>)|(?:>))(?P<name>.*?)</a>'
    x1=re.compile(r).findall(z)
    for n in x1:
        if n[1]=='\xe4\xb8\x8b\xe9\xa1\xb5':
            break
        set_body(cn('正在模拟阅读日志:\n')+cn(n[1]))
        get(n[0].strip('"').replace('amp;',''))
def sel_access_point():
        aps =[]
        aps.append({'iapid': 1, 'name': u'Easy WLAN'})
        for api in socket.access_points():
            aps.append(api)
        ap_labels = map(lambda x: x['name'], aps)
        item = appuifw.popup_menu(ap_labels,cn('选择接入点:'))        
        return aps[item]['iapid']
def set_s():
        list=[]
        apid = sel_access_point()
        list.append(apid)
        yq=appuifw.query('qq号码：'.decode('utf-8'),'number',223081080)
        ym=appuifw.query('qq密码：'.decode('utf-8'),'code')    
        if yq and ym:
            list.append(yq)
            list.append(ym)
            f = file(DB_FILE, "w")
            for item in list:
                print >> f, item
            f.close()            
            appuifw.note('保存设置！'.decode('utf-8'),'conf')
def shua():
    if os.path.exists(DB_FILE):
        f = file(DB_FILE, "r")
        lst = []
        for line in f:
            lst.append(line.strip())
        f.close()
        apid=lst[0]
        cq=lst[1]
        cm=lst[2]
    else:
        list=[]
        apid = sel_access_point()
        list.append(apid)
        yq=appuifw.query('qq号码：'.decode('utf-8'),'number',223081080)
        ym=appuifw.query('qq密码：'.decode('utf-8'),'code')    
        if yq and ym:
            list.append(yq)
            list.append(ym)
            cq,cm=yq,ym
            f = file(DB_FILE, "w")
            for item in list:
                print >> f, item
            f.close()
    def cancel_cb():
        pass
    point=socket.access_point(int(apid))
    socket.set_default_access_point(point)
    dlg = Wait(cn('正在连接网络'), False, cancel_cb)
    dlg.show()
    set_body(cn('正在连接网络'))
    get('http://z.qq.com')
    dlg.set_label(cn('请等待…\n正在获取网页地址'))
    a=step1('http://z.qq.com')
    set_body('打开网页'.decode('utf-8')+a)
    #过滤登录我的QQ空间
    strgl='\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x91\xe7\x9a\x84QQ\xe7\xa9\xba\xe9\x97\xb4'
    dlg.set_label(cn('如果您长期停留在某一界面请尝试更换接入点或退出程序稍后再试…'))
    c=lookurl(a,strgl)
    set_body('打开网页'.decode('utf-8')+c)
    dlg.set_label(cn('请等待\n正在登录空间…'))
    d=get_sid(c,cq,cm)
    set_body('提取sid为:'.decode('utf-8')+d)
    #手机美文链接
    gl='\xe6\x89\x8b\xe6\x9c\xba\xe7\xbe\x8e\xe6\x96\x87'
    libao='\xe6\x81\xad\xe5\x96\x9c\xe6\x82\xa8\xe8\x8e\xb7\xe5\xbe\x97\xe5\xb9\xb8\xe8\xbf\x90\xe5\xa4\xa7\xe7\xa4\xbc\xe5\x8c\x85'
    dlg.set_label(cn('正在预读美文日志链接…'))
    set_body(cn('正在预读美文链接…'))
    m=lookurl(a,gl)
    dlg.close()
    url=m[:m.find('&sid=')+5]+d
    for i in range(500):
        readnext(url)#读日志    
        set_body(cn('正在预读美文链接…'))
        url=lookurl(url,'\xe4\xb8\x8b\xe9\xa1\xb5')
        set_body(cn('正在检测进度…'))
        libaourl=lookurl(myzone_url,libao)
        if libaourl!=None:
            set_body(cn('恭喜你，刷到了\n快点击<我的空间>看看吧…'))
            break
        if url==None:break
    if libaourl==None:
        set_body(cn('呜呜呜，还没刷到喔…\n继续…加油…'))
    point.stop()
def exit():
    app_lock.signal()
    os.abort() 
        
menu=[(cn('开始刷包'),shua),('参数设置'.decode('utf-8'),set_s),('我的空间'.decode('utf-8'),open_browser),('更新软件'.decode('utf-8'),update_browser),(cn('关闭应用'),exit)]
appuifw.app.screen="normal"
appuifw.app.title='情侣空间助手'.decode('utf-8')
appuifw.app.body=body=appuifw.Text()
body.bind(63557,shua)
set_body(cn('\n按<ok键>开始吧\n最后更新日期2009-07-04'))
appuifw.app.menu = menu
appuifw.app.exit_key_handler = exit
app_lock = e32.Ao_lock()
app_lock.wait()