# -*- conding:utf-8 -*-
_name='乐讯编帖工具'#不知道叫啥好，名字都给人用了
_ver='3.1'
_author='张小烦'
_website='py.t.lexun.com'
_remarks='乐讯PyS60技术专版欢迎您'
_date='2010.2.23'
_tested=['n73']
'''版权所有 xwmqm@qq.com'''
'''简化了，取消了文件上传的部分，针对乐讯网站的升级变化，从新调整发帖的部分'''
#
import appuifw as ui,e32
ao=e32.Ao_lock()
run_start_page=1
def cn(x):return x.decode('utf8')
def en(x):return x.encode('utf8')
class edit:
    
    def __init__(self):
        try:
            from envy import set_app_system
            set_app_system(1)
        except:
            ui.note(cn('  注意：由于缺少envy模块，不能直接挂到后台，注意保存！'),'info')
        #    
        from socket import access_points,access_point,select_access_point,set_default_access_point       
        self.aps=access_points()#接入点列表        
        self.apid={} 
        self.ap=None
           
        self.txt_size=0
        ui.app.title=cn(_name)
        ui.app.body=self.t=ui.Text()
        ui.app.exit_key_handler=self.exit_edit
        self.t.bind(63557,self.addn)
        self.t.bind(63586,self.pop_menu)
        self.menu_list=[(cn('文件'),
                         ((cn('新建'),self.new),
                          (cn('打开'),self.read),
                          (cn('保存'),self.save))),
                        (cn('表情'),self.face),
                        (cn('转换'),self.rep),
                        (cn('还原'),self.rerep),
                        (cn('超链'),
                         ((cn('插入帖链'),self.bto_url),
                          (cn('直接输入URL'),self.url)),
                          ),
                        (cn('图链'),
                         ((cn('输入地址'),self.img),)
                          ),
                          (cn('社区专用UBB'),
                         ((cn('加粗'),lambda:self.add_ubb('b')),
                          (cn('下划线'),lambda:self.add_ubb('u')),
                          (cn('斜体'),lambda:self.add_ubb('i')),
                          (cn('电话'),lambda:self.add_ubb('tel')),
                          (cn('日期'),lambda:self.add_ubb('date')),
                          (cn('时间'),lambda:self.add_ubb('time')),
                          (cn('农历图片'),lambda:self.add_ubb('cct')),
                          ))
                        ]
        self.pop_menu_list=[cn('复制到UC'),cn('发表'),cn('上翻'),cn('下翻'),cn('设置'),cn('帮助')]
        ui.app.menu=self.menu_list
        self.setting=[u'14',#字体
            u'250,100,100',#颜色
            u'',#LXT
            u'5690:PyS\u7f16\u7a0b\u4e13\u533a,6019:\u7834\u89e3\u4e13\u533a',
            u'64:\u5973\u4eba\u5fc3\u4e8b,222:\u7537\u5b69\u522b\u54ed',
            u' ',#空格
            None,#接入点
            u'e:\\sys\\bin\\UcWeb60signed.exe']#UC路径
        self.sett('read')
        self.up_setting()
        self.face_list=[
      cn('胜利'),
      cn('摆酷'),
      cn('暴汗'),
      cn('晕了'),
      cn('大笑'),
      cn('脸红'),
      cn('偷笑'),
      cn('流泪'),
      cn('色色'),
      cn('惊讶'),
      cn('抽烟'),
      cn('疑问'),
      cn('调皮'),
      cn('飞吻'),
      cn('愤怒'),
      cn('害羞'),
      cn('别吵'),
      cn('欢迎'),
      cn('微笑'),
      cn('睡觉'),
      cn('送花'),
      cn('闭嘴'),
      cn('再见'),
      cn('擦汗'),
      cn('发呆'),
      cn('可怜'),
      cn('捉狂'),
      cn('亲亲'),
      cn('鄙视'),
      cn('咒骂'),
      cn('好困')
            ]
            
    #
    #对接入点的设置
    def set_ap(self):
        from socket import access_points,access_point,select_access_point,set_default_access_point
        apid=[k for k in self.aps if k['name']==u'WAP over GPRS']
        if apid:#找的默认的接入点
            self.apid=apid[0]
            self.ap=access_point(self.apid['iapid'])
            self.setting[6]=unicode(self.aps.index(self.apid))
            set_default_access_point(self.ap)
        else:#没找到就选一个
            self.apid_i=select_access_point()
            self.apid=[k for k in self.aps if k['iapid']==self.apid_i][0]
            self.ap=access_point(self.apid['iapid'])            
            self.setting[6]=unicode(self.aps.index(self.apid))
            set_default_access_point(self.ap)




    def sett(self,tpye='read'):#处理设置读取和保存
        import os,sys
        path=os.path.split(sys.argv[0])[0]+'\\set.ini'
        if tpye=='read':
            try:
                f=open(path)
                s=f.read()
                l=s.split(';')
                f.close()
                for i in range(len(self.setting)):
                    self.setting[i]=cn(l[i])

            except:#如果读取配置出错，将删除配置。恢复默认配置
                if os.path.exists(path):
                    os.remove(path)
                self.set_ap()

                #ui.note(cn('未设置！或读取设置出错！'),'info')
        elif tpye=='set':
            form_list=[(cn('字体大小:'),'number',eval(self.setting[0])),
                       (cn('文字颜色(RGB值):'),'text',self.setting[1]),
                       (cn('网站LXT:'),'text',self.setting[2]),
                       (cn('高手论坛ID设置:'),'text',self.setting[3]),
                       (cn('社区论坛ID设置:'),'text',self.setting[4]),
                       (cn('空格替换符:'),'text',self.setting[5]),
                       (cn('接入点:'),'combo',([k['name'] for k in self.aps],eval(self.setting[6]))),
                       (cn('自定义UC路径:'),'text',self.setting[7])]
            F=ui.Form(form_list,ui.FFormDoubleSpaced)
            F.execute()
            for i in range(F.__len__()):
                if i==6:
                    self.setting[i]=unicode(F[i][2][1])
                else:
                    self.setting[i]=unicode(F[i][2])
            try:
                f=open(path,'w')
                l=';'.join(self.setting)
                f.write(en(l))
                f.close()
                self.up_setting()
            except:
                ui.note(cn('保存设置出错！'),'info')
        elif tpye=='save':
            try:
                f=open(path,'w')
                l=u';'.join(self.setting)
                f.write(en(l))
                f.close()
                self.up_setting()
            except:
                ui.note(cn('保存设置出错！'),'info')
                
    def up_setting(self):#刷新设置
        self.t.font=('normal',eval(self.setting[0]))
        self.t.color=eval('('+self.setting[1]+')')
        s=self.t.get()
        self.t.set(s)
    def send(self,data='',url=''):#发送网络数据公用函数
        import httplib
        from socket import access_points,access_point,select_access_point,set_default_access_point
        self.apid=self.aps[eval(self.setting[6])]
        self.ap=access_point(self.apid['iapid'])
        set_default_access_point(self.ap)
        
        heads={"Accept":"text/plain","Content-Type":"application/x-www-form-urlencoded","User-Agent":"LeXun-PY_G-XWM-ZXF"}
        try:
            conn=httplib.HTTPConnection('10.0.0.172:80')
            conn.request('POST',url,data,heads)
            res=conn.getresponse()
        except:
            pass
        return res.status, res.reason, res.read()
    def post_txt(self,tpye='sj'):#发送文章
        if self.setting[2]:#检测SID是否有
            if tpye=='sj':#检测发帖区域为手机高手
                if self.setting[3]:#检测高手区论坛ID是否设置好
                    p_=self.setting[3].split(',')#从配置中获取论坛ID设置
                    p_id=[i.split(':')[0] for i in p_]#获取论坛ID列表
                    p_tx=[i.split(':')[1] for i in p_]#获取论坛名称列表
                    x=ui.popup_menu(p_tx,cn('选择目的论坛'))
                    if x!=None:
                        if self.t.len()>9:
                            t=ui.query(cn('定个题目哦(^m^)'),'text')
                            if t and len(t)>3:
                                cid=ui.popup_menu([cn('默认'),cn('综合'),cn('提问'),cn('原创')],cn('选择帖子类型'))
                                if cid==1:cid='5'                                    
                                elif cid==2:cid='1'                                    
                                elif cid==3:cid='11'                                   
                                else:cid='0'
                                score=ui.query(cn('要设悬赏分吗？'),'text',u'10')
                                if score==None:score="0"
                                
                                note=ui.InfoPopup()
                                note.show(cn('正在发送文章...\n请稍后'),(10,100),100000,0,ui.EHCenterVCenter)
                                pid=p_id[x]
                                url='http://sjgs3.lexun.com/writetextapp.aspx?write_Type=1&topic_page=1&lxt=%s&ForumId=%s' % (self.setting[2],pid)
                                from urllib import urlencode
                                self.rep()
                                s=self.t.get()
                                self.rerep()
                                data=urlencode({'Content':en(s),'Title':en(t),'cid':en(cid),'score':en(score)})
                                res=self.send(data,url)
                                if res[0]==200:
                                    if res[2].find('成功')!=-1:
                                        note.hide()
                                        ui.note(cn('文章成功发布！'))
                                    else:
                                        note.hide()
                                        ui.note(cn('文章发布失败！原因可能是权限和屏蔽问题！'))
                                else:
                                    note.hide()
                                    ui.note(cn('文章发布失败！原因可能是网络中断！'))
                            else:
                                ui.note(cn('标题太短'))
                        else:
                            ui.note(cn('正文字数不够9个'),'info')
                    else:
                        ui.note(cn('操作已取消'),'info')
                else:
                    ui.note(cn('你没有设置论坛ID'),'info')
            elif tpye=='bbs':#检测发帖区域为社区论坛
                if self.setting[4]:#检测高手区论坛ID是否设置好
                    p_=self.setting[4].split(',')#从配置中获取论坛ID设置
                    p_id=[i.split(':')[0] for i in p_]#获取论坛ID列表
                    p_tx=[i.split(':')[1] for i in p_]#获取论坛名称列表
                    x=ui.popup_menu(p_tx,cn('选择目的论坛'))
                    if x!=None:
                        if self.t.len()>9:
                            t=ui.query(cn('必须定个题目哦(^m^)'),'text')
                            if t and len(t)>3:
                                note=ui.InfoPopup()
                                note.show(cn('正在发送文章...\n请稍后'),(10,100),100000,0,ui.EHCenterVCenter)
                                pid=p_id[x]
                                url='http://f3.lexun.com/writeapp.aspx?lxt=%s&bid=%s&wtype=1' % (self.setting[2],pid)
                                from urllib import urlencode
                                self.rep()
                                s=self.t.get()
                                self.rerep()
                                data=urlencode({'Content':en(s),'Title':en(t)})
                                res=self.send(data,url)
                                if res[0]==200:
                                    if res[2].find('成功')!=-1:
                                        note.hide()
                                        ui.note(cn('文章成功发布！'))
                                    else:
                                        note.hide()
                                        ui.note(cn('文章发布失败！原因可能是权限和屏蔽问题！'))
                                else:
                                    note.hide()
                                    ui.note(cn('文章发布失败！原因可能是网络中断！'))
                            else:
                                ui.note(cn('标题太短'))
                        else:
                            ui.note(cn('正文字数不够9个'),'info')
                    else:
                        ui.note(cn('操作已取消'),'info')
                else:
                    ui.note(cn('你没有设置论坛ID'),'info')
            else:
                pass
        else:#没有SID的时候提示设置SID
            ui.note(cn('请先设置帐号LXT值和论坛ID值'),'info')
            if ui.query(cn('需要联网获取LXT值吗？'),'query'):
                self.get_sid()
    def new(self):#新建一篇内容前，要检查是否已经有内容了，是否保存了
        if self.t.len() !=0 and self.txt_size != self.t.len():
            if ui.query(cn('是否需要保存现在的文档？'),'query'):
                self.save()                       
        self.t.set('')
        self.txt_size=0
        self.path=''
    def read(self):#打开一篇内容前，一样要检查是否已经有内容了，是否保存
        if self.t.len() !=0 and self.txt_size != self.t.len():
            if ui.query(cn('是否需要保存现在的文档？'),'query'):
                self.save()
        import powlite_fm as fm
        t=fm.manager()
        self.path=t.AskUser(find='file',ext=['.txt'])
        try:
            if self.path:
                f=open(en(self.path))
                s=f.read()
                self.t.set(cn(s))
                f.close()
                self.txt_size=self.t.len()
        except:
                ui.note(cn('异常错误！'),'info')
                self.new()
    def save(self):#保存文件
        if self.path:
            f=open(en(self.path),'w')
            f.write(en(self.t.get()))
            f.close()
            self.txt_size=self.t.len()
            ui.note(cn('已保存！'),'info')
        else:
            import powlite_fm as fm
            t=fm.manager()
            self.path=t.AskUser(find='dir')
            if self.path:
                fn=ui.query(cn('保存为：'),'text')
                if fn:
                    self.path=self.path+fn+'.txt'
                    f=open(en(self.path),'w')
                    f.write(en(self.t.get()))
                    f.close()
                    self.txt_size=self.t.len()
                    ui.note(cn('已保存！'),'info')
    def get_sid(self):#获取SID函数
        x,y=ui.multi_query(cn('乐讯帐号：'),cn('密码：'))
        if x and y:
            from urllib import urlencode
            data=urlencode({"Num":en(x),"PWD":en(y)})
            url='http://117.135.136.38/login/login.aspx'
            res=self.send(data,url)
            if res[0]==200 and res[2]:
                import re
                re_get_sid=re.compile('\w{25}')
                sid=re_get_sid.findall(res[2])
                if sid:
                    self.setting[2]=cn(sid[0])
                    ui.note(cn('成功获取LXT并以设置成功！'))
                else:
                    ui.note(cn('获取LXT失败，请重试或手动设置！'))
            else:
                ui.note(cn('网络连接出错！请重试！'))
    def rep(self):#替换特符
        s=self.t.get()
        t=self.setting[5]
        s=s.replace(' ',t)
        l=s.split(u'\u2029')
        s='///'.join(l)
        self.t.set(s)
    def rerep(self):#还原
        s=self.t.get()
        t=self.setting[5]
        s=s.replace(t,' ')
        l=s.split('///')
        s=u'\u2029'.join(l)
        self.t.set(s)
    def addn(self):#添加换行符
        self.t.add(u'\n')
    def add_ubb(self,t):
        if t=='date' or t=='time' or t=='cct':
            self.t.add(u'(%s)'%t)
        elif t=='tel':
            x=ui.query(cn('输入电话号码'),'text')
            if x:
                self.t.add(u'(url=wtai://wp/mc;%s)%s(/url)'%(x,x))
        else:
            x=ui.query(cn('输入文字'),'text')
            self.t.add(u'(%s)%s(/%s)'%(t,x,t))
    def url(self):#添加url
        try:
            x,y=ui.multi_query(cn('链接名称'),cn('链接地址'))
            if x and y:
                self.t.add('(url=%s)%s(/url)'%(y,x))
        except: 
            pass
    def bto_url(self):#添加文章链接
        try:
            x,y=ui.multi_query(cn('链接名称'),cn('帖子ID:'))
            if x and y:
                self.t.add('(url=bto:%s)%s(/url)'%(y,x))
        except:
            pass
    def img(self):#添加img
        try:
            x=ui.query(cn('链接地址'),'text')
            if x:self.t.add(u'(img/)%s(/img)'%x)
        except:
            pass
    def face(self):#添加表情
        try:
            i=ui.popup_menu(self.face_list,cn('表情'))
            i+=1001
            self.t.add(u'BQ%s'% i)
        except:
            pass
    def pop_menu(self):#快捷菜单
        x=ui.popup_menu(self.pop_menu_list)
        if x==0:#切换到UC
            self.rep()
            try:
                import clipboard_CHN
                if clipboard_CHN.Set(self.t.get()):
                    ui.note(cn('已复制文本\n正切换到浏览器..'))
                else:
                    ui.note(cn('复制失败，请手动复制！\n准备切换到浏览器..'))
            except:
                ui.note(cn('无法正常使用复制功能'))
            self.rerep()
            import os
            try:
                if self.setting[6]:
                    e32.start_exe(self.setting[7],self.setting[7])
                else:
                    path=['E:\\sys\\bin\\UcWeb60signed.exe','C:\\sys\\bin\\UcWeb60signed.exe']
                    if os.path.exists(path[0]):
                        e32.start_exe(path[0],path[0])
                    elif os.path.exists(path[1]):
                        e32.start_exe(path[1],path[1])
                    else:
                        ui.note(cn('找不到UC7.0路径'))
            except:
                ui.note(cn('指定的路径无法运行UC！'))
        elif x==1:#发布文章
            n=ui.popup_menu([cn('发送到高手'),cn('发送到社区')],cn('选择类别'))
            if n==0:
                self.post_txt('sj')
            elif n==1:
                self.post_txt('bbs')
        elif x==2:#上翻
            try:
                self.t.set_pos(self.t.get_pos()-100)
            except:
                pass
        elif x==3:#下翻
            try:
                self.t.set_pos(self.t.get_pos()+100)
            except:
                pass
        elif x==4:#设置
            self.sett('set')
        elif x==5:#帮助
            y=ui.popup_menu([cn('帮助'),cn('留言')])
            if y==0:#关于   
                ui.note(cn('作者昵称：\n张小烦\n乐讯PyS60专区欢迎您\n网py.t.lexun.com'),'info')
            elif y==1:#留言(软件直发)
                if self.setting[2]:
                    z=ui.query(cn('给我留言：'),'text')
                    if z:
                        url='http://sjgs3.lexun.com/writerlyapp.aspx?topicid=23076710&rlypageType=1&cd=988&lxt=%s&ForumId=5690&topic_page=1&topic_cid=0'%self.setting[2]
                        from urllib import urlencode
                        data=urlencode({'content':'[编帖工具反馈]'+en(z)})
                        res=self.send(data,url)
                        if res[0]==200:
                            ui.note(cn('留言已送达！谢谢使用！'))
                else:
                    ui.note(cn('请先设置帐号LXT和论坛ID'),'info')
                    if ui.query(cn('需要联网获取LXT吗？'),'query'):
                        self.get_sid()
        else:
            pass
    def exit_edit(self):#退出处理
        if ui.query(cn('确定退出吗？'),'query'):
            if self.txt_size!=self.t.len():
                if ui.query(cn('是否保存？'),'query'):
                    self.save()
            self.sett('save')
            ao.signal()
            ui.app.set_exit()            
                
def start_menu_new():
    global run_start_page    
    run_start_page=0
    m=edit()
    m.new()
def start_menu_open():
    global run_start_page
    run_start_page=0
    m=edit()
    m.read()
def exit():
    global run_start_page
    run_start_page=0
    ao.signal()
    ui.app.set_exit()
def start_page():
    ui.app.title=cn('欢迎使用')
    ui.app.exit_key_handler=exit
    x,y=ui.app.layout(ui.EMainPane)[0]
    from graphics import Image
    im=Image.new((x,y))  
    im.clear(0xaaaaaa)
    im.text((25,63),cn(_name),0xff0000,('normal',30))
    im.text((25,90),cn('版本:'+_ver),0xffffff,('normal',15))
    im.text((25,115),cn('作者:'+_author),0xffffff,('normal',15))
    im.text((25,140),cn('日期:'+_date),0xffffff,('normal',15))
    im.text((100,200),cn(_remarks),0xffffff,('normal',12))
    im.text((100,220),cn(_website),0xffffff,('normal',11))
    im.line((20,65,220,65),0xff0000)
    ui.app.body=c=ui.Canvas()
    ui.app.menu=[(cn('新建'),start_menu_new),(cn('打开'),start_menu_open)]
    while run_start_page:
        c.blit(im)
        e32.ao_yield()
start_page()           
ao.wait()
