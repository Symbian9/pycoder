import appuifw as A
import os,e32
import uitricks
def cn(x):return x.decode('utf8')
def en(x):return x.encode('utf8')
def iii(i):A.note(cn(i),'error')
def ri(i):
  A.app.exit_key_handler=i
old = A.app.title
def pt(i,ii=True):
  A.app.title=i
  if ii:A.app.title=i
  try:A.app.body.focus = True
  except:pass
  e32.ao_yield()

try:import applist,appswitch
except:iii('模块缺失')
apps_ph=en(os.path.split(A.app.full_name())[0]+'\\my_apps\\')
if not os.path.exists(apps_ph): os.makedirs(apps_ph)


def page1():
  global list_1
  file=os.listdir(apps_ph)
  list_1=[]
  for i in range(0, len(file)):
    if os.path.isdir((apps_ph+'\\'+file[i])) == 1:
      list_1.append(cn(file[i]))

  def cli(cz=None):
    li=m_1.current()
    for x in range(0,len(list_1)):
      if li==x:
        if cz==0:
          n=A.query(cn('输入新目录名称?'), 'text', u'none')
          if n:pass
          else:return
          os.makedirs(apps_ph+en(n))
          page1()
        elif cz==1:
          n=en(A.query(cn('目录重命名为？'), 'text', list_1[x]))
          try:
            os.rename((apps_ph+en(list_1[x])+'\\'),(apps_ph+n+'\\'))
            page1()
          except:
            iii('目录有重名！')
        elif cz==2:
          if A.query(cn('确认删除吗？\n目录：')+list_1[x],'query'):
            try:
              decl(cn(apps_ph)+list_1[x])
              page1()
            except:
              iii('错误')

        elif cz==3:
          try:lilirun(apps_ph+list_1[x]+'\\')
          except:iii('未知错误！')

  if len(list_1)!=0:
    A.app.title=old
    A.app.body =m_1 = A.Listbox(list_1, lambda:cli(3))
    A.app.menu = [(cn('进入(4键)'),lambda:cli(3)),(cn('删除(c键)'),lambda:cli(2)),(cn('改名(0键)'),lambda:cli(1)),(cn('创建目录'),lambda:cli(0)),(cn('退出软件'),lambda:quit(1))]
    ri(lambda:quit(0))
  else:
    list_1 = [cn('-无目录-')]
    A.app.menu = [(cn('创建目录'),lambda: cnew(0))]
    A.app.body =m_1 = A.Listbox(list_1,lambda: cnew(0))
  m_1.bind(8,lambda:cli(2))
  m_1.bind(48,lambda:cli(1))
  m_1.bind(52,lambda:cli(3))
  m_1.bind(42,lambda:liup(list_1))
  m_1.bind(35,lambda:lidn(list_1))
  uitricks.set_text(cn("操作"),3000)
  uitricks.set_text(cn("隐藏"),3009)



def cnew(x):
  if x==0:
    n=A.query(cn('输入新目录名称?'), 'text', u'none')
    if n:pass
    else:return
    os.makedirs(apps_ph+en(n))
    page1()
  if x==1:
    pass

#
def lilirun(path):
  path=en(path)
  file=os.listdir(path)
  flist=[]
  for i in range(0, len(file)):
    if os.path.isfile((path+'\\'+file[i])) == 1:
      flist.append(cn(file[i]))

  def saps():
    list_4=[]
    li=applist.applist()
    for ii in li:
      if len(ii[1])!=0:
        list_4.append(ii[1])
    cz=A.selection_list(list_4,1)
    if cz:pass
    else:return 
    mc=li[cz][1]
    lj=li[cz][-1]
    f = open(path+en(mc), 'a')
    try:f.write(lj)
    except:f.write(en(lj))
    A.note(cn('添加成功！'),'conf')
    f.close()
    lilirun(cn(path))



  def hs():
    li=m.current()   
    run_to(li)

  def run_to(cz=None):
    li=m.current()
    for ii in range(0,len(flist)):
      if li==ii:
        if cz==0:
          try:file=cn(path)+flist[ii];f=open(en(file),"r");appslj=f.read();runapps(appslj);f.close()
          except:return
        if cz==1:
          n=en(A.query(cn('重命名为？'), 'text', flist[ii]))
          try:
            os.rename((path+en(flist[ii])),(path+n))
            lilirun(cn(path))
          except:
            iii('文件夹有重名！')
        if cz==2:
          if A.query(cn('确认要删除吗？\n菜单：')+flist[ii],'query'):
            os.remove((path+en(flist[ii])))
            lilirun(cn(path))
        elif cz==3:
          gl=A.popup_menu(list_1, flist[ii]+cn('归类到？'))
          if gl!=None:
            try:
              os.rename((path+en(flist[ii])),(en(apps_ph+list_1[gl]+'\\'+flist[ii])))
              lilirun(cn(path))
            except:
              iii('已存在同名文件')
      else:pass
  def lilt():
    ipy=path.split('\\')[-2]
    page1();A.app.body.set_list(list_1,list_1.index(cn(ipy)))

  ri(lilt)
  if len(flist) != 0:
    A.app.body=m=A.Listbox(flist,lambda:run_to(0))
    A.app.menu=[(cn('返回(4键)'),lilt),(cn('改名(0键)'),lambda: run_to(1)),(cn('删除(c键)'),lambda: run_to(2)),(cn('移动归类'),lambda: run_to(3)),(cn('新增菜单'),saps),(cn('退出软件'),lambda:quit(1))]
  else:
    A.app.body=m=A.Listbox([cn('-无文件-')],saps)
    A.app.menu=[(cn('新增菜单'),saps)]
  m.bind(52,lilt)
  m.bind(8,lambda: run_to(2))
  m.bind(48,lambda: run_to(1))
  m.bind(42,lambda:liup(flist))
  m.bind(35,lambda:lidn(flist))
  uitricks.set_text(cn("返回"),3009)


def lidn(i=[]):
  lh=len(i)
  dn=A.app.body.current()
  if dn+6<lh:
    dn+=6
    A.app.body.set_list(i,dn)
  elif dn+6>=lh:
    A.app.body.set_list(i,lh)
def liup(i=[]):
  dn=A.app.body.current()
  if dn-6>0:
    dn-=6
    A.app.body.set_list(i,dn)
  elif dn-6<=0:
    A.app.body.set_list(i,0)
#
def decl(path):
  try:
    try:
      os.rmdir(en(path))
      pt(cn('删除') + path)
    except:
      sa = os.listdir(en(path))
      for i in sa:
        pt(cn(('删除%s%s' % (en(path),i))))
        try:
          os.remove((en(path) +'\\'+ i))
        except:
          try:
            os.rmdir((en(path) +'\\'+ i))
          except:
            decl(((path + cn(i)) + '\\'))
      decl(path)

  except:
    pt(path+cn("不存在<或只读文件>"))
    app_lock = e32.Ao_lock()
    if A.query(path+cn("无法删除，跳过删除其它文件？"),"query"):
      app_lock.signal()
    else:
      pt(cn("\n删完完毕，剩下只读文件！"))
      app_lock.wait()
      e32.ao_yield()
  A.app.title=old

#
def page2():
  a=appswitch.application_list(0)
  list_2=[]
  for c in a:
    list_2.append(c)
  def sx():page2()
  def zj(cz):
    li=m.current()
    for ii in range(0,len(list_2)):
      if li==ii:
        if cz==0:appswitch.switch_to_fg(list_2[ii])
        if cz==1:
          if A.query(cn("确认关闭吗？\n线程：")+list_2[ii],"query"):
            try:appswitch.end_app(list_2[ii])
            except:appswitch.kill_app(list_2[ii])
        page2()

  A.app.title=old
  if len(list_2) != 0:A.app.body=m=A.Listbox(list_2,lambda:zj(0));m.bind(48,sx);m.bind(8,lambda:zj(1));m.bind(42,lambda:liup(list_2));m.bind(35,lambda:lidn(list_2));A.app.menu=[(cn("前台(ok键)"),lambda:zj(0)),(cn("结束(C键)"),lambda:zj(1)),(cn("刷新(0键)"),sx),(cn('退出软件'),lambda:quit(1))]



#
def page3():
  global list_3
  list_3,li=[],[]
  l=applist.applist()
  for i in range(0,len(l)):
    if l[i][-1][0]==u"C":li.append(l[i])
    if l[i][-1][0]==u"E":li.append(l[i])
  for ii in li:
    if len(ii[1])!=0:
      list_3.append(ii[1])
  def czapps(cz):
    gb=m_2.current()
    mc=li[gb][1]
    lj=li[gb][-1]
    dir2=(os.path.split(lj)[0])
    if cz==0:runapps(en(lj))
    if cz==1:
      bc=A.popup_menu(list_1, cn('菜单添加到？'))
      f = open(apps_ph+en(list_1[bc]+'\\'+mc), 'a')
      try:f.write(lj)
      except:f.write(en(lj))
      A.note(cn('添加成功！'),'conf')
      f.close()
    if cz==2:
      dir2=dir2+'\\'
      if A.query(cn("确认删除吗？\n程序：")+mc,"query"):
        import time
        start=time.clock()
        try:decl(en(dir2))
        except:decl(dir2)
        end=time.clock()
        A.note((cn('删除完毕！\n用时：%.2f 秒' %(end-start))),'conf')
        page1()
    if cz==3:
      app = dir2.split('\\')[-1]
      if ((app[0]==u'[') and (app[-1]==u']')):
        if len(app)==10:
          iii('Jar不支持共存')
          return
        else:pass
      app1=app+unicode(1)
      if A.query(cn("确认共存吗？\n软件：")+mc,"query"):
        try:gcgo(en(dir2),app1)
        except:iii('共存失败')
    if cz==4:
      uid = open(en(lj)).read(12)[-4:]
      A.query(mc+cn('软件的 UID：'), 'text', (u'0x' + unicode((((hex(ord(uid[3]))[2:] + hex(ord(uid[2]))[2:]) + hex(ord(uid[1]))[2:]) + hex(ord(uid[0]))[2:]))))

  def nameapps():
    global name1,name2
    gb=m_2.current()
    lj=li[gb][-1]
    dir1=lj.split('.')[0]
    dir2=(os.path.split(lj)[0]+'\\')
    app = dir2.split('\\')[-2]
    rsc = (dir1 + '_caption.rsc')
    name2 = A.query(cn('显示在功能表的名称：(自定义)'), 'text',cn('不知道…'))
    if (not name2):return 
    name1 = A.query(cn('显示程序标题的名称：(自定义)'), 'text',name2)
    if (not name1):return 
    A.note(cn('请耐心等候5步'))
    try:os.rename((dir1+'.aif'),(dir1+ '.aif_temp'))
    except:pass
    for file in os.listdir(dir2.encode('utf-8')):
        if ((file.lower().find('caption.r') >= 0) and (file[-4:] != '_old')):
            try:os.rename((dir2 + file), ((dir2 + file) + '_old'))
            except:pass
    name1 = name1.ljust(3).encode('utf-16')[2:]
    name2 = name2.ljust(3).encode('utf-16')[2:]
    seek = str(hex(((8 + len(name1)) + len(name2))))[2:]
    open(rsc.encode('utf-8'), 'w').write(((((((((((seek + '000500') + hex((len(name1) / 2))[2:].zfill(2)) + 'ab') + name1.encode('hex')) + hex((len(name2) / 2))[2:].zfill(2)) + 'ab') + name2.encode('hex')) + '0400') + seek) + '00').decode('hex').replace('01f2'.decode('hex'), '0a00'.decode('hex')))
    for p in range(5, 0, -1):
      pt(cn('还剩 %d 步…\n') % p)
      e32.ao_sleep(2.6)
    try:os.rename((dir1 + '.aif_temp'), (dir1 + '.aif'))
    except:pass
    A.note(cn('重命名完成！'),'conf')
    del name1,name2
    page3()

  A.app.title=old
  A.app.body=m_2 = A.Listbox(list_3, lambda:czapps(0))
  A.app.menu = [(cn('快捷方式'),lambda:czapps(1)),(cn('软件改名'),nameapps),(cn('删除软件'),lambda:czapps(2)),(cn('共存软件'),lambda:czapps(3)),(cn('软件u i d'),lambda:czapps(4)),(cn('退出软件'),lambda:quit(1))]
  m_2.bind(42,lambda:liup(list_3))
  m_2.bind(35,lambda:lidn(list_3))
##
running=True
def gcgo(gcdir,dirmc):
    import struct,random,lite_fm,uidcrc
    def copy_file(from_dir, to_dir):
        global running
        try:
            f = open(INIpath, 'r')
            Content = f.read()
            f.close()
            R = re.compile('\\[(.*?)->(.*?)\\]')
            ToBeRenamed = R.findall(Content)
            try:
                FN = re.compile('#\\[FileName:(.*?)]')
                Filename = FN.findall(Content)[0]
                MB = re.compile('#\\[MadeBy:(.*?)]')
                Madeby = MB.findall(Content)[0]
                CT = re.compile('#\\[Contact:(.*?)]')
                Contact = CT.findall(Content)[0]
                Filename = cn(Filename)
                Madeby = cn(Madeby)
                Contact = cn(Contact)
                if (running == 0):
                    pt((u'%s\n' % Filename))
                    e32.ao_sleep(1)
                    pt((cn('制作：') + (u'%s\n' % Madeby)))
                    e32.ao_sleep(2)
                    pt((cn('联系方式') + (u'%s' % Contact)))
                    pt(cn('正在读取...'))
                    running = 1
                    e32.ao_sleep(2)
            except:
                pt(cn('未发现作者相关信息'))
        except:
            ToBeRenamed = None
        All_files = os.listdir(en(from_dir))
        pt((cn('创建文件夹:%s') % to_dir))
        os.mkdir(en(to_dir))
        for i in range(0, len(All_files)):
            if (ToBeRenamed != None):
                for ti in ToBeRenamed:
                    if (ti[0].lower() == All_files[i].lower()):
                        try:
                            RenameTo = (ti[1] % ASK_path)
                        except:
                            RenameTo = ti[1]
                        break
                    else:
                        RenameTo = All_files[i]

            else:
                RenameTo = All_files[i]
            if (os.path.isfile(((en(from_dir) + '\\') + All_files[i])) == 1):
                try:
                    pt((cn('复制%s到%s') % (cn(All_files[i]),cn(RenameTo))))
                except:
                    pt((cn('复制%s到%s') % (cn(All_files[i]),RenameTo)))
                try:
                    e32.file_copy(((to_dir + '\\') + cn(RenameTo)), ((from_dir + '\\') + cn(All_files[i])))
                except:
                    e32.file_copy(((to_dir + '\\') + RenameTo), ((from_dir + '\\') + cn(All_files[i])))
            else:
                try:
                    RenameTo1 = cn(RenameTo)
                except:
                    RenameTo1 = RenameTo
                copy_file(((from_dir + '\\') + cn(All_files[i])), ((to_dir + '\\') + RenameTo1))


#
    try:
        Capps_path = 'c:\\system\\apps\\'
        Eapps_path = 'e:\\system\\apps\\'

        Source_path = gcdir
        pt((cn('源程序：%s') % cn(Source_path)))
        ASK_path = A.query(cn('请输入共存的程序路径名称(支持中文，但尽量不要中文…)'), 'text',dirmc)
        Source_path = cn(Source_path)
        To_path = (Eapps_path + ASK_path)
        if A.query(cn('使用共存配置文件？(百阅，掌迅通等确认，其它取消！)'), 'query'):
            INIpath = lite_fm.manager(u'e:\\system\\apps\\lbcl\\data\\Additionals\\', 'file')
        pt((cn('正在复制%s内所有文件到%s') % (Source_path,
         To_path)))
        if (os.path.exists(en((Capps_path + ASK_path))) or os.path.exists(en((Eapps_path + ASK_path)))):
            A.note((cn('已存在 %s 文件夹,创建取消!') % To_path),'error')
            return False
        copy_file(Source_path, To_path)
        pt(cn('文件夹内所有文件复制完成!'))
        pt(cn('正在改名...'))
        AppName = Source_path.split(u'\\')[-1]
        NewName = To_path.split(u'\\')[-1]
        pt((cn('源程序名:%s') % AppName))
        try:
            os.rename(en((((To_path + u'\\') + AppName) + u'.app')), en((((To_path + u'\\') + NewName) + u'.app')))
            pt(cn('app文件已经改名完成:)'))
        except:
            pt(cn('app文件改名失败:('))
        try:
            os.rename(en((((To_path + u'\\') + AppName) + u'.aif')), en((((To_path + u'\\') + NewName) + u'.aif')))
            pt(cn('aif文件已经改名完成:)'))
        except:
            pt(cn('aif文件改名失败:('))
        try:
            os.rename(en((((To_path + u'\\') + AppName) + u'.rsc')), en((((To_path + u'\\') + NewName) + u'.rsc')))
            pt(cn('rsc文件已经改名完成:)'))
        except:
            pt(cn('rsc文件改名失败:('))
        try:
            name = A.query(cn('输入显示在功能表里的软件名称'), 'text',cn('不知道…'))
            name1 =(name.encode('utf-16'))[2:]
            len4 = str(hex(((8 + len(name1)) + len(name1))))[2:]
            crsc = open(en((((To_path + u'\\') + NewName) + '_caption.rsc')), 'w+')
            crsc.write(((((((((((((len4 + '000500') + '0') + str((len(name1) / 2))) + 'ab') + name1.encode('hex')) + '0') + str((len(name1) / 2))) + 'ab') + name1.encode('hex')) + '0400') + len4) + '00').decode('hex'))
            crsc.close()
            pt(cn('_caption.rsc文件已经改名完成:)'))
        except:
            pt(cn('_caption.rsc文件改名失败:('))
        pt(cn('\napp,aif,rsc,_caption文件已经改名完成,如果其他文件需要修改,请手动修改.'))
        pt(cn('读取程序数据...'))
        Fan = file(en((((To_path + u'\\') + NewName) + u'.app')))
        app_content = Fan.read()
        Fan.close()
        Fuid = app_content[8:12]
        Ruid = (((Fuid[3:4] + Fuid[2:3]) + Fuid[1:2]) + Fuid[0:1])
        pt((cn('获取到源程序uid:%s') % (Ruid.encode('hex'))))
        uid = hex(random.randrange(16777216, 33554431, 1))
        uid = A.query(cn('请输入8位不同源程序的UID码（建议使用这个）'), 'text', cn(uid[2:]))
        if (uid == None):
            iii('制作取消')
            return False
        uid_int = 0
        try:
            uid_int = int(uid, 16)
        except:
            iii('错误的UID,劝你还是用自动分配的吧')
            return False
        AifFile = [cn('默认图标文件')]
        if os.path.exists(en((os.path.split(A.app.full_name())[0] + u'\\data\\Aif\\'))):
            aif_list = os.listdir(en((os.path.split(A.app.full_name())[0] + u'\\data\\Aif\\')))
            for i in range(0, len(aif_list)):
                if (cn(aif_list[i]).split('.')[-1] == 'aif'):
                    AifFile.append(cn(aif_list[i]))
                else:
                    continue

        slt = A.popup_menu(AifFile, cn('请选择aif图标文件--'))
        if (slt == 0):
            aif_path = ((os.path.split(A.app.full_name())[0] + u'\\') + u'lbcl.aif')
        else:
            aif_path = ((os.path.split(A.app.full_name())[0] + u'\\data\\Aif\\') + AifFile[slt])
        pt(cn('读取图标文件...'))
        aif_file = open(en(aif_path), 'r')
        aif_content = aif_file.read()
        aif_file.close()
        pt(cn('请稍候！正在写入图标文件...'))
        uid_1 = int(268435511)
        uid_2 = int(268450360)
        crc = uidcrc.sum(uid_1, uid_2, long(uid, 16))
        aif_file = open(en((((To_path + u'\\') + NewName) + '.aif')), 'w')
        aif_file.write(aif_content[0:8])
        aif_file.write(struct.pack('i', uid_int))
        aif_file.write(crc)
        aif_file.write(aif_content[16:])
        aif_file.close()
        pt(cn('写入图标完成，请稍候！'))
        uid_1 = int(268435577)
        uid_2 = int(268450254)
        crc = uidcrc.sum(uid_1, uid_2, long(uid, 16))
        crc2 = (uid_int + int(932))
        try:
            f = open(INIpath, 'r')
            Content = f.read()
            f.close()
            R = re.compile('ChangeAllUnicode\\[(.*?)->(.*?)\\]')
            RA = re.compile('ChangeAllAscii\\[(.*?)->(.*?)\\]')
            MD = re.compile('MkDir\\[(.*?)\\]')
            ToBeChangedUnicode = R.findall(Content)
            ToBeChangedAscii = RA.findall(Content)
            MakeDirPath = MD.findall(Content)
        except:
            ToBeChangedUnicode = None
            ToBeChangedAscii = None
            MakeDirPath = None
        if (MakeDirPath != None):
            for m in MakeDirPath:
                try:
                    os.mkdir(m)
                    pt((cn('创建文件夹:') + cn(m)))
                except:
                    pt(((cn('不能创建文件夹:') + cn(m)) + cn('\n请自行创建')))
                    e32.ao_sleep(2)

        app_content = (((((app_content[0:8] + struct.pack('i', uid_int)) + crc) + app_content[16:24]) + struct.pack('i', crc2)) + app_content[28:].replace(Fuid, struct.pack('i', uid_int)))
        app_content_hex = app_content.encode('hex')
        if (ToBeChangedUnicode != None):
            for i in ToBeChangedUnicode:
                try:
                    Ts = (i[1] % ASK_path)
                    try:
                        ASK_path.encode('ascii')
                        A_path = ASK_path
                        Ts = (i[1] % A_path)
                    except:
                        A_path = A.query(cn('您指定的软件名含有中文字符,请指定一个英文名称'), 'query')
                        Ts = (i[1] % A_path)
                except:
                    Ts = i[1]
                UnicodeString = i[0].encode('utf-16').encode('hex')[4:]
                ToUnicodeString = Ts.encode('utf-16').encode('hex')[4:]
                app_content_hex = app_content_hex.replace(UnicodeString, ToUnicodeString)
                pt((cn('已经替换') + (u'%s-->%s' % (UnicodeString,
                 ToUnicodeString))))

        if (ToBeChangedAscii != None):
            for i in ToBeChangedAscii:
                try:
                    Tsa = (i[1] % ASK_path)
                    try:
                        ASK_path.encode('ascii')
                        A_path = ASK_path
                        Tsa = (i[1] % A_path)
                    except:
                        A_path = A.query(cn('您指定的软件名含有中文字符,请指定一个英文名称'), 'query')
                        Tsa = (i[1] % A_path)
                except:
                    Tsa = i[1]
                AsciiString = i[0].encode('utf-8').encode('hex')
                ToAsciiString = Tsa.encode('utf-8').encode('hex')
                app_content_hex = app_content_hex.replace(AsciiString, ToAsciiString)
                pt((cn('已经替换') + (u'%s-->%s' % (AsciiString,
                 ToAsciiString))))

        app_content = app_content_hex.decode('hex')
        pt(cn('正在写入app程序...\n完成之前切勿进行*任何*其他操作!'))
        pt(cn('请勿切换到其他界面(关键时刻！)'))
        app_file = open(en((((To_path + u'\\') + NewName) + u'.app')), 'w')
        ActivateScreen = 0
        for i in range(0, ((len(app_content) / 10000) + 1)):
            ActivateScreen += 1
            if (ActivateScreen == 3):
                e32.reset_inactivity()
                ActivateScreen = 0
            nowSize = os.path.getsize(en((((To_path + u'\\') + NewName) + u'.app')))
            A.app.title = (cn('(操作中，勿动！)\n进度：%s/%s') % (nowSize,
             len(app_content)))
            if (app_content[(i * 10000):((i + 1) * 10000)] != ''):
                app_file.write(app_content[(i * 10000):((i + 1) * 10000)])

        app_file.close()
        pt(cn('写入app程序完成!'))
        A.app.title=old
        try:
            f = open(INIpath, 'r')
            Content = f.read()
            f.close()
            OT = re.compile('#\\[Others:(.*?)\\]')
            OtherInfo = OT.findall(Content)[0]
            pt((cn('其他信息:\n') + cn(OtherInfo)))
        except:
            A.note(cn("操作成功"),'conf')
            A.app.title=old
        return True
    except:
        iii("共存取消")
        A.app.title=old
    del struct,random,lite_fm,uidcrc


def runapps(apps):
  if (os.path.exists(apps)):
    try:e32.start_exe('z:\\system\\programs\\apprun.exe',apps)
    except:iii('软件出错！')
  else:iii('软件已不存在！\n切换等待刷新！')
##
ycxc=0
def quit(cz):
  global ycxc
#  cz=A.popup_menu([cn('线程隐藏'),cn('退出软件')])
  if cz==0:
    if ycxc==0:
      ycxc=1
      runapps(u"z:\\system\\apps\\phone\\phone.app")
      import pysys
      pysys.set_system(1)
      pysys.set_hidden(1)
    else:
      runapps(u"z:\\system\\apps\\phone\\phone.app")

  if cz==1:
    try:A.app.set_exit()
    except:os.abort()

def main(i):
    if (i == 0):page1()
    if (i == 1):page2()
    if (i == 2):page3()

A.app.set_tabs([cn('菜单'),cn('线程'),cn('程序')], main)
page1()
